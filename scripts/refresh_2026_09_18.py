from __future__ import annotations

import hashlib
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CHECKED = "2026-09-18 17:13（北京时间）"
CHECKED_ISO = "2026-09-18T17:13:00+08:00"
WINDOW_START = "2026-09-12"
WINDOW_END = "2026-09-18"

SOURCES = {
    "Suno": "https://app.foreplay.co/discovery/brands/oPvAH6CW7CEKiBLDuT4O",
    "ElevenLabs": "https://app.foreplay.co/discovery/brands/9Z7CseeEuZYSx2YRDbtg",
    "Bambu Lab 3D": "https://app.foreplay.co/discovery/brands/LiRME2YDApIGvg3zpOAp",
    "ELEGOO": "https://app.foreplay.co/discovery/brands/LgKtxP1bqsgM6QWZXZ4N",
    "Creality": "https://app.foreplay.co/discovery/brands/VxqhJPGt4z7mY0ipRIQZ",
    "Tripo3D": "https://app.foreplay.co/discovery/brands/VcPyFobqOqSrd6V4KRQG",
    "Tripoai": "https://app.foreplay.co/discovery/brands/j36CDWGTnin1cO9WCouE",
}


def c(brand, dup, rel, status, media, title, quote, analysis):
    started = {1: "2026-09-18", 2: "2026-09-17", 3: "2026-09-16", 5: "2026-09-14", 7: "2026-09-12"}[rel]
    return {
        "brand": brand,
        "id": hashlib.sha1(media.encode()).hexdigest()[:12],
        "duplicates": dup,
        "started": started,
        "ended": None if status == "Still Running" else "Foreplay 核查时已结束（结束日未在列表卡片显示）",
        "live": status == "Still Running",
        "format": "Video" if media.endswith(".mp4") else "Image",
        "video": media if media.endswith(".mp4") else None,
        "thumb": media if not media.endswith(".mp4") else None,
        "title": title,
        "quote": quote,
        "analysis": analysis,
        "language": "多语言" if brand in {"Bambu Lab 3D", "ELEGOO"} else "英语",
        "source": SOURCES[brand],
        "checked_at": CHECKED_ISO,
    }


