"""Part 3 (prompt techniques) and the break slide."""

from slides import A, C, G, P, R, arrow, fig, node, note, t, ul


def s_free():
    decided = [t("<b>Время и погода:</b> дождливый день, а не утро", "<b>Time & weather:</b> a rainy day, not a morning"),
               t("<b>Люди:</b> трое посетителей и бариста", "<b>People:</b> three guests and a barista"),
               t("<b>Детали:</b> камин, книжные полки, кот на подоконнике", "<b>Details:</b> fireplace, bookshelves, a cat on the sill"),
               t("<b>Кадр:</b> общий план, широкий угол", "<b>Framing:</b> wide shot, wide angle"),
               t("<b>Стиль:</b> «плёночное» фото в теплых тонах", "<b>Style:</b> warm \"film\" photo look")]
    body = f"""<div class="split-img wide">
      {fig("A1_free", t("Nano Banana Pro, первая же генерация", "Nano Banana Pro, first generation"), t("СВОБОДНЫЙ ПРОМПТ", "FREE-FORM"), A, contain=True)}
      <div class="col">
        <div class="pbox" style="--nc:{A}">a cozy coffee shop in the morning</div>
        <div class="dg-node flat" style="--nc:{A}"><div class="k">{t("ЧТО МОДЕЛЬ РЕШИЛА ЗА ВАС", "WHAT THE MODEL DECIDED FOR YOU")}</div>{ul(decided, A)}</div>
        {note(t("<b>Свободный стиль — это нормально</b> для поиска идей и мудборда. Но каждое слово, которое вы не написали, модель заполнит самым «средним» вариантом из обучающих данных.",
                 "<b>Free-form is fine</b> for ideation and moodboards. But every word you did not write gets filled with the most \"average\" option from the training data."))}
      </div></div>"""
    return dict(tag=t("ПРОМПТ-ТЕХНИКИ", "PROMPT TECHNIQUES"), info=t("ЧАСТЬ 3 • ШАГ 1", "PART 3 • STEP 1"),
                title=t("Свободный промпт: красиво, но решения принимает модель", "Free-form prompt: pretty, but the model makes the decisions"),
                lead=t("Шесть слов на входе — десятки неявных решений на выходе", "Six words in — dozens of implicit decisions out"),
                body=body,
                notes=t("Показываем картинку: получилось красиво. Спрашиваем аудиторию: это то, что вы хотели? Утро — а за окном дождь, люди, кот, камин. Модель не ошиблась — она заполнила пустоты. Отсюда переход к структуре.",
                        "Show the image: it is pretty. Ask the audience: is this what you wanted? Morning — yet rain outside, people, a cat, a fireplace. The model did not fail; it filled the gaps. Transition to structure."))


def s_struct():
    p = t("""<span class="s">Объект:</span> крапчатая кремовая кружка черного кофе с тонкой струйкой пара на старой дубовой стойке, в правой трети кадра.
<span class="s">Сцена:</span> маленькая кофейня в скандинавском стиле, 7 утра, пусто, стулья еще на столах.
<span class="s">Кадр и камера:</span> на уровне глаз, 35 мм, f/2.0, малая глубина резкости, резче всего — кружка.
<span class="s">Свет:</span> низкое теплое солнце из окна слева, длинные мягкие тени.
<span class="s">Стиль:</span> реалистичная редакционная фотография, легкое зерно.
<span class="x">Запреты:</span> без людей, без текста, без логотипов.""",
          """<span class="s">Subject:</span> a speckled cream ceramic mug of black coffee with a thin wisp of steam on a worn oak counter, right third of the frame.
<span class="s">Setting:</span> a small Scandinavian-style coffee shop at 7 a.m., empty, chairs still up on tables.
<span class="s">Composition & camera:</span> eye-level, 35mm, f/2.0, shallow depth of field, the mug is the sharpest object.
<span class="s">Lighting:</span> low warm sun from a window on the left, long soft shadows.
<span class="s">Style:</span> realistic editorial photography, slight film grain.
<span class="x">Constraints:</span> no people, no text, no logos.""")
    body = f"""<div class="split-img wider">
      <div class="col"><div class="pbox">{p}</div>
        {note(t("<b>Порядок слотов:</b> главное — в начале. Объект ➔ сцена ➔ кадр ➔ свет ➔ стиль ➔ запреты. Оригинальный английский промпт — <code>examples/prompts.json</code>, id <code>A2_structured</code>.",
                 "<b>Slot order:</b> most important first. Subject ➔ setting ➔ framing ➔ light ➔ style ➔ constraints. Full prompt: <code>examples/prompts.json</code>, id <code>A2_structured</code>."))}</div>
      {fig("A2_structured", t("Каждый слот выполнен: пустая кофейня, стулья на столах, кружка справа, свет слева", "Every slot honored: empty shop, chairs up, mug on the right, light from the left"), t("СТРУКТУРНЫЙ ПРОМПТ", "STRUCTURED"), G, contain=True)}
    </div>"""
    return dict(tag=t("ПРОМПТ-ТЕХНИКИ", "PROMPT TECHNIQUES"), info=t("ЧАСТЬ 3 • ШАГ 2", "PART 3 • STEP 2"),
                title=t("Структурный промпт: шесть слотов вместо одной фразы", "Structured prompt: six slots instead of one phrase"),
                lead=t("Та же идея «кофейня утром», но решения теперь принимаете вы", "Same idea, \"coffee shop in the morning\", but now you make the decisions"),
                body=body,
                notes=t("Читаем промпт по слотам и тут же показываем, где каждый слот на картинке. Это та же логика, что в L02 (роль, контекст, формат) — только слоты другие. Промпт для генерации писали на английском: подписи в обучающих данных в основном англоязычные, хотя современные чат-модели понимают и русский. Отдельно отметить: связный текст-описание работает лучше, чем список ключевых слов через запятую.",
                        "Read the prompt slot by slot and point at each slot in the image. Same logic as L02 (role, context, format) — only the slots differ. We wrote the generation prompt in English: training captions are mostly English, though modern chat models handle other languages. Note: a descriptive paragraph works better than a comma-separated keyword list."))


