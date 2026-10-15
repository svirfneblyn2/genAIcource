# -*- coding: utf-8 -*-
"""Build the L09 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Same engine and look as L05 deck_v2: every slide is one function, text is t("ru", "en").
Demo screenshots come from make_demo.py (run it first). Facts: ../L09_08_Source_Notes_Research_2026-10.md.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from icons import ico, ico_svg

HERE = Path(__file__).resolve().parent
L09 = HERE.parent
NAME = "presentation_L09_Claude_Ecosystem_and_Artifacts"
OUT = {"ru": L09 / f"{NAME}.html", "en": L09 / f"{NAME}_EN.html"}
IMG = "assets/img/"

LANG = "ru"

C = dict(bg="#0b0f17", surf="#121a28", card="#0f1624", line="#2b3648", fg="#f1f5f9", mut="#a3b1c4", dim="#6b7a90",
         cyan="#38bdf8", green="#34d399", amber="#fbbf24", red="#f87171", violet="#c084fc", pink="#f472b6", ico="#c9d4e3")


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 09 • Экосистема Claude и артефакты", "en": "GenAI Basics • Lesson 09 • Claude Ecosystem and Artifacts"}


def head(kicker, title, lead=None, k=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    s = f'<div class="kicker"{ks}>{kicker}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


def demo(n):
    return f"{IMG}demo_v{n}_{LANG}.png"


# ---------------------------------------------------------------- svg helpers
def svg(w, h, body):
    return (f'<svg class="svgfig" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Onest, Segoe UI, Arial, sans-serif">{body}</svg>')


def txt(x, y, s, size=20, color=C["fg"], weight=400, anchor="start", mono=False):
    fam = ' font-family="JetBrains Mono, Consolas, monospace" letter-spacing="1.5"' if mono else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}"{fam}>{s}</text>'


def panel(x, y, w, h, stroke=C["line"], fill=C["surf"], r=14, sw=1.2, dash=False):
    d = ' stroke-dasharray="6 6"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def arrow_defs(color=C["dim"], mid="a"):
    return (f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 Z" fill="{color}"/></marker></defs>')


def line(x1, y1, x2, y2, color=C["dim"], sw=2, mid="a", dash=False):
    d = ' stroke-dasharray="6 6"' if dash else ""
    m = f' marker-end="url(#{mid})"' if mid else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d}{m}/>'


def path(d, color=C["dim"], sw=2, mid="a", dash=False):
    ds = ' stroke-dasharray="6 6"' if dash else ""
    m = f' marker-end="url(#{mid})"' if mid else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{ds}{m}/>'


# ---------------------------------------------------------------- 01 cover
def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg"><img src="{IMG}cover.jpg" alt=""></div>
  <div class="shade"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 09 • Модуль 3: ИИ-ассистенты в работе", "GenAI Basics • Lesson 09 • Module 3: AI assistants at work")}</div>
    <h1>{t("Экосистема Claude и артефакты", "Claude Ecosystem and Artifacts")}</h1>
    <h2>{t("От ответа в чате — к вещи, которой можно пользоваться", "From a chat answer to something people can use")}</h2>
    <p>{t("Где живёт Claude, что такое артефакт, как попросить его так, чтобы результат можно было проверить, и чем делиться безопасно. Состояние на октябрь 2026.",
           "Where Claude lives, what an artifact is, how to ask for one so the result can be checked, and what is safe to share. As of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>
  <div class="keys" style="left:auto;right:30px">Image: Anthropic (claude.com)</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. В L07 мы смотрели экосистему Microsoft Copilot. Сегодня — второй большой ассистент, Claude от Anthropic, и его главная фишка: артефакты.",
                      "⏱ 2 min. Welcome. In L07 we looked at the Microsoft Copilot ecosystem. Today it is the second big assistant, Claude by Anthropic, and its signature feature: artifacts."),
                    t("План: где живёт Claude → что такое артефакт → как его заказать и проверить (живое демо) → перерыв → артефакт как приложение, проекты, коннекторы, скиллы → безопасность → домашка.",
                      "Plan: where Claude lives → what an artifact is → how to order and check one (live demo) → break → the artifact as an app, projects, connectors, skills → safety → homework.")))


# ---------------------------------------------------------------- 03 ecosystem map
def eco_svg():
    W, H = 1450, 560
    cols = [
        ("cyan", t("РАЗГОВАРИВАТЬ", "TALK"), [
            ("chat", t("Чат Claude", "Claude chat"), t("сайт, ПК, телефон", "web, PC, phone")),
            ("folder", t("Проекты", "Projects"), t("файлы + правила темы", "files + topic rules")),
        ]),
        ("green", t("СОЗДАВАТЬ ВЕЩИ", "MAKE THINGS"), [
            ("app", t("Артефакты", "Artifacts"), t("документ, слайды…", "doc, slides…")),
            ("sheet", t("Claude в Office", "Claude in Office"), "Excel, Word, PowerPoint"),
        ]),
        ("violet", t("ДЕЛАТЬ ЗА ВАС", "ACT FOR YOU"), [
            ("loop", t("Длинные задачи", "Long tasks"), t("много шагов сам", "many steps by itself")),
            ("globe", t("Claude в Chrome", "Claude in Chrome"), t("кликает в браузере", "clicks in the browser")),
        ]),
        ("amber", t("ДЛЯ РАЗРАБОТЧИКОВ", "FOR DEVELOPERS"), [
            ("terminal", "Claude Code", t("пишет код", "writes code")),
            ("key", "API", t("в вашей программе", "in your program")),
        ]),
    ]
    b = arrow_defs()
    cw, gap, x0, top = 335, 37, 0, 70
    for i, (k, tag, items) in enumerate(cols):
        x = x0 + i * (cw + gap)
        hl = k == "green"
        b += panel(x, top, cw, 330, stroke=C[k] if hl else C["line"], sw=2.4 if hl else 1.2)
        b += txt(x + 24, top + 42, tag, 19, C[k], 700, mono=True)
        for j, (ic, nm, ds) in enumerate(items):
            y = top + 74 + j * 124
            b += ico(ic, x + 24, y, 46, C["ico"] if not hl else C["green"])
            b += txt(x + 88, y + 20, nm, 24, C["fg"], 700)
            b += txt(x + 88, y + 50, ds, 18, C["mut"])
        b += line(x + cw / 2, top + 330, x + cw / 2, 452, C["line"], 2, None)
    # shared layer
    b += panel(0, 452, W, 96, stroke=C["line"], fill=C["card"])
    b += ico("chip", 24, 476, 48, C["cyan"])
    b += txt(90, 497, t("Одни и те же модели Claude", "The same Claude models"), 24, C["fg"], 700)
    b += txt(90, 527, t("Fable · Opus · Sonnet · Haiku — выбор в меню модели", "Fable · Opus · Sonnet · Haiku — pick in the model menu"), 18, C["mut"])
    b += ico("plug", 760, 478, 42, C["ico"])
    b += ico("skill", 812, 478, 42, C["ico"])
    b += txt(872, 497, t("Коннекторы и скиллы", "Connectors and skills"), 22, C["fg"], 700)
    b += txt(872, 527, t("подключаются к любому из этих мест", "plug into any of these places"), 18, C["mut"])
    b += txt(W / 2, 30, t("Одна модель — много «мест», где с ней работают", "One model — many places to work with it"), 20, C["dim"], 400, "middle")
    return svg(W, H, b)


def s_eco():
    return dict(min=4, html=f'''
  {head(t("Карта", "Map"), t("Где живёт Claude", "Where Claude lives"))}
  <div class="body">{eco_svg()}
    <div class="note" style="margin-top:18px;--k:var(--green)">{t("Сегодня — в основном <b>зелёная колонка</b>: артефакты. Агентов (длинные задачи, Code) разберём в уроках 11 и 16.", "Today is mostly the <b>green column</b>: artifacts. Agents (long tasks, Code) come in lessons 11 and 16.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Главная мысль: Claude — это не одно окно чата, а одна модель, к которой ведут разные «двери». Двери отличаются тем, сколько Claude делает сам.",
                      "⏱ 4 min. Key idea: Claude is not a single chat window but one model reached through different “doors”. The doors differ in how much Claude does by itself."),
                    t("Разговаривать: обычный чат на сайте claude.ai, в приложении для Windows/Mac и на телефоне; проекты — папка с файлами и правилами под одну тему.",
                      "Talk: the normal chat on claude.ai, in the Windows/Mac app and on the phone; projects are a folder of files and rules for one topic."),
                    t("Создавать вещи: артефакты — главная тема сегодня; плюс Claude прямо внутри Excel и PowerPoint.",
                      "Make things: artifacts — today’s main topic; plus Claude right inside Excel and PowerPoint."),
                    t("Делать за вас: Claude сам выполняет длинные многошаговые задачи и работает в браузере — подробнее на слайде 19. Для разработчиков: Claude Code и API.",
                      "Act for you: Claude carries out long multi-step tasks itself and works in the browser — more on slide 19. For developers: Claude Code and the API."),
                    t("Внизу общий слой: модели одни и те же, коннекторы и скиллы подключаются везде. Аналогия с L07: у Microsoft тоже один Copilot в разных приложениях.",
                      "At the bottom is the shared layer: the models are the same, connectors and skills plug in everywhere. Analogy with L07: Microsoft also has one Copilot across different apps.")))



def s_terms():
    terms = [
        ("green", "app", t("Артефакт", "Artifact"), t("готовая вещь рядом с чатом: документ, слайды, дашборд", "a finished thing next to the chat: doc, slides, dashboard")),
        ("cyan", "folder", t("Проект", "Project"), t("папка: файлы + правила для одной темы", "a folder: files + rules for one topic")),
        ("violet", "memory", t("Память", "Memory"), t("что Claude помнит о вас между чатами", "what Claude remembers about you across chats")),
        ("amber", "plug", t("Коннектор", "Connector"), t("доступ к вашему сервису: Drive, Gmail, GitHub", "access to your service: Drive, Gmail, GitHub")),
        ("pink", "skill", t("Скилл", "Skill"), t("готовый рецепт: «как делать отчёт»", "a ready recipe: “how to build a report”")),
        ("red", "loop", t("Агент", "Agent"), t("сам делает много шагов к цели", "takes many steps towards a goal by itself")),
    ]
    tt = "".join(f'<div style="display:grid;grid-template-columns:76px 1fr;gap:18px;align-items:start;border-left:4px solid var(--{k});padding:10px 0 10px 20px">'
                 f'{ico_svg(ic, 64, "var(--" + k + ")")}<div><div style="font-size:32px;font-weight:700">{h}</div>'
                 f'<div class="cap" style="font-size:21px;margin-top:4px">{d}</div></div></div>'
                 for k, ic, h, d in terms)
    return dict(min=3, html=f'''
  {head(t("Словарь урока", "Lesson vocabulary"), t("Шесть слов, которые понадобятся сегодня", "Six words you will need today"))}
  <div class="body"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:44px 40px">{tt}</div>
    <div class="note" style="margin-top:40px">{t("Похожее было в L07: у Copilot тоже есть агенты, коннекторы и память. <b>Названия разные — идеи те же.</b>", "You saw similar things in L07: Copilot also has agents, connectors and memory. <b>Different names — same ideas.</b>")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Пройдитесь по каждому слову одной фразой и примером. Дальше эти слова встречаются без объяснений.",
                      "⏱ 3 min. Go through each word with one sentence and one example. Later these words appear without explanation."),
                    t("Артефакт — главный. Проект — как папка на рабочем столе, только Claude читает всё, что в ней. Память — короткие заметки о вас, их можно посмотреть и стереть. Коннектор — «ключ» к одному сервису, работает с вашими правами. Скилл — инструкция плюс файлы, которые Claude открывает, когда задача подходит. Агент — Claude, который не просто отвечает, а сам выполняет шаги: открывает файлы, сайты, собирает результат.",
                      "The artifact is the main one. A project is like a desktop folder, except Claude reads everything in it. Memory is short notes about you that you can view and erase. A connector is a “key” to one service and uses your permissions. A skill is instructions plus files that Claude opens when the task fits. An agent is Claude that doesn’t just answer but carries out steps itself: opens files and sites, assembles the result.")))


# ---------------------------------------------------------------- 14 break
def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2>{t("5 минут", "5 minutes")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("После перерыва: живое демо, проекты, коннекторы, безопасность.", "After the break: live demo, projects, connectors, safety.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Перерыв. Запустите таймер.", "⏱ 5 min. Break. Start the timer.")))



# ================================================================ v2 slides (real claude.ai screens)
SCR = "assets/img/scr_"
CREDIT = {"ru": "Скриншот: claude.ai, 13.10.2026, аккаунт автора курса (история чатов размыта)",
          "en": "Screenshot: claude.ai, 13 Oct 2026, the course author’s account (chat history blurred)"}


def credit():
    return f'<div class="small" style="margin-top:6px">{CREDIT[LANG]}</div>'


def shot_with(img, marks, extra=""):
    """marks: (k, n, left%, top%, w%, h%) — ring + number badge at the ring's top-right corner."""
    m = ""
    for mk in marks:
        k, n, l, tp, w, h = mk[:6]
        pos = f"left:{l + w}%;top:{tp}%"
        if len(mk) > 6 and mk[6] == "r":  # badge to the right of the ring, vertically centred
            pos = f"left:{l + w}%;top:{tp + h / 2}%;transform:translate(25%,-50%)"
        m += f'<div class="ring" style="--k:var(--{k});left:{l}%;top:{tp}%;width:{w}%;height:{h}%"></div>'
        m += f'<div class="num" style="--k:var(--{k});{pos}">{n}</div>'
    return f'<div class="shot" {extra}><img src="{img}" alt="">{m}</div>'


