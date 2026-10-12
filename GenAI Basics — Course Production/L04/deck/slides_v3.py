"""L04 deck v3: the v2 layout plus graphics wherever something can be shown instead of told —
service interfaces, annotated images, radar/bar charts and simple process diagrams.
Slides not redefined here are taken from slides_v2 unchanged."""

import charts as ch
import slides_v2 as v2
from slides import t
from slides_v2 import AM, CY, GR, RD, VI, S, img, note, pic, pt, ul
import slides_patterns as pat
import slides_prompts as pr
import slides_services as sv

# literal colors for SVG (CSS variables are not reliable inside SVG presentation attributes)
H_CY, H_GR, H_AM, H_RD, H_VI = "#38bdf8", "#34d399", "#fbbf24", "#f87171", "#c084fc"


def ui(name: str) -> str:
    return f"assets/ui/{name}.jpg"


def shot(src, cap="", cover=True):
    return (f'<div class="pic{" cover" if cover else ""}"><div class="frame shot"><img src="{src}" alt=""></div>'
            f'{f"<div class=cap>{cap}</div>" if cap else ""}</div>')


def logo_tile():
    return (f'<div class="pic"><div class="frame shot" style="background:#ffffff;display:flex;align-items:center;justify-content:center;">'
            f'<img src="{ui("chatgpt_logo")}" alt="ChatGPT" style="width:38%;height:auto;max-height:70%;border-radius:0"></div></div>')


# ---------------------------------------------------------------- 3 agenda as a visual journey
def s03():
    parts = [("denoise_1", t("Как модель рисует", "How the model draws"), t("шум ➔ картинка", "noise ➔ image"), H_AM),
             ("ui:gemini", t("Пять сервисов", "Five services"), t("кто для чего", "which one for what"), H_CY),
             ("A2_structured", t("Промпт", "The prompt"), t("от фразы к структуре", "from phrase to structure"), H_GR),
             ("C3_door", t("Паттерны", "Patterns"), t("правка • персонаж • фотосессия", "edit • character • photo shoot"), H_VI),
             ("D4_banner", t("Риски и домашка", "Risks & homework"), t("где нельзя, что сдать", "where not to, what to submit"), H_RD)]
    cols = ""
    for i, (src, h, d, c) in enumerate(parts):
        s = ui(src[3:]) if src.startswith("ui:") else img(src)
        arrow = '<div class="jarrow">➔</div>' if i < len(parts) - 1 else ""
        cols += (f'<div class="jcol"><div class="jimg" style="border-color:{c}"><img src="{s}" alt=""></div>'
                 f'<div class="jn" style="color:{c}">{t("Часть", "Part")} {i + 1}</div><div class="jh">{h}</div><div class="jd">{d}</div></div>{arrow}')
    body = f"""<div class="journey">{cols}</div>
      <div style="margin-top:48px">{note(t("Красивая картинка получается и от случайного промпта. <b>Нужная</b> — когда решения про объект, кадр, свет и стиль принимаете вы, а результат правите, а не генерируете заново.",
                                           "A pretty picture comes even from a random prompt. The one you <b>need</b> comes when you decide on subject, framing, light and style, and edit the result instead of regenerating it."))}</div>"""
    return S(t("План на 90 минут", "Plan for 90 minutes"), t("Пять частей урока", "Five parts of the lesson"), body, v2.v1.s03()["notes"])


