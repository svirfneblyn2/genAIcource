"""L04 slide content. Every string is a t(ru, en) pair so RU/EN decks stay in parity."""

LANG = "ru"


def set_lang(lang: str) -> None:
    global LANG
    LANG = lang


def t(ru: str, en: str) -> str:
    return ru if LANG == "ru" else en


T = t

ARROW = '<div class="dg-arrow" style="--ac:{c}"><svg viewBox="0 0 54 14"><path d="M1 7H50M44 2L51 7L44 12"/></svg>{lbl}</div>'


def arrow(label: str = "", color: str = "var(--c4-primary)") -> str:
    return ARROW.format(c=color, lbl=f"<span>{label}</span>" if label else "")


def node(k: str, title: str, d: str = "", color: str = "var(--c4-primary)", extra: str = "", cls: str = "") -> str:
    dd = f'<div class="d">{d}</div>' if d else ""
    return f'<div class="dg-node {cls}" style="--nc:{color};"><div class="k">{k}</div><div class="t">{title}</div>{dd}{extra}</div>'


def fig(img: str, cap: str, tag: str = "", color: str = "var(--c4-primary)", contain: bool = False) -> str:
    tg = f'<span class="tagc">{tag}</span>' if tag else ""
    return (f'<div class="fig" style="--nc:{color}"><div class="ph{" contain" if contain else ""}">'
            f'<img src="assets/examples/web/{img}.jpg" alt="{img}"></div>'
            f'<div class="cap">{tg}{cap}</div></div>')


def note(text: str) -> str:
    return f'<div class="dg-note">{text}</div>'


def ul(items: list[str], color: str = "var(--c4-primary)") -> str:
    return f'<ul class="dl" style="--nc:{color}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


C, G, A, R, P, I = ("var(--c4-primary)", "var(--c4-success)", "var(--c4-warning)",
                    "var(--c4-danger)", "var(--c4-purple)", "var(--c4-indigo)")


# --------------------------------------------------------------------------- 01
def s01():
    return dict(
        cls="title-cover-slide", tag=t("GENAI BASICS • УРОК 04", "GENAI BASICS • LESSON 04"),
        info=t("МОДУЛЬ 2 • МУЛЬТИМОДАЛЬНОСТЬ", "MODULE 2 • MULTIMODALITY"), raw=True,
        body=f"""<div class="title-cover-centered">
          <div class="title-badge">{t("ПРАКТИКУМ", "HANDS-ON")}</div>
          <h1 class="title-main-h1">{t("Генерация изображений", "Image Generation")}</h1>
          <h2 class="title-sub-h2">{t("Сервисы, промпт-техники и паттерны контроля: от свободного промпта к фотосессии и консистентному персонажу",
                                      "Services, prompt techniques and control patterns: from a free-form prompt to a photo shoot and a consistent character")}</h2>
          <p class="title-lead-text">{t("ChatGPT, Nano Banana, Midjourney, Kling и Grok на одних и тех же задачах. Все картинки в этой презентации сгенерированы промптами, которые лежат в <code>examples/prompts.json</code> — их можно повторить вживую.",
                                        "ChatGPT, Nano Banana, Midjourney, Kling and Grok on the same tasks. Every image in this deck was generated from prompts stored in <code>examples/prompts.json</code> — you can rerun them live.")}</p>
        </div>""",
        notes=t("Приветствие. Открываем Модуль 2. Сегодня не про код, а про ремесло: какие сервисы есть, чем они отличаются и как писать промпты, чтобы получать предсказуемый результат. Все примеры на слайдах — реальные генерации, промпты в репозитории.",
                "Welcome. Module 2 starts today. Today is less about code and more about craft: which services exist, how they differ and how to prompt for predictable results. Every image on the slides is a real generation; prompts are in the repo."))


