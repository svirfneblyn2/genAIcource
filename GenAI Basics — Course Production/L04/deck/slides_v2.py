"""L04 deck v2 content: one idea per slide, short text, big images.
Every string is a t(ru, en) pair. Speaker notes are reused from the v1 slide modules."""

import slides as v1
import slides_patterns as pat
import slides_prompts as pr
import slides_services as sv
from slides import t


def img(name: str) -> str:
    return f"assets/examples/web/{name}.jpg"


def pic(name, cap="", cover=False, tag="", k=""):
    tg = f'<span class="tag"{f" style=--k:{k}" if k else ""}>{tag}</span>' if tag else ""
    c = f'<div class="cap">{tg}{cap}</div>' if (cap or tag) else ""
    return f'<div class="pic{" cover" if cover else ""}"><div class="frame"><img src="{img(name)}" alt="{name}"></div>{c}</div>'


def pt(h, d="", k=""):
    style = f' style="--k:{k}"' if k else ""
    return f'<div class="pt"{style}><div class="h">{h}</div>{f"<div class=d>{d}</div>" if d else ""}</div>'


def ul(items, k=""):
    style = f' style="--k:{k}"' if k else ""
    return f'<ul class="list"{style}>' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def note(text, k=""):
    style = f' style="--k:{k}"' if k else ""
    return f'<div class="note"{style}>{text}</div>'


def steps(items, k=""):
    style = f' style="--k:{k};grid-template-columns:repeat({len(items)},1fr)"'
    return f'<div class="steps"{style}>' + "".join(
        f'<div class="step"><div class="n">{i + 1:02d}</div><div class="h">{h}</div><div class="d">{d}</div></div>'
        for i, (h, d) in enumerate(items)) + "</div>"


CY, GR, AM, RD, VI = "var(--cyan)", "var(--green)", "var(--amber)", "var(--red)", "var(--violet)"


def S(kicker, title, body, notes, lead="", k=""):
    return dict(kicker=kicker, title=title, lead=lead, body=body, notes=notes, k=k)


# ---------------------------------------------------------------- 1 title
def s01():
    tiles = "".join(f'<img src="{img(n)}" alt="">' for n in
                    ["A2_structured", "C2_rain", "D2_flatlay", "B2_relight", "C4_break", "D4_banner", "E1_compose", "E2_style"])
    return dict(raw=True, cls="cover", notes=v1.s01()["notes"], title_text=t("Генерация изображений", "Image Generation"),
                body=f"""<div class="mosaic">{tiles}</div><div class="shade"></div>
      <div class="txt">
        <div class="kicker">{t("GenAI Basics • Урок 04 • Модуль 2: мультимодальность", "GenAI Basics • Lesson 04 • Module 2: multimodality")}</div>
        <h1>{t("Генерация изображений", "Image Generation")}</h1>
        <h2>{t("Сервисы, промпт-техники и паттерны контроля", "Services, prompt techniques and control patterns")}</h2>
        <p>{t("ChatGPT, Nano Banana, Midjourney, Kling и Grok. От свободного промпта — к фотосессии товара и персонажу, который узнаваем в каждом кадре. Все картинки урока — реальные генерации, промпты в <code>examples/prompts.json</code>.",
              "ChatGPT, Nano Banana, Midjourney, Kling and Grok. From a free-form prompt to a product photo shoot and a character that stays recognizable in every shot. Every image is a real generation; prompts are in <code>examples/prompts.json</code>.")}</p>
      </div>
      <div class="keys">{t("← → листать • N заметки • G все слайды • F полный экран", "← → navigate • N notes • G all slides • F fullscreen")}</div>""")


# ---------------------------------------------------------------- 2 roadmap
def s02():
    mods = [("01", t("Основы и API", "Foundations & API"), "L01–L03", "done"),
            ("02", t("Мультимодальность", "Multimodality"), t("L04 картинки<br>L05 видео • L06 звук", "L04 images<br>L05 video • L06 audio"), "here"),
            ("03", t("Среда инженера", "Engineer's toolkit"), "L07–L09", "future"),
            ("04", t("Локальный AI", "Local AI"), "L10", "future"),
            ("05", t("Агенты и MCP", "Agents & MCP"), "L11–L13", "future"),
            ("06", t("Продакшен", "Production"), "L14–L16", "future")]
    road = "".join(f'<div class="m {st}"><div class="dot">{n}</div><div class="nm">{nm}</div><div class="sub">{sub}</div></div>' for n, nm, sub, st in mods)
    body = f"""<div class="road">{road}</div><div style="margin-top:90px">{note(t(
        "<b>Что переносится из L02–L03:</b> конкретика, структура и примеры работают и для картинок. Только вместо примеров текста — референс-изображения.",
        "<b>What carries over from L02–L03:</b> specificity, structure and examples work for images too. Instead of text examples you pass reference images."))}</div>"""
    return S(t("Маршрут курса", "Course route"), t("Модуль 1 пройден. Сегодня — картинки", "Module 1 is done. Today: images"), body, v1.s02()["notes"])


