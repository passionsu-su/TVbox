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
TEXT_NAMES = ("tvbox", "live", "iptv", "m3u", "source", "直播", "频道")
EXCLUDED_NAMES = {
    "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
    "tsconfig.json", "manifest.json", "shield.json", "status.json",
    "status_history.json", "live_status.json", "live_status_history.json",
    "live_shield.json", "update_shield.json", "merge-meta.json", "probe.json",
}


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
    if name in EXCLUDED_NAMES or name.startswith("."):
        return None
    if lower.startswith((".github/", ".claude/", "node_modules/")):
        return None
    if name.endswith(".json"):
        return "json"
    if name.endswith((".m3u", ".m3u8")):
        return "m3u"
    if name.endswith(".txt") and any(k in name for k in TEXT_NAMES):
        return "txt"
    return None


def candidate_priority(path: str) -> tuple[int, str]:
    """Rank likely client-ready resources before metadata and helper configs."""
    lower = path.lower()
    name = lower.rsplit("/", 1)[-1]
    score = 0
    exact_names = {
        "tvbox.json", "lmw.json", "official.json", "aggregate.json",
        "subscribe.json", "js.json", "jsm.json", "xc.json", "xyq.json",
        "xbpq.json", "cat.json", "live.json", "live.txt", "live.m3u",
        "0821.json", "0822.json", "0825.json", "0826.json", "0827.json", "0828.json",
    }
    if name in exact_names:
        score += 100
    if any(token in name for token in ("tvbox", "official", "aggregate", "subscribe", "lmw", "jsm", "xbpq", "xyq")):
        score += 50
    if lower.startswith(("output/", "dist/")):
        score += 30
    if "/" not in path:
        score += 20
    if name.endswith((".m3u", ".m3u8", ".txt")):
        score += 15
    if any(token in name for token in ("source", "live", "iptv", "config", "直播", "频道")):
        score += 10
    if name.startswith(tuple("0123456789")) and name.endswith(".json"):
        score += 8
    return (-score, lower)


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
            lists = [obj.get(field) for field in ("sites", "lives", "urls", "parses")]
            if any(isinstance(value, list) for value in lists):
                count = sum(len(value) for value in lists if isinstance(value, list))
                return "tvbox-config", "JSON parsed; TVBox-like sites/lives/urls/parses field found", count
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
            candidates.sort(key=lambda x: candidate_priority(x[0]))
            for path, kind, size in candidates[:MAX_FILES_PER_REPO]:
                raw_branch = urllib.parse.quote(branch, safe="/")
                raw_url = "https://raw.githubusercontent.com/" + repo + "/" + raw_branch + "/" + urllib.parse.quote(path, safe="/")
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
        "validation_summary": {},
        "failures": failures,
        "resources": discovered,
        "notice": "Index only. No third-party file is mirrored or executed. A successful format check does not establish safety, legality, or playback availability.",
    }
    for item in discovered:
        status = item.get("validation", "unknown")
        payload["validation_summary"][status] = payload["validation_summary"].get(status, 0) + 1
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Resource catalog written: {len(discovered)} files from {len(repos)} source repositories; {len(failures)} repository failures.")
    return 0 if discovered or not repos else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"Resource discovery failed: {exc}", file=sys.stderr)
        sys.exit(1)