# ---------------------------------------------------------------- 5 services with interfaces
def s05():
    data = [("ChatGPT", "GPT Image 2 ➔ Images 2.5", t("текст на картинке, правки диалогом", "text in images, conversational edits"), logo_tile(), H_CY),
            ("Nano Banana", "Gemini • Nano Banana 2 / Pro", t("референсы и консистентность", "references and consistency"), shot(ui("gemini")), H_GR),
            ("Midjourney", "V8.2 + Edit Model", t("эстетика и стиль", "aesthetics and style"), shot(ui("midjourney")), H_VI),
            ("Kling", "IMAGE 3.0 • Omni", t("серии кадров, мост к видео", "image series, bridge to video"), shot(ui("kling")), H_AM),
            ("Grok Imagine", "Image 2.0", t("правка выделением, шаблоны", "region edits, templates"), shot(ui("grok")), H_RD)]
    cols = "".join(f'<div class="svc2" style="--k:{c}"><div class="svc2-img">{vis}</div><div class="name">{n}</div><div class="model">{m}</div><div class="best">{b}</div></div>'
                   for n, m, b, vis, c in data)
    body = f"""<div class="svc2-row">{cols}</div>
      <div style="margin-top:26px">{note(t("Все пятеро умеют текст ➔ картинку, правку и референсы. Отличаются характером. Версии меняются каждые 2–3 месяца.", "All five do text ➔ image, edits and references. They differ in character. Versions change every 2–3 months."))}</div>"""
    return S(t("Часть 2 • Сервисы • октябрь 2026", "Part 2 • Services • October 2026"), t("Пять сервисов: кто для чего", "Five services: which one for what"), body, sv.s_map()["notes"])


def svc_visual(kicker, title, k, visual, bullets, prompt_label, prompt, notes, extra=""):
    body = f"""<div class="row" style="grid-template-columns:1.05fr 1fr;gap:56px;">
      {visual}
      <div class="stack center">{ul(bullets, k)}<div><div class="prompt-label">{prompt_label}</div><div class="prompt" style="font-size:19px;">{prompt}</div></div>{extra}</div></div>"""
    return S(kicker, title, body, notes, k=k)


def s06():
    visual = f"""<div class="stack" style="gap:16px;">{logo_tile()}<div class="cap" style="font-size:20px;color:var(--muted)">chatgpt.com • {t("раздел Images", "Images section")}</div></div>"""
    return svc_visual(t("Сервис 1 • ChatGPT Images", "Service 1 • ChatGPT Images"), t("ChatGPT: сначала думает, потом рисует", "ChatGPT: thinks first, then draws"), CY, visual,
                      [t("<b>Рассуждает перед генерацией:</b> планирует композицию и текст", "<b>Reasons before generating:</b> plans layout and text"),
                       t("<b>Лучший текст на картинке,</b> включая кириллицу", "<b>Best text rendering,</b> including Cyrillic"),
                       t("<b>Правки диалогом;</b> в 2.5 — комментарий к области", "<b>Conversational edits;</b> 2.5 adds region comments")],
                      t("Порядок OpenAI: сцена ➔ объект ➔ детали ➔ ограничения", "OpenAI order: scene ➔ subject ➔ details ➔ constraints"),
                      t("<span class='s'>Сцена:</span> ночной город, постер 4:5\n<span class='s'>Объект:</span> ноутбук с редактором кода\n<span class='m'>Текст ровно:</span> \"GenAI Basics • Урок 04\"\n<span class='x'>Нельзя:</span> логотипы, ошибки в тексте",
                        "<span class='s'>Scene:</span> night city, 4:5 poster\n<span class='s'>Subject:</span> a laptop with a code editor\n<span class='m'>Exact text:</span> \"GenAI Basics • Lesson 04\"\n<span class='x'>Never:</span> logos, misspelled text"),
                      sv.s_chatgpt()["notes"])


