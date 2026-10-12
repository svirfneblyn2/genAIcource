"""Part 4 (patterns) and Part 5 (API, risks, homework, Q&A)."""

from slides import A, C, G, I, P, R, arrow, fig, node, note, t, ul


def s_edits():
    body = f"""<div style="display:grid;grid-template-columns:2.6fr 1fr;gap:14px;height:100%;min-height:0;">
      <div class="g22">
        {fig("A2_structured", t("<b>Оригинал</b>", "<b>Original</b>"), "", C, contain=True)}
        {fig("B1_replace", t("<b>Замена объекта:</b> кружка ➔ айс-латте, тень на месте", "<b>Object swap:</b> mug ➔ iced latte, shadow intact"), "", G, contain=True)}
        {fig("B2_relight", t("<b>Время суток:</b> вечер и дождь, кадр тот же", "<b>Time of day:</b> rainy evening, same framing"), "", A, contain=True)}
        {fig("E2_style", t("<b>Стиль:</b> плоская векторная иллюстрация", "<b>Style:</b> flat vector illustration"), "", P, contain=True)}
      </div>
      <div class="col">
        <div class="pbox" style="--nc:{G}">Replace only the ceramic mug with a tall glass of iced latte… Keep everything else exactly the same.</div>
        <div class="pbox" style="--nc:{A}">Change only the time of day to a rainy evening… Keep the exact same composition.</div>
        <div class="pbox" style="--nc:{P}">Redraw this exact scene as a flat vector illustration in five colors… Keep the composition identical.</div>
        {note(t("<b>Проверка:</b> при замене кружки стулья, кофемашина и тени не изменились.", "<b>Check:</b> during the swap the chairs, machine and shadows stayed the same."))}
      </div></div>"""
    return dict(tag=t("ПАТТЕРН 1 • РЕДАКТИРОВАНИЕ", "PATTERN 1 • EDITING"), info=t("ЧАСТЬ 4", "PART 4"), cls="visual-slide",
                title=t("Одна сцена — три правки: объект, свет, стиль", "One scene, three edits: object, light, style"),
                lead=t("Все три правки — к одному оригиналу, по шаблону «измени только X, сохрани остальное»", "All three edits apply to one original using the \"change only X, keep the rest\" template"),
                body=body,
                notes=t("Обратите внимание: при замене кружки стулья, кофемашина и свет не изменились — это и есть контроль. Где применяется: варианты товара для магазина, смена сезона в баннере, адаптация под стиль бренда. Технически это inpainting: в чат-моделях маску рисовать не нужно, модель находит зону по тексту. В Midjourney и Grok зону можно выделить вручную.",
                        "Note that during the mug swap the chairs, machine and light did not change — that is control. Use cases: product variants for a shop, seasonal banners, brand-style adaptation. Technically it is inpainting: chat models do not need a hand-drawn mask; they find the region from text. In Midjourney and Grok you can select the region by hand."))


