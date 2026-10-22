#!/usr/bin/env python3
"""Refresh GitHub repository metadata for the curated TVbox source index.

Only public GitHub repository metadata is requested. No repository is cloned,
no upstream resource file is fetched, and no upstream code is executed.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources" / "repositories.json"
OUTPUT = ROOT / "catalog" / "repositories.json"
API_BASE = "https://api.github.com/repos/"
USER_AGENT = "TVbox-Resource-Catalog/1.0"


def github_repo(repo: str) -> dict:
    request = urllib.request.Request(
        API_BASE + repo,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": USER_AGENT,
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.load(response)


def main() -> int:
    data = json.loads(SOURCES.read_text(encoding="utf-8"))
    entries = data.get("repositories", [])
    if not isinstance(entries, list):
        raise ValueError("'repositories' must be a list")

    results = []
    failures = []
    for entry in entries:
        repo = entry.get("repo", "")
        if repo.count("/") != 1 or any(part in ("", ".", "..") for part in repo.split("/")):
            failures.append({"repo": repo, "error": "invalid owner/repository format"})
            continue
        try:
            meta = github_repo(repo)
            results.append({
                "repo": meta["full_name"],
                "source_url": meta["html_url"],
                "description": meta.get("description"),
                "default_branch": meta.get("default_branch"),
                "visibility": "private" if meta.get("private") else "public",
                "archived": meta.get("archived", False),
                "stars": meta.get("stargazers_count", 0),
                "forks": meta.get("forks_count", 0),
                "updated_at": meta.get("updated_at"),
                "pushed_at": meta.get("pushed_at"),
                "license_spdx_id": (meta.get("license") or {}).get("spdx_id"),
                "license_name": (meta.get("license") or {}).get("name"),
                "category": entry.get("category", []),
                "purpose": entry.get("purpose", ""),
                "redistribution": entry.get("redistribution", "index-only"),
                "status": "metadata-fetched",
                "note": "Metadata only; file safety, source availability, and redistribution rights are not verified.",
            })
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, KeyError, ValueError) as exc:
            failures.append({
                "repo": repo,
                "http_status": getattr(exc, "code", None),
                "error": str(exc)[:300],
            })
        time.sleep(0.25)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_count": len(entries),
        "metadata_fetched": len(results),
        "failures": failures,
        "repositories": results,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Catalog written: {len(results)}/{len(entries)} repositories fetched; {len(failures)} failures.")
    return 0 if results or not entries else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"Catalog update failed: {exc}", file=sys.stderr)
        sys.exit(1)