def s07():
    visual = shot(ui("gemini"), t("gemini.google.com — Nano Banana внутри Gemini", "gemini.google.com — Nano Banana inside Gemini"))
    return svc_visual(t("Сервис 2 • Nano Banana (Gemini)", "Service 2 • Nano Banana (Gemini)"), t("Nano Banana: референсы и точечные правки", "Nano Banana: references and targeted edits"), GR, visual,
                      [t("<b>Все картинки урока</b> сделаны Nano Banana Pro", "<b>Every image in this lesson</b> is Nano Banana Pro"),
                       t("<b>Много референсов сразу:</b> персонаж + товар + фон", "<b>Many references:</b> character + product + background"),
                       t("<b>Правка без маски:</b> модель сама находит «кружку»", "<b>Mask-free edits:</b> the model finds \"the mug\" itself")],
                      t("Формула Google: картинки + связь + новая сцена", "Google's formula: images + relationship + new scene"),
                      t("<span class='s'>Картинка 1</span> — персонаж, <span class='s'>картинка 2</span> — товар.\nТот же курьер пьет из той самой кружки.",
                        "<span class='s'>Image 1</span> is the character, <span class='s'>image 2</span> the product.\nThe same courier drinks from exactly that mug."),
                      sv.s_nano()["notes"])


def s08():
    rows = [("--ar 4:5", t("формат", "aspect")), ("--s 0–1000", t("сила эстетики MJ", "MJ aesthetic strength")), ("--c 0–100", t("разброс вариантов", "variety")),
            ("--raw", t("буквальнее", "more literal")), ("--sref", t("референс стиля", "style reference")), ("--no", t("исключить", "exclude")),
            ("Edit", t("до 4 референсов", "up to 4 references"))]
    tbl = '<table class="t compact">' + "".join(f"<tr><td><code>{a}</code></td><td>{b}</td></tr>" for a, b in rows) + "</table>"
    body = f"""<div class="row" style="grid-template-columns:0.9fr 1.1fr;gap:56px;">
      {shot(ui("midjourney"), t("updates.midjourney.com: Edit Model — референс ➔ новые сцены", "updates.midjourney.com: Edit Model — reference ➔ new scenes"))}
      <div class="stack center">{tbl}<div class="prompt" style="font-size:18px;">editorial photo of a speckled mug, morning light <span class="m">--ar 4:5 --s 250 --raw --no text</span></div></div></div>"""
    return S(t("Сервис 3 • Midjourney V8.2", "Service 3 • Midjourney V8.2"), t("Midjourney: короткий промпт + параметры", "Midjourney: short prompt + parameters"), body, sv.s_midjourney()["notes"], k=VI)


def s09():
    body = f"""<div class="row c2" style="gap:48px;">
      <div class="stack" style="gap:18px;">{shot(ui("kling"), "app.klingai.com")}
        {ul([t("<b>Картинка — первый кадр</b> для видео (L05)", "<b>An image is the first frame</b> for video (L05)"), t("<b>До 10 референсов,</b> режим серии", "<b>Up to 10 references,</b> series mode")], AM)}</div>
      <div class="stack" style="gap:18px;">{shot(ui("grok"), "grok.com/imagine")}
        {ul([t("<b>Magic Wand:</b> выделил область ➔ описал правку", "<b>Magic Wand:</b> select a region ➔ describe the edit"), t("<b>Риск:</b> скандал с дипфейками, январь 2026", "<b>Risk:</b> deepfake scandal, January 2026")], RD)}</div></div>"""
    return S(t("Сервисы 4–5", "Services 4–5"), t("Kling — мост к видео. Grok — правка выделением", "Kling bridges to video. Grok edits by selection"), body, sv.s_kling_grok()["notes"])


