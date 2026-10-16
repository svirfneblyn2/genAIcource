# -*- coding: utf-8 -*-
"""Build the L15 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. No raster images: every visual is drawn in HTML.
Facts: ../L15_08_Source_Notes_Research_2026-10.md.
"""
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L15 = HERE.parent
NAME = "presentation_L15_Responsible_AI_Security_Regulation"
OUT = {"ru": L15 / f"{NAME}_v2.html", "en": L15 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 15 • Ответственный ИИ", "en": "GenAI Basics • Lesson 15 • Responsible AI"}


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


def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg"><div style="position:absolute;right:110px;top:190px;width:560px;font:800 220px/1 var(--body);color:#1e293b;text-align:right">AI<br><span style="color:#38bdf8;font-size:120px">✓</span></div></div>
  <div class="shade"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 15 • Модуль 4: от идеи к продукту", "GenAI Basics • Lesson 15 • Module 4: idea to product")}</div>
    <h1>{t("Ответственный ИИ", "Responsible AI")}</h1>
    <h2>{t("Ошибки, утечки, дипфейки и законы: как пользоваться ИИ на работе и не навредить", "Errors, leaks, deepfakes and laws: how to use AI at work without doing harm")}</h2>
    <p>{t("Реальные случаи 2023–2026, правила для данных, EU AI Act, Узбекистан, Казахстан, Россия. Данные на октябрь 2026.",
           "Real cases from 2023–2026, data rules, the EU AI Act, Uzbekistan, Kazakhstan, Russia. Data as of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. За курс мы научились генерировать текст, картинки, видео, звук, строить агентов и прототипы. Сегодня о том, как всем этим пользоваться на работе и не навредить: себе, компании и клиентам. Без юридических лекций: реальные случаи, простые правила и то, что уже требуют законы.",
                      "⏱ 2 min. Welcome. In this course we learned to generate text, images, video and audio, and to build agents and prototypes. Today: how to use all of that at work without harming yourself, your company or your customers. No legal lecture: real cases, simple rules and what laws already require.")))


def s_hook():
    return dict(min=5, html=f'''
  {head(t("Карта рисков", "Risk map"), t("Четыре главных риска ИИ на работе: что случается часто и что стоит дорого", "Four main AI risks at work: what happens often and what costs a lot"), k="red")}
  <div class="body" style="margin-top:4px;">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:34px;align-items:center;flex:none;">
      {risk_map()}
      <div class="stack" style="gap:16px;">
        {legend([(1, "amber", t("<b>Выдумки</b> (галлюцинации) — каждый день", "<b>Made-up facts</b> (hallucinations) — every day")),
                 (2, "red", t("<b>Утечка данных</b> — один вставленный файл", "<b>Data leak</b> — one pasted file")),
                 (3, "red", t("<b>Дипфейк-мошенничество</b> — редко, но миллионы", "<b>Deepfake fraud</b> — rare, but millions")),
                 (4, "violet", t("<b>Агент удалил данные</b> — секунды", "<b>An agent deletes data</b> — in seconds"))])}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Карта: по горизонтали — как часто случается, по вертикали — сколько стоит ущерб. Выдумки модели случаются постоянно, ущерб обычно умеренный, если результат проверяет человек. Утечка данных — один вставленный документ, но ущерб большой. Дипфейк-мошенничество редкое, но это миллионы. Агент, удаливший данные, — новый риск 2025–2026: секунды и катастрофа.",
                      "⏱ 5 min. The map: horizontally how often it happens, vertically how much damage it does. Model mistakes happen all the time; damage is usually moderate if a human checks the result. A data leak is one pasted document, but the damage is large. Deepfake fraud is rare but costs millions. An agent deleting data is the new 2025–2026 risk: seconds and a disaster."),
                    t("Дальше по каждому риску — реальный случай и правило. В конце — что требуют законы и ваше домашнее задание: правила ИИ для своей команды.",
                      "Next, for each risk a real case and a rule. At the end, what laws require, and your homework: AI rules for your own team.")))


def s_halluc():
    tiles = [("amber", "45%", t("ответов ИИ-ассистентов о новостях — с существенной ошибкой (EBU/BBC, 22 вещателя, октябрь 2025)", "of AI assistant answers about news had a significant issue (EBU/BBC, 22 broadcasters, October 2025)")),
             ("red", "2 190", t("судебных решений в мире, где суд указал на выдуманный ИИ материал — ссылки, цитаты (база Д. Шарлотена, октябрь 2026)", "court decisions worldwide where AI-invented citations were found (D. Charlotin’s database, October 2026)")),
             ("violet", "$5 000", t("штраф юристам в деле Mata v. Avianca (США, 2023): сослались на дела, которые придумал ChatGPT", "fine for lawyers in Mata v. Avianca (US, 2023): they cited cases ChatGPT made up"))]
    tt = "".join(f'<div class="stat" style="--k:var(--{k});flex:1"><div class="n">{n}</div><div class="d">{d}</div></div>' for k, n, d in tiles)
    return dict(min=6, html=f'''
  {head(t("Риск 1", "Risk 1"), t("Модель уверенно выдумывает — проверять ответ обязан человек", "The model confidently makes things up — a human must check the answer"), k="amber")}
  <div class="body" style="margin-top:14px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px;">{tt}</div>
    <div style="margin-top:40px">{flow([("amber", t("ИИ ответил", "AI answered"), t("уверенно и гладко — это не признак правды", "confident and fluent — not a sign of truth")),
                                        ("cyan", t("Найдите первоисточник", "Find the source"), t("закон, отчёт, сайт компании, документ", "the law, report, company site, document")),
                                        ("violet", t("Сверьте детали", "Check the details"), t("цифры, имена, даты, ссылки, цитаты", "numbers, names, dates, links, quotes")),
                                        ("green", t("Отправляете вы", "You send it"), t("и отвечаете за результат тоже вы", "and you are responsible for it"))])}</div>
    <div class="note" style="margin-top:30px;--k:var(--green)">{t("<b>Правило:</b> цифры, имена, ссылки, законы и цитаты из ответа ИИ проверяем по первоисточнику. Отвечает тот, кто отправил, а не ИИ.", "<b>Rule:</b> check numbers, names, links, laws and quotes from an AI answer against the original source. The sender is responsible, not the AI.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Риск номер один по частоте. Исследование Европейского вещательного союза и BBC, октябрь 2025: 22 общественных вещателя из 18 стран проверили больше 3000 ответов ChatGPT, Copilot, Gemini и Perplexity про новости. 45% содержали хотя бы одну существенную ошибку: неверный источник, устаревший факт.",
                      "⏱ 6 min. Risk number one by frequency. A study by the European Broadcasting Union and the BBC, October 2025: 22 public broadcasters from 18 countries checked over 3,000 answers from ChatGPT, Copilot, Gemini and Perplexity about news. 45% had at least one significant issue: a wrong source, an outdated fact."),
                    t("Самый известный случай — дело Mata v. Avianca в США, 2023: юристы подали в суд документ со ссылками на дела, которые выдумал ChatGPT, и получили штраф 5000 долларов. Судья подчеркнул: пользоваться ИИ можно, но проверять — обязанность юриста. Сейчас в открытой базе исследователя Дамьена Шарлотена уже 2190 таких судебных решений по всему миру. Правило простое: всё, что пойдёт дальше от вас, проверяется по первоисточнику.",
                      "The best-known case is Mata v. Avianca in the US, 2023: lawyers filed a brief citing cases ChatGPT had invented and were fined 5,000 dollars. The judge stressed that using AI is fine, but checking is the lawyer’s duty. The open database kept by researcher Damien Charlotin now lists 2,190 such court decisions worldwide. The rule is simple: anything that leaves your hands gets checked against the original source.")))


