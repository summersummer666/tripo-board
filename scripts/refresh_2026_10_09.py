from pathlib import Path
import html, json, re

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
CHECKED = "2026-10-09 17:12（北京时间）"
WINDOW = "2026-10-03–2026-10-09"

brands = {
 "Suno": {"url":"https://app.foreplay.co/discovery/brands/oPvAH6CW7CEKiBLDuT4O", "cards":[
  ("1678505087017103",29,"2026-10-06","Still Running","https://r2.foreplay.co/ed25c19b7d70d993ab6adaf78ebae608f98c6007ec6996c7e0d975eef2b6b473.jpg","Pro 权益清单：歌曲数、商用权、音频上传与优先队列","Unlock Suno’s best features with the Pro Plan","https://suno.com/go/paid"),
  ("4362193960579508",4,"2026-10-06","Still Running","https://r2.foreplay.co/66e601ed91ce403c21aae7687ad189d643054dc4c5e956119ea444875e36afe8.jpg","Pro 权益清单的另一视频媒体","Make Any Song You Can Imagine","https://suno.com/go/paid"),
  ("1480430640805754",1,"2026-10-07","Still Running","https://r2.foreplay.co/6e5a839dbd2a7ed4a62a8bcab751a315aa5efbcd753746aeab395fdf711c1af5.jpg","西语 Pro 权益版本","Crea cualquier canción que puedas imaginar","https://suno.com/go/paid"),
  ("1068109189387596",1,"2026-10-06","Still Running","https://r2.foreplay.co/d11a40573517394b5c34440a5079842442f8c347d20c6c07c48da6502b195650.jpg","日语共创：多段录音合成为歌曲","Sunoで一緒に曲づくり","https://suno.com/ja"),
  ("1081672444498655",1,"2026-10-06","Still Running","https://r2.foreplay.co/f9d950af83222fa2355e0e46753d06156dba6d6c2b3ff8407afab14e607302be.png","日语半成品素材再创作","Sunoを無料で試してみよう","https://suno.com/ja") ]},
 "ElevenLabs": {"url":"https://app.foreplay.co/discovery/brands/9Z7CseeEuZYSx2YRDbtg", "cards":[
  ("1679408323570915",20,"2026-10-08","Still Running","https://r2.foreplay.co/ef2d827e27f9442a47e05504b528f1f3bae11f5d63747c5aae6116768245aa77.jpg","Eleven v4 免费额度与多模态能力","Ranked #1 by Artificial Analysis","https://join.elevenlabs.io/v4-offer"),
  ("1740733457230921",19,"2026-10-08","Still Running","https://r2.foreplay.co/88fda292db36ec368c16018b2d4a519cc15b25fc954f4ab3af8fc5e58cff4619.jpg","1 美元 Starter 计划","Get the Starter plan for $1","https://elevenlabs.io/pricing"),
  ("1155371710387248",18,"2026-10-08","Still Running","https://r2.foreplay.co/bf54a1581d546fd83a2e418c8d41ef64cce8aff39786431dbc92a90edb8237ef.jpg","夜间来电由 ElevenAgents 承接","Never miss a call again","https://join.elevenlabs.io/agents/v6"),
  ("1629936708575832",10,"2026-10-08","Still Running","https://r2.foreplay.co/9d5ac651b45fa2edcc5bbfa7e200118d56bd1c31b5a25f58645ff20f134d12ed.jpg","低延迟与表现力并列","Eleven v4 now on ElevenAgents","https://elevenlabs.io/v4"),
  ("1809443150251429",9,"2026-10-08","Still Running","https://r2.foreplay.co/abcd77d9175f2e29a3917fec1e772f7649ff8447d655e1f62e47ffa083b820f7.jpg","用自然语言搭建语音代理","Meet ElevenAgents Architect","https://elevenlabs.io/app/agents/architect") ]},
 "Bambu Lab 3D": {"url":"https://app.foreplay.co/discovery/brands/LiRME2YDApIGvg3zpOAp", "cards":[
  ("2897547593961688",18,"2026-10-03","Ended 2026-10-08","https://r2.foreplay.co/c23c534f40eee666a3ac0357532384f445a9d0edf4aa5c1ce3294dd4775064e3.jpg","用 P2S 制作饼干工具","I used a 3D printer to help me cook","https://us.store.bambulab.com/products/pla-pure"),
  ("1792151515161949",13,"2026-10-04","Still Running","https://r2.foreplay.co/b872bb23ce10e07086088a88ee06a47840bcca83f4ed8ac1051d6921ea2845f4.jpg","小商家定制青蛙印章","make a stamp to personalize my envelopes","https://us.store.bambulab.com/collections/printers-for-home-decor"),
  ("1646381293904650",10,"2026-10-06","Still Running","https://r2.foreplay.co/6eee5d2e517f9d94b65db7e8d37c7039b22bf3cac14b90c5eb4455de3d9fbaa9.jpg","A1 彩色打印游戏角色爪件","printing in color","http://store.bambulab.com/products/a1"),
  ("1325519212861867",9,"2026-10-03","Still Running","https://r2.foreplay.co/077ce63c9396ba1691199b2e0f1a75262c03eb2ebe44dd59bebc0f5629d8ed66.jpg","桌游工具与微缩模型","hobby tools and miniatures","http://store.bambulab.com/products/a1"),
  ("28981377954886150",6,"2026-10-03","Ended 2026-10-08","https://r2.foreplay.co/cd481f338e5539026780178554dcae581f7593257f29134626d844238435ff03.jpg","桌游玩家套件与 token","player’s kit or token sets","http://store.bambulab.com/products/a1") ]},
 "ELEGOO": {"url":"https://app.foreplay.co/discovery/brands/LgKtxP1bqsgM6QWZXZ4N", "cards":[]},
 "Creality": {"url":"https://app.foreplay.co/discovery/brands/VxqhJPGt4z7mY0ipRIQZ", "cards":[
  ("1739238420701257",20,"2026-10-07","Still Running","https://r2.foreplay.co/d1bea56a9350a500032a3886eb81fad7aac2ce1c9d1b1e5095c65c7295128c2d.jpg","SPARKX i8 Benchy 速度与废料对比","Same Benchy. Different generation.","https://www.indiegogo.com/projects/creality-sparkx/creality-sparkx-i8-the-fastest-most-filament-efficient-four-color-3d-printer"),
  ("1775113037110960",1,"2026-10-07","Still Running","https://r2.foreplay.co/2afe4fb733108d9ebf84826581e5ad3db94b972649d120fe1b4ed3db2b950f7a.jpg","K2 Pro 小生意开箱套装","start printing sellable inventory in 24 hours","https://store.creality.com/products/k2-pro-combo-spacepi-x4-1-hyper-pla-3") ]}
}