def legend(items, size=None):
    st = f' style="font-size:{size}px"' if size else ""
    return '<div class="legend">' + "".join(
        f'<div class="lg" style="--k:var(--{k})"><span class="num">{n}</span><div><div class="h"{st}>{h}</div>'
        + (f'<div class="d">{d}</div>' if d else "") + '</div></div>'
        for k, n, h, d in items) + "</div>"


def img(name, style=""):
    return f'<img src="{SCR}{name}.jpg" alt="" style="width:100%;display:block;border-radius:12px;border:1px solid var(--line);{style}">'


# ---------------------------------------------------------------- 02 hook: gallery
def s_hook():
    chips = [("slides", t("Слайды", "Slides")), ("app", t("Тренажёр", "Coach app")), ("diagram", t("Схема", "Diagram")),
             ("doc", t("Документ", "Document")), ("design", t("Лендинг", "Landing page")), ("dash", t("Дашборд", "Dashboard"))]
    cc = "".join(f'<span class="chip on" style="font-size:19px;display:inline-flex;align-items:center;gap:8px;padding:6px 12px">{ico_svg(ic, 24, "#c9d4e3", 1.8)}{n}</span>' for ic, n in chips)
    return dict(min=4, html=f'''
  {head(t("Зачем этот урок", "Why this lesson"), t("Шесть рабочих вещей — по одной фразе на каждую", "Six working things — one sentence each"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:40px;align-items:center;">
      <div>{img("gallery")}{credit()}</div>
      <div class="stack" style="gap:20px">
        <div class="bubble me" style="font-size:22px">{t("«Сделай презентацию на 5 слайдов для новых курьеров…»", "“Make a 5-slide deck for new couriers…”")}</div>
        <div class="cap" style="font-size:22px">{t("Так выглядит вкладка <b>Artifacts</b> после 10 минут подготовки к уроку. Каждая плитка — отдельная вещь: её можно открыть, поправить, скачать, показать коллеге.",
                                                      "This is the <b>Artifacts</b> tab after 10 minutes of preparing this lesson. Each tile is a separate thing: open it, edit it, download it, show it to a colleague.")}</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px">{cc}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Покажите галерею и спросите: «Сколько времени у вас ушло бы на любую из этих вещей вручную?» Все шесть сделаны при подготовке урока, каждая — одной-двумя фразами (промпты — в demo_assets/prompts_ru.md).",
                      "⏱ 4 min. Show the gallery and ask: “How long would any of these take you by hand?” All six were made while preparing the lesson, each from one or two sentences (prompts in demo_assets/prompts_en.md)."),
                    t("Сегодня: где живёт Claude, как устроено окно, какие бывают артефакты, живое демо «таблица → дашборд → слайды», проекты и коннекторы, и чем безопасно делиться.",
                      "Today: where Claude lives, how the window works, what artifacts exist, a live demo “table → dashboard → slides”, projects and connectors, and what is safe to share.")))


# ---------------------------------------------------------------- 05 main window
def s_window():
    W, H = 1250, 490
    p = lambda x1, y1, x2, y2: (round(x1 / W * 100, 2), round(y1 / H * 100, 2), round((x2 - x1) / W * 100, 2), round((y2 - y1) / H * 100, 2))
    marks = [("cyan", 1, *p(8, 52, 278, 84), "r"), ("cyan", 2, *p(8, 88, 278, 116), "r"), ("green", 3, *p(8, 120, 278, 148), "r"),
             ("violet", 4, *p(206, 8, 280, 40), "r"), ("amber", 5, *p(592, 336, 1232, 440)), ("amber", 6, *p(598, 398, 634, 432), "r"),
             ("pink", 7, *p(1034, 446, 1160, 472), "r")]
    lg = [("cyan", 1, t("New — новый чат", "New — a new chat"), ""),
          ("cyan", 2, t("Projects — папки под темы", "Projects — folders for topics"), ""),
          ("green", 3, t("Artifacts — всё, что сделано", "Artifacts — everything you made"), ""),
          ("violet", 4, t("Чат ↔ Code — два режима", "Chat ↔ Code — two modes"), ""),
          ("amber", 5, t("Поле ввода: просьба или вопрос", "Input box: a request or question"), ""),
          ("amber", 6, t("«+» — файлы, коннекторы, поиск", "“+” — files, connectors, research"), ""),
          ("pink", 7, t("Модель и «усилие»", "Model and effort"), "")]
    return dict(min=6, html=f'''
  {head(t("Интерфейс", "Interface"), t("Главное окно: что где", "The main window: what is where"))}
  <div class="body">
    <div class="row" style="grid-template-columns:2.3fr 1fr;gap:30px;align-items:center;">
      <div>{shot_with(SCR + "main.jpg", marks)}{credit()}</div>
      {legend(lg, 21)}
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Тур по окну claude.ai (то же в приложении для Windows/Mac). Слева боковая панель: New — новый чат; Projects — проекты; Artifacts — все артефакты; ниже — закреплённые проекты и история чатов (на скриншоте размыта).",
                      "⏱ 6 min. A tour of the claude.ai window (the same in the Windows/Mac app). Left sidebar: New — a new chat; Projects; Artifacts — everything you made; below — pinned projects and chat history (blurred on the screenshot)."),
                    t("Вверху слева — переключатель «чат / Code»: Code — режим для программистов (слайд 19). В центре — поле ввода; «+» открывает файлы, скиллы, коннекторы, Research, память. Под полем — выбор модели (следующий слайд).",
                      "Top left — the chat / Code toggle: Code is the programmers’ mode (slide 19). In the centre — the input box; “+” opens files, skills, connectors, Research, memory. Under the box — the model picker (next slide)."),
                    t("Живьём: откройте claude.ai и покажите эти 7 мест на своём экране. В Teams — делитесь окном браузера, а не всем экраном, и откройте новый чат, чтобы не светить историю.",
                      "Live: open claude.ai and point at these 7 places on your own screen. In Teams share the browser window, not the whole screen, and open a new chat so your history isn’t visible.")))