def s_character():
    body = f"""<div class="dg" style="gap:10px;">
      <div style="display:grid;grid-template-columns:1.55fr 1fr 1fr 1fr;gap:12px;flex:1 1 0;min-height:0;">
        {fig("C1_sheet", t("<b>Шаг 1. Лист персонажа:</b> 4 ракурса, фиксированные приметы", "<b>Step 1. Character sheet:</b> 4 angles, fixed traits"), "", C, contain=True)}
        {fig("C2_rain", t("<b>Сцена 1:</b> велосипед, дождь", "<b>Scene 1:</b> bike, rain"), "", G)}
        {fig("C3_door", t("<b>Сцена 2:</b> доставка у двери", "<b>Scene 2:</b> doorstep delivery"), "", G)}
        {fig("C4_break", t("<b>Сцена 3:</b> перерыв, крупный план", "<b>Scene 3:</b> break, close-up"), "", G)}
      </div>
      <div class="grid-2" style="height:auto;flex-shrink:0;">
        <div class="pbox" style="--nc:{C}"><span class="s">{t("Приметы-якоря", "Anchor traits")}:</span> short curly dark-brown hair • silver hoop earring • yellow jacket <span class="m">with a reflective grey stripe</span> • black cargo trousers • white sneakers • <span class="m">turquoise</span> thermal backpack</div>
        <div class="pbox" style="--nc:{G}">Use the attached character sheet as the identity reference. <span class="g">The same courier (same face, hair, earring, yellow jacket with grey stripe, turquoise backpack)</span> is riding a city bicycle…</div>
      </div></div>"""
    return dict(tag=t("ПАТТЕРН 2 • КОНСИСТЕНТНОСТЬ", "PATTERN 2 • CONSISTENCY"), info=t("ЧАСТЬ 4", "PART 4"), cls="visual-slide",
                title=t("Один персонаж в разных сценах: лист персонажа + приметы-якоря", "One character across scenes: character sheet + anchor traits"),
                lead=t("Курьер доставки — тот же кейс, что в домашке L01. Референс + повтор примет в каждом промпте", "A delivery courier — the same case as the L01 homework. Reference + repeated traits in every prompt"),
                body=body,
                notes=t("Рецепт: 1) сгенерировать лист персонажа на нейтральном фоне в нескольких ракурсах; 2) в каждую новую сцену прикладывать лист как референс и повторять словами 4–6 примет-якорей. Яркие уникальные приметы (серая полоса, бирюзовый рюкзак) держатся лучше, чем «обычная куртка». Проверяем глазами: лицо, прическа, серьга, полоса, рюкзак — совпали во всех трех сценах.",
                        "Recipe: 1) generate a character sheet on a neutral background from several angles; 2) attach it as a reference to every new scene and repeat 4–6 anchor traits in words. Distinctive traits (grey stripe, turquoise backpack) hold better than \"a regular jacket\". Check visually: face, hair, earring, stripe and backpack match in all three scenes."))


def s_consistency_how():
    rows = [
        ("ChatGPT", t("продолжать в том же чате; прикладывать референсы; повторять список «что сохранить»", "stay in the same chat; attach references; restate the keep-list")),
        ("Nano Banana", t("несколько референсов в одном запросе (персонажи + объекты); лучше 3+ ракурса героя", "several references per request (characters + objects); 3+ angles of the subject work best")),
        ("Midjourney", t("Edit Model до 4 референсов; <code>--sref</code> и мудборд держат стиль; <code>--seed</code> — повторяемость", "Edit Model with up to 4 references; <code>--sref</code> and moodboards hold the style; <code>--seed</code> for repeatability")),
        ("Kling", t("до 10 референсов; режим Image Series для связной серии", "up to 10 references; Image Series mode for a coherent set")),
        ("Grok", t("до 5 референсов; шаблоны для товара и портрета", "up to 5 references; product and headshot templates")),
    ]
    trs = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    steps = f"""<div class="dg-row">{node("1", t("Мастер-референс", "Master reference"), t("лист персонажа / пэкшот товара", "character sheet / product packshot"), C)}{arrow()}{node("2", t("Якоря словами", "Anchors in words"), t("4–6 уникальных примет", "4–6 distinctive traits"), C)}{arrow()}{node("3", t("Сцена", "Scene"), t("референс + якоря + новое действие", "reference + anchors + new action"), G)}{arrow()}{node("4", t("Сверка", "Check"), t("приметы по списку", "traits against the list"), A)}</div>"""
    body = f"""<div class="dg">{steps}<table class="tbl"><tr><th>{t("Сервис", "Service")}</th><th>{t("Как удержать героя или товар", "How to keep the character or product")}</th></tr>{trs}</table>
      {note(t("<b>Чего не делать:</b> описывать героя заново в каждом запросе без референса — каждая генерация «придумает» нового человека. И не менять сразу и сцену, и одежду, и ракурс.", "<b>Do not:</b> re-describe the hero from scratch without a reference — each generation will invent a new person. And do not change scene, outfit and angle all at once."))}</div>"""
    return dict(tag=t("ПАТТЕРН 2 • КОНСИСТЕНТНОСТЬ", "PATTERN 2 • CONSISTENCY"), info=t("ЧАСТЬ 4", "PART 4"),
                title=t("Консистентность в каждом сервисе: общий рецепт, разные кнопки", "Consistency in each service: one recipe, different buttons"),
                lead=t("Четыре шага одинаковы везде; отличается только то, как передать референс", "The four steps are the same everywhere; only the way to pass the reference differs"),
                body=body,
                notes=t("Обобщаем рецепт. Старые курсы учат --cref в Midjourney — сейчас это Edit Model. Лимиты референсов меняются с версиями; принцип нет: мастер-референс + якоря словами.",
                        "Generalize the recipe. Older courses teach --cref in Midjourney — today it is the Edit Model. Reference limits change with versions; the principle does not: master reference + anchors in words."))


