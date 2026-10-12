"""Part 2: the five services (state as of October 2026, see L04_08_Source_Notes_Research_2026-10.md)."""

from slides import A, C, G, I, P, R, note, t, ul

def asof():
    return t("по состоянию на октябрь 2026", "as of October 2026")


def svc_card(name, model, access, best, color, style=""):
    return f"""<div class="dg-node" style="--nc:{color};"><div class="k">{name}</div>
      <div class="t" style="font-size:17px;">{model}</div>
      <div class="d"><b style="color:#fff">{t("Где:", "Where:")}</b> {access}</div>
      <div class="d"><b style="color:#fff">{t("Сильнее всего:", "Best at:")}</b> {best}</div>
      <div class="d" style="margin-top:auto;padding-top:8px;border-top:1px solid var(--border-subtle);"><b style="color:#fff">{t("Стиль промпта:", "Prompt style:")}</b> {style}</div></div>"""


def s_map():
    cards = [
        svc_card("ChatGPT", "GPT Image 2 ➔ ChatGPT Images 2.5", t("чат ChatGPT (все тарифы), OpenAI API", "ChatGPT chat (all plans), OpenAI API"),
                 t("текст и инфографика, правки диалогом, точное следование инструкции", "text and infographics, conversational edits, instruction following"), C,
                 t("сцена ➔ объект ➔ детали ➔ ограничения; текст в кавычках", "scene ➔ subject ➔ details ➔ constraints; text in quotes")),
        svc_card("Nano Banana", "Nano Banana 2 • Pro • 2 Lite", t("приложение Gemini, AI Studio, Gemini API / Vertex", "Gemini app, AI Studio, Gemini API / Vertex"),
                 t("смешивание нескольких референсов, консистентность, дешевый API", "multi-reference blending, consistency, cheap API"), G,
                 t("связное описание: объект + действие + место + кадр + стиль", "a descriptive paragraph: subject + action + place + framing + style")),
        svc_card("Midjourney", "V8.2 + Edit Model", t("midjourney.com и Discord, подписка от $10, без API", "midjourney.com and Discord, from $10/mo, no API"),
                 t("эстетика, поиск стиля, «журнальная» картинка", "aesthetics, style exploration, editorial look"), P,
                 t("коротко и конкретно + параметры <code>--ar --s --sref</code>", "short and concrete + parameters <code>--ar --s --sref</code>")),
        svc_card("Kling", "IMAGE 3.0 • 3.0 Omni • O1", t("kling.ai (кредиты), API", "kling.ai (credits), API"),
                 t("серии кадров и раскадровки, мост в видео (L05)", "image series and storyboards, bridge to video (L05)"), A,
                 t("кино-термины; «Keep everything else unchanged, modify…»", "cinema terms; \"Keep everything else unchanged, modify…\"")),
        svc_card("Grok Imagine", "Image 2.0 (Aurora)", t("grok.com/imagine, приложение, API", "grok.com/imagine, app, API"),
                 t("правка выделением (Magic Wand), шаблоны товара и портрета", "Magic Wand region edits, product and headshot templates"), R,
                 t("выделить область ➔ описать правку; шаблоны", "select a region ➔ describe the edit; templates")),
    ]
    body = f"""<div class="dg"><div class="svc">{''.join(cards)}</div>
      {note(t("<b>Рынок сошелся:</b> все пятеро умеют текст ➔ картинку, правку по инструкции и работу с референсами. Разница — в «характере»: кто лучше слушается, кто красивее рисует, у кого есть API и какие правила контента. Версии меняются каждые 2–3 месяца — проверяйте перед работой.",
               "<b>The market has converged:</b> all five do text ➔ image, instruction edits and references. They differ in character: who follows instructions best, who draws prettiest, who has an API and what the content rules are. Versions change every 2–3 months — check before you start."))}</div>"""
    return dict(tag=t("СЕРВИСЫ", "SERVICES"), info=asof().upper(),
                title=t("Пять сервисов: кто для чего", "Five services: which one for what"),
                lead=t("Не «какой лучший», а «какой под задачу»", "Not \"which is best\" but \"which fits the task\""),
                body=body,
                notes=t("Обзор на одном слайде. Дальше — по одному слайду на сервис. Подчеркнуть: версии из этого слайда устареют через пару месяцев, важно понимать характер сервиса, а не номер версии.",
                        "One-slide overview, then one slide per service. Stress that the versions here will be outdated in a couple of months; understand the service's character, not its version number."))