# ---------------------------------------------------------------- 10 radar small multiples
def s10():
    labels = [t("Текст", "Text"), t("Инструкции", "Instructions"), t("Правки", "Edits"), t("Консистентн.", "Consistency"), t("Эстетика", "Aesthetics"), "API"]
    data = [("ChatGPT", [3, 3, 3, 2, 2, 3], H_CY), ("Nano Banana", [3, 3, 3, 3, 2, 3], H_GR), ("Midjourney", [2, 2, 2, 2, 3, 1], H_VI),
            ("Kling", [2, 2, 3, 3, 2, 3], H_AM), ("Grok", [2, 2, 3, 2, 2, 3], H_RD)]
    cells = "".join(f'<div class="radar"><div class="radar-t" style="color:{c}">{n}</div>{ch.radar(s, labels, c, n)}</div>' for n, s, c in data)
    pick = f"""<div class="stack center" style="gap:22px;padding-left:20px;">{pt(t("Постер, слайд, инфографика", "Poster, slide, infographic"), "➔ ChatGPT", CY)}{pt(t("Серия с одним героем", "Series with one hero"), "➔ Nano Banana / Kling", GR)}{pt(t("Мудборд, стиль", "Moodboard, style"), "➔ Midjourney", VI)}</div>"""
    body = f"""<div class="radars">{cells}{pick}</div>"""
    return S(t("Сравнение • оценка преподавателя по 3-балльной шкале, не бенчмарк", "Comparison • instructor's 3-point rating, not a benchmark"), t("Профиль каждого сервиса", "Each service's profile"), body, sv.s_matrix()["notes"])


# ---------------------------------------------------------------- 11–12 annotated images
def s11():
    marks = [(12, 32, t("дождь", "rain"), H_AM), (29, 55, t("люди", "people"), H_AM), (22, 50, t("кот", "cat"), H_AM), (93, 72, t("камин", "fireplace"), H_AM), (73, 38, t("бариста", "barista"), H_AM)]
    body = f"""<div class="row" style="grid-template-columns:1.75fr 1fr;gap:44px;">
      <div class="pic"><div class="frame">{ch.annotated(img("A1_free"), 1376, 768, marks)}</div></div>
      <div class="stack center"><div class="prompt-label">{t("Весь промпт", "The whole prompt")}</div><div class="prompt" style="font-size:22px;">a cozy coffee shop in the morning</div>
        <div class="say" style="font-size:30px;">{t("Утро? За окном дождь. Людей, кота и камин <em>никто не просил</em> — модель заполнила пустоты сама.", "Morning? It's raining. Nobody <em>asked for</em> the people, the cat or the fireplace — the model filled the gaps.")}</div></div></div>"""
    return S(t("Часть 3 • Промпт • шаг 1", "Part 3 • Prompt • step 1"), t("Шесть слов — и все решения принимает модель", "Six words, and the model makes every decision"), body, pr.s_free()["notes"], k=AM)


def s12():
    marks = [(72, 72, t("объект", "subject"), H_CY), (52, 30, t("сцена", "setting"), H_CY), (18, 70, t("камера: размытие", "camera: blur"), H_CY), (10, 22, t("свет слева", "light: left"), H_CY)]
    p = t("<span class='s'>1 Объект:</span> крапчатая кружка с паром, правая треть\n<span class='s'>2 Сцена:</span> пустая кофейня, 7 утра, стулья на столах\n<span class='s'>3 Камера:</span> уровень глаз, 35 мм, f/2.0\n<span class='s'>4 Свет:</span> низкое солнце из окна слева\n<span class='s'>  Стиль:</span> редакционное фото\n<span class='x'>  Запреты:</span> без людей и текста",
          "<span class='s'>1 Subject:</span> a speckled mug with steam, right third\n<span class='s'>2 Setting:</span> empty café, 7 a.m., chairs up\n<span class='s'>3 Camera:</span> eye-level, 35mm, f/2.0\n<span class='s'>4 Light:</span> low sun from the left window\n<span class='s'>  Style:</span> editorial photo\n<span class='x'>  Constraints:</span> no people, no text")
    body = f"""<div class="row" style="grid-template-columns:1fr 1.6fr;gap:44px;"><div class="stack center"><div class="prompt" style="font-size:19px;">{p}</div>{note(t("Номера в промпте = метки на картинке", "Numbers in the prompt = marks on the image"), GR)}</div>
      <div class="pic"><div class="frame">{ch.annotated(img("A2_structured"), 1376, 768, marks)}</div></div></div>"""
    return S(t("Часть 3 • Промпт • шаг 2", "Part 3 • Prompt • step 2"), t("Шесть слотов — и решения принимаете вы", "Six slots, and you make the decisions"), body, pr.s_struct()["notes"], k=GR)


