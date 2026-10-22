# TVBox / 影视仓资源导航

这是一个 TVBox / 影视仓项目导航与检测仓库。GitHub Actions 每周搜集公开候选配置、验证 JSON 和部分 API，并生成检测报告；不会自动合并或执行第三方代码。

## 一键复制配置网页

- GitHub Pages：https://passionsu-su.github.io/TVbox/
- Hark 页面：https://hark.site/s/a3810ce6-dd21-4852-8698-fa455abb6a8a?hark_region=us

每个配置地址都有「复制」和「国内加速」（jsDelivr）按钮。

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

> 最近检测：**2026-10-22 07:32 UTC**。候选来自 GitHub 公开项目；结果不是安全审计、版权授权或客户端实播成功证明。仓库许可证不能证明配置指向的站点/媒体内容已获授权。

- 候选 JSON：**59**
- 只读取 JSON，不下载或执行第三方 Spider/JAR/脚本。
- 格式通过不代表接口可用；接口可访问不代表可播放。授权未核实的条目仅作诊断候选。

| 配置 JSON | 来源仓库 | Stars | 许可证 | JSON 检测 | API 检测 | 播放状态 | 授权说明 | 检测时间 / 备注 |
|---|---|---:|---|---|---|---|---|---|
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/%E5%A4%A9%E5%BE%AE/api.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式通过 | 接口可访问 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,rules,sites,spider; first API: HTTP 200; text/html;charset=utf-8; 7026 bytes (not playback proof) |
| [配置](https://raw.githubusercontent.com/songlees355-wq/okay/main/tvbox.json) | [songlees355-wq/okay](https://github.com/songlees355-wq/okay) | 22 | NOASSERTION | 格式通过 | 接口可访问 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys lives,parses,sites,spider; first API: HTTP 200; text/html;charset=utf-8; 5248 bytes (not playback proof) |
| [配置](https://raw.githubusercontent.com/chitue/dongliTV/main/api.json) | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | 25707 | Apache-2.0 | 格式通过 | 接口检测失败 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,rules,sites,spider; first API: 'ascii' codec can't encode characters in position 8-11: ordinal not in range(128) |
| [配置](https://raw.githubusercontent.com/qist/tvbox/master/fty.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys lives,rules,sites,spider |
| [配置](https://raw.githubusercontent.com/qist/tvbox/master/jsm.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,rules,sites,spider |
| [配置](https://raw.githubusercontent.com/qist/tvbox/master/xiaosa/api.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,rules,sites,spider |
| [配置](https://raw.githubusercontent.com/UndCover/PyramidStore/main/py.json) | [dongyubin/IPTV](https://github.com/dongyubin/IPTV) | 4562 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,sites,spider |
| [配置](https://raw.githubusercontent.com/xianyuyimu/TVBOX-/main/TVBox/%E4%B8%80%E6%9C%A8%E8%87%AA%E7%94%A8.json) | [xianyuyimu/TVBOX-](https://github.com/xianyuyimu/TVBOX-) | 3118 | NOASSERTION | 格式通过 | 接口检测失败 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,sites,spider; first API: [Errno -2] Name or service not known |
| [配置](https://raw.githubusercontent.com/xianyuyimu/TVBOX-/main/TVBox/%E5%A4%87%E7%94%A8.json) | [xianyuyimu/TVBOX-](https://github.com/xianyuyimu/TVBOX-) | 3118 | NOASSERTION | 格式通过 | 接口检测失败 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,sites,spider; first API: [Errno -2] Name or service not known |
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/%E5%8A%A8%E6%BC%AB%E9%A2%91%E9%81%93/api.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys parses,sites,spider |
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/%E5%8D%97%E9%A3%8E/api.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,rules,sites,spider |
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/%E5%A4%A9%E5%A4%A9%E5%BC%80%E5%BF%83/api.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,rules,sites,spider |
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/OK/api.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys ads,lives,parses,rules,sites,spider |
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/PG/api.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式通过 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys lives,parses,rules,sites,spider |
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/iptv365/api.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式通过 | 接口检测失败 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys lives,sites,spider; first API: [Errno -2] Name or service not known |
| [配置](https://raw.githubusercontent.com/mrgaoshuiquan/tvbox-config/main/tvbox.json) | [mrgaoshuiquan/tvbox-config](https://github.com/mrgaoshuiquan/tvbox-config) | 128 | MIT | 格式通过 | 未检测 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; valid JSON; keys lives,sites,spider |
| [配置](https://raw.githubusercontent.com/guot55/YGBH/main/vip2.json) | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | 25707 | Apache-2.0 | 格式失败 | 未检测 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting value: line 134 column 14 (char 3070) |
| [配置](https://raw.githubusercontent.com/maoystv/6/main/000.json) | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | 25707 | Apache-2.0 | 格式失败 | 未检测 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting property name enclosed in double quotes: line 2 column 1 (char 2) |
| [配置](https://raw.githubusercontent.com/xyq254245/xyqonlinerule/main/XYQTVBox.json) | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | 25707 | Apache-2.0 | 格式失败 | 未检测 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting value: line 39 column 9 (char 1984) |
| [配置](https://raw.githubusercontent.com/yoursmile66/TVBox/main/XC.json) | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | 25707 | Apache-2.0 | 格式失败 | 未检测 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Extra data: line 1 column 15 (char 14) |
| [配置](https://raw.githubusercontent.com/laoma528/awesome-zhuiju-free/main/resources/resources.json) | [laoma528/awesome-zhuiju-free](https://github.com/laoma528/awesome-zhuiju-free) | 12986 | CC-BY-4.0 | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/laoma528/awesome-zhuiju-free/main/resources/schema.json) | [laoma528/awesome-zhuiju-free](https://github.com/laoma528/awesome-zhuiju-free) | 12986 | CC-BY-4.0 | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/lm317379829/PyramidStore/pyramid/py.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 检测失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP Error 404: Not Found |
| [配置](https://raw.githubusercontent.com/qist/tvbox/master/cat/js/config_open.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/qist/tvbox/master/cat/js/config_open99.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/qist/tvbox/master/cat/js/config_open99_online.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/qist/tvbox/master/cat/js/config_open_online.json) | [qist/tvbox](https://github.com/qist/tvbox) | 12185 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/139%E5%BD%B1%E8%A7%86.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/300%E5%BD%B1%E8%A7%86.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting property name enclosed in double quotes: line 4 column 3 (char 45) |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/31%E7%9C%8B%E5%BD%B1%E8%A7%86.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/348%E7%94%B5%E5%BD%B1%E7%BD%91.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/4Kkan.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting property name enclosed in double quotes: line 4 column 35 (char 79) |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/555%E7%94%B5%E5%BD%B1.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting value: line 1 column 1 (char 0) |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/789%E5%BD%B1%E8%A7%86.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/liu673cn/bug/main/sub/MeowXB/AB%E5%BD%B1%E9%99%A2.json) | [liu673cn/bug](https://github.com/liu673cn/bug) | 10322 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting property name enclosed in double quotes: line 3 column 3 (char 24) |
| [配置](https://raw.githubusercontent.com/gaotianliuyun/gao/master/cat/js/config_open.json) | [gaotianliuyun/gao](https://github.com/gaotianliuyun/gao) | 7991 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/gaotianliuyun/gao/master/lib/singbox.json) | [gaotianliuyun/gao](https://github.com/gaotianliuyun/gao) | 7991 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/YuanHsing/freed/master/TVBox/meow.json) | [dongyubin/IPTV](https://github.com/dongyubin/IPTV) | 4562 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting value: line 1 column 1 (char 0) |
| [配置](https://raw.githubusercontent.com/noimank/tvbox/main/tvboxmuti.json) | [noimank/tvbox](https://github.com/noimank/tvbox) | 3559 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/config/alist-host.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/config/alist-mysql.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/config/alist.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/src/main/resources/META-INF/native-image/proxy-config.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; top-level must be object |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/src/main/resources/META-INF/native-image/reflect-config.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; top-level must be object |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/src/main/resources/META-INF/native-image/resource-config.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/src/main/resources/channels.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; top-level must be object |
| [配置](https://raw.githubusercontent.com/power721/alist-tvbox/master/src/main/resources/countries.json) | [power721/alist-tvbox](https://github.com/power721/alist-tvbox) | 3151 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/xianyuyimu/TVBOX-/main/TVBox/%E4%B8%80%E6%9C%A8%E5%A4%9A%E7%BA%BF%E8%B7%AF.json) | [xianyuyimu/TVBOX-](https://github.com/xianyuyimu/TVBOX-) | 3118 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/xianyuyimu/TVBOX-/main/TVBox/%E4%B8%80%E6%9C%A8cs.json) | [xianyuyimu/TVBOX-](https://github.com/xianyuyimu/TVBOX-) | 3118 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting value: line 1 column 1 (char 0) |
| [配置](https://raw.githubusercontent.com/xianyuyimu/TVBOX-/main/TVBox/%E5%A4%9A%E4%BB%93.json) | [xianyuyimu/TVBOX-](https://github.com/xianyuyimu/TVBOX-) | 3118 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting value: line 1 column 1 (char 0) |
| [配置](https://raw.githubusercontent.com/kknifer7/FreeBox/main/upgrade-config.json) | [kknifer7/FreeBox](https://github.com/kknifer7/FreeBox) | 2060 | GPL-3.0 | 格式失败 | 未检测 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/jinenge/tvbox/main/tvbox.json) | [jinenge/tvbox](https://github.com/jinenge/tvbox) | 1175 | MPL-2.0 | 格式失败 | 未检测 | 未实播验证 | 仓库声明开放许可证；配置和媒体授权仍需人工核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting value: line 1 column 1 (char 0) |
| [配置](https://raw.githubusercontent.com/kimwang1978/tvbox/main/PG/lib/singbox.json) | [kimwang1978/tvbox](https://github.com/kimwang1978/tvbox) | 388 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/fish2018/tvbox/master/all.json) | [fish2018/tvbox](https://github.com/fish2018/tvbox) | 322 | NOASSERTION | 检测失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP Error 404: Not Found |
| [配置](https://raw.githubusercontent.com/hackyjso/TVbox/main/js/config_open.json) | [hackyjso/TVbox](https://github.com/hackyjso/TVbox) | 190 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/hackyjso/TVbox/main/js/config_open99.json) | [hackyjso/TVbox](https://github.com/hackyjso/TVbox) | 190 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; JSON parse error: Expecting ',' delimiter: line 34 column 134 (char 2773) |
| [配置](https://raw.githubusercontent.com/Lightconer/tvbox-ysc-config/main/config/sources.json) | [Lightconer/tvbox-ysc-config](https://github.com/Lightconer/tvbox-ysc-config) | 186 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/fishforks/ol/main/tvbox.json) | [fishforks/ol](https://github.com/fishforks/ol) | 35 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |
| [配置](https://raw.githubusercontent.com/wzh15802/tvbox/main/tvboxadmin/pause.json) | [wzh15802/tvbox](https://github.com/wzh15802/tvbox) | 27 | NOASSERTION | 格式失败 | 未检测 | 未实播验证 | 许可证/授权待核实 | 2026-10-22 07:32 UTC；HTTP 200; no known TVBox config keys |

### 经授权测试源的媒体流探测

只有在 sources/authorized-playback-tests.json 中填写授权依据和直接媒体 URL 的条目才会执行 ffprobe，并尝试用 FFmpeg 解码最多 5 秒媒体样本；这仍不等于 TVBox 客户端实播。

当前未配置经授权的媒体测试源；本次没有任何资源被标记为已实播成功。

机器可读报告：[sources/catalog.json](sources/catalog.json)。

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