def card_html(card, rank, brand_url):
    ad_id, dup, start, status, media, title, quote, landing = card
    ended = " ended" if status.startswith("Ended") else ""
    return f'''<article class="sample" data-case-id="{ad_id}" data-rank="{rank}" data-variants="{dup}"><div class="top-rank">TOP {rank} <b>{dup}</b> 变体</div><img src="{media}" alt="{html.escape(title)}" loading="lazy"><div class="copy"><small>起投 {start} · 本期详情核实</small><h3>{html.escape(title)}</h3><p class="state{ended}">{html.escape(status)} · 10/09 核查</p><p>原文节选：“{html.escape(quote)}”</p><p>Creative Duplicates 为采集时复用指标，不代表花费或效果。</p><p><a href="{brand_url}" target="_blank" rel="noopener">Foreplay 品牌页 ↗</a> · <a href="{landing}" target="_blank" rel="noopener">落地页 ↗</a></p></div></article>'''

def section(name):
    b=brands[name]
    if not b["cards"]:
        body='<div class="callout"><b>近 7 天未找到符合条件素材</b><p>本次核实 Newest 可见前 8 条详情，真实起投均早于 10/03；其中多条虽只运行 1–5 天，但起投在 8/29–8/31，未用运行天数冒充近期起投，也未拿旧素材补位。</p></div>'
    else:
        body='<div class="samples case-samples">'+''.join(card_html(c,i,b["url"]) for i,c in enumerate(b["cards"],1))+'</div>'
    return f'<section id="top-{name.replace(" ","-")}"><h2>{name}</h2>{body}</section>'