def s_leak():
    return dict(min=6, html=f'''
  {head(t("Риск 2", "Risk 2"), t("Утечка начинается с одного вставленного файла: решите заранее, какие данные куда можно", "A leak starts with one pasted file: decide in advance which data may go where"), k="red")}
  <div class="body" style="margin-top:4px;">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:34px;align-items:center;flex:none;">
      <div>{traffic()}</div>
      <div class="stack" style="gap:16px;">
        <div class="note" style="--k:var(--red)">{t("<b>Samsung, 2023:</b> инженеры вставили в ChatGPT исходный код компании; после этого компания временно запретила генеративный ИИ на рабочих устройствах.", "<b>Samsung, 2023:</b> engineers pasted company source code into ChatGPT; the company then temporarily banned generative AI tools on work devices.")}</div>
        <div class="note" style="--k:var(--amber)">{t("<b>Grok, 2025:</b> кнопка «поделиться» сделала чаты публичными — по данным Forbes, более 370 000 разговоров нашлись в Google.", "<b>Grok, 2025:</b> the share button made chats public — Forbes found over 370,000 conversations in Google.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Светофор данных — простая схема для команды. Зелёное: публичные данные — тексты с сайта, опубликованные документы — можно в любой ИИ. Жёлтое: внутренние — планы, внутренние письма — только в одобренный компанией ИИ. Красное: персональные данные клиентов, пароли, договоры — в чат ИИ нельзя без явного разрешения.",
                      "⏱ 6 min. The data traffic light — a simple scheme for a team. Green: public data — website texts, published documents — any AI. Amber: internal — plans, internal emails — only company-approved AI. Red: customer personal data, passwords, contracts — never in an AI chat without explicit approval."),
                    t("Два случая. Samsung, 2023: инженеры вставили в ChatGPT внутренний код, и компания временно запретила генеративный ИИ на рабочих устройствах. Grok, 2025: кнопка «поделиться» публиковала чаты, около 370 тысяч разговоров попали в поиск Google, в некоторых — личные данные и даже пароль (по данным Forbes). Вывод: опасность не только в самой модели, но и в кнопках вокруг неё.",
                      "Two cases. Samsung, 2023: engineers pasted internal code into ChatGPT, and the company temporarily banned generative AI tools on work devices. Grok, 2025: the share button published chats, and about 370 thousand conversations appeared in Google search, some with personal data and even a password (as reported by Forbes). Takeaway: the danger is not only the model but the buttons around it.")))


def s_plans():
    rows = [("red", t("ChatGPT Free / Plus / Pro", "ChatGPT Free / Plus / Pro"), t("чаты могут идти в обучение, пока не выключите: Settings → Data controls", "your chats may be used for training unless you switch it off: Settings → Data controls")),
            ("amber", t("Claude Free / Pro / Max", "Claude Free / Pro / Max"), t("с августа 2025 выбираете сами; если разрешили — хранится до 5 лет", "since August 2025 you choose; if allowed, kept for up to 5 years")),
            ("green", t("ChatGPT Business / Enterprise", "ChatGPT Business / Enterprise"), t("по умолчанию не учится на данных компании", "does not train on company data by default")),
            ("green", t("Claude for Work · Gemini в Workspace", "Claude for Work · Gemini in Workspace"), t("по умолчанию не учится на данных компании", "does not train on company data by default"))]
    return dict(min=5, html=f'''
  {head(t("Тарифы", "Plans"), t("Одна и та же модель, разные правила: личный тариф и рабочий обращаются с данными по-разному", "Same model, different rules: personal and business plans treat data differently"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.4fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="light" style="gap:14px">{_lr(rows)}</div>
      <div class="plaque" style="font-size:22px;line-height:1.5">{t("<b>Рабочие данные — только в рабочий аккаунт</b> компании. Личный ChatGPT или Claude для документов клиентов не подходит, даже платный.", "<b>Work data goes only into the company’s business account.</b> A personal ChatGPT or Claude is not for customer documents, even a paid one.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Частая ошибка: «у меня платный ChatGPT Plus, значит безопасно». Нет: в личных тарифах ChatGPT по умолчанию может обучаться на ваших чатах, пока вы не выключите это в Settings → Data controls. У Claude с августа 2025 выбор за пользователем, и если обучение разрешено, данные хранятся до пяти лет.",
                      "⏱ 5 min. A common mistake: “I have paid ChatGPT Plus, so it is safe”. No: personal ChatGPT plans may train on your chats by default until you switch it off in Settings → Data controls. Since August 2025 Claude lets the user choose, and if training is allowed, data is kept for up to five years."),
                    t("Рабочие тарифы — ChatGPT Business и Enterprise, Claude for Work, Gemini в Google Workspace — по умолчанию не обучаются на данных компании. Поэтому правило: рабочие документы — только в рабочий аккаунт, который выдала компания.",
                      "Business plans — ChatGPT Business and Enterprise, Claude for Work, Gemini in Google Workspace — do not train on company data by default. So the rule: work documents only go into the business account the company gave you.")))


def s_deepfake():
    return dict(min=5, html=f'''
  {head(t("Риск 3", "Risk 3"), t("Видеозвонок с «директором» может быть подделкой: проверяйте денежные просьбы по другому каналу", "A video call with “the CFO” can be fake: verify money requests through another channel"), k="red")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1.15fr;gap:44px;align-items:center;flex:none;margin-bottom:40px">
      <div class="stat" style="--k:var(--red)"><div class="n" style="font-size:72px">$25 {t("млн", "M")}</div><div class="d">{t("Arup, Гонконг, 2024: сотрудник перевёл деньги после видеозвонка, где «финдиректор» и коллеги были дипфейками", "Arup, Hong Kong, 2024: an employee transferred money after a video call where the “CFO” and colleagues were deepfakes")}</div></div>
      <div class="stack" style="gap:16px;">
        <div class="note" style="--k:var(--green)">{t("<b>Перезвоните</b> по известному номеру, а не по тому, что в письме или чате.", "<b>Call back</b> on a known number, not the one in the email or chat.")}</div>
        <div class="note" style="--k:var(--green)">{t("<b>Кодовое слово</b> для срочных денежных просьб в семье и команде.", "<b>A code word</b> for urgent money requests in your family and team.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Срочность и секретность — главный признак обмана.", "Urgency and secrecy are the main sign of fraud.")}</div>
      </div>
    </div>
    {flow([("red", t("Звонок «директора»", "A call from “the CFO”"), t("лицо и голос знакомы — это может быть дипфейк", "face and voice are familiar — it may be a deepfake")),
           ("amber", t("Срочно и тайно", "Urgent and secret"), t("«переведи сегодня, никому не говори»", "“transfer today, tell no one”")),
           ("violet", t("Стоп", "Stop"), t("закончите звонок, ничего не платите", "end the call, pay nothing")),
           ("green", t("Перезвоните сами", "Call back yourself"), t("по известному номеру или спросите кодовое слово", "on a known number, or ask for the code word"))])}
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Один из самых дорогих известных случаев: инженерная компания Arup, Гонконг, начало 2024. Сотрудник финансового отдела подключился к видеозвонку, где «финансовый директор» и несколько «коллег» были дипфейками. Было сделано 15 переводов, около 200 миллионов гонконгских долларов, это примерно 25 миллионов долларов США. Arup подтвердила случай.",
                      "⏱ 5 min. One of the most expensive known cases: the engineering firm Arup, Hong Kong, early 2024. A finance employee joined a video call where the “CFO” and several “colleagues” were deepfakes. The employee made 15 transfers, about 200 million Hong Kong dollars, roughly 25 million US dollars. Arup confirmed the case."),
                    t("Похожие схемы есть и в нашем регионе: в 2025 году полиция Украины раскрыла колл-центры, которые звонили жителям Казахстана по видео и с помощью дипфейков и формы выдавали себя за полицию и сотрудников банка. Защита организационная: перезванивать по известному номеру, договориться о кодовом слове для срочных денежных просьб и помнить, что срочность плюс просьба держать в секрете — главный признак обмана.",
                      "Similar schemes exist in our region: in 2025 Ukrainian police broke up call centres that video-called people in Kazakhstan, using deepfakes and uniforms to pose as police and bank staff. The defence is organisational: call back on a known number, agree a code word for urgent money requests and remember that urgency plus a request for secrecy is the main sign of fraud.")))


def s_agents():
    tiles = [("red", t("9 секунд", "9 seconds"), t("PocketOS, апрель 2026: агент Cursor нашёл в файле лишний ключ доступа и удалил рабочую базу вместе с бэкапами; сервис лежал около 30 часов", "PocketOS, April 2026: a Cursor agent found a stray access key in a file and deleted the production database and its backups; about 30 hours of downtime")),
             ("amber", t("2025", "2025"), t("Replit, июль: агент удалил рабочую базу во время объявленной «заморозки» изменений", "Replit, July: an agent deleted a production database during a declared code freeze"))]
    tt = "".join(f'<div class="stat" style="--k:var(--{k});flex:1"><div class="n">{n}</div><div class="d">{d}</div></div>' for k, n, d in tiles)
    return dict(min=6, html=f'''
  {head(t("Риск 4", "Risk 4"), t("Избыточные полномочия: агент делает то, на что у него есть права, — даже если вы этого не хотели", "Excessive agency: an agent does whatever it has rights to — even if you did not want it to"), k="violet")}
  <div class="body" style="margin-top:14px;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:44px;">{tt}</div>
    <div style="margin-top:36px">{flow([("cyan", t("Задача агенту", "A task for the agent"), t("обычная рабочая просьба в Cursor", "an ordinary request in Cursor")),
                                        ("amber", t("Ключ в файле", "A key in a file"), t("агент нашёл доступ, который ему не давали", "the agent found access nobody meant to give")),
                                        ("red", t("База и бэкапы удалены", "Database and backups deleted"), t("за 9 секунд, без вопроса человеку", "in 9 seconds, without asking a human")),
                                        ("violet", t("~30 часов простоя", "~30 hours of downtime"), t("клиенты без сервиса", "customers without the service"))])}</div>
    <div class="note" style="margin-top:30px;--k:var(--green)">{t("<b>Правила из L11–L12:</b> минимум прав · никаких рабочих паролей и ключей рядом с агентом · подтверждение человеком для удаления и денег · резервные копии отдельно.", "<b>Rules from L11–L12:</b> least privilege · no production passwords or keys near the agent · human confirmation for deletion and money · backups kept separately.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Новый риск, о котором мы говорили в L11 и L12. Апрель 2026, компания PocketOS: агент разработки в Cursor наткнулся в постороннем файле на ключ доступа и за девять секунд удалил рабочую базу данных вместе с резервными копиями; сервис лежал около 30 часов. Июль 2025, Replit: агент удалил рабочую базу во время объявленной «заморозки» изменений и потом неверно доложил о состоянии.",
                      "⏱ 6 min. A new risk we discussed in L11 and L12. April 2026, PocketOS: a coding agent in Cursor came across an access token in an unrelated file and in nine seconds deleted the production database along with its backups; the service was down for about 30 hours. July 2025, Replit: an agent deleted a production database during a declared code freeze and then misreported the state."),
                    t("В списке рисков OWASP это называется «избыточные полномочия» (Excessive Agency). Агент не злой — он просто делает то, на что у него есть права. Отсюда правила: минимум прав, никаких рабочих ключей рядом с агентом, подтверждение человеком для удаления и денег, резервные копии отдельно, куда агент не дотянется.",
                      "OWASP’s risk list calls this “Excessive Agency”. The agent is not evil — it simply does what it has rights to. Hence the rules: least privilege, no production keys near the agent, human confirmation for deletion and money, backups kept separately where the agent cannot reach.")))


def s_owasp():
    items = [("red", "LLM01", t("Подмена инструкций (prompt injection)", "Prompt injection"), t("чужой текст командует моделью (L11)", "someone else’s text commands the model (L11)")),
             ("red", "LLM02", t("Утечка конфиденциального", "Sensitive information disclosure"), t("модель выдаёт то, что видеть нельзя", "the model reveals what must not be seen")),
             ("violet", "LLM06", t("Избыточные полномочия", "Excessive agency"), t("агенту дали слишком много прав", "the agent got too many rights")),
             ("amber", "LLM09", t("Дезинформация", "Misinformation"), t("уверенные выдумки", "confident fabrications"))]
    cards = "".join(f'<div class="task" style="--k:var(--{k});padding:20px 24px;align-items:flex-start"><div><div class="d" style="font-family:var(--mono);color:var(--{k});font-size:20px">{c}</div><div class="h" style="font-size:26px;margin-top:4px">{h}</div><div class="d" style="font-size:21px;margin-top:6px">{d}</div></div></div>' for k, c, h, d in items)
    return dict(min=5, html=f'''
  {head("OWASP", t("Топ-10 рисков OWASP для ИИ-приложений: четыре, которые касаются каждого", "The OWASP Top 10 for AI apps: the four that affect everyone"), t("OWASP — некоммерческое сообщество специалистов по безопасности.", "OWASP is a non-profit community of security specialists."), k="red")}
  <div class="body" style="margin-top:14px;">
    <div class="tasks">{cards}</div>
    <div class="note" style="margin-top:28px;--k:var(--cyan)">{t("Список 2025 года — общий язык для разработчиков и службы безопасности. Для агентов в декабре 2025 вышел отдельный список.", "The 2025 list is the common language of developers and security teams. A separate list for agents came out in December 2025.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. OWASP — некоммерческое сообщество специалистов по безопасности. Их «Топ-10 рисков для приложений на языковых моделях», версия 2025 года, — общий язык, на котором разработчики и служба безопасности обсуждают ИИ. Из десяти пунктов четыре касаются каждого пользователя: подмена инструкций, утечка конфиденциальной информации, избыточные полномочия и дезинформация.",
                      "⏱ 5 min. OWASP is a non-profit community of security specialists. Its “Top 10 for LLM Applications”, 2025 edition, is the common language developers and security teams use to discuss AI. Of the ten items, four affect every user: prompt injection, sensitive information disclosure, excessive agency and misinformation."),
                    t("Остальные шесть — для разработчиков: цепочка поставок, отравление данных, обработка ответа, утечка системного промпта, векторные базы, неограниченное потребление. Для агентов OWASP в декабре 2025 выпустил отдельный топ-10.",
                      "The other six are for developers: supply chain, data poisoning, output handling, system prompt leakage, vector stores, unbounded consumption. For agents, OWASP released a separate Top 10 in December 2025.")))


def s_bias():
    rows = [(t("«Белые» имена", "White-associated names"), t("предпочтены в 85% сравнений", "preferred in 85% of comparisons"), 85, "amber"),
            (t("«Чёрные» имена", "Black-associated names"), t("предпочтены в 9%", "preferred in 9%"), 9, "red"),
            (t("Мужские имена", "Male-associated names"), t("предпочтены в 52%", "preferred in 52%"), 52, "cyan"),
            (t("Женские имена", "Female-associated names"), t("предпочтены в 11%", "preferred in 11%"), 11, "violet")]
    ch = bars(rows, 0, 100, lambda v: f"{v:.0f}%", ticks=[(0, "0"), (50, "50"), (100, "100%")], label_w=300)
    return dict(min=5, html=f'''
  {head(t("Предвзятость", "Bias"), t("ИИ повторяет перекосы данных: резюме, отличавшиеся только именем, получали разные оценки", "AI repeats the biases in its data: CVs that differed only in the name were ranked differently"), t("Исследование Вашингтонского университета (2024): ИИ ранжировал резюме, отличавшиеся только именем.", "University of Washington study (2024): AI ranked CVs that differed only in the name."), k="amber")}
  <div class="body" style="margin-top:6px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:44px;align-items:center;flex:none;">
      {ch}
      <div class="note" style="--k:var(--green)">{t("<b>Правило:</b> решения о людях — найм, кредит, увольнение — ИИ может готовить, но принимает человек. К этому ведут и законы (слайды 11–12).", "<b>Rule:</b> decisions about people — hiring, credit, dismissal — AI may prepare, but a human decides. Laws are moving the same way (slides 11–12).")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Исследование Вашингтонского университета: языковым моделям давали ранжировать резюме, которые отличались только именем кандидата. Резюме с именами, которые ассоциируются с белыми, выбирались в 85% сравнений, с «чёрными» — в 9%. Мужские имена — в 52%, женские — в 11%. Модель не «хочет» дискриминировать — она повторяет перекосы данных, на которых училась.",
                      "⏱ 5 min. A University of Washington study had language models rank CVs that differed only in the candidate’s name. CVs with white-associated names were chosen in 85% of comparisons, Black-associated in 9%. Male-associated names in 52%, female in 11%. The model does not “want” to discriminate — it repeats the biases in the data it learned from."),
                    t("Поэтому решения о людях — найм, кредит, увольнение — ИИ может готовить, но принимает человек. В ЕС такие системы относятся к высокому риску (обязанности — с декабря 2027), а закон Узбекистана запрещает основывать решения, затрагивающие права человека, только на выводах ИИ.",
                      "That is why decisions about people — hiring, credit, dismissal — AI may prepare, but a human makes. In the EU such systems are high-risk (duties apply from December 2027), and Uzbekistan’s law forbids basing decisions that affect people’s rights on AI output alone.")))


def traffic():
    rows = [("#22c55e", t("Публичное", "Public"), t("тексты с сайта, опубликованные документы", "website texts, published documents"), t("в любой ИИ", "any AI tool")),
            ("#fbbf24", t("Внутреннее", "Internal"), t("планы, внутренние письма", "plans, internal emails"), t("только в одобренный компанией ИИ", "company-approved AI only")),
            ("#ef4444", t("Конфиденциальное", "Confidential"), t("персональные данные клиентов, пароли, договоры", "customer personal data, passwords, contracts"), t("в чат ИИ — нет, без явного разрешения", "never in AI chats without explicit approval"))]
    return "".join(
        f'<div style="display:grid;grid-template-columns:70px 1fr 50px 1fr;gap:18px;align-items:center;border:2px solid #2a3550;border-radius:16px;padding:16px 22px;margin-bottom:14px">'
        f'<div style="width:58px;height:58px;border-radius:50%;background:{c}"></div>'
        f'<div><div style="font:700 27px var(--body);color:var(--fg)">{h}</div><div style="font:400 20px/1.35 var(--body);color:var(--muted)">{d}</div></div>'
        f'<div style="font-size:34px;color:var(--cyan);text-align:center">→</div>'
        f'<div style="font:600 23px/1.35 var(--body);color:var(--fg)">{w}</div></div>' for c, h, d, w in rows)


def flow(steps):
    """Horizontal chain of numbered boxes with arrows: steps = [(colour, title, desc)]."""
    out = []
    for i, (k, h, d) in enumerate(steps):
        if i:
            out.append('<div style="align-self:center;font-size:40px;color:var(--muted);text-align:center">→</div>')
        out.append(f'<div style="background:var(--surface-card);border:1px solid var(--line);border-top:5px solid var(--{k});border-radius:14px;padding:20px 22px;min-height:150px">'
                   f'<div style="width:40px;height:40px;border-radius:50%;background:var(--{k});color:#0b0f17;font:800 22px/40px var(--body);text-align:center;margin-bottom:12px">{i + 1}</div>'
                   f'<div style="font:700 25px/1.25 var(--body);color:var(--fg)">{h}</div>'
                   f'<div style="font:400 19px/1.35 var(--body);color:var(--muted);margin-top:6px">{d}</div></div>')
    cols = " 50px ".join(["1fr"] * len(steps))
    return f'<div style="display:grid;grid-template-columns:{cols};gap:6px">{"".join(out)}</div>'


def risk_map():
    pts = [(t("Выдумки", "Made-up facts"), 88, 42, "amber", "1"), (t("Утечка данных", "Data leak"), 58, 76, "red", "2"),
           (t("Дипфейк-мошенничество", "Deepfake fraud"), 22, 92, "red", "3"), (t("Агент удалил данные", "Agent deletes data"), 12, 66, "violet", "4")]
    dots = "".join(f'<div style="position:absolute;left:{x}%;bottom:{y}%;width:46px;height:46px;margin-left:-23px;margin-bottom:-23px;border-radius:50%;background:var(--{k});color:#0b0f17;font:800 24px/46px var(--body);text-align:center">{n}'
                   f'<div style="position:absolute;{"right:56px" if x > 60 else "left:56px"};top:8px;font:600 23px var(--body);color:var(--fg);white-space:nowrap">{lab}</div></div>' for lab, x, y, k, n in pts)
    return (f'<div style="position:relative;height:560px;margin:10px 40px 40px 70px;border-left:2px solid var(--cyan);border-bottom:2px solid var(--cyan);'
            f'background:linear-gradient(to top right, transparent 55%, rgba(248,113,113,.10))">{dots}'
            f'<div style="position:absolute;left:-62px;top:50%;transform:rotate(-90deg) translateX(50%);transform-origin:left;font:600 20px var(--body);color:var(--muted);white-space:nowrap">{t("ущерб ↑", "damage ↑")}</div>'
            f'<div style="position:absolute;right:0;bottom:-36px;font:600 20px var(--body);color:var(--muted)">{t("как часто →", "how often →")}</div></div>')


def s_labels():
    rows = [("cyan", "SynthID (Google)", t("невидимая метка в пикселях, звуке и тексте; картинку можно проверить в приложении Gemini", "an invisible mark in pixels, sound and text; you can check an image in the Gemini app")),
            ("violet", "C2PA Content Credentials", t("подписанные сведения «кто и чем сделал»; пропадают при скриншоте", "signed “who made it, with what” metadata; lost on a screenshot")),
            ("amber", t("Нет метки ≠ сделал человек", "No mark ≠ made by a human"), t("и метка не доказывает, что содержание правда", "and a mark does not prove the content is true"))]
    return dict(min=5, html=f'''
  {head(t("Маркировка", "Labelling"), t("Законы требуют помечать ИИ-контент, а техника помогает: невидимые метки и подписи", "Laws require labelling AI content, and technology helps: invisible marks and signatures"), k="cyan")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="light" style="gap:14px">{_lr(rows)}</div>
      <div class="plaque" style="font-size:22px;line-height:1.5">{t("<b>Маркировку уже требуют:</b> Китай (с 1.09.2025), Казахстан (с 18.01.2026), ЕС — ст. 50 AI Act (с 2.08.2026). <b>Россия</b> — правила для крупных платформ с 1.03.2027.", "<b>Labelling is already required:</b> China (from 1.09.2025), Kazakhstan (from 18.01.2026), the EU — AI Act Art. 50 (from 2.08.2026). <b>Russia</b> — rules for large platforms from 1.03.2027.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Общая нить законов разных стран — маркировка ИИ-контента. Китай требует видимые и скрытые метки с 1 сентября 2025. В ЕС статья 50 AI Act с 2 августа 2026: чат-бот должен сообщать, что он ИИ, генераторы — добавлять машиночитаемую метку, дипфейки — видимую пометку; для генераторов, выпущенных до 2 августа 2026, машиночитаемая метка обязательна с 2 декабря 2026. Казахстан — с января 2026. В России для платформ больше 500 тысяч пользователей в день — с 1 марта 2027; источники расходятся, насколько это обязательно.",
                      "⏱ 5 min. The common thread across countries’ laws is labelling AI content. China has required visible and hidden labels since 1 September 2025. In the EU, AI Act Article 50 from 2 August 2026: a chatbot must say it is AI, generators must add a machine-readable mark, deepfakes need a visible label; generators already on the market before 2 August 2026 have until 2 December 2026 to add the machine-readable mark. Kazakhstan — from January 2026. In Russia, for platforms with over 500 thousand daily users — from 1 March 2027; sources disagree on how mandatory it is."),
                    t("Техника: SynthID от Google — невидимая метка прямо в изображении, звуке или тексте; проверить картинку можно в приложении Gemini. C2PA — подписанные сведения о происхождении файла, их поддерживают Adobe, Google, Microsoft, OpenAI и другие; но после скриншота они теряются. Два вывода: отсутствие метки не значит, что сделал человек, а наличие метки не значит, что содержание правдиво.",
                      "Technology: Google’s SynthID is an invisible mark inside an image, sound or text; you can check an image in the Gemini app. C2PA is signed provenance data supported by Adobe, Google, Microsoft, OpenAI and others; but a screenshot strips it. Two takeaways: no mark does not mean a human made it, and a mark does not mean the content is true.")))


def s_euact():
    events = [("2.02.2025", t("запрещённые практики", "prohibited practices"), "red"), ("2.08.2025", t("модели общего назначения", "general-purpose models"), "violet"),
              ("2.08.2026", t("основная часть + маркировка (ст. 50)", "most rules + labelling (Art. 50)"), "cyan"), ("2.12.2026", t("запрет «раздевающих» генераторов", "ban on “nudification” generators"), "red"),
              ("2.12.2027", t("«высокий риск» — системы, решающие о людях: найм, кредит, образование", "“high-risk” — systems deciding about people: hiring, credit, education"), "amber")]
    n = len(events)
    marks = "".join(f'<div style="position:absolute;left:{6 + i * 88 / (n - 1):.1f}%;top:0;transform:translateX(-50%);text-align:center;width:250px">'
                    f'<div style="font:700 24px var(--mono);color:var(--{k})">{d}</div><div style="width:22px;height:22px;border-radius:50%;background:var(--{k});margin:14px auto"></div>'
                    f'<div style="font:500 21px/1.35 var(--body);color:var(--fg)">{lab}</div></div>' for i, (d, lab, k) in enumerate(events))
    return dict(min=6, html=f'''
  {head("EU AI Act", t("Европейский закон об ИИ вступает в силу по частям — большая часть уже действует, высокий риск — с 2027", "The EU AI Act applies in stages — most of it is in force, high-risk rules from 2027"), k="violet")}
  <div class="body" style="margin-top:16px;">
    <div style="position:relative;height:250px;margin:0 30px;"><div style="position:absolute;left:3%;right:3%;top:58px;height:3px;background:#2a3550"></div>{marks}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:30px;">
      <div class="note" style="--k:var(--red)">{t("<b>Штрафы:</b> до €35 млн или 7% оборота за запрещённое; до €15 млн или 3% — за остальное, включая маркировку.", "<b>Fines:</b> up to €35M or 7% of turnover for prohibited practices; up to €15M or 3% for the rest, including labelling.")}</div>
      <div class="note" style="--k:var(--cyan)">{t("Касается и компаний вне ЕС, если их ИИ используют в ЕС.", "It also applies to companies outside the EU if their AI is used in the EU.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. EU AI Act — первый крупный закон об ИИ. Он вступает в силу частями. С февраля 2025 запрещены опасные практики, например социальный рейтинг. С августа 2025 — правила для моделей общего назначения. С 2 августа 2026 действует большая часть, включая маркировку по статье 50. Поправки 2026 года (Регламент 2026/1744) добавили с 2 декабря 2026 запрет генераторов интимных изображений без согласия и перенесли правила для высокорисковых систем — найм, кредит, образование — на декабрь 2027.",
                      "⏱ 6 min. The EU AI Act is the first major AI law. It applies in stages. Since February 2025 dangerous practices such as social scoring are banned. Since August 2025 — rules for general-purpose models. From 2 August 2026 most of it applies, including Article 50 labelling. The 2026 amendments (Regulation 2026/1744) added, from 2 December 2026, a ban on generators of non-consensual intimate images and moved the high-risk rules — hiring, credit, education — to December 2027."),
                    t("Штрафы: до 35 миллионов евро или 7% мирового оборота за запрещённые практики, до 15 миллионов или 3% — за большинство остальных нарушений. Закон касается и компаний вне ЕС, если их ИИ-системы используются в Евросоюзе.",
                      "Fines: up to 35 million euros or 7% of worldwide turnover for prohibited practices, up to 15 million or 3% for most other violations. The law also covers companies outside the EU if their AI systems are used in the EU.")))


def s_region():
    rows = [("cyan", t("Узбекистан", "Uzbekistan"), t("закон ЗРУ-1115 (январь 2026): решения о правах людей нельзя основывать только на ИИ; стратегия ИИ до 2030", "law ZRU-1115 (January 2026): decisions on people’s rights must not rest on AI alone; AI strategy to 2030")),
            ("green", t("Казахстан", "Kazakhstan"), t("закон «Об искусственном интеллекте» (с 18.01.2026): запрет манипуляций, маркировка", "Law “On Artificial Intelligence” (from 18.01.2026): manipulation ban, labelling")),
            ("violet", t("Россия", "Russia"), t("рамочный закон об ИИ (с 1.09.2026), правила маркировки для крупных платформ — с 1.03.2027", "a framework AI law (from 1.09.2026), labelling rules for large platforms from 1.03.2027")),
            ("amber", t("США · Великобритания", "US · UK"), t("единого закона нет; отдельные правила штатов и отраслей", "no single law; separate state and sector rules"))]
    return dict(min=6, html=f'''
  {head(t("Наш регион", "Our region"), t("В Узбекистане, Казахстане и России уже приняты законы или поправки об ИИ — и у них много общего", "Uzbekistan, Kazakhstan and Russia have already passed AI laws or amendments — with a lot in common"), k="green")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.45fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="light" style="gap:14px">{_lr(rows)}</div>
      <div class="stack" style="gap:18px;">
        <div class="note" style="--k:var(--green)">{t("<b>Общее:</b> человек отвечает за решения, персональные данные защищены; маркировку ИИ-контента уже требует Казахстан, Россия — с 2027.", "<b>In common:</b> a human is accountable for decisions and personal data is protected; Kazakhstan already requires labelling AI content, Russia from 2027.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Это обзор, не юридическая консультация: детали уточняйте у юристов компании.", "This is an overview, not legal advice: check details with your company’s lawyers.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Узбекистан: закон ЗРУ-1115, подписан 21 января 2026, — это поправки к закону об информатизации и Кодексу об административной ответственности. Решения, затрагивающие права человека, нельзя основывать только на результатах ИИ; распространять персональные данные через ИИ запрещено; штрафы 50–100 базовых расчётных величин. Есть стратегия развития ИИ до 2030 года (ПП-358). Обязательна ли маркировка ИИ-контента в финальном тексте — мы не подтвердили, в проекте она была.",
                      "⏱ 6 min. Uzbekistan: law ZRU-1115, signed on 21 January 2026, amends the Law on Informatization and the Code of Administrative Responsibility. Decisions affecting human rights must not rest solely on AI output; spreading personal data via AI is prohibited; fines are 50–100 base calculation units. There is an AI development strategy to 2030 (PP-358). Whether labelling made it into the final text we could not confirm; it was in the draft."),
                    t("Казахстан: закон «Об искусственном интеллекте», подписан 17 ноября 2025, действует с 18 января 2026 — по оценке юристов, первый отдельный закон об ИИ в Центральной Азии: запрет манипулятивного ИИ, обязательная маркировка. Россия: рамочный закон опубликован в июле 2026, общие положения с 1 сентября 2026, правила маркировки для платформ с аудиторией больше 500 тысяч в день — с 1 марта 2027; обязательна ли маркировка, источники расходятся. В США единого федерального закона об ИИ нет: есть законы штатов, указы президента и узкие федеральные законы, например против интимных дипфейков; в Великобритании — отраслевой подход. Это обзор, не юридическая консультация.",
                      "Kazakhstan: the Law “On Artificial Intelligence”, signed on 17 November 2025, in force since 18 January 2026 — described by lawyers as the first standalone AI law in Central Asia: a ban on manipulative AI, mandatory labelling. Russia: a framework law published in July 2026, general provisions from 1 September 2026, labelling rules for platforms with over 500 thousand daily users from 1 March 2027; sources disagree on whether labelling is mandatory. The US has no comprehensive federal AI law: there are state laws, executive orders and narrow federal laws, for example against intimate deepfakes; the UK takes a sector approach. This is an overview, not legal advice.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут: вспомните, что вы вставляли в ИИ на этой неделе", "5 minutes: recall what you pasted into AI this week")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: правила для команды, упражнение, ДЗ.", "Next: team rules, an exercise, homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт».", "⏱ 5 min. Press “Start”.")))


def s_rules():
    rules = [("cyan", t("Одобренные инструменты", "Approved tools"), t("список ИИ, которые можно для работы, и рабочие аккаунты", "a list of AI allowed for work, and business accounts")),
             ("red", t("Светофор данных", "Data traffic light"), t("что можно вставлять, что только в рабочий ИИ, что никогда", "what may be pasted, what only into work AI, what never")),
             ("green", t("Человек проверяет", "A human checks"), t("цифры, ссылки, решения о людях — до отправки", "numbers, links, decisions about people — before sending")),
             ("amber", t("Пометка и инциденты", "Labels and incidents"), t("помечать ИИ-контент; куда сообщить, если что-то утекло", "label AI content; where to report a leak"))]
    li = "".join(f'<div class="task" style="--k:var(--{k});padding:36px 34px;min-height:170px"><div><div class="h" style="font-size:34px">{h}</div><div class="d" style="font-size:24px">{d}</div></div></div>' for k, h, d in rules)
    return dict(min=6, html=f'''
  {head(t("Правила команды", "Team rules"), t("Правила ИИ для команды умещаются на одну страницу: четыре пункта", "AI rules for a team fit on one page: four points"), k="green")}
  <div class="body" style="margin-top:12px;">
    <div class="tasks">{li}</div>
    <div class="note" style="margin-top:26px;--k:var(--cyan)">{t("Это же — шаблон домашнего задания.", "This is also the homework template.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Всё, что мы обсудили, сводится к четырём пунктам, которые помещаются на одну страницу для команды. Первый: список одобренных инструментов и рабочих аккаунтов. Второй: светофор данных. Третий: человек проверяет цифры, ссылки и любые решения о людях до отправки. Четвёртый: как помечать ИИ-контент и куда сообщать, если что-то пошло не так.",
                      "⏱ 6 min. Everything we discussed boils down to four points that fit on one page for a team. One: a list of approved tools and business accounts. Two: the data traffic light. Three: a human checks numbers, links and any decisions about people before sending. Four: how to label AI content and where to report if something goes wrong."),
                    t("Если в компании уже есть политика ИИ — начните с неё и сделайте краткую версию для своей команды. Если нет — это хороший первый шаг, с которым можно прийти к руководителю.",
                      "If your company already has an AI policy, start from it and make a short version for your team. If not, this is a good first step to bring to your manager.")))


def s_exercise():
    cases = [("«Вставлю в ChatGPT договор клиента, чтобы сделать краткое изложение»", "“I’ll paste a client contract into ChatGPT to summarise it”"),
             ("«Сгенерирую картинку для поста в соцсетях компании»", "“I’ll generate an image for the company’s social media post”"),
             ("«ИИ отсортирует резюме, а я приглашу первых пятерых»", "“AI will sort the CVs and I’ll invite the top five”"),
             ("«Директор по видео просит срочно оплатить счёт»", "“The CEO asks on a video call to pay an invoice urgently”")]
    rows = "".join(f'<div class="lrow" style="--k:var(--cyan);padding:22px 24px"><div class="dot"></div><div><div class="h" style="font-size:26px">{t(r, e)}</div><div class="d">{t("можно? что сделать иначе?", "OK? what to do differently?")}</div></div></div>' for r, e in cases)
    return dict(min=6, html=f'''
  {head(t("Упражнение", "Exercise"), t("Упражнение: можно так или нет — и что сделать иначе?", "Exercise: is this OK — and what to do differently?"), k="cyan")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.45fr 1fr;gap:44px;align-items:center;flex:none;">
      <div class="light" style="gap:14px">{rows}</div>
      <div class="note" style="--k:var(--violet)">{t("Ответьте в чат по каждому случаю: «да», «да, но…» или «нет». Разбор — после обсуждения.", "Answer each case in the chat: “yes”, “yes, but…” or “no”. Walk-through after the discussion.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Четыре ситуации в чат. Разбор. Договор клиента в ChatGPT: только в рабочий аккаунт с договором о защите данных, а в личный — нет. Картинка для соцсетей: можно, но проверьте лицензию генератора, не изображайте реальных людей и брендов и помечайте ИИ-контент там, где этого требует закон или площадка.",
                      "⏱ 6 min. Four situations for the chat. Walk-through. A client contract into ChatGPT: only into a business account with a data protection agreement, never a personal one. An image for social media: fine, but check the generator’s licence, do not depict real people or brands, and label AI content where the law or the platform requires."),
                    t("Сортировка резюме: ИИ может помогать, но решение принимает человек, и нужно проверить перекосы — вспомните исследование с именами. Срочная оплата по видео от директора: стоп, перезвоните по известному номеру — это сценарий Arup.",
                      "Sorting CVs: AI may help, but a human decides, and you must check for bias — remember the names study. An urgent payment request on video from the CEO: stop and call back on a known number — that is the Arup scenario.")))


def s_hw():
    steps = [t("Возьмите свою команду и 3 реальных задачи с ИИ", "Take your team and 3 real AI tasks"),
             t("Список одобренных инструментов и аккаунтов", "A list of approved tools and accounts"),
             t("Светофор данных на примерах вашей работы", "A data traffic light with examples from your work"),
             t("Что проверяет человек и как помечать ИИ-контент", "What a human checks and how to label AI content"),
             t("Что делать при утечке или дипфейк-звонке", "What to do on a leak or a deepfake call")]
    ol = "".join(f'<li style="font-size:27px;color:var(--fg)"><span>{s}</span></li>' for s in steps)
    return dict(min=6, html=f'''
  {head(t("Домашнее задание", "Homework"), t("ДЗ: правила ИИ для своей команды на одну страницу", "Homework: one-page AI rules for your team"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:40px;align-items:center;flex:none;">
      <ol class="checklist" style="gap:26px;font-size:26px">{ol}</ol>
      <div class="stack" style="gap:18px;">
        <pre class="code" style="font-size:26px;line-height:1.6">L15_homework/\n├─ ai_rules.md\n└─ README.md</pre>
        <div class="note" style="--k:var(--amber)">{t("Можно попросить ИИ сделать черновик — но проверьте и дополните сами.", "You may ask AI for a draft — but check and complete it yourself.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. ДЗ: одна страница правил ИИ для вашей команды по четырём пунктам урока, на примерах ваших реальных задач. Черновик можно попросить у ИИ, но проверить и дополнить — ваша работа. Без названий клиентов и внутренних данных. Подробности в L15_05_Homework.",
                      "⏱ 6 min. Homework: a one-page set of AI rules for your team covering the four points of the lesson, with examples from your real tasks. You may ask AI for a draft, but checking and completing it is your job. No client names or internal data. Details in L15_05_Homework.")))


def s_summary():
    rules = [("amber", t("Проверяйте", "Check"), t("цифры, ссылки, цитаты — по первоисточнику", "numbers, links, quotes — against the source")),
             ("red", t("Светофор данных", "Data traffic light"), t("рабочее — только в рабочий ИИ", "work data only into work AI")),
             ("violet", t("Человек решает", "A human decides"), t("о людях, деньгах, удалении", "about people, money, deletion")),
             ("cyan", t("Помечайте ИИ", "Label AI"), t("дипфейки и ИИ-контент — там, где требует закон или площадка", "deepfakes and AI content — where the law or platform requires"))]
    li = "".join(f'<div class="task" style="--k:var(--{k});padding:36px 34px;min-height:170px"><div><div class="h" style="font-size:34px">{h}</div><div class="d" style="font-size:24px">{d}</div></div></div>' for k, h, d in rules)
    return dict(min=5, html=f'''
  {head(t("Итоги", "Summary"), t("Итоги урока", "Lesson summary"), k="green")}
  <div class="body" style="margin-top:10px;">
    <div class="tasks">{li}</div>
    <div class="note" style="margin-top:28px;--k:var(--violet)">{t("<b>Дальше, L16:</b> агентная разработка — как агенты пишут код и как ими управлять безопасно.", "<b>Next, L16:</b> agentic software development — how agents write code and how to steer them safely.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Четыре правила. Проверяйте цифры, ссылки и цитаты по первоисточнику. Светофор данных: рабочее — только в рабочий ИИ. Решения о людях, деньгах и удалении принимает человек. Помечайте дипфейки и ИИ-контент там, где этого требует закон или площадка. Последний урок — агентная разработка.",
                      "⏱ 5 min. Four rules. Check numbers, links and quotes against the source. The data traffic light: work data only into work AI. Decisions about people, money and deletion are made by a human. Label deepfakes and AI content where the law or the platform requires it. The last lesson: agentic software development.")))


SLIDES = [s_cover, s_hook, s_halluc, s_leak, s_plans, s_deepfake, s_agents, s_owasp, s_bias, s_labels,
          s_euact, s_region, s_break, s_rules, s_exercise, s_hw, s_summary]


# ---------------------------------------------------------------- page
EXTRA_CSS = """
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
    title = t("Урок 15: Ответственный ИИ | GenAI Basics", "Lesson 15: Responsible AI | GenAI Basics")
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