def s_details():
    body = f"""<div class="split-img wide">
      {fig("A3_details", t("Текст на табличке, круассан и лаванда — ровно как заказано", "Chalkboard text, croissant and lavender — exactly as ordered"), t("+ ВАЖНЫЕ ДЕТАЛИ", "+ MUST-HAVE DETAILS"), G, contain=True)}
      <div class="col">
        <div class="pbox" style="--nc:{G}"><span class="g">Must-have details:</span> {t("рядом с кружкой — черная меловая табличка, на которой рукописно написано ровно", "next to the mug, a small black chalkboard that reads exactly")} <span class="m">"FLAT WHITE 3.50"</span> {t("в первой строке и", "on the first line and")} <span class="m">"OPEN 7:00"</span> {t("во второй; один круассан на белой тарелке за кружкой; веточка лаванды в маленькой вазе.", "on the second; one croissant on a white plate behind the mug; a sprig of lavender in a tiny vase.")}</div>
        <div class="dg-node flat" style="--nc:{G}"><div class="k">{t("ПРАВИЛА ДЛЯ ДЕТАЛЕЙ", "RULES FOR DETAILS")}</div>{ul([
            t("<b>Текст — в кавычках</b> и со словом «ровно / exactly»; одна строка — одна фраза", "<b>Text in quotes</b> with \"exactly\"; one line, one phrase"),
            t("<b>Количество — числом:</b> «один круассан», а не «выпечка»", "<b>Counts as numbers:</b> \"one croissant\", not \"pastries\""),
            t("<b>Положение — явно:</b> «рядом с», «за», «в левой трети»", "<b>Position explicitly:</b> \"next to\", \"behind\", \"left third\""),
            t("<b>Материал и цвет — конкретно:</b> «черная меловая доска», а не «табличка»", "<b>Material & color concretely:</b> \"black chalkboard\", not \"a sign\""),
            t("<b>Запрет на лишнее:</b> «no other text» — иначе модель добавит вывески", "<b>Forbid extras:</b> \"no other text\" — otherwise it adds signage")], G)}</div>
      </div></div>"""
    return dict(tag=t("ПРОМПТ-ТЕХНИКИ", "PROMPT TECHNIQUES"), info=t("ЧАСТЬ 3 • ШАГ 3", "PART 3 • STEP 3"),
                title=t("Важные детали и текст на картинке: как их не потерять", "Must-have details and text in the image: how not to lose them"),
                lead=t("Добавляем к структурному промпту отдельный блок «обязательно» — и проверяем каждый пункт", "Add a separate \"must-have\" block to the structured prompt — and check every item"),
                body=body,
                notes=t("Сравниваем с предыдущим слайдом: сцена та же, добавились три детали и текст. Текст отрисован без ошибок — сильная сторона чат-моделей (GPT Image, Nano Banana). В Midjourney текст тоже возможен, но надежность ниже. Правило приемки: каждый пункт must-have — галочка в чек-листе.",
                        "Compare with the previous slide: same scene, plus three details and text. The text is rendered without errors — a strength of chat models (GPT Image, Nano Banana). Midjourney can render text too, but less reliably. Acceptance rule: every must-have item is a checklist tick."))