# ---------------------------------------------------------------- 06 models
def s_models():
    rows = [("violet", "Fable 5.1", "For your toughest challenges", t("самые сложные задачи; медленнее и дороже", "the hardest tasks; slower and pricier")),
            ("cyan", "Opus 5.5", "For complex work and everyday tasks", t("<b>хороший выбор по умолчанию</b>", "<b>a good default</b>")),
            ("green", "Sonnet 5.5", "Most efficient for simpler tasks", t("простые задачи, экономит лимит", "simpler tasks, saves your limit")),
            ("amber", "Haiku 5.5", "Fastest for quick answers", t("быстрые короткие ответы", "quick short answers"))]
    rr = "".join(f'<div style="display:grid;grid-template-columns:200px 1fr;gap:18px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)">'
                 f'<div style="font-size:30px;font-weight:800;color:var(--{k})">{n}</div><div><div class="cap" style="font-size:22px;color:var(--fg)">{d}</div>'
                 f'<div style="font-family:var(--mono);font-size:15px;color:var(--dim);margin-top:2px">«{ui}»</div></div></div>' for k, n, ui, d in rows)
    return dict(min=3, html=f'''
  {head(t("Модели", "Models"), t("Одно меню — четыре модели", "One menu — four models"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:44px;align-items:center;">
      <div>{img("models")}{credit()}</div>
      <div class="stack" style="gap:0">{rr}
        <div class="note" style="margin-top:18px">{t("Правило: <b>умнее → медленнее и быстрее тратит лимит</b>. Effort — сколько модель «думает» перед ответом.", "Rule: <b>smarter → slower and uses your limit faster</b>. Effort — how long the model “thinks” before answering.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Меню открывается кликом по названию модели под полем ввода. Подписи в меню — официальные (в кавычках на слайде). Названия меняются несколько раз в год, принцип — нет.",
                      "⏱ 3 min. The menu opens by clicking the model name under the input box. The captions are the official ones (in quotes on the slide). Names change several times a year; the principle doesn’t."),
                    t("Для учёбы хватает модели, которая стоит по умолчанию. Fable включают для очень сложных задач. На бесплатном плане выбор моделей меньше.",
                      "For learning, the default model is enough. Fable is for very hard tasks. The free plan offers fewer models.")))


# ---------------------------------------------------------------- 07 plans
def s_plans():
    cols = [("green", t("Бесплатно", "Free"), "$0", [t("чат на сайте, ПК и телефоне", "chat on web, PC and phone"), t("артефакты: Docs, Slides, Design", "artifacts: Docs, Slides, Design"),
                                                    t("поиск в интернете, память", "web search, memory"), t("до 5 проектов, коннекторы", "up to 5 projects, connectors")]),
            ("cyan", "Pro", t("$20 в месяц", "$20 / month"), [t("всё из Free, больше лимит", "everything in Free, a bigger limit"), t("Claude Code, Research", "Claude Code, Research"),
                                                             t("Claude в Chrome и в Office", "Claude in Chrome and Office"), t("Dashboards, данные в артефактах", "Dashboards, data in artifacts")]),
            ("violet", "Max · Team · Enterprise", t("Max от $100 · Team от $20 за место", "Max from $100 · Team from $20 a seat"), [t("Max — в 5–20 раз больше лимит", "Max — 5–20× the limit"), t("Team — общий доступ в компании", "Team — sharing inside the company"),
                                                                                              t("админ, единый вход", "admin controls, single sign-on"), t("данные не идут на обучение по умолчанию", "data not used for training by default")])]
    cc = "".join(f'<div style="display:flex;flex-direction:column;gap:12px;border-top:4px solid var(--{k});background:var(--surface-card);border-radius:12px;padding:22px 24px">'
                 f'<div style="font-size:30px;font-weight:800">{h}</div><div style="font-family:var(--mono);font-size:20px;color:var(--{k})">{pr}</div>'
                 + "".join(f'<div style="display:grid;grid-template-columns:30px 1fr;align-items:center;font-size:21px;color:var(--muted)">{ico_svg("check", 22, "var(--" + k + ")", 2.4)}<span>{li}</span></div>' for li in items)
                 + '</div>' for k, h, pr, items in cols)
    return dict(min=3, html=f'''
  {head(t("Планы • октябрь 2026", "Plans • October 2026"), t("Для этого урока хватит бесплатного плана", "The free plan is enough for this lesson"))}
  <div class="body"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px">{cc}</div>
    <div class="note" style="margin-top:26px">{t("Лимит — это «бак» на 5 часов, общий для сайта, приложения и Code. Кончился — подождать или перейти на план выше.", "The limit is a 5-hour “tank”, shared by the web, the app and Code. Ran out — wait or move up a plan.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Цены — с claude.com/pricing на 13.10.2026. Главное для студентов: артефакты, шаблоны Docs/Slides/Design, поиск и память есть бесплатно. Claude Code, Research, Chrome и надстройки Office — с Pro.",
                      "⏱ 3 min. Prices from claude.com/pricing as of 13 Oct 2026. Key point for students: artifacts, the Docs/Slides/Design templates, search and memory are free. Claude Code, Research, Chrome and the Office add-ins start at Pro."),
                    t("Лимит не в сообщениях, а в «объёме работы»: длинные файлы и мощные модели расходуют его быстрее. На платных планах есть ещё недельный лимит.",
                      "The limit isn’t counted in messages but in “amount of work”: long files and powerful models use it faster. Paid plans also have a weekly cap.")))