TOP = [
    c("Suno",127,3,"Still Running","https://r2.foreplay.co/9a1111b139191faa82f9df0316d44f37fca999aaf0835dbb29ee0014e8f7969a.png","创作者内容配乐：从帖子场景切入","The Perfect Sound for Your Content","用短视频、品牌曲和趋势内容三个使用场景解释产品；127 是同素材广告数，不代表效果。"),
    c("Suno",53,3,"Still Running","https://r2.foreplay.co/e1ad390aa312c383b5a368b11540f39d9dcc8ddbe2793bd412e27e9434f39b83.mp4","Pro 权益清单视频","Make Any Song You Can Imagine","把歌曲数量、商用权、音频上传和排队速度集中到一条付费信息中。"),
    c("Suno",50,3,"Still Running","https://r2.foreplay.co/30b769bb38acd42df9ea753221e5b440217ca007ca118243ea27af54e4430ac1.mp4","Studio 2.0：把编辑能力作为主角","Studio 2.0 is live.","直接展示浏览器 DAW 的可控性，适合参考为工作台功能演示。"),
    c("Suno",46,3,"Still Running","https://r2.foreplay.co/8d8b4efdde4ddc7e20c2a4e87da385077a204ec75f1165d2040499f45e49691d.jpg","歌词到成曲：输入与结果并列","Try Suno Today","单图同时交代写词、选风格和生成歌曲，信息路径短。"),
    c("Suno",34,3,"Still Running","https://r2.foreplay.co/a72a324426f249c3b1fbcc5f60f177725a9340a6e9247721c108fc81f1991528.mp4","Pro 权益视频的另一媒体版本","Make Any Song You Can Imagine","与第二名文案接近但媒体不同，按同媒体去重后保留；数值不可相加解读。"),
    c("ElevenLabs",30,3,"Still Running","https://r2.foreplay.co/ac753b8cab4787e2212f380f9aee4faa8a626c9213b9990d055b39d75ffd0bb8.jpg","生产级语音基础设施","Production Ready Voice Infrastructure","面向技术团队强调适配现有架构与扩展能力，可参考开发者诉求的表达。"),
    c("ElevenLabs",23,2,"Still Running","https://r2.foreplay.co/659cc8d12e9dc67ad382289160fab75f1f3100c586228b3ff07c7f43e73c7f70.jpg","限时优惠＋多模态能力清单","All-in-One AI Creative Editor","把语音、视频、4K 视觉与客户背书写在同一张图中；折扣信息仅作素材观察。"),
    c("ElevenLabs",18,3,"Still Running","https://r2.foreplay.co/3d9c44bc02c39f2456de4158b6c138a202064ab296b441be5ed5258ec74708bd.mp4","有声书：按交付任务组织功能","Create & publish audiobooks in minutes","围绕有声书制作、翻译和发行讲完整任务，比泛功能罗列更具体。"),
    c("ElevenLabs",17,2,"Still Running","https://r2.foreplay.co/9dc84526ea621abedfdae8ac99cf803792774409c9e244f609f10cfc7f49e911.mp4","播客：无需相机与麦克风","Generate podcast episodes in minutes","以播客交付切入，再补充多语言和多模态能力。"),
    c("ElevenLabs",14,3,"Still Running","https://r2.foreplay.co/5a1ea09a007fe2876d71e3589f8eaefaf23323cb8acb03d020f2ea8f61e4d1f2.mp4","移动端一站式创作入口","Create everything in one place","以应用下载承接语音、音乐、视频和图片生成。"),
    c("Bambu Lab 3D",14,3,"Still Running","https://r2.foreplay.co/65137bfa08c7d347dd9f0633c6331093c27b20e47c077da6db05b6091cea9c4a.mp4","家居角落改造：打印结构件与花盆","build my own","由真实空间问题展开，从结构连接件到定制花盆，完整展示用途。"),
    c("Bambu Lab 3D",7,3,"Still Running","https://r2.foreplay.co/ec0ad7b3a0f7ce5fd10d6abbf35e6ffbd2d854302b607e3b6774c9bc855a5f82.mp4","街头送花：作品与真人反应","humans appreciate art & connection","用打印花朵引出陌生人反应，产品存在于故事过程里。"),
    c("Bambu Lab 3D",7,3,"Still Running","https://r2.foreplay.co/245061be708d0fec2a91e2736e8eafafb21da3b990787de0fdf5fb633e0c660e.mp4","家庭项目：儿童玩具与收纳","millions de modèles sur MakerWorld","法语创作者通过家庭使用情境解释易用性，并明确商业合作。"),
    c("Bambu Lab 3D",6,3,"Still Running","https://r2.foreplay.co/faece4016a830a92633f65bbc128e66641a759abd3bf9a2e2242fffb9ee025dd.mp4","双项目并行：面具与兵器","two big projects at the same time","用多台设备并行完成大型道具，突出过程规模。"),
    c("Bambu Lab 3D",3,3,"Still Running","https://r2.foreplay.co/3ec57bdcaf65436ec1f9b612a76c6e066797982209c6ae14503de79fd0eaad07.mp4","游戏武器复刻：免费模型承接","Bloodhound’s Fang from Elden Ring","以明确 IP 道具成品吸引兴趣并导向 MakerWorld；借鉴时需使用自有或授权内容。"),
    c("ELEGOO",14,5,"Ended","https://r2.foreplay.co/27590571c16a04c4f8381a1acfb7e0d607df31b3ee77e13ea31ca2c6ddb04255.mp4","Saturn 4 Ultra 16K：速度与精度","Précision Ultra-HD 16K","法语视频将速度和精度集中表达；核查时已结束。"),
    c("ELEGOO",8,1,"Ended","https://r2.foreplay.co/bf5bf4ff05b764080eae56fbdbdf9365b2c8a9ccae9a00564c2934198b399192.png","Deals 静态促销素材","ELEGOO Deals","短期静态促销，起投当日核查已结束。"),
    c("ELEGOO",7,2,"Ended","https://r2.foreplay.co/d0345a06005c1e342a5ae12ae8956f657084083454235d5dad75ad3b5b1fe978.png","桌面配件：从文件到原型","Pourquoi acheter quand tu peux l'imprimer ?","用理线器、键帽、手机支架等具体清单解释桌面打印场景。"),
    c("ELEGOO",6,3,"Ended","https://r2.foreplay.co/095f6b257030aa99353b5f77d2b53a0d28c3f6d0758dc917e59e7df86fca9dd6.jpg","桌面配件清单的图片版本","Du fichier au prototype","与第三名主题接近但媒体不同，按同媒体去重保留；核查时已结束。"),
    c("ELEGOO",3,7,"Ended","https://r2.foreplay.co/61781ef59ad2de3fb0c6183b0dd151580ec57b1a2f9147ee3e1544765abff0d9.jpg","Saturn 4 Ultra 16K 英语图片","Experience Next-Level 3D Printing","用 16K、自动调平与快速倾斜剥离作为功能组合；广告宣称未独立实测。"),
    c("Creality",45,3,"Still Running","https://r2.foreplay.co/f04f837188765b1fd059eff90bb9046e4bca923a7b48b666a0f9297d30c3e4ae.jpg","SPARKX i8：四色速度与耗材效率","The Fastest, Most Filament Efficient Four-Color 3D Printer","众筹预热素材集中列出速度、废料、自动调平和监控；性能数字属于品牌宣称。"),
    c("Creality",21,3,"Still Running","https://r2.foreplay.co/67b5a135b964a15c33993d6d561fdd23f3db04737f4b5c0bab71690515660d14.jpg","SPARKX i8：倒计时与早鸟价","ONLY 7 DAYS LEFT","在同一能力清单前加入时间和价格钩子；优惠仅作广告观察。"),
    c("Creality",20,3,"Still Running","https://r2.foreplay.co/020523645b491ce95855fedfe65da81bea3a69360881ef1d7a38c9ea151ef3e5.jpg","SPARKX i8：限量价格版本","Don't wait!","同一众筹主张的另一张图片，按媒体去重保留。"),
    c("Creality",18,3,"Still Running","https://r2.foreplay.co/b9b6baba36a237ec4630b2090c4e146781560196d24cd00b60f403bb7672851f.jpg","SPARKX i8：第三张静态变体","Best price ever, strictly limited","保持同一落地页与能力清单，用不同媒体扩展测试。"),
    c("Creality",3,3,"Still Running","https://r2.foreplay.co/f23c68cac87650ae539dca90f7bf302a4ce21d68fe78fd7c71f1d33dbc56d849.jpg","K2 Pro Combo：专业项目升级","Take your production to the next level","用速度、精度和质量三点面向专业项目，信息明显短于 i8 众筹素材。"),
]

