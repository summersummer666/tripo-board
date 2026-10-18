from pathlib import Path
import html, json, re, runpy

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_1009 = (ROOT / "index-2026-10-09.html").read_bytes()
runpy.run_path(str(ROOT / "scripts" / "refresh_2026_10_09.py"))
INDEX = ROOT / "index.html"
CHECKED = "2026-10-16 17:00（北京时间）"
WINDOW = "2026-10-10–2026-10-16"

brands = {
 "Suno": {"url":"https://app.foreplay.co/discovery/brands/oPvAH6CW7CEKiBLDuT4O", "cards":[
  ("2959260737772544",63,"2026-10-14","Still Running","Video","https://r2.foreplay.co/e598e9a1ab0a0d72003d90f0f5df04c3e2900a377a0054d39b24814e061c2152.jpg","v6 发布主张","Welcome to the v6 era.","http://suno.com/go/paid"),
  ("945415831585149",2,"2026-10-14","Still Running","Image","https://r2.foreplay.co/09c992a4c72a28fdfb40f67cc197dd3b94426f032d720628ba2d51d1720999a9.png","日语外包替代场景另一版","外注先がひとつ減る","https://suno.com/ja"),
  ("1247918537539172",2,"2026-10-14","Still Running","Image","https://r2.foreplay.co/f961facaf2ff36ebbcd8ed64c7a29d469d2644e60c082c4170c214a8715fceb2.png","日语外包替代场景","外注先がひとつ減る","https://suno.com/ja"),
  ("1768943870822199",2,"2026-10-14","Still Running","Video","https://r2.foreplay.co/977fa5087fcd09a78b2259d861785095195338f86e098abbf25a661b58eb5a10.jpg","创作者歌曲共创","Listen and remix on @sunomusic","http://suno.com/collab/polina"),
  ("1403075184839503",1,"2026-10-15","Still Running","Video","https://r2.foreplay.co/362d4ef6ee7a450d696040ab9b36c1c87f5711d29367c1d6a37c01426303e38f.jpg","韩语玩具乐器变成歌曲","오타마톤도 음악이 된다","https://suno.com/ko") ]},
 "ElevenLabs": {"url":"https://app.foreplay.co/discovery/brands/9Z7CseeEuZYSx2YRDbtg", "cards":[
  ("1384692373646615",37,"2026-10-14","Still Running","DCO","https://r2.foreplay.co/11cac36db2478d2c7e31a43c3317b4e8f6581cbf6708e958cb025c658f756637.jpg","全能型移动订阅","Finally, a subscription that covers it all","http://itunes.apple.com/app/id6743162587"),
  ("1828126851949324",30,"2026-10-14","Still Running","Video","https://r2.foreplay.co/05e2a098e3a16f0e1f617bf32838808cb6e2bbf7be237b94a85c4b3eedd5c4e1.jpg","v4 声音表现力","Expressive, ultra-realistic voices","https://elevenlabs.io/v4"),
  ("2218095645777896",22,"2026-10-14","Still Running","DCO","https://r2.foreplay.co/f599230ddf6d3034777182311770c8a63a6efbeaeaa8d3ec26f7a5752d9c2374.jpg","全能型移动订阅另一版","Finally, a subscription that covers it all","http://itunes.apple.com/app/id6743162587"),
  ("1420105192924658",18,"2026-10-14","Still Running","DCO","https://r2.foreplay.co/f2dc2083c8d4f9c407f7d5b666f3b8a9bdcbb6de3d8e16136431dbd3d4635f14.jpg","MCP 配置成本预估","Check what a config change will cost before it ships.","https://elevenlabs.io/mcp"),
  ("2170566447224337",18,"2026-10-14","Still Running","DCO","https://r2.foreplay.co/1b1d5ccab6946f477663a4147ec83c7b90eb8397d3c8f322d2f10ede5fccd5c9.jpg","MCP 配置成本预估另一版","Check what a config change will cost before it ships.","https://elevenlabs.io/mcp") ]},
 "Bambu Lab 3D": {"url":"https://app.foreplay.co/discovery/brands/LiRME2YDApIGvg3zpOAp", "cards":[
  ("939014872291007",4,"2026-10-11","Still Running","Video","https://r2.foreplay.co/76f958fc8cbe9197bd82a0b6de8f54c4cbec72da316c1ba133fc10f7b1f787e0.jpg","暗黑链锯斧制作过程","How I made a Grimdark Chainaxe!","https://us.store.bambulab.com/products/h2c"),
  ("1441292714876713",1,"2026-10-15","Still Running","Video","https://r2.foreplay.co/accdc563e6a201957c59e4afbd412f8e4bec743adb95af5abf4400f45a6bc172.jpg","隐蔽式 3D 打印场景","Covert 3D Printing",""),
  ("1865611587937074",1,"2026-10-10","Still Running","Carousel","https://r2.foreplay.co/0ce9600db534cd09c077d138ea41c5029b21610131a475f0f8245cee2c244cac.png","品牌能力轮播","A new way to make things.","http://us.store.bambulab.com/"),
  ("28587960607520024",1,"2026-10-10","Still Running","Carousel","https://r2.foreplay.co/2df3e398d7d24a438351103cb236334118eb6af3bd6c0378f18bac3eae0717a5.png","打印质量轮播","Print quality. You can see.","http://us.store.bambulab.com/"),
  ("977173664730991",1,"2026-10-10","Still Running","Carousel","https://r2.foreplay.co/8ad4d1f9bda4d4f15a13038f417a49d1190396acac4be95fbb6e75464766d280.png","品牌探索轮播","Explore Bambu Lab.","https://us.store.bambulab.com/") ]},
 "ELEGOO": {"url":"https://app.foreplay.co/discovery/brands/LgKtxP1bqsgM6QWZXZ4N", "cards":[]},
 "Creality": {"url":"https://app.foreplay.co/discovery/brands/VxqhJPGt4z7mY0ipRIQZ", "cards":[
  ("1822614545325892",4,"2026-10-15","Ended 2026-10-16","Image","https://r2.foreplay.co/f19e5babdc714b176db4272f5eb3d56210e68b5547bb825fb346a0d083e2cf49.jpg","发布会倒计时","Just 1 day to go!","https://to.store.creality.com/mega_launch_ig"),
  ("1149454107735764",2,"2026-10-15","Still Running","Video","https://r2.foreplay.co/c27f3484f298aedbcaf780ba34e46fff3df2d499e057c06d0237e49a7a606911.jpg","3D 打印台球灯","Not just a pool table light. It’s 3D printed.",""),
  ("1477239467636524",2,"2026-10-15","Still Running","Image","https://r2.foreplay.co/d1515a62620f1d65dcd459c3dd9cf09c1b7b6f62cd92bf6569d7bbd5a7bde8ec.jpg","Maker Program 招募","CREALITY MAKER PROGRAM — CYCLE 2 IS OPEN!","https://www.creality.com/campaigns/maker-program-2026"),
  ("1612578539745669",2,"2026-10-15","Still Running","Video","https://r2.foreplay.co/d646a3ab858d0a802805d64a3b237f6ad2725f0775d5847efba3fe579c1a456a.jpg","K3 多材料换喷嘴","Beyond Nozzles. Conquer Materials.",""),
  ("2174929043145590",2,"2026-10-15","Still Running","Video","https://r2.foreplay.co/127a0802d79980d0af314a79c45c2f8e4fa37b532a49b467fc4d07be1456f.jpg","Ender 用户记忆","Do you remember your first Ender?","") ]}
}

