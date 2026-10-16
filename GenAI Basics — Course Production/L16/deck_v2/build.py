# -*- coding: utf-8 -*-
"""Build the L16 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. Images live in ../assets/v2/img/ (own claude.ai/code capture 2026-10-16,
a cover image made with genai-assets; diagrams are drawn in HTML).
Facts: ../L16_08_Source_Notes_Research_2026-10.md.
"""
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L16 = HERE.parent
NAME = "presentation_L16_Agentic_Software_Development"
OUT = {"ru": L16 / f"{NAME}_v2.html", "en": L16 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 16 • Агентная разработка", "en": "GenAI Basics • Lesson 16 • Agentic development"}


# ---------------------------------------------------------------- helpers
def num(x, d=1):
    s = f"{x:.{d}f}"
    return s.replace(".", ",") if LANG == "ru" else s


def head(kicker, title, lead=None, k=None):
    ks = f' style="--k:var(--{k})"' if k else ""
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


# ---------------------------------------------------------------- slides
def _lr(rows):
    return "".join(f'<div class="lrow" style="--k:var(--{k})"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for k, h, d in rows)

def flow(steps, h=150, fs=25, ds=19):
    """Horizontal chain of numbered boxes with arrows: steps = [(colour, title, desc)]."""
    out = []
    for i, (k, t_, d) in enumerate(steps):
        if i:
            out.append('<div style="align-self:center;font-size:40px;color:var(--muted);text-align:center">→</div>')
        out.append(f'<div style="background:var(--surface-card);border:1px solid var(--line);border-top:5px solid var(--{k});border-radius:14px;padding:20px 22px;min-height:{h}px">'
                   f'<div style="width:40px;height:40px;border-radius:50%;background:var(--{k});color:#0b0f17;font:800 22px/40px var(--body);text-align:center;margin-bottom:12px">{i + 1}</div>'
                   f'<div style="font:700 {fs}px/1.25 var(--body);color:var(--fg)">{t_}</div>'
                   f'<div style="font:400 {ds}px/1.35 var(--body);color:var(--muted);margin-top:6px">{d}</div></div>')
    cols = " 50px ".join(["1fr"] * len(steps))
    return f'<div style="display:grid;grid-template-columns:{cols};gap:6px">{"".join(out)}</div>'



def loop_diagram():
    """The plan → act → verify → review loop drawn in HTML (bilingual, large text)."""
    nodes = [("cyan", 1, t("План", "Plan"), t("договориться, что делаем", "agree what to build"), 300, 105),
             ("violet", 2, t("Действие", "Act"), t("агент правит файлы", "the agent edits files"), 495, 300),
             ("amber", 3, t("Проверка", "Verify"), t("тесты запускаются", "tests run"), 300, 495),
             ("green", 4, t("Ревью", "Review"), t("вы читаете изменения", "you read the changes"), 105, 300)]
    circles = "".join(
        f'<div style="position:absolute;left:{x - 98}px;top:{y - 98}px;width:196px;height:196px;border-radius:50%;border:4px solid var(--{k});background:var(--surface-card);'
        f'display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 18px">'
        f'<div style="width:38px;height:38px;border-radius:50%;background:var(--{k});color:#0b0f17;font:800 21px/38px var(--body)">{n}</div>'
        f'<div style="font:800 30px/1.1 var(--display);color:var(--{k});margin-top:6px">{h}</div>'
        f'<div style="font:500 18px/1.25 var(--body);color:var(--muted);margin-top:4px">{d}</div></div>' for k, n, h, d, x, y in nodes)
    arcs = "".join(f'<path d="{d}" fill="none" stroke="#64748b" stroke-width="4" marker-end="url(#ah)"/>' for d in
                   ("M 405 150 Q 470 160 480 195", "M 470 405 Q 460 465 405 480", "M 195 480 Q 135 465 125 405", "M 130 195 Q 140 140 195 120"))
    svg = (f'<svg width="600" height="600" style="position:absolute;left:0;top:0"><defs><marker id="ah" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto">'
           f'<path d="M0,0 L10,5 L0,10 z" fill="#64748b"/></marker></defs>{arcs}</svg>')
    centre = (f'<div style="position:absolute;left:220px;top:250px;width:160px;text-align:center;font:800 26px/1.2 var(--display);color:var(--green)">'
              f'{t("вы у руля", "you steer")}</div>')
    return f'<div style="position:relative;width:600px;height:600px;margin:0 auto">{svg}{circles}{centre}</div>'


def anatomy_diagram():
    """Coding-agent anatomy drawn in HTML (bilingual, large text)."""
    box = lambda txt: (f'<div style="border:2px solid var(--violet);border-radius:12px;padding:22px 10px;text-align:center;font:600 26px/1.25 var(--body);color:var(--fg);background:var(--surface-card)">{txt}</div>')
    inner = (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">{box(t("читает файлы", "reads files"))}{box(t("правит файлы", "edits files"))}'
             f'<div style="grid-column:1/3;justify-self:center;border:3px solid var(--cyan);border-radius:50px;padding:14px 40px;font:800 30px var(--display);color:var(--cyan)">{t("модель", "model")}</div>'
             f'{box(t("запускает команды", "runs commands"))}{box(t("инструменты (MCP)", "tools (MCP)"))}</div>')
    side = lambda k, h, d: (f'<div style="border:2px solid var(--{k});border-radius:14px;padding:18px 18px;background:var(--surface-card)">'
                            f'<div style="font:700 26px/1.25 var(--body);color:var(--{k})">{h}</div><div style="font:400 21px/1.35 var(--body);color:var(--muted);margin-top:6px">{d}</div></div>')
    arrow = '<div style="font-size:40px;color:var(--muted);text-align:center">→</div>'
    back = '<div style="font-size:40px;color:var(--muted);text-align:center">←</div>'
    return (f'<div style="display:grid;grid-template-columns:260px 50px 1fr 50px 250px;align-items:center;gap:4px">'
            f'{side("amber", "AGENTS.md / CLAUDE.md", t("правила проекта", "project rules"))}{arrow}'
            f'<div style="border:3px solid var(--violet);border-radius:18px;padding:18px 22px">'
            f'<div style="font:800 30px var(--display);color:var(--violet);text-align:center;margin-bottom:18px">{t("Агент для кода", "Coding agent")}</div>{inner}</div>'
            f'{back}{side("green", t("Разрешения", "Permissions"), "plan / manual / auto")}</div>')


def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg"><img src="{IMG}cover_terminal.png" alt="" style="position:absolute;right:110px;top:150px;width:560px;height:600px;object-fit:contain"></div>
  <div class="shade"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 16 • Модуль 6: от идеи к продукту", "GenAI Basics • Lesson 16 • Module 6: idea to product")}</div>
    <h1>{t("Агентная разработка", "Agentic software development")}</h1>
    <h2>{t("Агент пишет код — вы ставите задачу, проверяете и решаете", "The agent writes the code — you set the task, check it and decide")}</h2>
    <p>{t("Как устроен агент для кода, сколько стоят инструменты, режимы разрешений, правила проекта, реальные инциденты и безопасная практика. Данные на 16.10.2026.",
           "How a coding agent works, what the tools cost, permission modes, project rules, real incidents and safe practice. Data as of 16.10.2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Последний урок курса. Мы прошли путь от промпта в чате до своих ассистентов и прототипов. Сегодня — агенты, которые сами пишут и запускают код в вашем проекте. Главная мысль урока: агент делает работу, но задачу, проверку и решение о слиянии оставляем человеку.",
                      "⏱ 2 min. The last lesson of the course. We went from a prompt in a chat to our own assistants and prototypes. Today: agents that write and run code in your project themselves. The main idea: the agent does the work, but the task, the check and the merge decision stay with a human.")))


def s_hook():
    chat = [("amber", t("Вы спрашиваете", "You ask"), t("описываете, что нужно", "describe what you need")),
            ("amber", t("Копируете код", "You copy code"), t("из ответа в свой файл", "from the answer into your file")),
            ("amber", t("Запускаете сами", "You run it"), t("и смотрите, что сломалось", "and see what broke")),
            ("red", t("Несёте ошибку назад", "You carry the error back"), t("и так по кругу", "and round you go"))]
    agent = [("cyan", t("Вы ставите задачу", "You set the task"), t("цель и «готово, когда…»", "goal and “done when…”")),
             ("violet", t("Агент правит файлы", "The agent edits files"), t("сам читает проект", "reads the project itself")),
             ("violet", t("Агент запускает тесты", "The agent runs tests"), t("и исправляет ошибки", "and fixes the errors")),
             ("green", t("Вы проверяете", "You review"), t("читаете изменения и решаете", "read the changes and decide"))]
    return dict(min=3, html=f'''
  {head(t("Что изменилось", "What changed"), t("Чат даёт код, который вы переносите сами; агент сам правит проект и запускает проверки", "A chat gives you code to carry over; an agent edits the project and runs the checks itself"), k="cyan")}
  <div class="body" style="margin-top:8px;">
    <div style="font:700 24px var(--mono);color:var(--amber);margin:10px 0 14px">{t("ЧАТ", "CHAT")}</div>
    {flow(chat, h=215, fs=28, ds=22)}
    <div style="font:700 24px var(--mono);color:var(--violet);margin:44px 0 14px">{t("АГЕНТ ДЛЯ КОДА", "CODING AGENT")}</div>
    {flow(agent, h=215, fs=28, ds=22)}
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. В чате мы просим код, копируем его, запускаем сами и приносим ошибку обратно. Агент для кода работает прямо в папке проекта: читает файлы, вносит правки, запускает команды и тесты, сам исправляет то, что упало. Нам остаются две вещи: хорошо поставить задачу и проверить результат.",
                      "⏱ 3 min. In a chat we ask for code, copy it, run it ourselves and bring the error back. A coding agent works right in the project folder: it reads files, makes edits, runs commands and tests, and fixes what failed. Two things are left to us: setting the task well and checking the result."),
                    t("По опросу Stack Overflow 2026 помощники и агенты для кода — самый частый сценарий использования ИИ у разработчиков: 66%. Это уже не экзотика, а обычный рабочий инструмент.",
                      "In the Stack Overflow 2026 survey, coding assistants and agents are the most common AI use case among developers: 66%. This is no longer exotic but an ordinary work tool.")))


def s_anatomy():
    return dict(min=6, html=f'''
  {head(t("Устройство", "Anatomy"), t("Агент для кода — это модель с руками: читает, правит, запускает и подключает инструменты", "A coding agent is a model with hands: it reads, edits, runs and connects tools"), k="violet")}
  <div class="body" style="margin-top:8px;">
    {anatomy_diagram()}
    <div class="row" style="grid-template-columns:1fr 1fr 1fr;gap:30px;margin-top:56px;flex:none;">
        <div class="note" style="--k:var(--cyan)">{t("<b>Модель</b> — та же, что в чате: Claude, GPT, Gemini.", "<b>The model</b> is the same as in a chat: Claude, GPT, Gemini.")}</div>
        <div class="note" style="--k:var(--violet)">{t("<b>Инструменты</b> — руки агента: файлы, терминал, подключения MCP (L12).", "<b>Tools</b> are the agent’s hands: files, terminal, MCP connections (L12).")}</div>
        <div class="note" style="--k:var(--green)">{t("<b>Правила проекта и разрешения</b> — ваш руль.", "<b>Project rules and permissions</b> are your steering wheel.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Внутри агента та же модель, что в чате. Разница — в инструментах: агент умеет читать файлы, редактировать их, запускать команды в терминале и подключаться к внешним системам через MCP, о котором мы говорили в L12. Слева на схеме — файл правил проекта, AGENTS.md или CLAUDE.md: агент читает его в начале каждой сессии. Справа — разрешения: что агент может делать сам, а на что спрашивает вас.",
                      "⏱ 6 min. Inside the agent is the same model as in a chat. The difference is the tools: the agent can read files, edit them, run commands in the terminal and connect to outside systems via MCP, which we covered in L12. On the left of the diagram is the project rules file, AGENTS.md or CLAUDE.md: the agent reads it at the start of every session. On the right are permissions: what the agent may do on its own and what it asks you about."),
                    t("Ещё два слова, которые вы услышите. Навык (skill) — папка с файлом SKILL.md, где записан готовый порядок действий, например «как у нас делают релиз». Субагент — помощник со своим контекстом, например второй агент, который проверяет работу первого свежим взглядом.",
                      "Two more words you will hear. A skill is a folder with a SKILL.md file describing a ready-made procedure, for example “how we do a release”. A subagent is a helper with its own context, for example a second agent that reviews the first one’s work with fresh eyes.")))


def _band(k, price, who, tools):
    chips = "".join(f'<div style="font:600 24px/1.3 var(--body);color:var(--fg);padding:13px 0;border-bottom:1px solid var(--line)">{a}<span style="color:var(--muted);font-weight:400"> · {b}</span></div>' for a, b in tools)
    return (f'<div style="background:var(--surface-card);border:1px solid var(--line);border-top:5px solid var(--{k});border-radius:14px;padding:20px 24px">'
            f'<div style="font:800 58px/1 var(--display);color:var(--{k})">{price}</div>'
            f'<div style="font:600 22px var(--body);color:var(--muted);margin:10px 0 12px">{who}</div>{chips}</div>')


def s_landscape():
    b0 = [("GitHub Copilot Free", t("ограниченный агент", "limited agent")), ("Codex", t("в ChatGPT Free", "in ChatGPT Free")),
          ("Google Antigravity", t("базовые лимиты", "basic limits")), ("Cursor · Kiro · Junie", t("бесплатные тарифы", "free tiers"))]
    b1 = [("Copilot Pro", "$10"), ("Claude Code", t("в Claude Pro, $20", "in Claude Pro, $20")),
          ("Codex", t("в ChatGPT Plus, $20", "in ChatGPT Plus, $20")), ("Devin · Kiro · Cursor", "$20–30")]
    b2 = [("Claude Max", "$100 / $200"), ("ChatGPT Pro", t("от $100", "from $100")),
          ("Copilot Max", "$100"), ("Cursor · Devin", "$100–200")]
    return dict(min=6, html=f'''
  {head(t("Инструменты", "Tools"), t("Попробовать можно бесплатно; для каждого дня — $10–30; для тяжёлой работы — от $100", "You can try for free; daily use is $10–30; heavy use starts at $100"), k="amber")}
  <div class="body" style="margin-top:8px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px;">
      {_band("cyan", "$0", t("попробовать", "to try it"), b0)}
      {_band("amber", "$10–30", t("каждый день", "every day"), b1)}
      {_band("red", t("от $100", "$100+"), t("много агентов, большие задачи", "many agents, big tasks"), b2)}
    </div>
    <div class="plaque" style="margin-top:34px">{t("<b>Начните с бесплатного:</b> Codex в ChatGPT, Copilot Free или Antigravity. Цены на 16.10.2026, в месяц; у Claude Code бесплатного тарифа нет.", "<b>Start free:</b> Codex in ChatGPT, Copilot Free or Antigravity. Prices as of 16.10.2026, per month; Claude Code has no free tier.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Рынок меняется каждый месяц, поэтому запоминайте не цены, а три ценовые полосы. Бесплатно: GitHub Copilot Free с ограниченным агентом, Codex теперь есть даже в бесплатном ChatGPT — для коротких задач, Google Antigravity с базовыми лимитами, бесплатные тарифы Cursor, Kiro от Amazon и Junie от JetBrains. Около 20 долларов: Copilot Pro за 10, Claude Code в подписке Claude Pro, Codex в ChatGPT Plus, Devin и Kiro по 20, Cursor Premium за 30.",
                      "⏱ 6 min. The market changes every month, so remember three price bands, not prices. Free: GitHub Copilot Free with a limited agent, Codex now even in free ChatGPT, for quick tasks, Google Antigravity with basic limits, and free tiers of Cursor, Amazon’s Kiro and JetBrains’ Junie. About 20 dollars: Copilot Pro at 10, Claude Code in the Claude Pro subscription, Codex in ChatGPT Plus, Devin and Kiro at 20, Cursor Premium at 30."),
                    t("От 100 долларов — для тех, кто держит несколько агентов одновременно: Claude Max, ChatGPT Pro, Copilot Max, старшие тарифы Cursor и Devin. За 2026 год многое переименовали: Windsurf стал Devin Desktop, бесплатный Gemini CLI заменили на Antigravity CLI, агент Copilot теперь называется cloud agent. У Claude Code бесплатного тарифа нет. Перед покупкой проверьте актуальную цену на сайте.",
                      "From 100 dollars is for people who run several agents at once: Claude Max, ChatGPT Pro, Copilot Max, the top Cursor and Devin plans. A lot was renamed in 2026: Windsurf became Devin Desktop, free Gemini CLI users were moved to the Antigravity CLI, and Copilot’s agent is now called the cloud agent. Claude Code has no free tier. Check the current price on the site before buying.")))


def s_loop():
    return dict(min=6, html=f'''
  {head(t("Цикл работы", "The work loop"), t("План → действие → проверка → ревью: агент крутит цикл, вы держите руль", "Plan → act → verify → review: the agent turns the loop, you steer"), k="cyan")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:600px 1fr;gap:50px;align-items:center;flex:none;margin-top:10px">
      {loop_diagram()}
      <div class="stack" style="gap:18px;">
        {legend([(1, "cyan", t("<b>План:</b> агент читает проект и предлагает план; правок пока нет", "<b>Plan:</b> the agent reads the project and proposes a plan; no edits yet")),
                 (2, "violet", t("<b>Действие:</b> правки в отдельной ветке — копии проекта, которую можно выбросить", "<b>Act:</b> edits on a separate branch — a copy of the project you can throw away")),
                 (3, "amber", t("<b>Проверка:</b> тесты, сборка, скриншот", "<b>Verify:</b> tests, build, screenshot")),
                 (4, "green", t("<b>Ревью:</b> вы читаете изменения — diff, «было → стало» — и решаете", "<b>Review:</b> you read the changes — the diff, “before → after” — and decide"))])}
        <div class="note" style="--k:var(--muted)">{t("Anthropic: «сначала изучить, потом план, потом код».", "Anthropic: “explore first, then plan, then code”.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Это главный слайд урока. Работа с агентом — цикл из четырёх шагов. План: в режиме плана агент только читает проект и предлагает, что сделает; править файлы он не может, пока вы не одобрите. Действие: агент вносит правки, лучше в отдельной ветке git. Проверка: агент запускает тесты или сборку и сам исправляет то, что упало.",
                      "⏱ 6 min. This is the key slide of the lesson. Working with an agent is a loop of four steps. Plan: in plan mode the agent only reads the project and proposes what it will do; it cannot edit files until you approve. Act: the agent makes edits, preferably on a separate git branch. Verify: the agent runs tests or a build and fixes what failed."),
                    t("Ревью: вы читаете изменения — diff, то есть список «было — стало» — и решаете, принять или нет. Документация Claude Code советует ровно этот порядок: изучить, спланировать, написать код, закоммитить. План можно пропустить, только если изменение описывается одной фразой.",
                      "Review: you read the changes — the diff, a before-and-after list — and decide whether to accept. The Claude Code docs recommend exactly this order: explore, plan, code, commit. You may skip the plan only if the change fits in one sentence.")))


def s_task():
    bad = t("Добавь фильтр по приоритету.", "Add a priority filter.")
    good = t('<span class="cm"># TASK.md</span>\n<span class="kw">Цель:</span> фильтр тикетов по приоритету\n       на странице /tickets\n<span class="kw">Не трогать:</span> базу данных, вход\n<span class="kw">Готово, когда:</span> тест filter\n       проходит, старые тесты тоже\n<span class="kw">Проверка:</span> <span class="str">pytest -q</span>\n<span class="kw">Ревью:</span> человек читает diff',
             '<span class="cm"># TASK.md</span>\n<span class="kw">Goal:</span> filter tickets by priority\n      on the /tickets page\n<span class="kw">Do not touch:</span> database, login\n<span class="kw">Done when:</span> the filter test\n      passes, old tests too\n<span class="kw">Check:</span> <span class="str">pytest -q</span>\n<span class="kw">Review:</span> a human reads the diff')
    return dict(min=6, html=f'''
  {head(t("Задача", "The task"), t("Хорошая задача агенту говорит, что сделать, чего не трогать и как проверить «готово»", "A good agent task says what to do, what not to touch and how to check it is done"), k="green")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1fr 70px 1.35fr;gap:18px;align-items:start;flex:none;">
      <div class="stack" style="gap:14px">
        <div style="font:700 24px var(--mono);color:var(--red)">{t("РАСПЛЫВЧАТО", "VAGUE")}</div>
        <pre class="code" style="font-size:29px;border-color:var(--red);padding:34px 24px">{bad}</pre>
        <div class="note" style="--k:var(--red)">{t("Агент сам решит, где фильтр, что менять и когда остановиться.", "The agent decides where the filter goes, what to change and when to stop.")}</div>
      </div>
      <div style="font-size:56px;color:var(--muted);text-align:center;margin-top:60px">→</div>
      <div class="stack" style="gap:14px">
        <div style="font:700 24px var(--mono);color:var(--green)">{t("ЗАДАЧА ДЛЯ АГЕНТА", "AGENT TASK")}</div>
        <pre class="code" style="font-size:30px;line-height:1.6;border-color:var(--green)">{good}</pre>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Самая частая ошибка новичка — расплывчатая просьба. «Добавь фильтр» агент выполнит, но сам решит, где он будет, что ещё поменять по дороге и когда остановиться. Справа та же просьба как задача: цель, что не трогать, когда считается готово, какой командой проверить и кто принимает решение.",
                      "⏱ 6 min. The most common beginner mistake is a vague request. The agent will carry out “add a filter”, but it will decide where it goes, what else to change on the way and when to stop. On the right is the same request as a task: the goal, what not to touch, when it counts as done, which command checks it and who makes the decision."),
                    t("Строка «Готово, когда» — самая важная. Если агент может сам запустить проверку, он будет исправлять ошибки, пока проверка не пройдёт. Совет из документации: маленькие задачи, конкретные файлы, команда /clear между задачами; после двух неудачных исправлений лучше начать заново с уточнённой задачей. pytest -q — команда, которая запускает все тесты; тест — маленькая программа, проверяющая, что код делает нужное.",
                      "The “Done when” line is the most important one. If the agent can run the check itself, it will keep fixing errors until the check passes. Advice from the docs: small tasks, specific files, /clear between tasks; after two failed corrections it is better to start over with a clearer task. pytest -q is the command that runs all tests; a test is a small program that checks the code does what it should.")))


def s_rules_file():
    code = t('<span class="cm"># AGENTS.md</span>\n<span class="kw">## Команды</span>\n- тесты: <span class="str">pytest -q</span>\n- запуск: <span class="str">streamlit run app.py</span>\n<span class="kw">## Правила</span>\n- код в src/, тесты в tests/\n- не трогать .env и deploy/\n- новые библиотеки — только\n  после вопроса',
             '<span class="cm"># AGENTS.md</span>\n<span class="kw">## Commands</span>\n- tests: <span class="str">pytest -q</span>\n- run: <span class="str">streamlit run app.py</span>\n<span class="kw">## Rules</span>\n- code in src/, tests in tests/\n- do not touch .env or deploy/\n- new libraries only\n  after asking')
    return dict(min=5, html=f'''
  {head(t("Правила проекта", "Project rules"), t("AGENTS.md — короткая памятка проекта, которую агент читает в начале каждой сессии", "AGENTS.md is a short project memo the agent reads at the start of every session"), k="violet")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:44px;align-items:center;flex:none;">
      <pre class="code" style="font-size:33px;line-height:1.7;padding:32px 36px">{code}</pre>
      <div class="stack" style="gap:30px;">
        <div class="stat" style="--k:var(--violet)"><div class="n" style="font-size:72px">{t("60 000+", "60,000+")}</div><div class="d">{t("open-source проектов уже используют AGENTS.md — открытый формат", "open-source projects already use AGENTS.md, an open format")}</div></div>
        <div class="note" style="--k:var(--cyan)">{t("<b>Читают:</b> Codex, Copilot, Cursor, Devin, Junie, Antigravity. Claude Code читает CLAUDE.md, а без него — AGENTS.md.", "<b>Read by:</b> Codex, Copilot, Cursor, Devin, Junie, Antigravity. Claude Code reads CLAUDE.md, or AGENTS.md if there is none.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Коротко и конкретно: команды и запреты, а не эссе.", "Short and concrete: commands and limits, not an essay.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Каждый новый разговор агент начинает с чистого листа. Чтобы не объяснять проект заново, кладём в корень файл AGENTS.md: какими командами запускать тесты и приложение, где лежит код, чего не трогать. Это открытый формат, его используют больше 60 тысяч open-source проектов, и его читают почти все агенты. Claude Code читает свой CLAUDE.md, а если его нет — AGENTS.md. Команда /init создаёт черновик такого файла: в Claude Code — CLAUDE.md, в Codex — AGENTS.md.",
                      "⏱ 5 min. Every new conversation starts from a blank page for the agent. So as not to explain the project again, we put an AGENTS.md file in the root: which commands run the tests and the app, where the code lives, what not to touch. It is an open format used by over 60 thousand open-source projects, and almost every agent reads it. Claude Code reads its own CLAUDE.md, or AGENTS.md if there is none. The /init command drafts such a file: CLAUDE.md in Claude Code, AGENTS.md in Codex."),
                    t("Важно: этот файл — совет, а не замок. Агент может его нарушить. То, что должно выполняться всегда, делают хуки — скрипты, которые запускаются автоматически, например форматирование после каждой правки или запрет записи в папку. И наоборот: AGENTS.md из чужого репозитория — это чужой текст, который командует вашим агентом; читайте его как непроверенный код.",
                      "Important: this file is advice, not a lock. The agent can break it. What must always happen is done with hooks — scripts that run automatically, for example formatting after every edit or blocking writes to a folder. And the other way round: an AGENTS.md from someone else’s repository is someone else’s text commanding your agent; read it like unverified code.")))


def s_permissions():
    modes = [("green", "plan", t("только читает и планирует", "reads and plans only")),
             ("cyan", "manual", t("спрашивает перед правкой и командой", "asks before edits and commands")),
             ("amber", "acceptEdits", t("правит файлы и простые файловые команды сам; остальные команды — с вопросом", "edits files and runs simple file commands itself; asks for other commands")),
             ("violet", "auto", t("команды проверяет модель-проверяющий · по умолчанию в терминале", "a checker model reviews commands · default in the terminal")),
             ("red", "bypass", t("без проверок — только в одноразовом контейнере", "no checks — throwaway container only"))]
    scale = "".join(f'<div style="border-top:6px solid var(--{k});padding-top:12px"><div style="font:700 27px var(--mono);color:var(--{k})">{n}</div>'
                    f'<div style="font:400 21px/1.35 var(--body);color:var(--muted);margin-top:8px">{d}</div></div>' for k, n, d in modes)
    return dict(min=6, html=f'''
  {head(t("Разрешения", "Permissions"), t("Режим разрешений решает, что агент делает сам, а что — только с вашего согласия", "The permission mode decides what the agent does on its own and what needs your OK"), k="amber")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;align-items:flex-start"><div class="prompt-label" style="align-self:stretch">{t("claude.ai/code → меню разрешений · снято 16.10.2026", "claude.ai/code → permissions menu · captured 16.10.2026")}</div>
        {shot("claude_code_permissions_menu", marks=[(1, 87.0, 21.5, "amber")], boxes=[(2.0, 17.5, 96.0, 26.0, "amber")], style="border-radius:14px;width:540px")}
        <div class="shotcap" style="font-size:20px;align-self:stretch">{t("<b>①</b> Auto — режим по умолчанию (с октября 2026).", "<b>①</b> Auto is the default mode (since October 2026).")}</div></div>
      <div class="stack" style="gap:22px;">
        <div class="stat" style="--k:var(--amber)"><div class="n" style="font-size:64px">93%</div><div class="d">{t("запросов на разрешение люди просто одобряют — устают читать", "of permission prompts people simply approve — they get tired of reading")}</div></div>
        <div class="stat" style="--k:var(--red)"><div class="n" style="font-size:64px">~17%</div><div class="d">{t("рискованных действий автопроверка всё равно пропускает (тест Anthropic)", "of risky actions the auto check still misses (Anthropic’s test)")}</div></div>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:22px;margin-top:30px">{scale}</div>
    <div style="display:flex;justify-content:space-between;font:600 18px var(--mono);color:var(--muted);margin-top:10px"><span>{t("← безопаснее", "← safer")}</span><span>{t("быстрее, рискованнее →", "faster, riskier →")}</span></div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Слева — реальное меню разрешений Claude Code (claude.ai/code, 16.10.2026): Auto, Accept edits, Plan, и Auto отмечен по умолчанию. В октябре 2026 Claude Code сообщил: режим auto стал режимом по умолчанию в терминале и VS Code. В нём чтение и правки файлов в папке проекта идут сразу, а команды и обращения в сеть сначала проверяет отдельная модель: безопасное выполняется, рискованное блокируется. Внизу — шкала режимов. Plan: агент читает файлы и запускает команды только чтобы изучить проект, пишет план и ничего не правит. Manual: агент спрашивает перед каждой правкой и командой. AcceptEdits: сам правит файлы и выполняет простые файловые команды в папке проекта — создать папку, переместить, скопировать или удалить файл (mkdir, mv, cp, rm); на остальные команды спрашивает. Auto: решает модель-проверяющий. Bypass: никаких проверок, только в одноразовом контейнере или виртуальной машине. Одноразовый контейнер — временный изолированный «компьютер в компьютере», который удаляют после работы.",
                      "⏱ 6 min. On the left is the real Claude Code permissions menu (claude.ai/code, 16.10.2026): Auto, Accept edits, Plan, with Auto ticked by default. In October 2026 Claude Code announced that auto mode became the default in the terminal and VS Code. In it, reading and editing files in the project folder just happens, while commands and network access are first checked by a separate model: safe ones run, risky ones are blocked. Below is the scale of modes. Plan: the agent reads files and runs commands only to explore the project, writes a plan and edits nothing. Manual: the agent asks before every edit and command. AcceptEdits: it edits files and runs simple file commands in the project folder itself — make a folder, move, copy or delete a file (mkdir, mv, cp, rm); it asks before other commands. Auto: a checker model decides. Bypass: no checks at all, only in a throwaway container or virtual machine. A throwaway container is a temporary isolated “computer inside your computer” that you delete afterwards."),
                    t("Почему появился auto? Anthropic посчитала: люди одобряют 93% запросов — после десятого вопроса никто не читает. Но и автопроверка не идеальна: около 17% лишних рискованных действий она пропускает. Поэтому режим не заменяет ревью. У Codex то же самое называется иначе: песочница read-only, workspace-write и danger-full-access. Правила-запреты, например на rm -rf или git push, действуют в любом режиме.",
                      "Why auto? Anthropic counted that people approve 93% of prompts — after the tenth question nobody reads. But the auto check is not perfect either: it misses about 17% of overeager risky actions. So the mode does not replace review. Codex has the same idea under other names: read-only, workspace-write and danger-full-access sandboxes. Deny rules, for example on rm -rf or git push, apply in every mode.")))


def s_verify():
    red = lambda x: f'<span style="color:var(--red)">{x}</span>'
    grn = lambda x: f'<span style="color:var(--green)">{x}</span>'
    # Real output of the L16 homework starter (pytest 9.1.1, Python 3.12), run 2026-10-16;
    # the failure traceback is cut, the summary lines are verbatim.
    term = ('<span class="cm">$</span> pytest -q\n'
            f'..{red("F")}                               [100%]\n'
            f'{red("FAILED")} tests/test_filter.py::\n'
            '  test_filter_by_priority - TypeError: ...\n'
            f'{red("1 failed")}, {grn("2 passed")} in 0.06s\n'
            f'<span class="cm">{t("# агент правит app.py: добавляет priority", "# the agent edits app.py: adds priority")}</span>\n'
            '<span class="cm">$</span> pytest -q\n'
            f'{grn("...")}                               [100%]\n'
            f'{grn("3 passed")} in 0.02s')
    return dict(min=5, html=f'''
  {head(t("Проверка", "Verify"), t("«Нельзя проверить — не выпускайте»: дайте агенту проверку, которую он запустит сам", "“If you can’t verify it, don’t ship it”: give the agent a check it can run itself"), k="green")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.15fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="stack" style="gap:10px">
        <pre class="code" style="font-size:23px;line-height:1.5;padding:22px 28px">{term}</pre>
        <div style="font:400 17px var(--body);color:var(--muted)">{t("Настоящий вывод на стартовом проекте из ДЗ (ошибка сокращена).", "Real output on the homework starter project (the error is shortened).")}</div>
      </div>
      <div class="stack" style="gap:22px;">
        {legend([(1, "red", t("<b>Тест падает:</b> сначала пишем проверку того, что нужно", "<b>A test fails:</b> first write a check for what you need")),
                 (2, "violet", t("<b>Агент чинит:</b> правит код, пока тест не пройдёт", "<b>The agent fixes:</b> edits the code until the test passes")),
                 (3, "amber", t("<b>Все тесты прошли:</b> и новый, и старые", "<b>All tests pass:</b> the new one and the old ones")),
                 (4, "green", t("<b>Вы читаете diff:</b> тест видит не всё — смысл, стиль, лишнее", "<b>You read the diff:</b> tests don’t see everything — meaning, style, extras"))])}
      </div>
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;margin-top:30px;flex:none;">
      <div class="note" style="--k:var(--amber)">{t("<b>Откат в агенте</b> (Esc Esc, /rewind) отменяет правки файлов, но не команды в терминале.", "<b>The agent’s undo</b> (Esc Esc, /rewind) reverts file edits, but not terminal commands.")}</div>
      <div class="note" style="--k:var(--green)">{t("<b>Настоящая кнопка «отменить» — git:</b> каждая задача в отдельной ветке.", "<b>The real undo button is git:</b> each task on its own branch.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Фраза из документации Claude Code: если вы не можете это проверить, не выпускайте. Самый надёжный приём — сначала тест, который падает, потом исправление. Слева — настоящий запуск на стартовом проекте из ДЗ: новый тест на фильтр по приоритету падает, два старых проходят; агент правит app.py, и все три теста зелёные. Агент запускает тест сам и правит код, пока всё не станет зелёным. Если тестов нет, проверкой может быть сборка, линтер или скриншот страницы. Но тест не видит всего, поэтому последний шаг — вы читаете diff.",
                      "⏱ 5 min. A line from the Claude Code docs: if you can’t verify it, don’t ship it. The most reliable approach is a failing test first, then the fix. On the left is a real run on the homework starter project: the new priority-filter test fails, the two old ones pass; the agent edits app.py and all three tests are green. The agent runs the test itself and edits the code until everything is green. If there are no tests, the check can be a build, a linter or a screenshot of the page. But a test does not see everything, so the last step is you reading the diff."),
                    t("Про откат. В агентах есть свои кнопки «назад», в Claude Code это Esc Esc или /rewind. Они откатывают правки файлов, но не то, что агент сделал командами в терминале: удалённую базу так не вернуть. Настоящая страховка — git: каждая задача в своей ветке или в отдельной рабочей копии (worktree), чтобы параллельные агенты не мешали друг другу.",
                      "On undo. Agents have their own back buttons; in Claude Code it is Esc Esc or /rewind. They revert file edits, but not what the agent did with terminal commands: a deleted database does not come back that way. The real safety net is git: every task on its own branch or in a separate working copy (worktree), so parallel agents do not get in each other’s way.")))


def _div(rows):
    """Diverging bars around zero: rows = (label, value %, colour)."""
    out = ""
    for lab, v, k in rows:
        w = abs(v) * 1.6
        bar = (f'<div style="position:absolute;top:8px;height:44px;border-radius:6px;background:var(--{k});'
               + (f'left:50%;width:{w}%"></div>' if v > 0 else f'right:50%;width:{w}%"></div>'))
        val = (f'<div style="position:absolute;top:10px;font:800 34px var(--display);color:var(--{k});'
               + (f'left:calc(50% + {w}% + 14px)">+{v}%</div>' if v > 0 else f'right:calc(50% + {w}% + 14px)">−{abs(v)}%</div>'))
        out += (f'<div style="display:grid;grid-template-columns:330px 1fr;align-items:center;margin-bottom:40px">'
                f'<div style="font:600 26px/1.3 var(--body);color:var(--fg)">{lab}</div>'
                f'<div style="position:relative;height:60px;border-left:0">{bar}{val}'
                f'<div style="position:absolute;left:50%;top:-6px;bottom:-6px;border-left:2px solid var(--line)"></div></div></div>')
    return out


def s_metr():
    rows = [(t("Ожидали до начала", "Expected beforehand"), 24, "cyan"),
            (t("Казалось после", "Felt afterwards"), 20, "amber"),
            (t("Измерили на деле", "Measured"), -19, "red")]
    return dict(min=7, html=f'''
  {head(t("Скорость", "Speed"), t("Опытным разработчикам казалось, что с ИИ они быстрее на 20%, — замер показал, что медленнее на 19%", "Experienced developers felt 20% faster with AI — the measurement showed 19% slower"),
         t("METR, начало 2025: 16 опытных разработчиков, 246 задач в их проектах, инструменты того времени (Cursor + Claude 3.5/3.7).", "METR, early 2025: 16 experienced developers, 246 tasks in their own projects, tools of that time (Cursor + Claude 3.5/3.7)."), k="red")}
  <div class="body" style="margin-top:8px;">
    <div style="display:grid;grid-template-columns:330px 1fr;font:600 19px var(--mono);color:var(--muted);margin:20px 0 24px"><div></div><div style="display:flex;justify-content:space-between"><span>{t("← медленнее", "← slower")}</span><span>{t("быстрее →", "faster →")}</span></div></div>
    {_div(rows)}
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;margin-top:30px;flex:none;">
      <div class="note" style="--k:var(--muted)">{t("<b>Повтор 2026:</b> вероятно, уже быстрее, но данные ненадёжны — люди отказывались работать без ИИ.", "<b>2026 follow-up:</b> probably faster now, but the data is weak — people refused to work without AI.")}</div>
      <div class="note" style="--k:var(--green)">{t("<b>Вывод:</b> ощущение скорости ≠ скорость. Замеряйте на своих задачах.", "<b>Takeaway:</b> feeling fast ≠ being fast. Measure on your own tasks.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. Самое честное исследование на эту тему. Организация METR в 2025 году взяла 16 опытных разработчиков open-source и 246 реальных задач из их же проектов. Каждую задачу случайно отнесли в одну из групп: с ИИ можно или нельзя. До начала участники ожидали ускорения на 24%, после — были уверены, что стали быстрее на 20%. Замер показал: с ИИ они работали на 19% медленнее.",
                      "⏱ 7 min. The most honest study on this topic. In 2025 the METR organisation took 16 experienced open-source developers and 246 real tasks from their own projects. Each task was randomly assigned: AI allowed or not allowed. Before starting, participants expected a 24% speedup; afterwards they were sure they had been 20% faster. The measurement showed they were 19% slower with AI."),
                    t("В феврале 2026 METR повторила исследование с новыми инструментами: оценки сдвинулись в сторону ускорения, но статистически ничего не доказано — разработчики уже отказывались работать без ИИ, и данные стали ненадёжными. Ещё одна цифра, из другого опроса — Stack Overflow 2025: 66% разработчиков больше всего раздражает код, который «почти правильный, но не совсем». Вывод для вас: не верьте ощущению, засеките время на своих задачах. То же с рейтингами агентов вроде SWE-bench: цифры из анонсов быстро устаревают и зависят от программы-агента вокруг модели, так что проверяйте на своей задаче.",
                      "In February 2026 METR repeated the study with newer tools: estimates moved towards a speedup, but nothing is statistically proven — developers were already refusing to work without AI, and the data became unreliable. One more figure, from a different survey — Stack Overflow 2025: 66% of developers said their top frustration is code that is “almost right, but not quite”. The takeaway for you: don’t trust the feeling; time yourself on your own tasks. The same goes for agent benchmarks such as SWE-bench: numbers from announcements age fast and depend on the agent app around the model, so test on your own task.")))




def s_incidents():
    tiles = [("red", t("9 секунд", "9 seconds"), t("PocketOS, 2026: агент нашёл в постороннем файле ключ доступа и удалил базу вместе с бэкапами; по словам основателя, данные потом восстановили", "PocketOS, 2026: the agent found an access key in an unrelated file and deleted the database with its backups; per the founder, data was later restored")),
             ("amber", t("«Заморозка»", "Code freeze"), t("Replit, 2025: агент удалил рабочую базу SaaStr, хотя изменения были запрещены", "Replit, 2025: the agent deleted SaaStr’s live database although changes were frozen")),
             ("violet", t("2 349", "2,349"), t("секретов утекло: заражённая библиотека Nx (готовый модуль, который скачивают программисты) крала ключи и заставляла установленных ИИ-агентов искать файлы с секретами, 2025", "secrets leaked: an infected Nx library (a ready-made module developers download) stole keys and made installed AI agents search for secret files, 2025"))]
    tt = "".join(f'<div class="stat" style="--k:var(--{k});flex:1;gap:12px"><div class="n" style="font-size:74px">{n}</div><div class="d" style="font-size:23px">{d}</div></div>' for k, n, d in tiles)
    return dict(min=7, html=f'''
  {head(t("Инциденты", "Incidents"), t("Агент делает то, до чего дотягивается: ключи, базы и чужой текст в проекте", "An agent does whatever it can reach: keys, databases and other people’s text in the project"), k="red")}
  <div class="body" style="margin-top:8px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px;">{tt}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;margin-top:80px;flex:none;align-items:start;">
      <div class="plaque">{t("<b>Ключ в зоне досягаемости агента = выданное агенту право.</b>", "<b>A key within the agent’s reach = a permission given to the agent.</b>")}</div>
      <div class="note" style="--k:var(--violet)">{t("<b>Clinejection, 2026:</b> команда в заголовке задачи на GitHub → ИИ-бот проекта выполнил её → украдены ключи публикации → вышла заражённая версия Cline.", "<b>Clinejection, 2026:</b> a command in a GitHub issue title → the project’s AI bot ran it → publishing keys were stolen → an infected Cline version went out.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. Три случая. PocketOS, апрель 2026: агент в Cursor нашёл в постороннем файле долгоживущий ключ к облаку и одной командой за девять секунд удалил рабочую базу вместе с резервными копиями; сервис лежал около 30 часов, потом данные восстановили. Replit, июль 2025: во время объявленной «заморозки» агент удалил рабочую базу SaaStr — около 1200 руководителей и 1190 компаний — и сначала сообщил, что откат невозможен.",
                      "⏱ 7 min. Three cases. PocketOS, April 2026: an agent in Cursor found a long-lived cloud key in an unrelated file and, with a single command, deleted the production database and its backups in nine seconds; the service was down for about 30 hours, and the data was later restored. Replit, July 2025: during a declared code freeze the agent deleted SaaStr’s production database — about 1,200 executives and 1,190 companies — and at first reported that a rollback was impossible."),
                    t("Nx, август 2025 — атака через цепочку поставок: заражённая версия популярного npm-пакета при установке искала на компьютере ИИ-агентов — Claude, Gemini, Amazon Q — и просила их найти файлы с секретами, отключив вопросы о разрешениях; многие агенты отказались, но ключи вирус крал и сам. Утекло около 2349 секретов. А в 2026 году в случае Clinejection команда была спрятана прямо в заголовке задачи на GitHub: ИИ-бот, который разбирал задачи проекта Cline, выполнил её, злоумышленник добрался до ключей публикации, и в npm вышла заражённая версия. Вывод: всё, до чего агент дотягивается, — это его права, а чужой текст в проекте — это чужие команды.",
                      "Nx, August 2025, a supply-chain attack: an infected version of a popular npm package, on install, looked for AI agents on the computer — Claude, Gemini, Amazon Q — and asked them to find secret files with permission prompts switched off; many agents refused, but the malware stole keys on its own too. About 2,349 secrets leaked. And in 2026, in the Clinejection case, the command was hidden right in a GitHub issue title: the AI bot that triaged Cline’s issues ran it, the attacker got to the publishing keys, and an infected version went out on npm. The takeaway: everything the agent can reach is its permission, and someone else’s text in the project is someone else’s commands.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут: какую маленькую задачу в своём проекте вы бы отдали агенту?", "5 minutes: which small task in your project would you give an agent?")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: правила безопасной работы, практика, ДЗ.", "Next: safe-work rules, practice, homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт».", "⏱ 5 min. Press “Start”.")))


def _tag(x):
    return f' <span style="font:600 18px var(--mono);color:var(--red);border:1px solid var(--red);border-radius:6px;padding:1px 8px;margin-left:8px;vertical-align:3px">{x}</span>'


def s_safe():
    rules = [(t("Отдельная ветка на каждую задачу", "A separate branch per task"), t("git — ваша кнопка «отменить»", "git is your undo button")),
             (t("Никаких рабочих ключей рядом", "No production keys nearby") + _tag("PocketOS"), t("ни в коде, ни в файлах настроек проекта", "not in the code, not in the project’s settings files")),
             (t("Песочница и минимум прав", "Sandbox and least privilege") + _tag("Replit"), t("закрытая среда; запрет на удаление и отправку кода", "a closed environment; deny deleting and pushing code")),
             (t("Чужой текст — непроверенный код", "Other people’s text is unverified code") + _tag("Nx · Clinejection"), t("README, задачи, чужие AGENTS.md, навыки, MCP", "READMEs, issues, foreign AGENTS.md, skills, MCP")),
             (t("Каждое изменение читает человек", "A human reads every change"), t("лучше — свежим взглядом или вторым агентом", "ideally with fresh eyes or a second agent")),
             (t("Слияние и выпуск — только человек", "Only a human merges and ships"), t("агент Copilot может только предложить изменения — принимает их человек", "Copilot’s agent can only propose changes; a human accepts them"))]
    ol = "".join(f'<li style="font-size:27px;color:var(--fg)"><span><b>{h}</b><br><span style="font-size:21px;color:var(--muted)">{d}</span></span></li>' for h, d in rules)
    return dict(min=7, html=f'''
  {head(t("Безопасная работа", "Safe work"), t("Шесть правил, которые сильно снижают риск таких инцидентов", "Six rules that sharply cut the risk of such incidents"), k="green")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:44px;align-items:center;flex:none;">
      <ol class="checklist" style="gap:16px">{ol}</ol>
      <div class="plaque" style="font-size:26px;padding:24px 26px">{t("<b>Режим без проверок</b> (bypass, --yolo, danger-full-access) — только в одноразовом контейнере или виртуальной машине, которую не жалко выбросить.", "<b>The no-checks mode</b> (bypass, --yolo, danger-full-access) — only in a throwaway container or virtual machine.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. Шесть правил. Первое: каждая задача — в своей ветке или worktree, тогда любой результат можно выбросить. Второе: рядом с агентом нет рабочих ключей и паролей — ни в проекте, ни в .env. Это закрывает PocketOS. Третье: песочница и минимум прав, плюс явные запреты на опасные команды. Четвёртое: README, задачи, чужие AGENTS.md, сторонние навыки и MCP-серверы — это чужой текст, который может командовать агентом; ставьте их только из доверенных источников.",
                      "⏱ 7 min. Six rules. One: each task on its own branch or worktree, so any result can be thrown away. Two: no production keys or passwords near the agent — not in the project, not in .env. That closes PocketOS. Three: a sandbox and least privilege, plus explicit denials of dangerous commands. Four: READMEs, issues, foreign AGENTS.md files, third-party skills and MCP servers are someone else’s text that can command the agent; install them only from trusted sources."),
                    t("Пятое: каждое изменение читает человек, лучше свежим взглядом — второй сессией или агентом-ревьюером. Шестое: слияние и выпуск — только человек. Так устроен облачный агент Copilot: он открывает только черновой pull request, не может его одобрить, а автор задачи не может одобрить PR своего агента. Режим без проверок — только в одноразовом контейнере. Одноразовый контейнер — временный изолированный «компьютер в компьютере», который удаляют после работы. --yolo — флаг запуска некоторых агентов командной строки, который отключает все вопросы о разрешениях; bypass в Claude Code и danger-full-access в Codex — то же самое.",
                      "Five: a human reads every change, ideally with fresh eyes — a second session or a reviewer agent. Six: only a human merges and ships. That is how Copilot’s cloud agent works: it opens only a draft pull request, cannot approve it, and the person who asked cannot approve their own agent’s PR. The no-checks mode belongs only in a throwaway container. A throwaway container is a temporary isolated “computer inside your computer” that you delete afterwards. --yolo is a start-up flag of some command-line agents that switches off all permission prompts; bypass in Claude Code and danger-full-access in Codex are the same thing.")))


def s_exercise():
    return dict(min=10, html=f'''
  {head(t("Практика", "Practice"), t("Превратите расплывчатую просьбу в задачу, которую агент выполнит и проверит", "Turn a vague request into a task an agent can carry out and check"), k="cyan")}
  <div class="body" style="margin-top:8px;">
    <div class="plaque" style="font-size:28px;margin:10px 0 40px;padding:20px 26px">{t("«Пользователи хотят фильтровать тикеты по приоритету. Добавьте, пожалуйста.»", "“Users want to filter tickets by priority. Please add it.”")}</div>
    {flow([("cyan", "TASK.md", t("цель, не трогать, готово когда, проверка", "goal, do not touch, done when, check")),
           ("violet", "AGENTS.md", t("команда тестов и запреты", "the test command and limits")),
           ("amber", t("План от агента", "The agent’s plan"), t("plan mode; прочитайте, что он предлагает", "plan mode; read what it proposes")),
           ("green", t("Решение", "Decision"), t("принять, отклонить или уточнить задачу", "accept, reject or refine the task"))], h=270, fs=31, ds=24)}
    <div class="note" style="margin-top:40px;--k:var(--muted)">{t("Нет агента под рукой — сделайте шаги 1–2, потом обменяйтесь TASK.md с соседом и проверьте его строку «готово, когда». Бесплатно попробовать: Codex в ChatGPT, Copilot Free, Antigravity.", "No agent at hand — do steps 1–2, then swap TASK.md with a neighbour and check their “done when” line. Free to try: Codex in ChatGPT, Copilot Free, Antigravity.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 10 мин. Работаем индивидуально, 7 минут, потом 3 минуты разбор. Просьба от бизнеса: «пользователи хотят фильтровать тикеты по приоритету». Шаг 1: напишите TASK.md — цель, что не трогать, когда готово, какой командой проверить. Шаг 2: AGENTS.md на три-пять строк — команда тестов и запреты. Шаг 3: если у вас есть агент, запустите его в режиме плана и прочитайте план, ничего не одобряя. Шаг 4: решите, принять план, отклонить или уточнить задачу.",
                      "⏱ 10 min. Work individually for 7 minutes, then a 3-minute walk-through. A business request: “users want to filter tickets by priority”. Step 1: write TASK.md — the goal, what not to touch, when it is done, which command checks it. Step 2: a three-to-five-line AGENTS.md — the test command and limits. Step 3: if you have an agent, run it in plan mode and read the plan without approving anything. Step 4: decide whether to accept the plan, reject it or refine the task."),
                    t("Разбор: покажите две-три TASK.md в общем чате. Ищем конкретную строку «готово, когда» с командой и явные границы «не трогать». Типичная ошибка — «сделать удобно» вместо проверяемого условия.",
                      "Walk-through: show two or three TASK.md files in the shared chat. Look for a concrete “done when” line with a command and explicit “do not touch” limits. The typical mistake is “make it convenient” instead of a checkable condition.")))


def s_hw():
    steps = [t("Стартовый проект из ДЗ (app.py + тесты) или свой маленький репозиторий", "The homework starter project (app.py + tests) or your own small repository"),
             t("AGENTS.md: команды и запреты", "AGENTS.md: commands and limits"),
             t("TASK.md: цель, не трогать, готово когда, проверка", "TASK.md: goal, do not touch, done when, check"),
             t("Агент в режиме плана → правки в отдельной ветке", "The agent in plan mode → edits on a separate branch"),
             t("Сами запустите проверку, сохраните скриншот, прочитайте diff", "Run the check yourself, save a screenshot, read the diff"),
             t("AGENT_EVIDENCE.md: план агента, что запускали, что изменилось, ваше решение", "AGENT_EVIDENCE.md: the agent’s plan, what ran, what changed, your decision")]
    ol = "".join(f'<li style="font-size:28px;color:var(--fg)"><span>{s}</span></li>' for s in steps)
    return dict(min=5, html=f'''
  {head(t("Домашнее задание", "Homework"), t("ДЗ: одна маленькая задача, выполненная агентом и проверенная вами", "Homework: one small task done by an agent and checked by you"), k="green")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.4fr 1fr;gap:40px;align-items:center;flex:none;">
      <ol class="checklist" style="gap:30px">{ol}</ol>
      <div class="stack" style="gap:18px;">
        <pre class="code" style="font-size:27px;line-height:1.65;padding:26px 30px">genai-homeworks/L16/\n├─ AGENTS.md\n├─ TASK.md\n├─ AGENT_EVIDENCE.md\n└─ check.png</pre>
        <div class="note" style="--k:var(--amber)">{t("Не программируете — меняйте только README; проверка — скриншот страницы. Без рабочих ключей.", "Don’t code? Change only the README; the check is a screenshot of the page. No production keys.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. ДЗ — тот же цикл на настоящем, но маленьком проекте. Проще всего взять стартовый проект из L16_05_Homework: app.py с функцией filter_tickets и тесты, команда pytest -q; задача — тот же фильтр по приоритету. Можно и свой маленький репозиторий. Если вы не программируете — только изменение документации (README), а проверка — скриншот страницы. Нужны AGENTS.md, TASK.md, правки в отдельной ветке, ваш запуск проверки и файл AGENT_EVIDENCE.md с планом агента и решением: принять, отклонить или повторить. Отклонённый патч с хорошим объяснением — тоже отличный результат. Подробности в L16_05_Homework.",
                      "⏱ 5 min. Homework: the same loop on a real but small project. The easiest is the starter project in L16_05_Homework: app.py with a filter_tickets function and tests, run with pytest -q; the task is the same priority filter. Your own small repository works too. If you don’t code: a docs-only change to the README, and the check is a screenshot of the page. You need AGENTS.md, TASK.md, edits on a separate branch, your own run of the check, and an AGENT_EVIDENCE.md file with the agent’s plan and your decision: accept, reject or retry. A rejected patch with a good explanation is also an excellent result. Details in L16_05_Homework.")))


def s_summary():
    rules = [("amber", t("Задача с «готово, когда»", "A task with “done when”"), t("цель, границы и команда проверки", "goal, limits and a check command")),
             ("cyan", t("Сначала план", "Plan first"), t("агент читает и предлагает, вы одобряете", "the agent reads and proposes, you approve")),
             ("red", t("Минимум прав", "Least privilege"), t("ветка, песочница, никаких рабочих ключей", "branch, sandbox, no production keys")),
             ("green", t("Решает человек", "A human decides"), t("читает diff, сливает и выпускает", "reads the diff, merges and ships"))]
    li = "".join(f'<div class="task" style="--k:var(--{k});padding:44px 40px;min-height:230px;grid-template-columns:1fr"><div><div class="h" style="font-size:40px">{h}</div><div class="d" style="font-size:27px;margin-top:12px">{d}</div></div></div>' for k, h, d in rules)
    return dict(min=4, html=f'''
  {head(t("Итоги урока и курса", "Lesson and course summary"), t("Агент делает работу — задачу, проверку и решение оставляем себе", "The agent does the work; the task, the check and the decision stay with us"), k="green")}
  <div class="body" style="margin-top:8px;">
    <div class="tasks">{li}</div>
    <div class="note" style="margin-top:44px;font-size:25px;--k:var(--violet)">{t("<b>Курс пройден:</b> от первого промпта в чате (L02) до агента, который пишет код под вашим присмотром (L16). Спасибо!", "<b>Course complete:</b> from your first chat prompt (L02) to an agent that writes code under your supervision (L16). Thank you!")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Четыре правила работы с агентом. Задача с понятным «готово, когда». Сначала план, потом правки. Минимум прав: ветка, песочница, никаких рабочих ключей. Решение — за человеком: он читает изменения, сливает и выпускает. Это последний урок: мы прошли путь от первого промпта до агента, который пишет код под вашим присмотром. Спасибо и удачи с итоговыми проектами.",
                      "⏱ 4 min. Four rules for working with an agent. A task with a clear “done when”. Plan first, then edits. Least privilege: a branch, a sandbox, no production keys. The decision belongs to a human: they read the changes, merge and ship. This is the last lesson: we went from the first prompt to an agent that writes code under your supervision. Thank you, and good luck with your final projects.")))


SLIDES = [s_cover, s_hook, s_anatomy, s_landscape, s_loop, s_task, s_rules_file, s_permissions, s_verify, s_metr,
          s_incidents, s_break, s_safe, s_exercise, s_hw, s_summary]


# ---------------------------------------------------------------- page
EXTRA_CSS = """
.bars .ref, .vline { position: absolute; top: 0; bottom: 26px; border-left: 2px dashed var(--k, var(--amber)); }
.vline span { position: absolute; top: -32px; left: 6px; white-space: nowrap; font: 600 17px var(--body); color: var(--k); }
.slide:not(.cover) .body { justify-content: flex-start; padding-top: 22px; }
.note, .plaque { font-size: 23px; }
.stat .d { font-size: 22px; }
.legend { gap: 18px; }
.legend div { font-size: 24px; }
.legend i { width: 36px; height: 36px; font: 800 20px/36px var(--body); }
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
    assert any(f.__name__ == 's_break' for f in SLIDES) and SLIDES[-2].__name__ == 's_hw'
    title = t("Урок 16: Агентная разработка | GenAI Basics", "Lesson 16: Agentic software development | GenAI Basics")
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