for brand in SOURCES:
    rank = 0
    for item in TOP:
        if item["brand"] == brand:
            rank += 1
            item["rank"] = rank

TRIPO = [
    c("Tripo3D",3,3,"Still Running","https://r2.foreplay.co/b248645aed4612c31297e40a8a7f7b44b5ba778f79d56b118ebc0d7f6d1ff4aa.mp4","模块化角色：替换、组合与个性化","Build Unlimited 3D Modular Characters with AI","把编辑动作直接放在标题中，强调生成后的可组合性。"),
    c("Tripo3D",2,3,"Still Running","https://r2.foreplay.co/fd6f1106d731b230ae5a9dc9fb28f6d4dc7be803171b2f1814d46a028075c46b.png","韩语 GPT-6 Astra 3D 工作流","GPT-6 Astra 워크플로우를 3D로 확장하세요","延续模型工作流借势，并用韩语落地。"),
    c("Tripo3D",2,3,"Still Running","https://r2.foreplay.co/608ea9084a4183147f968dee8dab9912fa6e1b95978425b5f542502a26f66185.mp4","模块化角色视频变体","Swap, combine & personalize","同主题另一条视频，媒体不同。"),
    c("Tripo3D",1,3,"Still Running","https://r2.foreplay.co/9f0e00f83393590d12e078c6665a5f2fd3fd97f89b3e4984ce2c596099c9e1d5.mp4","日语高精细手办","高精細なフィギュアをAIで。","以手办结果切入日本受众。"),
    c("Tripo3D",1,3,"Still Running","https://r2.foreplay.co/ac502ead0ddfbc5649d05c2cea3df261b6b0e6d12d2004109b29fdd08d1cad1a.png","游戏 MOD：秒级生成资产","Make Game Mods in Minutes","延续游戏资产与 MOD 用途。"),
    c("Tripo3D",1,3,"Still Running","https://r2.foreplay.co/eba1d478b373c53e51ebd15ba433ba8522d0a6bae801a59088fbb201f716892b.mp4","物理设计：跳过手工建模","Skip Manual 3D Modeling","把快速迭代实体设计作为主张。"),
    c("Tripo3D",1,3,"Still Running","https://r2.foreplay.co/75142a6e897d7372e21cc6bccd3ff711fbfac7615942a19563f6e7880e13833a.png","电影感图片转 3D 环境","Cinematic Image → 3D Environment","同方向的新媒体版本；需继续观察存续。"),
    c("Tripo3D",1,3,"Still Running","https://r2.foreplay.co/51c0711f99576c25d2e1914db117b3f9cad07fa8eefb75774eecade477b90fa3.mp4","电影感环境视频版本","Create 3D environments","视频展示图像到环境的转换。"),
    c("Tripo3D",1,3,"Still Running","https://r2.foreplay.co/74914f15c497796e507687db498e5791c9303c5d48f98d35caa49157d75ceb3b.png","电影感环境图片变体","AI-powered modeling","同主题不同媒体。"),
    c("Tripo3D",1,3,"Still Running","https://r2.foreplay.co/18f068d0778eb1bc08bdfc7812bc5f4b2ef5f33f4c606ae5933e61305bc80be0.mp4","日语高精细手办视频变体","AIでアイデアを高精細な3Dモデルに。","与日语手办主题配套的视频媒体。"),
    c("Tripoai",4,3,"Ended","https://r2.foreplay.co/68ea2bcd293fa633f51681a49fef49b437376059780c4109dd0cbb7eb3bd3a45.mp4","创作者 Blender 制作过程","Trusting the process on a tight deadline","KOL 以分步制作和最终灯光变化呈现结果；核查时已结束。"),
    c("Tripoai",1,2,"Ended","https://r2.foreplay.co/041d23336ffc3a547ff843ec29fa7502a43cc3dc8b0e8ec31beb7804c0bc5e14.mp4","单图到可用 3D 模型","I didn't expect AI to make 3D modeling this simple.","创作者强调从一张图到可用模型；核查时已结束。"),
]
for item in TRIPO:
    if "韩语" in item["title"]:
        item["language"] = "韩语"
    elif "日语" in item["title"]:
        item["language"] = "日语"


