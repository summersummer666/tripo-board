from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
CHECKED = "2026-09-26 20:07（北京时间）"

report = '''<div class="latest-summary merged-report"><h2 id="weekly-report">本期周报 · 素材与热点追踪</h2>
<span class="status">2026-09-26 · 部分更新（Foreplay 未刷新）</span>
<p>本周窗口：9/21–9/26；遗漏期：9/19–9/20。原计划于周五 9/25 17:00 执行，本次实际在 9/26 完成。官方内容监测与健康检查已更新；Chrome 的 Foreplay 浏览器桥接连续失败，无法重新核实 Tripo 与五个品牌的广告详情，因此广告数据、横向参考和打印机 Top 5 均保留 9/18 的真实采集时间与排名，不改时间戳。</p>
<nav class="report-nav"><a href="#health">看板健康</a><a href="#hotspots">热点追踪</a><a href="#news">竞品动态</a><a href="#missing">未找到清单</a><a href="#audit">核查台账</a><a href="#view-ref">横向 Top 5（9/18）</a><a href="#view-printer">打印机 Top 5（9/18）</a><a href="index-2026-09-26-partial.html#weekly-report">9/26 日期归档</a><a href="index-2026-09-18-before-refresh.html">9/18 更新前归档</a></nav>
<section id="health"><h2>看板健康检查</h2><div class="callout"><b>判定：内容部分更新，广告数据已停留 8 天。</b><p>本地页面与线上发布源显示广告数据采集时间仍为“2026-09-18 17:13（北京时间）”。本期没有把周报撰写时间伪装成广告采集时间。Foreplay 读取失败的直接证据是 Chrome 浏览器控制连续 3 次无法加载请求策略，随后原生 Chrome 连接也超时；这只能说明本次采集通道不可用，不能据此断言设备、登录或 Foreplay 本身故障。</p><p><b>排查顺序：</b>①确认 Mac 与 Chrome 正常运行；②确认 Chrome 仍登录 Foreplay；③重新连接浏览器扩展后重跑；④检查未推送提交：<code>git log --oneline origin/main..HEAD</code>。本地仓库本次开始时无未提交文件。</p></div></section>
<section id="hotspots"><h2>值得我们跟进的热点</h2><p>以下“已核实信号”来自本次打开的官方页面或公开报道；建议均未执行。上期广告热点因 Foreplay 未连接，状态统一改为待复查。</p><div class="hot-grid">
<article class="hot-card"><span class="status">新增 · 优先验证</span><h3>把 UV 与去光照做成可检查的专业流程</h3><p><b>已核实信号：</b>Tripo 9/21 发布 Smart UV，9/24 发布 Remove Lighting 开关；前者同时展示 2D UV 图与 3D 模型，后者区分可重新打光的基础色与保留原始风格。</p><p><b>为什么值得跟：</b>竞争叙事从“生成得像”延伸到进入游戏、重打光与打印之前的资产准备。</p><p><b>建议动作：</b>用同一模型演示 UV 检查、纹理去光照和引擎重打光，公开输入、设置与导出文件。</p><p><b>复查指标：</b>工作流完成时间、UV 利用率、动态光照下的阴影冲突、打印颜色偏差。</p><footer>下次复查：2026-10-02 · <a href="https://www.tripo3d.ai/blog/smart-uv">Smart UV ↗</a> · <a href="https://www.tripo3d.ai/blog/tripo-texture-remove-lighting">Remove Lighting ↗</a></footer></article>
<article class="hot-card"><span class="status">新增 · 优先验证</span><h3>公开网格诊断，回应“只看渲染图不够”</h3><p><b>已核实信号：</b>9/22 的日语 VFX DESK 报道总结了一支同输入横评视频，使用 Meshwright 检查面数、孔洞、非流形边和浮游几何；报道也明确写出作者未自行生成模型。</p><p><b>为什么值得跟：</b>用户开始用可检查的网格指标讨论生产可用性，而不只比较渲染观感。</p><p><b>建议动作：</b>挑选三类输入，公开生成文件与诊断截图；把视觉质量、网格完整性和修复时间分开报告。</p><p><b>复查指标：</b>孔洞、非流形边、浮游几何、修复耗时及导入 DCC/切片器成功率。</p><footer>下次复查：2026-10-02 · <a href="https://vfx-desk.com/articles/yt-2xyp-fmku-u">VFX DESK ↗</a></footer></article>
<article class="hot-card"><span class="status">继续跟进</span><h3>教程从单功能转向完整交付链路</h3><p><b>已核实信号：</b>Tripo 9/21–9/24 连续发布草图到 UE5、GPT/Astra 到 Blender、单图到中秋 3D 资产、资产生成与场景搭建对比等工作流文章。</p><p><b>为什么值得跟：</b>内容把产品能力绑定到可复现任务，容易承接搜索与专业用户需求。</p><p><b>建议动作：</b>为 Meshy 做一条“参考图—生成—修复—引擎/打印”的可下载教程，并保留失败步骤。</p><p><b>复查指标：</b>教程完成率、示例文件下载、后续搜索词与用户复现反馈。</p><footer>下次复查：2026-10-02 · <a href="https://www.tripo3d.ai/blog">Tripo 官方博客 ↗</a></footer></article>
<article class="hot-card"><span class="status">待复查 · 数据未刷新</span><h3>上期 Foreplay 广告热点</h3><p><b>上期信号：</b>可组合角色、Suno Studio 2.0、ElevenLabs 生产级基础设施、Bambu 真实任务与 Creality 众筹预热均来自 9/18 Foreplay 采集。</p><p><b>本期处理：</b>未获得新详情，不延续“仍在投”判断，也不更新变体数；待浏览器桥接恢复后按 9/20–9/26 起投窗口重排。</p><p><b>复查指标：</b>真实起投日、当前状态、Creative Duplicates、媒体去重及广告 ID。</p><footer>下次复查：浏览器恢复后立即补采 · <a href="foreplay-top5-2026-09-18.json">9/18 台账 ↗</a></footer></article>
</div></section>
<section id="news"><h2>竞品动态</h2>
<div class="insight"><b>9/24 · Tripo：Texture 增加 Remove Lighting 开关。</b><p>官方正文说明可选择去除参考图环境光，获得适合重新打光的基础色，也可保留原始光照与风格；并列出游戏引擎、多色打印和 PBR 资产库场景。</p><blockquote>“choose whether to remove or preserve the original lighting”</blockquote><p><a href="https://www.tripo3d.ai/blog/tripo-texture-remove-lighting">官方正文</a>；日期来自同日打开的<a href="https://www.tripo3d.ai/blog">官方列表：“2026/09/24”</a>。</p></div>
<div class="insight"><b>9/21 · Tripo：发布 Smart UV。</b><p>官方正文称工具会自动放置接缝、生成并打包 UV 岛，同时显示 UV 利用率与双向高亮；当前正文列出的上限为 80,000 个三角面或 40,000 个四边面。</p><blockquote>“places UV seams, separates the surface into UV islands”</blockquote><p><a href="https://www.tripo3d.ai/blog/smart-uv">官方正文</a>；日期来自<a href="https://www.tripo3d.ai/blog">官方列表：“2026/09/21”</a>。</p></div>
<div class="insight"><b>9/22 · 日本垂直媒体：同输入比较开始加入网格诊断。</b><p>VFX DESK 复述了 9/21 发布的对比视频，并明确披露其没有自行注册服务或生成模型。该报道可作为舆情信号，不作为独立跑分。</p><blockquote>“面数・開いた穴・非多様体エッジ・浮遊ジオメトリを数えていく”</blockquote><p><a href="https://vfx-desk.com/articles/yt-2xyp-fmku-u">VFX DESK 原文</a>，页面日期：“2026.09.22”。</p></div>
<h3>遗漏期 9/19–9/20</h3><div class="insight"><b>9/19 · Tripo：GPT-6 Astra + Tripo CLI + Unreal MCP 城市场景工作流。</b><p>官方列表描述从 AI 3D 资产到关卡布局的完整流程。该条早于本周窗口，因 9/18 后未更新而单列。</p><blockquote>“from AI 3D assets to level layout”</blockquote><p><a href="https://www.tripo3d.ai/blog">Tripo 官方博客列表</a>，列表日期：“2026/09/19”。</p></div>
</section>
<section id="missing"><h2>未找到清单</h2><ul><li><b>Foreplay：</b>Chrome 浏览器控制连续失败，Tripo、Suno、ElevenLabs、Bambu Lab、ELEGOO、Creality 均未取得本期详情；不更新广告排名与状态。</li><li><b>Hi3D：</b>官方博客本次打开后顶部仍为 9/8 横评，未见 9/21–9/26 新条目。</li><li><b>Rodin/Hyper3D：</b>官方 changelog 显示 September 2026 条目，但页面没有逐条日期，不能断言发生在本周。</li><li><b>Hunyuan3D：</b>官方 2.1 仓库 News 最新仍为 2025-07-26，未找到本周产品发布。</li><li><b>Meshy 官方发布：</b>本期定向搜索返回的 7.1 发布与 API 记录均早于本周窗口，不用旧新闻填充。</li></ul></section>
<details id="audit"><summary>核查台账与限制</summary><ul><li><b>系统时间：</b>2026-09-26 20:07 +0800；本周窗口 9/21–9/26，遗漏期 9/19–9/20。</li><li><b>Web 搜索：</b>11 个查询，3 次调用。</li><li><b>页面打开：</b>10 次；成功 8 次（Tripo 官方列表及 3 篇正文、Hi3D 官方博客、Hyper3D changelog、Hunyuan3D 仓库、VFX DESK），失败 2 次（GitHub Pages 两个 URL 在 Web 工具中不可访问）。</li><li><b>Foreplay/浏览器：</b>Chrome 创建标签和列表读取共 3 次失败；原生 Chrome 连接随后超时。失败前未返回广告详情，故有效广告样本为 0。</li><li><b>本地核查：</b>读取维护规范、仓库状态与发布源；起始提交 b5d2fee，本地无未提交文件。</li></ul></details>
</div></div>
'''