# ---------------------------------------------------------------- 08 what is an artifact
def s_what():
    crit = [t("<b>Большое</b> — обычно больше 15 строк", "<b>Substantial</b> — usually more than 15 lines"),
            t("<b>Самостоятельное</b> — понятно без чата", "<b>Self-contained</b> — makes sense without the chat"),
            t("<b>Хочется править</b> и дорабатывать", "<b>Worth editing</b> and improving"),
            t("<b>Пригодится потом</b> — вернётесь или покажете", "<b>Useful later</b> — you will come back or show it")]
    cl = "".join(f'<li style="display:grid;grid-template-columns:44px 1fr;align-items:center;font-size:23px;line-height:1.35;color:var(--muted)">{ico_svg("check", 32, "var(--green)", 2.4)}<span>{c}</span></li>' for c in crit)
    marks = [("cyan", 1, 1.5, 10, 31, 63), ("green", 2, 34.2, 1, 64.5, 98)]
    return dict(min=3, html=f'''
  {head(t("Определение", "Definition"), t("Артефакт — то, что не стыдно показать другому человеку", "An artifact is something you would put in front of another person"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1fr 1.5fr;gap:40px;align-items:center;">
      <div class="stack" style="gap:14px">
        <div class="prompt-label">{t("Claude делает артефакт, когда результат…", "Claude makes an artifact when the result is…")}</div>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:18px">{cl}</ul>
        <div class="plaque" style="margin-top:10px">{t("<b>Короткий ответ</b> («сколько срочных?») — просто ответ, не артефакт.", "<b>A short answer</b> (“how many urgent?”) is just an answer, not an artifact.")}</div>
      </div>
      <div>{shot_with(SCR + "dashboard_chat.jpg", marks)}
        <div class="cap" style="margin-top:8px"><b style="color:var(--cyan)">1</b> {t("файл, просьба и карточка артефакта в чате", "the file, the request and the artifact card in the chat")} &nbsp; <b style="color:var(--green)">2</b> {t("артефакт — в своём окне справа", "the artifact — in its own window on the right")}</div>{credit()}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Определение из справки Anthropic: артефакт — всё, что Claude делает для вас и что вы бы показали кому-то: дизайн, презентацию, документ, дашборд или небольшой инструмент. Открывается рядом с разговором.",
                      "⏱ 3 min. Anthropic’s help-centre definition: an artifact is anything Claude makes for you that you’d put in front of someone — a design, a deck, a document, a dashboard or a small tool. It opens beside the conversation."),
                    t("Четыре признака — когда Claude сам решает сделать артефакт. Если нужен наверняка — скажите прямо: «сделай документ / презентацию / дашборд». Важно: в настройках должно быть включено «Artifacts» (Settings → Capabilities).",
                      "The four signs are when Claude decides by itself. If you want one for sure, say so: “make a document / deck / dashboard”. “Artifacts” must be on in Settings → Capabilities.")))


# ---------------------------------------------------------------- 09 Artifacts tab
def s_tab():
    marks = [("green", 1, 11.1, 47.8, 46.6, 19.2), ("cyan", 2, 11.1, 79, 76.5, 20.5)]
    lg = [("green", 1, t("Начать с шаблона", "Start from a template"), t("Docs, Slides, Design, Dashboard (бета)", "Docs, Slides, Design, Dashboard (beta)")),
          ("cyan", 2, t("Всё, что вы сделали", "Everything you made"), t("из любого чата, с датой", "from any chat, with dates")),
          ("amber", "+", t("Или просто попросить в чате", "Or just ask in a chat"), t("«сделай…» — Claude выберет сам", "“make…” — Claude picks the type"))]
    return dict(min=4, html=f'''
  {head(t("Вкладка Artifacts", "The Artifacts tab"), t("Все артефакты — в одном месте", "All your artifacts in one place"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.75fr 1fr;gap:36px;align-items:center;">
      <div>{shot_with(SCR + "artifacts_tab.jpg", marks)}{credit()}</div>
      <div class="stack" style="gap:24px">{legend(lg, 22)}
        <div class="small" style="font-size:17px">{t("С 16.09.2026 артефакты обновили; старые продолжают работать. Motion (анимация в MP4) — только Team/Enterprise.", "Artifacts were updated on 16 Sep 2026; older ones keep working. Motion (MP4 animation) is Team/Enterprise only.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Вкладка Artifacts в боковой панели. Наверху — «Make something new»: начать с шаблона Docs, Slides, Design или Dashboard. Ниже — всё, что вы сделали, из любых чатов (на скриншоте — артефакты, сделанные для этого урока).",
                      "⏱ 4 min. The Artifacts tab in the sidebar. At the top — “Make something new”: start from Docs, Slides, Design or Dashboard. Below — everything you made, from any chat (the screenshot shows artifacts made for this lesson)."),
                    t("Шаблоны Docs, Slides, Design есть на всех планах, Dashboards — бета с Pro. Но шаблон не обязателен: можно просто написать в чате «сделай презентацию…» — так мы и делали.",
                      "Docs, Slides and Design are on all plans, Dashboards is beta from Pro. A template isn’t required: you can just write “make a deck…” in a chat — that’s how we did it.")))


# ---------------------------------------------------------------- 10 Slides
def s_slides():
    marks = [("cyan", 1, 7.5, 12.5, 24, 21.5), ("green", 2, 35.6, 86, 54.3, 11.6), ("amber", 3, 35.6, 8.8, 10.8, 5.2)]
    lg = [("cyan", 1, t("Одна фраза в чате", "One sentence in the chat"), ""),
          ("green", 2, t("5 готовых слайдов", "5 finished slides"), t("можно править прямо на слайде", "edit right on the slide")),
          ("amber", 3, t("Текст, картинки, таблицы", "Text, images, tables"), "")]
    return dict(min=5, html=f'''
  {head(t("Тип 1 • Slides", "Type 1 • Slides"), t("Презентация из одной фразы", "A deck from one sentence"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.7fr 0.62fr 0.75fr;gap:26px;align-items:center;">
      <div>{shot_with(SCR + "slides.jpg", marks)}{credit()}</div>
      <div class="stack" style="gap:8px"><div class="prompt-label">Share → Export</div>{img("export")}</div>
      <div class="stack" style="gap:18px">{legend(lg, 21)}
        <div class="note" style="--k:var(--violet)">{t("Скачать: <b>PowerPoint, PDF, PNG</b> или сразу в <b>Google Slides</b>.", "Download: <b>PowerPoint, PDF, PNG</b> or straight to <b>Google Slides</b>.")}</div></div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Живьём: новый чат → «Сделай презентацию на 5 слайдов для новых курьеров службы доставки «Быстро»: как принять заказ, как общаться с клиентом, что делать, если адрес не найден, безопасность на дороге, итоги.» Генерация — около 2 минут.",
                      "⏱ 5 min. Live: new chat → “Make a 5-slide deck for new couriers of the «Bystro» delivery service: how to accept an order, how to talk to the customer, what to do if the address isn’t found, road safety, summary.” Takes about 2 minutes."),
                    t("Пока Claude работает — объясните: результат открывается справа, внизу — миниатюры слайдов, наверху — инструменты. Любой текст можно исправить кликом прямо на слайде или попросить Claude: «сделай слайд 3 короче».",
                      "While Claude works, explain: the result opens on the right, slide thumbnails at the bottom, tools at the top. Fix any text by clicking on the slide, or ask Claude: “make slide 3 shorter”."),
                    t("Share → Export: PDF, PowerPoint (.pptx), PNG, Google Slides. Совет из меню: если отправляете коллеге — лучше ссылка, у него всегда будет последняя версия.",
                      "Share → Export: PDF, PowerPoint (.pptx), PNG, Google Slides. Tip from the menu: when sending to a colleague, a link is better — they always get the latest version.")))


# ---------------------------------------------------------------- 11 Docs
def s_docs():
    marks = [("green", 2, 52, 33.6, 28.3, 5.4), ("cyan", 1, 41, 40.5, 50, 10, "r")]
    lg = [("cyan", 1, t("Выделили текст", "Selected some text"), ""),
          ("green", 2, t("Панель: формат и комментарий", "Toolbar: format and comment"), t("комментарий можно адресовать Claude", "a comment can be addressed to Claude")),
          ("amber", "↓", t("Экспорт", "Export"), "Word · PDF · Markdown · Google Docs")]
    return dict(min=4, html=f'''
  {head(t("Тип 2 • Docs", "Type 2 • Docs"), t("Документ, который пишете вместе с Claude", "A document you write together with Claude"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.8fr 1fr;gap:34px;align-items:center;">
      <div>{shot_with(SCR + "docs.jpg", marks)}{credit()}</div>
      <div class="stack" style="gap:22px">{legend(lg, 21)}
        <div class="note">{t("Правите сами, как в Word, или просите Claude: «перепиши этот абзац проще».", "Edit it yourself like in Word, or ask Claude: “rewrite this paragraph more simply”.")}</div></div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Промпт: «Сделай документ: памятка для нового оператора поддержки курьерской службы — 5 правил ответа клиенту и шаблоны ответов на 3 частые жалобы.» Получается живой документ (Claude Docs).",
                      "⏱ 4 min. Prompt: “Make a document: a guide for a new courier-service support agent — 5 rules for answering a customer and reply templates for 3 common complaints.” You get a living document (Claude Docs)."),
                    t("Покажите: выделите абзац — появляется панель форматирования и кнопка комментария. Документ можно редактировать руками, как обычный, или просить Claude изменить конкретное место. Коллег можно пригласить через Share — они смогут комментировать и править.",
                      "Show it: select a paragraph — a formatting toolbar and a comment button appear. Edit the document by hand like any other, or ask Claude to change a specific place. Invite colleagues via Share — they can comment and edit."),
                    t("Экспорт: Word, PDF, Markdown, Google Docs.", "Export: Word, PDF, Markdown, Google Docs.")))


# ---------------------------------------------------------------- 12 Design
def s_design():
    marks = [("amber", 1, 2.4, 26.4, 29.2, 30)]
    return dict(min=4, html=f'''
  {head(t("Тип 3 • Design", "Type 3 • Design"), t("Макет сайта — без дизайнера", "A website mockup — without a designer"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.8fr 1fr;gap:34px;align-items:center;">
      <div>{shot_with(SCR + "design.jpg", marks)}{credit()}</div>
      <div class="stack" style="gap:22px">
        <div class="bubble me" style="font-size:20px">{t("«Сделай дизайн: лендинг для курьерской службы «Быстро» — доставка за 30 минут, тарифы, кнопка «Заказать».»", "“Make a design: a landing page for the «Bystro» courier service — delivery in 30 minutes, prices, an “Order” button.”")}</div>
        {legend([("amber", 1, t("Claude честно пишет, что придумал сам", "Claude says honestly what it made up"), t("цены и телефоны оставил как [ЦЕНА] — чтобы не выдумывать", "left prices and phones as [PRICE] — so as not to invent them"))], 21)}
        <div class="note" style="--k:var(--violet)">{t("Экспорт: HTML, PDF, PowerPoint, архив .zip.", "Export: HTML, PDF, PowerPoint, a .zip archive.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Design — макеты, прототипы, лендинги, одностраничники. Результат открывается на холсте: можно двигать элементы, менять цвета (Tweaks), просить правки словами.",
                      "⏱ 4 min. Design — mockups, prototypes, landing pages, one-pagers. The result opens on a canvas: move elements, change colours (Tweaks), ask for edits in words."),
                    t("Обратите внимание на абзац «Что я допустил»: Claude сам перечислил, что придумал (названия тарифов), а цены и телефоны оставил заглушками. Это хорошая привычка — всегда спрашивать «что ты выдумал?» и проверять.",
                      "Point at the “What I assumed” paragraph: Claude listed what it made up (plan names) and left prices and phones as placeholders. A good habit — always ask “what did you make up?” and check.")))


# ---------------------------------------------------------------- 13 Diagram + dashboard
def s_more():
    return dict(min=4, html=f'''
  {head(t("Типы 4–5 • схема и дашборд", "Types 4–5 • diagram and dashboard"), t("Нарисовать процесс и показать данные", "Draw a process and show the data"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:34px;align-items:start;">
      <div class="stack" style="gap:10px">
        <div class="vlabel"><span class="badge" style="--k:var(--cyan)">{t("схема", "diagram")}</span>{t("«Нарисуй, как обрабатывается жалоба клиента»", "“Draw how a customer complaint is handled”")}</div>
        {img("diagram", "max-height:520px;object-fit:cover;object-position:top")}</div>
      <div class="stack" style="gap:10px">
        <div class="vlabel"><span class="badge" style="--k:var(--green)">{t("дашборд", "dashboard")}</span>{t("«Что разобрать первым на планёрке?» + файл CSV", "“What first at stand-up?” + a CSV file")}</div>
        {img("dashboard", "max-height:520px;object-fit:cover;object-position:top")}</div>
    </div>
    {credit()}
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Схема: Claude рисует шаги процесса с развилками («срочно?», «жалоба обоснована?»). Подходит для инструкций и объяснений. Дашборд: загрузили таблицу — получили экран с цифрами и списком «что первым». Его разберём подробно в живом демо после перерыва.",
                      "⏱ 4 min. Diagram: Claude draws the process steps with decision points (“urgent?”, “is the complaint valid?”). Good for guides and explanations. Dashboard: upload a table — get a screen with numbers and a “what first” list. We’ll walk through it in the live demo after the break."),
                    t("Интересный момент при подготовке: для схемы Claude сначала предложил использовать подключённый Figma — и спросил разрешения (слайд 18). Мы отказались, и он нарисовал схему прямо в артефакте — на слайде результат без Figma.",
                      "An interesting moment during preparation: for the diagram Claude first offered to use the connected Figma — and asked for permission (slide 18). We declined, and it drew the diagram right in the artifact — the slide shows the no-Figma result.")))


# ---------------------------------------------------------------- 14 Mini app
def s_app():
    marks = [("amber", 1, 2.4, 31.4, 29.2, 13.6)]
    return dict(min=4, html=f'''
  {head(t("Тип 6 • мини-приложение", "Type 6 • mini app"), t("Артефакт, внутри которого работает Claude", "An artifact with Claude working inside"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.8fr 1fr;gap:34px;align-items:center;">
      <div>{shot_with(SCR + "app.jpg", marks)}{credit()}</div>
      <div class="stack" style="gap:20px">
        <div class="bubble me" style="font-size:20px">{t("«Сделай тренажёр: Claude играет недовольного клиента, я отвечаю, а Claude оценивает ответ по 3 критериям.»", "“Make a coach: Claude plays an angry customer, I answer, and Claude grades my answer on 3 criteria.”")}</div>
        {legend([("amber", 1, t("Claude предупреждает", "Claude warns you"), t("при первом запуске спросит разрешение; запросы идут в лимит того, кто пользуется", "asks for permission on first use; requests count against the user’s limit"))], 21)}
        <div class="note" style="--k:var(--amber)">{t("Включается в Settings → Capabilities → <b>AI-powered artifacts</b>.", "Turned on in Settings → Capabilities → <b>AI-powered artifacts</b>.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Мини-приложение — артефакт с кнопками и полями, который сам обращается к Claude: тренажёры, генераторы карточек, викторины. Ключ API не нужен.",
                      "⏱ 4 min. A mini app is an artifact with buttons and fields that calls Claude itself: coaches, flashcard generators, quizzes. No API key needed."),
                    t("Кто платит: запросы считаются в лимит того, кто пользуется приложением, а не автора. При первом запуске артефакт спрашивает разрешения. Если кнопка не работает — проверьте переключатель AI-powered artifacts в настройках (у автора курса он был выключен).",
                      "Who pays: requests count against the person using the app, not the author. On first use the artifact asks for permission. If the button doesn’t work, check the AI-powered artifacts toggle in settings (it was off in the course author’s account)."),
                    t("Перед занятием проверьте на бесплатном аккаунте, что такой артефакт создаётся и запускается, — от этого зависит трек Б в домашке.",
                      "Before class, check on a free account that such an artifact can be created and run — homework track B depends on it.")))


# ---------------------------------------------------------------- 16 Live demo
def s_demo():
    step = lambda n, k, h, body: (f'<div class="stack" style="gap:10px"><div class="vlabel"><span class="num" style="position:static;transform:none;width:32px;height:32px;border-radius:50%;'
                                  f'background:var(--{k});color:#0b0f17;font-family:var(--mono);font-weight:800;display:inline-flex;align-items:center;justify-content:center">{n}</span>{h}</div>{body}</div>')
    checks = [t("Срочное наверху? <b>T-110 первым</b> — клиент видит чужие заказы", "Urgent on top? <b>T-110 first</b> — a customer sees other people’s orders"),
              t("Email клиентов на экране? <b>Нет</b>", "Customer emails on screen? <b>No</b>"),
              t("Цифры сходятся с файлом? <b>11 открыто, 4 срочных</b> — сверили", "Do the numbers match the file? <b>11 open, 4 urgent</b> — checked")]
    cl = "".join(f'<div style="display:grid;grid-template-columns:34px 1fr;align-items:center;font-size:20px;color:var(--muted)">{ico_svg("check", 26, "var(--green)", 2.6)}<span>{c}</span></div>' for c in checks)
    return dict(min=7, html=f'''
  {head(t("Живое демо", "Live demo"), t("Таблица → дашборд → слайды для планёрки", "Table → dashboard → stand-up slides"))}
  <div class="body" style="justify-content:flex-start;margin-top:20px">
    <div style="display:grid;grid-template-columns:0.7fr 1.15fr 1.15fr;gap:22px;align-items:start">
      {step(1, "cyan", t("Файл + одна фраза", "A file + one sentence"), img("prompt_csv"))}
      {step(2, "green", t("Дашборд", "Dashboard"), img("dashboard", "height:330px;object-fit:cover;object-position:top"))}
      {step(3, "violet", t("«Сделай 3 слайда для планёрки»", "“Make 3 slides for stand-up”"), img("dash_slides", "height:330px;object-fit:cover;object-position:top"))}
    </div>
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:30px;flex:none;margin-top:22px;align-items:start">
      <div class="stack" style="gap:10px"><div class="prompt-label">{t("Прежде чем показывать — проверить", "Before showing it — check")}</div>{cl}</div>
      <div class="plaque">{t("<b>Первый вариант — черновик.</b> Не нравится — просите точно: «перенеси срочные без ответственного наверх», а не «сделай лучше».", "<b>The first version is a draft.</b> If you don’t like it, be precise: “move urgent tickets without an owner to the top”, not “make it better”.")}</div>
    </div>
    {credit()}
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. Живьём, файл demo_assets/tickets_ru.csv (вымышленные обращения курьерской службы; в файле специально есть email клиентов и пустые ответственные). 1) Новый чат → «+» → Add files → tickets_ru.csv. Текст: «Сделай дашборд для руководителя поддержки: что разобрать первым на утренней планёрке? Email клиентов не показывай.»",
                      "⏱ 7 min. Live, file demo_assets/tickets_en.csv (made-up courier-support tickets; it deliberately contains customer emails and empty owners). 1) New chat → “+” → Add files → tickets_en.csv. Text: “Make a dashboard for the support lead: what should we tackle first at the morning stand-up? Don’t show customer emails.”"),
                    t("2) Через 2–3 минуты — дашборд. Проверяем вслух три вещи со слайда. На подготовке Claude сам поставил первым T-110 — P1 без ответственного, клиент видит чужие заказы. 3) В том же чате: «Сделай из этого 3 слайда для планёрки» — получаем презентацию с теми же цифрами.",
                      "2) After 2–3 minutes — the dashboard. Check the three things on the slide aloud. During preparation Claude put T-110 first by itself — a P1 with no owner, a customer seeing other people’s orders. 3) In the same chat: “Make 3 slides for stand-up from this” — a deck with the same numbers."),
                    t("Если сеть или Claude подводят — показывайте этот слайд: это реальные результаты. Никаких настоящих клиентских данных — только этот файл.",
                      "If the network or Claude fails, show this slide: these are real results. No real customer data — only this file.")))


# ---------------------------------------------------------------- 17 Projects
def s_projects():
    marks = [("cyan", 1, 4.2, 21.2, 59.5, 5.4, "r"), ("green", 2, 67, 35.2, 27.8, 7.2, "r"), ("violet", 3, 67, 44.4, 27.8, 9.4, "r")]
    lg = [("cyan", 1, t("Описание проекта", "Project description"), ""),
          ("green", 2, t("Инструкция", "Instructions"), t("«отвечай кратко, email не показывай»", "“answer briefly, never show emails”")),
          ("violet", 3, t("Файлы проекта", "Project files"), t("tickets.csv, регламенты, отчёты", "tickets.csv, guides, reports"))]
    return dict(min=4, html=f'''
  {head(t("Проекты", "Projects"), t("Проект — папка, которую Claude помнит в каждом чате", "A project is a folder Claude remembers in every chat"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.85fr 1fr;gap:34px;align-items:center;">
      <div>{shot_with(SCR + "project.jpg", marks)}{credit()}</div>
      <div class="stack" style="gap:22px">{legend(lg, 21)}
        <div class="note">{t("Не нужно каждый раз загружать файлы и объяснять правила. <b>Free — до 5 проектов.</b>", "No need to upload files and explain the rules every time. <b>Free — up to 5 projects.</b>")}</div></div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Projects → New project → название и цель. Справа: Instructions — правила для всех чатов проекта; Context — файлы, которые Claude читает каждый раз; Memory — что Claude запомнил в этом проекте.",
                      "⏱ 4 min. Projects → New project → name and goal. On the right: Instructions — rules for every chat in the project; Context — files Claude reads every time; Memory — what Claude remembered in this project."),
                    t("Пример на слайде — демо-проект урока: инструкция «отвечай кратко, по-русски, никогда не показывай email и телефоны» и файл с обращениями. Любой новый чат в проекте уже знает и правила, и данные. В Team проектом можно поделиться с коллегами.",
                      "The example is the lesson’s demo project: the instruction “answer briefly, never show emails or phone numbers” and the tickets file. Any new chat in the project already knows the rules and the data. On Team you can share a project with colleagues.")))


# ---------------------------------------------------------------- 18 Connectors and files
def s_connect():
    return dict(min=4, html=f'''
  {head(t("Коннекторы и файлы", "Connectors and files"), t("Claude знает только то, что вы ему дали", "Claude knows only what you gave it"))}
  <div class="body">
    <div class="row" style="grid-template-columns:0.9fr 1.3fr;gap:34px;align-items:center;">
      <div class="stack" style="gap:8px"><div class="prompt-label">{t("«+» → Connectors", "“+” → Connectors")}</div>{img("connectors")}</div>
      <div class="stack" style="gap:14px">
        <div class="prompt-label">{t("Перед действием в чужом сервисе — вопрос", "Before acting in another service — a question")}</div>
        {img("permission")}
        <div class="small" style="text-align:center">{t("… здесь Claude показывает, что именно отправит в Figma …", "… here Claude shows exactly what it will send to Figma …")}</div>
        {shot_with(SCR + "permission_btn.jpg", [("amber", 1, 1, 8, 98, 84)])}
        {legend([("amber", 1, t("Decline · Allow once · Always allow", "Decline · Allow once · Always allow"), t("решаете вы; «один раз» — безопасный выбор", "you decide; “once” is the safe choice"))], 21)}
      </div>
    </div>
    {credit()}
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Три способа дать Claude информацию: прикрепить файл («+» → Add files: PDF, Excel, CSV, фото), подключить сервис (коннекторы: Gmail, Google Drive, Календарь, GitHub, Figma и сотни других) и включить поиск в интернете.",
                      "⏱ 4 min. Three ways to give Claude information: attach a file (“+” → Add files: PDF, Excel, CSV, photos), connect a service (connectors: Gmail, Google Drive, Calendar, GitHub, Figma and hundreds more) and turn on web search."),
                    t("Коннектор работает с вашими правами: что не видите вы, не увидит и Claude. Перед действием в чужом сервисе Claude спрашивает — на скриншоте он хотел нарисовать схему в Figma. Если сомневаетесь — Decline или Allow once.",
                      "A connector uses your permissions: what you can’t see, Claude can’t either. Before acting in another service Claude asks — on the screenshot it wanted to draw the diagram in Figma. If in doubt — Decline or Allow once.")))