def media_html(item):
    url = html.escape(item["video"] or item["thumb"], quote=True)
    if item["video"]:
        return f'<video src="{url}" controls muted playsinline preload="none"></video>'
    return f'<img src="{url}" alt="{html.escape(item["title"], quote=True)}" loading="lazy">'


def cards_html(items):
    chunks = []
    for item in items:
        state_cls = "" if item["live"] else " ended"
        state = "仍在投" if item["live"] else "已结束（结束日未在列表卡片显示）"
        rank_label = f'TOP {item["rank"]}' if item.get("rank") else "本期新增"
        chunks.append(
            f'<article class="sample" data-case-id="{item["id"]}" data-rank="{item.get("rank", "")}" data-variants="{item["duplicates"]}">'
            f'<div class="top-rank">{rank_label} <b>{item["duplicates"]}</b> 变体</div>{media_html(item)}'
            f'<div class="copy"><small>起投 {item["started"]} · {item["format"]} · {item["language"]}</small>'
            f'<h3>{html.escape(item["title"])}</h3><p class="state{state_cls}">{state} · 9/18 核查</p>'
            f'<p>原文节选：“{html.escape(item["quote"]) }”</p><p>{html.escape(item["analysis"])}</p>'
            f'<p><a href="{item["source"]}" target="_blank" rel="noopener">Foreplay 来源 ↗</a></p></div></article>'
        )
    return '<div class="samples case-samples">' + ''.join(chunks) + '</div>'