def svc_slide(tag, title, lead, features, prompt_tip, prompt_box, color, notes, caveat=""):
    cav = note(caveat) if caveat else ""
    body = f"""<div class="dg-split l"><div class="dg-node flat" style="--nc:{color}"><div class="k">{t("ОСОБЕННОСТИ", "FEATURES")}</div>{ul(features, color)}</div>
      <div class="dg-col"><div class="dg-node flat" style="--nc:{color}"><div class="k">{t("КАК С НИМ ГОВОРИТЬ", "HOW TO PROMPT IT")}</div><div class="d">{prompt_tip}</div></div>
      <div class="pbox" style="--nc:{color}">{prompt_box}</div>{cav}</div></div>"""
    return dict(tag=tag, info=asof().upper(), title=title, lead=lead, body=body, notes=notes)


def s_chatgpt():
    return svc_slide(
        t("СЕРВИС 1 • CHATGPT", "SERVICE 1 • CHATGPT"),
        t("ChatGPT Images: модель, которая сначала думает, потом рисует", "ChatGPT Images: a model that thinks first, then draws"),
        t("GPT Image 2 (апрель 2026) ➔ ChatGPT Images 2.5 (сентябрь 2026)", "GPT Image 2 (April 2026) ➔ ChatGPT Images 2.5 (September 2026)"),
        [t("<b>Рассуждение перед генерацией:</b> планирует композицию, текст и связи объектов", "<b>Reasoning before generation:</b> plans layout, text and object relations"),
         t("<b>Лучший текст на картинке,</b> включая кириллицу: постеры, меню, инфографика, UI-макеты", "<b>Best-in-class text,</b> including non-Latin: posters, menus, infographics, UI mockups"),
         t("<b>Правки диалогом;</b> в 2.5 — комментарий к области картинки и <code>@Sketch</code> (набросок ➔ картинка)", "<b>Conversational edits;</b> 2.5 adds region comments and <code>@Sketch</code> (sketch ➔ image)"),
         t("<b>Несколько референсов</b> в одном сообщении: товар + фон + стиль", "<b>Several references</b> in one message: product + background + style"),
         t("<b>Водяные знаки:</b> метаданные C2PA и невидимый SynthID (с мая 2026)", "<b>Provenance:</b> C2PA metadata and invisible SynthID (since May 2026)")],
        t("Обычный язык, порядок из гайда OpenAI: <b>сцена ➔ объект ➔ ключевые детали ➔ ограничения</b>. Текст — в кавычках. При правке каждый раз повторять, что сохранить.",
          "Plain language, OpenAI guide order: <b>scene ➔ subject ➔ key details ➔ constraints</b>. Literal text in quotes. When editing, restate what to keep every turn."),
        t("Постер митапа 4:5. Сцена: ночной город в синих тонах.\nОбъект: ноутбук с открытым редактором кода.\nТекст ровно: \"GenAI Basics • Урок 04\".\nОграничения: без логотипов, текст без ошибок.",
          "Meetup poster 4:5. Scene: night city in blue tones.\nSubject: a laptop with a code editor open.\nExact text: \"GenAI Basics • Lesson 04\".\nConstraints: no logos, text spelled exactly."),
        C,
        t("Главное отличие ChatGPT — модель рассуждает перед генерацией, поэтому лучше всех держит сложные инструкции и текст. Сценарий использования: постеры, слайды, инфографика, мокапы интерфейсов. Ограничение: в «чистой эстетике» уступает Midjourney; плотный мелкий текст все еще ломается.",
          "ChatGPT's key difference: it reasons before generating, so it handles complex instructions and text best. Use cases: posters, slides, infographics, UI mockups. Limitation: trails Midjourney on pure aesthetics; dense small text can still break."))