# ---------------------------------------------------------------- 19 Claude acts
def s_agents():
    return dict(min=4, html=f'''
  {head(t("Следующий шаг", "Next step"), t("Когда Claude не только отвечает, но и делает сам", "When Claude doesn’t just answer but acts"), k="violet")}
  <div class="body">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:34px;align-items:start;">
      <div class="stack" style="gap:10px"><div class="vlabel"><span class="badge" style="--k:var(--violet)">{t("в чате", "in the chat")}</span>{t("сам открыл браузер и собирает цены", "opened a browser itself and collects prices")}</div>
        <img src="{IMG}off_agent.jpg" alt="" style="width:100%;border-radius:12px;border:1px solid var(--line);display:block"><div class="small">Image: Anthropic</div></div>
      <div class="stack" style="gap:10px"><div class="vlabel"><span class="badge" style="--k:var(--amber)">Code</span>{t("режим для программистов", "the programmers’ mode")}</div>
        {img("code", "height:auto")}{credit()}</div>
    </div>
    <div class="note" style="margin-top:20px;--k:var(--violet)">{t("Это <b>агенты</b>: цель → шаги → результат. Подробно — в L11 и L16. А <b>скиллы</b> — готовые «рецепты», которые Claude открывает сам (например, «сделай файл Excel»).", "These are <b>agents</b>: goal → steps → result. Details in L11 and L16. And <b>skills</b> are ready-made “recipes” Claude opens by itself (e.g. “make an Excel file”).")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Короткий анонс. С 16 сентября 2026 бывший Cowork влит в обычный чат («One Claude»): Claude сам понимает, когда нужна длинная работа из многих шагов, — например, открыть сайты и собрать сравнение цен. Сначала — на Pro и Max.",
                      "⏱ 4 min. A short preview. Since 16 September 2026 the former Cowork is part of the normal chat (“One Claude”): Claude decides when long multi-step work is needed — e.g. opening sites and building a price comparison. Pro and Max first."),
                    t("Claude Code — переключатель «Code» вверху боковой панели: Claude читает проект, пишет код, запускает тесты. Эта презентация собрана в нём. Скиллы — папки с инструкцией и файлами (например, встроенные Word/Excel/PowerPoint/PDF), поэтому Claude отдаёт настоящие файлы.",
                      "Claude Code — the “Code” toggle at the top of the sidebar: Claude reads a project, writes code, runs tests. This deck was built with it. Skills are folders with instructions and files (e.g. the built-in Word/Excel/PowerPoint/PDF ones), which is why Claude hands you real files.")))


# ---------------------------------------------------------------- 20 Safety
def s_safety():
    never = [t("пароли, ключи, номера карт", "passwords, keys, card numbers"), t("личные данные клиентов и коллег", "personal data of customers and colleagues"),
             t("закрытые документы компании — без разрешения", "confidential company documents — without permission")]
    nl = "".join(f'<li style="display:grid;grid-template-columns:36px 1fr;align-items:center;font-size:21px;color:var(--muted)">{ico_svg("x", 26, "var(--red)", 2.4)}<span>{n}</span></li>' for n in never)
    return dict(min=6, html=f'''
  {head(t("Безопасность", "Safety"), t("Публичная ссылка — это публикация", "A public link is a publication"), k="red")}
  <div class="body">
    <div class="row" style="grid-template-columns:0.85fr 1.2fr 0.8fr;gap:26px;align-items:start;">
      <div class="stack" style="gap:8px"><div class="prompt-label">Share</div>
        {shot_with(SCR + "share.jpg", [("red", 1, 13.8, 74.6, 68, 20.8)])}
        <div class="cap"><b style="color:var(--red)">1</b> {t("«Anyone with the link» — увидит любой, у кого ссылка", "“Anyone with the link” — anyone who has it can see")}</div></div>
      <div class="stack" style="gap:8px"><div class="prompt-label">Settings → Privacy</div>
        {shot_with(SCR + "privacy.jpg", [("amber", 2, 2.9, 84, 93.5, 13.4)])}
        <div class="cap"><b style="color:var(--amber)">2</b> {t("«Help improve our AI models» — ваши чаты идут на обучение. Решаете вы.", "“Help improve our AI models” — your chats are used for training. Your call.")}</div></div>
      <div class="stack" style="gap:16px">
        <div class="prompt-label">{t("Не вставлять в чат", "Never paste into the chat")}</div>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:12px">{nl}</ul>
        <div class="note" style="--k:var(--green)">{t("Новый артефакт видите <b>только вы</b>. Делитесь, когда проверили, что внутри нет личных данных.", "A new artifact is visible <b>only to you</b>. Share it once you’ve checked there’s no personal data inside.")}</div>
      </div>
    </div>
    {credit()}
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Share: по умолчанию «Only people invited» — только вы и приглашённые. «Anyone with the link» — ссылку можно переслать дальше, относитесь к ней как к публикации в интернете. В Team/Enterprise публичные ссылки включает администратор. На вашем плане названия пунктов могут чуть отличаться — смысл тот же: «только вы» → «любой со ссылкой».",
                      "⏱ 6 min. Share: by default “Only people invited” — you and the people you invite. “Anyone with the link” — the link can be forwarded, treat it like publishing on the internet. On Team/Enterprise public links are enabled by the admin. On your plan the labels may differ slightly — the idea is the same: “only you” → “anyone with the link”."),
                    t("Privacy: переключатель «Help improve our AI models». Включён — чаты и сессии кода могут использоваться для обучения моделей и хранятся до 5 лет; выключен — 30 дней. В Team и Enterprise по умолчанию на обучение не идут. Покажите, где это, — пусть каждый решит сам.",
                      "Privacy: the “Help improve our AI models” toggle. On — chats and coding sessions may be used to train models and are kept up to 5 years; off — 30 days. Team and Enterprise are not used for training by default. Show where it is — let everyone decide."),
                    t("Самая частая утечка — красивый артефакт, которым хочется поделиться, пока никто не посмотрел, какие данные внутри. Поэтому в демо мы сразу попросили «email не показывай».",
                      "The most common leak is a beautiful artifact everyone wants to share before anyone checked what data is inside. That’s why in the demo we asked “don’t show emails” right away.")))