def view_html(view_id, heading, brands):
    nav = ''.join(f'<a href="#top-{b.replace(" ", "-")}">{b}</a>' for b in brands)
    sections = []
    for brand in brands:
        items = [x for x in TOP if x["brand"] == brand]
        sections.append(f'<section id="top-{brand.replace(" ", "-")}"><h2>{brand}</h2>{cards_html(items)}</section>')
    return (
        f'<div class="view" id="{view_id}"><div class="latest-summary merged-report"><h2>{heading}</h2>'
        f'<span class="status">起投窗口：{WINDOW_START}–{WINDOW_END} · 9/18 核查</span>'
        '<p>每个品牌独立排名：仅纳入近 7 天起投的素材，按 Foreplay Creative Duplicates 降序，同媒体去重后最多 5 项。包括仍在投和已结束；不足 5 条不使用旧素材补位。数值是素材复用指标，不代表花费或效果。</p>'
        f'<nav class="report-nav">{nav}</nav>{"".join(sections)}'
        '<details><summary>排名口径与覆盖限制</summary><p>本次按 Foreplay 品牌页 Newest 列表读取卡片，并以卡片相对天数换算起投日；一条 Suno 详情已抽查确认“3D”对应 9/16 起投。页面日期筛选未用于起投过滤。状态以卡片圆点核查；ELEGOO 入榜素材均显示结束，列表卡片未给出结束日期。</p><p>本次可见卡片：Suno 10、ElevenLabs 8、Bambu Lab 8、ELEGOO 10、Creality 8。动态列表可能受平台同步和加载影响，因此排名描述的是本次读取范围，不是 Meta 全库排名。</p><p><a href="foreplay-top5-2026-09-18.json">下载本期 Top 5 台账</a> · <a href="foreplay-top5-2026-09-15.json">查看 9/15 台账</a></p></details>'
        '</div></div>'
    )