# ---------------------------------------------------------------- 3 agenda
def s03():
    items = [(t("Как модель рисует", "How the model draws"), t("две ментальные модели", "two mental models")),
             (t("Пять сервисов", "Five services"), t("кто для чего", "which one for what")),
             (t("Промпт", "The prompt"), t("от одной фразы к структуре", "from one phrase to a structure")),
             (t("Паттерны", "Patterns"), t("правка, персонаж, фотосессия", "edit, character, photo shoot")),
             (t("Риски и домашка", "Risks & homework"), t("где нельзя и что сдать", "where not to use it, what to submit"))]
    body = f"""<div class="row" style="grid-template-columns:1fr 1.1fr;gap:64px;">
      <div class="stack center">{steps(items[:3])}<div style="height:24px"></div>{steps(items[3:])}</div>
      <div class="stack center"><div class="say">{t("Красивая картинка получается и от случайного промпта. <em>Нужная</em> — когда решения про объект, кадр, свет и стиль принимаете вы, а результат правите, а не генерируете заново.",
          "A pretty picture comes even from a random prompt. The picture you <em>need</em> comes when you decide on subject, framing, light and style — and edit the result instead of regenerating it.")}</div></div>
    </div>"""
    return S(t("План на 90 минут", "Plan for 90 minutes"), t("Сначала понимаем инструмент, потом управляем им", "First understand the tool, then control it"), body, v1.s03()["notes"])


# ---------------------------------------------------------------- 4 mental model
def s04():
    frames = "".join(f'<div class="pic"><div class="frame"><img src="{img(f"denoise_{i}")}" alt=""></div><div class="cap">{c}</div></div>'
                     for i, c in enumerate([t("шаг 0: чистый шум", "step 0: pure noise"), t("проявляются формы", "shapes emerge"),
                                            t("детали", "details"), t("готово", "done")]))
    body = f"""<div class="stack" style="gap:30px;flex:1">
      <div style="display:grid;grid-template-columns:340px 1fr;gap:36px;align-items:stretch;flex:1;min-height:0;">
        {pt(t("Диффузия", "Diffusion"), t("Midjourney, FLUX, Stable Diffusion. Картинка «проявляется» из шума, текст подсказывает направление. Новый запуск — новый шум.", "Midjourney, FLUX, Stable Diffusion. The image emerges from noise; text steers it. New run, new noise."), AM)}
        <div class="row c4" style="gap:14px;height:100%;">{frames}</div>
      </div>
      <div style="display:grid;grid-template-columns:340px 1fr;gap:36px;align-items:stretch;flex:1;min-height:0;">
        {pt(t("Чат-модели", "Chat models"), t("ChatGPT, Nano Banana, Grok. Мультимодальная LLM читает весь диалог и прошлые картинки.", "ChatGPT, Nano Banana, Grok. A multimodal LLM reads the whole chat and earlier images."), GR)}
        <div style="display:grid;grid-template-columns:1fr 1.1fr 1fr;gap:20px;height:100%;min-height:0;">
          {pic("A2_structured", t("картинка из диалога", "image from the chat"))}
          <div class="prompt" style="font-size:20px;align-self:center;">{t("«Замени <span class='m'>только</span> кружку на айс-латте. Остальное <span class='g'>не трогай</span>»", "\"Replace <span class='m'>only</span> the mug with an iced latte. <span class='g'>Keep everything else</span>\"")}</div>
          {pic("B1_replace", t("правка точечная", "targeted edit"))}
        </div>
      </div></div>"""
    return S(t("Часть 1 • Ментальная модель", "Part 1 • Mental model"),
             t("Два способа нарисовать картинку", "Two ways to draw an image"), body, v1.s04()["notes"])


# ---------------------------------------------------------------- 5 services map
def s05():
    data = [("ChatGPT", "GPT Image 2 ➔ Images 2.5", t("Текст на картинке, инфографика, правки диалогом", "Text in images, infographics, conversational edits"), t("чат ChatGPT • OpenAI API", "ChatGPT chat • OpenAI API"), CY),
            ("Nano Banana", "Nano Banana 2 • Pro • 2 Lite", t("Несколько референсов, консистентность, дешевый API", "Multiple references, consistency, cheap API"), t("приложение Gemini • AI Studio • API", "Gemini app • AI Studio • API"), GR),
            ("Midjourney", "V8.2 + Edit Model", t("Эстетика и поиск стиля «из коробки»", "Aesthetics and style exploration out of the box"), t("сайт и Discord • от $10/мес • нет API", "web & Discord • from $10/mo • no API"), VI),
            ("Kling", "IMAGE 3.0 • Omni • O1", t("Серии кадров и раскадровки, мост в видео", "Image series and storyboards, bridge to video"), t("kling.ai • API", "kling.ai • API"), AM),
            ("Grok Imagine", "Image 2.0", t("Правка выделением, шаблоны товара и портрета", "Region edits, product and headshot templates"), t("grok.com • приложение • API", "grok.com • app • API"), RD)]
    cols = "".join(f'<div class="svc" style="--k:{k}"><div class="name">{n}</div><div class="model">{m}</div><div class="best">{b}</div><div class="where">{w}</div></div>' for n, m, b, w, k in data)
    body = f"""<div class="row c5" style="gap:36px;flex:0 0 auto;height:470px;">{cols}</div>
      <div style="margin-top:auto">{note(t("Все пятеро умеют текст ➔ картинку, правку и референсы. Отличаются характером. Версии меняются каждые 2–3 месяца — проверяйте перед работой.", "All five do text ➔ image, edits and references. They differ in character. Versions change every 2–3 months — check before you start."))}</div>"""
    return S(t("Часть 2 • Сервисы • октябрь 2026", "Part 2 • Services • October 2026"), t("Пять сервисов: кто для чего", "Five services: which one for what"), body, sv.s_map()["notes"])


