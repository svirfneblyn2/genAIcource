# -*- coding: utf-8 -*-
"""Build the L10 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. Images live in ../assets/v2/img/ (own captures 2026-10-16,
one official LM Studio image with credit; schematics are drawn in HTML).
Facts: ../L10_08_Source_Notes_Research_2026-10.md.
"""
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L10 = HERE.parent
NAME = "presentation_L10_Open_Models_Local_and_RunPod"
OUT = {"ru": L10 / f"{NAME}_v2.html", "en": L10 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 10 • Открытые модели", "en": "GenAI Basics • Lesson 10 • Open models"}


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


# Line icons drawn inline (64×64 grid), so diagrams have no baked-in English text.
ICONS = {
    "cloud": '<path d="M19 47h27a12 12 0 0 0 1-24 15 15 0 0 0-29 3 10.5 10.5 0 0 0 1 21z"/><rect x="27" y="31" width="12" height="9" rx="1.5"/><path d="M29.5 31v-3a3.5 3.5 0 0 1 7 0v3"/>',
    "laptop": '<rect x="12" y="13" width="40" height="28" rx="3"/><path d="M4 46h56l-4 6H8z"/><path d="M27 21h8l4 4v9H27z"/>',
    "server": '<rect x="9" y="7" width="40" height="14" rx="3"/><rect x="9" y="25" width="40" height="14" rx="3"/><rect x="9" y="43" width="40" height="14" rx="3"/><circle cx="17" cy="14" r="2"/><circle cx="17" cy="32" r="2"/><circle cx="17" cy="50" r="2"/><path d="M53 22v20M58 26v12"/>',
    "file": '<path d="M16 6h22l12 12v40H16z"/><path d="M38 6v12h12"/><path d="M23 32h18M23 40h18M23 48h12"/>',
    "gear": '<circle cx="32" cy="32" r="8"/><circle cx="32" cy="32" r="18"/><path d="M32 8v6M32 50v6M8 32h6M50 32h6M15 15l4.5 4.5M44.5 44.5L49 49M15 49l4.5-4.5M44.5 19.5L49 15"/>',
    "chip": '<rect x="17" y="17" width="30" height="30" rx="3"/><rect x="26" y="26" width="12" height="12" rx="1"/><path d="M24 17v-8M32 17v-8M40 17v-8M24 47v8M32 47v8M40 47v8M17 24h-8M17 32h-8M17 40h-8M47 24h8M47 32h8M47 40h8"/>',
    "globe": '<circle cx="32" cy="32" r="23"/><path d="M9 32h46M32 9c9 8 9 38 0 46M32 9c-9 8-9 38 0 46"/>',
    "app": '<rect x="6" y="11" width="52" height="42" rx="4"/><path d="M6 21h52"/><path d="M26 30l-7 7 7 7M38 30l7 7-7 7"/>',
}


def icon(name, size=64, k="cyan", sw=3):
    return (f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" fill="none" stroke="var(--{k})" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" style="flex:none">{ICONS[name]}</svg>')


def places():
    """The three places a model can run (cloud / laptop / rented GPU), bilingual."""
    return [("violet", "cloud", t("Облачный API", "Cloud API"), "api.openai.com"),
            ("green", "laptop", t("Ваш ноутбук", "Your laptop"), "localhost:1234"),
            ("amber", "server", t("Арендованная видеокарта", "Rented GPU"), "pod-id.runpod.net")]


def places_cover():
    """Cover visual: three destination cards with their addresses."""
    cards = "".join(
        f'<div style="display:flex;align-items:center;gap:22px;border:2px solid var(--{k});border-radius:16px;padding:18px 24px;background:var(--surface-card)">'
        f'{icon(ic, 76, k)}<div><div style="font:800 30px/1.15 var(--display);color:var(--{k})">{h}</div>'
        f'<div style="font:500 20px var(--mono);color:var(--muted);margin-top:6px">{a}</div></div></div>' for k, ic, h, a in places())
    return f'<div style="position:absolute;right:90px;top:50%;transform:translateY(-50%);width:560px;display:flex;flex-direction:column;gap:26px">{cards}</div>'


def places_diagram():
    """Slide 2: one app → three addresses → three places."""
    app = (f'<div style="grid-row:1/4;align-self:center;display:flex;flex-direction:column;align-items:center;gap:12px;border:2px solid var(--cyan);'
           f'border-radius:16px;padding:26px 16px;background:var(--surface-card);text-align:center">{icon("app", 96, "cyan")}'
           f'<div style="font:800 27px/1.2 var(--display);color:var(--cyan)">{t("Ваше приложение", "Your app")}</div>'
           f'<div style="font:500 18px/1.3 var(--body);color:var(--muted)">{t("один и тот же код", "the same code")}</div></div>')
    rows = ""
    for k, ic, h, a in places():
        rows += (f'<div style="position:relative;height:100%;display:flex;align-items:center">'
                 f'<div style="flex:1;border-top:3px dashed var(--{k})"></div><div style="color:var(--{k});font-size:26px;line-height:1;margin-left:-4px">▶</div>'
                 f'<div style="position:absolute;left:18px;right:18px;top:50%;transform:translateY(-130%);text-align:center;font:600 20px var(--mono);color:var(--fg)">{a}</div></div>'
                 f'<div style="display:flex;align-items:center;gap:18px;border:2px solid var(--{k});border-radius:14px;padding:24px 20px;background:var(--surface-card)">'
                 f'{icon(ic, 72, k)}<div style="font:800 26px/1.2 var(--display);color:var(--{k})">{h}</div></div>')
    return (f'<div style="display:grid;grid-template-columns:230px 1fr 340px;grid-template-rows:repeat(3,auto);row-gap:44px;column-gap:0;align-items:stretch">'
            f'{app}{rows}</div>')


def parts_diagram():
    """Slide 5: file → engine → hardware → server → app, with the LM Studio bracket over the first four."""
    parts = [("file", t("Файл модели", "Model file"), t("веса, .gguf", "weights, .gguf")),
             ("gear", t("Движок", "Engine"), "llama.cpp"),
             ("chip", t("Железо", "Hardware"), t("процессор, видеокарта, память", "CPU, GPU, memory")),
             ("globe", t("Сервер", "Server"), "localhost:1234"),
             ("app", t("Приложение", "Your app"), t("чат или Python", "chat or Python"))]
    cells = []
    for i, (ic, h, d) in enumerate(parts):
        if i:
            cells.append('<div style="grid-row:2;align-self:start;margin-top:60px;font-size:44px;color:var(--muted);text-align:center">→</div>')
        k = "green" if ic == "app" else "cyan"
        cells.append(f'<div style="grid-row:2;display:flex;flex-direction:column;align-items:center;text-align:center;gap:12px">'
                     f'<div style="width:170px;height:170px;border:2px solid var(--{k});border-radius:22px;background:var(--surface-card);display:flex;align-items:center;justify-content:center">{icon(ic, 110, k)}</div>'
                     f'<div style="font:800 28px/1.15 var(--display);color:var(--fg)">{h}</div>'
                     f'<div style="font:500 19px/1.3 var(--body);color:var(--muted)">{d}</div></div>')
    cols = " 56px ".join(["1fr"] * len(parts))
    bracket = (f'<div style="grid-row:1;grid-column:1/8;display:flex;flex-direction:column;align-items:stretch;margin-bottom:14px">'
               f'<div style="text-align:center;font:800 26px var(--display);color:var(--violet)">{t("LM Studio или Ollama делают это за вас", "LM Studio or Ollama does this for you")}</div>'
               f'<div style="height:18px;border:3px solid var(--violet);border-bottom:none;border-radius:10px 10px 0 0;margin:8px 40px 0"></div></div>')
    return f'<div style="display:grid;grid-template-columns:{cols};row-gap:0">{bracket}{"".join(cells)}</div>'


# ---------------------------------------------------------------- slides
def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg">{places_cover()}</div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 10 • Модуль 4: открытые модели", "GenAI Basics • Lesson 10 • Module 4: open models")}</div>
    <h1>{t("Открытые модели", "Open models")}</h1>
    <h2>{t("Как запустить языковую модель на своём ноутбуке и на арендованной видеокарте", "How to run a language model on your laptop and on a rented GPU")}</h2>
    <p>{t("Hugging Face, LM Studio, Ollama, Runpod. Размер модели, память, скорость, цена. Данные на октябрь 2026.",
           "Hugging Face, LM Studio, Ollama, Runpod. Model size, memory, speed, price. Data as of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. До сих пор мы пользовались чужими моделями: ChatGPT, Gemini, Claude, ElevenLabs. Они живут в облаке, мы платим за подписку или за токены, а данные уходят к поставщику. Сегодня ставим модель к себе.",
                      "⏱ 2 min. Welcome. So far we have used other people’s models: ChatGPT, Gemini, Claude, ElevenLabs. They live in the cloud; we pay a subscription or per token, and our data goes to the vendor. Today we run a model ourselves."),
                    t("План: что такое открытая модель, что нужно компьютеру, LM Studio и локальный сервер, агент ставит модель за вас, рынок открытых моделей. После перерыва: когда ноутбука мало, аренда видеокарты в Runpod, цена, как выбрать, домашнее задание.",
                      "Plan: what an open model is, what your computer needs, LM Studio and a local server, an agent installs a model for you, the open model market. After the break: when a laptop is not enough, renting a GPU on Runpod, price, how to choose, homework.")))