report = f'''<div class="latest-summary merged-report"><h2 id="weekly-report">本期周报 · 素材与热点追踪</h2>
<span class="status">2026-09-18 · 周五更新已完成</span>
<p>本周窗口：9/14–9/18；广告起投 Top 5 窗口：9/12–9/18。9/18 已重新读取 Tripo、Suno、ElevenLabs、Bambu Lab、ELEGOO 与 Creality 的 Foreplay 品牌页。完整 Tripo 历史台账仍截至 9/15，本期新增一组 9/16–9/17 起投素材补充，不把局部读取写成全库总量。</p>
<nav class="report-nav"><a href="#hotspots">热点追踪</a><a href="#tripo-new">Tripo 新素材</a><a href="#view-ref">横向 Top 5</a><a href="#view-printer">打印机 Top 5</a><a href="#news">竞品动态</a><a href="#audit">核查与限制</a><a href="creative-report-2026-09-15.html">9/15 历史报告</a></nav>
<section id="hotspots"><h2>值得我们跟进的热点</h2><p>以下是基于本次可见素材与官方来源的选题建议，不是投放效果结论。</p><div class="hot-grid">
<article class="hot-card"><span class="status">新增 · 优先验证</span><h3>可组合 3D：把“生成后能改”拍清楚</h3><p><b>信号：</b>Tripo 9/16 起投的模块化角色视频有 3 个同素材广告，另一媒体版本有 2 个。</p><p><b>建议：</b>制作角色部件替换、组合、个性化的屏录，明确每一步输入与输出；记录编辑耗时与导出结果。</p><footer>下次复查：2026-09-25 · <a href="{SOURCES['Tripo3D']}">Foreplay 来源 ↗</a></footer></article>
<article class="hot-card"><span class="status">新增 · 优先验证</span><h3>专业工作台：功能演示代替泛结果片</h3><p><b>信号：</b>Suno Studio 2.0 视频显示 50 个同素材广告；ElevenLabs 的生产级语音基础设施图片显示 30 个。</p><p><b>建议：</b>选 Meshy 的一个专业流程，用界面操作、可控参数与导出物连续演示，避免只用前后对比。</p><footer>下次复查：2026-09-25 · <a href="{SOURCES['Suno']}">Suno 来源 ↗</a></footer></article>
<article class="hot-card"><span class="status">新增 · 优先验证</span><h3>打印场景从“机器展示”转向真实任务</h3><p><b>信号：</b>Bambu 的家居角落改造视频显示 14 个同素材广告；街头送花与家庭项目各显示 7 个。</p><p><b>建议：</b>用原创桌面收纳、家居装饰或游戏道具完成“设计—生成—分件—打印—使用”全链路，拍出真人使用。</p><footer>下次复查：2026-09-25 · <a href="{SOURCES['Bambu Lab 3D']}">Bambu 来源 ↗</a></footer></article>
<article class="hot-card"><span class="status">持续观察</span><h3>众筹预热：同一卖点用多张静态图扩展</h3><p><b>信号：</b>Creality SPARKX i8 近 7 天 Top 4 均为同一众筹能力主张的不同图片，变体数为 45、21、20、18。</p><p><b>建议：</b>同一经验证卖点可以拆成“功能清单、痛点、限时入口、成品用途”四张图，但结论仍需自身数据验证。</p><footer>下次复查：2026-09-25 · <a href="{SOURCES['Creality']}">Creality 来源 ↗</a></footer></article>
<article class="hot-card"><span class="status">持续观察</span><h3>日韩本地化继续出现，但样本小</h3><p><b>信号：</b>Tripo 9/16 新增韩语 Astra 工作流图片与日语高精细手办视频；当前各自的同素材广告数为 2 和 1。</p><p><b>建议：</b>继续做语言、画面、落地页三项一致性核查；样本量不足，不据此判断整体加码。</p><footer>下次复查：2026-09-25 · <a href="{SOURCES['Tripo3D']}">Tripo 来源 ↗</a></footer></article>
<article class="hot-card"><span class="status">短周期信号</span><h3>ELEGOO 多条素材快速结束</h3><p><b>信号：</b>近 7 天 Top 5 均在 9/18 核查时显示结束，最高素材为 Saturn 4 Ultra 16K 法语视频，14 个同素材广告。</p><p><b>建议：</b>保留为短周期测试案例，复查是否出现新媒体或重新上线；不推断停投原因。</p><footer>下次复查：2026-09-25 · <a href="{SOURCES['ELEGOO']}">ELEGOO 来源 ↗</a></footer></article>
</div></section>
<section id="tripo-new"><h2>Tripo 本期新素材 · 9/16–9/17 起投</h2><p>本次在两个 Tripo 品牌页核实 12 个新媒体：Tripo3D 10 个仍在投，Tripoai 2 个显示结束。它们是本次可见列表的新增补充，不代表完整新增量。</p>{cards_html(TRIPO)}</section>
<section id="news"><h2>竞品动态与来源核查</h2>
<div class="insight"><b>9/15 · Tripo：上线 GPT-Image-2.5 Sunburst 参考图工作流。</b><p>官方博客列表写明可在 Tripo 中生成、编辑并准备多视图参考图，用于角色、资产和 3D 工作流。本期把它列为“参考图准备—多视图—3D”的选题依据。</p><blockquote>“generate, edit, and prepare detailed multi-view image references”</blockquote><p><a href="https://www.tripo3d.ai/blog">Tripo 官方博客列表</a>，列表日期：“2026/09/15”。</p></div>
<div class="insight"><b>9/10 · Meshy 7.1：Ultra 2K/4K 细节能力继续处于发布期。</b><p>该发布早于本次周报窗口，作为持续跟进项保留。官方正文称 9/10 起逐步上线；Ultra 2K 支持单图和多图，Ultra 4K 仅支持单图。</p><blockquote>“Starting September 10, 2026, Meshy 7.1 rolls out gradually”</blockquote><p><a href="https://www.meshy.ai/blog/meshy-7-1-launch">Meshy 官方发布</a>。</p></div>
<div class="callout"><b>本次未核实到的新发布</b><p>Hi3D、Rodin/Hyper3D、Hunyuan3D 在 9/14–9/18 窗口内未找到可写入的官方更新。该结论只描述本次检索范围，不等于品牌没有动态。</p></div>
</section>
<details id="audit"><summary>核查范围与限制</summary><ul><li>Foreplay：逐个打开 7 个品牌页的 Newest 列表；本次读取可见卡片共 64 条，其中按近 7 天起投筛选并去重后生成五品牌 Top 5。</li><li>Tripo：本次新增补充 12 个媒体；完整 147 条历史台账未重新全量回溯，因此全库统计继续标记为 9/15。</li><li>状态：列表绿点记为仍在投，其余记为已结束；列表未显示结束日时不臆测具体日期。</li><li>新闻：官方来源正文或列表日期可核实后才写入；广告宣称与 Foreplay 变体数不作为效果证据。</li></ul></details>
</div></div>
'''