def svc(kicker, title, k, bullets, prompt_label, prompt, notes, lead="", side=""):
    right = f'<div class="stack center"><div class="prompt-label">{prompt_label}</div><div class="prompt">{prompt}</div>{side}</div>'
    body = f'<div class="row c2" style="gap:64px;"><div class="stack center">{ul(bullets, k)}</div>{right}</div>'
    return S(kicker, title, body, notes, lead, k)


# ---------------------------------------------------------------- 6–9 services
def s06():
    return svc(t("Сервис 1 • ChatGPT Images", "Service 1 • ChatGPT Images"), t("ChatGPT: сначала думает, потом рисует", "ChatGPT: thinks first, then draws"), CY,
               [t("<b>Рассуждает перед генерацией</b> — планирует композицию и текст", "<b>Reasons before generating</b> — plans layout and text"),
                t("<b>Лучший текст на картинке,</b> включая кириллицу: постеры, меню, слайды", "<b>Best text rendering,</b> including Cyrillic: posters, menus, slides"),
                t("<b>Правки диалогом;</b> в 2.5 — комментарий к области картинки", "<b>Conversational edits;</b> 2.5 adds comments on an image region"),
                t("<b>Слабее</b> в «чистой эстетике», чем Midjourney", "<b>Weaker</b> than Midjourney on pure aesthetics")],
               t("Порядок из гайда OpenAI: сцена ➔ объект ➔ детали ➔ ограничения", "OpenAI guide order: scene ➔ subject ➔ details ➔ constraints"),
               t("<span class='s'>Сцена:</span> ночной город в синих тонах, постер 4:5\n<span class='s'>Объект:</span> ноутбук с открытым редактором кода\n<span class='m'>Текст ровно:</span> \"GenAI Basics • Урок 04\"\n<span class='x'>Нельзя:</span> логотипы, ошибки в тексте",
                 "<span class='s'>Scene:</span> night city in blue tones, 4:5 poster\n<span class='s'>Subject:</span> a laptop with a code editor open\n<span class='m'>Exact text:</span> \"GenAI Basics • Lesson 04\"\n<span class='x'>Never:</span> logos, misspelled text"),
               sv.s_chatgpt()["notes"])


def s07():
    return svc(t("Сервис 2 • Nano Banana (Gemini)", "Service 2 • Nano Banana (Gemini)"), t("Nano Banana: референсы и точечные правки", "Nano Banana: references and targeted edits"), GR,
               [t("<b>Все картинки этого урока</b> сделаны Nano Banana Pro", "<b>Every image in this lesson</b> was made with Nano Banana Pro"),
                t("<b>Много референсов сразу:</b> персонаж + товар + фон", "<b>Many references at once:</b> character + product + background"),
                t("<b>Правка без маски:</b> модель сама находит «кружку», «фон», «небо»", "<b>Mask-free edits:</b> the model finds \"the mug\", \"the background\", \"the sky\""),
                t("<b>Тот же SDK, что в L03:</b> <code>gemini-3.1-flash-image</code>", "<b>Same SDK as L03:</b> <code>gemini-3.1-flash-image</code>")],
               t("Формула Google: картинки + связь между ними + новая сцена", "Google's formula: images + relationship + new scene"),
               t("<span class='s'>Картинка 1</span> — персонаж, <span class='s'>картинка 2</span> — товар.\nТот же курьер из картинки 1 пьет\nиз той самой кружки с картинки 2.\nУтренний свет, 35 мм, фото.",
                 "<span class='s'>Image 1</span> is the character, <span class='s'>image 2</span> the product.\nThe same courier from image 1 drinks\nfrom exactly the mug in image 2.\nMorning light, 35mm, photo."),
               sv.s_nano()["notes"],
               side=note(t("Пишите сценой, а не списком слов, и позитивно: «пустая улица», а не «без машин».", "Describe a scene, not a keyword list, and phrase positively: \"an empty street\", not \"no cars\"."), GR))


def s08():
    rows = [("--ar 4:5", t("формат кадра", "aspect ratio")), ("--s 0–1000", t("сколько «своей эстетики» добавить", "how much MJ aesthetic to add")),
            ("--c 0–100", t("насколько разные 4 варианта", "how different the 4 variants are")), ("--raw", t("буквальнее к промпту", "more literal")),
            ("--sref", t("референс стиля", "style reference")), ("--no", t("чего не должно быть", "what must not appear")),
            ("--seed", t("повторить стартовый шум", "repeat the starting noise")), ("Edit", t("правка с референсами (вместо --cref/--oref)", "edit with references (replaces --cref/--oref)"))]
    tbl = '<table class="t">' + "".join(f"<tr><td><code>{a}</code></td><td>{b}</td></tr>" for a, b in rows) + "</table>"
    left = f"""<div class="stack center">{ul([t("<b>Эстетика из коробки</b> даже от короткого промпта", "<b>Aesthetics out of the box</b> even from a short prompt"),
        t("<b>Управление параметрами</b> в конце промпта", "<b>Control via parameters</b> at the end of the prompt"),
        t("<b>Нет официального API,</b> текст слабее", "<b>No official API,</b> weaker text")], VI)}
      <div class="prompt">editorial photo of a speckled mug on oak, morning window light <span class="m">--ar 4:5 --s 250 --raw --no text</span></div></div>"""
    body = f'<div class="row c2" style="gap:64px;">{left}<div class="stack center">{tbl}</div></div>'
    return S(t("Сервис 3 • Midjourney V8.2", "Service 3 • Midjourney V8.2"), t("Midjourney: короткий промпт + параметры", "Midjourney: short prompt + parameters"), body, sv.s_midjourney()["notes"], k=VI)