text = INDEX.read_text()

# Keep the advertising timestamp untouched: no ad source was successfully read this run.
text = re.sub(r'<div class="meta"><b>.*?</b>', '<div class="meta"><b>本周部分更新 · 2026-09-26（Foreplay 未刷新）</b>', text, count=1)
stats_start = text.index('<!--STATS_START-->')
stats_end = text.index('<!--STATS_END-->', stats_start) + len('<!--STATS_END-->')
stats = '<!--STATS_START--><b>官方动态已核实至 9/26</b>｜广告数据仍为 9/18 采集：Tripo 新媒体 12 个；五品牌 Top 5 未刷新｜完整台账 147 条截至 9/15<!--STATS_END-->'
text = text[:stats_start] + stats + text[stats_end:]

report_start = text.index('<div class="latest-summary merged-report"><h2 id="weekly-report">')
board_start = text.index('<div class="view on" id="view-board">', report_start)
text = text[:report_start] + report + '\n' + text[board_start:]

view_warning = '<div class="callout"><b>本期未刷新 Foreplay 数据</b><p>Chrome 浏览器桥接在 9/26 采集时不可用；以下继续显示 9/18 已核实的近 7 天 Top 5，不代表 9/20–9/26 当前排名或状态。</p></div>'
text = text.replace(view_warning, '')
for view_id in ('view-ref', 'view-printer'):
    marker = f'<div class="view" id="{view_id}"><div class="latest-summary merged-report">'
    replacement = marker + view_warning
    text = text.replace(marker, replacement, 1)