top_payload = {
    "window_start": WINDOW_START,
    "window_end": WINDOW_END,
    "checked_at": CHECKED_ISO,
    "ranking": "Creative Duplicates descending; same media deduplicated; all statuses; visible Newest-list coverage",
    "visible_card_counts": {"Suno": 10, "ElevenLabs": 8, "Bambu Lab 3D": 8, "ELEGOO": 10, "Creality": 8},
    "cases": TOP,
}
(ROOT / "foreplay-top5-2026-09-18.json").write_text(json.dumps(top_payload, ensure_ascii=False, indent=2) + "\n")
(ROOT / "tripo-new-ads-2026-09-18.json").write_text(json.dumps({"checked_at": CHECKED_ISO, "coverage": "visible Newest-list cards", "cases": TRIPO}, ensure_ascii=False, indent=2) + "\n")

index = ROOT / "index.html"
text = index.read_text()
archive = ROOT / "index-2026-09-18-before-refresh.html"
if not archive.exists():
    archive.write_text(text)

updated_start = text.index("<!--UPDATED_START-->")
updated_end = text.index("<!--UPDATED_END-->", updated_start) + len("<!--UPDATED_END-->")
text = text[:updated_start] + f"<!--UPDATED_START-->{CHECKED}<!--UPDATED_END-->" + text[updated_end:]
old_stats_start = text.index("<!--STATS_START-->")
old_stats_end = text.index("<!--STATS_END-->", old_stats_start) + len("<!--STATS_END-->")
new_stats = "<!--STATS_START--><b>9/18 新增核实 12 个 Tripo 媒体</b>（10 在投 / 2 已结束）｜五品牌 Top 素材已按近 7 天重排｜完整 Tripo 台账 147 条仍截至 9/15<!--STATS_END-->"
text = text[:old_stats_start] + new_stats + text[old_stats_end:]
text = text.replace('<div class="meta"><b>广告数据已重新采集 · 2026-09-15</b>', '<div class="meta"><b>周五更新已发布 · 2026-09-18</b>')
text = text.replace('📊 最新素材（9/15）', '📊 完整台账（9/15）')
text = text.replace("最近核实的 Tripo 3D 起投日期：2026-09-13", "最近核实的 Tripo 3D 起投日期：2026-09-16")