def s09():
    body = f"""<div class="row c2" style="gap:72px;">
      <div class="stack center" style="--k:{AM}"><div class="svc" style="--k:{AM};border-top-width:4px;"><div class="name">Kling</div><div class="model">IMAGE 3.0 • Omni • O1</div></div>
        {ul([t("<b>Картинка — первый кадр</b> для видео (урок 05)", "<b>An image is the first frame</b> for video (lesson 05)"),
             t("<b>До 10 референсов</b> и режим серии кадров", "<b>Up to 10 references</b> and an image-series mode"),
             t("<b>Понимает кино-термины:</b> план, ракурс, объектив", "<b>Understands cinema terms:</b> shot size, angle, lens")], AM)}
        <div class="prompt" style="font-size:17px;">Keep everything else unchanged, modify the jacket to a red raincoat.</div></div>
      <div class="stack center"><div class="svc" style="--k:{RD};border-top-width:4px;"><div class="name">Grok Imagine</div><div class="model">Image 2.0 • Aurora</div></div>
        {ul([t("<b>Magic Wand:</b> выделили область ➔ описали правку", "<b>Magic Wand:</b> select a region ➔ describe the edit"),
             t("<b>Шаблоны:</b> предметка, портрет, иконки", "<b>Templates:</b> product shots, headshots, icons"),
             t("<b>Риск:</b> мягкие правила ➔ скандал с дипфейками в январе 2026", "<b>Risk:</b> lax rules ➔ deepfake scandal in January 2026")], RD)}
        {note(t("Фото реальных людей и материалы компании — только в сервисах с понятными правилами.", "Photos of real people and company assets only in services with clear rules."), RD)}</div>
    </div>"""
    return S(t("Сервисы 4–5", "Services 4–5"), t("Kling — мост к видео. Grok — правка выделением", "Kling bridges to video. Grok edits by selection"), body, sv.s_kling_grok()["notes"])


def s10():
    def d(n):
        return '<span class="dots">' + "".join(f'<span class="{c}">●</span>' for c in (["on"] * n + ["off"] * (3 - n))) + "</span>"
    rows = [(t("Текст на картинке", "Text in image"), 3, 3, 2, 2, 2), (t("Следует инструкции", "Follows instructions"), 3, 3, 2, 2, 2),
            (t("Правка «только X»", "\"Only X\" edits"), 3, 3, 2, 3, 3), (t("Тот же герой/товар", "Same character/product"), 2, 3, 2, 3, 2),
            (t("Эстетика", "Aesthetics"), 2, 2, 3, 2, 2), (t("API", "API"), 3, 3, 1, 3, 3), (t("Бесплатный старт", "Free tier"), 3, 3, 1, 2, 2)]
    head = "".join(f'<th class="c">{n}</th>' for n in ["ChatGPT", "Nano Banana", "Midjourney", "Kling", "Grok"])
    trs = "".join(f"<tr><td>{r[0]}</td>" + "".join(f'<td class="c">{d(v)}</td>' for v in r[1:]) + "</tr>" for r in rows)
    body = f"""<div class="row" style="grid-template-columns:1.7fr 1fr;gap:56px;">
      <div class="stack center"><table class="t"><tr><th></th>{head}</tr>{trs}</table></div>
      <div class="stack center">{pt(t("Постер, слайд, инфографика", "Poster, slide, infographic"), "➔ ChatGPT", CY)}{pt(t("Серия с одним героем", "A series with one hero"), "➔ Nano Banana / Kling", GR)}{pt(t("Мудборд, стиль, концепт", "Moodboard, style, concept"), "➔ Midjourney", VI)}</div></div>"""
    return S(t("Сравнение • оценка преподавателя, не бенчмарк", "Comparison • instructor's rating, not a benchmark"), t("Выбираем сервис под задачу", "Pick the service for the task"), body, sv.s_matrix()["notes"])


# ---------------------------------------------------------------- 11–14 prompting
def s11():
    body = f"""<div class="row img-l">{pic("A1_free", t("Nano Banana Pro, первая же генерация", "Nano Banana Pro, first generation"))}
      <div class="stack center"><div class="prompt-label">{t("Промпт", "Prompt")}</div><div class="prompt" style="font-size:22px;">a cozy coffee shop in the morning</div>
        <div class="prompt-label" style="margin-top:12px;">{t("Модель решила сама", "The model decided")}</div>
        {ul([t("дождь вместо утреннего солнца", "rain instead of morning sun"), t("посетители и бариста", "guests and a barista"), t("камин, полки, кот", "fireplace, shelves, a cat"), t("общий план, широкий угол", "wide shot, wide angle")], AM)}</div></div>"""
    return S(t("Часть 3 • Промпт • шаг 1", "Part 3 • Prompt • step 1"), t("Шесть слов — и все решения принимает модель", "Six words, and the model makes every decision"), body, pr.s_free()["notes"], k=AM)