def s_nano():
    return svc_slide(
        t("СЕРВИС 2 • NANO BANANA", "SERVICE 2 • NANO BANANA"),
        t("Nano Banana (Gemini): референсы и консистентность", "Nano Banana (Gemini): references and consistency"),
        t("Все картинки этого урока сделаны Nano Banana Pro — промпты в examples/prompts.json", "Every image in this lesson was made with Nano Banana Pro — prompts in examples/prompts.json"),
        [t("<b>Линейка:</b> Nano Banana 2 (по умолчанию в Gemini), Pro (сложные сцены, 4K), 2 Lite (самая быстрая и дешевая)", "<b>Lineup:</b> Nano Banana 2 (Gemini default), Pro (complex scenes, 4K), 2 Lite (fastest, cheapest)"),
         t("<b>Много референсов сразу:</b> персонажи + объекты в одной сцене (лимиты зависят от модели)", "<b>Many references at once:</b> characters + objects in one scene (limits vary by model)"),
         t("<b>Правка словами без маски:</b> модель сама находит зону «кружка», «фон», «небо»", "<b>Mask-free edits:</b> the model finds \"the mug\", \"the background\", \"the sky\" itself"),
         t("<b>Привязка к поиску Google:</b> актуальные факты для инфографики (проверяйте цифры!)", "<b>Google Search grounding:</b> fresh facts for infographics (verify the numbers!)"),
         t("<b>API с той же моделью:</b> <code>gemini-3.1-flash-image</code> — тот же SDK, что в L03", "<b>Same model via API:</b> <code>gemini-3.1-flash-image</code> — the same SDK as in L03")],
        t("Формула из гайда Google: <b>[Объект] + [Действие] + [Место] + [Композиция] + [Стиль]</b>. С референсами: <b>[Картинки] + [Связь между ними] + [Новая сцена]</b>. Описывать сцену предложениями, а не списком слов; формулировать позитивно: «пустая улица», а не «без машин».",
          "Google's formula: <b>[Subject] + [Action] + [Location] + [Composition] + [Style]</b>. With references: <b>[Images] + [Relationship] + [New scenario]</b>. Describe the scene in sentences, not keyword lists; phrase positively: \"an empty street\", not \"no cars\"."),
        t("Картинка 1 — персонаж, картинка 2 — товар.\nТот же курьер из картинки 1 сидит у окна кофейни\nи пьет из той самой кружки с картинки 2.\nУтренний свет, 35 мм, реалистичное фото.",
          "Image 1 is the character, image 2 is the product.\nThe same courier from image 1 sits at a coffee-shop window\nand drinks from exactly the mug from image 2.\nMorning light, 35mm, realistic photo."),
        G,
        t("Nano Banana — наш рабочий инструмент на этом уроке: все примеры сделаны им. Сильные стороны — работа с несколькими референсами и точечные правки без маски. Доступ бесплатно через приложение Gemini и AI Studio (с дневными лимитами), в коде — через google-genai, как в L03.",
          "Nano Banana is our workhorse today: every example was made with it. Strengths: multi-reference work and mask-free targeted edits. Free access via the Gemini app and AI Studio (daily limits); in code via google-genai, as in L03."))