def s_photoshoot():
    body = f"""<div style="display:grid;grid-template-columns:1fr 1.45fr 0.95fr;gap:14px;height:100%;min-height:0;">
      <div class="stack">{fig("D0_packshot", t("<b>Мастер-кадр:</b> пэкшот на белом", "<b>Master shot:</b> packshot on white"), "", C, contain=True)}</div>
      <div class="g22">
      {fig("D1_kitchen", t("<b>Лайфстайл:</b> кухня, утро", "<b>Lifestyle:</b> kitchen, morning"), "", G, contain=True)}
      {fig("D2_flatlay", t("<b>Флэтлей:</b> сверху", "<b>Flat lay:</b> top-down"), "", G, contain=True)}
      {fig("D3_hands", t("<b>В руках:</b> улица, осень", "<b>In hands:</b> street, autumn"), "", G, contain=True)}
      {fig("D4_banner", t("<b>Баннер:</b> с текстом", "<b>Banner:</b> with text"), "", A, contain=True)}
      </div>
      <div class="col">
      <div class="pbox" style="--nc:{G}">Product photo session. Place <span class="g">exactly this mug</span> (same shape, speckled cream glaze, terracotta base band, handle) on a light travertine kitchen counter… 50mm, f/2.8. <span class="m">Do not change the mug's shape, color, glaze pattern or proportions.</span></div>
      {note(t("<b>Схема фотосессии:</b> один мастер-кадр ➔ N сцен из шот-листа (лайфстайл, флэтлей, в руках, баннер). Каждый промпт: <b>сохраняемые признаки товара</b> + новая сцена + камера и свет. Проверка: форма ручки, крапинки, полоска у дна.", "<b>Shoot scheme:</b> one master shot ➔ N scenes from a shot list (lifestyle, flat lay, in hands, banner). Each prompt: <b>preserved product traits</b> + new scene + camera and light. Check: handle shape, speckles, base band."))}
    </div></div>"""
    return dict(tag=t("ПАТТЕРН 3 • ФОТОСЕССИЯ", "PATTERN 3 • PHOTO SHOOT"), info=t("ЧАСТЬ 4", "PART 4"), cls="visual-slide",
                title=t("AI-фотосессия товара: один пэкшот — пять кадров для магазина", "AI product photo shoot: one packshot, five shots for a store"),
                lead=t("Тот же паттерн, что с персонажем: мастер-референс + неизменяемые признаки + новая сцена", "Same pattern as the character: master reference + preserved traits + new scene"),
                body=body,
                notes=t("Это самый популярный бизнес-кейс в курсах: e-commerce, маркетплейсы, соцсети. Рабочий процесс: снять товар на телефон на белом фоне (или сгенерировать) ➔ шот-лист ➔ серия. Показываем, что кружка узнаваема во всех кадрах. Честно: мелкие детали могут «плыть» — поэтому в Красной зоне (упаковка, состав, логотипы) обязательна проверка человеком.",
                        "This is the most popular business case in courses: e-commerce, marketplaces, social media. Workflow: photograph the product on white with a phone (or generate it) ➔ shot list ➔ series. Show that the mug is recognizable in every shot. Honestly: small details can drift — so in the Red zone (packaging, ingredients, logos) human review is mandatory."))


