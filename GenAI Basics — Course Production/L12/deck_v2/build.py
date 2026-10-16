# -*- coding: utf-8 -*-
"""Build the L12 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. Images live in ../assets/v2/img/ (own captures 2026-10-16,
claude.ai captures reused from L09, 2× Pillow insets); schematics are drawn in HTML below.
Facts: ../L12_08_Source_Notes_Research_2026-10.md.
"""
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L12 = HERE.parent
NAME = "presentation_L12_MCP_and_Agent_Frameworks"
OUT = {"ru": L12 / f"{NAME}_v2.html", "en": L12 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 12 • MCP и фреймворки", "en": "GenAI Basics • Lesson 12 • MCP and frameworks"}


# ---------------------------------------------------------------- helpers
def num(x, d=1):
    s = f"{x:.{d}f}"
    return s.replace(".", ",") if LANG == "ru" else s


def head(kicker, title, lead=None, k=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    title = title.replace("MCP-", "MCP‑")  # non-breaking hyphen: never break "MCP-/серверы"
    s = f'<div class="kicker"{ks}>{kicker}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


def shot(name, marks=(), boxes=(), style="", ext="png"):
    """Screenshot with numbered badges and highlight boxes in % of the image.
    marks: (n, x%, y%, colour); boxes: (x%, y%, w%, h%, colour)."""
    b = "".join(f'<div class="co" style="left:{x}%;top:{y}%;width:{w}%;height:{h}%;--k:var(--{k})"></div>' for x, y, w, h, k in boxes)
    m = "".join(f'<div class="bn" style="left:{x}%;top:{y}%;--k:var(--{k})">{n}</div>' for n, x, y, k in marks)
    return f'<div class="shot" style="{style}"><img src="{IMG}{name}.{ext}" alt="">{b}{m}</div>'


def zoom(name, n, k, cap, width=None):
    """A 2× Pillow crop of the key line of a screenshot, shown under it with the same badge."""
    w = f"width:{width}px;" if width else ""
    return (f'<div style="display:flex;align-items:center;gap:14px;margin-top:12px;--k:var(--{k})">'
            f'<div class="legend"><div><i>{n}</i></div></div>'
            f'<img src="{IMG}{name}.png" alt="" style="{w}border:3px solid var(--{k});border-radius:10px;display:block">'
            f'<span class="small" style="font-size:17px;color:var(--dim)">{cap}</span></div>')


def legend(items):
    return '<div class="legend">' + "".join(
        f'<div style="--k:var(--{k})"><i>{n}</i><span>{s}</span></div>' for n, k, s in items) + "</div>"


def bars(rows, lo, hi, fmt, log=False, ticks=(), label_w=300, ref=None):
    """Horizontal bar chart. rows: (label, sub, value, colour). ref: (value, label) vertical line."""
    def pct(v):
        if log:
            return 100 * math.log10(v / lo) / math.log10(hi / lo)
        return 100 * (v - lo) / (hi - lo)
    out = ""
    for lab, sub, v, k in rows:
        p = max(pct(v), 1.2)
        inside = p > 78
        vs = f'left:{p:.1f}%' + (";transform:translate(-100%,-50%);color:#0b0f17;padding-right:12px" if inside else "")
        out += (f'<div class="br" style="--k:var(--{k});grid-template-columns:{label_w}px 1fr"><div class="bl">{lab}<small>{sub}</small></div>'
                f'<div class="bt"><div class="bf" style="width:{p:.1f}%"></div><div class="bv" style="{vs}">{fmt(v)}</div></div></div>')
    tk = "".join(f'<span style="left:{pct(x):.1f}%">{lab}</span>' for x, lab in ticks)
    refl = ""
    if ref:
        rv, rl = ref
        refl = f'<div class="ref" style="left:calc({label_w}px + 16px + (100% - {label_w}px - 16px) * {pct(rv) / 100:.4f})"><span>{rl}</span></div>'
    axis = f'<div class="axis" style="grid-template-columns:{label_w}px 1fr"><div></div><div>{tk}</div></div>' if ticks else ""
    return f'<div class="bars" style="position:relative">{out}{axis}{refl}</div>'


def gb(v):
    v = math.floor(v * 10 + 0.5) / 10  # half-up, so 5.35 -> 5.4 everywhere
    return (f"{v:.1f} ГБ".replace(".", ",") if LANG == "ru" else f"{v:.1f} GB")


# ---------------------------------------------------------------- HTML diagrams (bilingual, replace the old English PNGs)
def node(x, y, w, h, k, label, fs=22, solid=False):
    bg, col = (f"var(--{k})", "#0b0f17") if solid else ("var(--surface-card)", "var(--fg)")
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border:2px solid var(--{k});border-radius:12px;background:{bg};'
            f'display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font:600 {fs}px/1.15 var(--body);color:{col};padding:0 8px">{label}</div>')


def label(x, y, w, txt, k="muted", fs=22, weight=700):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;text-align:center;font:{weight} {fs}px/1.2 var(--body);color:var(--{k})">{txt}</div>'


def path(d, k, wd=3):
    return f'<path d="{d}" fill="none" style="stroke:var(--{k})" stroke-width="{wd}"/>'


def canvas(w, h, inner, lines, style="margin:0 auto"):
    svg = f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0">{lines}</svg>'
    return f'<div style="position:relative;width:{w}px;height:{h}px;flex:none;{style}">{svg}{inner}</div>'


def mcp_box(x, y, w, h, fs=40):
    return node(x, y, w, h, "violet", f'MCP<span style="font:600 18px/1.2 var(--body);margin-top:6px">{t("один стандарт", "one standard")}</span>', fs=fs, solid=True)


SERVERS = lambda: ["Google Drive", "GitHub", "Figma", t("Ваша база данных", "Your database")]


def hub_diagram(apps=True):
    """Apps (hosts) → MCP → servers. apps=False draws only the MCP → servers half (cover)."""
    ys = [50, 150, 250, 350] if not apps else [60, 175, 290, 405]
    my = (ys[0] + ys[-1]) // 2 + 35
    ox = 335 if apps else 0
    inner, lines = "", ""
    if apps:
        inner += label(-20, 0, 300, t("ИИ-приложения (хосты)", "AI apps (hosts)"), "cyan", 21)
        for y, a in zip(ys, ["Claude", "ChatGPT", "VS Code", "LM Studio"]):
            inner += node(0, y, 230, 70, "cyan", a, 24)
            lines += path(f"M230 {y + 35} H282 V{my} H{ox}", "cyan")
    inner += mcp_box(ox, my - 75, 230, 150)
    sx = ox + 335
    inner += label(sx - 35, 0, 300, t("MCP-серверы", "MCP servers"), "green", 21)
    for y, s in zip(ys, SERVERS()):
        inner += node(sx, y, 230, 70, "green", s, 24)
        lines += path(f"M{ox + 230} {my} H{ox + 282} V{y + 35} H{sx}", "green")
    return canvas(sx + 230, ys[-1] + 80, inner, lines)


def nm_diagram():
    """Without MCP: 3 × 3 point-to-point links; with MCP: 3 + 3 through one standard."""
    ys = [50, 160, 270]
    apps, svcs = ["Claude", "ChatGPT", "VS Code"], ["Google Drive", "GitHub", "CRM"]

    def side(with_mcp):
        inner, lines = "", ""
        inner += label(0, 0, 600, t("С MCP", "With MCP") if with_mcp else t("Без MCP", "Without MCP"), "violet" if with_mcp else "amber", 28, 800)
        for y, a in zip(ys, apps):
            inner += node(0, y, 180, 70, "cyan", a, 23)
        for y, s in zip(ys, svcs):
            inner += node(420, y, 180, 70, "green", s, 23)
        if with_mcp:
            inner += mcp_box(240, 145, 120, 100, 30)
            for y in ys:
                lines += path(f"M180 {y + 35} H210 V195 H240", "cyan") + path(f"M360 195 H390 V{y + 35} H420", "green")
        else:
            for ya in ys:
                for yb in ys:
                    lines += path(f"M180 {ya + 35} C300 {ya + 35} 300 {yb + 35} 420 {yb + 35}", "amber", 2.5)
        cap = (t("3 + 3 = 6 стандартных подключений", "3 + 3 = 6 standard connections") if with_mcp
               else t("3 × 3 = 9 отдельных связок", "3 × 3 = 9 separate links"))
        inner += label(0, 362, 600, cap, "fg", 24)
        return canvas(600, 400, inner, lines, "margin:0")
    return (f'<div style="display:flex;justify-content:center;align-items:center;gap:60px">{side(False)}'
            f'<div style="width:2px;height:360px;background:var(--line)"></div>{side(True)}</div>')


def a2a_diagram():
    """MCP (agent ↔ tools) vs A2A (agent ↔ another company's agent)."""
    inner, lines = "", ""
    inner += node(0, 40, 250, 70, "violet", t("Файлы", "Files"), 24)
    inner += node(0, 140, 250, 70, "violet", t("Почта, календарь", "Mail, calendar"), 24)
    inner += node(0, 240, 250, 70, "violet", t("Ваша база данных", "Your database"), 24)
    inner += node(470, 105, 300, 140, "cyan", f'{t("Ваш агент", "Your agent")}<span style="font:500 19px/1.2 var(--body);color:var(--muted);margin-top:6px">{t("ассистент для поездки", "trip assistant")}</span>', 30)
    inner += node(990, 105, 300, 140, "amber", f'{t("Агент отеля", "Hotel agent")}<span style="font:500 19px/1.2 var(--body);color:var(--muted);margin-top:6px">{t("другая компания", "another company")}</span>', 30)
    for y in (75, 175, 275):
        lines += path(f"M250 {y} H360 V175 H470", "violet", 4)
    lines += path("M770 175 H990", "amber", 4)
    inner += label(250, 0, 220, "MCP", "violet", 30, 800)
    inner += label(250, 320, 220, t("агент ↔ инструменты", "agent ↔ tools"), "violet", 21, 600)
    inner += label(770, 120, 220, "A2A", "amber", 30, 800)
    inner += label(770, 195, 220, t("агент ↔ агент", "agent ↔ agent"), "amber", 21, 600)
    inner += label(990, 265, 300, t("«забронируй номер<br>на 12–14 мая»", "“book a room<br>for 12–14 May”"), "fg", 20, 500)
    return canvas(1290, 360, inner, lines)


def layers_diagram():
    """Nested layers: a framework can use MCP, and inside MCP is still function calling."""
    box = lambda k, h, d, w, inner="": (
        f'<div style="border:3px solid var(--{k});border-radius:20px;padding:24px 30px 28px;background:rgba(255,255,255,.02);display:flex;flex-direction:column;gap:20px;{w}">'
        f'<div><div style="font:800 34px/1.1 var(--display);color:var(--{k})">{h}</div>'
        f'<div style="font:500 24px/1.3 var(--body);color:var(--muted);margin-top:6px">{d}</div></div>{inner}</div>')
    fc = box("cyan", t("Вызов функций · L11", "Function calling · L11"), t("как модель просит действие", "how the model asks for an action"), "")
    mcp = box("violet", t("MCP · сегодня", "MCP · today"), t("как приложение находит и вызывает чужие инструменты", "how an app finds and calls other people’s tools"), "", fc)
    return box("green", t("Фреймворк агентов · после перерыва", "Agent framework · after the break"), t("кто крутит цикл: шаги, память, подтверждения, журнал", "who runs the loop: steps, memory, approvals, logs"), "", mcp)


# ---------------------------------------------------------------- slides
def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg"><div style="position:absolute;left:1000px;top:235px">{hub_diagram(apps=False)}</div></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 12 • Модуль 5: агенты, инструменты и MCP", "GenAI Basics • Lesson 12 • Module 5: agents, tools and MCP")}</div>
    <h1>{t("MCP и фреймворки агентов", "MCP and agent frameworks")}</h1>
    <h2>{t("Один стандартный «разъём», чтобы подключать инструменты к любому ИИ", "One standard “plug” to connect tools to any AI app")}</h2>
    <p>{t("Хосты, серверы, коннекторы Claude, реестр MCP, безопасность, свой мини-сервер, фреймворки агентов. Данные на октябрь 2026.",
           "Hosts, servers, Claude connectors, the MCP registry, security, your own mini server, agent frameworks. Data as of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. В L11 мы вручную описали функцию get_order_status для одной модели в AI Studio. Сегодня — как сделать инструмент один раз и подключать его к любому ИИ-приложению: Claude, ChatGPT, VS Code, LM Studio. Для этого есть стандарт MCP, Model Context Protocol.",
                      "⏱ 2 min. Welcome. In L11 we described get_order_status by hand for one model in AI Studio. Today: how to build a tool once and plug it into any AI app: Claude, ChatGPT, VS Code, LM Studio. There is a standard for this, MCP, the Model Context Protocol."),
                    t("План: зачем стандарт, как он устроен, где вы его уже видели (коннекторы Claude), разрешения, реестр серверов, локальные и удалённые серверы, свой мини-сервер, безопасность. После перерыва: фреймворки агентов, когда они нужны, агенты, которые говорят с агентами, упражнение и ДЗ.",
                      "Plan: why a standard, how it works, where you have seen it (Claude connectors), permissions, the server registry, local and remote servers, your own mini server, security. After the break: agent frameworks, when you need one, agents talking to agents, an exercise and homework.")))