# ---------------------------------------------------------------- 21 Homework + summary
def s_hw():
    rules = [("cyan", t("Чат — подумать, артефакт — сделать вещь", "Chat to think, artifact to make a thing")),
             ("green", t("Просите конкретно: что, для кого, из каких данных", "Ask precisely: what, for whom, from which data")),
             ("amber", t("Проверяйте: цифры, выдумки, личные данные", "Check: numbers, made-up facts, personal data")),
             ("red", t("Делитесь осознанно: ссылка = публикация", "Share deliberately: a link = a publication"))]
    rr = "".join(f'<div class="rule" style="--k:var(--{k});grid-template-columns:44px 1fr"><div class="n" style="font-size:34px">{i + 1}</div><div class="t" style="font-size:23px">{h}</div></div>' for i, (k, h) in enumerate(rules))
    return dict(min=7, html=f'''
  {head(t("Домашнее задание • итоги", "Homework • summary"), t("Сделайте две вещи разных типов", "Make two things of different types"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:50px;align-items:center;">
      <div class="stack" style="gap:16px">
        <div class="track" style="--k:var(--cyan);grid-template-columns:80px 1fr">{ico_svg("slides", 58, "var(--cyan)")}<div><div class="h">{t("1. Презентация или документ", "1. A deck or a document")}</div><div class="d">{t("на рабочую или учебную тему", "on a work or study topic")}</div></div></div>
        <div class="track" style="--k:var(--green);grid-template-columns:80px 1fr">{ico_svg("dash", 58, "var(--green)")}<div><div class="h">{t("2. Дашборд, схема или тренажёр", "2. A dashboard, diagram or coach")}</div><div class="d">{t("по своим <b>обезличенным</b> данным", "from your own <b>anonymised</b> data")}</div></div></div>
        <div class="note">{t("Сдаёте: 2 промпта, 2 ссылки или скриншота и <b>одну правку</b>, которую попросили после проверки.", "Hand in: 2 prompts, 2 links or screenshots and <b>one fix</b> you asked for after checking.")}</div>
      </div>
      <div class="stack" style="gap:18px">
        <div class="prompt-label">{t("Четыре правила", "Four rules")}</div><div class="rules" style="gap:22px">{rr}</div>
        <div class="note" style="--k:var(--violet)"><b>{t("Урок 10:", "Lesson 10:")}</b> {t("открытые модели на своём компьютере (LM Studio) и в облаке.", "open models on your own computer (LM Studio) and in the cloud.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. ДЗ: две вещи разных типов. Первая — презентация или документ. Вторая — дашборд, схема или мини-приложение по своим данным, обязательно обезличенным (замените имена, email, телефоны). Бесплатного плана хватает.",
                      "⏱ 7 min. Homework: two things of different types. First — a deck or a document. Second — a dashboard, diagram or mini app from your own data, anonymised (replace names, emails, phones). The free plan is enough."),
                    t("Сдаёте промпты, ссылки (только если внутри нет личных данных) или скриншоты и одну точную правку после проверки: что не понравилось → что попросили изменить. Шаблон — в L09_05_Homework.",
                      "Hand in the prompts, links (only if there’s no personal data inside) or screenshots, and one precise fix after checking: what you didn’t like → what you asked to change. Template in L09_05_Homework."),
                    t("Итоги — четыре правила. Вопросы. Мост: в L10 уходим от облачных ассистентов к открытым моделям — LM Studio, локальный запуск, RunPod.",
                      "Summary — four rules. Questions. Bridge: in L10 we move from cloud assistants to open models — LM Studio, local inference, RunPod.")))


SLIDES = [s_cover, s_hook, s_terms, s_eco, s_window, s_models, s_plans, s_what, s_tab, s_slides, s_docs, s_design, s_more, s_app,
          s_break, s_demo, s_projects, s_connect, s_agents, s_safety, s_hw]


# ---------------------------------------------------------------- page
def build(lang):
    global LANG
    LANG = lang
    css = (HERE / "style.css").read_text(encoding="utf-8")
    js = (HERE / "deck.js").read_text(encoding="utf-8")
    total = len(SLIDES)
    secs, minutes = [], 0
    for i, fn in enumerate(SLIDES, 1):
        s = fn()
        minutes += s["min"]
        cls = ("slide " + s.get("cls", "")).strip()
        foot = "" if s.get("cls") == "cover" else f'\n  <div class="foot"><span>{FOOT[lang]}</span><span>{i:02d} / {total}</span></div>'
        secs.append(f'<!-- SLIDE {i:02d} · {fn.__name__} · {s["min"]} min -->\n<section class="{cls}" data-n="{i}">{s["html"]}{foot}\n'
                    f'  <template class="notes">{s["notes"]}</template>\n</section>')
    assert minutes == 90, minutes
    title = t("Урок 09: Экосистема Claude и артефакты | GenAI Basics", "Lesson 09: Claude Ecosystem and Artifacts | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<!-- generated by deck/build.py — edit the generator, not this file -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
{css}</style>
</head>
<body>
<main class="stage" id="stage">

{chr(10).join(secs)}

</main>

<aside class="drawer" id="drawer"><div class="hd"></div><div class="tx"></div></aside>
<div class="grid" id="grid"></div>

<script>
const T = {tconst};
{js}</script>
</body>
</html>
'''
    OUT[lang].write_text(html, encoding="utf-8")
    print(f"{lang}: {OUT[lang].name} — {total} slides, {minutes} min")
    return OUT[lang]


EDGE = next((c for c in [shutil.which("msedge"),
                         r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                         r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"] if c and Path(c).exists()), None)


def pdf(html):
    out = html.with_suffix(".pdf")
    prof = tempfile.mkdtemp(prefix="edgepdf_")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=10000",
                    f"--user-data-dir={prof}", f"--print-to-pdf={out}", html.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    shutil.rmtree(prof, ignore_errors=True)
    print("pdf:", out.name, f"{out.stat().st_size / 1e6:.1f} MB")


def shots(lang, outdir, which=None):
    """PNG of every slide (for visual QA)."""
    outdir.mkdir(parents=True, exist_ok=True)
    prof = tempfile.mkdtemp(prefix="edgeshot_")
    for i in range(1, len(SLIDES) + 1):
        if which and i not in which:
            continue
        subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1600,900", "--virtual-time-budget=5000",
                        f"--user-data-dir={prof}", f"--screenshot={outdir / f'{lang}_{i:02d}.png'}", OUT[lang].as_uri() + f"#{i}"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    shutil.rmtree(prof, ignore_errors=True)


if __name__ == "__main__":
    for lg in ("ru", "en"):
        h = build(lg)
        if "--shots" in sys.argv:
            shots(lg, Path(sys.argv[sys.argv.index("--shots") + 1]))
        if "--no-pdf" not in sys.argv:
            pdf(h)