def s_vocab():
    rows = [
        (t("Ракурс", "Angle"), "eye-level • low angle • high angle • top-down / flat lay", t("уровень глаз — «документально», снизу — «героически»", "eye-level feels documentary, low angle heroic")),
        (t("План", "Shot size"), "extreme close-up • close-up • medium shot • full body • wide shot", t("сколько объекта и окружения в кадре", "how much subject vs environment")),
        (t("Объектив", "Lens"), "24mm wide • 35mm • 50mm • 85mm portrait • 100mm macro", t("85 мм — портреты, 24 мм — интерьеры, macro — текстуры", "85mm portraits, 24mm interiors, macro textures")),
        (t("Глубина резкости", "Depth of field"), "f/1.8 shallow DOF, bokeh • f/8 everything sharp", t("размытый фон отделяет объект", "a blurred background isolates the subject")),
        (t("Свет", "Lighting"), "golden hour • soft window light • softbox studio • rim light • hard noon sun", t("свет задает настроение сильнее, чем стиль", "light sets mood more than style does")),
        (t("Стиль / носитель", "Style / medium"), "editorial photo • 35mm film grain • packshot • watercolor • flat vector • 3D render", t("сначала носитель, потом эпоха и настроение", "medium first, then era and mood")),
        (t("Формат", "Aspect"), "16:9 • 4:5 • 1:1 • 9:16", t("задаем параметром сервиса, а не словами", "set via the service option, not words")),
    ]
    trs = "".join(f"<tr><td>{a}</td><td><code>{b}</code></td><td>{c}</td></tr>" for a, b, c in rows)
    body = f"""<div class="dg"><table class="tbl"><tr><th>{t("Слот", "Slot")}</th><th>{t("Слова, которые модель понимает", "Words models understand")}</th><th>{t("Что дает", "Effect")}</th></tr>{trs}</table>
      {note(t("<b>Почему это работает:</b> модели учились на миллионах фото с подписями, где встречаются именно эти термины. «85mm, f/1.8» — сжатая инструкция сразу на десяток визуальных решений.",
               "<b>Why it works:</b> models learned from millions of captioned photos that use exactly these terms. \"85mm, f/1.8\" is a compressed instruction for a dozen visual decisions."))}</div>"""
    return dict(tag=t("ПРОМПТ-ТЕХНИКИ", "PROMPT TECHNIQUES"), info=t("ЧАСТЬ 3 • ШПАРГАЛКА", "PART 3 • CHEAT SHEET"),
                title=t("Словарь фотографа: короткие слова с самым сильным эффектом", "The photographer's vocabulary: short words, big effect"),
                lead=t("Не нужно быть фотографом — достаточно знать 30 терминов", "You do not need to be a photographer — 30 terms are enough"),
                body=body,
                notes=t("Это раздаточная шпаргалка. Разбираем 2–3 примера: 85 мм + f/1.8 = портрет с размытым фоном; top-down = флэтлей для товаров; golden hour = теплый мягкий свет. Формат кадра задаем параметром (--ar в Midjourney, выбор формата в ChatGPT и Gemini), а не словами.",
                        "This is a handout. Walk through 2–3 examples: 85mm + f/1.8 = portrait with a blurred background; top-down = product flat lay; golden hour = warm soft light. Aspect ratio is a service option (--ar in Midjourney, a format option in ChatGPT and Gemini), not words."))


def s_break():
    body = f"""<div class="slide-content-arena"><div class="break-timer-card">
        <div style="font-size: 42px; margin-bottom: 6px;">☕</div>
        <h2 style="font-size: 28px; font-weight: 800; color: #fff; margin-bottom: 8px;">{t("Экватор занятия: кофе-пауза", "Halfway: coffee break")}</h2>
        <p style="font-size: 15.5px; color: var(--text-muted); max-width: 580px; line-height: 1.5;">{t("Пять минут отдыха. Во второй части — итерации и паттерны: замена объекта, один персонаж в разных сценах, фотосессия товара и сцена из нескольких референсов.", "Five minutes of rest. Part two: iteration and patterns — object swap, one character across scenes, a product photo shoot and a scene built from several references.")}</p>
        <div class="break-timer-digits" id="breakTimerDisplay">05:00</div>
        <div class="timer-btn-row">
          <button class="timer-btn" id="timerToggleBtn" onclick="toggleBreakTimer()">{t("СТАРТ 5 МИН", "START 5 MIN")}</button>
          <button class="timer-btn secondary" onclick="resetBreakTimer()">{t("СБРОС", "RESET")}</button>
        </div></div></div>"""
    return dict(tag=t("ПЕРЕРЫВ 5 МИНУТ", "5-MINUTE BREAK"), info=t("ЭКВАТОР ЗАНЯТИЯ", "HALFWAY"), raw=True, body=body,
                notes=t("Включаем таймер. Никаких заданий в чат — только отдых.", "Start the timer. No chat tasks — rest only."))