def s_hook():
    return dict(min=4, html=f'''
  {head(t("Проблема", "The problem"), t("Без стандарта каждое ИИ-приложение подключают к каждому сервису отдельно", "Without a standard, every AI app is wired to every service separately"), k="red")}
  <div class="body" style="margin-top:6px;">
    <div style="zoom:1.12">{nm_diagram()}</div>
    <div class="note" style="margin-top:34px;--k:var(--violet)">{t("Чем больше приложений и сервисов, тем больше выигрыш: 10 × 10 = 100 против 10 + 10 = 20.", "The more apps and services, the bigger the gain: 10 × 10 = 100 vs 10 + 10 = 20.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. В прошлом уроке функция get_order_status жила внутри одного чата AI Studio. А если её нужно дать Claude, ChatGPT, VS Code и своему боту? Без стандарта каждую пару «приложение — сервис» связывают отдельным кодом: у каждого свой формат описания инструментов, свой вход, свои ошибки.",
                      "⏱ 4 min. In the last lesson get_order_status lived inside one AI Studio chat. What if Claude, ChatGPT, VS Code and your own bot all need it? Without a standard every app-service pair is wired with separate code: each has its own tool format, its own login, its own errors."),
                    t("Слева три приложения и три сервиса: девять отдельных связок. Справа то же через MCP: каждый подключается один раз к общему стандарту, и связок шесть. Чем больше приложений и сервисов, тем больше выигрыш.",
                      "On the left: three apps and three services, nine separate links. On the right, the same through MCP: each connects once to the shared standard, six links. The more apps and services, the bigger the gain.")))


def s_hub():
    return dict(min=5, html=f'''
  {head("MCP", t("MCP — как USB-C для ИИ-приложений: один разъём для любых инструментов", "MCP is like USB-C for AI apps: one plug for any tool"), k="violet")}
  <div class="body" style="margin-top:4px;">
    <div class="row" style="grid-template-columns:900px 1fr;gap:44px;align-items:center;flex:none;">
      {hub_diagram()}
      <div class="stack" style="gap:22px;">
        <div class="note" style="--k:var(--violet)">{t("<b>MCP</b> (Model Context Protocol) — открытый стандарт подключения ИИ-приложений к данным и инструментам. Создан Anthropic в ноябре 2024.", "<b>MCP</b> (Model Context Protocol) is an open standard for connecting AI apps to data and tools. Created by Anthropic in November 2024.")}</div>
        <div class="note" style="--k:var(--green)">{t("Сервис делает <b>один MCP-сервер</b>, и он работает в Claude, ChatGPT, VS Code, LM Studio (ChatGPT — только удалённые, по адресу в интернете).", "A service ships <b>one MCP server</b>, and it works in Claude, ChatGPT, VS Code, LM Studio (ChatGPT: remote only, by internet address).")}</div>
        <div class="small" style="font-size:18px">{t("Сравнение с USB-C — из официальной документации modelcontextprotocol.io", "The USB-C comparison comes from the official docs at modelcontextprotocol.io")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Официальная документация сравнивает MCP с портом USB-C: как USB-C стандартно подключает устройства, так MCP стандартно подключает ИИ-приложения к внешним системам. Слева приложения: Claude, ChatGPT, VS Code, LM Studio. Справа то, к чему подключаемся: Google Drive, GitHub, Figma, ваша база данных.",
                      "⏱ 5 min. The official docs compare MCP to a USB-C port: as USB-C connects devices in a standard way, MCP connects AI apps to external systems in a standard way. On the left the apps: Claude, ChatGPT, VS Code, LM Studio. On the right what we connect to: Google Drive, GitHub, Figma, your database."),
                    t("MCP придумала Anthropic в ноябре 2024 и сразу открыла как стандарт; его поддержали OpenAI, Google, Microsoft. Важно: MCP не заменяет вызов функций из L11. Внутри тот же механизм: модель предлагает вызов, программа выполняет. MCP стандартизирует, как программа узнаёт об инструментах и как их вызывает.",
                      "Anthropic created MCP in November 2024 and opened it as a standard; OpenAI, Google and Microsoft adopted it. Important: MCP does not replace function calling from L11. Inside it is the same mechanism: the model proposes a call, the program runs it. MCP standardises how the program learns about tools and how it calls them.")))