def s_hook():
    return dict(min=4, html=f'''
  {head(t("Идея урока", "The idea"), t("Одно приложение, три места, где работает модель", "One app, three places where the model runs"), k="cyan")}
  <div class="body big" style="margin-top:8px;">
    <div style="height:20px"></div>
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:48px;align-items:center;flex:none;">
      {places_diagram()}
      <div class="legend" style="gap:22px">
        <div style="--k:var(--violet)"><i>1</i><span>{t("<b>Облачный API</b>: модель у поставщика, платим за токены, данные уходят к нему", "<b>Cloud API</b>: the vendor runs the model; you pay per token and your data goes to them")}</span></div>
        <div style="--k:var(--green)"><i>2</i><span>{t("<b>Ваш ноутбук</b> (localhost = «этот компьютер»): файл модели у вас, интернет не нужен, платите железом", "<b>Your laptop</b> (localhost = “this computer”): the model file is yours, no internet needed, you pay with hardware")}</span></div>
        <div style="--k:var(--amber)"><i>3</i><span>{t("<b>Арендованная видеокарта</b>: ваша модель на чужом мощном компьютере, оплата по часам", "<b>Rented GPU</b>: your model on someone else’s powerful machine, paid by the hour")}</span></div>
      </div>
    </div>
    <div class="note" style="margin-top:40px;font-size:23px;--k:var(--cyan)">{t("<b>Главное:</b> код приложения почти не меняется: меняются только адрес и имя модели.", "<b>Key point:</b> the app’s code barely changes: only the address and model name change.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Слева приложение, например бот поддержки из прошлых уроков. Оно отправляет запрос модели. Первый вариант нам знаком: облачный API, адрес api.openai.com или Gemini API. Второй: та же задача, но модель лежит файлом на вашем ноутбуке, адрес localhost, то есть «этот компьютер». Третий: ваша модель на арендованной видеокарте в облаке Runpod.",
                      "⏱ 4 min. On the left is an app, for example the support bot from earlier lessons. It sends a request to a model. The first option we know: a cloud API at api.openai.com or the Gemini API. The second: the same task, but the model is a file on your laptop, at localhost, meaning “this computer”. The third: your model on a rented GPU in the Runpod cloud."),
                    t("Почему это важно. Многие локальные программы (LM Studio, Ollama) говорят на том же «языке», что и OpenAI API. Поэтому переход между тремя вариантами — это смена адреса и имени модели в настройках, а не переписывание приложения. К концу урока вы сможете осознанно выбрать один из трёх.",
                      "Why it matters. Many local tools (LM Studio, Ollama) speak the same “language” as the OpenAI API. So moving between the three options means changing the address and the model name in settings, not rewriting the app. By the end of the lesson you can choose one of the three on purpose."),
                    t("Вопрос в чат: какие данные вашей компании вы не стали бы отправлять в ChatGPT? Это и есть первый повод для локальной модели.",
                      "Question for the chat: what company data would you not send to ChatGPT? That is the first reason for a local model.")))


def s_open():
    return dict(min=5, html=f'''
  {head(t("Открытая модель", "Open model"), t("Открытая модель — это файл, который можно скачать, и лицензия к нему", "An open model is a file you can download, plus its licence"), k="green")}
  <div class="body" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:36px;align-items:start;flex:none;">
      <div class="stack" style="gap:10px;">
        <div class="prompt-label">{t("Hugging Face · ibm-granite/granite-4.2-8b-GGUF · снято 16.10.2026", "Hugging Face · ibm-granite/granite-4.2-8b-GGUF · captured 16.10.2026")}</div>
        {shot("hf_granite_header", marks=[(1, 48.5, 4.5, "cyan"), (2, 72.0, 31.0, "green")], boxes=[(1.5, 4.0, 46.0, 17.0, "cyan"), (52.5, 23.0, 18.0, 16.0, "green")])}
        {shot("hf_granite_files", marks=[(3, 96.0, 6.5, "amber")], boxes=[(1.0, 0.5, 98.0, 12.0, "amber"), (1.0, 87.5, 98.0, 12.0, "amber")])}
      </div>
      <div class="stack" style="gap:20px;">
        {legend([(1, "cyan", t("<b>Кто сделал</b>: IBM, Granite 4.2 8B. <b>8B</b> = 8 млрд параметров, то есть чисел внутри модели", "<b>Who made it</b>: IBM, Granite 4.2 8B. <b>8B</b> = 8 billion parameters, the numbers inside the model")),
                 (2, "green", t("<b>Лицензия</b> Apache-2.0: можно в работе и в коммерции", "<b>Licence</b> Apache-2.0: fine for work and commercial use")),
                 (3, "amber", t("<b>Файлы .gguf</b> (формат для LM Studio и Ollama): одна модель в разных размерах, здесь около 5–9 ГБ; полный список — слайд 6", "<b>.gguf files</b> (the format for LM Studio and Ollama): one model in several sizes, here about 5–9 GB; full list on slide 6"))])}
        <div class="note" style="--k:var(--green)">{t("<b>Hugging Face</b> — главный «склад» открытых моделей. У каждой есть карточка: что умеет, ограничения, лицензия.", "<b>Hugging Face</b> is the main “warehouse” of open models. Each has a card: what it does, its limits, its licence.")}</div>
        <div class="note" style="--k:var(--red)">{t("«Открытая» ≠ «можно всё». У Llama 4 своя лицензия с ограничениями, у MusicGen (L06) только некоммерческая.", "“Open” ≠ “anything goes”. Llama 4 has its own restrictive licence; MusicGen (L06) is non-commercial only.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Покажите страницу вживую, если есть время: huggingface.co, поиск «granite-4.2-8b-GGUF». Открытая модель — это прежде всего файлы весов: обученные числа, которые можно скачать и запустить у себя. ChatGPT так скачать нельзя, это закрытая модель.",
                      "⏱ 5 min. Show the page live if there is time: huggingface.co, search “granite-4.2-8b-GGUF”. An open model is first of all weight files: trained numbers you can download and run yourself. You cannot download ChatGPT like that; it is a closed model."),
                    t("Три вещи на странице. Первое: кто сделал. IBM, модель Granite 4.2 на 8 миллиардов параметров. Параметры — это те самые числа внутри модели; чем их больше, тем модель обычно умнее и тяжелее. Второе: лицензия. Apache-2.0 разрешает использовать в работе и в коммерческих продуктах, если сохранить текст лицензии. Третье: файлы. Одна и та же модель лежит в нескольких размерах: Q2, Q4, Q8. Это сжатие, разберём на слайде 6.",
                      "Three things on the page. One: who made it. IBM, Granite 4.2 with 8 billion parameters. Parameters are the numbers inside the model; more of them usually means a smarter and heavier model. Two: the licence. Apache-2.0 allows use at work and in commercial products, as long as you keep the licence text. Three: files. The same model comes in several sizes: Q2, Q4, Q8. That is compression; slide 6 covers it."),
                    t("Формат GGUF — это файл модели для программ вроде LM Studio и Ollama: веса плюс описание модели в одном файле. Лицензии бывают разные. Apache-2.0 и MIT — свободные. У Llama 4 своя лицензия Meta с условиями и доступом по запросу. Правило: прочитали лицензию до того, как строить на модели продукт.",
                      "GGUF is a model file format for tools like LM Studio and Ollama: weights plus a model description in one file. Licences vary. Apache-2.0 and MIT are permissive. Llama 4 has Meta’s own licence with conditions and gated access. Rule: read the licence before you build a product on a model.")))


def s_why():
    rows = [(t("Лучшая закрытая", "Best closed"), "Claude Opus 5.5", 58, "violet"),
            (t("Лучшая открытая", "Best open"), "MiMo-V2.6-Pro", 46, "green"),
            (t("Для 1 видеокарты", "Fits 1 GPU"), t("открытая Qwen3.8 27B", "open Qwen3.8 27B"), 34, "cyan")]
    ch = bars(rows, 0, 65, lambda v: f"{v:.0f}", ticks=[(0, "0"), (20, "20"), (40, "40"), (60, "60")], label_w=280)
    return dict(min=4, html=f'''
  {head(t("Зачем", "Why"), t("Своя модель: данные не уходят, но качество ниже лидеров", "Your own model: data stays home, but quality trails the leaders"), k="amber")}
  <div class="body big">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:56px;align-items:start;flex:none;margin-top:50px">
      <div class="stack" style="gap:34px;">
        <div class="note" style="--k:var(--green)">{t("<b>Плюсы:</b> данные не покидают компьютер · работает без интернета · нет счёта за токены · модель не поменяют без вас", "<b>Pros:</b> data never leaves the machine · works offline · no per-token bill · nobody changes the model behind your back")}</div>
        <div class="note" style="--k:var(--red)">{t("<b>Минусы:</b> слабее лучших облачных · нужна память и видеокарта · установка и обновления на вас", "<b>Cons:</b> weaker than the best cloud models · needs memory and a GPU · setup and updates are your job")}</div>
        <div class="note" style="--k:var(--cyan)">{t("<b>Хорошо подходит:</b> разбор писем и тикетов, черновики, поиск по своим документам. <b>Плохо:</b> сложные рассуждения, большой код.", "<b>Good for:</b> sorting emails and tickets, drafts, search over your own documents. <b>Poor at:</b> hard reasoning, large codebases.")}</div>
      </div>
      <div class="stack" style="gap:22px;">
        <div class="prompt-label">{t("Индекс «интеллекта» Artificial Analysis, октябрь 2026", "Artificial Analysis Intelligence Index, October 2026")}</div>
        {ch}
        <div class="small" style="font-size:20px">{t("Чем выше, тем лучше. Разрыв между лучшей закрытой и лучшей открытой ≈ 12 пунктов.", "Higher is better. The gap between the best closed and best open model is ≈ 12 points.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Честная картина. Плюсы своей модели: данные не уходят из компьютера, работает в самолёте и в закрытой сети, нет счёта за каждый запрос, и модель не изменится завтра без вашего ведома (у облачных моделей версии меняются).",
                      "⏱ 4 min. The honest picture. Pros of your own model: data never leaves the computer, it works on a plane or in a closed network, there is no bill per request, and the model will not change tomorrow without you knowing (cloud model versions do change)."),
                    t("Минусы: качество. Независимый рейтинг Artificial Analysis (индекс v4.3, октябрь 2026): лучшая закрытая модель Claude Opus 5.5 — 58 пунктов, лучшая открытая MiMo-V2.6-Pro — 46. Но MiMo огромная, на ноутбук не влезет. Открытая модель, которая помещается на одну игровую видеокарту, Qwen3.8 27B, — 34. Для простых задач этого хватает, для сложных рассуждений нет.",
                      "Cons: quality. The independent Artificial Analysis ranking (index v4.3, October 2026): the best closed model, Claude Opus 5.5, scores 58; the best open model, MiMo-V2.6-Pro, 46. But MiMo is huge and will not fit a laptop. An open model that fits one gaming GPU, Qwen3.8 27B, scores 34. Enough for simple tasks, not for hard reasoning."),
                    t("Вывод: локальная модель хороша для повторяющихся простых задач на чувствительных данных: классифицировать тикеты, вытащить поля из письма, сделать черновик. Для сложного оставляем облако.",
                      "Takeaway: a local model is good for repetitive simple tasks on sensitive data: classify tickets, extract fields from an email, write a draft. Keep the cloud for hard work.")))


def s_layers():
    return dict(min=4, html=f'''
  {head(t("Как это устроено", "How it fits together"), t("Пять частей: файл, движок, железо, сервер, приложение", "Five parts: file, engine, hardware, server, app"), k="violet")}
  <div class="body big" style="margin-top:6px;">
    <div style="margin-top:14px">{parts_diagram()}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:44px;">
      <div class="note" style="--k:var(--violet)">{t("<b>Движок</b> (llama.cpp) умеет «прочитать» файл модели и посчитать ответ. <b>Сервер</b> даёт к нему адрес, как у облачного API.", "<b>The engine</b> (llama.cpp) reads the model file and computes the answer. <b>The server</b> gives it an address, just like a cloud API.")}</div>
      <div class="note" style="--k:var(--amber)">{t("<b>Если тормозит</b>, ищем, какая часть виновата: файл слишком большой? нет видеокарты? Не «модель плохая».", "<b>If it is slow</b>, find which part is to blame: file too big? no GPU? Not “the model is bad”.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Когда мы пользуемся ChatGPT, всё спрятано. Локально видно пять частей. Файл модели: веса, формат GGUF. Движок: программа, которая умеет его выполнить; почти везде это llama.cpp. Железо: процессор, видеокарта и их память. Сервер: даёт модели адрес localhost:1234, чтобы к ней могли обращаться другие программы. И ваше приложение: окно чата или скрипт на Python.",
                      "⏱ 4 min. When we use ChatGPT everything is hidden. Locally you see five parts. The model file: weights, GGUF format. The engine: a program that can run it; almost everywhere that is llama.cpp. Hardware: CPU, GPU and their memory. The server: gives the model an address, localhost:1234, so other programs can call it. And your app: a chat window or a Python script."),
                    t("LM Studio собирает первые четыре части в одну программу с кнопками. Ollama делает то же из командной строки. Зачем знать про части: когда что-то не работает, сразу понятно, где искать. Модель не загружается — файл не влезает в память. Отвечает медленно — считает процессор вместо видеокарты. Приложение получает ошибку — неправильный адрес или имя модели.",
                      "LM Studio packs the first four parts into one program with buttons. Ollama does the same from the command line. Why know the parts: when something breaks you know where to look. The model will not load — the file does not fit in memory. It answers slowly — the CPU is computing instead of the GPU. The app gets an error — wrong address or model name.")))