def s12():
    p = t("<span class='s'>Объект:</span> крапчатая кружка кофе с паром, в правой трети кадра\n<span class='s'>Сцена:</span> пустая скандинавская кофейня, 7 утра, стулья на столах\n<span class='s'>Камера:</span> уровень глаз, 35 мм, f/2.0\n<span class='s'>Свет:</span> низкое солнце из окна слева\n<span class='s'>Стиль:</span> редакционное фото, легкое зерно\n<span class='x'>Запреты:</span> без людей, текста, логотипов",
          "<span class='s'>Subject:</span> a speckled mug of coffee with steam, right third\n<span class='s'>Setting:</span> empty Scandinavian café, 7 a.m., chairs up\n<span class='s'>Camera:</span> eye-level, 35mm, f/2.0\n<span class='s'>Light:</span> low sun from a window on the left\n<span class='s'>Style:</span> editorial photo, slight grain\n<span class='x'>Constraints:</span> no people, text or logos")
    body = f"""<div class="row img-r"><div class="stack center"><div class="prompt" style="font-size:19px;">{p}</div>{note(t("Главное — в начале. Полный текст: <code>prompts.json</code> ➔ <code>A2_structured</code>", "Most important first. Full text: <code>prompts.json</code> ➔ <code>A2_structured</code>"), GR)}</div>
      {pic("A2_structured", t("Каждый слот на месте: пусто, стулья на столах, кружка справа, свет слева", "Every slot honored: empty, chairs up, mug right, light from the left"))}</div>"""
    return S(t("Часть 3 • Промпт • шаг 2", "Part 3 • Prompt • step 2"), t("Шесть слотов — и решения принимаете вы", "Six slots, and you make the decisions"), body, pr.s_struct()["notes"], k=GR)


def s13():
    body = f"""<div class="row img-l">{pic("A3_details", t("Текст, круассан и лаванда — ровно как заказано", "Text, croissant and lavender — exactly as ordered"))}
      <div class="stack center"><div class="prompt" style="font-size:17px;"><span class="g">Must-have:</span> {t("меловая табличка с текстом ровно", "a chalkboard that reads exactly")} <span class="m">"FLAT WHITE 3.50"</span> / <span class="m">"OPEN 7:00"</span>; {t("один круассан за кружкой; лаванда в вазе", "one croissant behind the mug; lavender in a vase")}</div>
        {ul([t("<b>Текст</b> — в кавычках, со словом exactly", "<b>Text</b> in quotes, with \"exactly\""), t("<b>Количество</b> — числом", "<b>Counts</b> as numbers"),
             t("<b>Место</b> — явно: «за», «рядом с»", "<b>Position</b> explicitly: \"behind\", \"next to\""), t("<b>Лишнее</b> — запретить: «no other text»", "<b>Extras</b> forbidden: \"no other text\"")], GR)}</div></div>"""
    return S(t("Часть 3 • Промпт • шаг 3", "Part 3 • Prompt • step 3"), t("Важные детали — отдельным блоком", "Must-have details as a separate block"), body, pr.s_details()["notes"], k=GR)


def s14():
    rows = [(t("Ракурс", "Angle"), "eye-level • low angle • top-down / flat lay"), (t("План", "Shot size"), "close-up • medium shot • full body • wide shot"),
            (t("Объектив", "Lens"), "24mm • 35mm • 50mm • 85mm portrait • macro"), (t("Резкость", "Depth of field"), "f/1.8 bokeh • f/8 all sharp"),
            (t("Свет", "Light"), "golden hour • window light • softbox • rim light"), (t("Стиль", "Style"), "editorial photo • film grain • watercolor • flat vector")]
    tbl = '<table class="t">' + "".join(f"<tr><td>{a}</td><td><code>{b}</code></td></tr>" for a, b in rows) + "</table>"
    body = f"""<div class="row" style="grid-template-columns:1.6fr 1fr;gap:56px;"><div class="stack center">{tbl}</div>
      <div class="stack center"><div class="say" style="font-size:30px;">{t("«85mm, f/1.8» — <em>одна фраза</em> вместо десятка решений: портрет, размытый фон, мягкая перспектива.", "\"85mm, f/1.8\" is <em>one phrase</em> instead of a dozen decisions: portrait, blurred background, flattering perspective.")}</div>
      {note(t("Формат кадра задаем настройкой сервиса, а не словами.", "Set the aspect ratio with the service option, not words."))}</div></div>"""
    return S(t("Часть 3 • Шпаргалка", "Part 3 • Cheat sheet"), t("Словарь фотографа: 30 слов с сильным эффектом", "Photographer's vocabulary: 30 high-impact words"), body, pr.s_vocab()["notes"])