def card_html(card, rank, brand_url):
    ad_id, dup, start, status, fmt, media, title, quote, landing = card
    display_media = "assets/preview-unavailable.svg" if ad_id == "2174929043145590" else media
    links = f'<a href="{brand_url}" target="_blank" rel="noopener">Foreplay 品牌页 ↗</a>'
    if landing: links += f' · <a href="{landing}" target="_blank" rel="noopener">落地页 ↗</a>'
    preview_note = '<p><b>预览说明：</b>Foreplay 缩略图在页面核查后返回 404；保留广告 ID 与品牌页供复核。</p>' if display_media != media else ''
    return f'''<article class="sample" data-case-id="{ad_id}" data-rank="{rank}" data-variants="{dup}"><div class="top-rank">TOP {rank} <b>{dup}</b> 变体</div><img src="{display_media}" alt="{html.escape(title)}" loading="lazy"><div class="copy"><small>起投 {start} · {fmt} · ID {ad_id}</small><h3>{html.escape(title)}</h3><p class="state">{html.escape(status)} · 10/16 核查</p><p>原文节选：“{html.escape(quote)}”</p>{preview_note}<p>Creative Duplicates 为采集时复用指标，不代表花费或效果。</p><p>{links}</p></div></article>'''

def section(name):
    b = brands[name]
    if not b["cards"]:
        body = '<div class="callout"><b>近 7 天未找到符合条件素材</b><p>本次按 Newest 打开 6 条候选详情，起投日均早于 10/10；再用 Still Running 复查可见在投素材，仍未发现窗口内起投。未用旧素材补位。</p></div>'
    else:
        body = '<div class="samples case-samples">' + ''.join(card_html(c, i, b["url"]) for i, c in enumerate(b["cards"], 1)) + '</div>'
    return f'<section id="top-{name.replace(" ","-")}"><h2>{name}</h2>{body}</section>'