def s_multiref():
    body = f"""<div style="display:grid;grid-template-columns:1fr 44px 2.2fr;gap:12px;height:100%;min-height:0;align-items:stretch;">
      <div class="stack">
        {fig("C1_sheet", t("<b>Картинка 1:</b> персонаж", "<b>Image 1:</b> character"), "", C, contain=True)}
        {fig("D0_packshot", t("<b>Картинка 2:</b> товар", "<b>Image 2:</b> product"), "", C, contain=True)}
      </div>
      <div style="display:flex;align-items:center;justify-content:center;color:var(--c4-success);font-size:30px;">➔</div>
      <div class="stack">
        {fig("E1_compose", t("<b>Результат:</b> тот же курьер пьет из той же кружки", "<b>Result:</b> the same courier drinking from the same mug"), "", G, contain=True)}
        <div class="pbox" style="--nc:{G};flex-shrink:0;"><span class="s">Image 1 is the character</span> (identity reference), <span class="s">image 2 is the product</span>. The same courier from image 1… drinks from exactly the mug from image 2. Her turquoise backpack is on the floor next to her stool.</div>
      </div></div>"""
    return dict(tag=t("ПАТТЕРН 4 • КОМПОЗИЦИЯ", "PATTERN 4 • COMPOSITION"), info=t("ЧАСТЬ 4", "PART 4"), cls="visual-slide",
                title=t("Сцена из нескольких референсов: назовите роль каждой картинки", "A scene from several references: name the role of each image"),
                lead=t("Формула Google: [Картинки] + [Связь между ними] + [Новая сцена]", "Google's formula: [Images] + [Relationship] + [New scenario]"),
                body=body,
                notes=t("Главная ошибка — приложить три картинки и написать «объедини». Модель не знает, что откуда брать. Правильно: пронумеровать референсы и назвать роль каждого (персонаж, товар, стиль, фон). Так собирают рекламные сцены, примерку одежды, интерьер с конкретной мебелью.",
                        "The main mistake: attach three images and write \"combine\". The model does not know what to take from where. Instead number the references and name each one's role (character, product, style, background). This is how ad scenes, clothing try-ons and interiors with specific furniture are built."))


def s_api():
    code = """<span class="kw">from</span> google <span class="kw">import</span> genai
<span class="kw">from</span> google.genai <span class="kw">import</span> types
<span class="kw">from</span> PIL <span class="kw">import</span> Image

client = genai.<span class="fn">Client</span>()              <span class="cm"># key from Colab Secrets</span>
sheet = Image.<span class="fn">open</span>(<span class="str">"C1_sheet.png"</span>)       <span class="cm"># master reference</span>

resp = client.models.<span class="fn">generate_content</span>(
    model=<span class="str">"gemini-3.1-flash-image"</span>,       <span class="cm"># Nano Banana 2</span>
    contents=[sheet, PROMPT],               <span class="cm"># reference + text</span>
    config=types.<span class="fn">GenerateContentConfig</span>(
        response_modalities=[<span class="str">"IMAGE"</span>],
        image_config=types.<span class="fn">ImageConfig</span>(aspect_ratio=<span class="str">"4:3"</span>)))

<span class="kw">for</span> part <span class="kw">in</span> resp.parts:
    <span class="kw">if</span> part.inline_data:
        part.<span class="fn">as_image</span>().<span class="fn">save</span>(<span class="str">"scene_1.png"</span>)"""
    body = f"""<div class="dg-split l"><div class="dg-code" style="font-size:13.5px;">{code}</div>
      <div class="dg-col">
        <div class="dg-node flat" style="--nc:{C}"><div class="k">{t("ЗАЧЕМ ИНЖЕНЕРУ API", "WHY ENGINEERS NEED THE API")}</div>{ul([
            t("<b>Серия из 50 карточек товара</b> руками в чате — день работы; скриптом — минуты", "<b>A series of 50 product cards</b> by hand in chat is a day; by script, minutes"),
            t("<b>Промпт — шаблон с переменными:</b> товар, сцена, формат подставляются из таблицы", "<b>The prompt is a template:</b> product, scene and format come from a table"),
            t("<b>Журнал генераций:</b> модель, промпт, референсы, дата ➔ можно повторить и проверить", "<b>Generation log:</b> model, prompt, references, date ➔ reproducible and auditable")], C)}</div>
        {note(t("<b>Colab урока:</b> <code>notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb</code> — все паттерны этого урока в коде. Генерация картинок в API обычно платная; без биллинга используйте те же промпты в приложении Gemini или AI Studio.", "<b>Lesson Colab:</b> <code>notebooks/L04_Image_Generation_Prompts_and_Patterns.ipynb</code> — every pattern from this lesson in code. Image generation via API is usually paid; without billing use the same prompts in the Gemini app or AI Studio."))}
      </div></div>"""
    return dict(tag=t("ТО ЖЕ САМОЕ В КОДЕ", "SAME THING IN CODE"), info=t("ЧАСТЬ 5 • COLAB", "PART 5 • COLAB"),
                title=t("Паттерн «референс + промпт» через API: тот же SDK, что в L03", "The \"reference + prompt\" pattern via API: the same SDK as L03"),
                lead=t("Картинка — просто еще один элемент в contents; ответ — байты изображения вместо текста", "An image is just another item in contents; the response carries image bytes instead of text"),
                body=body,
                notes=t("Связываем с L03: тот же client.models.generate_content, только в contents добавляется картинка, а в config — response_modalities IMAGE. Вся галерея этого урока собрана скриптом examples/build_examples.py из prompts.json — это и есть журнал генераций. 10/90: вызов модели — малая часть; остальное — шаблоны, хранение, проверка.",
                        "Tie to L03: the same client.models.generate_content; contents gains an image and config gets response_modalities IMAGE. This lesson's whole gallery was built by examples/build_examples.py from prompts.json — that is the generation log. 10/90: the model call is the small part; the rest is templates, storage and review."))