def s_quant():
    sizes = [("Q2_K", 3.41, "red"), ("Q3_K_M", 4.35, "amber"), ("Q4_K_M", 5.35, "green"), ("Q5_K_M", 6.25, "cyan"),
             ("Q6_K", 7.22, "cyan"), ("Q8_0", 9.35, "cyan"), ("BF16", 17.59, "violet")]
    sub = {"Q2_K": t("2 бита · заметно хуже", "2 bits · noticeably worse"), "Q3_K_M": t("3 бита", "3 bits"),
           "Q4_K_M": t("4 бита · старт по умолчанию", "4 bits · default start"), "Q5_K_M": t("5 бит", "5 bits"),
           "Q6_K": t("6 бит", "6 bits"), "Q8_0": t("8 бит · почти как оригинал", "8 bits · close to original"),
           "BF16": t("16 бит · оригинал", "16 bits · original")}
    ch = bars([(n, sub[n], v, k) for n, v, k in sizes], 0, 18.5, gb,
              ticks=[(0, "0"), (5, "5"), (10, "10"), (15, t("15 ГБ", "15 GB"))], label_w=300)
    return dict(min=5, html=f'''
  {head(t("Размер файла", "File size"), t("Сжатие (квантизация): та же модель <span style='white-space:nowrap'>в 2–5 раз</span> меньше, чуть хуже качество", "Quantisation: the same model <span style='white-space:nowrap'>2–5×</span> smaller, slightly lower quality"), k="green")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="stack" style="gap:10px;">
        <div class="prompt-label">{t("Granite 4.2 8B: размеры файлов на Hugging Face", "Granite 4.2 8B: file sizes on Hugging Face")}</div>
        {ch}
      </div>
      <div class="stack" style="gap:22px;">
        <div class="stat" style="--k:var(--green)"><div class="n">Q4</div><div class="d">{t("начинаем с 4 бит: так советует и документация LM Studio", "start with 4 bits; the LM Studio docs say the same")}</div></div>
        <div class="note" style="--k:var(--cyan)">{t("<b>Как это работает:</b> каждое число модели хранят грубее, меньшим числом бит. Как JPEG для фото: файл меньше, детали чуть теряются.", "<b>How it works:</b> each number in the model is stored more coarsely, with fewer bits. Like JPEG for photos: a smaller file, slightly fewer details.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. На Hugging Face мы видели много файлов одной модели. Буква Q и число — это квантизация, по-простому сжатие. Оригинал хранит каждое число модели в 16 битах: для Granite 8B это 17,6 ГБ. Если хранить каждое число грубее, в 8 битах, файл 9,4 ГБ; в 4 битах — 5,4 ГБ, втрое меньше оригинала.",
                      "⏱ 5 min. On Hugging Face we saw many files for one model. The letter Q and a number mean quantisation, in plain words compression. The original stores each number in 16 bits: 17.6 GB for Granite 8B. Store each number more coarsely, in 8 bits, and the file is 9.4 GB; in 4 bits, 5.4 GB, a third of the original."),
                    t("Цена сжатия — качество. 8 бит почти неотличимы от оригинала. 4 бита — разумный компромисс, с него советует начинать и документация LM Studio. 2–3 бита заметно хуже: модель чаще путается. Буквы K_M в названии — вариант метода сжатия; для старта просто берите Q4_K_M.",
                      "The cost of compression is quality. 8 bits are nearly indistinguishable from the original. 4 bits are a sensible compromise, and the LM Studio docs recommend starting there. 2–3 bits are noticeably worse: the model gets confused more often. The K_M letters are a variant of the method; to start, just take Q4_K_M."),
                    t("Аналогия: фото в JPEG. При высоком качестве разницы не видно, при сильном сжатии появляются квадратики. Правило: берите самый крупный файл, который комфортно влезает в память, но не меньше Q4.",
                      "Analogy: a JPEG photo. At high quality you see no difference; at heavy compression you see blocks. Rule: take the largest file that fits comfortably in memory, but no smaller than Q4.")))


def s_fit():
    models = [("Granite 4.2 3B", "IBM", 2.24),
              ("Qwen3.5 4B", "Alibaba", 2.74),
              ("Granite 4.2 8B", "IBM", 5.35),
              ("Qwen3.5 9B", "Alibaba", 5.63),
              ("Gemma 4 12B", "Google", 7.38),
              ("gpt-oss-20b", "OpenAI", 12.11),
              ("Qwen3.8 27B", "Alibaba", 16.81)]
    mem = [(6, "green"), (16, "amber"), (24, "violet")]
    hi, lw = 26.0, 250
    rows = ""
    for lab, sub, v in models:
        k = next(c for m, c in mem if v * 1.25 <= m)  # colour = the smallest memory line it fits under
        p1, p2 = 100 * v / hi, 100 * v * 1.25 / hi
        rows += (f'<div class="br" style="--k:var(--{k});grid-template-columns:{lw}px 1fr"><div class="bl">{lab}<small>{sub}</small></div>'
                 f'<div class="bt"><div class="bf" style="width:{p1:.1f}%;position:absolute;left:0;top:0;border-radius:6px 0 0 6px"></div>'
                 f'<div style="position:absolute;left:{p1:.1f}%;width:{p2 - p1:.1f}%;top:0;height:100%;border-radius:0 6px 6px 0;'
                 f'background:repeating-linear-gradient(135deg,var(--k) 0 4px,transparent 4px 9px);opacity:.75"></div>'
                 f'<div class="bv" style="left:{p2:.1f}%;z-index:3;background:var(--surface-card);border:1px solid var(--line);border-radius:6px;padding:1px 8px;margin-left:8px">{gb(v)}</div></div></div>')
    ticks = "".join(f'<span style="left:{100 * x / hi:.1f}%">{x}</span>' for x in (0, 6, 12, 16, 24))
    rows += f'<div class="axis" style="grid-template-columns:{lw}px 1fr"><div></div><div>{ticks}</div></div>'
    vram = t(" ГБ VRAM", " GB VRAM")
    lines = "".join(
        f'<div class="vline" style="left:calc({lw + 16}px + (100% - {lw + 16}px) * {v / hi:.4f});--k:var(--{k})">'
        f'<span style="{"left:auto;right:6px" if v == 24 else ""}">{v}{vram if v == 24 else t(" ГБ", " GB")}</span></div>'
        for v, k in mem)
    return dict(min=5, html=f'''
  {head(t("Влезет ли", "Will it fit"), t("Файл модели плюс запас на разговор должен влезть в память видеокарты", "The model file plus room for the conversation must fit the GPU memory"), k="cyan")}
  <div class="body big" style="margin-top:4px;">
    <div class="row" style="grid-template-columns:1.7fr 1fr;gap:40px;align-items:start;flex:none;margin-top:16px">
      <div class="stack" style="gap:10px;">
        <div class="prompt-label">{t("Файл Q4_K_M + запас 25% (штриховка) · цвет = наименьшая видеокарта, куда модель влезает", "Q4_K_M file + 25% margin (hatched) · colour = the smallest GPU it fits")}</div>
        <div class="bars" style="position:relative;padding-top:40px">{rows}{lines}</div>
      </div>
      <div class="stack" style="gap:22px;">
        <div class="stat" style="--k:var(--amber)"><div class="n">+25%</div><div class="d">{t("к файлу: память на контекст, то есть историю разговора (обычно 20–30%)", "on top of the file: memory for the context, the conversation history (usually 20–30%)")}</div></div>
        <div class="note" style="--k:var(--green)">{t("Память видеокарты (VRAM): <b style='color:var(--green)'>6&nbsp;ГБ</b> → до 4B · <b>8&nbsp;ГБ</b> → до 9B · <b style='color:var(--amber)'>16&nbsp;ГБ</b> → до 12B (20B впритык) · <b style='color:var(--violet)'>24&nbsp;ГБ</b> → до 27B.", "GPU memory (VRAM): <b style='color:var(--green)'>6&nbsp;GB</b> → up to 4B · <b>8&nbsp;GB</b> → up to 9B · <b style='color:var(--amber)'>16&nbsp;GB</b> → up to 12B (20B just fits) · <b style='color:var(--violet)'>24&nbsp;GB</b> → up to 27B.")}</div>
        <div class="note" style="--k:var(--red)">{t("Без видеокарты модель живёт в обычной памяти: влезет, но будет медленно. Берите 3–4B.", "Without a GPU the model lives in system RAM: it fits, but runs slowly. Take 3–4B.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Главный вопрос новичка: какая модель влезет в мой компьютер. Сплошная полоска — реальный размер файла в 4 битах, штриховка — запас 25% на контекст, то есть на историю разговора и вложенные документы. Вертикальные линии — память видеокарты (её называют VRAM): 6 ГБ у игровой видеокарты ноутбука (как RTX 3060 Laptop), 16 ГБ у видеокарты среднего класса, 24 ГБ у RTX 4090.",
                      "⏱ 5 min. The beginner’s main question: which model fits my computer. The solid bar is the real 4-bit file size; the hatching is a 25% margin for the context, meaning the conversation history and attached documents. The vertical lines are GPU memory (called VRAM): 6 GB on a laptop gaming GPU (like the RTX 3060 Laptop), 16 GB on a mid-range card, 24 GB on an RTX 4090."),
                    t("Читаем так: если полоска вместе со штриховкой левее линии, модель целиком влезает в эту видеокарту; цвет полоски — самая маленькая из трёх видеокарт, куда она влезает. 6 ГБ — модели до 4B. 8 ГБ (частый вариант в ноутбуках, линии на графике нет) — до 9B: Granite 8B и Qwen3.5 9B с запасом занимают около 7 ГБ. 16 ГБ — до 12B, а gpt-oss-20b впритык. 24 ГБ — до 27B. Если модель не влезает в видеокарту целиком, LM Studio положит часть в обычную память, но скорость упадёт в разы.",
                      "Read it like this: if the bar plus hatching is left of a line, the model fits that GPU entirely; the bar colour is the smallest of the three GPUs it fits. 6 GB — models up to 4B. 8 GB (common in laptops, no line on the chart) — up to 9B: Granite 8B and Qwen3.5 9B take about 7 GB with the margin. 16 GB — up to 12B, with gpt-oss-20b just squeezing in. 24 GB — up to 27B. If the model does not fit the GPU entirely, LM Studio puts part of it in system RAM, but speed drops several times."),
                    t("Ноутбук без видеокарты: модель хранится в обычной памяти, и 16 ГБ хватит даже для 8B, но процессор считает медленно (слайд 8). Поэтому без видеокарты берите 3–4B, Granite 3B или Qwen 4B. Начинайте с самой маленькой модели, которая решает задачу; «самая большая, что влезет» — не цель. LM Studio рекомендует от 16 ГБ памяти, а на Windows — от 4 ГБ видеопамяти; процессор с AVX2 на Windows обязателен.",
                      "A laptop without a GPU: the model sits in system RAM, and 16 GB is enough even for 8B, but the CPU computes slowly (slide 8). So without a GPU take 3–4B, Granite 3B or Qwen 4B. Start with the smallest model that does the job; “the biggest that fits” is not the goal. LM Studio recommends 16 GB of memory or more and, on Windows, 4 GB of VRAM or more; a CPU with AVX2 is required on Windows.")))