def s_roles():
    lane = lambda k, h, sub, ex: (f'<div class="task" style="--k:var(--{k});padding:36px 30px;align-items:flex-start"><div><div class="h" style="font-size:34px">{h}</div>'
                                  f'<div class="d" style="font-size:24px;margin-top:8px">{sub}</div><div class="d" style="font-size:23px;margin-top:12px;color:var(--fg)">{ex}</div></div></div>')
    arrow = '<div style="font-size:46px;color:var(--dim);align-self:center;text-align:center">→</div>'
    prims = [("cyan", t("Инструменты", "Tools"), t("действия: найти заказ, создать задачу", "actions: find an order, create a task")),
             ("green", t("Ресурсы", "Resources"), t("данные для чтения: файлы, записи", "data to read: files, records")),
             ("amber", t("Промпты", "Prompts"), t("готовые шаблоны запросов", "ready-made request templates"))]
    pr = legend([(i, k, f"<b>{h}</b>: {d}") for i, (k, h, d) in enumerate(prims, 1)])
    return dict(min=5, html=f'''
  {head(t("Как устроено", "How it works"), t("Три роли: приложение-хост, клиент внутри него и сервер с инструментами", "Three roles: the host app, a client inside it and a server with tools"), k="violet")}
  <div class="body" style="margin-top:10px;">
    <div style="display:grid;grid-template-columns:1fr 50px 1fr 50px 1fr;gap:6px;align-items:stretch;">
      {lane("cyan", t("Хост", "Host"), t("ИИ-приложение, в котором вы работаете", "the AI app you work in"), "Claude, ChatGPT, VS Code")}{arrow}
      {lane("violet", t("Клиент", "Client"), t("MCP-«разъём» внутри хоста, один на сервер", "the MCP “socket” inside the host, one per server"), t("встроен в приложение", "built into the app"))}{arrow}
      {lane("green", t("Сервер", "Server"), t("программа, которая даёт инструменты и данные", "a program that offers tools and data"), "Google Drive, GitHub, Figma")}
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:64px;align-items:center;">
      <div class="stack" style="gap:12px;"><div class="prompt-label">{t("Что сервер даёт хосту", "What a server offers the host")}</div>{pr}</div>
      <div class="note" style="--k:var(--cyan)">{t("Вам как пользователю важны два слова: <b>приложение</b> (хост) и <b>подключение</b> (сервер). Клиент работает незаметно.", "As a user you need two words: the <b>app</b> (host) and the <b>connection</b> (server). The client works out of sight.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Три роли. Хост — приложение, в котором вы общаетесь с ИИ: Claude, ChatGPT, VS Code. Сервер — отдельная программа, которая даёт инструменты и данные: сервер Google Drive умеет искать и читать файлы, сервер GitHub — задачи и код. Клиент — маленький «разъём» внутри хоста, по одному на каждый подключённый сервер; пользователь его не видит.",
                      "⏱ 5 min. Three roles. The host is the app where you talk to the AI: Claude, ChatGPT, VS Code. The server is a separate program that offers tools and data: the Google Drive server can search and read files, the GitHub server issues and code. The client is a small “socket” inside the host, one per connected server; the user never sees it."),
                    t("Сервер может давать три вида вещей. Инструменты — действия, как наша get_order_status. Ресурсы — данные для чтения: файлы, записи в базе. Промпты — готовые шаблоны, например «сделай сводку по задаче». Чаще всего вы встретите инструменты.",
                      "A server can offer three kinds of things. Tools — actions, like our get_order_status. Resources — data to read: files, database records. Prompts — ready-made templates, such as “summarise this issue”. Most often you will meet tools.")))


def s_connectors():
    sh = shot("claude_connectors", marks=[(1, 96.0, 6.8, "cyan"), (2, 96.0, 15.8, "violet"), (3, 96.0, 50.0, "green")],
              boxes=[(51.5, 3.0, 47.0, 7.6, "cyan"), (51.5, 12.0, 47.0, 7.6, "violet"), (51.5, 22.5, 47.0, 55.0, "green")])
    return dict(min=5, html=f'''
  {head(t("Вы это уже видели", "You have seen this"), t("Коннекторы в Claude — это MCP-серверы: включил и пользуешься", "Connectors in Claude are MCP servers: switch on and use"), k="cyan")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;">
        <div class="prompt-label">{t("claude.ai → + → Connectors · снято в L09", "claude.ai → + → Connectors · captured for L09")}</div>
        {sh}
      </div>
      <div class="stack" style="gap:20px;">
        {legend([(1, "cyan", t("<b>Add connector</b>: подключить новый сервер, в том числе свой по адресу", "<b>Add connector</b>: connect a new server, including your own by URL")),
                 (2, "violet", t("<b>Manage connectors</b>: какие инструменты разрешены", "<b>Manage connectors</b>: which tools are allowed")),
                 (3, "green", t("<b>Подключённые</b>: Atlassian, Figma, Gmail, Calendar, Drive, Chrome — каждый можно выключить", "<b>Connected</b>: Atlassian, Figma, Gmail, Calendar, Drive, Chrome — each can be switched off"))])}
        <div class="note" style="--k:var(--amber)">{t("Выключайте коннекторы, которые не нужны в этом чате: меньше инструментов — меньше ошибок и рисков.", "Switch off connectors you do not need in this chat: fewer tools, fewer mistakes and risks.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Если вы делали L09, вы уже пользовались MCP. В Claude кнопка плюс → Connectors (постоянная настройка — раздел Customize → Connectors). Каждый пункт списка — MCP-сервер: Atlassian, Figma, Gmail, Google Calendar, Google Drive. Переключатель включает или выключает его для этого чата. Add connector — подключить новый, в том числе свой по адресу. Manage connectors — настроить, какие инструменты сервера разрешены.",
                      "⏱ 5 min. If you did L09, you have already used MCP. In Claude: the plus button → Connectors (for permanent setup: Customize → Connectors). Each list item is an MCP server: Atlassian, Figma, Gmail, Google Calendar, Google Drive. The switch turns it on or off for this chat. Add connector connects a new one, including your own by URL. Manage connectors sets which of a server’s tools are allowed."),
                    t("Совет из L11: чем меньше инструментов включено, тем реже модель путается. Для чата про отпуск не нужен GitHub.",
                      "Advice from L11: the fewer tools are on, the less the model gets confused. A chat about leave does not need GitHub.")))


def s_permission():
    sh = shot("claude_permission", marks=[(1, 56.0, 6.5, "violet"), (2, 97.0, 30.0, "amber"), (3, 47.0, 81.0, "green")],
              boxes=[(1.5, 2.5, 52.0, 8.5, "violet"), (1.5, 18.0, 97.0, 46.0, "amber"), (1.5, 75.5, 97.0, 11.0, "green")])
    return dict(min=5, html=f'''
  {head(t("Разрешения", "Permissions"), t("Перед вызовом инструмента Claude спрашивает разрешение и показывает, что отправит", "Before a tool call Claude asks permission and shows what it will send"), k="amber")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:36px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;"><div class="prompt-label">{t("claude.ai · инструмент Figma «Generate Diagram» · снято в L09", "claude.ai · Figma tool “Generate Diagram” · captured for L09")}</div>{sh}
        {zoom("claude_permission_zoom", 1, "violet", t("крупно", "zoomed"), 620)}</div>
      <div class="stack" style="gap:18px;">
        {legend([(1, "violet", t("<b>Какой</b> инструмент и <b>из какого</b> сервера", "<b>Which</b> tool from <b>which</b> server")),
                 (2, "amber", t("<b>Что именно</b> уйдёт в сервис: прочитайте, при обрезке — Show full input", "<b>Exactly what</b> goes to the service: read it; if cut short, open Show full input")),
                 (3, "green", t("<b>Decline · Allow once · Always allow</b>", "<b>Decline · Allow once · Always allow</b>"))])}
        <div class="note" style="--k:var(--red)">{t("«Always allow» — только для безопасных инструментов чтения. Для отправки, удаления, оплаты — каждый раз вручную.", "“Always allow” only for safe read-only tools. For sending, deleting, paying — approve every time.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Это правило «человек в цикле» из L11 в настоящем продукте. Мы попросили Claude нарисовать схему обработки жалобы, и он решил вызвать инструмент Generate Diagram из сервера Figma. Прежде чем вызвать, Claude показывает: какой инструмент, из какого сервера и что именно он отправит — здесь код схемы с текстом про жалобу.",
                      "⏱ 5 min. This is the “human in the loop” rule from L11 inside a real product. We asked Claude to draw a complaint-handling diagram, and it decided to call the Generate Diagram tool from the Figma server. Before calling, Claude shows which tool, which server and exactly what it will send — here the diagram code with the complaint text."),
                    t("Три кнопки. Decline — отказать. Allow once — разрешить один раз. Always allow — больше не спрашивать для этого инструмента. Правило: «всегда» только для безопасных инструментов, которые читают. Всё, что отправляет письма, удаляет, платит или публикует, подтверждаем каждый раз и читаем, что уходит.",
                      "Three buttons. Decline — refuse. Allow once — allow this time. Always allow — stop asking for this tool. Rule: “always” only for safe tools that read. Anything that sends emails, deletes, pays or publishes gets approved every time, after reading what is being sent.")))


def s_code():
    code = ('from mcp.server import MCPServer\n\n'
            'mcp = MCPServer("courier")                 # имя сервера\n\n'
            '<span style=\'color:var(--green)\'>@mcp.tool()</span>\n'
            'def get_order_status(order_id: str) -> dict:\n'
            '    """<span style=\'color:var(--amber)\'>Current status and ETA of one delivery order.</span>"""\n'
            '    return {"status": "on the way", "courier": "Anna", "eta_minutes": 12}\n\n'
            'if __name__ == "__main__":\n'
            '    mcp.run()                            # запуск на этом компьютере')
    if LANG == "en":
        code = code.replace("# имя сервера", "# server name").replace("# запуск на этом компьютере", "# run on this computer")
    return dict(min=5, html=f'''
  {head(t("Свой сервер (справочно)", "Your own server (reference)"), t("Та же функция из L11 становится MCP-сервером за 10 строк", "The same L11 function becomes an MCP server in 10 lines"), k="violet")}
  <div class="body" style="margin-top:8px;">
    <div><div class="prompt-label">{t("Python, официальный пакет mcp, версия 2", "Python, the official mcp package, version 2")}</div><pre class="code" style="font-size:24px;line-height:1.6">{code}</pre></div>
    <div class="row" style="grid-template-columns:repeat(3,1fr);gap:36px;align-items:start;flex:none;margin-top:26px">
        <div class="note" style="--k:var(--green)">{t("<b>@mcp.tool()</b> — одна строка превращает обычную функцию в инструмент MCP.", "<b>@mcp.tool()</b> — one line turns a plain function into an MCP tool.")}</div>
        <div class="note" style="--k:var(--amber)">{t("<b>Docstring</b> — описание инструмента, как в L11. Модель выбирает по нему.", "The <b>docstring</b> is the tool description, as in L11. The model picks by it.")}</div>
        <div class="note" style="--k:var(--cyan)">{t("Дальше этот сервер можно подключить к Claude Desktop, LM Studio, VS Code — без изменений в коде.", "This server can then be plugged into Claude Desktop, LM Studio, VS Code — with no code changes.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Для тех, кто программирует. Официальный Python-пакет mcp (версия 2, Python 3.11+) содержит класс MCPServer — самый короткий способ сделать сервер; в старых статьях он называется FastMCP. Создаём сервер с именем courier, ставим над функцией строку @mcp.tool() — и функция get_order_status из L11 становится инструментом MCP. Docstring снова служит описанием для модели. mcp.run() запускает сервер на этом компьютере.",
                      "⏱ 5 min. For those who code. The official Python package mcp (version 2, Python 3.11+) contains the MCPServer class, the shortest way to build a server; older articles call it FastMCP. Create a server named courier, put @mcp.tool() above the function, and get_order_status from L11 becomes an MCP tool. The docstring again serves as the description for the model. mcp.run() starts the server on this computer."),
                    t("Главное отличие от L11: там функция жила внутри одного приложения. Здесь она — отдельный сервер, который можно подключить к любому хосту, поддерживающему MCP. Проверено с mcp 2.3.0, 16.10.2026; перед показом установите пакет (pip install mcp) и проверьте ещё раз.",
                      "The key difference from L11: there the function lived inside one app. Here it is a separate server that plugs into any MCP host. Tested with mcp 2.3.0 on 16.10.2026; before showing it, install the package (pip install mcp) and test it again.")))


def s_connect():
    cfg = ('{\n  "mcpServers": {\n    "courier": {\n      "command": "C:\\\\courier\\\\.venv\\\\Scripts\\\\python.exe",\n      "args": ["C:\\\\courier\\\\courier_server.py"]\n    }\n  }\n}')
    return dict(min=4, html=f'''
  {head(t("Подключить", "Plug it in"), t("Подключение — это несколько строк настроек: где лежит сервер и как его запустить", "Connecting is a few lines of settings: where the server is and how to start it"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:950px 1fr;gap:44px;align-items:center;flex:none;">
      <div><div class="prompt-label">{t("Настройки MCP: Claude Desktop (claude_desktop_config.json), LM Studio (mcp.json)", "MCP settings: Claude Desktop (claude_desktop_config.json), LM Studio (mcp.json)")}</div><pre class="code" style="font-size:25px;line-height:1.75;padding:28px 30px">{cfg}</pre></div>
      <div class="stack" style="gap:16px;">
        {legend([(1, "green", t("<b>Локальный сервер</b>: программа на вашем компьютере, хост запускает её сам (настройки слева, пути полные)", "<b>Local server</b>: a program on your computer; the host starts it itself (settings on the left, full paths)")),
                 (2, "cyan", t("<b>Удалённый сервер</b> — адрес в интернете + вход через ваш аккаунт (так работают коннекторы Claude)", "<b>Remote server</b> — an internet address + sign-in with your account (this is how Claude connectors work)")),
                 (3, "amber", t("<b>MCP Inspector</b> — бесплатная утилита, чтобы проверить сервер до подключения", "<b>MCP Inspector</b> — a free tool to test a server before connecting it"))])}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Чтобы хост узнал о сервере, ему дают несколько строк настроек. Для локального сервера: имя, команда запуска и аргументы — хост сам запускает программу на вашем компьютере. Такой формат с разделом mcpServers используют Claude Desktop (файл claude_desktop_config.json), LM Studio и Cursor (файл mcp.json); у VS Code похожий, но раздел называется servers. Путь к файлу сервера указывайте полный. Укажите полный путь к python.exe, где установлен пакет mcp, например C:\\courier\\.venv\\Scripts\\python.exe: просто «python» хост может не найти.",
                      "⏱ 4 min. For a host to know about a server, you give it a few lines of settings. For a local server: a name, a start command and arguments — the host starts the program on your computer itself. Claude Desktop (claude_desktop_config.json), LM Studio and Cursor (mcp.json) use this mcpServers format; VS Code uses a similar one with a servers key. Give the full path to the server file. Give the full path to the python.exe that has mcp installed, for example C:\\courier\\.venv\\Scripts\\python.exe: the host may not find a bare “python”."),
                    t("Удалённые серверы живут в интернете: вы указываете адрес и входите своим аккаунтом, как при подключении Google Drive в Claude. Перед подключением свой сервер удобно проверить в MCP Inspector — это официальная утилита, которая показывает список инструментов сервера и позволяет вызвать их вручную.",
                      "Remote servers live on the internet: you give an address and sign in with your account, as when connecting Google Drive in Claude. Before connecting your own server, check it in MCP Inspector — the official tool that lists a server’s tools and lets you call them by hand.")))


def s_agentbuild():
    prompt = t(
        "Сделай MCP-сервер на Python для курьерской службы. Только синтетические данные.\n"
        "1. Официальный пакет mcp версии 2 (класс MCPServer), сервер «courier», данные из orders.json (5 заказов).\n"
        "2. Инструменты: get_order_status(order_id) — только чтение; create_return(order_id, reason).\n"
        "3. Хорошие docstring: что делает, когда звать.\n"
        "4. Проверь сервер в MCP Inspector и покажи список инструментов.\n"
        "5. Дай настройки mcpServers для Claude Desktop и LM Studio.",
        "Build a Python MCP server for a courier service. Synthetic data only.\n"
        "1. The official mcp package v2 (MCPServer class), server “courier”, data from orders.json (5 orders).\n"
        "2. Tools: get_order_status(order_id) — read only; create_return(order_id, reason).\n"
        "3. Good docstrings: what it does, when to call it.\n"
        "4. Test the server in MCP Inspector and show the tool list.\n"
        "5. Give me the mcpServers settings for Claude Desktop and LM Studio.")
    return dict(min=4, html=f'''
  {head(t("Практика с агентом", "Hands-on with an agent"), t("Промпт для агента разработки: Codex в ChatGPT или Antigravity (бесплатно с лимитом), Claude Code (платно)", "Prompt for a coding agent: Codex in ChatGPT or Antigravity (free, with limits), Claude Code (paid)"), k="violet")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.65fr 1fr;gap:40px;align-items:center;flex:none;">
      <div><div class="prompt-label">{t("Промпт: MCP-сервер курьерской службы", "Prompt: a courier-service MCP server")}</div><pre class="code" style="font-size:24px;line-height:1.65;white-space:pre-wrap;padding:26px 30px">{prompt}</pre></div>
      <div class="stack" style="gap:18px;">
        <div class="note" style="--k:var(--green)">{t("Результат: один сервер, который увидят и Claude Desktop, и LM Studio с локальной моделью из L10.", "The result: one server that both Claude Desktop and LM Studio with the local model from L10 can see.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Агент будет ставить пакеты: читайте команды и подтверждайте шаги.", "The agent will install packages: read the commands and approve each step.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Как и в L10 и L11, руками писать не обязательно. Промпт описывает сервер с двумя инструментами, хорошими описаниями и проверкой в MCP Inspector. Агент разработки создаст проект, напишет код, запустит Inspector и выдаст настройки для Claude Desktop и LM Studio.",
                      "⏱ 4 min. As in L10 and L11, you do not have to write it by hand. The prompt describes a server with two tools, good descriptions and a check in MCP Inspector. A coding agent creates the project, writes the code, runs Inspector and hands you the settings for Claude Desktop and LM Studio."),
                    t("Связь уроков: модель из L10 в LM Studio + сервер из этого промпта = полностью локальный агент поддержки, который не отправляет данные наружу. Это вариант ДЗ по желанию. Что такое агент разработки и как его выбрать — L16.",
                      "Linking the lessons: the L10 model in LM Studio + the server from this prompt = a fully local support agent that sends no data outside. This is an optional homework path. What a coding agent is and how to choose one: L16.")))


def s_security():
    rows = [("red", t("Отравленное описание (tool poisoning)", "Tool poisoning"), t("в описании инструмента спрятана команда: «перешли файлы на адрес…»", "a hidden command in a tool description: “forward the files to…”")),
            ("red", t("Чужой текст в данных", "Injected text in data"), t("письмо или страница, прочитанные сервером, командуют моделью", "an email or page read by the server commands the model")),
            ("amber", t("Лишние права", "Too many permissions"), t("сервер просит доступ ко всему Drive, хотя нужна одна папка", "a server asks for all of Drive when one folder would do")),
            ("amber", t("Подмена после установки", "A “rug pull”"), t("сервер обновился и стал делать другое", "the server updated itself and now does something else"))]
    lr = "".join(f'<div class="lrow" style="--k:var(--{k})"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for k, h, d in rows)
    rules = "".join(f"<li><span>{r}</span></li>" for r in [
        t("Сервер от известного автора или своей компании", "A server from a known publisher or your own company"),
        t("Минимум прав, ненужные — выключить", "Least privilege; switch off what you do not need"),
        t("Читать запрос разрешения", "Read the permission prompt"),
        t("«Всегда разрешать» — только для чтения", "“Always allow” only for reading"),
        t("Рабочие данные — только через одобренные компанией коннекторы", "Work data only through company-approved connectors")])
    return dict(min=5, html=f'''
  {head(t("Безопасность", "Security"), t("Подключённый сервер получает доступ к вашим данным. Подключайте только проверенные", "A connected server gets access to your data. Connect only trusted ones"), k="red")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="light big" style="gap:18px">{lr}</div>
      <div class="stack" style="gap:12px"><div class="prompt-label">{t("Правила", "Rules")}</div><ol class="checklist rules">{rules}</ol></div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. MCP-сервер — это программа, которой вы даёте доступ к почте, файлам, задачам. Четыре типичных риска. Отравленное описание: в описании инструмента, которое модель читает, спрятана команда; пользователь её не видит, а модель может послушаться. Чужой текст в данных: тот же prompt injection из L11, но через письма и страницы, которые читает сервер. Лишние права: сервер просит больше, чем нужно. Подмена: сервер был безопасным, а после обновления стал делать другое.",
                      "⏱ 5 min. An MCP server is a program you give access to your mail, files and tasks. Four typical risks. Tool poisoning: a command hidden in a tool description the model reads; the user does not see it, the model may obey. Injected text in data: the same prompt injection as in L11, through emails and pages the server reads. Too many permissions: a server asks for more than it needs. A rug pull: a server was safe, then an update changed what it does."),
                    t("Правила простые: подключать серверы от известных авторов или своей компании, давать минимум прав, выключать ненужные, читать запрос разрешения и разрешать «всегда» только чтение. Для рабочих данных — только коннекторы, одобренные вашей компанией.",
                      "The rules are simple: connect servers from known publishers or your own company, grant least privilege, switch off what you do not need, read the permission prompt and allow “always” only for reading. For work data, only connectors approved by your company.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут: отключитесь от всех серверов", "5 minutes: disconnect from every server")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: фреймворки агентов, когда они нужны, агенты, которые говорят с агентами, упражнение и ДЗ.", "Next: agent frameworks, when you need one, agents talking to agents, an exercise and homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт».", "⏱ 5 min. Press “Start”.")))


def s_exercise():
    qs = [(t("Отдел продаж: «Подготовь сводку по клиенту из CRM и почты»", "Sales: “Prepare a client summary from the CRM and mail”"), "cyan"),
          (t("Бухгалтерия: «Сверь счета из папки Drive с таблицей»", "Accounting: “Match invoices in a Drive folder against a sheet”"), "cyan"),
          (t("Поддержка: «Ответь клиенту и закрой тикет»", "Support: “Reply to the customer and close the ticket”"), "cyan"),
          (t("HR: «Найди в резюме кандидатов знание Python»", "HR: “Find Python skills in candidates’ CVs”"), "cyan")]
    rows = "".join(f'<div class="lrow" style="--k:var(--{k})"><div class="dot"></div><div><div class="h">{q}</div><div class="d">{t("какие серверы? какие права? где подтверждение?", "which servers? which permissions? where is the confirmation?")}</div></div></div>' for q, k in qs)
    return dict(min=4, html=f'''
  {head(t("Упражнение", "Exercise"), t("Упражнение: какие MCP-серверы подключить и что разрешить?", "Exercise: which MCP servers to connect, and what to allow?"), k="cyan")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="light big" style="gap:12px">{rows}</div>
      <div class="stack" style="gap:18px;">
        <div class="note" style="--k:var(--violet)">{t("Выберите одну задачу и ответьте в чат тремя строками: серверы, права (чтение или запись), где нужен человек.", "Pick one task and answer in the chat in three lines: servers, permissions (read or write), where a human is needed.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Подсказка: «закрыть тикет» и «ответить клиенту» — действия с последствиями.", "Hint: “close the ticket” and “reply to the customer” are actions with consequences.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Упражнение в чат, 3 минуты. Каждый выбирает одну задачу и пишет: какие серверы нужны, какие права (только чтение или запись) и где должен подтверждать человек.",
                      "⏱ 4 min. Chat exercise, 3 minutes. Everyone picks one task and writes which servers are needed, what permissions (read only or write) and where a human must confirm."),
                    t("Разбор. Продажи: CRM и почта, только чтение, подтверждение не нужно — это сводка. Бухгалтерия: Drive и таблицы, чтение одной папки; если агент правит таблицу — подтверждение. Поддержка: тикеты и почта; ответ клиенту и закрытие тикета — действия с последствиями, их подтверждает человек. HR: файлы с резюме — персональные данные: только одобренный компанией коннектор и только нужная папка.",
                      "Walk-through. Sales: CRM and mail, read only, no confirmation — it is a summary. Accounting: Drive and sheets, read one folder; if the agent edits the sheet — confirmation. Support: tickets and mail; replying to the customer and closing the ticket have consequences, a human confirms. HR: CV files are personal data: only a company-approved connector and only the folder needed.")))


def s_hw():
    tree = ("genai-homeworks/L12/\n├─ README.md      # задача и вывод\n├─ servers.md     # 2–3 сервера: что дают\n├─ demo.png       # запрос разрешения\n└─ rules.md       # права и подтверждения")
    if LANG == "en":
        tree = ("genai-homeworks/L12/\n├─ README.md      # task, conclusion\n├─ servers.md     # 2–3 servers: tools\n├─ demo.png       # permission prompt\n└─ rules.md       # permissions, confirmations")
    steps = [t("Выберите рабочую задачу, где ИИ нужны ваши данные или сервисы", "Pick a work task where the AI needs your data or services"),
             t("Найдите 2–3 подходящих MCP-сервера (коннекторы Claude/ChatGPT или реестр)", "Find 2–3 suitable MCP servers (Claude/ChatGPT connectors or the registry)"),
             t("Подключите один на тестовых данных и сделайте скриншот запроса разрешения", "Connect one on test data and screenshot the permission prompt"),
             t("Для каждого сервера: автор, какие инструменты, какие права нужны", "For each server: publisher, which tools, which permissions it needs"),
             t("Правила: что разрешить «всегда», что — каждый раз, что не подключать", "Rules: what to allow “always”, what every time, what not to connect")]
    ol = "".join(f"<li><span>{s}</span></li>" for s in steps)
    return dict(min=5, html=f'''
  {head(t("Домашнее задание", "Homework"), t("ДЗ: подобрать MCP-серверы для своей задачи и описать правила доступа", "Homework: pick MCP servers for your task and write the access rules"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:44px;align-items:start;flex:none;">
      <div class="stack" style="gap:26px"><ol class="checklist hw">{ol}</ol>
        <div class="note" style="--k:var(--red)">{t("Бесплатный план: Claude → Customize → Connectors → Add custom connector (на Free — один). Адрес — удалённый сервер из официального реестра или с сайта сервиса; скриншот запроса разрешения. Кто пишет код — LM Studio + сервер со слайда 11.", "Free plan: Claude → Customize → Connectors → Add custom connector (one on Free). Use a remote server URL from the official registry or the service's site; screenshot the permission prompt. If you code: LM Studio + the slide 11 server.")}</div></div>
      <div class="stack" style="gap:18px;">
        <pre class="code" style="font-size:21px;line-height:1.6">{tree}</pre>
        <div class="note" style="--k:var(--amber)">{t("Код по желанию: свой сервер по промпту со слайда 11.", "Code optional: your own server with the slide 11 prompt.")}</div>
        <div class="note" style="--k:var(--green)">{t("Только тестовые данные и личные или учебные аккаунты.", "Test data and personal or training accounts only.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. ДЗ без обязательного кода. Выбрать задачу, найти 2–3 MCP-сервера, подключить один в Claude или ChatGPT на тестовых данных и сделать скриншот запроса разрешения. Для каждого сервера записать автора, инструменты и нужные права. В конце — правила: что разрешать всегда, что каждый раз, что не подключать вовсе. На бесплатном плане свой сервер в ChatGPT не добавить: берите готовый коннектор Claude (Google Drive) или LM Studio с сервером со слайда 11. Подробности в L12_05_Homework.",
                      "⏱ 5 min. Homework with no required code. Pick a task, find 2–3 MCP servers, connect one in Claude or ChatGPT on test data and screenshot the permission prompt. For each server record the publisher, the tools and the permissions needed. Finally the rules: what to allow always, what every time, what never to connect. On a free plan you cannot add your own server in ChatGPT: use a ready-made Claude connector (Google Drive) or LM Studio with the slide 11 server. Details in L12_05_Homework.")))


def s_summary():
    rules = [("violet", t("MCP = стандартный разъём", "MCP = a standard plug"), t("один сервер работает во многих приложениях", "one server works in many apps")),
             ("cyan", t("Хост · клиент · сервер", "Host · client · server"), t("сервер даёт инструменты, ресурсы, промпты", "the server offers tools, resources, prompts")),
             ("amber", t("Разрешения и минимум прав", "Permissions and least privilege"), t("«всегда» — только для чтения", "“always” only for reading")),
             ("green", t("Фреймворк — когда нужен", "A framework when needed"), t("много шагов, память, несколько агентов", "many steps, memory, several agents"))]
    li = "".join(f'<div class="task" style="--k:var(--{k});padding:44px 34px"><div><div class="h" style="font-size:35px">{h}</div><div class="d" style="font-size:26px;margin-top:12px">{d}</div></div></div>' for k, h, d in rules)
    return dict(min=3, html=f'''
  {head(t("Итоги", "Summary"), t("MCP подключает инструменты, разрешения берегут данные, фреймворк — только когда шагов много", "MCP plugs in tools, permissions protect your data, a framework only when there are many steps"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="tasks" style="gap:30px 34px">{li}</div>
    <div class="note" style="margin-top:56px;--k:var(--green)">{t("<b>Дальше, L13:</b> свои ассистенты без кода (проекты Claude, плагины ChatGPT, агенты Copilot) и Agents SDK.", "<b>Next, L13:</b> your own assistants without code (Claude projects, ChatGPT plugins, Copilot agents) and the Agents SDK.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Четыре мысли. MCP — стандартный разъём: один сервер работает во многих приложениях. Роли: хост, клиент, сервер; сервер даёт инструменты, ресурсы и промпты. Безопасность: читать запрос разрешения, давать минимум прав, «всегда» только для чтения. Фреймворк агентов нужен, когда шагов много, нужна память или несколько агентов.",
                      "⏱ 3 min. Four ideas. MCP is a standard plug: one server works in many apps. Roles: host, client, server; the server offers tools, resources and prompts. Security: read the permission prompt, grant least privilege, “always” only for reading. An agent framework is needed when there are many steps, memory or several agents."),
                    t("Следующий урок: свои ассистенты без кода — проекты в Claude, плагины в ChatGPT (они заменяют GPTs), агенты Copilot — и Agents SDK для тех, кто пишет код.",
                      "Next lesson: your own assistants without code — projects in Claude, plugins in ChatGPT (they replace GPTs), Copilot agents — and the Agents SDK for those who code.")))


def s_hosts():
    sh = shot(t("chatgpt_plugins", "chatgpt_plugins_en"),
              marks=[(1, t(69.0, 77.0), 6.0, "green"), (2, t(22.0, 48.0), t(34.0, 35.5), "violet"), (3, 3.0, t(54.0, 50.0), "cyan")],
              boxes=[(t(71.0, 79.0), 1.5, t(27.5, 18.0), 9.0, "green"), (t(24.0, 50.0), t(29.5, 31.5), t(72.0, 46.0), 8.5, "violet"),
                     (1.5, t(53.0, 49.0), 97.0, t(46.5, 50.5), "cyan")])
    return dict(min=4, html=f'''
  {head(t("Где работает", "Where it works"), t("В ChatGPT это называется «Плагины»: туда тоже можно добавить свой MCP-сервер", "In ChatGPT this is called Plugins: you can add your own MCP server there too"), k="cyan")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:553px 1fr;gap:44px;align-items:start;flex:none;">
      <div class="stack" style="gap:8px;"><div class="prompt-label">{t("chatgpt.com/plugins → Добавить · 16.10.2026", "chatgpt.com/plugins → Add · 16.10.2026")}</div>{sh}</div>
      <div class="stack" style="gap:18px;">
        {legend([(1, "green", t("<b>Добавить</b>: меню создания", "<b>Add</b>: the create menu")),
                 (2, "violet", t("<b>Добавить пользовательский сервер MCP</b>: свой сервер по адресу в интернете", "<b>Add custom MCP server</b>: your own server by internet address")),
                 (3, "cyan", t("<b>Готовые</b>: Google Drive, Calendar, Slack, а также Gmail, GitHub, Outlook", "<b>Ready-made</b>: Google Drive, Calendar, Slack, plus Gmail, GitHub, Outlook"))])}
        <div class="small" style="font-size:19px">{t("В английском интерфейсе: Plugins → Add → Add custom MCP server.", "In the Russian UI: Плагины → Добавить → Добавить пользовательский сервер MCP.")}</div>
        <div class="note" style="--k:var(--red)">{t("Свой сервер в ChatGPT — только на платных тарифах (режим разработчика); проверьте свой план.", "Your own server in ChatGPT needs a paid plan (developer mode); check yours.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Ещё MCP понимают VS Code, Cursor, Codex (L16) и LM Studio (модель из L10).", "VS Code, Cursor, Codex (L16) and LM Studio (the L10 model) speak MCP too.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Тот же стандарт в ChatGPT. Раздел «Плагины» (раньше — приложения и коннекторы): готовые Gmail, Google Drive, GitHub, Google Calendar, Outlook, Slack. Кнопка «Добавить» → «Добавить пользовательский сервер MCP»: свой сервер по адресу в интернете (локальный — только через защищённый туннель). Плагины в ChatGPT также заменяют GPTs, их отключают 11 декабря 2026 — об этом L13. Добавить свой сервер можно только на платных тарифах (режим разработчика); в документации OpenAI бесплатный план среди допущенных не указан.",
                      "⏱ 4 min. The same standard in ChatGPT. The Plugins section (formerly apps and connectors): ready-made Gmail, Google Drive, GitHub, Google Calendar, Outlook, Slack. The Add button → Add custom MCP server: your own server by internet address (a local one only through a secure tunnel). Plugins in ChatGPT also replace GPTs, which retire on 11 December 2026 — see L13. Adding your own server needs a paid plan (developer mode); OpenAI’s docs do not list the free plan as eligible."),
                    t("Ещё хосты: VS Code, Cursor и Codex (агенты разработки, L16), LM Studio с версии 0.3.17 (Program → Install → Edit mcp.json, инструменты для локальной модели из L10), Microsoft Copilot Studio, приложение Gemini (пока только США, английский). Ollama сама не хост: она отдаёт модель приложению.",
                      "More hosts: VS Code, Cursor and Codex (coding agents, L16), LM Studio since 0.3.17 (Program → Install → Edit mcp.json, tools for the L10 local model), Microsoft Copilot Studio, the Gemini app (US and English only for now). Ollama is not a host itself: it serves the model to an app.")))


def s_registry():
    sh = shot("mcp_registry_crop", marks=[(1, 56.5, 10.0, "cyan"), (2, 97.0, 50.0, "amber")], boxes=[(0.6, 1.0, 54.0, 20.0, "cyan"), (0.6, 49.0, 98.8, 50.0, "amber")])
    return dict(min=4, html=f'''
  {head(t("Реестр", "Registry"), t("Официальный реестр: десятки тысяч серверов, и опубликовать может любой", "The official registry: tens of thousands of servers, and anyone can publish"), k="amber")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:960px 1fr;gap:40px;align-items:start;flex:none;">
      <div class="stack" style="gap:8px;"><div class="prompt-label">{t("registry.modelcontextprotocol.io · снято 16.10.2026", "registry.modelcontextprotocol.io · captured 16.10.2026")}</div>{sh}</div>
      <div class="stack" style="gap:22px;">
        <div class="note" style="--k:var(--red)">{t("Реестр хранит только описания и не проверяет безопасность. Ищите <b>официальный сервер компании</b>: GitHub, Notion, Figma, Atlassian, Stripe, Slack делают свои.", "The registry stores descriptions only and does not vet security. Look for the <b>company’s official server</b>: GitHub, Notion, Figma, Atlassian, Stripe, Slack run their own.")}</div>
        {legend([(1, "cyan", t("<b>Официальный реестр</b>, пока в статусе превью", "<b>The official registry</b>, still in preview")), (2, "amber", t("<b>Недавно обновлённые</b>: опубликовать может любой", "<b>Recently updated</b>: anyone can publish"))])}
        <div class="stat" style="--k:var(--amber);margin-top:20px"><div class="n" style="font-size:68px">≈ {t("44 000", "44,000")}</div><div class="d">{t("серверов в реестре (наш подсчёт через его API, 16.10.2026)", "servers in the registry (our count via its API, 16.10.2026)")}</div></div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Где искать серверы. Официальный реестр registry.modelcontextprotocol.io — пока в статусе превью. Мы посчитали через его API около 44 тысяч записей. Посмотрите на «недавно обновлённые»: от чатов для агентов до данных о криптовалютах. Реестр хранит только описания и не проверяет, безопасен ли сервер.",
                      "⏱ 4 min. Where to find servers. The official registry at registry.modelcontextprotocol.io is still in preview. We counted about 44 thousand entries via its API. Look at “recently updated”: from agent chat rooms to crypto data. The registry stores descriptions only and does not check whether a server is safe."),
                    t("Правило: для популярного сервиса ищите сервер от самой компании. GitHub, Notion, Figma, Atlassian, Stripe и Slack запускают официальные серверы; например, GitHub держит свой по адресу api.githubcopilot.com/mcp, а старый пакет из репозитория примеров устарел. Сторонний сервер для почты или банка — красный флаг.",
                      "Rule: for a popular service, look for the company’s own server. GitHub, Notion, Figma, Atlassian, Stripe and Slack run official servers; GitHub, for example, hosts its own at api.githubcopilot.com/mcp, and the old package from the examples repo is deprecated. A third-party server for your mail or bank is a red flag.")))


def s_adoption():
    stats = [("cyan", t("≈ 0,5 млрд", "≈ 0.5 bn"), t("загрузок библиотек MCP для программистов в месяц (официальный блог, июль 2026)", "downloads a month of the MCP developer libraries (official blog, July 2026)")),
             ("green", t("> 10 000", "> 10,000"), t("активных публичных серверов уже в декабре 2025", "active public servers already in December 2025")),
             ("violet", t("Дек 2025", "Dec 2025"), t("MCP передан в Agentic AI Foundation (Linux Foundation); соучредители Anthropic, Block, OpenAI", "MCP donated to the Agentic AI Foundation (Linux Foundation); co-founded by Anthropic, Block, OpenAI"))]
    tiles = "".join(f'<div class="stat" style="--k:var(--{k});flex:1"><div class="n" style="font-size:72px">{n}</div><div class="d" style="font-size:23px;margin-top:6px">{d}</div></div>' for k, n, d in stats)
    pts = [(t("Ноя 2024", "Nov 2024"), t("Anthropic открывает MCP", "Anthropic opens MCP")),
           (t("Дек 2025", "Dec 2025"), t("передан в фонд при Linux Foundation", "donated to a Linux Foundation fund")),
           (t("Июл 2026", "Jul 2026"), t("новая версия стандарта, Python-библиотека v2", "new spec version, Python library v2")),
           (t("Окт 2026", "Oct 2026"), t("≈ 44 000 серверов в реестре", "≈ 44,000 servers in the registry"))]
    tl = "".join(f'<div style="position:relative;padding-top:34px"><div style="position:absolute;top:0;left:0;width:22px;height:22px;border-radius:50%;background:var(--violet)"></div>'
                 f'<div style="font:800 30px/1.2 var(--display);color:var(--violet)">{d}</div><div style="font:500 23px/1.35 var(--body);color:var(--muted);margin-top:6px">{x}</div></div>' for d, x in pts)
    timeline = (f'<div style="position:relative;margin-top:84px"><div style="position:absolute;left:11px;right:0;top:10px;height:3px;background:var(--violet);opacity:.5"></div>'
                f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:30px">{tl}</div></div>')
    return dict(min=4, html=f'''
  {head(t("Масштаб", "Scale"), t("За два года MCP стал общим стандартом, а не проектом одной компании", "In two years MCP became a shared standard, not one company’s project"), k="green")}
  <div class="body" style="margin-top:16px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px;">{tiles}</div>
    {timeline}
    <div class="note" style="margin-top:80px;--k:var(--amber)">{t("Стандарт быстро меняется: в июле 2026 вышла новая версия. Код из старых статей может не работать.", "The standard moves fast: a new version came out in July 2026. Code from older articles may not work.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Почему MCP стоит учить. По официальному блогу MCP, SDK скачивают почти полмиллиарда раз в месяц. Уже в декабре 2025 было больше 10 тысяч активных публичных серверов. В том же декабре Anthropic передала MCP в Agentic AI Foundation при Linux Foundation, её соучредители — Anthropic, Block и OpenAI. То есть стандарт больше не принадлежит одной компании.",
                      "⏱ 4 min. Why MCP is worth learning. According to the official MCP blog, the SDKs are downloaded almost half a billion times a month. Already in December 2025 there were over 10 thousand active public servers. That same December Anthropic donated MCP to the Agentic AI Foundation at the Linux Foundation, co-founded by Anthropic, Block and OpenAI. So the standard no longer belongs to one company."),
                    t("Минус быстрого роста: стандарт меняется. Спецификация от 28 июля 2026 стала проще для облачных серверов; часть старых функций устарела. Python-библиотека перешла на версию 2, и код из статей 2025 года может не запускаться.",
                      "The downside of fast growth: the standard changes. The 28 July 2026 spec became simpler for cloud servers; some old features were deprecated. The Python library moved to version 2, and code from 2025 articles may not run.")))


def s_layers():
    return dict(min=4, html=f'''
  {head(t("Три слоя", "Three layers"), t("Вызов функций, MCP и фреймворк: слои вложены друг в друга, их не надо путать", "Function calling, MCP and a framework are nested layers; do not mix them up"), k="violet")}
  <div class="body" style="margin-top:14px;">
    {layers_diagram()}
    <div class="note" style="margin-top:30px;--k:var(--amber)">{t("Берите минимум, который решает задачу: один чат с парой функций — хватит вызова функций; один инструмент для многих приложений — MCP; много шагов и агентов — фреймворк.", "Use the least machinery that solves the task: one chat with a couple of functions — function calling is enough; one tool for many apps — MCP; many steps and agents — a framework.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Три слова часто путают. Вызов функций (L11) отвечает на вопрос, как модель просит действие. MCP отвечает, как приложение находит готовые инструменты и вызывает их стандартным способом. Фреймворк агентов отвечает, кто крутит цикл: сколько шагов, что запомнить, где спросить человека, как записать журнал.",
                      "⏱ 4 min. These three words get mixed up. Function calling (L11) answers how the model asks for an action. MCP answers how an app finds ready-made tools and calls them in a standard way. An agent framework answers who runs the loop: how many steps, what to remember, where to ask a human, how to log."),
                    t("Слои складываются: фреймворк может использовать MCP-серверы, а внутри всё равно работает вызов функций. Но не начинайте с «MCP плюс фреймворк» для задачи, где хватит одного чата с двумя функциями.",
                      "The layers stack: a framework can use MCP servers, and inside it is still function calling. But do not start with “MCP plus a framework” for a task that one chat with two functions would solve.")))


def s_frameworks():
    fw = [("cyan", "OpenAI Agents SDK", "MIT", t("агенты, передача задачи другому агенту, автоматические проверки", "agents, handing a task to another agent, automatic checks")),
          ("violet", "Claude Agent SDK", t("условия Anthropic", "Anthropic terms"), t("тот же движок, что у Claude Code", "the same engine as Claude Code")),
          ("green", "Google ADK", "Apache-2.0", t("агенты на Gemini и других моделях, запуск в Google Cloud", "agents on Gemini and other models, run in Google Cloud")),
          ("amber", "LangGraph", "MIT", t("агент как схема шагов с памятью и паузами на подтверждение", "an agent as a graph of steps with memory and approval pauses")),
]
    rows = [(n, f"{d}", k) for k, n, v, d in fw]
    lr = "".join(f'<div class="lrow" style="--k:var(--{k})"><div class="dot"></div><div><div class="h">{n} <span style="font-weight:400;color:var(--dim);font-size:19px">{v}</span></div><div class="d">{d}</div></div></div>' for k, n, v, d in fw)
    return dict(min=5, html=f'''
  {head(t("Фреймворки", "Frameworks"), t("Фреймворки агентов: готовый цикл, память, подтверждения и журнал", "Agent frameworks: a ready loop, memory, approvals and logs"), k="green")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.4fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="light big" style="gap:16px">{lr}</div>
      <div class="stack" style="gap:24px;">
        <div class="note" style="--k:var(--green)">{t("Сами библиотеки бесплатные, почти все с открытым кодом; платите за модель. Ещё: Microsoft Agent Framework, CrewAI, LlamaIndex, Pydantic AI.", "The libraries are free and almost all are open source; you pay for the model. Also: Microsoft Agent Framework, CrewAI, LlamaIndex, Pydantic AI.")}</div>
        <div class="note" style="--k:var(--violet)">{t("Почти все умеют подключать MCP-серверы — инструменты из первой части урока переносятся.", "Almost all can connect MCP servers, so the tools from the first part carry over.")}</div>
        
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Фреймворк агентов — библиотека, которая берёт на себя цикл из L11 и всё вокруг него: память между шагами, передачу задачи другому агенту, паузы на подтверждение человеком, журнал (трассировку). OpenAI Agents SDK и Claude Agent SDK — от поставщиков моделей; Claude Agent SDK использует тот же движок, что Claude Code, код Python-версии открыт под MIT, но использование SDK регулируется коммерческими условиями Anthropic.",
                      "⏱ 5 min. An agent framework is a library that takes over the L11 loop and everything around it: memory between steps, handing a task to another agent, pauses for human approval, logging (tracing). The OpenAI Agents SDK and the Claude Agent SDK come from model vendors; the Claude Agent SDK uses the same engine as Claude Code; the Python SDK code is MIT, but use of the SDK is governed by Anthropic’s commercial terms."),
                    t("Google ADK — агенты на Gemini и других моделях с удобным деплоем в Google Cloud. LangGraph описывает агента как схему шагов с памятью и паузами. Microsoft Agent Framework — прямой преемник AutoGen и Semantic Kernel; AutoGen теперь только поддерживается, а новым проектам Microsoft советует Agent Framework. CrewAI — «команда» агентов с ролями. Ещё есть LlamaIndex и Pydantic AI. Выбирать по экосистеме: на какой модели и в каком облаке вы работаете.",
                      "Google ADK — agents on Gemini and other models with easy deployment to Google Cloud. LangGraph describes an agent as a graph of steps with memory and pauses. Microsoft Agent Framework is the direct successor to AutoGen and Semantic Kernel; AutoGen is now maintenance-only, and Microsoft points new projects to Agent Framework. CrewAI — a “crew” of agents with roles. There are also LlamaIndex and Pydantic AI. Choose by ecosystem: which model and which cloud you work with.")))


def s_when():
    steps = [("cyan", t("Один чат, 1–3 функции", "One chat, 1–3 functions"), t("вызов функций, как в L11", "function calling, as in L11")),
             ("violet", t("Один инструмент — много приложений", "One tool, many apps"), t("MCP-сервер", "an MCP server")),
             ("green", t("Много шагов, память, подтверждения", "Many steps, memory, approvals"), t("фреймворк агентов", "an agent framework")),
             ("amber", t("Несколько агентов разных компаний", "Several agents from different companies"), t("A2A (следующий слайд)", "A2A (next slide)"))]
    flow = '<div class="arr" style="font-size:40px;color:var(--dim)">↓</div>'.join(
        f'<div class="task" style="--k:var(--{k});padding:24px 30px;width:100%"><div style="display:flex;justify-content:space-between;width:100%;gap:20px"><div class="h" style="font-size:29px">{a}</div><div class="d" style="font-size:26px;color:var(--{k})">→ {b}</div></div></div>' for k, a, b in steps)
    return dict(min=4, html=f'''
  {head(t("Когда что", "When to use what"), t("Добавляйте сложность только тогда, когда простого перестало хватать", "Add complexity only when the simple option stops being enough"), k="cyan")}
  <div class="body" style="margin-top:10px;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:8px;max-width:1300px;margin:0 auto;width:100%">{flow}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Лестница сложности. Начинаем сверху, с самого простого, и спускаемся ниже, только если упёрлись. Один чат и пара функций — хватит вызова функций. Нужно, чтобы один инструмент работал в Claude, ChatGPT и вашем боте — делаем MCP-сервер. Агент делает много шагов, должен помнить контекст, спрашивать подтверждение и вести журнал — берём фреймворк. Несколько агентов от разных компаний должны договориться между собой — протокол A2A.",
                      "⏱ 4 min. A complexity ladder. Start at the top and step down only when you hit a limit. One chat and a couple of functions — function calling is enough. One tool must work in Claude, ChatGPT and your bot — build an MCP server. The agent takes many steps, must remember context, ask for approval and keep a log — use a framework. Several agents from different companies must coordinate — the A2A protocol.")))


def s_a2a():
    return dict(min=4, html=f'''
  {head("A2A", t("A2A: стандарт, по которому агенты разных компаний договариваются друг с другом", "A2A: a standard for agents from different companies to work with each other"), k="amber")}
  <div class="body" style="margin-top:16px;">
    <div style="zoom:1.12;margin-top:10px">{a2a_diagram()}</div>
    <div class="note" style="margin-top:40px;--k:var(--green)">{t("A2A начинал Google; версия 1.0 вышла в марте 2026, с августа 2026 протокол в том же фонде, что и MCP.", "Google started A2A; version 1.0 shipped in March 2026, and since August 2026 it lives in the same foundation as MCP.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Последний стандарт урока, для общего понимания. MCP соединяет агента с инструментами и данными. A2A, Agent2Agent, соединяет агентов между собой: ваш агент-ассистент просит агента отеля забронировать номер, и они договариваются, не зная, как устроены друг у друга внутри.",
                      "⏱ 4 min. The last standard of the lesson, for general understanding. MCP connects an agent to tools and data. A2A, Agent2Agent, connects agents to each other: your assistant agent asks a hotel’s agent to book a room, and they coordinate without knowing each other’s internals."),
                    t("A2A начинал Google, версия 1.0 вышла в марте 2026, а 17 августа 2026 протокол перешёл в тот же фонд при Linux Foundation, что и MCP. Для новичка достаточно знать, что такое слово есть и что это про общение агентов разных компаний.",
                      "Google started A2A; version 1.0 shipped in March 2026, and on 17 August 2026 the protocol moved to the same Linux Foundation foundation as MCP. For a beginner it is enough to know the word exists and means agents from different companies talking.")))


SLIDES = [s_cover, s_hook, s_hub, s_roles, s_connectors, s_permission, s_hosts, s_registry, s_code, s_connect,
          s_agentbuild, s_security, s_layers, s_adoption, s_break, s_frameworks, s_when, s_a2a, s_exercise, s_hw, s_summary]


# ---------------------------------------------------------------- page
EXTRA_CSS = """
.bars .ref, .vline { position: absolute; top: 0; bottom: 26px; border-left: 2px dashed var(--k, var(--amber)); }
.vline span { position: absolute; top: -32px; left: 6px; white-space: nowrap; font: 600 17px var(--body); color: var(--k); }
/* final audit: top-aligned bodies (break slide keeps its own centred .brk) and ~15% larger running text */
.slide:not(.cover) .body { justify-content: flex-start; padding-top: 22px; }
.note { font-size: 23px; }
.legend div { font-size: 23px; }
.lrow .h { font-size: 26px; } .lrow .d { font-size: 21px; }
.light.big .lrow { padding: 24px 24px; } .light.big .lrow .h { font-size: 28px; } .light.big .lrow .d { font-size: 22px; margin-top: 4px; }
.checklist li { font-size: 24px; } .checklist { gap: 18px; }
.checklist.rules li::before { background: var(--amber); }
"""


def build(lang):
    global LANG
    LANG = lang
    css = (HERE / "style.css").read_text(encoding="utf-8") + EXTRA_CSS
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
    assert total == 21 and SLIDES[14] is s_break and SLIDES[19] is s_hw
    title = t("Урок 12: MCP и фреймворки агентов | GenAI Basics", "Lesson 12: MCP and agent frameworks | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<!-- generated by deck_v2/build.py; edit the generator, not this file -->
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
    print(f"{lang}: {OUT[lang].name}: {total} slides, {minutes} min")
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


if __name__ == "__main__":
    for lg in ("ru", "en"):
        h = build(lg)
        if "--no-pdf" not in sys.argv:
            pdf(h)