INDEX.write_text(text)
(ROOT / 'index-2026-09-26-partial.html').write_text(text)
(ROOT / 'monitor-2026-09-26.md').write_text('''# 周中监测 2026-09-26（周六）

> 本期原计划周五执行，实际于周六完成。官方内容监测已更新；Foreplay 浏览器桥接失败，广告数据保留 9/18 采集结果。

## 一、看板健康检查

- 内容：已更新至 9/26。
- 广告：停留在 9/18，已明确标记未刷新；没有仅修改广告时间戳。
- 排查：确认 Mac/Chrome、Foreplay 登录、浏览器扩展连接和 `git log --oneline origin/main..HEAD`。

## 二、竞品动态

- 9/24 Tripo Remove Lighting：在清洁基础色与保留原始风格之间切换。
- 9/21 Tripo Smart UV：自动接缝、UV 岛打包、利用率与双向高亮。
- 9/22 VFX DESK：同输入横评加入面数、孔洞、非流形边和浮游几何检查；文章明确其未自行生成模型。
- 遗漏期 9/19：Tripo 发布 GPT-6 Astra + Tripo CLI + Unreal MCP 城市场景工作流。

## 三、未找到清单

- Foreplay 六个品牌本期详情均未取得。
- Hi3D 官方博客顶部仍为 9/8。
- Hyper3D 九月条目无逐条日期，无法归入本周。
- Hunyuan3D 2.1 仓库 News 最新仍为 2025-07-26。

## 四、核查台账

- Web 搜索 11 个查询 / 3 次调用。
- 页面打开 10 次：成功 8，失败 2。
- Foreplay/浏览器 4 次连接尝试均未返回广告详情，有效广告样本 0。
''')

redirect = '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=index-2026-09-26-partial.html#weekly-report"><title>Tripo 2026-09-26 周报</title></head><body><p><a href="index-2026-09-26-partial.html#weekly-report">打开 2026-09-26 周报</a></p></body></html>'
(ROOT / 'creative-report-2026-09-26.html').write_text(redirect)
print('partial refresh prepared', CHECKED)