def s_risks():
    risks = [
        (t("Текст и мелочи", "Text and small details"), t("короткий текст — надежно; плотный мелкий текст, руки в толпе, мелкие логотипы — ломаются", "short text is reliable; dense small text, hands in crowds, tiny logos still break"), A),
        (t("Дрейф при правках", "Drift during edits"), t("после многих правок «плывут» лицо и цвета ➔ одна правка за шаг, возврат к мастер-референсу", "after many edits faces and colors drift ➔ one edit per turn, return to the master reference"), A),
        (t("Факты в инфографике", "Facts in infographics"), t("модель может нарисовать неверные цифры; Google прямо советует их проверять", "the model may draw wrong numbers; Google explicitly says to verify them"), A),
        (t("Права и лица", "Rights and likeness"), t("в США картинка только по промпту не охраняется авторским правом; реальные люди и бренды — только с согласия", "in the US a prompt-only image is not copyrightable; real people and brands only with consent"), R),
        (t("Водяные знаки", "Provenance"), t("SynthID (невидимый) и C2PA (метаданные) у Google и OpenAI; C2PA теряется при скриншоте", "SynthID (invisible) and C2PA (metadata) on Google and OpenAI; C2PA is lost on screenshot"), C),
    ]
    rows = "".join(node(a, "", b, c, cls="flat").replace('<div class="t"></div>', "") for a, b, c in risks)
    zones = f"""<div class="dg-node" style="--nc:{G}"><div class="k">{t("ЗЕЛЕНАЯ", "GREEN")}</div><div class="d">{t("мудборды, иллюстрации к слайдам, раскадровки, идеи", "moodboards, slide illustrations, storyboards, ideas")}</div></div>
      <div class="dg-node" style="--nc:{A}"><div class="k">{t("ЖЕЛТАЯ • ЧЕЛОВЕК ПРОВЕРЯЕТ", "YELLOW • HUMAN REVIEWS")}</div><div class="d">{t("карточки товаров, баннеры, обложки YouTube, посты", "product cards, banners, YouTube thumbnails, posts")}</div></div>
      <div class="dg-node" style="--nc:{R}"><div class="k">{t("КРАСНАЯ • НЕ ГЕНЕРИРУЕМ", "RED • DO NOT GENERATE")}</div><div class="d">{t("документы и «доказательства», упаковка с составом, чужие логотипы, реальные люди без согласия", "documents and \"evidence\", packaging with ingredients, others' logos, real people without consent")}</div></div>"""
    body = f"""<div class="dg-split l"><div class="dg-col" style="gap:8px;">{rows}</div><div class="dg-col">{zones}</div></div>"""
    return dict(tag=t("РИСКИ И ОГРАНИЧЕНИЯ", "RISKS & LIMITS"), info=t("ЧАСТЬ 5 • BLAST RADIUS", "PART 5 • BLAST RADIUS"),
                title=t("Где генерация подводит и где ее нельзя применять", "Where generation fails and where it must not be used"),
                lead=t("Пять технических и юридических ограничений + светофор Blast Radius из L01", "Five technical and legal limits + the Blast Radius traffic light from L01"),
                body=body,
                notes=t("Технические риски: текст, мелкие детали, дрейф, неверные факты. Юридические: права на результат, лица и бренды. Водяные знаки: SynthID и C2PA — их ставят Google и OpenAI; это помогает отличать AI-картинки, но C2PA легко теряется. Светофор: зеленая — внутренние черновики, желтая — публичные материалы после проверки человеком, красная — не генерируем.",
                        "Technical risks: text, small details, drift, wrong facts. Legal: rights to the output, faces and brands. Provenance: SynthID and C2PA are applied by Google and OpenAI; they help identify AI images, but C2PA is easily lost. Traffic light: green — internal drafts, yellow — public materials after human review, red — do not generate."))