# ---------------------------------------------------------------- 15 break
def s15():
    return dict(raw=True, notes=pr.s_break()["notes"], title_text=t("Перерыв", "Break"), body=f"""<div class="brk">
      <div class="kicker" style="--k:var(--amber)">{t("Экватор занятия", "Halfway")}</div>
      <h2 class="title">{t("Перерыв 5 минут", "5-minute break")}</h2>
      <div class="clock" id="clock">05:00</div>
      <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
      <p>{t("Дальше: правки, персонаж, фотосессия товара", "Next: edits, a character, a product photo shoot")}</p></div>""")


# ---------------------------------------------------------------- 16 iterate
def s16():
    loop = steps([(t("Черновик", "Draft"), t("2–4 варианта", "2–4 candidates")), (t("Выбор", "Pick"), t("по списку must-have", "against the must-haves")),
                  (t("Одна правка", "One edit"), t("«измени только X»", "\"change only X\"")), (t("Проверка", "Check"), t("что еще уплыло?", "what else drifted?")),
                  (t("Финал", "Final"), t("сохранить промпт", "save the prompt"))], GR)
    tpl = t("Отредактируй фото. Замени <span class='m'>только</span> X на Y.\n<span class='g'>Сохрани:</span> ракурс, кадр, фон, свет и тени.",
            "Edit this photo. Replace <span class='m'>only</span> X with Y.\n<span class='g'>Keep:</span> angle, framing, background, light and shadows.")
    body = f"""<div class="stack" style="gap:44px;flex:1;justify-content:center;">{loop}
      <div class="row c2" style="flex:0 0 auto;gap:56px;"><div class="stack"><div class="prompt-label">{t("Шаблон правки", "Edit template")}</div><div class="prompt" style="font-size:20px;">{tpl}</div></div>
      <div class="stack">{ul([t("<b>Одна правка за шаг</b>", "<b>One edit per turn</b>"), t("<b>Называйте, что сохранить</b>", "<b>Name what to keep</b>"), t("<b>После 6–8 правок</b> — новый чат с лучшей картинкой", "<b>After 6–8 edits</b> start a new chat with the best image")], GR)}</div></div></div>"""
    return S(t("Часть 3 • Промпт • шаг 4", "Part 3 • Prompt • step 4"), t("Правим, а не перегенерируем", "Edit, do not regenerate"), body, pr.s_iterate()["notes"], k=GR)


# ---------------------------------------------------------------- 17–21 patterns
def s17():
    body = f"""<div class="row c2" style="grid-template-rows:1fr 1fr;gap:18px 28px;">
      {pic("A2_structured", t("<b>Оригинал</b>", "<b>Original</b>"))}
      {pic("B1_replace", t("<b>Только объект:</b> кружка ➔ айс-латте. Фон и тени не изменились", "<b>Object only:</b> mug ➔ iced latte. Background and shadows unchanged"))}
      {pic("B2_relight", t("<b>Только время суток:</b> дождливый вечер, кадр тот же", "<b>Time of day only:</b> rainy evening, same framing"))}
      {pic("E2_style", t("<b>Только стиль:</b> плоская векторная иллюстрация", "<b>Style only:</b> flat vector illustration"))}</div>"""
    return S(t("Часть 4 • Паттерн 1 • редактирование", "Part 4 • Pattern 1 • editing"), t("Одна сцена — три правки", "One scene, three edits"), body, pat.s_edits()["notes"], k=GR)


def s18():
    body = f"""<div class="stack" style="flex:1;gap:20px;">
      <div style="display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr;gap:18px;flex:1;min-height:0;">
        {pic("C1_sheet", t("<b>1. Лист персонажа</b> — мастер-референс", "<b>1. Character sheet</b> — master reference"))}
        {pic("C2_rain", t("<b>2.</b> в пути", "<b>2.</b> on the road"), cover=True)}
        {pic("C3_door", t("<b>3.</b> у двери", "<b>3.</b> at the door"), cover=True)}
        {pic("C4_break", t("<b>4.</b> перерыв", "<b>4.</b> on a break"), cover=True)}</div>
      <div class="prompt" style="font-size:18px;"><span class="s">{t("Якоря в каждом промпте", "Anchors in every prompt")}:</span> curly hair • silver earring • yellow jacket <span class="m">with a grey stripe</span> • <span class="m">turquoise</span> backpack</div></div>"""
    return S(t("Часть 4 • Паттерн 2 • консистентность", "Part 4 • Pattern 2 • consistency"), t("Один курьер — в любой сцене", "One courier, any scene"), body, pat.s_character()["notes"], k=CY)


def s19():
    rows = [("ChatGPT", t("тот же чат + референсы + список «что сохранить»", "same chat + references + keep-list")),
            ("Nano Banana", t("несколько референсов в одном запросе", "several references in one request")),
            ("Midjourney", t("Edit до 4 референсов • <code>--sref</code> для стиля", "Edit with up to 4 references • <code>--sref</code> for style")),
            ("Kling", t("до 10 референсов • режим серии", "up to 10 references • series mode")), ("Grok", t("до 5 референсов • шаблоны", "up to 5 references • templates"))]
    tbl = '<table class="t">' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + "</table>"
    rec = steps([(t("Мастер-референс", "Master reference"), t("лист или пэкшот", "sheet or packshot")), (t("Якоря словами", "Anchors in words"), t("4–6 ярких примет", "4–6 distinctive traits")),
                 (t("Новая сцена", "New scene"), t("референс + якоря + действие", "reference + anchors + action")), (t("Сверка", "Check"), t("приметы по списку", "traits against the list"))], CY)
    body = f'<div class="stack" style="gap:44px;flex:1;justify-content:center;">{rec}{tbl}</div>'
    return S(t("Часть 4 • Паттерн 2", "Part 4 • Pattern 2"), t("Рецепт один, кнопки разные", "One recipe, different buttons"), body, pat.s_consistency_how()["notes"])