ref_view = f'''<div class="view" id="view-ref"><div class="latest-summary merged-report"><h2>横向参考 · 近 7 天变体数 Top 5</h2><span class="status">起投窗口：{WINDOW} · {CHECKED}核查</span><p>按真实 Status 起投日筛选，Creative Duplicates 降序，同媒体去重；不足 5 条显示实际数量。</p><nav class="report-nav"><a href="#top-Suno">Suno</a><a href="#top-ElevenLabs">ElevenLabs</a></nav>{section("Suno")}{section("ElevenLabs")}<details><summary>覆盖限制</summary><p>Suno 读取 8 条并逐条打开详情；ElevenLabs 读取至少 10 条，入榜 5 条逐项打开。动态列表不是 Meta 全库，因此仅称本次可见范围 Top 5。</p><p><a href="foreplay-top5-2026-10-09.json">下载本期台账</a> · <a href="foreplay-top5-2026-09-18.json">2026-09-18 历史台账</a></p></details></div></div>'''
printer_view = f'''<div class="view" id="view-printer"><div class="latest-summary merged-report"><h2>打印机厂商 · 近 7 天变体数 Top 5</h2><span class="status">起投窗口：{WINDOW} · {CHECKED}核查</span><p>规则同横向参考；广告 Case 与新闻分开，数值不解释为效果。</p><nav class="report-nav"><a href="#top-Bambu-Lab-3D">Bambu Lab 3D</a><a href="#top-ELEGOO">ELEGOO</a><a href="#top-Creality">Creality</a></nav>{section("Bambu Lab 3D")}{section("ELEGOO")}{section("Creality")}<details><summary>覆盖限制</summary><p>Bambu Lab 可见 10 条并核实所有可能入榜候选；Creality 本期仅找到 2 条符合窗口；ELEGOO 核实 Newest 前 8 条可见详情后为 0 条。受动态加载限制，仅代表本次读取范围。</p><p><a href="foreplay-top5-2026-10-09.json">下载本期台账</a></p></details></div></div>'''