def s_homework():
    tracks = f"""<div class="grid-2" style="height:auto;">
      <div class="dg-node" style="--nc:{C}"><div class="k">{t("ТРЕК А • ФОТОСЕССИЯ ТОВАРА", "TRACK A • PRODUCT SHOOT")}</div><div class="t">{t("1 товар ➔ 4 кадра", "1 product ➔ 4 shots")}</div>
        <div class="d">{t("Снимите свой предмет на телефон (или сгенерируйте пэкшот) ➔ шот-лист: лайфстайл, флэтлей, в руках, баннер с текстом. Товар должен быть узнаваем в каждом кадре.", "Photograph your own object (or generate a packshot) ➔ shot list: lifestyle, flat lay, in hands, banner with text. The product must be recognizable in every shot.")}</div></div>
      <div class="dg-node" style="--nc:{G}"><div class="k">{t("ТРЕК Б • ПЕРСОНАЖ", "TRACK B • CHARACTER")}</div><div class="t">{t("Курьер доставки: лист + 3 сцены + 1 правка", "Delivery courier: sheet + 3 scenes + 1 edit")}</div>
        <div class="d">{t("Кейс курьера из L01: свой персонаж, лист персонажа, три сцены его рабочего дня и одна точечная правка (замена объекта или времени суток).", "The courier case from L01: your own character, a character sheet, three scenes from a working day and one targeted edit (object swap or time of day).")}</div></div></div>"""
    common = f"""<div class="dg-row">{node("1", t("Свободный ➔ структурный", "Free-form ➔ structured"), t("один кадр двумя промптами", "one shot with two prompts"), A)}{arrow()}{node("2", t("Два сервиса", "Two services"), t("один и тот же промпт, сравнение", "the same prompt, compared"), I)}{arrow()}{node("3", t("prompts.md", "prompts.md"), t("сервис, модель, дата, промпт для каждой картинки", "service, model, date, prompt for every image"), C)}{arrow()}{node("4", "qa.md", t("чек-лист: что сохранилось, что «уплыло»", "checklist: what held, what drifted"), G)}{arrow(t("коммит", "commit"), G)}{node(t("СДАЧА", "SUBMIT"), "genai-homeworks / L04 /", t("images/ + prompts.md + qa.md", "images/ + prompts.md + qa.md"), G)}</div>"""
    body = f"""<div class="dg">{tracks}{common}{note(t("<b>Инструменты:</b> любые два из пяти сервисов (бесплатных тарифов ChatGPT и Gemini достаточно). Colab урока — по желанию, для тех, кто хочет собрать серию скриптом. Шаблоны: <code>L04_05_Homework.md</code>.", "<b>Tools:</b> any two of the five services (ChatGPT and Gemini free tiers are enough). The lesson Colab is optional, for those who want to script the series. Templates: <code>L04_05_Homework_EN.md</code>."))}</div>"""
    return dict(tag=t("ДОМАШНЕЕ ЗАДАНИЕ №4", "HOMEWORK #4"), info=t("ДВА ТРЕКА НА ВЫБОР", "TWO TRACKS"),
                title=t("Домашнее задание: фотосессия товара или персонаж-курьер", "Homework: a product photo shoot or a courier character"),
                lead=t("Выберите трек; обязательная часть одинакова: сравнение промптов, двух сервисов и чек-лист", "Pick a track; the common part is the same: prompt comparison, two services and a checklist"),
                body=body,
                notes=t("Трек А — для тех, кому ближе e-commerce и маркетинг; Трек Б продолжает кейс курьера из L01. Оценка: виден ли переход от свободного промпта к структурному, сохранен ли товар/персонаж, честно ли заполнен qa.md (что «уплыло» — это не минус, а наблюдение).",
                        "Track A suits e-commerce and marketing; Track B continues the courier case from L01. Grading: is the move from free-form to structured visible, is the product/character preserved, is qa.md honest (drift is an observation, not a penalty)."))