ref_view = f'''<div class="view" id="view-ref"><div class="latest-summary merged-report"><h2>横向参考 · 近 7 天变体数 Top 5</h2><span class="status">起投窗口：{WINDOW} · {CHECKED}核查</span><p>按 Status 真实起投日筛选，Creative Duplicates 降序，同媒体取最大值去重；同分按较新起投日、广告 ID 升序。不足 5 条显示实际数量。</p><nav class="report-nav"><a href="#top-Suno">Suno</a><a href="#top-ElevenLabs">ElevenLabs</a></nav>{section("Suno")}{section("ElevenLabs")}<details><summary>覆盖限制</summary><p>Suno 可见 6 条逐项打开；ElevenLabs 可见 10 条，入榜 5 条逐项打开。动态列表不是 Meta 全库，仅称本次可见范围 Top 5。</p><p><a href="foreplay-top5-2026-10-16.json">下载本期台账</a> · <a href="foreplay-top5-2026-10-09.json">10/09 历史台账</a> · <a href="foreplay-top5-2026-09-18.json">9/18 历史台账</a></p></details></div></div>'''
printer_view = f'''<div class="view" id="view-printer"><div class="latest-summary merged-report"><h2>打印机厂商 · 近 7 天变体数 Top 5</h2><span class="status">起投窗口：{WINDOW} · {CHECKED}核查</span><p>规则同横向参考；广告 Case 与新闻分开，数值不解释为效果。</p><nav class="report-nav"><a href="#top-Bambu-Lab-3D">Bambu Lab 3D</a><a href="#top-ELEGOO">ELEGOO</a><a href="#top-Creality">Creality</a></nav>{section("Bambu Lab 3D")}{section("ELEGOO")}{section("Creality")}<details><summary>覆盖限制</summary><p>Bambu Lab 核实 6 条边界候选，5 条入榜；Creality 6 条候选逐项核实，按规则取 5；ELEGOO 同时核查 Newest 与 Still Running，窗口内为 0。仅代表本次读取范围。</p><p><a href="foreplay-top5-2026-10-16.json">下载本期台账</a></p></details></div></div>'''

