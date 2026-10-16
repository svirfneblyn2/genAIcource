# -*- coding: utf-8 -*-
"""Build the L14 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. Images live in ../assets/v2/img/ (own captures 2026-10-16 and
their crops); the cover window, the prototype path and the rerun loop are drawn in HTML/SVG below.
Facts: ../L14_08_Source_Notes_Research_2026-10.md.
"""
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L14 = HERE.parent
NAME = "presentation_L14_Streamlit_Rapid_Prototyping"
OUT = {"ru": L14 / f"{NAME}_v2.html", "en": L14 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 14 • Быстрый прототип", "en": "GenAI Basics • Lesson 14 • Rapid prototype"}


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


# ---------------------------------------------------------------- drawn diagrams (bilingual, no English-only images)
ICON = {
    "bulb": '<path d="M32 8a16 16 0 0 0-9 29c2 2 3 4 3 7h12c0-3 1-5 3-7A16 16 0 0 0 32 8z"/><path d="M26 50h12M27 56h10"/>',
    "window": '<rect x="8" y="12" width="48" height="40" rx="5"/><path d="M8 22h48"/><circle cx="15" cy="17" r="1.6"/><circle cx="21" cy="17" r="1.6"/><circle cx="27" cy="17" r="1.6"/>',
    "chat": '<path d="M10 14h36a4 4 0 0 1 4 4v20a4 4 0 0 1-4 4H26l-10 8v-8h-6a4 4 0 0 1-4-4V18a4 4 0 0 1 4-4z"/><circle cx="20" cy="28" r="1.8"/><circle cx="28" cy="28" r="1.8"/><circle cx="36" cy="28" r="1.8"/>',
    "shield": '<path d="M32 6l20 8v14c0 14-9 24-20 30C21 52 12 42 12 28V14z"/><path d="M23 31l7 7 12-13"/>',
    "cursor": '<path d="M16 8l32 22-14 3 8 16-6 3-8-16-12 10z"/>',
    "file": '<path d="M16 6h22l12 12v40H16z"/><path d="M38 6v12h12M24 30h18M24 38h18M24 46h12"/>',
    "db": '<ellipse cx="32" cy="14" rx="18" ry="6"/><path d="M14 14v36c0 3.3 8 6 18 6s18-2.7 18-6V14M14 26c0 3.3 8 6 18 6s18-2.7 18-6M14 38c0 3.3 8 6 18 6s18-2.7 18-6"/>',
    "redraw": '<rect x="8" y="12" width="48" height="40" rx="5"/><path d="M8 22h48"/><path d="M42 36a10 10 0 1 1-3-7"/><path d="M40 24v6h-6"/>',
}


def icon(name, k="cyan", size=72):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" fill="none" stroke="var(--{k})" stroke-width="3" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>')


def path_diagram():
    """Idea -> prototype -> feedback -> product, with a 'this lesson' bracket under the first three."""
    stages = [("cyan", "bulb", t("Идея", "Idea"), t("одна фраза", "one sentence")),
              ("cyan", "window", t("Прототип", "Prototype"), t("Streamlit, 1 день", "Streamlit, 1 day")),
              ("cyan", "chat", t("Отзывы", "Feedback"), t("3 настоящих человека", "3 real people")),
              ("green", "shield", t("Продукт", "Product"), t("инженеры, безопасность, масштаб", "engineers, security, scale"))]
    box = lambda k, ic, h, d: (f'<div style="border:3px solid var(--{k});border-radius:22px;background:var(--surface-card);padding:40px 16px;'
                               f'display:flex;flex-direction:column;align-items:center;text-align:center;gap:14px">{icon(ic, k, 100)}'
                               f'<div style="font:800 38px/1.1 var(--display);color:var(--fg)">{h}</div>'
                               f'<div style="font:500 24px/1.3 var(--body);color:var(--muted)">{d}</div></div>')
    arrow = '<div style="font-size:40px;color:var(--dim);text-align:center;align-self:center">→</div>'
    cells = arrow.join(box(*s) for s in stages)
    bracket = (f'<div style="grid-column:1/6;margin-top:10px"><div style="height:26px;border:3px solid var(--amber);border-top:none;border-radius:0 0 12px 12px"></div>'
               f'<div style="text-align:center;font:800 28px var(--display);color:var(--amber);margin-top:6px">{t("этот урок", "this lesson")}</div></div>')
    return f'<div style="display:grid;grid-template-columns:1fr 54px 1fr 54px 1fr 54px 1fr;align-items:stretch">{cells}{bracket}</div>'


def rerun_diagram(S=580):
    """Streamlit's rerun loop drawn in HTML (pattern of L16 loop_diagram)."""
    f = S / 600
    nodes = [("cyan", 1, "cursor", t("Вы кликаете", "You click"), t("или пишете", "or type"), 300, 105),
             ("violet", 2, "file", t("Файл заново", "File reruns"), t("сверху вниз", "top to bottom"), 495, 300),
             ("green", 3, "db", t("Память", "Memory"), "session_state", 300, 495),
             ("amber", 4, "redraw", t("Страница", "Page"), t("перерисована", "redrawn"), 105, 300)]
    r = 100 * f
    circles = "".join(
        f'<div style="position:absolute;left:{x * f - r:.0f}px;top:{y * f - r:.0f}px;width:{2 * r:.0f}px;height:{2 * r:.0f}px;border-radius:50%;border:4px solid var(--{k});background:var(--surface-card);'
        f'display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 12px">'
        f'<div style="display:flex;align-items:center;gap:8px"><span style="width:32px;height:32px;border-radius:50%;background:var(--{k});color:#0b0f17;font:800 19px/32px var(--body)">{n}</span>{icon(ic, k, 40)}</div>'
        f'<div style="font:800 24px/1.1 var(--display);color:var(--{k});margin-top:6px">{h}</div>'
        f'<div style="font:500 19px/1.2 var(--body);color:var(--muted);margin-top:3px">{d}</div></div>' for k, n, ic, h, d, x, y in nodes)
    arcs = "".join(f'<path d="{d}" fill="none" stroke="#64748b" stroke-width="4" marker-end="url(#ah)"/>' for d in
                   ("M 405 150 Q 470 160 480 195", "M 470 405 Q 460 465 405 480", "M 195 480 Q 135 465 125 405", "M 130 195 Q 140 140 195 120"))
    svg = (f'<svg width="{S}" height="{S}" viewBox="0 0 600 600" style="position:absolute;left:0;top:0"><defs><marker id="ah" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto">'
           f'<path d="M0,0 L10,5 L0,10 z" fill="#64748b"/></marker></defs>{arcs}</svg>')
    centre = (f'<div style="position:absolute;left:{S / 2 - 80:.0f}px;top:{S / 2 - 46:.0f}px;width:160px;display:flex;flex-direction:column;align-items:center">'
              f'{icon("file", "cyan", 48)}<div style="font:700 24px var(--mono);color:var(--cyan);margin-top:4px">app.py</div></div>')
    return f'<div style="position:relative;width:{S}px;height:{S}px;margin:0 auto">{svg}{circles}{centre}</div>'


def cover_visual():
    """A chat-window sketch for the cover, labels via t() (replaces an English-labelled crop)."""
    bub = lambda txt, right, k: (f'<div style="align-self:{"flex-end" if right else "flex-start"};max-width:80%;border:2px solid var(--{k});border-radius:16px;'
                                 f'padding:12px 18px;font:500 22px/1.3 var(--body);color:var(--fg);background:rgba(255,255,255,.03)">{txt}</div>')
    dots = "".join('<span style="width:14px;height:14px;border-radius:50%;background:var(--cyan)"></span>' for _ in range(3))
    return (f'<div style="position:absolute;right:110px;top:200px;width:500px;border:3px solid var(--cyan);border-radius:24px;background:var(--surface-card);overflow:hidden">'
            f'<div style="display:flex;align-items:center;gap:9px;padding:16px 20px;border-bottom:3px solid var(--cyan)">{dots}'
            f'<span style="margin-left:14px;font:600 19px var(--mono);color:var(--muted)">app.py</span></div>'
            f'<div style="display:flex;flex-direction:column;gap:16px;padding:26px 24px">'
            f'{bub(t("Как оформить отпуск?", "How do I book leave?"), True, "violet")}'
            f'{bub(t("Заявление в портале за 2 недели — раздел 3 FAQ.", "Apply in the portal 2 weeks ahead — FAQ section 3."), False, "green")}'
            f'<div style="margin-top:10px;border:2px solid var(--line);border-radius:12px;padding:12px 18px;font:500 19px var(--body);color:var(--dim)">{t("Ваш вопрос", "Your question")}</div>'
            f'</div></div>')


# ---------------------------------------------------------------- slides
def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg">{cover_visual()}</div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 14 • Модуль 6: от идеи к продукту", "GenAI Basics • Lesson 14 • Module 6: idea to product")}</div>
    <h1>{t("Быстрый прототип ИИ-приложения", "Rapid AI app prototype")}</h1>
    <h2>{t("Своё окно чата на Streamlit за день — и когда хватит конструктора без кода", "Your own chat window with Streamlit in a day — and when a no-code builder is enough")}</h2>
    <p>{t("Streamlit, агент разработки, публикация, секреты. Google AI Studio Build, Claude Artifacts. Данные на октябрь 2026.",
           "Streamlit, a coding agent, publishing, secrets. Google AI Studio Build, Claude Artifacts. Data as of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. До сих пор мы пользовались чужими окнами: ChatGPT, Claude, AI Studio. Сегодня делаем своё веб-приложение с ИИ, которое можно показать коллегам и заказчику. Инструмент — Streamlit: веб-страница на чистом Python без HTML. Код напишет агент разработки, а мы научимся его понимать и проверять.",
                      "⏱ 2 min. Welcome. So far we have used other people’s windows: ChatGPT, Claude, AI Studio. Today we build our own AI web app that we can show colleagues and clients. The tool is Streamlit: a web page in plain Python, no HTML. A coding agent writes the code; we learn to understand and check it.")))