def s_speed():
    rows = [(t("Процессор ноутбука", "Laptop CPU"), t("без видеокарты · оценка", "no GPU · estimate"), 10, "red"),
            ("Apple M5", t("базовый Mac", "base Mac"), 32, "amber"),
            ("RTX 4050 Laptop", t("игровой ноутбук", "gaming laptop"), 44, "amber"),
            ("Apple M5 Max", t("топовый Mac", "top Mac"), 120, "green"),
            ("RTX 4090", t("игровая видеокарта · 24 ГБ", "gaming GPU · 24 GB"), 186, "green"),
            ("H100", t("серверная · 80 ГБ", "data centre · 80 GB"), 268, "violet")]
    ch = bars(rows, 0, 290, lambda v: f"{v:.0f}", ticks=[(0, "0"), (100, "100"), (200, "200")], label_w=300)
    return dict(min=4, html=f'''
  {head(t("Скорость", "Speed"), t("Видеокарта отвечает в 2–25 раз быстрее процессора", "A GPU answers 2–25× faster than a CPU"), t("Токенов в секунду (токен ≈ часть слова), модель 7B в 4 битах, llama.cpp. Человек читает ≈ 4–7 токенов в секунду.", "Tokens per second (a token ≈ part of a word), 7B model at 4 bits, llama.cpp. People read ≈ 4–7 tokens per second."), k="amber")}
  <div class="body big" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.6fr 1fr;gap:44px;align-items:center;flex:none;margin-top:20px">
      {ch}
      <div class="stack" style="gap:22px;">
        <div class="stat" style="--k:var(--green)"><div class="n">{t("≥ 20 т/с", "≥ 20 t/s")}</div><div class="d">{t("комфортно: длинный ответ без ожидания; 10 т/с терпимо только для коротких", "comfortable: long answers without waiting; 10 t/s is bearable only for short ones")}</div></div>
        <div class="note" style="--k:var(--amber)">{t("Числа ориентировочные: зависят от модели, длины разговора и настроек. Свою скорость LM Studio показывает под каждым ответом.", "Numbers are approximate: they depend on the model, conversation length and settings. LM Studio shows your own speed under each answer.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Скорость меряют в токенах в секунду; токен — кусочек слова, как в L02. Данные из открытых замеров llama.cpp для модели на 7 миллиардов параметров в 4 битах; для 8B умножайте примерно на 0,7. Процессор ноутбука без видеокарты — порядка 5–15 токенов в секунду, это наша оценка: медленно, но для коротких ответов терпимо.",
                      "⏱ 4 min. Speed is measured in tokens per second; a token is a piece of a word, as in L02. The data are open llama.cpp measurements for a 7-billion-parameter model at 4 bits; for 8B multiply by about 0.7. A laptop CPU without a GPU gives roughly 5–15 tokens per second, our estimate: slow, but bearable for short answers."),
                    t("Игровой ноутбук с RTX 4050 — около 44, базовый Mac M5 — 32, топовый M5 Max — 120 (у Mac видеокарта встроена в процессор и делит с ним память). Видеокарта RTX 4090 — 186, серверная H100 — 268; обе можно арендовать, это вторая часть урока. Человек читает примерно 4–7 токенов в секунду, поэтому от 20 и выше чат ощущается живым. Для пакетной обработки, например 10 000 писем за ночь, скорость важнее: там и пригодится аренда видеокарты.",
                      "A gaming laptop with an RTX 4050 gives about 44, a base M5 Mac 32, a top M5 Max 120 (on a Mac the GPU is built into the chip and shares its memory). An RTX 4090 gives 186, a server H100 268; both can be rented, which is the second half of the lesson. People read about 4–7 tokens per second, so from 20 upwards chat feels live. For batch work, such as 10,000 emails overnight, speed matters more, and that is where renting a GPU helps."),
                    t("Почему видеокарта быстрее: модель — это огромное число умножений, а видеокарта делает тысячи умножений одновременно и у неё очень быстрая память.",
                      "Why the GPU is faster: a model is a huge number of multiplications, and a GPU does thousands of them at once and has very fast memory.")))


def s_lmstudio():
    app = shot("lmstudio_app", marks=[(1, 6.0, 6.0, "cyan"), (4, 10.8, 12.0, "violet"), (2, 6.0, 21.0, "green"), (3, 23.5, 94.0, "amber")],
               boxes=[(0.4, 5.2, 2.8, 4.4, "cyan"), (0.4, 9.4, 2.8, 4.4, "violet"), (0.4, 17.8, 2.8, 4.4, "green"), (4.5, 91.0, 17.5, 6.5, "amber")])
    return dict(min=5, html=f'''
  {head("LM Studio", t("LM Studio: чат как ChatGPT, но модель работает у вас", "LM Studio: a chat like ChatGPT, but the model runs on your machine"), k="cyan")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.6fr 1fr;gap:36px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;">
        {app}
        <div class="small" style="font-size:17px">{t("Изображение: LM Studio / Element Labs, блог версии 0.4.0", "Image: LM Studio / Element Labs, 0.4.0 release blog")}</div>
      </div>
      <div class="stack" style="gap:20px;">
        {legend([(1, "cyan", t("<b>Chat</b> — разговор с моделью", "<b>Chat</b> — talk to the model")),
                 (2, "green", t("<b>Discover</b> — поиск и скачивание моделей с Hugging Face", "<b>Discover</b> — find and download models from Hugging Face")),
                 (3, "amber", t("<b>Выбор модели</b>: какую загрузить в память", "<b>Model picker</b>: which one to load into memory")),
                 (4, "violet", t("<b>Developer</b> — локальный сервер (слайд 11)", "<b>Developer</b> — the local server (slide 11)"))])}
        <div class="note" style="--k:var(--green)">{t("Бесплатно, в том числе для работы. Windows, Mac (Apple Silicon), Linux. Версия 0.4.26.", "Free, including for work. Windows, Mac (Apple Silicon), Linux. Version 0.4.26.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. LM Studio — бесплатное приложение для запуска открытых моделей на своём компьютере. Выглядит как ChatGPT: слева узкая панель разделов, в центре чат, под полем ввода выбор модели. Отличие: модель скачана на ваш диск и считает ваш процессор или видеокарта. На скриншоте сразу два разговора с моделью GLM-4.7-Flash.",
                      "⏱ 5 min. LM Studio is a free app for running open models on your own computer. It looks like ChatGPT: a narrow section bar on the left, the conversation in the middle, the model picker under the input box. The difference: the model is downloaded to your disk and computed by your CPU or GPU. The screenshot shows two chats with GLM-4.7-Flash side by side."),
                    t("Главные разделы. Chat — разговор. Discover — поиск моделей прямо из Hugging Face; LM Studio сам подсказывает, какие файлы влезут в вашу память. My Models — что уже скачано. Developer — локальный сервер, о нём через слайд. С июля 2025 LM Studio бесплатна и для работы в компании. Текущая версия 0.4.26 (октябрь 2026).",
                      "Main sections. Chat — the conversation. Discover — model search straight from Hugging Face; LM Studio tells you which files fit your memory. My Models — what is already downloaded. Developer — the local server, two slides from now. Since July 2025 LM Studio is free for work use too. The current version is 0.4.26 (October 2026)."),
                    t("Не путайте: на странице загрузки lmstudio.ai сейчас первым предлагается LM Studio Bionic — это отдельный агент (вышел в июле 2026). Для урока нужна обычная LM Studio, ссылка ниже на странице загрузки. Альтернатива — Ollama, бесплатная, лицензия MIT; ей удобно управлять командами.",
                      "Do not confuse: the lmstudio.ai download page now offers LM Studio Bionic first — a separate agent app (released July 2026). The lesson needs the classic LM Studio, further down the download page. The alternative is Ollama, free, MIT licence; it is easy to drive with commands.")))


def s_demo():
    st = [(t("Найти", "Find"), t("Discover → «granite-4.2-3b»", "Discover → “granite-4.2-3b”")),
          (t("Скачать", "Download"), "Q4_K_M · 2,2 ГБ" if LANG == "ru" else "Q4_K_M · 2.2 GB"),
          (t("Загрузить", "Load"), t("выбрать модель в чате", "pick the model in Chat")),
          (t("Спросить", "Ask"), t("промпт ниже", "the prompt below")),
          (t("Посмотреть", "Look"), t("токенов/с под ответом", "tokens/s under the answer"))]
    n = len(st)
    dots = "".join(
        f'<div style="position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px">'
        + (f'<div style="position:absolute;top:31px;left:calc(-50% + 36px);right:calc(50% + 36px);border-top:3px solid var(--green);opacity:.6"></div>' if i else "")
        + f'<div style="width:64px;height:64px;border-radius:50%;background:var(--green);color:#0b0f17;font:800 30px/64px var(--display)">{i + 1}</div>'
        f'<div style="font:800 27px/1.2 var(--display);color:var(--fg)">{a}</div><div style="font:500 20px/1.3 var(--body);color:var(--muted)">{b}</div></div>'
        for i, (a, b) in enumerate(st))
    flow = f'<div style="display:grid;grid-template-columns:repeat({n},1fr);gap:16px">{dots}</div>'
    prompt = t("Тикет: «Клиент не может сбросить пароль после смены телефона».\nВерни JSON: проблема, срочность (низкая/средняя/высокая), следующий шаг.",
               "Ticket: “The customer cannot reset their password after changing phones.”\nReturn JSON: issue, urgency (low/medium/high), next_step.")
    keys = t(("проблема", "срочность", "следующий_шаг"), ("issue", "urgency", "next_step"))
    vals = t(("сброс пароля после смены телефона", "средняя", "проверить личность и сбросить вход вручную"),
             ("password reset after a phone change", "medium", "verify identity and reset sign-in manually"))
    answer = "{\n" + ",\n".join(f'  "<span style="color:#7dd3fc">{k_}</span>": "{v_}"' for k_, v_ in zip(keys, vals)) + "\n}"
    return dict(min=5, html=f'''
  {head(t("Демо 1", "Demo 1"), t("Демо: скачать маленькую модель и задать ей рабочий вопрос", "Demo: download a small model and ask it a work question"), k="green")}
  <div class="body">
    {flow}
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;flex:none;margin-top:44px;align-items:stretch;">
      <div><div class="prompt-label">{t("Промпт", "Prompt")}</div><pre class="code" style="font-size:21px;white-space:pre-wrap;line-height:1.5">{prompt}</pre></div>
      <div><div class="prompt-label" style="color:var(--green)">{t("Образец хорошего ответа (JSON)", "What a good answer looks like (JSON)")}</div><pre class="code" style="font-size:21px;white-space:pre-wrap;line-height:1.5;border-color:var(--green)">{answer}</pre></div>
    </div>
    <div class="note" style="margin-top:30px;font-size:22px;--k:var(--cyan)">{t("<b>Что замечаем:</b> ответ приходит без интернета; под ответом скорость в токенах в секунду; в диспетчере задач растёт память.", "<b>What to notice:</b> the answer arrives with no internet; the speed in tokens/s is under the answer; memory use rises in Task Manager.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Живая демонстрация. До урока скачайте модель granite-4.2-3b в Q4_K_M (2,2 ГБ), чтобы не зависеть от интернета. Пять шагов: Discover, поиск по имени, кнопка Download у файла Q4_K_M, затем в Chat выбор модели в нижнем меню (она загружается в память за несколько секунд) и промпт. Справа на слайде образец хорошего ответа: сравните с тем, что выдала модель. Запасной план: если Wi-Fi медленный, показывайте на заранее скачанной модели.",
                      "⏱ 5 min. Live demo. Before class download granite-4.2-3b at Q4_K_M (2.2 GB) so you do not depend on the internet. Five steps: Discover, search by name, Download on the Q4_K_M file, then in Chat pick the model in the bottom menu (it loads into memory in a few seconds) and send the prompt. On the right of the slide is what a good answer looks like: compare it with what the model returns. Fallback: if the Wi-Fi is slow, demo with the model downloaded in advance."),
                    t("Промпт рабочий, из L03: вытащить из тикета проблему, срочность и следующий шаг в JSON. Для показа можно выключить Wi-Fi перед отправкой: модель всё равно ответит. Покажите строку со скоростью под ответом (токены в секунду) и откройте диспетчер задач: видно, сколько памяти заняла модель.",
                      "The prompt is a work task from L03: extract the issue, urgency and next step from a ticket as JSON. For effect, turn off Wi-Fi before sending: the model still answers. Point at the speed line under the answer (tokens per second) and open Task Manager: you can see how much memory the model took."),
                    t("Вопрос в чат: ответ хуже или лучше, чем у ChatGPT? Обычно маленькая модель справляется с такой простой задачей, но может перепутать формат. Это нормальная цена за 2 ГБ.",
                      "Question for the chat: is the answer worse or better than ChatGPT’s? A small model usually handles such a simple task but may get the format wrong. That is a fair price for 2 GB.")))


def s_server():
    code = ('from openai import OpenAI\n\nticket = "Клиент не может сбросить пароль"\nclient = OpenAI(\n    base_url="<span style=\'color:var(--green)\'>http://localhost:1234/v1</span>",\n'
            '    api_key="lm-studio")                # для облака: ваш ключ\n\nr = client.chat.completions.create(\n'
            '    model="<span style=\'color:var(--green)\'>granite-4.2-3b</span>",\n    messages=[{"role": "user", "content": ticket}])\nprint(r.choices[0].message.content)')
    if LANG == "en":
        code = code.replace("# для облака: ваш ключ", "# for the cloud: your key").replace("Клиент не может сбросить пароль", "Customer cannot reset password")
    cfg = lambda k, h, a, m: f'<div class="note" style="--k:var(--{k})"><b>{h}</b><br><code>{a}</code><br><code>{m}</code></div>'
    return dict(min=5, html=f'''
  {head(t("Локальный сервер", "Local server"), t("Включили сервер — и модель отвечает вашему коду, как облачный API", "Turn on the server and the model answers your code like a cloud API"), k="violet")}
  <div class="body big" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:40px;align-items:start;flex:none;margin-top:16px">
      <div><div class="prompt-label">{t("Python, тот же код, что в L03", "Python, the same code as in L03")}</div><pre class="code" style="font-size:21px;line-height:1.55">{code}</pre></div>
      <div class="stack" style="gap:22px;">
        <div class="prompt-label">{t("Меняются адрес и имя модели (и ключ)", "The address and model name change (and the key)")}</div>
        {cfg("violet", t("Облако (OpenAI)", "Cloud (OpenAI)"), "https://api.openai.com/v1", "gpt-5.4-mini")}
        {cfg("green", t("Ноутбук (LM Studio)", "Laptop (LM Studio)"), "http://localhost:1234/v1", "granite-4.2-3b")}
        {cfg("green", t("Ноутбук (Ollama)", "Laptop (Ollama)"), "http://localhost:11434/v1", "granite4.2:3b")}
      </div>
    </div>
    <div class="note" style="margin-top:22px;--k:var(--cyan)">{t("В LM Studio: вкладка <b>Developer → Start server</b>. Адрес <code>localhost</code> значит «этот компьютер».", "In LM Studio: <b>Developer → Start server</b>. The address <code>localhost</code> means “this computer”.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Самый важный слайд для тех, кто программирует. В LM Studio на вкладке Developer есть переключатель Start server. После этого модель доступна по адресу localhost:1234 и понимает те же запросы, что и OpenAI API: chat/completions, responses, embeddings. Также есть совместимость с API Anthropic.",
                      "⏱ 5 min. The key slide for those who code. LM Studio’s Developer tab has a Start server toggle. After that the model is available at localhost:1234 and understands the same requests as the OpenAI API: chat/completions, responses, embeddings. There is also Anthropic API compatibility."),
                    t("Слева код из L03. Меняются две строки, выделены зелёным: адрес (base_url) и имя модели. Ключ для локального сервера не нужен, библиотека просто требует какую-то строку. Окончание /v1 в адресе — номер версии API, как у OpenAI; пишем как есть. У Ollama адрес другой, localhost:11434, но принцип тот же. Поэтому адрес и имя модели держим в настройках (файл .env), а не в коде: тогда переезд из облака на ноутбук или в Runpod — это правка адреса и имени модели, без изменения кода.",
                      "On the left is the L03 code. Two lines change, highlighted in green: the address (base_url) and the model name. The local server needs no key; the library just wants some string. The /v1 at the end of the address is the API version, as at OpenAI; keep it as is. Ollama uses a different address, localhost:11434, but the idea is the same. So keep the address and model name in settings (a .env file), not in code: moving from the cloud to a laptop or to Runpod then means editing the address and model name, not the code."),
                    t("Оговорка: «совместимый» не значит «одинаковый». Маленькая модель хуже следует формату JSON и может не поддерживать вызов инструментов. Проверяйте на своей задаче.",
                      "Caveat: “compatible” does not mean “identical”. A small model follows the JSON format less reliably and may not support tool calling. Test on your own task.")))


def s_agent():
    prompt = t(
        "Установи на этот компьютер Ollama (официальный установщик с ollama.com) и запусти открытую модель granite4.2:3b.\n"
        "1. Проверь видеокарту и её память, оперативную память и свободное место на диске. Скажи, какая модель подойдёт.\n"
        "2. Скачай модель и задай ей вопрос: «Кратко: что такое квантизация?»\n"
        "3. Замерь скорость (токенов в секунду) и сколько памяти заняла модель.\n"
        "4. Покажи, по какому адресу работает локальный сервер, и пришли пример запроса на Python.\n"
        "5. Ничего не открывай в сеть, сервер только на localhost.",
        "Install Ollama on this computer (official installer from ollama.com) and run the open model granite4.2:3b.\n"
        "1. Check the GPU and its memory, system RAM and free disk. Tell me which model fits.\n"
        "2. Download the model and ask it: “Briefly: what is quantisation?”\n"
        "3. Measure the speed (tokens per second) and how much memory the model uses.\n"
        "4. Show the local server address and give me an example request in Python.\n"
        "5. Expose nothing to the network; the server stays on localhost only.")
    return dict(min=4, html=f'''
  {head(t("Практика с агентом", "Hands-on with an agent"), t("Агент разработки ставит модель за вас и сам меряет скорость", "A coding agent installs the model for you and measures the speed"), k="violet")}
  <div class="body big" style="margin-top:8px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:40px;align-items:start;flex:none;margin-top:16px">
      <div><div class="prompt-label">{t("Промпт для агента разработки: Codex в ChatGPT или Antigravity — бесплатно с лимитом, Claude Code — платно", "Prompt for a coding agent: Codex in ChatGPT or Antigravity (free, with limits), Claude Code (paid)")}</div><pre class="code" style="font-size:21px;line-height:1.55;white-space:pre-wrap">{prompt}</pre></div>
      <div class="stack" style="gap:30px;">
        <div class="note" style="--k:var(--cyan)">{t("<b>Ollama</b> — похожая программа, которой удобно управлять командами: <code>ollama run granite4.2:3b</code>.", "<b>Ollama</b> — a similar tool that is easy to drive with commands: <code>ollama run granite4.2:3b</code>.")}</div>
        <div class="note" style="--k:var(--green)">{t("Агент проверит железо, поставит программу, скачает модель и принесёт отчёт: скорость, память, адрес сервера.", "The agent checks the hardware, installs the program, downloads the model and reports back: speed, memory, server address.")}</div>
        <div class="note" style="--k:var(--red)">{t("Агент ставит программы на ваш компьютер: читайте, что он предлагает выполнить, и подтверждайте шаги.", "The agent installs software on your computer: read what it proposes to run and approve each step.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Связь с уроками про агентов разработки. Не обязательно ставить всё руками: Codex, Antigravity или Claude Code сделают это по такому промпту. Шаги нумерованы, чтобы агент ничего не пропустил, а пункт 5 запрещает открывать сервер в сеть. Что такое агент разработки и как его выбрать — L16.",
                      "⏱ 4 min. A link to the coding-agent lessons. You do not have to install everything by hand: Codex, Antigravity or Claude Code will do it from a prompt like this. The steps are numbered so the agent skips nothing, and step 5 forbids exposing the server to the network. What a coding agent is and how to choose one: L16."),
                    t("Почему Ollama, а не LM Studio: в Ollama всё можно сделать командами (окно чата у неё тоже есть, но оно не обязательно), поэтому агенту проще. Это открытая программа с лицензией MIT; версия 0.40.5 от 14 октября 2026. Сервер Ollama работает на localhost:11434 и тоже понимает запросы в стиле OpenAI. У LM Studio для командной строки есть утилита lms, а для серверов без экрана — llmster.",
                      "Why Ollama rather than LM Studio: everything in Ollama can be done with commands (it also has a chat window, but you don't need it), which is easier for an agent. It is open-source under the MIT licence; version 0.40.5 from 14 October 2026. The Ollama server runs on localhost:11434 and also understands OpenAI-style requests. LM Studio has the lms command-line tool, and llmster for servers without a screen."),
                    t("Важно: агент будет предлагать команды установки. Читайте их перед подтверждением; ставим только с официальных сайтов. Это вариант для домашнего задания по желанию.",
                      "Important: the agent will propose install commands. Read them before approving; install only from official sites. This is an optional homework path.")))


def s_private():
    rows = [("green", t("Модель считает на вашем компьютере", "The model computes on your machine"), t("сам текст запроса никуда не уходит", "the request text goes nowhere")),
            ("amber", t("Скачивание моделей и обновления", "Model downloads and updates"), t("идут в интернет; качайте из официальных источников", "go to the internet; download from official sources")),
            ("amber", t("Плагины и веб-поиск", "Plug-ins and web search"), t("могут отправлять данные наружу", "may send data outside")),
            ("red", t("Сервер открыт в сеть (не localhost)", "Server exposed to the network (not localhost)"), t("к модели могут обратиться другие; включайте Require Authentication (вход по токену)", "others can reach the model; turn on Require Authentication (token login)"))]
    lr = "".join(f'<div class="lrow" style="--k:var(--{k});border:none;background:none;padding:12px 0"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for k, h, d in rows)
    return dict(min=4, html=f'''
  {head(t("Безопасность", "Security"), t("«Локально» ещё не значит «приватно»: смотрим весь путь данных", "“Local” does not automatically mean “private”: check the whole data path"), k="red")}
  <div class="body big" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:56px;align-items:center;flex:none;margin-top:24px">
      <div class="light" style="gap:46px">{lr}</div>
      <div class="stack" style="gap:20px;">
        <div class="plaque" style="font-size:22px">{t("<b>Правило урока:</b> сервер только на <code>localhost</code>, модели только из официальных источников (Hugging Face, ollama.com) от известных авторов, документы клиентов — только с разрешения.", "<b>Class rule:</b> server on <code>localhost</code> only, models only from official sources (Hugging Face, ollama.com) by known publishers, client documents only with permission.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Лицензия модели тоже часть безопасности: нельзя «случайно» встроить некоммерческую модель в продукт.", "The model licence is part of security too: do not “accidentally” ship a non-commercial model in a product.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Частое заблуждение: поставил модель локально — значит всё приватно. Сама генерация действительно остаётся на компьютере. Но вокруг неё есть путь данных. Скачивание модели и обновления — это интернет. Если подключить плагины (в LM Studio это MCP-серверы) или веб-поиск, они могут отправлять данные наружу.",
                      "⏱ 4 min. A common mistake: I installed the model locally, so everything is private. The generation itself does stay on the computer. But around it there is a data path. Downloading the model and updates use the internet. If you connect plug-ins (MCP servers in LM Studio) or web search, they may send data out."),
                    t("Самый опасный пункт красный: если в LM Studio включить «Serve on local network», к модели смогут обращаться другие компьютеры в сети. Для этого в настройках сервера есть Require Authentication: доступ только по токену. Для урока и домашнего задания держим сервер только на localhost.",
                      "The most dangerous item is red: if you enable “Serve on local network” in LM Studio, other computers on the network can reach the model. For this case the server settings have Require Authentication: access by token only. For class and homework keep the server on localhost only."),
                    t("И про источник: файлы моделей качаем у известных авторов (IBM, Google, Alibaba Qwen, Microsoft, OpenAI, сообщество lmstudio-community). Неизвестные перепаковки могут быть испорчены.",
                      "And the source: download model files from known publishers (IBM, Google, Alibaba Qwen, Microsoft, OpenAI, the lmstudio-community group). Unknown repacks may be tampered with.")))


def s_market():
    cols = [
        ("green", t("Видеокарта до 8 ГБ", "GPU up to 8 GB"), [("Granite 4.2 3B · 8B", "Apache-2.0"), ("Qwen3.5 4B · 9B", "Apache-2.0"), (t("Gemma 4 E4B <small>(≈4B, для телефонов и ноутбуков)</small>", "Gemma 4 E4B <small>(≈4B, for phones and laptops)</small>"), "Apache-2.0")]),
        ("amber", t("Видеокарта 16–24 ГБ", "16–24 GB GPU"), [("Gemma 4 12B", "Apache-2.0"), ("gpt-oss-20b", "Apache-2.0"), ("Qwen3.8 27B", "Apache-2.0")]),
        ("violet", t("Сервер, много видеокарт", "Server, many GPUs"), [("DeepSeek V4.1", "MIT"), ("gpt-oss-120b", "Apache-2.0"), ("Llama 4", t("своя лицензия", "custom licence"))]),
    ]
    html_cols = ""
    for k, h, ms in cols:
        items = "".join(f'<li class="mli" style="--k:var(--{k})"><i></i><span>{n}<em>{lic}</em></span></li>' for n, lic in ms)
        html_cols += (f'<div><div class="mhead" style="--k:var(--{k})">{h}</div>'
                      f'<ul class="mlist">{items}</ul></div>')
    return dict(min=4, html=f'''
  {head(t("Рынок • октябрь 2026", "Market • October 2026"), t("Открытые модели по размеру: что запускать на чём", "Open models by size: what runs where"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:repeat(3,1fr);gap:48px;flex:none;align-items:start;margin-top:20px">{html_cols}</div>
    <div class="note" style="margin-top:40px;font-size:23px;--k:var(--cyan)">{t("Почти всё под Apache-2.0. Для старта: <b>Granite 4.2 3B</b>; умнее, но нужна видеокарта: <b>Qwen3.5 9B</b> или <b>Gemma 4 12B</b>.", "Almost everything is Apache-2.0. To start: <b>Granite 4.2 3B</b>; smarter but needs a GPU: <b>Qwen3.5 9B</b> or <b>Gemma 4 12B</b>.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Карта по размеру, а не по рейтингу: что вообще можно запустить на вашем железе. Почти всё в зелёной зоне под лицензией Apache-2.0: можно в работе. Ноутбук: Granite 4.2 от IBM (3B и 8B), Qwen3.5 от Alibaba (4B и 9B), Gemma 4 от Google (E4B и 12B), Ministral 3 от Mistral; Phi-4 от Microsoft (14B, ≈ 9 ГБ) уже требует видеокарту на 12–16 ГБ.",
                      "⏱ 4 min. A map by size, not by ranking: what you can run on your hardware at all. Almost everything here is Apache-2.0: fine for work. Laptop: IBM Granite 4.2 (3B and 8B), Alibaba Qwen3.5 (4B and 9B), Google Gemma 4 (E4B and 12B), Mistral Ministral 3; Microsoft Phi-4 (14B, ≈ 9 GB) already needs a 12–16 GB GPU."),
                    t("Одна видеокарта на 16–24 ГБ: gpt-oss-20b от OpenAI (младшая из двух открытых моделей OpenAI, 12 ГБ), Qwen3.8 27B, Gemma 4 31B, Granite 4.2 30B, Muse Glimmer 30B — новая открытая модель Meta. Сервер: DeepSeek V4.1 и Llama 4 огромные, их запускают на кластере или берут через API. У Llama 4 и Qwen3.8-Flash-Next собственные лицензии с условиями: читайте перед использованием.",
                      "One GPU with 16–24 GB: OpenAI’s gpt-oss-20b (the smaller of OpenAI’s two open models, 12 GB), Qwen3.8 27B, Gemma 4 31B, Granite 4.2 30B, Muse Glimmer 30B — Meta’s new open model. Server: DeepSeek V4.1 and Llama 4 are huge; they run on a cluster or via an API. Llama 4 and Qwen3.8-Flash-Next have custom licences with conditions: read them first."),
                    t("Названия меняются каждые пару месяцев, поэтому учим критерии: размер файла, лицензия, известный автор. Перепроверьте список перед занятием.",
                      "Names change every couple of months, so we teach the criteria: file size, licence, known publisher. Recheck the list before class.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут: пока модель скачивается, можно выпить кофе", "5 minutes: grab a coffee while the model downloads")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: аренда видеокарты в Runpod, цена, как выбрать, домашнее задание.", "Next: renting a GPU on Runpod, price, how to choose, homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт». Можно предложить студентам поставить LM Studio и начать скачивать маленькую модель.",
                              "⏱ 5 min. Press “Start”. You can suggest students install LM Studio and start downloading a small model.")))


def s_limits():
    cards = [("red", t("Не влезает", "Does not fit"), t("модель больше памяти ноутбука", "the model is bigger than the laptop’s memory")),
             ("amber", t("Слишком медленно", "Too slow"), t("10 000 писем за ночь на процессоре не успеть", "10,000 emails overnight is too much for a CPU")),
             ("violet", t("Много пользователей", "Many users"), t("один ноутбук отвечает одному человеку", "one laptop serves one person")),
             ("cyan", t("Нужно 24/7", "Needs 24/7"), t("ноутбук закрывают и уносят домой", "laptops get closed and taken home"))]
    cc = "".join(f'<div class="task" style="--k:var(--{k});padding:30px 30px;min-height:200px;align-content:center"><div><div class="h" style="font-size:34px">{h}</div><div class="d" style="font-size:23px;margin-top:10px">{d}</div></div></div>' for k, h, d in cards)
    return dict(min=3, html=f'''
  {head(t("Предел ноутбука", "Laptop limits"), t("Когда ноутбука мало: четыре признака", "When a laptop is not enough: four signs"), k="amber")}
  <div class="body">
    <div class="tasks" style="gap:28px 32px;margin-top:20px">{cc}</div>
    <div class="note" style="margin-top:40px;font-size:24px;--k:var(--green)">{t("<b>Решение:</b> оставляем ту же модель и тот же код, но переносим расчёт на мощную видеокарту в облаке. Меняются только адрес и имя модели.", "<b>Solution:</b> keep the same model and the same code, but move the computing to a powerful cloud GPU. Only the address and model name change.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Ноутбук хорош для пробы, для одного человека и для работы без интернета. Четыре признака, что пора дальше. Модель не влезает в память. Нужна скорость: например, разобрать 10 000 писем за ночь. Много одновременных пользователей: ноутбук отвечает по очереди. Нужна работа круглосуточно.",
                      "⏱ 3 min. A laptop is good for trying things, for one person and for offline work. Four signs it is time to move on. The model does not fit in memory. You need speed: say, process 10,000 emails overnight. Many simultaneous users: a laptop answers one at a time. It must run around the clock."),
                    t("Тогда не обязательно сразу идти в облачный API. Можно оставить ту же открытую модель, ту же лицензию и тот же код, а арендовать видеокарту. Самый понятный для новичка сервис — Runpod.",
                      "Then you do not have to jump straight to a cloud API. You can keep the same open model, the same licence and the same code, and rent a GPU. The most beginner-friendly service is Runpod.")))


def s_runpod():
    def lane(k, lab, segs, cap):
        cells = "".join(f'<div style="position:absolute;left:{a / 24 * 100:.2f}%;width:{(b - a) / 24 * 100:.2f}%;top:0;bottom:0;background:var(--{k});border-radius:4px;opacity:.9"></div>' for a, b in segs)
        return (f'<div style="display:grid;grid-template-columns:150px 1fr;gap:14px;align-items:center"><div style="font-size:21px;font-weight:700;color:var(--{k})">{lab}</div>'
                f'<div><div style="position:relative;height:34px;background:#121a28;border-radius:6px">{cells}</div><div class="small" style="font-size:18px;margin-top:6px">{cap}</div></div></div>')
    ticks = "".join(f'<span style="position:absolute;left:{h / 24 * 100:.1f}%;transform:translateX(-50%)">{h:02d}:00</span>' for h in (0, 6, 12, 18))
    tl = (lane("violet", "Pod", [(9, 18)], t("включили утром, выключили вечером: платим все 9 часов, даже за обед", "on in the morning, off in the evening: you pay all 9 hours, lunch included"))
          + lane("cyan", "Serverless", [(9.3, 9.6), (10.5, 10.7), (12.2, 12.6), (14.0, 14.2), (16.4, 16.9)], t("видеокарта просыпается на запрос: платим только эти минуты", "the GPU wakes per request: you pay only those minutes"))
          + f'<div style="display:grid;grid-template-columns:150px 1fr;gap:14px"><div></div><div style="position:relative;height:22px;font:17px var(--mono);color:var(--dim)">{ticks}</div></div>')
    return dict(min=5, html=f'''
  {head("Runpod", t("Runpod: видеокарта в аренду с посекундной оплатой, два режима", "Runpod: a GPU rented with per-second billing, two modes"), k="violet")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1fr 1.1fr;gap:40px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;">
        <div class="prompt-label">{t("runpod.io/pricing · Community Cloud · снято 16.10.2026", "runpod.io/pricing · Community Cloud · captured 16.10.2026")}</div>
        {shot("runpod_pricing_community", boxes=[(1.0, 75.0, 98.0, 12.0, "green")])}
        <div class="small" style="font-size:18px">{t("Зелёным: RTX 4090, 24 ГБ — $0.34 в час", "Green: RTX 4090, 24 GB — $0.34 per hour")}</div>
      </div>
      <div class="stack" style="gap:22px;">
        <div class="prompt-label">{t("Один рабочий день бота поддержки", "One working day of a support bot")}</div>
        {tl}
        <div class="note" style="--k:var(--red)">{t("<b>Ловушка:</b> остановленный Pod (Stop) продолжает брать плату за диск. Закончили — удалите (Terminate).", "<b>Trap:</b> a stopped Pod (Stop) still bills for its disk. When you are done, delete it (Terminate).")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Runpod — облако видеокарт с посекундной оплатой. Слева страница цен (обновлена 8 октября, снято 16 октября), режим Community Cloud — компьютеры партнёров: RTX 4090 с 24 ГБ стоит $0.34 в час, RTX 3090 — $0.22. В Secure Cloud, в надёжных дата-центрах, дороже: например, L40S $1.09 против $0.79. Справа один рабочий день бота поддержки в двух режимах.",
                      "⏱ 5 min. Runpod is a GPU cloud billed per second. On the left is the pricing page (updated 8 October, captured 16 October) in Community Cloud mode, partners’ machines: an RTX 4090 with 24 GB costs $0.34 per hour, an RTX 3090 $0.22. Secure Cloud, in certified data centres, costs more: for example an L40S is $1.09 versus $0.79. On the right, one working day of a support bot in both modes."),
                    t("Два режима. Pod — как свой компьютер в облаке: выбрали видеокарту и готовый шаблон (например, PyTorch), подключились через браузер (веб-терминал, JupyterLab) или SSH, поставили Ollama или vLLM и работаете. Платите за каждую секунду, пока он включён, включая время, когда вы ушли пить кофе. Serverless — для приложений: видеокарта просыпается, когда приходит запрос, и засыпает без них. Первый запрос после сна ждёт загрузки модели (холодный старт).",
                      "Two modes. A Pod is like your own computer in the cloud: pick a GPU and a ready template (for example PyTorch), connect via the browser (web terminal, JupyterLab) or SSH, install Ollama or vLLM, and work. You pay for every second it is on, including while you are off getting coffee. Serverless is for apps: the GPU wakes when a request arrives and sleeps without them. The first request after sleep waits for the model to load (cold start)."),
                    t("Главная ловушка для новичков: кнопка Stop не останавливает оплату полностью. Диск остановленного Pod стоит $0.20 за ГБ в месяц. Закончили — Terminate. И помните про лимит расходов: по умолчанию $80 в час на все ресурсы. Для учёбы кладите на счёт небольшую сумму, но следите за ней: при нулевом балансе Pod останавливается, а без сетевого тома (network volume) удаляется вместе с данными. Демо Runpod в этом уроке показываем на скриншотах; самостоятельный запуск — по желанию, он платный.",
                      "The main beginner trap: Stop does not fully stop billing. A stopped Pod’s disk costs $0.20 per GB per month. When done — Terminate. And mind the spend limit: by default it is $80 per hour across all resources. For learning, top up only a small amount, but watch it: at a zero balance the Pod stops, and without a network volume it is deleted together with its data. In this lesson Runpod is shown on screenshots; launching one yourself is optional and paid.")))


def s_cost():
    rows = [("RTX 4090 · 24 ГБ" if LANG == "ru" else "RTX 4090 · 24 GB", "Community", 0.34, "green"),
            ("RTX 5090 · 32 ГБ" if LANG == "ru" else "RTX 5090 · 32 GB", "Community", 0.69, "green"),
            ("L40S · 48 ГБ" if LANG == "ru" else "L40S · 48 GB", "Community", 0.79, "cyan"),
            ("A100 SXM · 80 ГБ" if LANG == "ru" else "A100 SXM · 80 GB", "Community", 1.39, "amber"),
            ("H100 SXM · 80 ГБ" if LANG == "ru" else "H100 SXM · 80 GB", "Community", 2.69, "violet")]
    ch = bars(rows, 0, 3.0, lambda v: f"${v:.2f}", ticks=[(0, "$0"), (1, "$1"), (2, "$2"), (3, "$3")], label_w=300)
    return dict(min=5, html=f'''
  {head(t("Цена", "Price"), t("Аренда видеокарты выгодна, только если она всё время занята", "Renting a GPU only pays off if it is busy all the time"), t("Runpod Pods, цена за час, 16.10.2026", "Runpod Pods, price per hour, 16.10.2026"), k="amber")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.4fr 1fr;gap:44px;align-items:center;flex:none;">
      {ch}
      <div class="stack" style="gap:20px;">
        <div class="stat" style="--k:var(--green)"><div class="n">$0.73 → <span style="color:var(--red)">$7.30</span></div><div class="d">{t("за 1 млн токенов на RTX 4090 (модель 8B, ≈130 токенов/с): занята <b>100%</b> времени → занята <b>10%</b>", "per 1M tokens on an RTX 4090 (8B model, ≈130 tokens/s): busy <b>100%</b> of the time → busy <b>10%</b>")}</div></div>
        <div class="stat" style="--k:var(--violet)"><div class="n">$0.40–4.50</div><div class="d">{t("за 1 млн токенов ответа у дешёвых облачных моделей (Gemini Flash-Lite, GPT mini)", "per 1M output tokens for cheap cloud models (Gemini Flash-Lite, GPT mini)")}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:18px;--k:var(--amber)">{t("Простаивающая видеокарта стоит столько же, сколько работающая. Причина брать свою модель — чаще приватность и контроль, а не экономия.", "An idle GPU costs as much as a busy one. The reason for your own model is usually privacy and control, not savings.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Цены за час в Community Cloud Runpod: RTX 4090 $0.34, RTX 5090 $0.69, L40S $0.79, A100 SXM $1.39, H100 SXM $2.69 (SXM — серверная версия карты; вариант PCIe дешевле). В Secure Cloud дороже примерно в 1,3–2,6 раза. Serverless дороже за час (RTX 4090 около $1.10), зато платите только за секунды работы.",
                      "⏱ 5 min. Hourly prices in Runpod Community Cloud: RTX 4090 $0.34, RTX 5090 $0.69, L40S $0.79, A100 SXM $1.39, H100 SXM $2.69 (SXM is the server-board version; the PCIe variant is cheaper). Secure Cloud is roughly 1.3–2.6× more. Serverless costs more per hour (RTX 4090 about $1.10), but you pay only for seconds of work."),
                    t("Сравним с облачным API. RTX 4090 с моделью 8B даёт примерно 130 токенов в секунду, это около 470 тысяч токенов в час. При $0.34 в час выходит около $0.73 за миллион токенов, но только если карта занята без перерыва. Дешёвые облачные модели стоят $0.40–4.50 за миллион токенов ответа и не берут денег за простой.",
                      "Compare with a cloud API. An RTX 4090 with an 8B model gives about 130 tokens per second, about 470 thousand tokens per hour. At $0.34 per hour that is about $0.73 per million tokens, but only if the card is busy non-stop. Cheap cloud models cost $0.40–4.50 per million output tokens and charge nothing for idle time."),
                    t("Если карта занята только 10% времени, тот же миллион токенов обходится уже в $7.30 — дороже облака. Вывод: по деньгам своя модель выигрывает только при большом и ровном потоке задач. Чаще её выбирают из-за приватности, контроля над версией и работы без интернета. Это честный ответ на вопрос «а не дешевле ли?». Оговорка: $0.73 — худший случай, когда карту использует один человек. Сервер с пакетной обработкой (например, vLLM) обслуживает много запросов одновременно, и общая скорость, а с ней и цена за миллион токенов, становится в разы лучше.",
                      "If the card is busy only 10% of the time, the same million tokens costs $7.30, more than the cloud. Takeaway: money-wise your own model wins only with a large, steady stream of work. More often it is chosen for privacy, version control and offline work. That is the honest answer to “isn’t it cheaper?”. Caveat: $0.73 is the single-user worst case. A server with batching (for example vLLM) handles many requests at once, so total throughput, and with it the price per million tokens, gets several times better.")))