# ---------------------------------------------------------------- 14 vocabulary as images
def s14():
    items = [("V1_low", "low angle", t("снизу — «героично»", "from below: heroic")), ("V2_top", "top-down", t("сверху — схема, флэтлей", "from above: layout, flat lay")),
             ("V3_wide", "24mm wide", t("герой + окружение", "subject + surroundings")), ("V4_85", "85mm f/1.8", t("портрет, размытый фон", "portrait, blurred background")),
             ("V5_golden", "golden hour", t("теплый контровой свет", "warm backlight")), ("V6_studio", "softbox studio", t("ровный студийный свет", "even studio light"))]
    cells = "".join(f'<div class="pic cover"><div class="frame"><img src="{img(n)}" alt=""></div><div class="cap"><code>{term}</code> {d}</div></div>' for n, term, d in items)
    body = f"""<div class="row c3" style="grid-template-rows:1fr 1fr;gap:18px 26px;">{cells}</div>"""
    return S(t("Часть 3 • Словарь фотографа", "Part 3 • Photographer's vocabulary"), t("Одна героиня — шесть слов камеры и света", "One character, six camera and light words"), body, pr.s_vocab()["notes"])


# ---------------------------------------------------------------- 16 iteration loop diagram
def s16():
    steps = [(t("Черновик", "Draft"), t("2–4 варианта", "2–4 candidates")), (t("Выбор", "Pick"), t("по must-have", "by must-haves")),
             (t("Одна правка", "One edit"), t("«только X»", "\"only X\"")), (t("Проверка", "Check"), t("что уплыло?", "what drifted?")),
             (t("Финал", "Final"), t("сохранить промпт", "save the prompt"))]
    tpl = t("Отредактируй фото. Замени <span class='m'>только</span> X на Y.\n<span class='g'>Сохрани:</span> ракурс, кадр, фон, свет и тени.",
            "Edit this photo. Replace <span class='m'>only</span> X with Y.\n<span class='g'>Keep:</span> angle, framing, background, light, shadows.")
    body = f"""<div class="row" style="grid-template-columns:1.1fr 1fr;gap:40px;">
      <div style="min-height:0;display:flex;align-items:center;">{ch.loop(steps, [H_CY, H_CY, H_GR, H_AM, H_VI])}</div>
      <div class="stack center"><div class="prompt-label">{t("Шаблон правки", "Edit template")}</div><div class="prompt" style="font-size:20px;">{tpl}</div>
        {ul([t("<b>Одна правка за шаг</b>", "<b>One edit per turn</b>"), t("<b>Называйте, что сохранить</b>", "<b>Name what to keep</b>"), t("<b>6–8 правок</b> — новый чат с лучшей картинкой", "<b>After 6–8 edits</b> start a new chat")], GR)}</div></div>"""
    return S(t("Часть 3 • Промпт • шаг 4", "Part 3 • Prompt • step 4"), t("Правим по кругу, а не перегенерируем", "Iterate in a loop, do not regenerate"), body, pr.s_iterate()["notes"], k=GR)