def s_hook():
    return dict(min=5, html=f'''
  {head(t("Зачем", "Why"), t("Прототип отвечает на вопрос «а как это будет выглядеть?» за день, а не за квартал", "A prototype answers “what will it look like?” in a day, not a quarter"), k="cyan")}
  <div class="body">
    {path_diagram()}
    <div class="note" style="margin-top:34px;font-size:24px;--k:var(--cyan)">{t("Кликабельный прототип собирает требования лучше любого обсуждения: люди тыкают, ломают и говорят, чего им на самом деле не хватает.", "A clickable prototype gathers requirements better than any meeting: people click, break it and say what they actually miss.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Типичная история: идея «бот, который отвечает сотрудникам по регламенту» обсуждается месяцами. Прототип за день меняет разговор: люди открывают ссылку, задают свои вопросы, видят ошибки и говорят, что им нужно на самом деле. Эти отзывы ценнее ещё одного сравнения моделей.",
                      "⏱ 5 min. A typical story: the idea “a bot that answers staff from our policy” is discussed for months. A one-day prototype changes the conversation: people open a link, ask their own questions, see the mistakes and say what they really need. That feedback is worth more than another model comparison."),
                    t("Четыре этапа: идея одной фразой, прототип за день, отзывы трёх настоящих людей и только потом продукт, которым занимаются инженеры: безопасность, масштаб, поддержка. Сегодня проходим первые три.",
                      "Four stages: the idea in one sentence, a prototype in a day, feedback from three real people, and only then a product that engineers take on: security, scale, support. Today we cover the first three.")))


def s_what():
    sh = shot("streamlit_chatbot_crop", marks=[(1, 41.5, 33.0, "amber"), (2, 78.0, 41.0, "green"), (3, 96.5, 71.0, "cyan")],
              boxes=[(1.8, 33.0, 39.7, 25.5, "amber"), (48.0, 41.5, 30.0, 16.0, "green"), (47.0, 71.5, 50.5, 23.0, "cyan")])
    return dict(min=5, html=f'''
  {head("Streamlit", t("Streamlit — веб-страница на Python: ни HTML, ни JavaScript", "Streamlit is a web page in Python: no HTML, no JavaScript"), k="cyan")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:2.1fr 1fr;gap:32px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;"><div class="prompt-label">{t("Официальный пример llm-examples.streamlit.app · фрагмент, снято 16.10.2026", "Official example llm-examples.streamlit.app · excerpt, captured 16.10.2026")}</div>{sh}</div>
      <div class="stack" style="gap:18px;">
        {legend([(1, "amber", t("<b>Боковая панель</b>: поле для ключа API", "<b>Sidebar</b>: a field for the API key")),
                 (2, "green", t("<b>Сообщения</b> чата", "<b>Chat messages</b>")),
                 (3, "cyan", t("<b>Поле ввода</b> внизу", "<b>Input box</b> at the bottom"))])}
        <div class="note" style="--k:var(--green)">{t("Официальный пример — около 25 строк Python; наш упрощённый чат — 14 (слайд 4). Бесплатно, открытый код (Apache-2.0), версия 1.66.", "The official example is about 25 lines of Python; our simplified chat is 14 (slide 4). Free, open source (Apache-2.0), version 1.66.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Это официальный пример от команды Streamlit, он открыт по адресу llm-examples.streamlit.app. Слева боковая панель с полем для ключа API, в центре сообщения чата, внизу поле ввода. Весь этот интерфейс — около двадцати пяти строк на Python, без HTML и JavaScript. Streamlit бесплатный, с открытым кодом; текущая версия 1.66 от 14 октября 2026, нужен Python 3.11 или новее.",
                      "⏱ 5 min. This is the official example from the Streamlit team at llm-examples.streamlit.app. On the left a sidebar with a field for the API key, in the middle the chat messages, at the bottom the input box. This whole interface is about twenty-five lines of Python, no HTML or JavaScript. Streamlit is free and open source; the current version is 1.66 from 14 October 2026, and it needs Python 3.11 or newer."),
                    t("Обратите внимание на поле ключа в примере: ключ вводит сам пользователь. Для своих прототипов так делать не стоит — про ключи и секреты на слайде 6.",
                      "Note the key field in the example: the user types the key in. For your own prototypes, do not do that — keys and secrets are on slide 6.")))


def s_code():
    code = ('import streamlit as st\n\n'
            '<span style=\'color:var(--amber)\'>def ask_llm(messages):</span>  # заглушка — замените вызовом API из L03\n'
            '    return "Демо-ответ: " + messages[-1]["content"]\n\n'
            'st.title("Помощник поддержки")\n\n'
            '<span style=\'color:var(--violet)\'>if "messages" not in st.session_state:</span>\n'
            '    st.session_state.messages = []          # память чата\n\n'
            'for m in st.session_state.messages:          # показать историю\n'
            '    st.chat_message(m["role"]).write(m["content"])\n\n'
            'if prompt := <span style=\'color:var(--cyan)\'>st.chat_input("Ваш вопрос")</span>:\n'
            '    st.session_state.messages.append({"role": "user", "content": prompt})\n'
            '    st.chat_message("user").write(prompt)\n'
            '    answer = <span style=\'color:var(--amber)\'>ask_llm</span>(st.session_state.messages)   # спросить модель\n'
            '    st.session_state.messages.append({"role": "assistant", "content": answer})\n'
            '    st.chat_message("assistant").write(answer)')
    if LANG == "en":
        code = (code.replace("Помощник поддержки", "Support assistant").replace("# память чата", "# chat memory").replace("# показать историю", "# show history")
                    .replace("Ваш вопрос", "Your question").replace("# спросить модель", "# ask the model")
                    .replace("# заглушка — замените вызовом API из L03", "# stub — replace with your L03 API call").replace("Демо-ответ: ", "Demo answer: "))
    n_lines = sum(1 for ln in code.split("\n") if ln.strip())
    assert n_lines == 14, n_lines  # docs (script, README) say 14
    return dict(min=6, html=f'''
  {head(t("Код (справочно)", "Code (reference)"), t(f"Весь чат — {n_lines} строк: показать историю, принять вопрос, спросить модель, показать ответ", f"The whole chat is {n_lines} lines: show history, take the question, ask the model, show the answer"), k="violet")}
  <div class="body">
    <div class="row" style="grid-template-columns:2.1fr 1fr;gap:30px;align-items:center;flex:none;">
      <div><div class="prompt-label">{t("app.py · запуск: streamlit run app.py", "app.py · run: streamlit run app.py")}</div><pre class="code" style="font-size:20px;line-height:1.33;padding:14px 22px">{code}</pre></div>
      <div class="stack" style="gap:16px;">
        <div class="note" style="--k:var(--violet)">{t("<b>session_state</b> — память чата между кликами", "<b>session_state</b> — chat memory between clicks")}</div>
        <div class="note" style="--k:var(--green)">{t("<b>for … chat_message</b> — показать всю историю", "<b>for … chat_message</b> — show the whole history")}</div>
        <div class="note" style="--k:var(--cyan)">{t("<b>chat_input</b> — поле ввода внизу", "<b>chat_input</b> — the input box at the bottom")}</div>
        <div class="note" style="--k:var(--amber)">{t("<b>ask_llm</b> — пока заглушка; агент заменит её вызовом модели: Gemini, OpenAI, локальная из L10", "<b>ask_llm</b> — a stub for now; the agent swaps in a model call: Gemini, OpenAI, the local one from L10")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Код, который рисует чат с прошлого слайда, в упрощённом виде. Писать его самим не нужно — его напишет агент. Но понимать четыре части стоит. Первая: session_state — память. Без неё история чата стиралась бы после каждого сообщения (почему — на следующем слайде).",
                      "⏱ 6 min. The code behind the chat on the previous slide, simplified. You do not need to be able to write it — an agent will. But you should understand four parts. One: session_state — memory. Without it the chat history would be wiped after every message (why — next slide)."),
                    t("Вторая: цикл, который показывает всю историю сообщениями st.chat_message. Третья: st.chat_input — поле ввода; когда человек отправил вопрос, мы добавляем его в историю и показываем. Четвёртая: ask_llm — ваш вызов модели. Вверху файла это заглушка, которая просто повторяет вопрос, — так код запускается сразу; потом её заменяют вызовом API из L03: Gemini, OpenAI или локальная модель из L10. Ответ тоже кладём в историю и показываем. Запуск: streamlit run app.py — откроется страница в браузере.",
                      "Two: the loop that shows the whole history with st.chat_message. Three: st.chat_input — the input box; when someone sends a question we add it to the history and show it. Four: ask_llm — your model call. At the top of the file it is a stub that just echoes the question, so the code runs at once; later it is replaced with the L03 API call: Gemini, OpenAI or the local model from L10. The answer goes into the history and is shown too. To run: streamlit run app.py — a page opens in the browser.")))


def s_rerun():
    return dict(min=5, html=f'''
  {head(t("Как работает", "How it works"), t("При каждом клике Streamlit заново выполняет весь файл — поэтому нужна память", "On every click Streamlit reruns the whole file — that is why memory is needed"), k="violet")}
  <div class="body">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:40px;align-items:center;flex:none;">
      <div>{rerun_diagram(560)}</div>
      <div class="stack" style="gap:24px;font-size:24px">
        <div class="note" style="--k:var(--violet)">{t("Всё, что не положили в <b>session_state</b>, при следующем клике исчезнет.", "Anything not stored in <b>session_state</b> disappears on the next click.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Самая частая «ошибка» новичка: «чат стирается» — это не баг, а этот цикл.", "The most common beginner “bug” — “the chat gets wiped” — is not a bug, it is this loop.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Главная особенность Streamlit. Обычная программа запускается один раз. Streamlit при каждом действии пользователя — клик, ввод текста — выполняет весь файл app.py заново сверху вниз и перерисовывает страницу. Это делает код простым, но всё, что было в обычных переменных, теряется.",
                      "⏱ 5 min. Streamlit’s key feature. An ordinary program runs once. Streamlit reruns the whole app.py from top to bottom on every user action — a click, typed text — and redraws the page. That keeps the code simple, but anything held in ordinary variables is lost."),
                    t("Поэтому есть session_state — память, которая переживает перезапуск, отдельная для каждого посетителя. Если студент жалуется «у меня стирается чат», почти всегда история лежит не в session_state.",
                      "That is why session_state exists — memory that survives the rerun, separate for each visitor. If a student complains “my chat gets wiped”, the history is almost always not in session_state.")))


def s_three():
    cards = [("violet", "session_state", t("память одного посетителя: история чата, выбранные настройки", "one visitor’s memory: chat history, chosen settings")),
             ("green", "cache_data", t("общий кэш для всех: файл faq.md читается один раз, а не при каждом клике", "a shared cache for everyone: faq.md is read once, not on every click")),
             ("red", "secrets", t("ключи API в файле .streamlit/secrets.toml, никогда в коде", "API keys in .streamlit/secrets.toml, never in code"))]
    cc = "".join(f'<div class="task" style="--k:var(--{k});padding:40px 32px;min-height:300px;align-items:flex-start"><div><div class="h" style="font-size:34px;font-family:var(--mono)">{h}</div><div class="d" style="font-size:26px;line-height:1.4;margin-top:16px">{d}</div></div></div>' for k, h, d in cards)
    return dict(min=5, html=f'''
  {head(t("Три слова", "Three words"), t("Память, кэш и секреты — три вещи, которые нельзя путать", "Memory, cache and secrets — three things not to mix up"), k="violet")}
  <div class="body" style="margin-top:16px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px;">{cc}</div>
    <div class="note" style="margin-top:44px;font-size:25px;--k:var(--red)">{t("Ключ в коде = ключ на GitHub (сайт, где хранят код) = ключ у всех. Добавьте secrets.toml в <b>.gitignore</b> — список файлов, которые не уходят на GitHub.", "A key in code = a key on GitHub (the site where code is stored) = a key for everyone. Add secrets.toml to <b>.gitignore</b> — the list of files that never go to GitHub.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Три понятия, которые новички путают. session_state — память одного посетителя. cache_data (команда st.cache_data) — общий кэш для всех посетителей: например, файл faq.md читается один раз, а не при каждом клике. Поэтому в кэш никогда не кладут личные данные и ключи: их увидят все.",
                      "⏱ 5 min. Three ideas beginners confuse. session_state — one visitor’s memory. cache_data (the st.cache_data command) — a shared cache for every visitor: for example, faq.md is read once, not on every click. That is why you never put personal data or keys in the cache: everyone would see them."),
                    t("secrets — ключи API. Они лежат в файле .streamlit/secrets.toml и читаются через st.secrets. Файл добавляют в .gitignore, иначе ключ уйдёт на GitHub. GitHub по умолчанию блокирует отправку найденных ключей в публичные репозитории, но надеяться на это не стоит.",
                      "secrets — API keys. They live in .streamlit/secrets.toml and are read through st.secrets. The file goes into .gitignore, otherwise the key ends up on GitHub. GitHub blocks pushing detected keys to public repos by default, but do not rely on that.")))


def s_agent():
    prompt = t(
        "Сделай прототип на Streamlit: чат-помощник, который отвечает сотрудникам по файлу faq.md.\n"
        "1. Python 3.11+, отдельное окружение (своя папка библиотек для проекта):\n   pip install streamlit google-genai\n"
        "2. Сначала выполни streamlit skills, чтобы подключить официальные навыки Streamlit.\n"
        "3. Модель Gemini 3.8 Flash, ключ из st.secrets; если ключа нет — демо-режим с заготовленным ответом.\n"
        "4. История в session_state, faq.md читать через st.cache_data.\n"
        "5. secrets.toml в .gitignore, рядом secrets.example.toml с заглушкой.\n"
        "6. Запусти streamlit run app.py и объясни мне каждую часть кода.",
        "Build a Streamlit prototype: a chat assistant that answers staff from faq.md.\n"
        "1. Python 3.11+, a separate environment:\n   pip install streamlit google-genai\n"
        "2. First run streamlit skills to add Streamlit’s official skills.\n"
        "3. Model Gemini 3.8 Flash, key from st.secrets; with no key, a demo mode with a canned answer.\n"
        "4. History in session_state, read faq.md with st.cache_data.\n"
        "5. secrets.toml in .gitignore, plus a secrets.example.toml with a placeholder.\n"
        "6. Run streamlit run app.py and explain every part of the code to me.")
    return dict(min=5, html=f'''
  {head(t("С агентом", "With an agent"), t("Код пишет агент разработки, а вы ставите задачу и проверяете результат", "A coding agent writes the code; you set the task and check the result"), k="violet")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:34px;align-items:center;flex:none;">
      <div><div class="prompt-label">{t("Промпт для агента разработки: Codex в ChatGPT или Antigravity — бесплатно с лимитом, Claude Code — платно", "Prompt for a coding agent: Codex in ChatGPT or Antigravity (free, with limits), Claude Code (paid)")}</div><pre class="code" style="font-size:21px;line-height:1.62;white-space:pre-wrap;padding:24px 26px">{prompt}</pre></div>
      <div class="stack" style="gap:18px;">
        <div class="note" style="--k:var(--violet)">{t("<b>streamlit skills</b> — официальная команда: даёт агенту инструкции, как правильно писать на Streamlit (Claude Code, Codex, Cursor).", "<b>streamlit skills</b> — an official command: it gives the agent instructions on writing Streamlit properly (Claude Code, Codex, Cursor).")}</div>
        <div class="note" style="--k:var(--green)">{t("<b>Демо-режим без ключа</b> — прототип можно показать сразу, даже без оплаты API.", "<b>A demo mode without a key</b> — the prototype can be shown at once, even without paying for an API.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Последний пункт обязателен: попросите агента объяснить код.", "The last step is a must: ask the agent to explain the code.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Как это делается на практике. Вы не пишете код руками — вы даёте агенту разработки (Codex, Antigravity, Claude Code) хорошее задание. В нём: что строим, на чём, где ключ, что делать без ключа, где хранить историю, как не утечь ключу и, главное, просьба объяснить код. Что такое агент разработки и как его выбрать — L16.",
                      "⏱ 5 min. How it is done in practice. You do not write the code by hand — you give a coding agent (Codex, Antigravity, Claude Code) a good task. It says what to build, with what, where the key is, what to do without a key, where to keep the history, how not to leak the key and, most importantly, asks to explain the code. What a coding agent is and how to choose one: L16."),
                    t("Новое с весны 2026: у Streamlit есть официальная команда streamlit skills. Она подключает к агенту навыки — инструкции от авторов Streamlit, как правильно строить приложения. Агенты Claude Code, Codex и Cursor их понимают. Демо-режим без ключа — хорошая привычка: прототип можно показать на встрече, даже если ключа ещё нет.",
                      "New since spring 2026: Streamlit has an official streamlit skills command. It plugs skills into the agent — instructions from the Streamlit authors on building apps properly. Claude Code, Codex and Cursor understand them. A demo mode without a key is a good habit: you can show the prototype at a meeting even before you have a key.")))


def s_run():
    steps = [("cyan", t("Поставить", "Install"), "pip install streamlit", t("Python 3.11 или новее", "Python 3.11 or newer")),
             ("violet", t("Запустить", "Run"), "streamlit run app.py", t("откроется localhost:8501", "opens localhost:8501")),
             ("green", t("Править", "Edit"), t("сохранили файл → Rerun", "save the file → Rerun"), t("или Always rerun — дальше само", "or Always rerun — then automatic")),
             ("amber", t("Показать", "Show"), t("Community Cloud или экран", "Community Cloud or screen share"), t("слайд 9", "slide 9"))]
    flow = '<div class="arr">→</div>'.join(f'<div class="box" style="--k:var(--{k});flex:1;padding:30px 22px;border:2px solid var(--{k})"><b style="color:var(--{k});font-size:32px">{h}</b><div style="font-family:var(--mono);font-size:21px;margin-top:14px">{c}</div><small style="font-size:20px;margin-top:10px">{d}</small></div>' for k, h, c, d in steps)
    return dict(min=5, html=f'''
  {head(t("Запуск", "Running it"), t("Четыре шага: поставить, запустить, править, показать", "Four steps: install, run, edit, show"), k="green")}
  <div class="body">
    <div class="flow" style="gap:14px;align-items:stretch">{flow}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:56px;font-size:24px">
      <div class="note" style="--k:var(--cyan)">{t("<b>localhost:8501</b> — приложение работает на вашем компьютере. В интернете его нет; в офисной сети коллега может открыть его по адресу Network URL из терминала.", "<b>localhost:8501</b> — the app runs on your computer. It is not on the internet; on an office network a colleague may open it via the Network URL shown in the terminal.")}</div>
      <div class="note" style="--k:var(--green)">{t("Изменили текст или код — сохранили — нажали Rerun (кнопка появится справа вверху). Удобно править вместе с заказчиком.", "Changed text or code — saved — clicked Rerun (the button appears top right). Handy to edit together with a client.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Четыре шага. Установить: pip install streamlit, нужен Python 3.11 или новее. Запустить: streamlit run app.py — откроется браузер с адресом localhost:8501; localhost, как в L10, значит «этот компьютер». Править: сохраняете файл, Streamlit предлагает Rerun, страница обновляется. Показать: через демонстрацию экрана или публикацию в Community Cloud.",
                      "⏱ 5 min. Four steps. Install: pip install streamlit, Python 3.11 or newer. Run: streamlit run app.py — a browser opens at localhost:8501; localhost, as in L10, means “this computer”. Edit: save the file, Streamlit offers Rerun, the page refreshes. Show: via screen share or by publishing to Community Cloud.")))


def s_deploy():
    rows = [("green", t("Свой компьютер", "Your own computer"), t("бесплатно; видят вы и, в офисной сети, коллеги; для показа — экран", "free; you, and colleagues on the office network; share your screen to show")),
            ("amber", "Streamlit Community Cloud", t("бесплатно, из репозитория (папки с кодом) на GitHub; из публичного репозитория — публичное; приватное — только одно", "free, from a GitHub repo (a code folder); from a public repo it is public; only one private app")),
            ("violet", t("Компания", "Your company"), t("Snowflake (владелец Streamlit), своё облако — с доступом по ролям; решают инженеры", "Snowflake (Streamlit’s owner), your own cloud — role-based access; engineers decide"))]
    lr = "".join(f'<div class="lrow" style="--k:var(--{k})"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for k, h, d in rows)
    return dict(min=5, html=f'''
  {head(t("Публикация", "Publishing"), t("Где показать прототип: свой компьютер, бесплатное облако Streamlit или облако компании", "Where to show a prototype: your computer, the free Streamlit cloud or your company cloud"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="light" style="gap:14px">{lr}</div>
      <div class="stack" style="gap:18px;">
        <div class="plaque" style="font-size:22px;line-height:1.5">{t("<b>Публичная ссылка = публичные данные и ваш счёт за API.</b> Любой, у кого есть ссылка, тратит ваш лимит. В публичный прототип — только синтетические данные.", "<b>A public link = public data and your API bill.</b> Anyone with the link spends your quota. A public prototype gets synthetic data only.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Бесплатное приложение засыпает через 12 часов без посетителей.", "A free app goes to sleep after 12 hours without visitors.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Три места. Свой компьютер: бесплатно; видите вы и, если вы в офисной сети, коллеги по адресу Network URL; остальным показываете через демонстрацию экрана в Teams. Streamlit Community Cloud: бесплатно, приложение публикуется из репозитория GitHub. Приложение из публичного репозитория — публичное; приватное приложение можно только одно. Засыпает через 12 часов без посетителей, первый зашедший его будит. Ключ кладут в настройки приложения, раздел Secrets.",
                      "⏱ 5 min. Three places. Your own computer: free; you see it, and so can colleagues on the office network via the Network URL; everyone else sees it when you share your screen in Teams. Streamlit Community Cloud: free, the app is published from a GitHub repo. An app from a public repo is public; you may have only one private app. It sleeps after 12 hours without visitors, and the first visitor wakes it. The key goes into the app settings, the Secrets section."),
                    t("Внутри компании — Snowflake (компания, которой принадлежит Streamlit) или своё облако с доступом по ролям, это решают инженеры. Hugging Face Spaces, которые раньше были популярным бесплатным вариантом для Streamlit, больше не бесплатны для таких приложений. Главное правило: публичная ссылка — это публичные данные и ваш счёт за API.",
                      "Inside a company — Snowflake (the company that owns Streamlit) or your own cloud with role-based access; engineers decide. Hugging Face Spaces, once a popular free option for Streamlit, are no longer free for such apps. The main rule: a public link means public data and your API bill.")))


def s_alternatives():
    sh = shot("aistudio_build_crop", marks=[(1, 98.0, 53.0, "cyan")], boxes=[(1.5, 40.0, 97.0, 36.0, "cyan")])
    rows = [("cyan", "Google AI Studio Build", t("опишите приложение здесь — получите работающее; приватно по умолчанию", "describe the app here — get a working one; private by default")),
            ("violet", "Claude Artifacts", t("маленькое приложение прямо в чате (L09)", "a small app right in the chat (L09)")),
            ("amber", "Lovable · Bolt · v0", t("сайт целиком по описанию; бесплатно — небольшой дневной лимит", "a whole site from a description; free — a small daily allowance"))]
    lr = "".join(f'<div class="lrow" style="--k:var(--{k})"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for k, h, d in rows)
    return dict(min=6, html=f'''
  {head(t("Без кода", "No code"), t("Иногда хватает конструктора: приложение по описанию, без единой строки кода", "Sometimes a builder is enough: an app from a description, no code at all"), k="cyan")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:36px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;"><div class="prompt-label">{t("aistudio.google.com → Build · снято 16.10.2026", "aistudio.google.com → Build · captured 16.10.2026")}</div>{sh}</div>
      <div class="light" style="gap:12px">{lr}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Не всегда нужен Streamlit. Google AI Studio, раздел Build: пишете «приложение, которое...» — и получаете работающее веб-приложение с предпросмотром; его можно выгрузить в GitHub или развернуть в облаке Google. Приложения приватные по умолчанию, ключ Gemini остаётся на сервере. Если вы им поделитесь, запросы других людей пойдут в ваши лимиты.",
                      "⏱ 6 min. You do not always need Streamlit. Google AI Studio, the Build section: you write “an app that...” and get a working web app with a preview; you can push it to GitHub or deploy it to Google’s cloud. Apps are private by default, and the Gemini key stays on the server. If you share it, other people’s requests count against your limits."),
                    t("Claude Artifacts из L09 — маленькие приложения прямо в чате. Lovable, Bolt и v0 делают сайт целиком по описанию; у всех есть бесплатный уровень с небольшим дневным лимитом: у Lovable и v0 это несколько запросов в день, у Bolt — лимит токенов. Streamlit выигрывает, когда нужны данные на Python, свои файлы и полный контроль над кодом.",
                      "Claude Artifacts from L09 — small apps right in the chat. Lovable, Bolt and v0 build a whole site from a description; all have a free tier with a small daily allowance: a few requests a day on Lovable and v0, a token budget on Bolt. Streamlit wins when you need Python data work, your own files and full control over the code.")))


def s_when():
    cell = lambda k, h, d: (f'<div class="layer" style="--k:var(--{k});padding:30px 30px;min-height:200px;display:flex;flex-direction:column;justify-content:center">'
                            f'<div class="lh" style="font-size:32px">{h}</div><div class="ls" style="font-size:24px;margin-top:10px">{d}</div></div>')
    ax = 'font:600 23px var(--body);color:var(--muted);display:flex;align-items:center;justify-content:center;text-align:center'
    grid = (f'<div style="display:grid;grid-template-columns:240px 1fr 1fr;grid-template-rows:auto 1fr 1fr;gap:20px;">'
            f'<div></div><div style="{ax}">{t("Показать идею", "Show an idea")}</div><div style="{ax}">{t("Работать с данными", "Work with data")}</div>'
            f'<div style="{ax}">{t("Не программирую", "I don’t code")}</div>'
            + cell("cyan", "AI Studio Build · Artifacts", t("за 10 минут, по описанию", "in 10 minutes, from a description"))
            + cell("violet", t("Claude / ChatGPT + файлы", "Claude / ChatGPT + files"), t("анализ без приложения (L08)", "analysis without an app (L08)"))
            + f'<div style="{ax}">{t("Готов читать код с агентом", "Ready to read code with an agent")}</div>'
            + cell("green", "Streamlit", t("свой интерфейс, свои правила", "your own UI, your own rules"))
            + cell("amber", "Streamlit + pandas", t("pandas — библиотека для таблиц: графики, свои файлы", "pandas — a table library: charts, your own files"))
            + '</div>')
    return dict(min=5, html=f'''
  {head(t("Что выбрать", "What to choose"), t("Выбор по двум вопросам: что показываем и готовы ли вы читать код", "Choose by two questions: what you are showing and whether you will read code"), k="cyan")}
  <div class="body" style="margin-top:12px;">{grid}</div>''',
                notes=notes(
                    t("⏱ 5 мин. Простая таблица выбора. Если нужно быстро показать идею и вы не программируете — AI Studio Build или Claude Artifacts. Если нужно поработать с данными без своего приложения — Claude или ChatGPT с файлами, как в L08. Если вы готовы читать код вместе с агентом — Streamlit: свой интерфейс и свои правила, а с pandas — таблицы и графики по вашим файлам.",
                      "⏱ 5 min. A simple choice table. To show an idea quickly without coding — AI Studio Build or Claude Artifacts. To work with data without your own app — Claude or ChatGPT with files, as in L08. If you are ready to read code with an agent — Streamlit: your own UI and rules, and with pandas, tables and charts from your files.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут: придумайте, какой прототип покажете коллегам", "5 minutes: think which prototype you will show colleagues")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: практика, безопасность, путь к продукту, ДЗ.", "Next: hands-on, security, the path to a product, homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт».", "⏱ 5 min. Press “Start”.")))


def s_practice():
    steps = [(t("Идея", "Idea"), t("одна фраза", "one sentence")), (t("Данные", "Data"), t("текст FAQ, синтетика", "FAQ text, synthetic")),
             (t("Сборка", "Build"), t("AI Studio Build или агент", "AI Studio Build or an agent")), (t("Тест", "Test"), t("3 вопроса", "3 questions")),
             (t("Показ", "Show"), t("экран в Teams", "Teams screen share"))]
    flow = '<div class="arr" style="font-size:34px">→</div>'.join(
        f'<div class="box" style="flex:1;padding:36px 18px;font-size:28px;font-weight:700;border:2px solid var(--green);text-align:center">'
        f'<b style="color:var(--green)">{i}</b> {a}<small style="font-size:22px;font-weight:500;margin-top:8px">{b}</small></div>' for i, (a, b) in enumerate(steps, 1))
    return dict(min=10, html=f'''
  {head(t("Практика", "Hands-on"), t("Практика 10 минут: прототип помощника по вашему FAQ", "10-minute hands-on: a helper prototype for your FAQ"), k="green")}
  <div class="body">
    <div class="flow" style="--k:var(--green);gap:12px;align-items:stretch">{flow}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:56px;align-items:start;">
      <div class="note" style="--k:var(--cyan)">{t("<b>Без кода:</b> AI Studio → Build → «Сделай чат-помощника, который отвечает по этому FAQ» + вставьте 10 вопросов-ответов.", "<b>No code:</b> AI Studio → Build → “Make a chat helper that answers from this FAQ” + paste 10 Q&As.")}</div>
      <div class="note" style="--k:var(--violet)">{t("<b>С кодом</b> (только если Python и агент уже установлены): промпт со слайда 7; запуск streamlit run app.py.", "<b>With code</b> (only if Python and an agent are already installed): the slide 7 prompt; run streamlit run app.py.")}</div>
    </div>
    <div class="plaque g" style="margin-top:44px">{t("<b>0–7 мин</b> — соберите прототип и задайте ему 3 вопроса. <b>7–10 мин</b> — 2–3 человека показывают экран: вопрос и ответ прототипа.", "<b>0–7 min</b> — build the prototype and ask it 3 questions. <b>7–10 min</b> — 2–3 people share their screen: the question and the prototype’s answer.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 10 мин. Практика. Каждый делает прототип помощника по своему FAQ: 10 вопросов и ответов, придуманных или обезличенных. Без кода — через AI Studio Build. С кодом — промптом со слайда 7 агенту разработки. Через 7 минут 2–3 человека показывают экран: какой вопрос задали и что ответил прототип.",
                      "⏱ 10 min. Hands-on. Everyone builds a helper prototype for their own FAQ: 10 questions and answers, made up or anonymised. Without code — via AI Studio Build. With code — the slide 7 prompt to a coding agent. After 7 minutes 2–3 people share their screen: what they asked and what the prototype answered.")))


def s_safety():
    rows = [("red", t("Ключи", "Keys"), t("только в secrets, не в коде и не в чате с агентом", "only in secrets, not in code and not in the chat with the agent")),
            ("red", t("Данные", "Data"), t("публичный прототип — только синтетика", "a public prototype — synthetic data only")),
            ("amber", t("Деньги", "Money"), t("лимит расходов в консоли API; демо-режим без ключа", "a spending limit in the API console; a demo mode with no key")),
            ("violet", t("Вход", "Sign-in"), t("приватное приложение в Community Cloud + приглашения по email", "a private Community Cloud app + email invites"))]
    lr = "".join(f'<div class="lrow" style="--k:var(--{k})"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for k, h, d in rows)
    return dict(min=5, html=f'''
  {head(t("Безопасность", "Security"), t("Четыре правила прототипа: ключи, данные, деньги, вход", "Four prototype rules: keys, data, money, sign-in"), k="red")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="light" style="gap:14px">{lr}</div>
      <div class="plaque" style="font-size:22px;line-height:1.5">{t("Прототип — не продукт. Пока его не проверили инженеры и безопасность, он не трогает настоящие данные клиентов.", "A prototype is not a product. Until engineers and security review it, it does not touch real customer data.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Четыре правила. Ключи: только в secrets; не вставляйте ключ в чат с агентом разработки — он может попасть в журналы. Данные: в публичный прототип только синтетика. Деньги: поставьте лимит расходов в консоли API и сделайте демо-режим без ключа. Вход: если прототип не для всех, сделайте его приватным в Community Cloud и пригласите людей по email. Для инженеров: в Streamlit есть и встроенный вход через st.login.",
                      "⏱ 5 min. Four rules. Keys: only in secrets; do not paste a key into the chat with a coding agent — it may end up in logs. Data: a public prototype gets synthetic data only. Money: set a spending limit in the API console and add a demo mode with no key. Sign-in: if the prototype is not for everyone, make it private in Community Cloud and invite people by email. For engineers: Streamlit also has built-in sign-in with st.login.")))


def s_product():
    rows = [(t("Прототип", "Prototype"), t("Продукт", "Product")),
            (t("один файл app.py", "one app.py file"), t("код в репозитории, ревью, тесты", "code in a repo, reviews, tests")),
            (t("синтетические данные", "synthetic data"), t("реальные данные, права доступа, журнал", "real data, access rights, logs")),
            (t("ключ разработчика", "a developer’s key"), t("ключ сервиса, лимиты, мониторинг", "a service key, limits, monitoring")),
            (t("работает у меня", "works on my machine"), t("работает у всех, 24/7", "works for everyone, 24/7"))]
    trs = "".join(f'<div style="display:grid;grid-template-columns:1fr 60px 1fr;gap:10px;align-items:center;{"font-weight:700;color:var(--fg);font-size:32px" if i == 0 else "font-size:27px;color:var(--muted)"}">'
                  f'<div style="padding:18px 22px;border-left:5px solid var(--cyan)">{a}</div><div style="text-align:center;color:var(--dim);font-size:30px">→</div>'
                  f'<div style="padding:18px 22px;border-left:5px solid var(--green)">{b}</div></div>' for i, (a, b) in enumerate(rows))
    return dict(min=5, html=f'''
  {head(t("Дальше", "Next"), t("Что меняется, когда прототип становится продуктом", "What changes when a prototype becomes a product"), k="green")}
  <div class="body" style="margin-top:16px;">
    <div style="display:flex;flex-direction:column;gap:16px">{trs}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Прототип сделал своё дело: показал идею и собрал отзывы. Дальше его передают инженерам, и меняется многое. Код живёт в репозитории с ревью и тестами. Данные реальные, поэтому нужны права доступа и журнал. Ключ — не ваш личный, а служебный, с лимитами и мониторингом. И приложение должно работать у всех и круглосуточно. Об агентной разработке продуктов — урок 16.",
                      "⏱ 5 min. The prototype has done its job: it showed the idea and gathered feedback. Then it goes to engineers, and much changes. The code lives in a repo with reviews and tests. The data is real, so access rights and logs are needed. The key is not your personal one but a service key with limits and monitoring. And the app must work for everyone, around the clock. Agentic product development — lesson 16.")))


def s_hw():
    tree = ("genai-homeworks/L14/\n├─ README.md      # идея и вывод\n├─ app.py или ссылка\n├─ faq.md         # синтетика\n├─ feedback.md    # отзывы 3 людей\n└─ demo.png")
    if LANG == "en":
        tree = ("genai-homeworks/L14/\n├─ README.md      # idea, conclusion\n├─ app.py or a link\n├─ faq.md         # synthetic\n├─ feedback.md    # 3 people’s feedback\n└─ demo.png")
    steps = [t("Идея прототипа одной фразой: для кого и что делает", "The prototype idea in one sentence: for whom and what it does"),
             t("Соберите: Streamlit с агентом или AI Studio Build", "Build it: Streamlit with an agent, or AI Studio Build"),
             t("Только синтетические данные, ключ — в secrets", "Synthetic data only; the key in secrets"),
             t("Покажите 3 коллегам, запишите их отзывы", "Show it to 3 colleagues and record their feedback"),
             t("Что бы вы поменяли — 3 пункта", "What you would change — 3 points")]
    ol = "".join(f"<li><span>{s}</span></li>" for s in steps)
    return dict(min=6, html=f'''
  {head(t("Домашнее задание", "Homework"), t("ДЗ: прототип и отзывы трёх настоящих людей", "Homework: a prototype and feedback from three real people"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:40px;align-items:center;flex:none;">
      <ol class="checklist">{ol}</ol>
      <pre class="code" style="font-size:24px;line-height:1.7;padding:30px 30px">{tree}</pre>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. ДЗ: прототип для своей работы и, главное, отзывы трёх коллег. Собрать любым способом — Streamlit с агентом или AI Studio Build. Только синтетические данные. Показать трём людям и записать, что они сказали, и три изменения, которые вы бы внесли. Оценивается не красота, а то, насколько прототип помог понять задачу. Подробности в L14_05_Homework.",
                      "⏱ 6 min. Homework: a prototype for your work and, above all, feedback from three colleagues. Build it any way — Streamlit with an agent or AI Studio Build. Synthetic data only. Show it to three people, record what they said and three changes you would make. Grading looks not at polish but at how much the prototype helped you understand the task. Details in L14_05_Homework.")))


def s_summary():
    rules = [("cyan", t("Прототип за день", "A prototype in a day"), t("лучше месяца обсуждений", "beats a month of meetings")),
             ("violet", t("Streamlit = Python + перезапуск", "Streamlit = Python + reruns"), t("память в session_state", "memory in session_state")),
             ("red", t("Ключи в secrets", "Keys in secrets"), t("публичная ссылка = публичные данные", "a public link = public data")),
             ("green", t("Агент пишет, вы проверяете", "The agent writes, you check"), t("попросите объяснить код", "ask it to explain the code"))]
    li = "".join(f'<div class="task" style="--k:var(--{k});padding:34px 30px;min-height:170px"><div><div class="h" style="font-size:32px">{h}</div><div class="d" style="font-size:25px;margin-top:10px">{d}</div></div></div>' for k, h, d in rules)
    return dict(min=5, html=f'''
  {head(t("Итоги", "Summary"), t("Прототип за день, память в session_state, ключи в secrets, код проверяете вы", "A prototype in a day, memory in session_state, keys in secrets, you check the code"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="tasks">{li}</div>
    <div class="note" style="margin-top:40px;font-size:24px;--k:var(--violet)">{t("<b>Дальше, L15:</b> ответственный ИИ, безопасность и законы — что можно и нельзя с данными и контентом.", "<b>Next, L15:</b> responsible AI, security and law — what you may and may not do with data and content.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Четыре мысли. Прототип за день полезнее месяца обсуждений. Streamlit — это Python и перезапуск при каждом клике, поэтому память храним в session_state. Ключи — только в secrets, публичная ссылка — это публичные данные. Код пишет агент, а вы проверяете и просите объяснить. Следующий урок — ответственный ИИ, безопасность и законы.",
                      "⏱ 5 min. Four ideas. A prototype in a day is more useful than a month of meetings. Streamlit is Python plus a rerun on every click, so memory lives in session_state. Keys only in secrets; a public link means public data. The agent writes the code, and you check it and ask for explanations. Next lesson — responsible AI, security and law.")))


SLIDES = [s_cover, s_hook, s_what, s_code, s_rerun, s_three, s_agent, s_run, s_deploy, s_alternatives,
          s_when, s_break, s_practice, s_safety, s_product, s_hw, s_summary]


# ---------------------------------------------------------------- page
EXTRA_CSS = """
.slide:not(.cover) .body { justify-content: flex-start; padding-top: 22px; }
.slide .note { font-size: 23px; }
.light { gap: 20px !important; }
.lrow { padding: 24px 26px; grid-template-columns: 34px 1fr; }
.lrow .dot { width: 30px; height: 30px; }
.lrow .h { font-size: 29px; }
.lrow .d { font-size: 23px; margin-top: 4px; }
.plaque { font-size: 24px !important; padding: 22px 26px; }
.checklist { gap: 34px; }
.checklist li { font-size: 27px; grid-template-columns: 52px 1fr; }
.checklist li::before { width: 36px; height: 36px; font-size: 20px; }
.legend div { font-size: 24px; }
.flow .arr { align-self: center; }
.bars .ref, .vline { position: absolute; top: 0; bottom: 26px; border-left: 2px dashed var(--k, var(--amber)); }
.vline span { position: absolute; top: -32px; left: 6px; white-space: nowrap; font: 600 17px var(--body); color: var(--k); }
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
    title = t("Урок 14: Быстрый прототип ИИ-приложения | GenAI Basics", "Lesson 14: Rapid AI app prototype | GenAI Basics")
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