def s_decide():
    def cell(k, h, ex):
        return (f'<div class="layer" style="--k:var(--{k});padding:28px 28px;min-height:180px;display:flex;flex-direction:column;justify-content:center">'
                f'<div class="lh" style="font-size:31px">{h}</div><div class="ls" style="font-size:22px;margin-top:6px">{ex}</div></div>')
    ax = 'font:600 22px var(--body);color:var(--muted);display:flex;align-items:center;justify-content:center;text-align:center'
    grid = (f'<div style="display:grid;grid-template-columns:200px 1fr 1fr;grid-template-rows:auto 1fr 1fr;gap:18px;margin-top:16px">'
            f'<div></div><div style="{ax}">{t("Мало запросов", "Few requests")}</div><div style="{ax}">{t("Много запросов", "Many requests")}</div>'
            f'<div style="{ax};color:var(--violet)">{t("Данные можно отдать поставщику модели", "Data may go to the model vendor")}</div>'
            + cell("violet", t("Облачный API", "Cloud API"), t("ChatGPT, Gemini, Claude: лучшее качество, платим за запросы", "ChatGPT, Gemini, Claude: best quality, pay per request"))
            + cell("violet", t("Облачный API", "Cloud API"), t("пакетная обработка у поставщика обычно дешевле аренды", "the vendor’s batch processing is usually cheaper than renting"))
            + f'<div style="{ax};color:var(--green)">{t("Данные должны остаться у вас", "Data must stay with you")}</div>'
            + cell("green", t("Свой ноутбук", "Your laptop"), "LM Studio, Ollama")
            + cell("amber", "Runpod", t("Pod — ровный поток; Serverless — запросы волнами", "Pod for a steady flow; Serverless for bursts"))
            + '</div>')
    return dict(min=4, html=f'''
  {head(t("Как выбрать", "How to choose"), t("Выбор по двум вопросам: можно ли отдать данные и сколько работы", "Choose by two questions: can the data leave, and how much work is there"), k="cyan")}
  <div class="body" style="margin-top:12px;">
    {grid}
    <div class="note" style="margin-top:28px;font-size:22px;--k:var(--cyan)">{t("Runpod — тоже чужой компьютер, но модель и данные под вашим контролем, а не у поставщика модели. При переезде меняются только адрес и имя модели. Для чувствительных данных — Secure Cloud (дороже, напр. RTX 4090 $0.89/ч).", "Runpod is also someone else’s computer, but the model and data are under your control, not the model vendor’s. When you move, only the address and model name change. For sensitive data use Secure Cloud (pricier, e.g. RTX 4090 $0.89/h).")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Сводим всё в два вопроса. Первый: можно ли отдавать данные поставщику модели? Если да и задача сложная — облачный API: лучшее качество, платите за использование. Если нет — своя модель. Второй: сколько работы? Один человек и немного задач — ноутбук. Запросы волнами, например бот поддержки днём — Serverless. Большой ровный поток или эксперименты с моделью — Pod.",
                      "⏱ 4 min. Everything comes down to two questions. One: may the data go to the model vendor? If yes and the task is hard — a cloud API: best quality, pay for use. If no — your own model. Two: how much work? One person and a few tasks — a laptop. Requests in bursts, such as a daytime support bot — Serverless. A large steady flow or model experiments — a Pod."),
                    t("Упражнение в чат (1 мин): юрист хочет искать по договорам клиентов, 20 запросов в день. Что выбрать? Ответ: ноутбук или рабочий компьютер с локальной моделью; данные чувствительные, объём маленький.",
                      "Chat exercise (1 min): a lawyer wants to search client contracts, 20 queries a day. What to choose? Answer: a laptop or workstation with a local model; the data is sensitive and the volume small.")))


def s_hw():
    tree = ("genai-homeworks/L10/\n├─ README.md   # выбор и вывод\n├─ results.md  # 3 задачи: у себя и в облаке\n├─ speed.png   # скриншот с токенами/с\n└─ decision.md # карточка выбора")
    if LANG == "en":
        tree = ("genai-homeworks/L10/\n├─ README.md   # choice and conclusion\n├─ results.md  # 3 tasks: local vs cloud\n├─ speed.png   # screenshot with tokens/s\n└─ decision.md # decision card")
    steps = [t("Поставьте LM Studio или Ollama, скачайте модель 3–9B в Q4 (видеокарта 16 ГБ+: до 20B)", "Install LM Studio or Ollama; download a 3–9B model at Q4 (16 GB+ GPU: up to 20B)"),
             t("Дайте ей 3 рабочие задачи и те же задачи ChatGPT или Gemini", "Give it 3 work tasks, and the same tasks to ChatGPT or Gemini"),
             t("Запишите скорость (токенов/с) и сколько памяти заняла модель", "Record the speed (tokens/s) and the memory the model uses"),
             t("Сравните ответы по шкале 1–5 и сделайте вывод", "Score the answers 1–5 and draw a conclusion"),
             t("Заполните карточку: API / ноутбук / Pod / Serverless и почему", "Fill the card: API / laptop / Pod / Serverless and why")]
    ol = "".join(f"<li><span>{s}</span></li>" for s in steps)
    return dict(min=5, html=f'''
  {head(t("Домашнее задание", "Homework"), t("ДЗ: запустить модель у себя и честно сравнить с облаком", "Homework: run a model yourself and compare it honestly with the cloud"), k="green")}
  <div class="body big" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:44px;align-items:start;flex:none;margin-top:24px">
      <ol class="checklist hw">{ol}</ol>
      <div class="stack" style="gap:24px;">
        <pre class="code" style="font-size:22px;line-height:1.6">{tree}</pre>
        <div class="note" style="--k:var(--amber)">{t("Нет подходящего компьютера? Возьмите самую маленькую модель (Granite 4.2 3B, 2,2 ГБ) — она работает и без видеокарты.", "No suitable computer? Take the smallest model (Granite 4.2 3B, 2.2 GB); it runs without a GPU.")}</div>
        <div class="small" style="font-size:20px">{t("Только синтетические или свои данные. Runpod — по желанию, платно.", "Synthetic or your own data only. Runpod is optional and paid.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Домашнее задание на неделю. Поставить LM Studio или Ollama, скачать модель на 3–9 миллиардов параметров в Q4. Дать ей три задачи из своей работы (на синтетических данных): например, классифицировать письмо, сделать выжимку, ответить клиенту. Те же задачи отдать ChatGPT или Gemini.",
                      "⏱ 5 min. Homework for the week. Install LM Studio or Ollama, download a 3–9B model at Q4. Give it three tasks from your work (on synthetic data): for example, classify an email, summarise, reply to a customer. Give the same tasks to ChatGPT or Gemini."),
                    t("Записать скорость и занятую память (скриншот), оценить ответы по шкале от 1 до 5 и сделать вывод: для каких задач локальная модель годится. В конце карточка выбора: API, ноутбук, Pod или Serverless для своей задачи и почему. Оценивается честность сравнения, а не то, какая модель победила. Подробности и критерии в файле L10_05_Homework.",
                      "Record the speed and memory used (a screenshot), score the answers 1 to 5 and conclude which tasks a local model is good for. Finally a decision card: API, laptop, Pod or Serverless for your task, and why. Grading looks at an honest comparison, not at which model won. Details and criteria are in L10_05_Homework.")))