# ---------------------------------------------------------------- 19 consistency: flow + bar chart
def s19():
    flow = f"""<div class="mflow"><div class="mref">{pic("C1_sheet", t("мастер-референс", "master reference"))}</div>
      <div class="mfan"><svg viewBox="0 0 80 300" preserveAspectRatio="none" style="width:100%;height:100%"><path d="M0,150 C40,150 40,40 78,40 M0,150 L78,150 M0,150 C40,150 40,260 78,260" stroke="#38bdf8" stroke-width="3" fill="none"/></svg></div>
      <div class="mout">{pic("C2_rain", cover=True)}{pic("C3_door", cover=True)}{pic("C4_break", cover=True)}</div></div>"""
    bars = ch.hbars([("Nano Banana 2", 14, H_GR, t("объектов", "objects")), ("Kling", 10, H_AM, ""), ("Grok", 5, H_RD, ""), ("Midjourney", 4, H_VI, "Edit Model")])
    body = f"""<div class="row" style="grid-template-columns:1.1fr 1fr;gap:56px;">
      <div class="stack" style="gap:14px;">{flow}<div class="prompt" style="font-size:17px;">{t("референс + <span class='s'>4–6 примет словами</span> + новое действие", "reference + <span class='s'>4–6 traits in words</span> + new action")}</div></div>
      <div class="stack center"><div class="prompt-label">{t("Сколько референсов можно приложить", "How many references you can attach")}</div>{bars}
        {note(t("ChatGPT: несколько картинок в одном сообщении + тот же чат. Лимиты меняются с версиями.", "ChatGPT: several images per message + the same chat. Limits change with versions."))}</div></div>"""
    return S(t("Часть 4 • Паттерн 2", "Part 4 • Pattern 2"), t("Рецепт один, кнопки разные", "One recipe, different buttons"), body, pat.s_consistency_how()["notes"])


# ---------------------------------------------------------------- 22 API pipeline
def s22():
    pipe = ch.pipeline([(t("Таблица", "Table"), t("товар, сцена, формат", "product, scene, format"), H_AM),
                        (t("Шаблон промпта", "Prompt template"), "build_prompt(spec)", H_CY),
                        ("Gemini API", "generate_content", H_GR),
                        (t("Картинки", "Images"), "out/*.png", H_VI),
                        (t("Журнал", "Log"), "prompts.md", H_CY)])
    code = """resp = client.models.<span class="fn">generate_content</span>(
    model=<span class="str">"gemini-3.1-flash-image"</span>,
    contents=[sheet, PROMPT],      <span class="cm"># reference + text</span>
    config=types.<span class="fn">GenerateContentConfig</span>(
        response_modalities=[<span class="str">"IMAGE"</span>]))
resp.parts[0].<span class="fn">as_image</span>().<span class="fn">save</span>(<span class="str">"scene.png"</span>)"""
    body = f"""<div class="stack" style="gap:40px;flex:1;justify-content:center;">{pipe}
      <div class="row" style="grid-template-columns:1.3fr 1fr;gap:48px;flex:0 0 auto;"><pre class="code" style="font-size:19px;">{code}</pre>
      <div class="stack center">{pt(t("50 карточек за минуты", "50 cards in minutes"), t("вместо дня ручной работы в чате", "instead of a day of manual chat work"), GR)}
        {note(t("Colab: <code>L04_Image_Generation_Prompts_and_Patterns.ipynb</code>", "Colab: <code>L04_Image_Generation_Prompts_and_Patterns.ipynb</code>"))}</div></div></div>"""
    return S(t("Часть 5 • То же в коде", "Part 5 • Same thing in code"), t("Серия картинок скриптом — тот же SDK, что в L03", "An image series by script — the same SDK as L03"), body, pat.s_api()["notes"])