report_start = text.index('<div class="latest-summary merged-report"><h2 id="weekly-report">')
board_start = text.index('<div class="view on" id="view-board">', report_start)
text = text[:report_start] + report + "\n" + text[board_start:]

ref_start = text.index('<div class="view" id="view-ref">')
printer_start = text.index('<div class="view" id="view-printer">', ref_start)
new_ref = view_html("view-ref", "横向参考 · 近 7 天变体数 Top 5", ["Suno", "ElevenLabs"])
text = text[:ref_start] + new_ref + "\n" + text[printer_start:]
printer_start = text.index('<div class="view" id="view-printer">')
script_start = text.index('<script>', printer_start)
new_printer = view_html("view-printer", "打印机厂商 · 近 7 天变体数 Top 5", ["Bambu Lab 3D", "ELEGOO", "Creality"])
text = text[:printer_start] + new_printer + "\n" + text[script_start:]

text = text.replace('<h2>最新广告数据 · 2026-09-15 15:48</h2>', '<h2>完整广告台账 · 截至 2026-09-15 15:48</h2>')
text = text.replace('已核实 147 条广告记录，111 条在投、36 条已结束。下面展示 57 张精选预览；全部 147 条记录均可在下方台账查看原始广告。', '完整台账保留 9/15 已核实的 147 条广告记录（111 条在投、36 条已结束）。9/18 新素材请查看上方“Tripo 本期新素材”；本区不把局部补采并入全库统计。')
index.write_text(text)

monitor = f'''# Meshy 周中监测｜2026-09-18\n\n## 本次更新\n\n- Foreplay：重读 Tripo3D、Tripoai、Suno、ElevenLabs、Bambu Lab、ELEGOO、Creality 的 Newest 列表。\n- Tripo：新增核实 12 个媒体，10 个在投、2 个已结束；完整 147 条历史台账仍截至 9/15。\n- 排名：窗口 {WINDOW_START}–{WINDOW_END}，每品牌按 Creative Duplicates 降序 Top 5，同媒体去重，含在投与已结束，不足 5 条不补旧素材。\n- 官网动态：核实 Tripo 9/15 Sunburst 工作流；Meshy 7.1 作为 9/10 发布的持续跟进项。\n\n## 值得跟进\n\n1. 可组合 3D：用角色部件替换与组合证明“生成后能改”。\n2. 专业工作台：用真实界面、参数与导出物讲完整流程。\n3. 打印真实任务：家居改造、桌面配件、游戏道具从生成走到使用。\n4. 众筹预热：同一卖点拆成能力清单、痛点、限时入口和用途图。\n5. 日韩本地化：继续检查语言、画面和落地页一致性，当前样本仍小。\n\n## 限制\n\n- Foreplay 动态列表可能受同步和加载影响；本期排名描述本次可见范围。\n- 列表状态可核实，但已结束素材的具体结束日未显示，不补写日期。\n- Creative Duplicates 是素材复用指标，不代表花费、转化或效果。\n'''
(ROOT / "monitor-2026-09-18.md").write_text(monitor)

redirect = '''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=index.html#weekly-report"><title>Tripo 素材周报</title></head><body><p><a href="index.html#weekly-report">打开 2026-09-18 周报</a></p></body></html>'''
(ROOT / "creative-report-2026-09-18.html").write_text(redirect)
(ROOT / "creative-report.html").write_text(redirect)

print("refreshed", index)