# --------------------------------------------------------------------------- 02
def s02():
    mods = [("01", t("Основы и API", "Foundations & API"), "L01–L03", "done"),
            ("02", t("Мультимодальность", "Multimodality"), t("L04 картинки • L05 видео • L06 звук", "L04 images • L05 video • L06 audio"), "here"),
            ("03", t("Среда инженера", "Engineer's toolkit"), "L07–L09", ""),
            ("04", t("Локальный AI", "Local AI"), "L10", ""),
            ("05", t("Агенты и MCP", "Agents & MCP"), "L11–L13", ""),
            ("06", t("Продакшен", "Production"), "L14–L16", "")]
    cells = []
    for num, name, sub, st in mods:
        if st == "here":
            ring, lab, col = f"3px solid {C}", t("ВЫ ЗДЕСЬ", "YOU ARE HERE"), C
        elif st == "done":
            ring, lab, col = f"2px solid {G}", t("ПРОЙДЕН", "DONE"), G
        else:
            ring, lab, col = "2px solid rgba(255,255,255,0.2)", t("МОДУЛЬ", "MODULE") + " " + num[1], "var(--text-dim)"
        cells.append(f"""<div style="display:flex;flex-direction:column;align-items:center;text-align:center;width:15%;z-index:3;">
          <div style="width:44px;height:44px;border-radius:50%;background:#0c111a;border:{ring};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:15px;color:{col};margin-bottom:10px;">{num}</div>
          <div style="font-size:11px;font-family:var(--font-mono);font-weight:700;color:{col};text-transform:uppercase;">{lab}</div>
          <div style="font-weight:700;font-size:14.5px;color:#fff;margin-top:3px;">{name}</div>
          <div style="font-size:12px;color:var(--text-muted);margin-top:2px;">{sub}</div></div>""")
    body = f"""<div style="background:#090e17;border:1px solid var(--border-card);border-radius:12px;padding:26px 20px;display:flex;flex-direction:column;gap:24px;">
      <div style="display:flex;align-items:center;justify-content:space-between;position:relative;">
        <div style="position:absolute;top:22px;left:40px;right:40px;height:3px;background:rgba(255,255,255,0.1);z-index:1;"></div>
        <div style="position:absolute;top:22px;left:40px;width:24%;height:3px;background:var(--c4-primary);z-index:2;"></div>
        {''.join(cells)}
      </div>
      <div style="background:rgba(56,189,248,0.05);border-left:4px solid var(--c4-primary);padding:12px 18px;border-radius:4px;font-size:14px;color:var(--text-muted);">
        {t("<strong>Связь с L02–L03:</strong> промпт для картинки подчиняется тем же законам — конкретика, структура, примеры (здесь — референс-изображения) и проверка результата. Новое сегодня: словарь фотографа, редактирование и консистентность.",
           "<strong>Link to L02–L03:</strong> an image prompt follows the same laws — specificity, structure, examples (here: reference images) and result checks. New today: the photographer's vocabulary, editing and consistency.")}
      </div></div>"""
    return dict(tag=t("МАРШРУТ ОБУЧЕНИЯ", "LEARNING PATH"), info=t("16 ЗАНЯТИЙ • 6 МОДУЛЕЙ", "16 LESSONS • 6 MODULES"),
                title=t("Дорожная карта курса: где мы находимся", "Course roadmap: where we are"),
                lead=t("Модуль 1 закрыт: токены, промпты, API. Открываем Модуль 2 — модели, которые работают с пикселями",
                       "Module 1 is done: tokens, prompts, API. Module 2 starts — models that work with pixels"),
                arena="zoom-up", body=body,
                notes=t("Мы прошли текстовый фундамент. Модуль 2: картинки, видео, звук. Важно: навыки промптинга из L02 переносятся почти полностью.",
                        "We finished the text foundation. Module 2: images, video, audio. Prompting skills from L02 transfer almost entirely."))


# --------------------------------------------------------------------------- 03
def s03():
    steps = [
        (t("ЧАСТЬ 1", "PART 1"), t("Как модель рисует", "How the model draws"), t("ментальная модель за 5 минут", "mental model in 5 minutes"), C),
        (t("ЧАСТЬ 2", "PART 2"), t("5 сервисов", "5 services"), t("ChatGPT • Nano Banana • Midjourney • Kling • Grok", "ChatGPT • Nano Banana • Midjourney • Kling • Grok"), I),
        (t("ЧАСТЬ 3", "PART 3"), t("Промпт-техники", "Prompt techniques"), t("свободный ➔ структурный ➔ детали ➔ итерации", "free-form ➔ structured ➔ details ➔ iteration"), A),
        (t("ЧАСТЬ 4", "PART 4"), t("Паттерны", "Patterns"), t("замена объекта • персонаж • фотосессия • композиция", "object swap • character • photo shoot • composition"), G),
        (t("ЧАСТЬ 5", "PART 5"), t("Риски и домашка", "Risks & homework"), t("права, водяные знаки, проверка", "rights, watermarks, review"), R),
    ]
    row = []
    for i, (k, tt, d, c) in enumerate(steps):
        row.append(node(k, tt, d, c))
        if i < len(steps) - 1:
            row.append(arrow())
    body = f"""<div class="dg"><div class="dg-row">{''.join(row)}</div>
      {note(t("<b>Главная мысль урока:</b> красивая картинка получается и от случайного промпта. Нужная картинка — от промпта, где вы сами приняли решения про объект, кадр, свет, стиль и запреты, и от умения править результат, а не генерировать заново.",
               "<b>Key idea:</b> a pretty picture comes even from a random prompt. The picture you need comes from a prompt where you made the decisions on subject, framing, light, style and constraints yourself — and from editing the result instead of regenerating it."))}</div>"""
    return dict(tag=t("ПЛАН ЗАНЯТИЯ", "AGENDA"), info=t("90 МИНУТ", "90 MINUTES"),
                title=t("Маршрут урока: пять частей", "Lesson route: five parts"),
                lead=t("Сначала понимаем инструмент, потом учимся им управлять", "First understand the tool, then learn to control it"),
                body=body,
                notes=t("Проговариваем план. Подчеркиваем: каждую технику покажем на реальных картинках.",
                        "Walk through the plan. Stress that every technique is shown on real images."))