def s_midjourney():
    rows = [
        ("--ar 16:9", t("формат кадра", "aspect ratio")),
        ("--s 0–1000", t("stylize: сколько «своей эстетики» добавит MJ (по умолч. 100)", "stylize: how much MJ aesthetic to add (default 100)")),
        ("--c 0–100", t("chaos: насколько разными будут 4 варианта", "chaos: how different the 4 variants are")),
        ("--raw", t("меньше украшательства, буквальнее к промпту", "less embellishment, more literal")),
        ("--sref &lt;url&gt; --sw", t("референс стиля и его сила", "style reference and its weight")),
        ("--p • moodboard", t("личный вкус: профиль из ваших оценок или мудборда", "personal taste: profile from your ratings or a moodboard")),
        ("--no text, people", t("негативный промпт: чего не должно быть", "negative prompt: what must not appear")),
        ("--seed 42", t("повторяемость стартового шума", "repeatable starting noise")),
        ("--edit / Edit", t("правка до 4 референсов, inpaint/outpaint (заменил --oref и --cref)", "edit with up to 4 references, inpaint/outpaint (replaced --oref and --cref)")),
    ]
    trs = "".join(f"<tr><td><code>{a}</code></td><td>{b}</td></tr>" for a, b in rows)
    body = f"""<div class="dg-split r"><div class="dg-col">
        <div class="dg-node flat" style="--nc:{P}"><div class="k">{t("ОСОБЕННОСТИ", "FEATURES")}</div>{ul([
            t("<b>Эстетика из коробки:</b> свет, цвет и композиция «как в журнале» даже от короткого промпта", "<b>Aesthetics out of the box:</b> magazine-grade light, color and composition from short prompts"),
            t("<b>Управление параметрами</b> в конце промпта, а не словами", "<b>Control via parameters</b> at the end of the prompt, not words"),
            t("<b>4 варианта на запрос</b> ➔ выбор ➔ Vary / Edit / Upscale", "<b>4 variants per prompt</b> ➔ pick ➔ Vary / Edit / Upscale"),
            t("<b>/describe:</b> картинка ➔ 4 промпта, хороший способ учиться", "<b>/describe:</b> image ➔ 4 prompts, a good way to learn"),
            t("<b>Минусы:</b> нет официального API, текст слабее, чем у ChatGPT и Gemini", "<b>Downsides:</b> no official API, weaker text than ChatGPT and Gemini")], P)}</div>
        <div class="pbox" style="--nc:{P}">editorial photo of a speckled ceramic mug on oak, morning window light <span class="m">--ar 4:5 --s 250 --raw --no text</span></div></div>
      <table class="tbl"><tr><th>{t("Параметр", "Parameter")}</th><th>{t("Что делает", "What it does")}</th></tr>{trs}</table></div>"""
    return dict(tag=t("СЕРВИС 3 • MIDJOURNEY", "SERVICE 3 • MIDJOURNEY"), info=asof().upper(),
                title=t("Midjourney: эстетика и параметры", "Midjourney: aesthetics and parameters"),
                lead=t("V8.2 по умолчанию; в августе 2026 появился Edit Model — правка с референсами вместо --oref/--cref", "V8.2 is the default; in August 2026 the Edit Model replaced --oref/--cref with reference-based editing"),
                body=body,
                notes=t("Midjourney — другая философия: короткий промпт + параметры. Показать таблицу параметров; в старых курсах учат --cref и --oref — в V8 их заменил Edit Model (до 4 референсов). Важно: промпт в Midjourney лучше короче и конкретнее; главное — в начале. Для студентов EPAM: нет API, поэтому в автоматизацию не встраивается.",
                        "Midjourney is a different philosophy: short prompt + parameters. Walk through the table; older courses teach --cref and --oref — in V8 the Edit Model (up to 4 references) replaced them. Midjourney prompts work best short and concrete, key subject first. For engineers: no API, so it does not fit automation."))


def s_kling_grok():
    body = f"""<div class="grid-2">
      <div class="dg-node flat" style="--nc:{A}"><div class="k">KLING • IMAGE 3.0 / OMNI / O1</div>{ul([
          t("<b>Корни в видео:</b> картинка — первый кадр для ролика в Kling (тема L05)", "<b>Video roots:</b> an image is the first frame for a Kling clip (topic of L05)"),
          t("<b>До 10 референсов,</b> «замок» на контуры, ключевые элементы и тон объекта", "<b>Up to 10 references,</b> locks the subject's contours, key elements and tone"),
          t("<b>Image Series:</b> связная серия кадров и раскадровки", "<b>Image Series:</b> coherent sets and storyboards"),
          t("<b>Кино-словарь:</b> план, ракурс, фокусное расстояние, диафрагма", "<b>Cinema vocabulary:</b> shot size, angle, focal length, aperture"),
          t("<b>Виртуальная примерка</b> и мульти-ракурс в Omni", "<b>Virtual try-on</b> and multi-view in Omni")], A)}
        <div class="pbox" style="--nc:{A};margin-top:8px;">Keep everything else unchanged, modify the jacket to a red raincoat.</div>
        <div class="d" style="font-size:13px;color:var(--text-dim);margin-top:4px;">{t("официальный шаблон правки из гайда Kling IMAGE 3.0", "official edit template from the Kling IMAGE 3.0 guide")}</div></div>
      <div class="dg-node flat" style="--nc:{R}"><div class="k">GROK IMAGINE • IMAGE 2.0</div>{ul([
          t("<b>Собственная модель Aurora</b> (xAI, теперь в составе SpaceX)", "<b>Own Aurora model</b> (xAI, now part of SpaceX)"),
          t("<b>Magic Wand:</b> выделили область ➔ описали правку", "<b>Magic Wand:</b> select a region ➔ describe the edit"),
          t("<b>До 5 референсов,</b> удаление фона с прозрачностью, Smart Resize на 9 форматов", "<b>Up to 5 references,</b> background removal with transparency, Smart Resize to 9 formats"),
          t("<b>Шаблоны:</b> предметная съемка, портрет-хедшот, иконки", "<b>Templates:</b> product shots, headshots, icons"),
          t("<b>Риск:</b> мягкие правила контента ➔ скандал с дипфейками в январе 2026, блокировки в ряде стран", "<b>Risk:</b> lax content rules ➔ deepfake scandal in January 2026, blocks in several countries")], R)}
        {note(t("<b>Для работы:</b> корпоративные материалы и фото реальных людей — только в сервисах с понятными правилами и условиями использования данных.", "<b>For work:</b> corporate assets and photos of real people only in services with clear content and data-use terms."))}</div>
    </div>"""
    return dict(tag=t("СЕРВИСЫ 4–5 • KLING И GROK", "SERVICES 4–5 • KLING & GROK"), info=asof().upper(),
                title=t("Kling и Grok: серии кадров и правка выделением", "Kling and Grok: image series and region edits"),
                lead=t("Kling — мост к видео; Grok — быстрые правки и шаблоны, но с оговорками по политике контента", "Kling bridges to video; Grok offers fast edits and templates, with content-policy caveats"),
                body=body,
                notes=t("Kling знают как видеогенератор, но у него сильная генерация картинок с референсами — удобно готовить кадры для видео (следующий урок). Grok Imagine 2.0 — быстрые правки выделением и шаблоны; обязательно упомянуть историю с дипфейками: это аргумент, почему в рабочих задачах важно, где и с какими правилами генерировать.",
                        "Kling is known for video, but its reference-based image generation is strong — handy for preparing frames for video (next lesson). Grok Imagine 2.0 offers region edits and templates; mention the deepfake story: it is why, at work, it matters where and under which rules you generate."))