report = f'''<div class="latest-summary merged-report"><h2 id="weekly-report">本期周报 · 素材与热点追踪</h2><span class="status">2026-10-09 · 已更新并补抓 Foreplay</span>
<p>本周窗口：10/05–10/09；广告起投筛选窗口：{WINDOW}。遗漏期：9/27–10/04（其中 10/02 周五未形成发布）。本期重新读取 Foreplay 六个品牌页，广告数据不再停留 9/18。</p>
<nav class="report-nav"><a href="#health">看板健康</a><a href="#hotspots">热点追踪</a><a href="#news">竞品动态</a><a href="#missing">未找到清单</a><a href="#audit">核查台账</a><a href="#view-ref">横向 Top 5</a><a href="#view-printer">打印机 Top 5</a><a href="index-2026-10-09.html#weekly-report">10/09 日期归档</a><a href="index-2026-09-26-partial.html#weekly-report">9/26 归档</a></nav>
<section id="health"><h2>看板健康检查</h2><div class="callout"><b>判定：本期广告与公开动态均已刷新。</b><p>采集时间为 {CHECKED}；起投日来自 Foreplay 详情 Status。完整历史广告台账仍截至 9/15，本期文件是 10/03–10/09 窗口增量，不把样本称作全库。</p></div></section>
<section id="hotspots"><h2>值得我们跟进的热点</h2><div class="hot-grid">
<article class="hot-card"><span class="status">新增 · 高优先级</span><h3>把功能清单变成“同一任务的完整链路”</h3><p><b>已核实信号：</b>Tripo 10/08 官方教程展示 Concept → Smart Mesh P2.0 → Segment → Texture → Retopo → DCC Bridge → Unity；本期 Tripo3D 广告同步强调 Smart Mesh、High Detail、8K Texture 与 Segment V2。</p><p><b>跟进价值：</b>官网教程与广告共同把“生成”推进到可交付工作流。</p><p><b>建议动作：</b>用同一游戏角色制作 Meshy 的生成、局部修复、减面、贴图与引擎导入公开演示。</p><p><b>复查指标：</b>完成时长、DCC 导入成功率、修复步骤数、教程完成率。</p><footer>下次复查：2026-10-16 · <a href="https://www.tripo3d.ai/blog/workflow-game-scene">Tripo 官方教程 ↗</a></footer></article>
<article class="hot-card"><span class="status">新增 · 广告信号</span><h3>从能力演示转向可立刻想象的具体任务</h3><p><b>已核实信号：</b>Bambu 入榜 Case 集中在饼干工具、商家印章、桌游工具与角色道具；Creality 用 Benchy 前后对比和小生意开箱套装承接。</p><p><b>跟进价值：</b>案例先给用途与结果，再解释设备；适合 Meshy 联动打印和小游戏资产。</p><p><b>建议动作：</b>测试“一个输入→一个可打印用途”短视频，避免只展示转台模型。</p><p><b>复查指标：</b>3 秒停留、生成到打印点击、保存率、评论中的用途提问。</p><footer>下次复查：2026-10-16 · <a href="#view-printer">本期打印机 Case</a></footer></article>
<article class="hot-card"><span class="status">继续跟进</span><h3>代理式创作正在把产品放进多工具流程</h3><p><b>已核实信号：</b>Meshy 10/04 开发者文章比较 Astra 单独制作角色与 Astra+Meshy；Tripoai 10/08 在投 KOL 素材也以 Astra 对比、Unreal 工作流和打印成品承接。</p><p><b>建议动作：</b>为 Meshy API 做可复现的代理任务模板，并公开成功与失败步骤。</p><p><b>复查指标：</b>任务完成率、人工接管次数、API 调用成本、最终资产可编辑性。</p><footer>下次复查：2026-10-16 · <a href="https://www.meshy.ai/developers/blog/astra-with-and-without-meshy/">Meshy 开发者文章 ↗</a></footer></article>
</div></section>
<section id="news"><h2>竞品动态</h2><div class="insight"><b>10/08 · Tripo：发布 Unity 游戏场景完整工作流。</b><p>正文从概念图、P2.0、分件、贴图、Retopo 到 DCC Bridge/Unity，明确 HD Model 与 Smart Mesh 是两条路线。</p><blockquote>“Concept image → Smart Mesh P2.0 → segment → texture → Retopo → DCC Bridge → Unity”</blockquote><p><a href="https://www.tripo3d.ai/blog/workflow-game-scene">官方正文</a>；日期来自<a href="https://www.tripo3d.ai/blog">官方列表</a>。</p></div><div class="insight"><b>10/06–10/09 · Hi3D：集中发布搜索型比较与打印主题文章。</b><p>官方列表在 10/06 出现角色、人体、2D→3D、浮雕等多篇比较内容，10/09 新增模型转换器和动漫角色主题；这是内容分发信号，不等同于产品发布。</p><blockquote>“Image &amp; File Formats Compared”</blockquote><p><a href="https://www.hi3d.ai/blog">Hi3D 官方列表</a>。</p></div><div class="insight"><b>10/04 · Meshy：Astra 单独与 Astra+Meshy 角色工作流对比。</b><p>官方开发者文章的列表摘要称两条流程都完成绑定和行走，但 Meshy 路径更贴近概念图；该结论来自 Meshy 自家实验，应视为品牌侧证据。</p><blockquote>“only the Meshy run looked like the concept art”</blockquote><p><a href="https://www.meshy.ai/developers/blog/astra-with-and-without-meshy/">官方正文</a>。</p></div></section>
<section id="missing"><h2>未找到清单</h2><ul><li><b>ELEGOO：</b>Newest 前 8 条可见素材详情起投均早于 10/03；近 7 天合规素材为 0，不补旧素材。</li><li><b>Rodin/Hyper3D：</b>官方 changelog 顶部仍为 September 2026，未见 10/05–10/09 条目。</li><li><b>Hunyuan3D：</b>2.1 官方仓库 News 最新仍为 2025-07-26，未找到本周产品发布。</li><li><b>舆情：</b>本期没有核实到足以独立归因的 JA/ZH 新评测；不以搜索摘要填充。</li></ul></section>
<details id="audit"><summary>核查台账与限制</summary><ul><li><b>系统时间：</b>2026-10-09 17:12 +0800；本周窗口 10/05–10/09，遗漏期 9/27–10/04。</li><li><b>Foreplay：</b>打开 7 个品牌页（Tripo3D、Tripoai、Suno、ElevenLabs、Bambu Lab、ELEGOO、Creality）；详情成功核实 34 条，失败/动态索引失效 6 次。五品牌入榜 17 条；ELEGOO 为 0。</li><li><b>Web：</b>4 个定向搜索；打开 8 个页面/列表，7 成功、1 个 Hi3D 文章详情内部错误；所有写入事实均来自成功打开页面。</li><li><b>限制：</b>Foreplay 动态列表受可见加载范围影响，排名是本次读取范围 Top 5，不宣称 Meta 全库；变体数不是效果指标。</li></ul></details></div></div>'''