def s20():
    body = f"""<div style="display:grid;grid-template-columns:1fr 2fr;gap:28px;flex:1;min-height:0;">
      <div class="stack" style="gap:18px;">{pic("D0_packshot", t("<b>Мастер-кадр</b> — пэкшот на белом", "<b>Master shot</b> — packshot on white"))}
        <div class="prompt" style="font-size:16px;">Place <span class="g">exactly this mug</span> on … <span class="m">Do not change shape, color, glaze or proportions.</span></div></div>
      <div class="row c2" style="grid-template-rows:1fr 1fr;gap:16px 20px;">
        {pic("D1_kitchen", t("лайфстайл", "lifestyle"), cover=True)}{pic("D2_flatlay", t("флэтлей", "flat lay"), cover=True)}
        {pic("D3_hands", t("в руках", "in hands"), cover=True)}{pic("D4_banner", t("баннер с текстом", "banner with text"))}</div></div>"""
    return S(t("Часть 4 • Паттерн 3 • фотосессия", "Part 4 • Pattern 3 • photo shoot"), t("Один пэкшот — четыре кадра для магазина", "One packshot, four shots for a store"), body, pat.s_photoshoot()["notes"], k=GR)


def s21():
    body = f"""<div style="display:grid;grid-template-columns:1fr 70px 2.3fr;gap:20px;flex:1;min-height:0;align-items:stretch;">
      <div class="stack" style="gap:18px;">{pic("C1_sheet", t("<b>Картинка 1</b> — персонаж", "<b>Image 1</b> — character"))}{pic("D0_packshot", t("<b>Картинка 2</b> — товар", "<b>Image 2</b> — product"))}</div>
      <div style="display:flex;align-items:center;justify-content:center;font-size:48px;color:var(--green);">➔</div>
      <div class="stack" style="gap:16px;">{pic("E1_compose", t("Тот же курьер пьет из той же кружки", "The same courier drinking from the same mug"))}
        <div class="prompt" style="font-size:17px;"><span class="s">Image 1 is the character, image 2 is the product.</span> The same courier from image 1 drinks from exactly the mug from image 2…</div></div></div>"""
    return S(t("Часть 4 • Паттерн 4 • композиция", "Part 4 • Pattern 4 • composition"), t("Назовите роль каждой картинки", "Name the role of each image"), body, pat.s_multiref()["notes"], k=GR)


# ---------------------------------------------------------------- 22–25
def s22():
    code = """<span class="kw">from</span> google <span class="kw">import</span> genai
<span class="kw">from</span> google.genai <span class="kw">import</span> types
<span class="kw">from</span> PIL <span class="kw">import</span> Image

client = genai.<span class="fn">Client</span>()
sheet = Image.<span class="fn">open</span>(<span class="str">"C1_sheet.png"</span>)

resp = client.models.<span class="fn">generate_content</span>(
    model=<span class="str">"gemini-3.1-flash-image"</span>,
    contents=[sheet, PROMPT],      <span class="cm"># reference + text</span>
    config=types.<span class="fn">GenerateContentConfig</span>(
        response_modalities=[<span class="str">"IMAGE"</span>]))

resp.parts[<span class="str">0</span>].<span class="fn">as_image</span>().<span class="fn">save</span>(<span class="str">"scene.png"</span>)"""
    body = f"""<div class="row" style="grid-template-columns:1.25fr 1fr;gap:56px;"><div class="stack center"><pre class="code">{code}</pre></div>
      <div class="stack center">{ul([t("<b>50 карточек товара</b> скриптом — минуты, а не день", "<b>50 product cards</b> by script: minutes, not a day"),
          t("<b>Промпт — шаблон:</b> товар и сцена из таблицы", "<b>The prompt is a template:</b> product and scene from a table"),
          t("<b>Журнал генераций:</b> модель, промпт, референсы, дата", "<b>Generation log:</b> model, prompt, references, date")])}
        {note(t("Colab: <code>L04_Image_Generation_Prompts_and_Patterns.ipynb</code> — все паттерны урока в коде", "Colab: <code>L04_Image_Generation_Prompts_and_Patterns.ipynb</code> — every lesson pattern in code"))}</div></div>"""
    return S(t("Часть 5 • То же в коде", "Part 5 • Same thing in code"), t("Референс + промпт через API — тот же SDK, что в L03", "Reference + prompt via API — the same SDK as L03"), body, pat.s_api()["notes"])


