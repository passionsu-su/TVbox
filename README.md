# TVBox / 影视仓资源导航

这是一个**手动维护的导航页**：整理 TVBox / 影视仓相关项目、接口目录和客户端。仓库保持 Private，不自动抓取、合并或分发第三方资源。

## 上游项目一览

Stars / Forks 为 **2026-10-22 的 GitHub 快照**，会变化。按 Stars 大致从高到低排列；“配置/资源”指配置、接口或资源合集，“客户端”指 App 项目，两者不要混淆。

| 项目 | 类型 | Stars ⭐ | Forks | 项目主页 | 主要用途 / 说明 |
|---|---|---:|---:|---|---|
| [qist/tvbox](https://github.com/qist/tvbox) | 配置/资源 | 12,184 | 4,291 | [GitHub](https://github.com/qist/tvbox) | TVBox / OK影视配置与资源集合；使用前阅读项目说明 |
| [FongMi/TV](https://github.com/FongMi/TV) | 客户端 | 10,006 | 2,956 | [GitHub](https://github.com/FongMi/TV) | FongMi 系列 Android TV 客户端项目 |
| [takagen99/Box](https://github.com/takagen99/Box) | 客户端 | 3,074 | 1,683 | [GitHub](https://github.com/takagen99/Box) | TVBoxOS 衍生客户端 |
| [q215613905/TVBoxOS](https://github.com/q215613905/TVBoxOS) | 客户端 | 2,968 | 2,382 | [GitHub](https://github.com/q215613905/TVBoxOS) | TVBoxOS 客户端源码 |
| [tushen6/Tomorrow](https://github.com/tushen6/Tomorrow) | 配置/资源 | 2,308 | 348 | [GitHub](https://github.com/tushen6/Tomorrow) | 配置文件、JSON、直播列表等资源 |
| [scovis/TVBox](https://github.com/scovis/TVBox) | 配置/资源 | 1,721 | 613 | [GitHub](https://github.com/scovis/TVBox) | TVBox 配置、解析源和直播资源导航 |
| [XiaoRanLiu3119/TVBoxOS-Mobile](https://github.com/XiaoRanLiu3119/TVBoxOS-Mobile) | 客户端 | 1,554 | 325 | [GitHub](https://github.com/XiaoRanLiu3119/TVBoxOS-Mobile) | TVBox 手机端项目 |
| [wuxierj/TVBox](https://github.com/wuxierj/TVBox) | 配置/资源 | 325 | 41 | [GitHub](https://github.com/wuxierj/TVBox) | TVBox、影视仓接口合集，包含单接口和多仓入口 |
| [Lightconer/tvbox-ysc-config](https://github.com/Lightconer/tvbox-ysc-config) | 配置聚合 | 185 | 48 | [GitHub](https://github.com/Lightconer/tvbox-ysc-config) | 多源配置聚合示例；上游项目本身使用自动更新 |
| [riowang88/tvbox-source-aggregator](https://github.com/riowang88/tvbox-source-aggregator) | 聚合工具 | 184 | 441 | [GitHub](https://github.com/riowang88/tvbox-source-aggregator) | TVBox 资源聚合工具与项目示例 |
| [TVboxorg/TVbox](https://github.com/TVboxorg/TVbox) | 接口目录 | 8 | 0 | [GitHub](https://github.com/TVboxorg/TVbox) · [官网](https://www.tvbox.org/) | 接口清单、格式/可用性探测；提供聚合配置文件 |
| [JianghaoPi/my-tvbox-sources](https://github.com/JianghaoPi/my-tvbox-sources) | 配置聚合 | 0 | 0 | [GitHub](https://github.com/JianghaoPi/my-tvbox-sources) | 聚合配置与直播资源的参考项目 |

> 表格是项目导航，不代表安全审计、版权授权或播放可用性保证。客户端与配置资源是不同类别；Stars 高也不等于接口稳定、内容合法或没有风险。第三方仓库可能没有明确许可证，引用或转载前请检查各自 README、许可证和使用条款。

<!-- TVBOX-CATALOG:START -->
## 每周自动发现与检测结果

工作流每周二 03:17 UTC 自动运行，也可以在 GitHub Actions 页面手动触发。首次工作流运行前尚无自动检测报告。

- 自动搜索 GitHub 公开 TVBox 相关仓库，发现候选 JSON 并去重。
- 检查 JSON 结构，并对部分配置中的第一个 HTTP API 进行受限可访问性检测。
- **格式正确、HTTP 响应均不代表内容获授权或可以播放。** 未经人工核实授权的条目仅作诊断候选。
- 不下载或执行第三方 Spider、JAR、脚本或 APK。
- 只有在 `sources/authorized-playback-tests.json` 中明确填写授权依据和直接媒体测试 URL，才会运行 ffprobe 媒体流探测；这仍不等于 TVBox 客户端实际播放。
- 机器可读结果会写入 [sources/catalog.json](sources/catalog.json)。只有 README 或报告变化时才提交。

当前尚未完成首次自动检测；不会将未经真实客户端验证的资源标记为“已播放成功”。

<!-- TVBOX-CATALOG:END -->

## TVBox / 影视仓配置方法（新手版）

不同客户端版本的菜单名称可能略有区别，通常按以下步骤操作：

1. **先安装客户端**：从对应客户端项目的官方 GitHub Releases 或作者认可的渠道获取。不要安装来路不明的 APK。
2. **复制一个配置地址**：优先使用下面的示例之一。地址要完整复制，不要把 Markdown 链接文字一起复制。
3. **打开客户端的设置**：找到“配置地址”“接口地址”“订阅配置”或类似入口。
4. **粘贴并确认**：保存后返回首页，等待站点/分类加载；部分版本需要重新载入或重启应用。
5. **如果失败**：检查地址是否完整、网络能否访问该域名、客户端是否支持该配置格式；再尝试同一项目 README 中提供的备用地址。接口失效时换一个来源，不要安装陌生插件或 JAR 来“修复”。

### 可用于尝试的配置地址

| 用途 | 配置地址 | 怎么填 |
|---|---|---|
| **单仓聚合配置（适合先试）** | `https://raw.githubusercontent.com/TVboxorg/TVbox/main/dist/official.json` | 粘贴到“配置地址 / 接口地址” |
| **单仓聚合备用（jsDelivr）** | `https://cdn.jsdelivr.net/gh/TVboxorg/TVbox@main/dist/official.json` | 上一个地址访问慢或失败时再试 |
| **多仓入口（需要客户端支持多仓）** | `https://raw.githubusercontent.com/wxrjck/-YSC-/refs/heads/main/wx.json` | 仅填入支持“多仓 / 仓库列表”的入口；若网络无法访问 GitHub，可查看 [wuxierj/TVBox](https://github.com/wuxierj/TVBox) README 中的当前地址 |
| **qist 配置示例** | `https://raw.githubusercontent.com/qist/tvbox/master/jsm.json` | 粘贴到“配置地址 / 接口地址” |

**建议第一次只添加一个配置地址。** 不要把“多仓列表”误填进只接受单个配置 JSON 的输入框。各客户端对“多仓”“单仓”和配置格式的支持不完全相同；如果某个入口不兼容，回到对应上游 README 查看说明。

### 常见问题

- **首页空白或一直转圈**：配置地址可能失效、网络无法访问，或源返回格式与客户端不兼容。
- **能打开配置但没有内容**：配置可读取不代表其站点可用；尝试更新客户端、换一个来源或稍后再试。
- **播放失败**：可能是上游接口、解析服务、网络、地区限制或内容源本身的问题，本导航无法保证播放成功。
- **地址需要代理吗？** 只有在当前网络无法直连时才考虑可靠的网络访问方式。不要随意使用未知第三方代理输入账号、令牌或其他敏感信息。

## 本仓库怎么维护

本仓库每周通过 GitHub Actions 搜集和验证公开候选配置，详见上方自动检测报告。工作流仅检查 JSON 和受限的 API 响应，不执行第三方代码；授权和实际播放状态必须谨慎标注。

## 安全与使用提醒

- 仅使用你有权访问的内容，并遵守当地法律法规、平台规则及上游项目的许可条款。
- 配置文件可能包含第三方接口、解析服务、脚本或外部依赖。不要因为它能导入就认定安全；不明来源的配置可能导致隐私、网络访问或设备安全风险。
- 本仓库只提供导航和一般配置说明，不托管影视内容，不保证第三方资源的安全、合法性、持续可用性或播放质量。