def s_summary():
    rules = [("cyan", t("Открытая модель = файл + лицензия", "Open model = file + licence"), t("ищем на Hugging Face, читаем карточку", "find it on Hugging Face, read the card")),
             ("green", t("Q4 + 25% должно влезть в видеокарту", "Q4 + 25% must fit the GPU"), t("иначе медленно; без видеокарты берём 3–4B", "otherwise it is slow; without a GPU take 3–4B")),
             ("violet", t("LM Studio или Ollama → localhost", "LM Studio or Ollama → localhost"), t("в коде меняются только адрес и имя модели; сервер не открываем в сеть", "only the address and model name change in code; never expose the server")),
             ("amber", t("Runpod: платим и за простой", "Runpod: idle time costs money"), t("закончили — Terminate, не Stop", "when done — Terminate, not Stop"))]
    li = "".join(f'<div class="task" style="--k:var(--{k});padding:30px 30px;min-height:200px;align-content:center"><div><div class="h" style="font-size:32px">{h}</div><div class="d" style="font-size:23px;margin-top:10px">{d}</div></div></div>' for k, h, d in rules)
    return dict(min=3, html=f'''
  {head(t("Итоги", "Summary"), t("Своя модель — это файл и память, а в коде меняются только адрес и имя модели", "Your own model is a file and memory; in code only the address and model name change"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="tasks" style="gap:28px 32px;margin-top:20px">{li}</div>
    <div class="note" style="margin-top:40px;font-size:24px;--k:var(--violet)">{t("<b>Дальше, L11:</b> вызов функций и первый агент: модель не только отвечает, но и действует.", "<b>Next, L11:</b> function calling and your first agent: the model not only answers but acts.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Четыре правила. Открытая модель — это файл и лицензия, ищем на Hugging Face и читаем карточку. Размер подбираем под память: Q4 плюс запас 25% должен влезть в видеокарту. LM Studio или Ollama дают сервер на localhost, и в коде меняются только адрес и имя модели; сервер не открываем в сеть, потому что локально не значит приватно. В Runpod платим и за простой: закончили — Terminate.",
                      "⏱ 3 min. Four rules. An open model is a file and a licence: find it on Hugging Face and read the card. Fit the size to memory: Q4 plus a 25% margin must fit the GPU. LM Studio or Ollama give you a server on localhost, and only the address and model name change in code; never expose the server, because local does not mean private. On Runpod idle time costs money too: when done — Terminate."),
                    t("Следующий урок: вызов функций. Модель научится не только отвечать текстом, но и вызывать инструменты: искать, считать, отправлять. Это первый шаг к агентам.",
                      "Next lesson: function calling. The model learns not only to answer in text but to call tools: search, compute, send. That is the first step towards agents.")))


SLIDES = [s_cover, s_hook, s_open, s_why, s_layers, s_quant, s_fit, s_speed, s_lmstudio, s_demo,
          s_server, s_agent, s_private, s_market, s_break, s_limits, s_runpod, s_cost, s_decide, s_hw, s_summary]


# ---------------------------------------------------------------- page
EXTRA_CSS = """
.bars .ref, .vline { position: absolute; top: 0; bottom: 26px; border-left: 2px dashed var(--k, var(--amber)); }
.vline span { position: absolute; top: 2px; left: 6px; white-space: nowrap; font: 700 18px var(--body); color: var(--k); }
.slide:not(.cover) .body { justify-content: flex-start; padding-top: 22px; }
.big .note { font-size: 23px; }
.big .legend div { font-size: 23px; }
.big .bars .bt { height: 50px; }
.big .bars .br { margin-bottom: 4px; }
.big .bars .bl { font-size: 23px; }
.big .bars .bl small { font-size: 19px; }
.big .stat .d { font-size: 22px; }
.big .lrow .h { font-size: 29px; }
.big .lrow .dot { width: 30px; height: 30px; }
.big .lrow .d { font-size: 22px; }
.big .plaque { font-size: 26px; padding: 22px 26px; }
.checklist.hw { gap: 40px; }
.checklist.hw li { font-size: 27px; grid-template-columns: 48px 1fr; }
.checklist.hw li::before { width: 34px; height: 34px; font-size: 19px; }
.mhead { font: 800 30px/1.2 var(--display); color: var(--k); padding-bottom: 12px; border-bottom: 4px solid var(--k); }
.mlist { list-style: none; margin: 0; padding: 0; }
.mli { display: flex; gap: 16px; align-items: baseline; padding: 32px 0 22px; }
.mli i { width: 13px; height: 13px; border-radius: 50%; background: var(--k); flex: none; transform: translateY(-3px); }
.mli span { font: 700 30px/1.25 var(--body); color: var(--fg); }
.mli small { font-size: 19px; font-weight: 500; color: var(--muted); }
.mli em { display: block; font: 500 20px var(--mono); font-style: normal; color: var(--muted); margin-top: 4px; }
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
    title = t("Урок 10: Открытые модели | GenAI Basics", "Lesson 10: Open models | GenAI Basics")
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