def s_matrix():
    Y, M, N = '<span class="y">●●●</span>', '<span class="m">●●○</span>', '<span class="n">●○○</span>'
    rows = [
        (t("Текст на картинке", "Text in image"), Y, Y, M, M, M),
        (t("Следование инструкции", "Instruction following"), Y, Y, M, M, M),
        (t("Правка «измени только X»", "\"Change only X\" edits"), Y, Y, M, Y, Y),
        (t("Консистентность персонажа/товара", "Character/product consistency"), M, Y, M, Y, M),
        (t("Эстетика «из коробки»", "Out-of-the-box aesthetics"), M, M, Y, M, M),
        (t("API для автоматизации", "API for automation"), Y, Y, N, Y, Y),
        (t("Бесплатный старт", "Free tier"), Y, Y, N, M, M),
    ]
    trs = "".join(f"<tr><td>{r[0]}</td>" + "".join(f'<td style="text-align:center">{c}</td>' for c in r[1:]) + "</tr>" for r in rows)
    body = f"""<div class="dg"><table class="tbl"><tr><th></th><th style="text-align:center">ChatGPT</th><th style="text-align:center">Nano Banana</th><th style="text-align:center">Midjourney</th><th style="text-align:center">Kling</th><th style="text-align:center">Grok</th></tr>{trs}</table>
      <div class="grid-3" style="height:auto;">
        {note(t("<b>Постер, слайд, инфографика</b> ➔ ChatGPT", "<b>Poster, slide, infographic</b> ➔ ChatGPT"))}
        {note(t("<b>Серия с одним героем или товаром</b> ➔ Nano Banana / Kling", "<b>Series with one character or product</b> ➔ Nano Banana / Kling"))}
        {note(t("<b>Мудборд, стиль, концепт-арт</b> ➔ Midjourney", "<b>Moodboard, style, concept art</b> ➔ Midjourney"))}
      </div></div>"""
    return dict(tag=t("СРАВНЕНИЕ", "COMPARISON"), info=t("ОЦЕНКА ПРЕПОДАВАТЕЛЯ", "INSTRUCTOR'S ASSESSMENT"),
                title=t("Матрица выбора: какой сервис под какую задачу", "Selection matrix: which service for which task"),
                lead=t("Качественная оценка на основе обзоров и наших тестов, не бенчмарк", "Qualitative rating from reviews and our tests, not a benchmark"),
                body=body,
                notes=t("Это субъективная матрица, а не бенчмарк — честно говорим об этом. Смысл: выбирать по задаче. В домашке попросим сравнить два сервиса на одной задаче и самим заполнить такую строку.",
                        "This is a subjective matrix, not a benchmark — say so openly. The point: choose by task. The homework asks students to compare two services on one task and fill in such a row themselves."))