def s_qa():
    body = f"""<div class="grid-2">
      <div class="c4-card accent-cyan"><div class="card-label" style="color: var(--c4-primary);">{t("4 ГЛАВНЫХ ВЫВОДА", "4 KEY TAKEAWAYS")}</div>
        <div style="display:flex;flex-direction:column;gap:16px;margin-top:10px;font-size:18.5px;color:#e2e8f0;line-height:1.5;">
          <div>{t("<strong>1. Выбирайте сервис под задачу:</strong> текст — ChatGPT, референсы и серии — Nano Banana/Kling, эстетика — Midjourney.", "<strong>1. Pick the service for the task:</strong> text — ChatGPT, references and series — Nano Banana/Kling, aesthetics — Midjourney.")}</div>
          <div>{t("<strong>2. Структура вместо одной фразы:</strong> объект, сцена, кадр, свет, стиль, обязательные детали, запреты.", "<strong>2. Structure instead of a phrase:</strong> subject, setting, framing, light, style, must-haves, constraints.")}</div>
          <div>{t("<strong>3. Правьте, а не перегенерируйте:</strong> «измени только X, сохрани остальное», одна правка за шаг.", "<strong>3. Edit, do not regenerate:</strong> \"change only X, keep the rest\", one edit per turn.")}</div>
          <div>{t("<strong>4. Консистентность = мастер-референс + якоря словами</strong> — для персонажа и для товара.", "<strong>4. Consistency = master reference + anchors in words</strong> — for characters and products.")}</div>
        </div></div>
      <div class="c4-card accent-purple"><div class="card-label" style="color: var(--c4-purple);">{t("СЛЕДУЮЩИЙ УРОК • L05", "NEXT LESSON • L05")}</div>
        <div class="card-title" style="font-size:23px;margin-top:6px;">{t("Генерация видео", "Video generation")}</div>
        <div class="card-desc" style="font-size:18.5px;line-height:1.6;margin-top:10px;">{t("Картинки этого урока станут первыми кадрами: image-to-video в Kling, Veo и других. Персонаж-курьер и кружка «оживут» — и появятся новые проблемы: движение, физика и консистентность во времени.", "Today's images become first frames: image-to-video in Kling, Veo and others. The courier and the mug will come alive — with new problems: motion, physics and consistency over time.")}</div></div>
    </div>
    <div style="margin-top:14px;text-align:center;font-size:18px;color:var(--c4-primary);font-weight:600;">{t("🎙 Открываем микрофоны — ваши вопросы", "🎙 Open mic — your questions")}</div>"""
    return dict(tag=t("ФИНАЛ ЗАНЯТИЯ", "WRAP-UP"), info=t("ИТОГИ И СЛЕДУЮЩИЙ ШАГ", "TAKEAWAYS & NEXT STEP"),
                title=t("Вопросы и ответы: главные итоги", "Q&A: key takeaways"),
                lead=t("Открытый микрофон и анонс урока о видео", "Open mic and a preview of the video lesson"),
                body=body,
                notes=t("Повторяем 4 вывода, отвечаем на вопросы, напоминаем про дедлайн домашки и папку genai-homeworks/L04/.",
                        "Repeat the 4 takeaways, answer questions, remind about the homework deadline and the genai-homeworks/L04/ folder."))