def s23():
    risks = ul([t("<b>Мелкий текст и руки в толпе</b> всё еще ломаются", "<b>Small text and hands in crowds</b> still break"),
                t("<b>Дрейф:</b> после многих правок «плывут» лицо и цвета", "<b>Drift:</b> after many edits faces and colors shift"),
                t("<b>Цифры в инфографике</b> бывают выдуманными", "<b>Numbers in infographics</b> can be made up"),
                t("<b>Права:</b> картинка по одному промпту не охраняется (США)", "<b>Rights:</b> a prompt-only image is not copyrightable (US)"),
                t("<b>Водяные знаки:</b> SynthID и C2PA у Google и OpenAI", "<b>Provenance:</b> SynthID and C2PA on Google and OpenAI")], AM)
    zones = "".join(f'<div class="zone" style="--k:{k}"><div class="h">{h}</div><div class="d">{d}</div></div>' for h, d, k in [
        (t("Зеленая • сами", "Green • go"), t("мудборды, иллюстрации к слайдам, раскадровки", "moodboards, slide art, storyboards"), GR),
        (t("Желтая • человек проверяет", "Yellow • human reviews"), t("карточки товаров, баннеры, обложки YouTube", "product cards, banners, YouTube thumbnails"), AM),
        (t("Красная • не генерируем", "Red • do not generate"), t("документы, упаковка с составом, чужие логотипы, реальные люди без согласия", "documents, packaging with ingredients, others' logos, real people without consent"), RD)])
    body = f'<div class="row" style="grid-template-columns:1.15fr 1fr;gap:64px;"><div class="stack center">{risks}</div><div class="stack center" style="gap:30px;">{zones}</div></div>'
    return S(t("Часть 5 • Риски • Blast Radius", "Part 5 • Risks • Blast Radius"), t("Где генерация подводит и где ее нельзя применять", "Where generation fails and where not to use it"), body, pat.s_risks()["notes"], k=AM)


def s24():
    body = f"""<div class="row c2" style="flex:0 0 auto;gap:56px;">
      {pt(t("<span class='mark'>Трек А</span> • фотосессия товара", "<span class='mark'>Track A</span> • product photo shoot"), t("Свой предмет ➔ 4 кадра: лайфстайл, флэтлей, в руках, баннер. Товар узнаваем в каждом.", "Your own object ➔ 4 shots: lifestyle, flat lay, in hands, banner. The product is recognizable in each."), CY)}
      {pt(t("<span class='mark'>Трек Б</span> • курьер доставки", "<span class='mark'>Track B</span> • delivery courier"), t("Кейс из L01: лист персонажа ➔ 3 сцены рабочего дня ➔ 1 точечная правка.", "The L01 case: character sheet ➔ 3 scenes from a working day ➔ 1 targeted edit."), GR)}</div>
      <div style="margin-top:44px;">{steps([(t("Свободный ➔ структурный", "Free-form ➔ structured"), t("один кадр двумя промптами", "one shot, two prompts")),
          (t("Два сервиса", "Two services"), t("один промпт, сравнение", "one prompt, compared")), ("prompts.md", t("промпт к каждой картинке", "a prompt for every image")),
          ("qa.md", t("что сохранилось, что уплыло", "what held, what drifted"))], AM)}</div>
      <div style="margin-top:auto">{note(t("Сдать в <code>genai-homeworks/L04/</code>: <code>images/</code> + <code>prompts.md</code> + <code>qa.md</code>. Подробности и шаблоны — <code>L04_05_Homework.md</code>.", "Submit to <code>genai-homeworks/L04/</code>: <code>images/</code> + <code>prompts.md</code> + <code>qa.md</code>. Details and templates: <code>L04_05_Homework_EN.md</code>."))}</div>"""
    return S(t("Домашнее задание №4", "Homework #4"), t("Фотосессия товара или персонаж-курьер", "A product photo shoot or a courier character"), body, pat.s_homework()["notes"])


def s25():
    body = f"""<div class="row" style="grid-template-columns:1.4fr 1fr;gap:72px;">
      <div class="stack center" style="gap:26px;">
        {pt(t("Сервис — под задачу", "Service per task"), t("текст — ChatGPT, серии — Nano Banana и Kling, эстетика — Midjourney", "text — ChatGPT, series — Nano Banana and Kling, aesthetics — Midjourney"))}
        {pt(t("Структура вместо фразы", "Structure, not a phrase"), t("объект, сцена, камера, свет, стиль, детали, запреты", "subject, setting, camera, light, style, details, constraints"))}
        {pt(t("Правка вместо перегенерации", "Edit, do not regenerate"), t("«измени только X», одна правка за шаг", "\"change only X\", one edit per turn"))}
        {pt(t("Консистентность", "Consistency"), t("мастер-референс + якоря словами", "master reference + anchors in words"))}</div>
      <div class="stack center" style="gap:18px;">{pic("C2_rain", "", cover=True)}<div class="pt" style="--k:var(--violet)"><div class="h"><span class="mark">{t("Урок 05", "Lesson 05")}:</span> {t("генерация видео", "video generation")}</div><div class="d">{t("Эти картинки станут первыми кадрами: курьер поедет.", "These images become first frames: the courier starts riding.")}</div></div></div></div>"""
    return S(t("Итоги • вопросы", "Takeaways • Q&A"), t("Четыре вещи, которые стоит унести", "Four things to take away"), body, pat.s_qa()["notes"])


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15,
          s16, s17, s18, s19, s20, s21, s22, s23, s24, s25]