def s_iterate():
    loop = f"""<div class="dg-row">{node("1", t("Черновик", "Draft"), t("структурный промпт, 2–4 варианта", "structured prompt, 2–4 candidates"), C)}{arrow()}{node("2", t("Выбор", "Pick"), t("лучший по чек-листу must-have", "best one against the must-have list"), C)}{arrow()}{node("3", t("Одна правка", "One edit"), t("«оставь всё, измени только X»", "\"keep everything, change only X\""), G)}{arrow()}{node("4", t("Проверка", "Check"), t("что еще «уплыло»?", "what else drifted?"), A)}{arrow(t("повтор", "repeat"), A)}{node("5", t("Финал", "Final"), t("апскейл, сохранить промпт", "upscale, save the prompt"), P)}</div>"""
    rules = [
        t("<b>Одна правка за шаг.</b> Три изменения сразу — и непонятно, какое что сломало", "<b>One edit per turn.</b> Three changes at once and you cannot tell which broke what"),
        t("<b>Называйте, что сохранить:</b> ракурс, кадр, свет, фон", "<b>Name what to keep:</b> angle, framing, light, background"),
        t("<b>Правьте, а не генерируйте заново,</b> если 80% картинки уже устраивает", "<b>Edit, do not regenerate,</b> when 80% of the image already works"),
        t("<b>Длинный диалог «устает»:</b> после 6–8 правок начните новый чат, приложив лучшую картинку", "<b>Long chats degrade:</b> after 6–8 edits start a new chat with the best image attached"),
        t("<b>Сохраняйте финальный промпт</b> — это рецепт для следующей серии", "<b>Save the final prompt</b> — it is the recipe for the next series"),
    ]
    tpl = t("Отредактируй это фото. Замени <span class='m'>только</span> X на Y.\n<span class='g'>Сохрани без изменений:</span> ракурс, кадрирование, фон, направление света и тени.\nНовый объект должен отбрасывать такую же тень.",
            "Edit this photo. Replace <span class='m'>only</span> X with Y.\n<span class='g'>Keep exactly the same:</span> camera angle, framing, background, light direction and shadows.\nThe new object must cast a matching shadow.")
    body = f"""<div class="dg">{loop}<div class="grid-2" style="height:auto;"><div class="dg-node flat" style="--nc:{G}"><div class="k">{t("ПРАВИЛА ИТЕРАЦИЙ", "ITERATION RULES")}</div>{ul(rules, G)}</div>
      <div class="col"><div class="pbox" style="--nc:{G}">{tpl}</div>
      {note(t("<b>Шаблон правки</b> работает в ChatGPT, Nano Banana и Grok. В Midjourney то же делается инструментом Edit: выделяете зону (inpaint) и описываете, что там должно быть.", "<b>The edit template</b> works in ChatGPT, Nano Banana and Grok. In Midjourney use the Edit tool: select the area (inpaint) and describe what belongs there."))}</div></div></div>"""
    return dict(tag=t("ПРОМПТ-ТЕХНИКИ", "PROMPT TECHNIQUES"), info=t("ЧАСТЬ 3 • ШАГ 4", "PART 3 • STEP 4"),
                title=t("Итерация: правим диалогом, а не крутим барабан", "Iteration: edit through dialogue, do not spin the slot machine"),
                lead=t("Профессионалы редко получают результат с первой генерации — они доводят лучший черновик", "Pros rarely nail it on the first try — they refine the best draft"),
                body=body,
                notes=t("Ключевой навык. Новички жмут «перегенерировать» 20 раз. Правильно: выбрать лучший черновик и править его точечно, каждый раз называя, что сохранить. Следующий слайд показывает, как это выглядит на практике.",
                        "Key skill. Beginners hit regenerate 20 times. Instead pick the best draft and edit it surgically, each time naming what to keep. The next slide shows what that looks like."))
