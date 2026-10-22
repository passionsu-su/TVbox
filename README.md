# TVbox Resource Catalog

A source-first catalog for discovering and tracking public TVBox / 影视仓-related repositories.

## Principles

- **Index first:** record upstream repository URLs and metadata rather than bulk-copying third-party files.
- **Respect licenses:** only mirror files when the upstream license clearly permits redistribution; otherwise link to the original.
- **Validate before use:** inclusion does not guarantee safety, compatibility, authorization, or working media endpoints.
- **No automatic execution:** scripts, crawlers, JARs, APKs, and other binaries are not downloaded or executed by the catalog workflow.

## Structure

- `sources/repositories.json` — maintained list of upstream repositories and their purpose.
- `catalog/repositories.json` — metadata refreshed automatically from the GitHub API.
- `scripts/update_catalog.py` — metadata refresh and validation script.
- `.github/workflows/update-catalog.yml` — scheduled refresh workflow.
- `LICENSES.md` — source licensing and redistribution policy.

## Updating the source list

Edit `sources/repositories.json`. Add a GitHub owner/repository, category, purpose, and redistribution policy. Use `index-only` unless you have verified permission to redistribute the upstream content.

The workflow refreshes repository metadata daily. It does not mirror upstream files or verify media endpoints.

## Disclaimer

This project is an index and research aid. Repository metadata and content may change at any time. Review upstream terms, local law, content safety, and client compatibility before using any resource.