# ---------------------------------------------------------------- 23 risks + traffic light
def s23():
    light = ch.traffic([(t("ЗЕЛЕНАЯ • САМИ", "GREEN • GO"), t("мудборды, иллюстрации к слайдам, раскадровки", "moodboards, slide art, storyboards"), H_GR),
                        (t("ЖЕЛТАЯ • ПРОВЕРЯЕТ ЧЕЛОВЕК", "YELLOW • HUMAN REVIEWS"), t("карточки товаров, баннеры, обложки YouTube", "product cards, banners, YouTube thumbnails"), H_AM),
                        (t("КРАСНАЯ • НЕ ГЕНЕРИРУЕМ", "RED • DO NOT GENERATE"), t("документы, упаковка с составом, чужие логотипы, реальные люди без согласия", "documents, packaging with ingredients, others' logos, real people without consent"), H_RD)])
    risks = ul([t("<b>Мелкий текст, руки в толпе</b> — ломаются", "<b>Small text, hands in crowds</b> break"),
                t("<b>Дрейф</b> лица и цвета после многих правок", "<b>Drift</b> of faces and colors after many edits"),
                t("<b>Цифры в инфографике</b> бывают выдуманными", "<b>Numbers in infographics</b> can be made up"),
                t("<b>Права:</b> картинка только по промпту не охраняется (США)", "<b>Rights:</b> prompt-only images are not copyrightable (US)"),
                t("<b>Водяные знаки:</b> SynthID и C2PA", "<b>Provenance:</b> SynthID and C2PA")], AM)
    body = f'<div class="row" style="grid-template-columns:1fr 1.05fr;gap:56px;"><div class="stack center">{risks}</div><div style="min-height:0;display:flex;align-items:center;">{light}</div></div>'
    return S(t("Часть 5 • Риски • Blast Radius", "Part 5 • Risks • Blast Radius"), t("Где генерация подводит и где ее нельзя применять", "Where generation fails and where not to use it"), body, pat.s_risks()["notes"], k=AM)


# ---------------------------------------------------------------- 24 homework: tracks with thumbnails + folder tree
def s24():
    trackA = f"""<div class="track" style="--k:var(--cyan)"><div class="pt"><div class="h"><span class="mark">{t("Трек А", "Track A")}</span> • {t("фотосессия товара", "product shoot")}</div><div class="d">{t("свой предмет ➔ 4 кадра", "your object ➔ 4 shots")}</div></div>
      <div class="thumbs">{''.join(f'<img src="{img(n)}" alt="">' for n in ["D0_packshot", "D1_kitchen", "D2_flatlay", "D4_banner"])}</div></div>"""
    trackB = f"""<div class="track" style="--k:var(--green)"><div class="pt"><div class="h"><span class="mark">{t("Трек Б", "Track B")}</span> • {t("курьер доставки", "delivery courier")}</div><div class="d">{t("лист ➔ 3 сцены ➔ 1 правка", "sheet ➔ 3 scenes ➔ 1 edit")}</div></div>
      <div class="thumbs">{''.join(f'<img src="{img(n)}" alt="">' for n in ["C1_sheet", "C2_rain", "C3_door", "C4_break"])}</div></div>"""
    folder = ch.tree([(0, "genai-homeworks/", "", H_CY), (1, "L04/", "", H_CY),
                      (2, "images/", t("01_free.png, 02_structured.png …", "01_free.png, 02_structured.png …"), H_GR),
                      (2, "prompts.md", t("промпт к каждой картинке", "a prompt per image"), H_AM),
                      (2, "qa.md", t("что сохранилось, что уплыло", "what held, what drifted"), H_AM)])
    body = f"""<div class="row" style="grid-template-columns:1.25fr 1fr;gap:56px;">
      <div class="stack center" style="gap:30px;">{trackA}{trackB}</div>
      <div class="stack center" style="gap:26px;">{folder}{note(t("Обязательно: один кадр свободным и структурным промптом + один промпт в двух сервисах. Шаблоны — <code>L04_05_Homework.md</code>", "Required: one shot with a free-form and a structured prompt + one prompt in two services. Templates: <code>L04_05_Homework_EN.md</code>"))}</div></div>"""
    return S(t("Домашнее задание №4", "Homework #4"), t("Фотосессия товара или персонаж-курьер", "A product photo shoot or a courier character"), body, pat.s_homework()["notes"])


SLIDES = [v2.s01, v2.s02, s03, v2.s04, s05, s06, s07, s08, s09, s10, s11, s12, v2.s13, s14, v2.s15,
          s16, v2.s17, v2.s18, s19, v2.s20, v2.s21, s22, s23, s24, v2.s25]