report = f'''<div class="latest-summary merged-report"><h2 id="weekly-report">本期周报 · 素材与热点追踪</h2><span class="status">2026-10-16 · Foreplay 与公开动态已刷新</span>
<p>本周监测窗口：10/12–10/16；广告起投窗口：{WINDOW}。上次成功更新为 10/09，遗漏期仅为 10/10–10/11 周末，本周五按计划执行。</p>
<nav class="report-nav"><a href="#health">看板健康</a><a href="#hotspots">热点追踪</a><a href="#news">竞品动态</a><a href="#missing">未找到清单</a><a href="#audit">核查台账</a><a href="#view-ref">横向 Top 5</a><a href="#view-printer">打印机 Top 5</a><a href="index-2026-10-16.html#weekly-report">10/16 日期归档</a><a href="index-2026-10-09.html#weekly-report">10/09 归档</a></nav>
<section id="health"><h2>看板健康检查</h2><div class="callout"><b>判定：本期增量已刷新。</b><p>采集时间为 {CHECKED}；五品牌共入榜 20 条。Tripo 完整台账保留 10/12 深度回溯后的 52 条代表记录，本期 JSON 是 10/10–10/16 的横向与打印机品牌核实样本，不将可见样本称作全库。</p></div></section>
<section id="hotspots"><h2>值得我们跟进的热点</h2><div class="hot-grid">
<article class="hot-card"><span class="status">继续跟进 · 高优先级</span><h3>“生产可用”正在由单点能力变成完整工作流</h3><p><b>已核实信号：</b>Tripo 本周连续发布角色/道具完整流程、Rigging &amp; Animation 与 SketchUp Bridge；10/15 Foreplay 素材同步覆盖 P2.0、游戏角色和商品预览。</p><p><b>跟进价值：</b>内容与投放都在证明从输入到 DCC/引擎交付。</p><p><b>建议动作：</b>用同一角色制作 Meshy 从生成、Smart Topology、贴图、绑定到引擎导入的计时案例。</p><p><b>复查指标：</b>总时长、人工修复次数、DCC 导入成功率、教程完成率。</p><footer>下次复查：2026-10-23 · <a href="https://www.tripo3d.ai/blog">Tripo 官方列表 ↗</a></footer></article>
<article class="hot-card"><span class="status">新增 · 高优先级</span><h3>工具链入口正在向 SketchUp、MCP 与创作者代理扩展</h3><p><b>已核实信号：</b>Tripo 10/15 发布 SketchUp Bridge；ElevenLabs 本期高变体广告用“配置变更成本”承接 MCP；Tripoai 在投素材持续使用 KOL 工作流和邀请码。</p><p><b>跟进价值：</b>用户先在熟悉工具或代理任务里触发生成，产品主页不再是唯一入口。</p><p><b>建议动作：</b>挑选一个高频 DCC 与一个代理任务，分别验证一键传输与可复现调用模板。</p><p><b>复查指标：</b>激活率、任务完成率、人工接管次数、回访率。</p><footer>下次复查：2026-10-23 · <a href="https://www.tripo3d.ai/blog/tripo-dcc-bridge-for-sketchup">Tripo SketchUp Bridge ↗</a></footer></article>
<article class="hot-card"><span class="status">新增 · 自家能力</span><h3>Meshy Smart Topology 升级适合做同输入对比</h3><p><b>已核实信号：</b>Meshy API changelog 10/15 新增 meshy-t2.5，说明更锐利的游戏资产细节，100–30,000 目标面数，并成为 Smart Topology 默认模型。</p><p><b>建议动作：</b>使用相同图片、相同目标面数对比 T2 与 T2.5 的轮廓、细节和导入表现，公开限制。</p><p><b>复查指标：</b>轮廓偏差、坏面率、减面后细节保持、引擎导入时间。</p><footer>下次复查：2026-10-23 · <a href="https://docs.meshy.ai/en/api/changelog">Meshy API changelog ↗</a></footer></article>
</div></section>
<section id="news"><h2>竞品动态</h2>
<div class="insight"><b>10/13–10/16 · Tripo：密集发布工作流与 DCC 内容。</b><p>官方列表显示 10/13 发布 Rigging &amp; Animation，10/14 发布角色、道具与 Godot 工作流，10/15 发布 SketchUp Bridge，10/16 发布多代理游戏教程。</p><blockquote>“send generated models … directly into SketchUp in real time”</blockquote><p><a href="https://www.tripo3d.ai/blog">官方列表</a> · <a href="https://www.tripo3d.ai/blog/tripo-dcc-bridge-for-sketchup">SketchUp 正文</a>。</p></div>
<div class="insight"><b>10/13 · Hi3D：继续用 3D 打印比较内容承接搜索需求。</b><p>官方列表新增儿童 3D 打印玩具生成器比较；10/10 的 STL 生成器正文强调多视图、拆件与打印准备。这是内容分发信号，不是产品发布。</p><blockquote>“STL export is only one step in the workflow”</blockquote><p><a href="https://www.hi3d.ai/blog">官方列表</a> · <a href="https://www.hi3d.ai/blog/best-ai-stl-generators">STL 比较正文</a>。</p></div>
<div class="insight"><b>10/15 · Meshy：API 新增 Smart Topology 模型 meshy-t2.5。</b><p>官方 changelog 写明该模型用于 Text/Image to 3D，输出三角面，目标面数 100–30,000，并成为未指定 ai_model 时的默认选项。</p><blockquote>“the newest Smart Topology model”</blockquote><p><a href="https://docs.meshy.ai/en/api/changelog">官方 changelog</a>。</p></div>
</section>
<section id="missing"><h2>未找到清单</h2><ul><li><b>ELEGOO 广告：</b>Newest 与 Still Running 均复查，窗口内起投为 0。</li><li><b>Rodin/Hyper3D：</b>官方 changelog 顶部仍为 September 2026；官方博客最新新闻为 9/29，未见 10/12–10/16 产品发布。</li><li><b>Hunyuan3D：</b>本次打开官方 Hunyuan3D-2 仓库，模型表日期仍为 2025 年，未核实到本周发布。</li><li><b>独立 EN/JA/ZH 舆情：</b>Tripo 官方 EN/JA/ZH 页面均可访问，但未找到本周可独立归因的新评测，未以搜索摘要填充。</li></ul></section>
<details id="audit"><summary>核查台账与限制</summary><ul><li><b>系统时间：</b>2026-10-16 17:00 +0800；本周窗口 10/12–10/16；遗漏期 10/10–10/11。</li><li><b>Foreplay：</b>打开 7 个品牌页；逐项核实详情 41 条（Tripo3D 6、Tripoai Still Running 6、Suno 6、ElevenLabs 5、Bambu 6、ELEGOO 6、Creality 6），详情打开成功 41，失败 0。五品牌入榜 20 条。</li><li><b>Web：</b>12 个定向搜索；打开 10 次官方页面/列表，9 成功、Hi3D 列表直接 open 1 次内部错误，后续成功打开其官方正文核实。</li><li><b>限制：</b>Foreplay 动态可见范围不是 Meta 全库；变体数为采集时指标，不是窗口新增量、花费或效果。</li></ul></details></div></div>'''

