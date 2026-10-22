# TVbox Resource Catalog

A source-first catalog for discovering and tracking public TVBox / 影视仓-related repositories and likely resource files.

## What is automated

- Maintains a curated list of public upstream repositories.
- Refreshes GitHub repository metadata daily.
- Discovers likely TVBox JSON, M3U/M3U8, and relevant TXT files in those repositories.
- Performs bounded, read-only format checks for candidate files.
- Generates machine-readable resource and repository catalogs.
- Runs offline parser smoke tests before each catalog refresh.

## Catalog files

- [Source repositories](sources/repositories.json) — maintained upstream list and policy.
- [Repository metadata](catalog/repositories.json) — default branch, activity, stars, license metadata where available.
- [Discovered resources](catalog/resources.json) — upstream file links, format checks, and candidate entry counts.
- [License policy](LICENSES.md) — third-party attribution and redistribution rules.

Raw catalog links:

- `https://raw.githubusercontent.com/passionsu-su/TVbox/main/catalog/repositories.json`
- `https://raw.githubusercontent.com/passionsu-su/TVbox/main/catalog/resources.json`

## How discovery works

The workflow reads public GitHub repository trees, selects likely configuration or playlist filenames, and fetches only those files from the same allowlisted GitHub repository for format checks. It records both the upstream GitHub file page and its raw URL.

It does **not** execute upstream code, download JAR/APK/binary files, follow URLs embedded in configurations, probe playback streams, or copy upstream contents into this repository. JSON structure checks are heuristic and do not guarantee client compatibility or that a source works.

## Updating sources

Edit `sources/repositories.json` to add/remove repositories. Use `redistribution: "index-only"` unless you have verified that redistribution is permitted. Adding a repository allows the workflow to inspect its public file tree and a bounded number of candidate text/config files; add only sources you intend to review.

## Automation

- Scheduled daily at 03:23 UTC.
- Runs on changes to source list, scripts, or workflow.
- Can also be started from **Actions → Update TVbox repository and resource catalogs → Run workflow**.
- The generated catalogs are committed to `main` only after the checks succeed.

## Disclaimer

This project is an index and research aid. A valid JSON/M3U format does not establish legality, security, or playback availability. Review source terms, local law, content safety, and client compatibility before use. Third-party resources remain under their own licenses and terms.