text=INDEX.read_text()
text=re.sub(r'<div class="meta"><b>.*?</b>', '<div class="meta"><b>本周已更新 · 2026-10-09</b>', text, count=1)
text=re.sub(r'<!--UPDATED_START-->.*?<!--UPDATED_END-->', '<!--UPDATED_START-->'+CHECKED+'<!--UPDATED_END-->', text, count=1)
text=text.replace('最近核实的 Tripo 3D 起投日期：2026-09-16', '最近核实的 Tripo 3D 起投日期：2026-10-07；Tripoai KOL 起投日期：2026-10-08')
text=re.sub(r'<!--STATS_START-->.*?<!--STATS_END-->', '<!--STATS_START--><b>广告与公开动态已核实至 10/09</b>｜五品牌近 7 天入榜 17 条：Suno 5、ElevenLabs 5、Bambu 5、ELEGOO 0、Creality 2｜Tripo 两品牌页发现本周新广告｜完整历史台账 147 条截至 9/15<!--STATS_END-->', text, count=1)
rs=text.index('<div class="latest-summary merged-report"><h2 id="weekly-report">')
bs=text.index('<div class="view on" id="view-board">',rs)
text=text[:rs]+report+'\n'+text[bs:]
vr=text.index('<div class="view" id="view-ref">')
vp=text.index('<div class="view" id="view-printer">',vr)
tail=text.index('<script>',vp)
text=text[:vr]+ref_view+'\n'+printer_view+'\n'+text[tail:]
INDEX.write_text(text)
(ROOT/'index-2026-10-09.html').write_text(text)
(ROOT/'monitor-2026-10-09.md').write_text('# Tripo 看板周报 2026-10-09\n\n- 广告采集：Foreplay 7 个品牌页，详情成功 34 条。\n- 五品牌近 7 天 Top：Suno 5、ElevenLabs 5、Bambu Lab 5、ELEGOO 0、Creality 2。\n- 公开动态：Tripo Unity 完整工作流、Hi3D 搜索型内容集群、Meshy Astra 协作实验。\n- 遗漏期：2026-09-27–2026-10-04，10/02 未形成发布。\n')
payload={"checked_at":CHECKED,"window":WINDOW,"method":"Foreplay Newest; verified each shortlisted Status start date; deduped by media; Creative Duplicates descending","brands":{k:{"source":v["url"],"items":[{"ad_id":c[0],"creative_duplicates":c[1],"start_date":c[2],"status":c[3],"media":c[4],"title_zh":c[5],"quote":c[6],"landing_page":c[7]} for c in v["cards"]]} for k,v in brands.items()},"limitations":["Dynamic visible range, not Meta full library","ELEGOO: 8 visible details checked, all started before window","Creative Duplicates is a capture-time reuse count, not spend or performance"]}
(ROOT/'foreplay-top5-2026-10-09.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
redirect='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=index.html#weekly-report"><title>Tripo 周报与热点</title></head><body><p><a href="index.html#weekly-report">打开统一周报与热点入口</a></p></body></html>'
(ROOT/'creative-report.html').write_text(redirect)
(ROOT/'creative-report-2026-10-09.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=index-2026-10-09.html#weekly-report"><title>Tripo 2026-10-09 周报</title></head><body><p><a href="index-2026-10-09.html#weekly-report">打开 2026-10-09 周报</a></p></body></html>')
print('refresh prepared',CHECKED)