text = INDEX.read_text()
text = re.sub(r'<div class="meta"><b>.*?</b>', '<div class="meta"><b>本周已更新 · 2026-10-16</b>', text, count=1)
text = re.sub(r'<!--UPDATED_START-->.*?<!--UPDATED_END-->', '<!--UPDATED_START-->'+CHECKED+'<!--UPDATED_END-->', text, count=1)
text = re.sub(r'最近核实的 Tripo 3D 起投日期：[^<]+', '最近核实的 Tripo3D 起投日期：2026-10-15；Tripoai 在投起投日期：2026-10-13–10-14', text, count=1)
text = re.sub(r'<!--STATS_START-->.*?<!--STATS_END-->', '<!--STATS_START--><b>广告与公开动态已核实至 10/16</b>｜五品牌近 7 天入榜 20 条：Suno 5、ElevenLabs 5、Bambu 5、ELEGOO 0、Creality 5｜Tripo3D 10/15 新素材与 Tripoai 在投均已复查｜完整台账 52 条截至 10/12<!--STATS_END-->', text, count=1)
text = re.sub(r'(同素材广告数采用 Foreplay Creative Duplicates，不代表花费或效果。).*?</div>', r'\1最近核实的 Tripo3D 起投日期：2026-10-15；Tripoai 在投起投日期：2026-10-13–10-14。</div>', text, count=1)
rs = text.index('<div class="latest-summary merged-report"><h2 id="weekly-report">')
bs = text.index('<div class="view on" id="view-board">', rs)
text = text[:rs] + report + '\n' + text[bs:]
vr = text.index('<div class="view" id="view-ref">')
vp = text.index('<div class="view" id="view-printer">', vr)
tail = text.index('<script>', vp)
text = text[:vr] + ref_view + '\n' + printer_view + '\n' + text[tail:]
INDEX.write_text(text)
(ROOT/'index-2026-10-16.html').write_text(text)
(ROOT/'monitor-2026-10-16.md').write_text('# Tripo 看板周报 2026-10-16\n\n- Foreplay：7 个品牌页，详情成功 41 条。\n- 五品牌近 7 天 Top：Suno 5、ElevenLabs 5、Bambu Lab 5、ELEGOO 0、Creality 5。\n- 重点：Tripo 完整工作流与 SketchUp Bridge；Meshy Smart Topology t2.5；打印机用途型 Case。\n- 遗漏期：2026-10-10–2026-10-11（上次 10/09 成功，本周五按计划执行）。\n')
payload = {"checked_at":CHECKED,"window":WINDOW,"method":"Foreplay Newest; ELEGOO and Tripoai also checked Still Running; verified Status start date; media dedupe; Creative Duplicates desc; ties by newer start then ad ID asc","brands":{k:{"source":v["url"],"items":[{"ad_id":c[0],"creative_duplicates":c[1],"start_date":c[2],"status":c[3],"format":c[4],"media":c[5],"title_zh":c[6],"quote":c[7],"landing_page":c[8]} for c in v["cards"]]} for k,v in brands.items()},"limitations":["Dynamic visible range, not Meta full library","ELEGOO: Newest and Still Running checked; no eligible start date","Creative Duplicates is a capture-time reuse count, not spend or performance"]}
(ROOT/'foreplay-top5-2026-10-16.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
redirect='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=index.html#weekly-report"><title>Tripo 周报与热点</title></head><body><p><a href="index.html#weekly-report">打开统一周报与热点入口</a></p></body></html>'
(ROOT/'creative-report.html').write_text(redirect)
(ROOT/'creative-report-2026-10-16.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=index-2026-10-16.html#weekly-report"><title>Tripo 2026-10-16 周报</title></head><body><p><a href="index-2026-10-16.html#weekly-report">打开 2026-10-16 周报</a></p></body></html>')
(ROOT / "index-2026-10-09.html").write_bytes(ARCHIVE_1009)
print('refresh prepared', CHECKED)
