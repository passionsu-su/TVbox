#!/usr/bin/env python3
"""Discover likely TVBox/playlist files in curated public GitHub repositories.

The scanner indexes upstream URLs only. It never executes downloaded code,
downloads binaries, follows arbitrary URLs embedded in configs, or mirrors files.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources" / "repositories.json"
OUTPUT = ROOT / "catalog" / "resources.json"
API = "https://api.github.com"
USER_AGENT = "TVbox-Resource-Catalog/1.0"
MAX_BYTES = 1_500_000
MAX_FILES_PER_REPO = 30
TIMEOUT = 12
JSON_NAMES = ("tvbox", "tv", "config", "source", "live", "iptv", "m3u", "json", "lmw", "jsm", "xc", "cat", "xyq", "xbpq", "vod", "多仓", "直播")
TEXT_NAMES = ("tvbox", "live", "iptv", "m3u", "source", "直播", "频道")


def request_bytes(url: str, limit: int = MAX_BYTES) -> bytes:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API + "/"):
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError(f"response exceeds {limit} bytes")
    return data


def request_json(url: str) -> dict:
    return json.loads(request_bytes(url).decode("utf-8"))


def classify(path: str) -> str | None:
    lower = path.lower()
    name = lower.rsplit("/", 1)[-1]
    if name.endswith(".json") and any(k in name for k in JSON_NAMES):
        return "json"
    if name.endswith(".m3u") or name.endswith(".m3u8"):
        return "m3u"
    if name.endswith(".txt") and any(k in name for k in TEXT_NAMES):
        return "txt"
    return None


def validate_content(kind: str, content: bytes) -> tuple[str, str, int]:
    text = content.decode("utf-8-sig", errors="replace")
    stripped = text.strip()
    if not stripped:
        return "empty", "File is empty", 0
    if kind == "json":
        try:
            obj = json.loads(text)
        except json.JSONDecodeError as exc:
            return "invalid-json", f"JSON parse error at line {exc.lineno}, column {exc.colno}", 0
        if isinstance(obj, dict):
            sites = obj.get("sites")
            lives = obj.get("lives")
            urls = obj.get("urls")
            if isinstance(sites, list) or isinstance(lives, list) or isinstance(urls, list):
                return "tvbox-config", "JSON parsed; TVBox-like sites/lives/urls field found", len(sites or []) + len(lives or []) + len(urls or [])
        return "valid-json-other", "JSON parsed but expected TVBox fields were not found", 0
    if kind == "m3u":
        if stripped.startswith("#EXTM3U"):
            return "valid-m3u", "M3U header found", sum(1 for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#"))
        return "invalid-m3u", "Missing #EXTM3U header", 0
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if any(line.startswith(("http://", "https://")) for line in lines):
        return "txt-with-urls", "Text contains HTTP(S) URL lines; format may require manual review", len(lines)
    return "text-review", "Text file indexed; format requires manual review", len(lines)


def main() -> int:
    source_data = json.loads(SOURCES.read_text(encoding="utf-8"))
    repos = source_data.get("repositories", [])
    if not isinstance(repos, list):
        raise ValueError("'repositories' must be a list")

    discovered = []
    failures = []
    for source in repos:
        repo = source.get("repo", "")
        if repo.count("/") != 1 or any(part in ("", ".", "..") for part in repo.split("/")):
            failures.append({"repo": repo, "error": "invalid owner/repository format"})
            continue
        try:
            meta = request_json(f"{API}/repos/{repo}")
            branch = meta.get("default_branch")
            if not branch:
                failures.append({"repo": repo, "error": "default branch unavailable"})
                continue
            encoded_branch = urllib.parse.quote(branch, safe="")
            tree = request_json(f"{API}/repos/{repo}/git/trees/{encoded_branch}?recursive=1")
            if tree.get("truncated"):
                failures.append({"repo": repo, "warning": "Git tree was truncated; some files may be omitted"})
            candidates = []
            for item in tree.get("tree", []):
                if item.get("type") != "blob":
                    continue
                path = item.get("path", "")
                kind = classify(path)
                if not kind or int(item.get("size", 0)) > MAX_BYTES:
                    continue
                candidates.append((path, kind, int(item.get("size", 0))))
            candidates.sort(key=lambda x: (0 if any(k in x[0].lower() for k in ("output/", "dist/", "config/")) else 1, x[0].lower()))
            for path, kind, size in candidates[:MAX_FILES_PER_REPO]:
                raw_url = "https://raw.githubusercontent.com/" + repo + "/" + encoded_branch + "/" + urllib.parse.quote(path, safe="/")
                row = {
                    "repo": meta.get("full_name", repo),
                    "path": path,
                    "kind": kind,
                    "source_url": f"https://github.com/{repo}/blob/{encoded_branch}/{urllib.parse.quote(path, safe='/')}",
                    "raw_url": raw_url,
                    "redistribution": "index-only",
                    "declared_size_bytes": size,
                }
                try:
                    content = request_bytes(raw_url)
                    status, note, entries = validate_content(kind, content)
                    row.update({"validation": status, "validation_note": note, "entry_count": entries, "checked_bytes": len(content)})
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as exc:
                    row.update({"validation": "fetch-failed", "validation_note": str(exc)[:240], "entry_count": 0})
                discovered.append(row)
                time.sleep(0.12)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, KeyError, ValueError) as exc:
            failures.append({"repo": repo, "error": str(exc)[:300]})

    # Stable output ordering makes reviews and diffs easier.
    discovered.sort(key=lambda x: (x["repo"].lower(), x["kind"], x["path"].lower()))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_repositories": len(repos),
        "resource_count": len(discovered),
        "validated_count": sum(1 for item in discovered if item.get("validation", "").startswith(("tvbox-", "valid-")) or item.get("validation") == "txt-with-urls"),
        "failures": failures,
        "resources": discovered,
        "notice": "Index only. No third-party file is mirrored or executed. A successful format check does not establish safety, legality, or playback availability.",
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Resource catalog written: {len(discovered)} files from {len(repos)} source repositories; {len(failures)} repository failures.")
    return 0 if discovered or not repos else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"Resource discovery failed: {exc}", file=sys.stderr)
        sys.exit(1)
