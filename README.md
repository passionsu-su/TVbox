# TVbox Resource Catalog

A source-first catalog for discovering and tracking public TVBox / 影视仓-related repositories and likely resource files.

## 上游项目一览

以下为当前维护的 6 个上游项目。Star、Fork、默认分支等元数据来自 GitHub 仓库信息，**Star/Fork 数量为 2026-10-22 的快照，会随上游变化**。

| 项目 | Stars ⭐ | Forks | 项目主页 | 主要用途 / 特点 | 默认分支 | 主要语言 |
|---|---:|---:|---|---|---|---|
| [qist/tvbox](https://github.com/qist/tvbox) | 12,184 | 4,291 | [GitHub](https://github.com/qist/tvbox) | TVBox / OK影视配置及资源集合 | `master` | JavaScript |
| [tushen6/Tomorrow](https://github.com/tushen6/Tomorrow) | 2,308 | 348 | [GitHub](https://github.com/tushen6/Tomorrow) | TVBox / 影视仓配置、JSON 与直播列表等资源 | `master` | HTML |
| [Lightconer/tvbox-ysc-config](https://github.com/Lightconer/tvbox-ysc-config) | 185 | 48 | [GitHub](https://github.com/Lightconer/tvbox-ysc-config) | 影视仓 / TVBox 多源聚合，使用 GitHub Actions 定时更新 | `main` | Python |
| [riowang88/tvbox-source-aggregator](https://github.com/riowang88/tvbox-source-aggregator) | 184 | 441 | [GitHub](https://github.com/riowang88/tvbox-source-aggregator) | TVBox 资源聚合工具与自动化项目 | `main` | TypeScript |
| [TVboxorg/TVbox](https://github.com/TVboxorg/TVbox) | 8 | 0 | [GitHub](https://github.com/TVboxorg/TVbox) · [官网](https://www.tvbox.org/) | 接口汇总、可用性探测及生成清单 | `main` | Python |
| [JianghaoPi/my-tvbox-sources](https://github.com/JianghaoPi/my-tvbox-sources) | 0 | 0 | [GitHub](https://github.com/JianghaoPi/my-tvbox-sources) | 自动聚合配置、冗余回退与缓存兜底 | `main` | Python |

> 说明：此表是上游项目导航，不代表对其全部配置、接口或脚本进行安全审计，也不保证资源可用。使用前请阅读各项目 README、许可条款和风险提示。Stars/Forks 仅反映 GitHub 互动数据，不代表资源质量或播放成功率。

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