# --------------------------------------------------------------------------- 04
def s04():
    diff = f"""<div class="dg-row">{node(t("ВХОД", "INPUT"), t("Шум + текст", "Noise + text"), t("старт с случайного шума", "start from random noise"), A)}{arrow(t("20–50 шагов", "20–50 steps"), A)}{node(t("ДИФФУЗИЯ", "DIFFUSION"), t("Пошаговое «проявление»", "Step-by-step denoising"), t("текст подсказывает, куда убирать шум", "text guides which noise to remove"), A)}{arrow("", A)}{node(t("ВЫХОД", "OUTPUT"), t("Картинка", "Image"), t("каждый запуск — новый шум ➔ новая картинка", "every run = new noise ➔ new image"), A)}</div>"""
    native = f"""<div class="dg-row">{node(t("ВХОД", "INPUT"), t("Диалог + картинки", "Chat + images"), t("текст, референсы, прошлые версии", "text, references, earlier versions"), G)}{arrow(t("одна модель", "one model"), G)}{node(t("НАТИВНО МУЛЬТИМОДАЛЬНАЯ", "NATIVE MULTIMODAL"), t("LLM, которая «пишет» картинку", "An LLM that \"writes\" the image"), t("понимает инструкцию и контекст разговора", "understands instructions and chat context"), G)}{arrow("", G)}{node(t("ВЫХОД", "OUTPUT"), t("Картинка + правки", "Image + edits"), t("«оставь всё, поменяй только…»", "\"keep everything, change only…\""), G)}</div>"""
    body = f"""<div class="dg">
      <div class="dg-lane" style="--nc:{A}"><div class="dg-lane-label"><b>{t("Диффузия", "Diffusion")}</b><small>Midjourney, FLUX, Stable Diffusion</small></div>{diff}</div>
      <div class="dg-lane" style="--nc:{G}"><div class="dg-lane-label"><b>{t("Чат-модели", "Chat models")}</b><small>ChatGPT Images, Nano Banana, Grok</small></div>{native}</div>
      {note(t("<b>Практический вывод:</b> чат-модели лучше слушаются длинных инструкций, пишут текст на картинке и правят «точечно». Диффузионные сервисы сильнее в эстетике и стиле, но чаще «перерисовывают всё». Внутри оба типа давно смешиваются — важно поведение, а не архитектура.",
               "<b>Practical takeaway:</b> chat models follow long instructions better, render text and do targeted edits. Diffusion services excel at aesthetics and style but tend to \"redraw everything\". Internally both types are blending — behavior matters, not architecture."))}
    </div>"""
    return dict(tag=t("МЕНТАЛЬНАЯ МОДЕЛЬ", "MENTAL MODEL"), info=t("ЧАСТЬ 1", "PART 1"),
                title=t("Как модель рисует: шум ➔ картинка и диалог ➔ картинка", "How the model draws: noise ➔ image and chat ➔ image"),
                lead=t("Два семейства генераторов — и почему от этого зависит, как писать промпт",
                       "Two families of generators — and why it changes how you prompt"),
                body=body,
                notes=t("Без формул. Диффузия: картинка «проявляется» из шума, текст подсказывает направление; новый запуск — новый шум, поэтому результат всегда разный. Чат-модели (GPT Image, Gemini Image) — это мультимодальная LLM: она читает весь диалог и прошлые картинки, поэтому умеет «поменяй только кружку». Это объясняет, почему для правок мы будем брать ChatGPT/Nano Banana, а для эстетики — Midjourney.",
                        "No formulas. Diffusion: the image emerges from noise, text steers it; each run starts from new noise, so results always differ. Chat models (GPT Image, Gemini Image) are multimodal LLMs that read the whole chat and earlier images, so they can \"change only the mug\". That is why we use ChatGPT/Nano Banana for edits and Midjourney for aesthetics."))


from slides_patterns import (s_api, s_character, s_consistency_how, s_edits, s_homework,  # noqa: E402
                             s_multiref, s_photoshoot, s_qa, s_risks)
from slides_prompts import s_break, s_details, s_free, s_iterate, s_struct, s_vocab  # noqa: E402
from slides_services import s_chatgpt, s_kling_grok, s_map, s_matrix, s_midjourney, s_nano  # noqa: E402

SLIDES = [
    s01, s02, s03, s04,                                          # intro + mental model
    s_map, s_chatgpt, s_nano, s_midjourney, s_kling_grok, s_matrix,  # part 2: services
    s_free, s_struct, s_details, s_vocab,                         # part 3: prompts
    s_break,
    s_iterate, s_edits, s_character, s_consistency_how, s_photoshoot, s_multiref,  # part 3-4
    s_api, s_risks, s_homework, s_qa,                             # part 5
]
