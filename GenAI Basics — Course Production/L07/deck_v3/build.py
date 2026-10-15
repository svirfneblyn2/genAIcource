# -*- coding: utf-8 -*-
"""Build the L07 v3 decks (RU + EN) and their PDFs: an overview of the Microsoft Copilot ecosystem.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side. Pictures are real:
own_*  = our captures from the Microsoft Copilot app on 2026-10-13 (synthetic courier data, names blurred),
ms_*   = official Microsoft / GitHub screenshots (support.microsoft.com, blogs, learn), credited on the slide,
yt_*   = frames from official Microsoft / reviewer videos, credited on the slide.
Facts: ../L07_12_Research_MS_Ecosystem_2026-10-13.md (state of 2026-10-13). Plan: ../L07_11_Lesson_Plan_v3_Ecosystem.md.
"""
import html as _html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L07 = HERE.parent
NAME = "presentation_L07_Copilot_Ecosystem"
OUT = {"ru": L07 / f"{NAME}_v3.html", "en": L07 / f"{NAME}_EN_v3.html"}
IMG = "assets/v3/img/"
ART = json.loads((HERE / "artifacts.json").read_text(encoding="utf-8"))

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 07 • Экосистема Microsoft Copilot", "en": "GenAI Basics • Lesson 07 • The Microsoft Copilot ecosystem"}


# ---------------------------------------------------------------- helpers
def esc(s):
    return _html.escape(s, quote=False)


def head(kicker, title, lead=None, k=None, badge=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    b = f' <span class="badge solid" style="--k:var(--amber)">{badge}</span>' if badge else ""
    s = f'<div class="kicker"{ks}>{kicker}{b}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


# availability badges: the same four on every product slide
AV = {"free": ("green", ("бесплатно", "free")), "lic": ("cyan", ("рабочая лицензия", "work licence")),
      "prev": ("amber", ("превью, не у всех", "preview, not for all")), "us": ("violet", ("только США", "US only")),
      "pc": ("pink", ("Copilot+ ПК", "Copilot+ PC"))}


def av(*keys):
    return '<div class="avs">' + "".join(
        f'<span class="av" style="--k:var(--{AV[k][0]})">{t(*AV[k][1])}</span>' for k in keys) + "</div>"


SRC = {  # credit lines, shown under every picture
    "own": ("Наш снимок, 13.10.2026", "Our capture, 13 Oct 2026"),
    "own_dia": ("Наша схема, 13.10.2026", "Our diagram, 13 Oct 2026"),
    "ms_blog": ("Источник: Microsoft, 25.09.2026", "Source: Microsoft, 25 Sep 2026"),
    "ms_support": ("Источник: Microsoft Support, 2026", "Source: Microsoft Support, 2026"),
    "ms_learn": ("Источник: Microsoft Learn, 09.2026", "Source: Microsoft Learn, Sep 2026"),
    "ms_edge": ("Источник: Microsoft Edge blog, 13.05.2026", "Source: Microsoft Edge blog, 13 May 2026"),
    "ms_ai": ("Источник: Microsoft AI, Build 02.06.2026", "Source: Microsoft AI, Build 2 Jun 2026"),
    "ms_win": ("Источник: Windows blog, 16.10.2025", "Source: Windows blog, 16 Oct 2025"),
    "gh": ("Источник: GitHub blog, 02.06.2026", "Source: GitHub blog, 2 Jun 2026"),
    "yt_word": ("Кадр: Microsoft Copilot, YouTube, 09.07.2026", "Frame: Microsoft Copilot, YouTube, 9 Jul 2026"),
    "yt_vision": ("Кадр: Kevin Stratvert, YouTube, 22.10.2025", "Frame: Kevin Stratvert, YouTube, 22 Oct 2025"),
    "yt_mech_win": ("Кадр: Microsoft Mechanics, YouTube, 18.02.2026", "Frame: Microsoft Mechanics, YouTube, 18 Feb 2026"),
    "yt_cowork": ("Кадр: Kevin Stratvert, YouTube, 16.07.2026", "Frame: Kevin Stratvert, YouTube, 16 Jul 2026"),
    "yt_researcher": ("Кадр: Mike Tholfsen, YouTube, 13.04.2026", "Frame: Mike Tholfsen, YouTube, 13 Apr 2026"),
    "yt_studio": ("Кадр: Microsoft Mechanics, YouTube, 05.10.2026", "Frame: Microsoft Mechanics, YouTube, 5 Oct 2026"),
    "yt_foundry": ("Кадр: Microsoft Mechanics, YouTube, 03.12.2025", "Frame: Microsoft Mechanics, YouTube, 3 Dec 2025"),
    "yt_security": ("Кадр: Microsoft Security, YouTube, 03.02.2026", "Frame: Microsoft Security, YouTube, 3 Feb 2026"),
    "yt_teams": ("Кадр: Microsoft Teams, YouTube, 17.07.2026", "Frame: Microsoft Teams, YouTube, 17 Jul 2026"),
}


def shot(img, cap, src, pos="50% 0%", h=None, cls="", tag=None, tagk="cyan"):
    hs = f"height:{h}px;flex:none;" if h else ""
    tg = f'<span class="tag" style="--k:var(--{tagk})">{tag}</span>' if tag else ""
    return (f'<figure class="shot"><div class="fr {cls}" style="{hs}--pos:{pos}">{tg}<img src="{IMG}{img}" alt=""></div>'
            f'<figcaption><span>{cap}</span><span class="src">{t(*SRC[src])}</span></figcaption></figure>')


def thread(txt):
    return f'<div class="thread"><span class="ic">{t("КОМАНДА", "TEAM")}</span><span>{txt}</span></div>'


# ---------------------------------------------------------------- 01 cover
def s_cover():
    return dict(min=2, cls="cover v3", html=f'''
  <div class="bg"><img src="{IMG}ms_copilot_hero.jpg" alt=""></div>
  <div class="shade"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 07 • Экосистема Microsoft", "GenAI Basics • Lesson 07 • The Microsoft ecosystem")}</div>
    <h1>{t("Copilot — это не кнопка, а семья", "Copilot is not a button, it is a family")}</h1>
    <h2>{t("Какие ИИ-помощники есть у Microsoft, где они живут, что из этого бесплатно и как проверять их ответы", "Which AI assistants Microsoft has, where they live, what is free, and how to check their answers")}</h2>
    <p>{t("Карта семьи • для себя • для работы • агенты • для компании • 2 живых демо • ДЗ без лицензии. Все данные курьерского кейса придуманные. Факты на 13.10.2026.",
          "Family map • for you • for work • agents • for companies • 2 live demos • homework without a licence. All courier data is synthetic. Facts as of 13 Oct 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. «Слово Copilot вы видели везде: в Windows, в Edge, в Teams, в Word, на GitHub. Сегодня разберёмся, что это за семья, чем её члены отличаются и что из этого вы можете открыть уже сегодня бесплатно.»",
                      "⏱ 2 min. “You have seen the word Copilot everywhere: Windows, Edge, Teams, Word, GitHub. Today we sort out what this family is, how its members differ, and what you can open today for free.”"),
                    t("На фоне официальная картинка Microsoft от 25 сентября 2026: в сентябре личный и рабочий Copilot объединили в одно приложение. Это главная новость сезона, к ней вернёмся на слайде 6.",
                      "In the background is Microsoft's official picture of 25 September 2026: in September the personal and work Copilot were merged into one app. This is the news of the season; we come back to it on slide 6."),
                    t("Сквозной пример — наша курьерская команда из L04–L06: Анна (продукт), Павел (разработчик), Оля (поддержка) и одна фича: Prime-подписчики получают бесплатную доставку от $75 в городе. Все данные придуманные.",
                      "Running example: our courier team from L04–L06: Anna (product), Pavel (developer), Ola (support) and one feature: Prime subscribers get free delivery from $75 in the city. All data is made up."),
                    t("Перед уроком: открыть Copilot (личный и рабочий вход), запустить опрос в Teams для слайда 2, держать открытыми demo_courier_copilot/meeting_notes.md и release_checklist.txt.",
                      "Before class: open Copilot (personal and work sign-in), prepare the Teams poll for slide 2, keep demo_courier_copilot/meeting_notes.md and release_checklist.txt open.")))


# ---------------------------------------------------------------- 02 poll + ecosystem map
def app(letter, name, color, sm=False, dark=False):
    st = f"--c:{color};" + ("color:#111;" if dark else "")
    return f'<div class="app{" sm" if sm else ""}"><i style="{st}">{letter}</i><span>{name}</span></div>'


def s_map():
    you = "".join([app("✦", "Copilot", "linear-gradient(135deg,#2b7cff,#b14cff 55%,#ff8a3d)"), app("⊞", "Windows 11", "#0078D4"),
                   app("e", "Edge", "linear-gradient(135deg,#0c59a4,#2fd0a0)"), app("Pa", t("Paint, Фото", "Paint, Photos"), "#C239B3"),
                   app("b", "Bing", "#00809D")])
    m365 = "".join([app("W", "Word", "#185ABD"), app("X", "Excel", "#107C41"), app("P", "PowerPoint", "#C43E1C"), app("O", "Outlook", "#0F6CBD"),
                    app("T", "Teams", "#4B53BC"), app("N", "OneNote", "#7719AA"), app("☁", "OneDrive", "#0364B8"), app("S", "SharePoint", "#03787C"),
                    app("L", "Loop, Pages", "linear-gradient(135deg,#5b2bd9,#d04dd9)")])
    dev = "".join([app("GH", "GitHub Copilot", "#24292F"), app("VS", "VS Code", "#007ACC"), app("F", "Foundry", "#5C2D91"),
                   app("CS", "Copilot Studio", "#0B556A")])
    biz = "".join([app("D", "Dynamics 365", "#002050", True), app("PA", "Power Apps", "#742774", True), app("Au", "Power Automate", "#0066FF", True),
                   app("BI", "Power BI, Fabric", "#F2C811", True, True), app("🛡", "Security Copilot", "#1F6FB2", True), app("A", "Agent 365", "#3B3B98", True),
                   app("Dr", "Dragon Copilot", "#00A4EF", True)])
    ags = "".join(f'<span class="ag">{a}</span>' for a in ["Researcher", "Analyst", "Cowork", "Facilitator", "Agent Builder"])
    return dict(min=5, html=f'''
  {head(t("Карта", "The map"), t("Семья ИИ Microsoft: кто где живёт", "The Microsoft AI family: who lives where"),
        t("Один бренд Copilot — четыре зоны. Выбирайте по вопросу: <b>чья это информация и где она лежит?</b>", "One Copilot brand, four zones. Choose by one question: <b>whose information is it and where does it live?</b>"))}
  <div class="body" style="margin-top:12px;justify-content:flex-start;gap:12px;">
    <div class="poll" style="padding:8px 14px;"><b>{t("Опрос в Teams:", "Teams poll:")}</b> {t("какой Copilot у вас уже есть? — в Windows · в Edge · на телефоне · рабочий/учебный · GitHub · никакого", "which Copilot do you already have? in Windows · in Edge · on the phone · work/school · GitHub · none")}</div>
    <div class="eco">
      <div class="grp" style="--k:var(--green)"><div class="gh"><b>{t("Для себя", "For you")}</b><span>{t("личный аккаунт, бесплатно", "personal account, free")}</span></div><div class="apps">{you}</div></div>
      <div class="grp" style="--k:var(--cyan)"><div class="gh"><b>Microsoft 365</b><span>{t("работа и учёба: Copilot Chat бесплатно, с лицензией — ваши данные", "work and school: Copilot Chat free; with a licence, your data")}</span></div>
        <div class="apps">{m365}</div><div class="agents"><span class="lbl">{t("АГЕНТЫ", "AGENTS")}</span>{ags}</div></div>
      <div class="grp" style="--k:var(--violet)"><div class="gh"><b>{t("Для разработчиков", "For developers")}</b><span>{t("код, модели, свои агенты", "code, models, own agents")}</span></div><div class="apps">{dev}</div></div>
      <div class="grp wide" style="--k:var(--amber)"><div class="gh"><b>{t("Для компании", "For the company")}</b><span>{t("включает ИТ-отдел: продажи, процессы, отчёты, безопасность", "turned on by IT: sales, processes, reports, security")}</span></div><div class="apps">{biz}</div></div>
      <div class="core">{t("Внутри всех:", "Inside them all:")} <span class="m">OpenAI GPT</span><span class="m">Anthropic Claude</span><span class="m">Microsoft MAI</span> {t("+ <b>то, что Copilot видит</b> (веб, файл, почта, экран)", "+ <b>what Copilot can see</b> (web, file, mail, screen)")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Сначала опрос (1 мин): «Какой Copilot у вас уже есть?» Ответ «никакого» почти всегда неверный: Copilot уже стоит в Windows 11 и Edge, а у студентов IT Park есть учебный аккаунт с Copilot Chat.",
                      "⏱ 5 min. Poll first (1 min): “Which Copilot do you already have?” “None” is almost always wrong: Copilot ships with Windows 11 and Edge, and IT Park students have a school account with Copilot Chat."),
                    t("Пройдите по карте. Для себя: приложение Copilot, Copilot в Windows 11 и в Edge, картинки в Paint и Фото, поиск Bing — личный аккаунт, бесплатно. В центре Microsoft 365 — пакет для работы и учёбы: Word, Excel, PowerPoint, Outlook, Teams, OneNote, OneDrive, SharePoint, Loop и Pages. В каждом приложении есть кнопка Copilot; с бесплатным Copilot Chat он отвечает по вебу и вставленному тексту, с лицензией Microsoft 365 Copilot — видит ваши письма, файлы и встречи. Там же агенты: Researcher, Analyst, Cowork, Facilitator в Teams и Agent Builder для своих агентов.",
                      "Walk the map. For you: the Copilot app, Copilot in Windows 11 and Edge, images in Paint and Photos, Bing search: personal account, free. In the centre is Microsoft 365, the work and school suite: Word, Excel, PowerPoint, Outlook, Teams, OneNote, OneDrive, SharePoint, Loop and Pages. Every app has a Copilot button; with free Copilot Chat it answers from the web and pasted text, with a Microsoft 365 Copilot licence it sees your mail, files and meetings. Here too are the agents: Researcher, Analyst, Cowork, Facilitator in Teams and Agent Builder for your own agents."),
                    t("Справа разработчики: GitHub Copilot в VS Code и на github.com, Microsoft Foundry — модели и агенты для своих приложений, Copilot Studio — сборка агентов и процессов. Внизу продукты для компании, их включает ИТ-отдел: Dynamics 365, Power Apps, Power Automate, Power BI и Fabric, Security Copilot, Agent 365, Dragon Copilot для врачей. И общее ядро: модели OpenAI, Anthropic и собственные модели Microsoft MAI. Отличается только то, что Copilot видит и что ему разрешено.",
                      "On the right, developers: GitHub Copilot in VS Code and on github.com, Microsoft Foundry for models and agents in your own apps, Copilot Studio for building agents and workflows. Below, company products, turned on by IT: Dynamics 365, Power Apps, Power Automate, Power BI and Fabric, Security Copilot, Agent 365, Dragon Copilot for doctors. And the common core: OpenAI, Anthropic and Microsoft's own MAI models. Only what Copilot sees and is allowed to do differs."),
                    t("Иконки на слайде — упрощённые плитки, не официальные логотипы.", "The icons on the slide are simplified tiles, not official logos.")))


# ---------------------------------------------------------------- 03 new words: model, chat, assistant, agent + parts
def dia(name):
    """Our explainer diagram: the RU file when it exists, otherwise the EN one."""
    ru = f"{name}_ru.png"
    return ru if LANG == "ru" and (L07 / IMG / ru).exists() else f"{name}_en.png"


def dia_slide(name, cap):
    return (f'<div class="body" style="margin-top:10px;align-items:center;">'
            f'<div style="width:1120px;max-width:100%;margin:0 auto;">'
            f'{shot(dia(name), cap, "own_dia", pos="50% 50%", h=630, cls="fit dark")}</div></div>')


def s_terms():
    return dict(min=2, html=f'''
  {head(t("Новые слова", "New words"), t("Модель → чат → ассистент → агент", "Model → chat → assistant → agent"),
        t("Каждая ступень = предыдущая <b>+ одна новая способность</b>.", "Each stage = the previous one <b>+ one new ability</b>."))}
  {dia_slide("own_dia_agent_stages", t("Четыре ступени: что добавляет каждая и пример из Copilot", "Four stages: what each one adds, with a Copilot example"))}''',
                notes=notes(
                    t("⏱ 2 мин. «На карте мы увидели слова: Copilot, агенты, Agent Builder. Прежде чем идти дальше — договоримся, что они значат.»",
                      "⏱ 2 min. “On the map we saw words like Copilot, agents, Agent Builder. Before we go on, let's agree on what they mean.”"),
                    t("Читаем слева направо. Модель — это LLM, большая языковая модель, которую вы вызывали из Python в L03: текст на входе, текст на выходе. Сама она ничего не видит и ничего не делает. Чат — модель плюс окно разговора: вы спросили, она ответила и помнит эту беседу. Пример — Copilot Chat. Ассистент живёт внутри приложения и видит ваш файл: Copilot в Word подсвечивает абзац и предлагает правку, но решаете и делаете вы. Агент получает цель — «подготовь встречу с клиентом в пятницу» — и сам крутит цикл «план → действие → проверка»: пишет письмо, ставит встречу, готовит файл. Почту, календарь и файлы он открывает через коннекторы. Результат вы утверждаете. Пример — Copilot Cowork.",
                      "Read left to right. A model is the LLM, the large language model you called from Python in L03: text in, text out. By itself it sees nothing and does nothing. A chat is a model plus a conversation window: you ask, it answers and remembers this conversation. Example: Copilot Chat. An assistant lives inside an app and sees your file: Copilot in Word highlights a paragraph and suggests an edit, but you decide and do the work. An agent gets a goal, “prepare Friday's client meeting”, and runs the loop plan → act → check by itself: drafts the email, books the meeting, prepares the file. It reaches email, calendar and files through connectors. You approve the result. Example: Copilot Cowork.")))


def s_assist_agent():
    return dict(min=2, html=f'''
  {head(t("Новые слова", "New words"), t("Ассистент или агент: кто ведёт работу", "Assistant or agent: who drives the work"),
        t("Ассистент отвечает на <b>одну просьбу</b>. Агент получает <b>цель</b>, сам делает много шагов, а вы утверждаете.", "An assistant answers <b>one request</b>. An agent gets a <b>goal</b>, takes many steps itself, and you approve."))}
  {dia_slide("own_dia_assistant_vs_agent", t("Один и тот же Copilot в двух ролях", "The same Copilot in two roles"))}''',
                notes=notes(
                    t("⏱ 2 мин. «Это самая важная разница сегодняшнего урока. Запомните: либо ведёте вы, либо ведёт он.»",
                      "⏱ 2 min. “This is the most important difference in today's lesson. Remember: either you drive, or it drives.”"),
                    t("Слева ассистент. Вы просите «сократи этот абзац», Copilot отвечает прямо в Word, вы принимаете правку и следующий шаг делаете сами. Одна просьба — один ответ. Справа агент. Вы ставите цель: «подготовь встречу с клиентом в пятницу». Агент сам планирует, действует и проверяет: смотрит календарь, пишет письмо, собирает файл. Перед важными действиями, например отправкой письма, он спрашивает ваше «да». Одна цель — много шагов, потом ваше подтверждение.",
                      "On the left is the assistant. You ask “shorten this paragraph”, Copilot answers right in Word, you accept the edit and take the next step yourself. One request, one answer. On the right is the agent. You set a goal: “prepare Friday's client meeting”. The agent plans, acts and checks by itself: looks at the calendar, drafts the email, builds the file. Before important actions such as sending the email it asks for your “yes”. One goal, many steps, then your OK.")))


def s_anatomy():
    return dict(min=2, html=f'''
  {head(t("Свой агент • из чего он собран", "Your own agent • what it is made of"), t("Анатомия агента", "Anatomy of an agent"), k="amber",
        lead=t("<b>Харнесс</b> — программа, которая крутит цикл и подключает остальные детали. В Agent Builder вы заполняете их сами.", "The <b>harness</b> is the program that runs the loop and plugs in the other parts. In Agent Builder you fill them in yourself."))}
  {dia_slide("own_dia_agent_anatomy", t("Пять деталей вокруг модели и коннекторы к системам компании", "Five parts around the model and connectors to company systems"))}''',
                notes=notes(
                    t("⏱ 2 мин. «Сейчас мы соберём своего агента. Сначала посмотрим, из каких деталей он состоит.»",
                      "⏱ 2 min. “We are about to build our own agent. First, let's see which parts it is made of.”"),
                    t("В центре модель — тот же LLM. Вокруг неё харнесс: программа, которая крутит цикл «план → действие → проверка» и подключает пять деталей. Инструкция — роль, правила и цель. Контекст — то, что агент видит прямо сейчас: переписку, открытый файл, результаты шагов. Инструмент — одно действие, например «отправить письмо». Навык, или скилл, — готовый рецепт из нескольких шагов, например «собрать отчёт». Коннектор — доступ к системе компании: почте, файлам, базе клиентов (CRM). Подробно про коннекторы и MCP — в L12.",
                      "In the centre is the model, the same LLM. Around it is the harness: the program that runs the loop plan → act → check and plugs in five parts. Instruction: role, rules and goal. Context: what the agent sees right now: the conversation, the open file, the results of its steps. Tool: one action, such as “send an email”. Skill: a ready recipe of several steps, such as “build a report”. Connector: access to a company system: mail, files, the customer database (CRM). Connectors and MCP in detail come in L12."),
                    t("Мостик: на следующих двух слайдах заполним эти детали в Agent Builder — инструкцию, знания, навыки — и получим работающего агента.",
                      "Bridge: on the next two slides we fill these parts in Agent Builder (instructions, knowledge, skills) and get a working agent.")))


# ---------------------------------------------------------------- 03 same models, three levels
def s_models():
    lad = "".join(f'<div class="stp" style="--k:var(--{k});min-height:{hgt}px"><div class="n">{n}</div><div class="h">{h}</div><div class="d">{d}</div></div>'
                  for k, hgt, n, h, d in [
                      ("green", 170, t("УРОВЕНЬ 1", "LEVEL 1"), t("Отвечает", "Answers"), t("чат: вопрос → текст. Вы копируете сами.", "chat: question → text. You copy it yourself.")),
                      ("cyan", 220, t("УРОВЕНЬ 2", "LEVEL 2"), t("Правит документ", "Edits the document"), t("Word, Excel, PowerPoint: меняет файл, вы видите, что изменилось.", "Word, Excel, PowerPoint: changes the file, you see what changed.")),
                      ("amber", 270, t("УРОВЕНЬ 3", "LEVEL 3"), t("Делает работу (агент)", "Does the work (agent)"), t("сам планирует шаги: ищет, пишет письма, собирает файлы. Спрашивает разрешения.", "plans the steps itself: searches, drafts emails, builds files. Asks for approval."))])
    return dict(min=3, html=f'''
  {head(t("Как это устроено", "How it works"), t("Внутри — те же модели, что вы вызывали в L03", "Inside are the same models you called in L03"),
        t("Copilot — это обёртка: <b>модель + то, что она видит + то, что ей разрешено делать</b>.", "Copilot is a wrapper: <b>a model + what it can see + what it is allowed to do</b>."))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="stack" style="gap:22px;">
        <div class="ladder">{lad}</div>
        <ul class="pts sm">
          <li>{t("<b>Модели:</b> OpenAI GPT, Anthropic Claude и собственные модели Microsoft (MAI). Режим <b>Auto</b> выбирает модель сам.", "<b>Models:</b> OpenAI GPT, Anthropic Claude and Microsoft's own MAI models. <b>Auto</b> picks the model for you.")}</li>
          <li>{t("Названия моделей меняются каждый месяц — запоминайте не их, а уровни.", "Model names change every month: remember the levels, not the names.")}</li>
        </ul>
      </div>
      <div class="stack" style="gap:14px;">
        {shot("own_work_model_picker.jpg", t("Наш рабочий Copilot: <b>Auto, быстрый ответ, «подумать дольше», GPT-5.6</b>", "Our work Copilot: <b>Auto, quick, think deeper, GPT-5.6</b>"), "own", pos="0% 0%", h=470)}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. «В L03 вы сами вызывали модель из Python. Copilot делает тот же вызов за вас и подставляет в запрос ваш контекст: файл, письмо, экран.»",
                      "⏱ 3 min. “In L03 you called a model from Python yourself. Copilot makes the same call for you and adds your context to the request: a file, an email, the screen.”"),
                    t("Три уровня помогут не путаться в названиях. Первый — отвечает: обычный чат. Второй — правит документ: Copilot в Word или Excel сам меняет файл. Третий — агент: вы описываете результат, а он сам планирует шаги и выполняет их, спрашивая разрешения перед важным.",
                      "Three levels keep the names apart. One: answers, an ordinary chat. Two: edits the document: Copilot in Word or Excel changes the file itself. Three: an agent: you describe the result and it plans and runs the steps, asking before anything important."),
                    t("Справа наш настоящий снимок: рабочий Copilot IT Park, меню модели. Видно Auto и GPT-5.6. В платной версии в этом меню есть и Claude. На Build 2026 Microsoft показала семь собственных моделей MAI. Вывод: Copilot не одна модель, а несколько, и Microsoft выбирает их под задачу.",
                      "On the right is our real capture: the IT Park work Copilot, model menu. You see Auto and GPT-5.6. With a paid licence the menu also shows Claude. At Build 2026 Microsoft showed seven of its own MAI models. Takeaway: Copilot is not one model but several, chosen for the task.")))


# ---------------------------------------------------------------- 04 one app, two doors
def s_app():
    dct = [(t("Office app", "Office app"), t("Microsoft 365 Copilot app", "Microsoft 365 Copilot app"), "Microsoft Copilot"),
           ("Bing Chat", "", "Copilot"), ("Copilot Pro", "", t("закрыт → Microsoft 365 Premium", "retired → Microsoft 365 Premium"))]
    drow = "".join(f'<div class="dict"><span class="old">{a}</span><span class="arr">→</span>{f"<span class=old>{b}</span><span class=arr>→</span>" if b else ""}<span class="new">{c}</span></div>' for a, b, c in dct)
    return dict(min=4, html=f'''
  {head(t("Приложение", "The app"), t("Одно приложение Microsoft Copilot — два входа", "One Microsoft Copilot app, two doors"),
        t("С сентября 2026 личный и рабочий Copilot — одно приложение. <b>Данные между аккаунтами не смешиваются.</b>", "Since September 2026 the personal and work Copilot are one app. <b>Data never flows between the accounts.</b>"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.05fr 1fr;gap:30px;flex:none;align-items:start;">
      <div class="stack" style="gap:12px;">
        {shot("own_account_switcher.jpg", t("Переключатель аккаунтов: <b>личный</b> и <b>рабочий IT Park</b> в одном окне", "Account switcher: <b>personal</b> and <b>IT Park work</b> in one window"), "own", pos="0% 45%", h=330)}
        <div class="row" style="grid-template-columns:1fr 1fr;gap:16px;flex:none;">
          <div class="note" style="--k:var(--green);font-size:18px;"><b>{t("Личный", "Personal")}</b>: {t("чат, голос, картинки; видит веб и то, что вы дали", "chat, voice, images; sees the web and what you give it")}</div>
          <div class="note" style="--k:var(--cyan);font-size:18px;"><b>{t("Рабочий", "Work")}</b>: {t("Copilot Chat бесплатно; с лицензией — ваша почта, файлы, встречи", "Copilot Chat free; with a licence: your mail, files, meetings")}</div>
        </div>
      </div>
      <div class="stack" style="gap:14px;">
        {shot("ms_app_home.jpg", t("Новый Copilot: вкладки <b>Home · Code · Autopilot</b>", "The new Copilot: <b>Home · Code · Autopilot</b> tabs"), "ms_blog", pos="50% 45%", h=260)}
        <div class="stack" style="gap:8px;"><div class="prompt-label">{t("Словарь имён", "Name dictionary")}</div>{drow}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «Если запутались в названиях — вы не одни. Microsoft переименовывала эти продукты несколько раз за два года.»",
                      "⏱ 4 min. “If the names confuse you, you are not alone. Microsoft renamed these products several times in two years.”"),
                    t("Слева наш снимок: одно приложение Microsoft Copilot, внизу переключатель аккаунтов. Личный аккаунт и рабочий аккаунт IT Park живут рядом, но данные между ними не перетекают. Почты и фото на снимке закрыты.",
                      "On the left is our capture: one Microsoft Copilot app with the account switcher. The personal account and the IT Park work account sit side by side, but data does not flow between them. E-mails and photos are hidden."),
                    t("Главное различие для работы. Copilot Chat — бесплатный для рабочих и учебных аккаунтов: отвечает по вебу и по тому, что вы вставили или загрузили, с корпоративной защитой данных (зелёный щит). Microsoft 365 Copilot — платная лицензия: Copilot видит вашу почту, файлы, встречи и чаты. У нашего аккаунта IT Park — Copilot Chat (Basic), без лицензии. У вас, скорее всего, так же.",
                      "The key difference at work. Copilot Chat is free for work and school accounts: it answers from the web and from what you paste or upload, with enterprise data protection (the green shield). Microsoft 365 Copilot is a paid licence: Copilot sees your mail, files, meetings and chats. Our IT Park account has Copilot Chat (Basic), no licence. Yours most likely too."),
                    t("Справа официальная картинка: новое приложение с тремя вкладками. Home — чат и агент Cowork. Code — собрать маленькое приложение словами. Autopilot — фоновый агент, пока в превью. Словарь внизу: Office app стал Microsoft 365 Copilot app, а теперь просто Microsoft Copilot; Bing Chat — это Copilot; Copilot Pro закрыт и заменён подпиской Microsoft 365 Premium.",
                      "On the right is the official picture: the new app with three tabs. Home: chat and the Cowork agent. Code: build a small app by describing it. Autopilot: a background agent, still in preview. The dictionary below: the Office app became the Microsoft 365 Copilot app, now simply Microsoft Copilot; Bing Chat is Copilot; Copilot Pro was retired and replaced by Microsoft 365 Premium.")))


# ---------------------------------------------------------------- 05 money
def s_money():
    tiers = [
        ("green", t("Бесплатно", "Free"), t("у всех", "everyone"), [(t("Copilot (личный)", "Copilot (personal)"), "$0"), (t("Copilot Chat (рабочий)", "Copilot Chat (work)"), "$0"), ("GitHub Copilot Free", "$0")]),
        ("violet", t("Для дома", "Home"), t("подписка Microsoft 365, в месяц", "Microsoft 365, per month"), [("Personal", "$9.99"), ("Family", "$12.99"), (t("Premium: Researcher, Analyst", "Premium: Researcher, Analyst"), "$19.99")]),
        ("cyan", t("Для работы", "Work"), t("за человека в месяц, годовой договор", "per user per month, annual"), [("Copilot Business", "$21"), ("Microsoft 365 Copilot", "$30"), ("GitHub Copilot Business", "$19")]),
        ("amber", t("Агенты", "Agents"), t("оплата по использованию", "pay as you go"), [("Cowork, Code, Autopilot", t("кредиты", "credits")), (t("новейшие модели", "newest models"), t("кредиты", "credits")), ("GitHub AI Credits", "$0.01")]),
    ]
    cols = "".join(f'<div class="tier" style="--k:var(--{k});min-height:{200 + i * 30}px"><div class="h">{h}</div><div class="who">{w}</div>'
                   + "".join(f'<div class="ln"><span>{a}</span><b>{b}</b></div>' for a, b in lines) + '</div>'
                   for i, (k, h, w, lines) in enumerate(tiers))
    return dict(min=3, html=f'''
  {head(t("Деньги", "Money"), t("Что бесплатно, а что платно", "What is free and what is paid"),
        t("Для учёбы и этого урока хватает бесплатного. Цены США, <b>на 13.10.2026</b>, изменятся после Microsoft Ignite (17–20.11).", "Free is enough for study and this lesson. US prices <b>as of 13 Oct 2026</b>; expect changes after Microsoft Ignite (17–20 Nov)."),
        badge=t("ОКТЯБРЬ 2026", "OCTOBER 2026"))}
  <div class="body">
    <div class="price">{cols}</div>
    <div class="note" style="--k:var(--green);margin-top:24px;">{t("Студентам IT Park: учебный аккаунт = <b>Copilot Chat бесплатно</b>; GitHub даёт студентам <b>Copilot Student</b>. Остальное в ДЗ не нужно.", "IT Park students: a school account = <b>Copilot Chat for free</b>; GitHub gives students <b>Copilot Student</b>. Nothing else is needed for the homework.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Единственный слайд урока с ценами. «Цены меняются, поэтому названия планов и цифры есть только здесь, с датой.»",
                      "⏱ 3 min. The only slide with prices. “Prices change, so plan names and numbers live only here, with a date.”"),
                    t("Слева направо — лестница. Бесплатно: личный Copilot, рабочий Copilot Chat и GitHub Copilot Free. Для дома: подписки Microsoft 365 Personal, Family и Premium; в Premium есть агенты Researcher и Analyst. Copilot Pro больше не продаётся. Для работы: Copilot Business для небольших компаний $21 и Microsoft 365 Copilot $30 за человека в месяц.",
                      "Left to right is a ladder. Free: personal Copilot, work Copilot Chat and GitHub Copilot Free. Home: Microsoft 365 Personal, Family and Premium; Premium includes the Researcher and Analyst agents. Copilot Pro is no longer sold. Work: Copilot Business for small companies at $21 and Microsoft 365 Copilot at $30 per user per month."),
                    t("Агенты — отдельная история: Cowork, Code, Autopilot и самые новые модели оплачиваются по использованию, в кредитах. Это новинка 2026 года. Для домашнего задания ничего платного не нужно.",
                      "Agents are a separate story: Cowork, Code, Autopilot and the newest models are billed by usage, in credits. This is new in 2026. Nothing paid is needed for the homework.")))


# ---------------------------------------------------------------- 06 for you + demo A
def s_you():
    return dict(min=3, html=f'''
  {head(t("Демо A • бесплатный Copilot", "Demo A • free Copilot"), t("Заметки встречи → бриф → картинка-анонс", "Meeting notes → brief → launch picture"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:28px;flex:none;align-items:start;">
      {shot("own_work_chat_brief_1.jpg", t("Copilot Chat, учебный аккаунт IT Park, <b>без лицензии</b>: бриф по нашим заметкам", "Copilot Chat, IT Park school account, <b>no licence</b>: a brief from our notes"), "own", pos="50% 0%", h=400, tag="Copilot Chat (Basic)", tagk="green")}
      <div class="stack" style="gap:14px;">
        {shot("own_prime_poster.jpg", t("Личный Copilot: <b>картинка за 30 секунд</b>", "Personal Copilot: <b>a picture in 30 seconds</b>"), "own", pos="50% 50%", h=232)}
        <div class="steps3" style="--k:var(--amber)">
          <div>{t("Вставить <code>meeting_notes.md</code>: «Только по этим заметкам — бриф. <b>В конце: что ты добавил сам</b>».", "Paste <code>meeting_notes.md</code>: “Only from these notes, a brief. <b>At the end: what you added yourself</b>.”")}</div>
          <div>{t("Сверить: $75 Prime, $100 для всех, вне зоны без изменений.", "Check: $75 Prime, $100 for all, outside the zone unchanged.")}</div>
          <div>{t("«Нарисуй картинку-анонс» → редактор: стереть, фон, кадрировать.", "“Draw a launch picture” → editor: erase, background, crop.")}</div>
        </div>
      </div>
    </div>
    <div style="margin-top:14px;">{av("free")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Коротко покажите, что есть в приложении; живое демо — по желанию. Откройте приложение Copilot под учебным аккаунтом (Copilot Chat) — так же, как будет у студентов.",
                      "⏱ 3 min. Briefly show what the app has; the live demo is optional. Open the Copilot app with the school account (Copilot Chat), exactly as students will."),
                    t("Шаг 1. Вставьте заметки встречи и промпт со слайда. Важная часть промпта — «перечисли, что добавил от себя». Это простая защита от выдумок. На нашем запуске 13.10 Copilot один раз ответил «ничего не добавлено», а в другой раз честно перечислил: структуру разделов и пояснение, что rollout — это поэтапный запуск. Один и тот же промпт даёт разные ответы — это нормально, поэтому проверяем.",
                      "Step 1. Paste the meeting notes and the prompt from the slide. The key part is “list what you added yourself”. A simple guard against invention. In our run on 13 Oct, once Copilot said “nothing added”, another time it honestly listed the section structure and an explanation that rollout means a staged launch. The same prompt gives different answers; that is normal, which is why we check."),
                    t("Шаг 2. Проверка по источнику вслух вместе с группой: $75 только для Prime и только в городе; $100 бесплатно для всех остаётся; вне зоны ничего не меняется; кто ведёт флаг — открытый вопрос.",
                      "Step 2. Check against the source out loud with the group: $75 only for Prime and only in the city; free from $100 for everyone stays; nothing changes outside the zone; who owns the flag is an open question."),
                    t("Шаг 3. Личный аккаунт: «Нарисуй картинку-анонс…». Справа наш результат. Откройте картинку: там встроенный редактор — Erase, Upscale, Edit object, Background, Crop. Это то, что раньше называлось Designer. Если интернет или аккаунт подвёл: этот слайд и есть результат, не чините больше 90 секунд.",
                      "Step 3. Personal account: “Draw a launch picture…”. On the right is our result. Open the picture: there is a built-in editor: Erase, Upscale, Edit object, Background, Crop. This used to be called Designer. If the network or account fails: this slide is the result; do not troubleshoot for more than 90 seconds.")))


# ---------------------------------------------------------------- 07 Vision wow
def s_vision():
    return dict(min=3, html=f'''
  {head(t("Демо B • вау", "Demo B • wow"), t("Copilot Vision: помощник видит окно, которое вы показали", "Copilot Vision: the assistant sees the window you share"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:28px;flex:none;align-items:start;">
      {shot("yt_vision_picker.jpg", t("Copilot в Windows: <b>Share screen / Share app</b> — вы выбираете, что показать", "Copilot in Windows: <b>Share screen / Share app</b>: you choose what to show"), "yt_vision", pos="50% 60%", h=430)}
      <div class="stack" style="gap:16px;">
        <div class="steps3" style="--k:var(--amber)">
          <div>{t("Открыть <code>release_checklist.txt</code> в Блокноте.", "Open <code>release_checklist.txt</code> in Notepad.")}</div>
          <div>{t("Copilot → голос → <b>Vision</b> → выбрать окно Блокнота.", "Copilot → voice → <b>Vision</b> → pick the Notepad window.")}</div>
          <div>{t("Спросить: «Какой пункт поймает изменение платы вне зоны?» → пункт 6.", "Ask: “Which item catches a fee change outside the zone?” → item 6.")}</div>
        </div>
        <ul class="pts sm">
          <li>{t("Видит <b>только выбранное окно</b> и только пока вы делитесь.", "Sees <b>only the chosen window</b>, only while you share.")}</li>
          <li>{t("Подсказывает и подсвечивает, <b>но не кликает за вас</b>.", "Points and highlights, <b>but does not click for you</b>.")}</li>
          <li>{t("Нет микрофона — вставьте текст в чат: результат тот же.", "No microphone? Paste the text into chat: same result.")}</li>
        </ul>
        {av("free", "prev")}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Вау-момент урока. «До сих пор мы копировали текст в чат. Теперь Copilot сам посмотрит на окно.»",
                      "⏱ 3 min. The wow moment. “So far we pasted text into chat. Now Copilot looks at the window itself.”"),
                    t("Слева кадр из обзора: окно Copilot в Windows и выбор, чем поделиться — весь экран или одно приложение. Выбирайте одно приложение: так Copilot не увидит ничего лишнего.",
                      "On the left is a frame from a review: the Copilot window in Windows and the choice of what to share, the whole screen or one app. Choose one app: then Copilot sees nothing extra."),
                    t("Живое демо: откройте чек-лист релиза, включите Vision, выберите Блокнот и спросите голосом. Правильный ответ — пункт 6: «Откатить флаг, если плата вне зоны неожиданно изменилась». Vision для личных аккаунтов работает в 170+ странах; для рабочих аккаунтов только выкатывается — поэтому значок «превью».",
                      "Live demo: open the release checklist, turn on Vision, pick Notepad and ask by voice. The right answer is item 6: “Roll back the flag if outside-zone fees change unexpectedly.” Vision for personal accounts works in 170+ markets; for work accounts it is only rolling out, hence the preview badge."),
                    t("Запасной путь без микрофона: вставьте текст чек-листа в чат и задайте тот же вопрос. Правило то же, что на слайде 5: Copilot видит только то, что вы ему показали.",
                      "Fallback without a microphone: paste the checklist text into chat and ask the same question. Same rule as slide 5: Copilot sees only what you show it.")))


# ---------------------------------------------------------------- 08 Windows: what you can do and the limits
def s_windows():
    can = [t("<b>Чат и голос</b> — на любом ПК с Windows 11; «Hey Copilot» включается в настройках.", "<b>Chat and voice</b>: on any Windows 11 PC; “Hey Copilot” is a setting."),
           t("<b>Скриншот и Vision</b> — показать окно; Copilot подсвечивает, но <b>не кликает</b>.", "<b>Screenshot and Vision</b>: share a window; Copilot highlights but <b>does not click</b>."),
           t("<b>Файлы</b> — загрузить или найти на ПК и спросить по ним.", "<b>Files</b>: upload or find on the PC and ask about them."),
           t("<b>Создать</b> картинку, файл Word, Excel, PowerPoint из ответа.", "<b>Create</b> an image or a Word, Excel, PowerPoint file from an answer."),
           t("<b>Подключить</b> OneDrive, Outlook.com, Gmail, Google Drive, Календарь — на copilot.com и в телефоне.", "<b>Connect</b> OneDrive, Outlook.com, Gmail, Google Drive, Calendar: on copilot.com and mobile.")]
    canl = "".join(f"<li>{x}</li>" for x in can)
    lim = [("green", "20", t("файлов в одном чате", "files per chat")), ("green", "50 MB", t("на файл: PDF, DOCX, XLSX, PPTX, PNG, JPEG, TXT, CSV, MD", "per file: PDF, DOCX, XLSX, PPTX, PNG, JPEG, TXT, CSV, MD")),
           ("cyan", t("18 мес", "18 mo"), t("хранится история чатов (по умолчанию)", "chat history kept (default)")),
           ("amber", "?", t("лимит сообщений, длины, картинок и голоса <b>Microsoft не публикует</b>; подписка Microsoft 365 даёт больше", "message, length, image and voice limits <b>are not published</b>; a Microsoft 365 subscription gives more")),
           ("pink", "Copilot+", t("только на Copilot+ ПК: Click to Do, Recall, агент в Параметрах", "Copilot+ PC only: Click to Do, Recall, the Settings agent"))]
    liml = "".join(f'<div class="ln" style="--k:var(--{k})"><b style="min-width:120px;color:var(--{k})">{n}</b><span>{d}</span></div>' for k, n, d in lim)
    return dict(min=5, html=f'''
  {head(t("На вашем ПК • Windows и Edge", "On your PC • Windows and Edge"), t("Copilot в Windows: что можно и где границы", "Copilot in Windows: what it can do and where the limits are"))}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1.05fr 1fr;gap:28px;flex:none;align-items:start;">
      <div class="stack" style="gap:12px;">
        <div class="prompt-label">{t("Что можно бесплатно (личный аккаунт)", "What you can do for free (personal account)")}</div>
        <ul class="pts sm" style="--k:var(--green)">{canl}</ul>
        {shot("yt_ask_copilot_taskbar.jpg", t("<b>Ask Copilot</b> на панели задач", "<b>Ask Copilot</b> on the taskbar"), "yt_mech_win", pos="50% 10%", h=190)}
      </div>
      <div class="stack" style="gap:12px;">
        <div class="prompt-label">{t("Ограничения (официально на 13.10.2026)", "Limits (official, as of 13 Oct 2026)")}</div>
        <div class="tier" style="--k:var(--line);border-color:var(--line);background:var(--surface);gap:6px;">{liml}</div>
        <div class="note" style="--k:var(--red);font-size:18px;">{t("Личный аккаунт: обучение на ваших чатах <b>включено по умолчанию</b>. Выключить: профиль → Settings → Privacy → <b>Training on conversation activity</b>.", "Personal account: training on your chats is <b>on by default</b>. Turn it off: profile → Settings → Privacy → <b>Training on conversation activity</b>.")}</div>
        <div class="small">{t("Edge: вопросы по открытым вкладкам и истории, Journeys. Отдельный Copilot Mode закрыт в мае 2026; действия в браузере — Premium, только США.", "Edge: questions about open tabs and history, Journeys. The separate Copilot Mode closed in May 2026; browser actions: Premium, US only.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. «Copilot в Windows уже стоит у каждого. Разберёмся, что он умеет бесплатно и где упирается.»",
                      "⏱ 5 min. “Copilot is already on everyone's Windows. Let's see what it does for free and where it stops.”"),
                    t("Что можно на обычном ПК с Windows 11 и личным аккаунтом: чат и голос; вход по клавише Copilot или Win+C; «Hey Copilot» — по желанию в настройках. Скриншот или Vision: вы показываете окно, Copilot подсвечивает, куда нажать, но сам ничего не кликает. Файлы: можно загрузить или попросить найти файл на компьютере и задать вопрос. Можно создать картинку, а также файл Word, Excel или PowerPoint из ответа. Коннекторы к OneDrive, Outlook.com, Gmail и Google Drive работают на copilot.com и в телефоне; для них Microsoft называет подписку Microsoft 365.",
                      "What works on a normal Windows 11 PC with a personal account: chat and voice; open with the Copilot key or Win+C; “Hey Copilot” is an optional setting. Screenshot or Vision: you share a window, Copilot highlights where to click but clicks nothing itself. Files: upload one or ask it to find a file on the PC and ask about it. Create an image or a Word, Excel or PowerPoint file from an answer. Connectors to OneDrive, Outlook.com, Gmail and Google Drive work on copilot.com and mobile; Microsoft lists a Microsoft 365 subscription for them."),
                    t("Официальные цифры только такие: до 20 файлов в чате, до 50 МБ на файл, история хранится 18 месяцев. Лимиты на число сообщений, длину запроса, число картинок и минуты голоса Microsoft для бесплатного уровня не публикует — в интернете ходят цифры вроде «15 быстрых картинок», но это неофициально. Подписки Microsoft 365 Personal, Family, Premium дают «больше» — тоже без чисел.",
                      "The only official numbers: up to 20 files per chat, up to 50 MB per file, history kept 18 months. Microsoft does not publish message, prompt-length, image or voice limits for the free tier; numbers like “15 fast images” online are unofficial. Microsoft 365 Personal, Family and Premium give “more”, also without numbers."),
                    t("Только на Copilot+ ПК с нейропроцессором: Click to Do, Recall и агент в Параметрах. Copilot Actions, когда агент сам работает в приложениях, пока только у инсайдеров. Важное про приватность: в личном аккаунте обучение на ваших разговорах включено по умолчанию — покажите, где выключить: профиль, Settings, Privacy, Training on conversation activity. Для рабочих и учебных аккаунтов обучения нет.",
                      "Copilot+ PCs with an NPU only: Click to Do, Recall and the Settings agent. Copilot Actions, where an agent works inside apps, is still Insider-only. Privacy: in a personal account training on your conversations is on by default; show where to turn it off: profile, Settings, Privacy, Training on conversation activity. Work and school accounts are never used for training.")))


# ---------------------------------------------------------------- 09 Teams
def s_teams():
    return dict(min=6, html=f'''
  {head(t("Для работы • Teams", "For work • Teams"), t("Teams: встреча превращается в итоги и задачи", "Teams: a meeting becomes a recap and tasks"), k="cyan")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:26px;flex:none;align-items:start;">
      {shot("ms_teams_facilitator.jpg", t("<b>Facilitator</b> в встрече: повестка, таймер, живые заметки, ответы в чате", "<b>Facilitator</b> in a meeting: agenda, timer, live notes, chat answers"), "ms_support", pos="50% 0%", h=380)}
      <div class="stack" style="gap:12px;">
        {shot("ms_teams_recap_copilot.jpg", t("<b>Recap</b> после встречи: итоги, задачи, вопросы к Copilot", "<b>Recap</b> after the meeting: notes, tasks, questions to Copilot"), "ms_support", pos="100% 0%", h=190)}
        <ul class="pts sm">
          <li>{t("<b>Во время:</b> «что я пропустил?», «какие вопросы остались открытыми?»", "<b>During:</b> “what did I miss?”, “what is still open?”")}</li>
          <li>{t("<b>После:</b> итоги, задачи с именами, документ Word по встрече.", "<b>After:</b> notes, tasks with names, a Word document of the meeting.")}</li>
          <li>{t("Нужна <b>расшифровка</b> встречи; @Copilot в чате — превью.", "Needs the meeting <b>transcript</b>; @Copilot in chat is in preview.")}</li>
        </ul>
        {av("lic", "prev")}
      </div>
    </div>
    <div style="margin-top:12px;">{thread(t("Анна не вела заметки на встрече в понедельник: Facilitator записал <b>3 решения, 2 открытых вопроса и 3 задачи</b>.", "Anna took no notes in Monday's meeting: Facilitator wrote down <b>3 decisions, 2 open questions and 3 tasks</b>."))}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин, живой показ. «Урок идёт в Teams — значит, вы уже сидите внутри одного из Copilot.»",
                      "⏱ 6 min, live. “This lesson runs in Teams, so you are already sitting inside one of the Copilots.”"),
                    t("Слева официальный скриншот Microsoft: агент Facilitator во встрече. Он ведёт повестку с таймером по темам, пишет общие заметки, которые участники могут править, и отвечает на вопросы в чате встречи. После встречи может сделать документ Word.",
                      "On the left is Microsoft's official screenshot: the Facilitator agent in a meeting. It runs the agenda with a timer per topic, writes shared notes participants can edit, and answers questions in the meeting chat. After the meeting it can produce a Word document."),
                    t("Справа Recap — вкладка «Итоги» после встречи: заметки ИИ, задачи, главы, кто что говорил. Внутри можно спросить Copilot: «какие вопросы остались открытыми?». Всё это работает, только если включена расшифровка и есть лицензия Microsoft 365 Copilot. Без лицензии в Teams есть Copilot Chat и подсказки ответов.",
                      "On the right is Recap, the tab after the meeting: AI notes, tasks, chapters, who said what. Inside you can ask Copilot: “which questions are still open?”. All of this needs the transcript turned on and a Microsoft 365 Copilot licence. Without a licence Teams has Copilot Chat and suggested replies."),
                    t("Вау-вариант, если у преподавателя есть лицензия: включите Facilitator на этом уроке и покажите итоги в конце занятия. Нет лицензии — покажите этот слайд и правило: «кнопка переехала, правило нет».",
                      "Wow option if the instructor has a licence: turn on Facilitator for this lesson and show the recap at the end. No licence: show this slide and the rule “the button moved, the rule did not”."),
                    t("Как показываем на этом курсе: Copilot в Teams требует лицензию Microsoft 365 Copilot, у учебного аккаунта IT Park её нет. Поэтому Teams — по скриншотам на слайде. Вживую то же самое: откройте Copilot Chat (IT Park), вставьте meeting_notes.md как «расшифровку» и спросите «Что решили? Какие вопросы открыты? Кто что делает?» — получится тот же Recap.", "How we show it in this course: Copilot in Teams needs a Microsoft 365 Copilot licence and the IT Park school account has none. So Teams is shown with the screenshots. Live, do the same thing: open Copilot Chat (IT Park), paste meeting_notes.md as a “transcript” and ask “What was decided? What is open? Who does what?”: you get the same recap.")))


# ---------------------------------------------------------------- 10 Word
def s_word():
    return dict(min=5, html=f'''
  {head(t("Для работы • Word", "For work • Word"), t("Word: черновик по файлу и правка прямо в документе", "Word: a draft from a file and edits right in the document"), k="cyan")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1.1fr;gap:32px;flex:none;align-items:start;">
      {shot("yt_word_edit.jpg", t("Copilot в Word: промпт ссылается на файл, справа — <b>«Что я изменил в документе»</b>", "Copilot in Word: the prompt points to a file; on the right, <b>“What I updated in the document”</b>"), "yt_word", pos="50% 0%", h=430)}
      <div class="stack" style="gap:16px;">
        <ul class="pts">
          <li>{t("<b>Черновик:</b> «напиши бриф по /meeting_notes» — Copilot берёт ваш файл как источник.", "<b>Draft:</b> “write a brief from /meeting_notes”: Copilot uses your file as the source.")}</li>
          <li>{t("<b>Правка:</b> выделить абзац → «короче», «проще», «таблицей».", "<b>Edit:</b> select a paragraph → “shorter”, “simpler”, “as a table”.")}</li>
          <li>{t("<b>Проверка:</b> Copilot подсвечивает изменённые слова и даёт ссылки на источник.", "<b>Check:</b> Copilot highlights the changed words and cites the source.")}</li>
        </ul>
        {av("lic")}
        {thread(t("Бриф Анны со слайда 8 в Word делается тем же промптом, только с файлом вместо вставки.", "Anna's brief from slide 8 is the same prompt in Word, with a file instead of pasted text."))}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин, живой показ. «Тот же бриф, что мы сделали в чате, только прямо в документе.»", "⏱ 5 min, live. “The same brief we made in chat, only right inside the document.”"),
                    t("Кадр из официального видео Microsoft (июль 2026). Пользователь пишет промпт, который ссылается на файл. Copilot выполняет работу за несколько шагов и справа пишет отчёт: «Что я изменил в документе». Это уровень 2 со слайда 5: Copilot правит файл, а вы видите список изменений.",
                      "A frame from an official Microsoft video (July 2026). The user writes a prompt that points to a file. Copilot works in a few steps and reports on the right: “What I updated in the document”. That is level 2 from slide 5: Copilot edits the file and you see the list of changes."),
                    t("Три приёма: черновик по файлу; правка выделенного текста; проверка — Copilot подсвечивает слова, которые изменил, и ставит ссылки. Нужна рабочая лицензия; без неё тот же результат даёт Copilot Chat со вставленным текстом, как в демо A.",
                      "Three moves: a draft from a file; editing selected text; checking: Copilot highlights the words it changed and adds citations. Needs a work licence; without one, Copilot Chat with pasted text gives the same result, as in demo A."),
                    t("Как показываем: Copilot внутри Word требует лицензию (в Word без неё на ленте только «Купить Microsoft 365» — проверено 13.10.2026). Вживую в Copilot Chat IT Park: загрузите meeting_notes (кнопка + → файл) и попросите «Сделай бриф на одну страницу и создай файл Word». Затем «сократи раздел Решения до трёх пунктов» — это и есть правка документа.", "How we show it: Copilot inside Word needs a licence (without one the Word ribbon only shows “Buy Microsoft 365”, checked 13 Oct 2026). Live in IT Park Copilot Chat: upload meeting_notes (+ → file) and ask “Write a one-page brief and create a Word file”. Then “shorten the Decisions section to three bullets”: that is document editing.")))


# ---------------------------------------------------------------- 11 Excel + our real mistake
def s_excel():
    return dict(min=5, html=f'''
  {head(t("Для работы • Excel", "For work • Excel"), t("Excel: спросить таблицу словами — и проверить цифры", "Excel: ask the table in words, then check the numbers"), k="cyan")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1.15fr;gap:28px;flex:none;align-items:start;">
      <div class="stack" style="gap:12px;">
        {shot("ms_excel_modes.jpg", t("Три режима: <b>правка · план · только чат</b>", "Three modes: <b>edit · plan · chat only</b>"), "ms_support", pos="0% 0%", h=250, cls="fit")}
        <ul class="pts sm">
          <li>{t("Формулы, сводные, графики, оформление — словами.", "Formulas, pivots, charts, formatting: in words.")}</li>
          <li>{t("Функцию <code>=COPILOT()</code> из старых роликов убрали 14.09.2026.", "The <code>=COPILOT()</code> function from old videos was removed on 14 Sep 2026.")}</li>
        </ul>
        {av("lic")}
      </div>
      <div class="stack" style="gap:12px;">
        {shot("own_orders_crop.jpg", t("Наш бесплатный Copilot Chat, 12 заказов: <b>вне зоны «3 бесплатно» — ошибка</b>", "Our free Copilot Chat, 12 orders: <b>“3 free outside the zone” is wrong</b>"), "own", pos="0% 0%", h=300, cls="fit")}
        <div class="plaque">{t("Правило Prime работает <b>только в городе</b>. Вне зоны бесплатен один заказ — №1011 ($130, правило «от $100 для всех»). Copilot не знал правила, потому что мы его не дали, и пометил допущение звёздочкой.",
                               "The Prime rule applies <b>only in the city</b>. Outside the zone one order is free: #1011 ($130, the “from $100 for all” rule). Copilot did not know the rule because we did not give it, and marked its assumption with an asterisk.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. «Excel — самое сильное место Copilot и самое опасное: цифры выглядят убедительно.»", "⏱ 5 min. “Excel is where Copilot is strongest and most dangerous: numbers look convincing.”"),
                    t("Слева официальный скриншот: Copilot в Excel теперь работает в трёх режимах. Правка — меняет книгу сразу. План — сначала показывает шаги, вы подтверждаете. Только чат — ничего не меняет. Если в старом ролике видите функцию =COPILOT() в ячейке — её убрали в сентябре 2026.",
                      "On the left is the official screenshot: Copilot in Excel now has three modes. Edit changes the workbook directly. Plan shows the steps first and you approve. Chat only changes nothing. If an old video shows =COPILOT() in a cell, it was removed in September 2026."),
                    t("Справа наш настоящий запуск в бесплатном Copilot Chat: 12 придуманных заказов, вопрос «в какой зоне больше всего Prime-заказов от $75 и сколько из них теперь бесплатно?». Copilot посчитал 4 в городе (верно) и 3 бесплатных вне зоны (неверно). Правило Prime действует только в городе; вне зоны бесплатен только заказ 1011 за $130 — по общему правилу «от $100». Мы повторили запрос дважды — ошибка повторилась.",
                      "On the right is our real run in free Copilot Chat: 12 made-up orders, the question “which zone has the most Prime orders from $75 and how many are free now?”. Copilot counted 4 in the city (right) and 3 free outside the zone (wrong). The Prime rule applies only in the city; outside the zone only order 1011 for $130 is free, under the general “from $100” rule. We ran it twice; the mistake repeated."),
                    t("Вывод для группы: Copilot не знал правила, потому что мы его не написали, и честно отметил допущение звёздочкой — но вывод всё равно неверный. Дайте правило в промпте и проверьте одну-две строки руками. В L08 разберём анализ данных подробно.",
                      "Takeaway: Copilot did not know the rule because we did not write it, and honestly marked its assumption with an asterisk, but the conclusion is still wrong. Put the rule into the prompt and check a row or two by hand. L08 covers data analysis in depth."),
                    t("Как показываем: Copilot внутри Excel — по скриншоту слева. Вживую в Copilot Chat IT Park: загрузите orders.csv или вставьте его текстом и задайте вопрос со слайда; затем добавьте правило «Prime бесплатно только в CITY» и сравните ответы. Бесплатно и у каждого студента.", "How we show it: Copilot inside Excel via the screenshot on the left. Live in IT Park Copilot Chat: upload orders.csv or paste it as text and ask the slide question; then add the rule “Prime is free only in CITY” and compare the answers. Free, and every student can do it.")))


# ---------------------------------------------------------------- 12 PowerPoint + Outlook
def s_ppt_outlook():
    return dict(min=4, html=f'''
  {head(t("Для работы • PowerPoint и Outlook", "For work • PowerPoint and Outlook"), t("Та же кнопка — другой документ", "The same button, a different document"), k="cyan")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:28px;flex:none;align-items:start;">
      <div class="stack" style="gap:10px;">
        {shot("ms_ppt_visualize.jpg", t("PowerPoint: <b>«Visualize this slide»</b> — Copilot переделывает слайд", "PowerPoint: <b>“Visualize this slide”</b>: Copilot redesigns the slide"), "ms_support", pos="50% 30%", h=340)}
        <ul class="pts sm"><li>{t("Презентация <b>из документа Word</b>: Copilot сначала уточняет аудиторию и стиль.", "A deck <b>from a Word document</b>: Copilot first asks about audience and style.")}</li></ul>
      </div>
      <div class="stack" style="gap:10px;">
        {shot("ms_outlook_summary.jpg", t("Outlook: <b>сводка ветки</b> со ссылками [1] [2]", "Outlook: <b>thread summary</b> with citations [1] [2]"), "ms_support", pos="0% 0%", h=240, cls="fit")}
        <ul class="pts sm">
          <li>{t("Черновик ответа и «тон»: вежливее, короче.", "Draft a reply and set the tone: politer, shorter.")}</li>
          <li>{t("Разбор входящих словами — с подтверждением.", "Sort the inbox in words, with confirmation.")}</li>
        </ul>
        {av("lic")}
      </div>
    </div>
    <div style="margin-top:12px;">{thread(t("Оля попросила в Outlook сводку жалоб клиентов, а Анна сделала из брифа 5 слайдов для руководства.", "Ola asked Outlook for a summary of customer complaints; Anna turned the brief into 5 slides for management."))}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «Та же модель, то же правило про контекст — только открыт другой документ.»", "⏱ 4 min. “Same model, same context rule, only a different document is open.”"),
                    t("PowerPoint. Copilot делает презентацию из Word-файла и сначала задаёт уточняющие вопросы: для кого, какой стиль. На скриншоте навык «Visualize this slide»: Copilot переделывает текстовый слайд в картинку со схемой. Проверяйте цифры и названия на каждом слайде — Copilot любит дописывать красивые, но придуманные детали.",
                      "PowerPoint. Copilot builds a deck from a Word file and first asks clarifying questions: for whom, which style. In the screenshot is the “Visualize this slide” skill: Copilot turns a text slide into a picture with a diagram. Check numbers and names on every slide: Copilot likes to add nice but invented details."),
                    t("Outlook. Сводка длинной ветки писем со ссылками на конкретные письма — цифры в квадратных скобках. Черновик ответа и выбор тона. Разбор входящих: «перемести все рассылки в папку» — Copilot попросит подтверждения, если писем больше пяти.",
                      "Outlook. A summary of a long thread with citations to specific emails, the numbers in square brackets. A reply draft and tone. Inbox sorting: “move all newsletters into a folder”; Copilot asks for confirmation if more than five emails are affected."),
                    t("Без лицензии: вставьте текст письма в Copilot Chat и попросите сводку — результат похожий.", "Without a licence: paste the email text into Copilot Chat and ask for a summary: a similar result.")))


# ---------------------------------------------------------------- 13 break
def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут: кофе и отдых от экрана", "5 minutes: coffee and a rest from the screen")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: агенты, которые делают работу сами, свой агент, GitHub Copilot, Copilot для компаний, игра и домашнее задание.", "Next: agents that do the work, your own agent, GitHub Copilot, Copilot for companies, a game and homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт». Только отдых, без заданий в чате.", "⏱ 5 min. Press “Start”. Rest only, no chat tasks.")))


# ---------------------------------------------------------------- 14 agents
def s_agents():
    return dict(min=4, html=f'''
  {head(t("Уровень 3 • агенты", "Level 3 • agents"), t("Агенты: Copilot делает работу, а не только отвечает", "Agents: Copilot does the work, not just answers"), k="amber")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr 0.8fr;gap:20px;flex:none;align-items:start;">
      <div class="stack" style="gap:8px;">
        {shot("yt_researcher_report.jpg", t("<b>Researcher</b>: отчёт со ссылками; «составил GPT, проверил Claude»", "<b>Researcher</b>: a cited report; “generated by GPT, refined by Claude”"), "yt_researcher", pos="60% 30%", h=300)}
        {av("lic")}
        <div class="small">{t("для дома — в подписке Microsoft 365 Premium", "at home: in the Microsoft 365 Premium subscription")}</div>
      </div>
      <div class="stack" style="gap:8px;">
        {shot("yt_cowork_workspace.jpg", t("<b>Cowork</b>: план шагов, письмо ждёт вашего «да», готовые файлы", "<b>Cowork</b>: step plan, an email waiting for your “yes”, finished files"), "yt_cowork", pos="100% 30%", h=300)}
        {av("lic", "prev")}
      </div>
      <div class="stack" style="gap:8px;">
        {shot("own_work_agent_store.jpg", t("<b>Магазин агентов</b> в нашем Copilot Chat", "The <b>Agent Store</b> in our Copilot Chat"), "own", pos="40% 30%", h=300)}
        {av("free")}
      </div>
    </div>
    <ul class="pts sm" style="margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:10px 30px;">
      <li>{t("<b>Researcher</b> — многошаговое исследование веба и ваших файлов, отчёт со ссылками.", "<b>Researcher</b>: multi-step research over the web and your files, a cited report.")}</li>
      <li>{t("<b>Analyst</b> — анализ загруженных таблиц: тренды, прогнозы (подробно в L08).", "<b>Analyst</b>: analysis of uploaded tables: trends, forecasts (more in L08).")}</li>
      <li>{t("<b>Cowork</b> — опишите результат, он соберёт документы, письма, встречи; <b>спросит разрешения</b>.", "<b>Cowork</b>: describe the result; it builds documents, emails, meetings; <b>asks for approval</b>.")}</li>
      <li>{t("<b>Autopilot</b> — фоновый агент «на дежурстве», пока закрытое превью.", "<b>Autopilot</b>: a background agent “on duty”, still a private preview.")}</li>
    </ul>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «Главный тренд 2026 года: от помощника, который отвечает, к агенту, который делает.»", "⏱ 4 min. “The big trend of 2026: from an assistant that answers to an agent that does.”"),
                    t("Researcher. Кадр из обзора Mike Tholfsen (апрель 2026): отчёт по исследованию рынка, 112 шагов рассуждений, внизу подпись «Generated by GPT — Refined by Claude». Microsoft использует две модели: одна пишет, другая проверяет. Это отвечает на вопрос, зачем Copilot несколько моделей.",
                      "Researcher. A frame from Mike Tholfsen's review (April 2026): a market research report, 112 reasoning steps, labelled “Generated by GPT — Refined by Claude”. Microsoft uses two models: one writes, the other checks. That answers why Copilot has several models."),
                    t("Cowork. Кадр из обзора Kevin Stratvert (июль 2026): справа план шагов, в центре черновик письма, которое ждёт вашего подтверждения, внизу готовые файлы PowerPoint, Excel, Word. Главное правило агентов: он спрашивает разрешения перед важными действиями — отправкой письма, приглашением на встречу. Cowork сделан вместе с Anthropic, оплачивается по использованию.",
                      "Cowork. A frame from Kevin Stratvert's review (July 2026): on the right the step plan, in the centre an email draft waiting for your approval, below finished PowerPoint, Excel and Word files. The key agent rule: it asks before important actions such as sending an email or a meeting invite. Cowork was built with Anthropic and is billed by usage."),
                    t("Справа наш снимок: магазин агентов есть даже в бесплатном Copilot Chat IT Park — Prompt Coach, Writing Coach, Learning. Попробуйте Prompt Coach в ДЗ: он учит писать промпты лучше.",
                      "On the right is our capture: the Agent Store exists even in the free IT Park Copilot Chat: Prompt Coach, Writing Coach, Learning. Try Prompt Coach in the homework: it teaches better prompts.")))


# ---------------------------------------------------------------- 15a Agent Builder: what and examples
def s_ab_what():
    parts = [("cyan", t("Инструкция", "Instructions"), t("кто ты, как отвечаешь, чего не делаешь", "who you are, how you answer, what you never do")),
             ("green", t("Знания", "Knowledge"), t("бесплатно: веб и до 4 сайтов; файлы и SharePoint — если организация включила оплату", "free: the web and up to 4 sites; files and SharePoint if the organisation enabled billing")),
             ("violet", t("Навыки", "Skills"), t("код и файлы Word/Excel/PowerPoint, картинки — включены сразу", "code and Word/Excel/PowerPoint files, images: on by default")),
             ("amber", t("Стартовые вопросы", "Starter prompts"), t("кнопки-подсказки для пользователя", "suggestion buttons for the user"))]
    pc = "".join(f'<div class="stp" style="--k:var(--{k});min-height:0"><div class="h" style="font-size:21px">{h}</div><div class="d">{d}</div></div>' for k, h, d in parts)
    ex = [t("<b>Помощник поддержки</b> — отвечает по правилам доставки (наш пример)", "<b>Support helper</b>: answers from the delivery rules (our example)"),
          t("<b>Репетитор по курсу</b> — объясняет темы урока и задаёт вопросы", "<b>Course tutor</b>: explains lesson topics and quizzes you"),
          t("<b>Проверяющий по рубрике</b> — сверяет ДЗ с 6 проверками", "<b>Rubric checker</b>: compares homework with the 6 checks"),
          t("<b>Переводчик</b> — шаблон Text Translator: RU ↔ EN ↔ UZ", "<b>Translator</b>: the Text Translator template: RU ↔ EN ↔ UZ"),
          t("<b>Автор постов</b> — пишет анонсы по правилам бренда", "<b>Post writer</b>: drafts announcements in the brand style"),
          t("<b>FAQ кафедры</b> — отвечает по файлам с правилами учёбы", "<b>Department FAQ</b>: answers from the study-rules files")]
    exl = "".join(f"<li>{e}</li>" for e in ex)
    return dict(min=3, html=f'''
  {head(t("Свой агент • Agent Builder", "Your own agent • Agent Builder"), t("Агент — это Copilot с вашей инструкцией и вашими знаниями", "An agent is Copilot with your instructions and your knowledge"), k="amber",
        lead=t("Agent Builder есть <b>даже в бесплатном Copilot Chat</b> учебного аккаунта IT Park: Agents → New agent.", "Agent Builder exists <b>even in the free Copilot Chat</b> of the IT Park school account: Agents → New agent."))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:28px;flex:none;align-items:start;">
      <div class="stack" style="gap:16px;">
        <div class="ladder" style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">{pc}</div>
        <div class="prompt-label">{t("Идеи для студентов и команд", "Ideas for students and teams")}</div>
        <ul class="pts sm" style="--k:var(--amber);display:grid;grid-template-columns:1fr 1fr;gap:10px 22px;">{exl}</ul>
      </div>
      <div class="stack" style="gap:10px;">
        {shot("own_ab_01_start_crop.jpg", t("Agent Builder: <b>опишите агента словами</b> или возьмите шаблон", "Agent Builder: <b>describe the agent in words</b> or start from a template"), "own", pos="50% 0%", h=360, cls="fit")}
        {av("free", "prev")}
        <div class="small">{t("В организации функцию может выключить ИТ-отдел. Для компании и сложных процессов — Copilot Studio.", "IT can turn the feature off in an organisation. For companies and complex workflows: Copilot Studio.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. «Агент — это не магия, а Copilot, которому один раз объяснили роль и дали нужные файлы. Дальше он работает по этим правилам каждый раз.»",
                      "⏱ 3 min. “An agent is not magic: it is Copilot that was told its role once and given the right files. Then it follows those rules every time.”"),
                    t("Четыре части агента в Agent Builder. Инструкция: кто ты, как отвечаешь и чего не делаешь. Знания: файлы, сайты, папки SharePoint; поиск в вебе включается переключателем. Навыки: с осени 2026 каждый агент сразу умеет писать код, создавать файлы Word, Excel и PowerPoint и рисовать картинки — мы видели это в окне «What's new». Стартовые вопросы: кнопки, с которых пользователь начинает разговор.",
                      "The four parts of an agent in Agent Builder. Instructions: who you are, how you answer, what you never do. Knowledge: files, websites, SharePoint folders; web search is a toggle. Skills: since autumn 2026 every agent can write code, create Word, Excel and PowerPoint files and generate images by default; we saw this in the “What's new” window. Starter prompts: buttons the user starts with."),
                    t("Важная находка: мы проверили 13.10.2026 — в учебном аккаунте IT Park с бесплатным Copilot Chat кнопка New agent есть и агент создаётся. То есть студенты могут сделать агента сами. Знания из SharePoint и Teams в бесплатном варианте ограничены; в организации ИТ-отдел может функцию отключить.",
                      "An important finding: we checked on 13 Oct 2026, the IT Park school account with free Copilot Chat has the New agent button and the agent gets created. So students can build an agent themselves. Knowledge from SharePoint and Teams is limited on the free tier; IT can switch the feature off in an organisation."),
                    t("Идеи справа можно предложить группе как варианты для ДЗ. Если нужен агент для всей компании с процессами и подключениями к системам — это Copilot Studio, тема L12.",
                      "Offer the ideas as homework options. For an agent for a whole company with workflows and system connections, use Copilot Studio; that is L12.")))


# ---------------------------------------------------------------- 15b Agent Builder: how, our real build
def s_ab_how():
    cells = [("own_ab_03_configure_instructions_crop.jpg", "50% 0%", t("<b>1. Описали словами</b> — Agent Builder сам написал имя, описание и инструкцию", "<b>1. Described it in words</b>: Agent Builder wrote the name, description and instructions")),
             ("own_ab_04_knowledge_prompts_crop.jpg", "50% 100%", t("<b>2. Проверили настройки</b>: знания, веб-поиск, 4 стартовых вопроса", "<b>2. Checked the settings</b>: knowledge, web search, 4 starter prompts")),
             ("own_ab_05_preview_test_crop.jpg", "50% 0%", t("<b>3. Тест в Preview</b>: Prime, $80, вне зоны → $18.00 — верно", "<b>3. Test in Preview</b>: Prime, $80, outside the zone → $18.00, correct")),
             ("own_ab_07_created_crop.jpg", "50% 50%", t("<b>4. Create</b> → агент <b>личный</b>; поделиться — по кнопке Share", "<b>4. Create</b> → the agent is <b>private</b>; share with the Share button"))]
    grid = "".join(shot(img, cap, "own", pos=pos, h=232) for img, pos, cap in cells)
    return dict(min=5, html=f'''
  {head(t("Свой агент • как собрать", "Your own agent • how to build"), t("Собрали агента поддержки за 5 минут — настоящий запуск", "We built a support agent in 5 minutes: a real run"), k="amber")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:16px 24px;flex:none;">{grid}</div>
    <div class="plaque" style="margin-top:12px;font-size:19px;">{t("Наш промпт: «Создай агента «Помощник поддержки курьеров»… Prime — бесплатно от $75 только в городе; от $100 — всем; город $7.50, вне зоны $18.00. <b>Показывай расчёт, не хватает данных — уточни, не выдумывай скидок</b>». На вопрос «сколько стоит доставка за $70?» агент переспросил зону и Prime.",
                                                                  "Our prompt: “Create a ‘Courier support helper’ agent… Prime is free from $75 only in the city; from $100 free for all; city $7.50, outside $18.00. <b>Show the calculation, ask if data is missing, never invent discounts</b>.” Asked “how much is delivery for $70?”, the agent asked back for the zone and Prime.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Можно показать вживую (учебный аккаунт, Agents → New agent) или по этим снимкам — это наш настоящий запуск 13.10.2026.",
                      "⏱ 5 min. Show it live (school account, Agents → New agent) or with these captures: our real run of 13 Oct 2026."),
                    t("Шаг 1. Пишем описание обычными словами — тот же приём, что промпт в L02: роль, правила, формат, чего не делать. Agent Builder сам придумывает имя, описание и раскладывает инструкцию по разделам «Назначение» и «Основные правила». Шаг 2. Вкладка Configure: можно добавить знания (файлы, сайты), включить веб-поиск; стартовые вопросы он тоже придумал сам — четыре кнопки.",
                      "Step 1. Write the description in plain words, the same move as a prompt in L02: role, rules, format, what not to do. Agent Builder invents the name and description and splits the instructions into “Purpose” and “Main rules”. Step 2. The Configure tab: add knowledge (files, sites), toggle web search; it also wrote four starter prompts."),
                    t("Шаг 3. Preview — проверка до публикации. Мы задали каверзный вопрос: Prime, $80, адрес за городом. Агент ответил $18.00 и объяснил: Prime действует только в городе. Второй вопрос без данных — «сколько стоит доставка за $70?» — он не стал угадывать, а переспросил зону и наличие Prime. Это и есть результат хорошей инструкции. Мелочь: в превью ответ продублировался — интерфейс ещё сырой.",
                      "Step 3. Preview: test before publishing. We asked a tricky one: Prime, $80, an address outside the city. The agent answered $18.00 and explained that Prime only applies in the city. The second question had missing data, “how much is delivery for $70?”, and it did not guess but asked for the zone and Prime. That is what good instructions buy you. A detail: in preview the answer was duplicated; the interface is still rough."),
                    t("Шаг 4. Create — агент создан и он личный. Поделиться можно кнопкой Share: ссылкой или с организацией, если ИТ разрешил. Сравните со слайдом 13: там Copilot ошибся, потому что правила не знал; здесь правила в инструкции — и ответ верный.",
                      "Step 4. Create: the agent exists and is private. Share it with the Share button, by link or with the organisation if IT allows. Compare with slide 13: there Copilot got it wrong because it did not know the rule; here the rule is in the instructions, and the answer is right.")))


# ---------------------------------------------------------------- 16 GitHub (one slide)
def s_github():
    lines = [ln for ln in ART["diff_u1"].splitlines() if ln.startswith("+    if") or ln.startswith("+        return 0.0")]
    diff = "".join(f'<div class="a">{esc(ln)}</div>' for ln in lines[:2])
    return dict(min=4, html=f'''
  {head(t("Для разработчиков", "For developers"), t("GitHub Copilot — Copilot для кода (подробно в L16)", "GitHub Copilot: Copilot for code (more in L16)"), k="violet")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:28px;flex:none;align-items:start;">
      {shot("gh_code_review.jpg", t("Copilot-ревью pull request: <b>находит проблему и предлагает правку</b>", "Copilot reviewing a pull request: <b>finds a problem and suggests a fix</b>"), "gh", pos="50% 0%", h=400, cls="fit")}
      <div class="stack" style="gap:14px;">
        <ul class="pts" style="--k:var(--violet)">
          <li>{t("<b>Редактор</b> (VS Code и др.): подсказки, чат, агент.", "<b>Editor</b> (VS Code etc.): completions, chat, agent.")}</li>
          <li>{t("<b>github.com</b>: ревью pull request, облачный агент по задаче.", "<b>github.com</b>: pull request review, a cloud agent per issue.")}</li>
          <li>{t("<b>Терминал и приложение</b>: Copilot CLI, GitHub Copilot app.", "<b>Terminal and app</b>: Copilot CLI, the GitHub Copilot app.")}</li>
          <li>{t("<b>В Teams</b>: GitHub Copilot как агент (октябрь 2026).", "<b>In Teams</b>: GitHub Copilot as an agent (October 2026).")}</li>
        </ul>
        <div><div class="prompt-label">{t("Наш настоящий результат: правило Prime — 2 строки, 7 тестов зелёные", "Our real result: the Prime rule in 2 lines, 7 tests green")}</div>
          <div class="dif" style="font-size:15px;line-height:23px;">{diff}</div></div>
        {av("free")}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «GitHub Copilot — самый старый член семьи, с 2021 года. Сегодня один слайд, весь урок L16 — про ИИ для кода.»", "⏱ 4 min. “GitHub Copilot is the oldest family member, since 2021. One slide today; all of L16 is about AI for code.”"),
                    t("Где он живёт: в редакторе — подсказывает строки, отвечает в чате, в режиме агента сам правит файлы и запускает тесты. На github.com — делает ревью pull request (на картинке находит проблему и предлагает исправление) и как облачный агент берёт задачу и сам открывает pull request. В терминале и отдельном приложении. И с октября 2026 — как агент в Teams.",
                      "Where it lives: in the editor it suggests lines, answers in chat, and in agent mode edits files and runs tests itself. On github.com it reviews pull requests (in the picture it finds a problem and suggests a fix) and, as a cloud agent, takes an issue and opens a pull request itself. In the terminal and a separate app. And since October 2026 as an agent in Teams."),
                    t("Наш пример: Павел попросил реализовать правило Prime. Настоящий diff — две строки логики, плюс три теста, все семь тестов зелёные (demo_courier_copilot/sample_repo). Правило то же, что везде: смотрим на изменения и тесты, а не на слово «готово». GitHub Copilot Free достаточно; студентам GitHub даёт Copilot Student.",
                      "Our example: Pavel asked for the Prime rule. The real diff is two lines of logic plus three tests, all seven tests green (demo_courier_copilot/sample_repo). Same rule as everywhere: look at the changes and tests, not at the word “done”. GitHub Copilot Free is enough; GitHub gives students Copilot Student.")))


# ---------------------------------------------------------------- 17 for the company
def s_company():
    tiles = [("yt_foundry_models.jpg", "Microsoft Foundry", t("модели и агенты для разработчиков: GPT, Claude, DeepSeek, Grok…", "models and agents for developers: GPT, Claude, DeepSeek, Grok…"), "yt_foundry", "50% 30%", "dark"),
             ("yt_security_copilot.jpg", "Security Copilot", t("агент сам разбирает подозрительные письма: 12 из 12", "an agent triages suspicious emails itself: 12 of 12"), "yt_security", "30% 20%", ""),
             ("yt_studio_workflow.jpg", t("Процессы: Copilot Studio, Power Platform", "Workflows: Copilot Studio, Power Platform"), t("схема: пришло письмо → классифицировать → агент оценивает", "a flow: email arrives → classify → an agent evaluates"), "yt_studio", "30% 50%", "")]
    cards = "".join(f'<div class="stack" style="gap:8px;"><div class="vlabel" style="--k:var(--amber)">{h}</div>{shot(img, d, src, pos=pos, h=300, cls=c)}</div>'
                    for img, h, d, src, pos, c in tiles)
    return dict(min=2, html=f'''
  {head(t("Для компании", "For the company"), t("Copilot для компании: три примера", "Copilot for the company: three examples"), k="amber")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr 1fr;gap:20px;flex:none;">{cards}</div>
    <div class="note" style="--k:var(--amber);margin-top:18px;">{t("Ещё в семье: <b>Dynamics 365</b> (продажи и сервис), <b>Power BI / Fabric</b> (отчёты), <b>Dragon Copilot</b> (врачи), <b>Agent 365</b> (учёт и защита всех агентов компании).",
                                                              "Also in the family: <b>Dynamics 365</b> (sales and service), <b>Power BI / Fabric</b> (reports), <b>Dragon Copilot</b> (doctors), <b>Agent 365</b> (inventory and protection of all company agents).")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 2 мин. «Эти продукты вы не откроете сами — их включает ИТ-отдел. Но знать их полезно: на собеседовании и на работе вы их встретите.»",
                      "⏱ 2 min. “You will not open these yourself; IT turns them on. But it helps to know them: you will meet them in interviews and at work.”"),
                    t("Microsoft Foundry (раньше Azure AI Foundry) — площадка для разработчиков: тысячи моделей разных компаний, сборка своих агентов и приложений. Именно здесь живёт то, что вы делали в L03, только в масштабе компании.",
                      "Microsoft Foundry (formerly Azure AI Foundry) is the developer platform: thousands of models from many vendors, building your own agents and apps. This is where what you did in L03 lives at company scale."),
                    t("Security Copilot — помощник отдела безопасности. На кадре агент разбора фишинга сам проверил 12 подозрительных писем из 12. С сентября 2026 включён в пакеты Microsoft 365 E5 и E7.",
                      "Security Copilot is the security team's assistant. In the frame the phishing triage agent handled 12 of 12 suspicious emails itself. Since September 2026 it is included in Microsoft 365 E5 and E7."),
                    t("Процессы: в Copilot Studio и Power Platform собирают цепочки — пришло письмо, его классифицировали, агент оценил, человек утвердил. Остальные продукты назовите одной фразой: Dynamics — продажи и сервис, Power BI и Fabric — отчёты, Dragon Copilot — заметки врача, Agent 365 — учёт и защита всех агентов в компании.",
                      "Workflows: in Copilot Studio and Power Platform people build chains: an email arrives, it is classified, an agent evaluates it, a person approves. Name the others in one line: Dynamics for sales and service, Power BI and Fabric for reports, Dragon Copilot for doctors' notes, Agent 365 for inventory and protection of all agents in a company.")))


# ---------------------------------------------------------------- 18 game + limits
def s_game():
    qs = [t("«Сделай сводку встречи, на которой меня не было»", "“Summarise the meeting I missed”"),
          t("«Что за ошибка в этом окне?»", "“What is this error in the window?”"),
          t("«Почему тест в pull request упал?»", "“Why did the test in the pull request fail?”"),
          t("«Нарисуй обложку для поста»", "“Draw a cover for my post”")]
    cards = "".join(f'<div class="qcard"><div class="n">{t("ВОПРОС", "QUESTION")} {i}</div><div class="q">{q}</div></div>' for i, q in enumerate(qs, 1))
    zk = "".join(f'<span style="--k:var(--{k})">{a} · {n}</span>' for a, k, n in [
        ("A", "green", t("для себя", "for you")), ("B", "cyan", t("для работы", "for work")), ("C", "violet", t("для разработчиков", "for developers")), ("D", "amber", t("для компании", "for the company"))])
    rules = [("green", t("Copilot видит <b>только то, что можете открыть вы</b>.", "Copilot sees <b>only what you can open</b>.")),
             ("cyan", t("Рабочие данные <b>под защитой договора</b>; в личном — <b>выключите обучение</b>.", "Work data is <b>protected by contract</b>; in a personal account <b>turn training off</b>.")),
             ("red", t("<b>Пароли, ключи, данные клиентов</b> в чат не вставляем.", "<b>No passwords, keys or customer data</b> in chat.")),
             ("amber", t("Ответ — <b>черновик</b>: цифры и имена проверяем.", "An answer is <b>a draft</b>: check numbers and names."))]
    rl = "".join(f'<div class="note" style="--k:var(--{k});font-size:19px;">{x}</div>' for k, x in rules)
    return dict(min=5, html=f'''
  {head(t("Игра • опрос в Teams", "Game • Teams poll"), t("Куда пойдёт этот вопрос?", "Where does this question go?"),
        t("Для каждого вопроса выберите зону A–D со слайда 2. Ответы — в заметках спикера.", "For each question pick zone A–D from slide 2. Answers are in the speaker notes."))}
  <div class="body" style="margin-top:16px;gap:18px;">
    <div class="zkey">{zk}</div>
    <div class="qcards">{cards}</div>
    <div class="prompt-label" style="margin-top:6px;">{t("Четыре правила безопасности", "Four safety rules")}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:12px 30px;flex:none;">{rl}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Запустите опрос в Teams на каждый вопрос или попросите писать в чат «1-B, 2-A…». 3 минуты на игру, 3 — на правила.",
                      "⏱ 5 min. Run a Teams poll per question or ask for answers in chat: “1-B, 2-A…”. 3 minutes for the game, 3 for the rules."),
                    t("Ответы. 1 — B, для работы: Recap в Teams (нужна лицензия) или вставить расшифровку в Copilot Chat. 2 — A, для себя: Copilot Vision или скриншот в чат. 3 — C, для разработчиков: GitHub Copilot в pull request или в редакторе. 4 — A, для себя: картинка в приложении Copilot. Спорные ответы — хорошо: обсудите, где лежит информация.",
                      "Answers. 1: B, for work: Recap in Teams (licence) or paste the transcript into Copilot Chat. 2: A, for you: Copilot Vision or a screenshot into chat. 3: C, for developers: GitHub Copilot in the pull request or editor. 4: A, for you: an image in the Copilot app. Arguable answers are good: discuss where the information lives."),
                    t("Правила. Copilot видит только то, к чему у вас самих есть доступ: если вам не открыли папку, Copilot её тоже не увидит. Рабочие и учебные аккаунты защищены корпоративным договором — зелёный щит в приложении. Пароли, ключи и данные клиентов в чат не вставляем ни в каком аккаунте. И любой ответ — черновик: цифры и имена проверяем, как на слайде 13.",
                      "Rules. Copilot sees only what you can access yourself: if a folder is not shared with you, Copilot cannot see it either. Work and school accounts are covered by an enterprise agreement: the green shield in the app. No passwords, keys or customer data in chat in any account. And every answer is a draft: check numbers and names, as on slide 13.")))


# ---------------------------------------------------------------- 19 homework
def s_hw():
    steps = [t("<b>Бриф</b> из <code>meeting_notes.md</code> + список «что добавил Copilot» + одна найденная выдумка или ошибка.", "<b>Brief</b> from <code>meeting_notes.md</code> + “what Copilot added” + one invention or mistake you found."),
             t("<b>Таблица:</b> вставьте <code>orders.csv</code> текстом, задайте вопрос со слайда 13 <b>с правилом</b> — и проверьте руками.", "<b>Table:</b> paste <code>orders.csv</code> as text, ask the slide 13 question <b>with the rule</b>, and check by hand."),
             t("<b>Творческое:</b> текст для 3 слайдов <b>или</b> картинка-анонс фичи.", "<b>Creative:</b> text for 3 slides <b>or</b> a launch picture."),
             t("<b>Своя карта:</b> 5 задач из учёбы или работы → какой Copilot, что он видит, бесплатно ли.", "<b>Your map:</b> 5 tasks from study or work → which Copilot, what it sees, whether it is free.")]
    checks = [t("источник указан", "source named"), t("выдумки отмечены", "inventions marked"), t("цифры проверены руками", "numbers checked by hand"),
              t("скриншоты настоящие", "real screenshots"), t("в карте — продукт и что он видит", "the map names the product and what it sees"), t("нет имён, почт, секретов", "no names, e-mails, secrets")]
    ck = "".join(f'<li>{c}</li>' for c in checks)
    return dict(min=5, html=f'''
  {head(t("Практика", "Practice"), t("ДЗ: неделя курьерской команды с Copilot", "Homework: the courier team's week with Copilot"),
        t("Нужен только бесплатный Copilot: <b>личный</b> или <b>учебный IT Park</b>. Сдать один документ со скриншотами.", "Only free Copilot is needed: <b>personal</b> or <b>IT Park school</b>. Hand in one document with screenshots."))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.4fr 1fr;gap:36px;flex:none;align-items:start;">
      <div class="steps3 big" style="--k:var(--cyan);gap:26px;">{"".join(f"<div>{s}</div>" for s in steps)}</div>
      <div class="stack" style="gap:12px;">
        {shot("own_work_home.jpg", t("Здесь: учебный аккаунт IT Park, <b>Copilot Chat</b>", "Here: the IT Park school account, <b>Copilot Chat</b>"), "own", pos="0% 0%", h=210)}
        <div class="prompt-label">{t("Оценка: 6 проверок", "Grading: 6 checks")}</div>
        <ul class="pts big" style="--k:var(--green);gap:16px;">{ck}</ul>
        <div class="small">{t("Файлы: <code>demo_courier_copilot/</code>. Данные только придуманные.", "Files: <code>demo_courier_copilot/</code>. Synthetic data only.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. «Всё задание делается в бесплатном Copilot — личном или учебном. Ничего покупать не нужно.»", "⏱ 5 min. “The whole assignment works in free Copilot, personal or school. Nothing to buy.”"),
                    t("Шаг 1 повторяет демо A: бриф и список того, что Copilot добавил сам, плюс одна найденная ошибка или выдумка. Шаг 2 повторяет слайд 13, но с правилом в промпте: «Prime бесплатно от $75 только в городе; от $100 бесплатно всем». Сравните ответ со своим ручным счётом. Шаг 3 — текст для трёх слайдов или картинка-анонс. Шаг 4 — самое важное: ваша карта из пяти задач и выбор Copilot для каждой.",
                      "Step 1 repeats demo A: the brief and what Copilot added, plus one mistake or invention you found. Step 2 repeats slide 13 with the rule in the prompt: “Prime is free from $75 only in the city; free from $100 for everyone”. Compare with your hand count. Step 3: text for three slides or a launch picture. Step 4 matters most: your map of five tasks and the Copilot for each."),
                    t("Рубрика — шесть проверок справа. Важная: на скриншотах не должно быть имён, почт и секретов. Правильный ответ для шага 2 с правилом: в городе 4 Prime-заказа от $75 (1001, 1004, 1006, 1009), вне зоны бесплатен только 1011.",
                      "The rubric is six checks on the right. An important one: screenshots must show no names, e-mails or secrets. Correct answer for step 2 with the rule: 4 Prime orders from $75 in the city (1001, 1004, 1006, 1009); outside the zone only 1011 is free.")))


# ---------------------------------------------------------------- 20 summary
def s_summary():
    rules = [t("Сначала спросите: <b>чья информация и где она лежит?</b>", "First ask: <b>whose information is it and where does it live?</b>"),
             t("Внутри — те же модели; разница в том, <b>что Copilot видит и что ему разрешено</b>.", "Same models inside; the difference is <b>what Copilot sees and is allowed to do</b>."),
             t("Бесплатно: личный Copilot, Copilot Chat, GitHub Copilot Free.", "Free: personal Copilot, Copilot Chat, GitHub Copilot Free."),
             t("Агент делает работу, но <b>спрашивает вашего «да»</b>.", "An agent does the work but <b>asks for your “yes”</b>."),
             t("Любой ответ — черновик: <b>проверяйте цифры</b>.", "Every answer is a draft: <b>check the numbers</b>.")]
    rl = "".join(f'<li>{r}</li>' for r in rules)
    zt = [("green", t("для себя", "for you"), "own_prime_poster.jpg", "50% 50%"), ("cyan", t("для работы", "for work"), "ms_teams_facilitator.jpg", "50% 30%"),
          ("violet", t("для кода", "for code"), "gh_code_review.jpg", "50% 30%"), ("amber", t("для компании", "for the company"), "yt_security_copilot.jpg", "30% 20%")]
    zrow = "".join(f'<div class="shot"><div class="fr" style="height:200px;flex:none;--pos:{pos};border:2px solid var(--{k})"><span class="tag" style="--k:var(--{k})">{lab}</span><img src="{IMG}{img}" alt=""></div></div>'
                   for k, lab, img, pos in zt)
    return dict(min=3, html=f'''
  {head(t("Итоги", "Summary"), t("Семья Copilot в одну строку: для себя · для работы · для кода · для компании", "The Copilot family in one line: for you · for work · for code · for the company"))}
  <div class="body" style="gap:26px;">
    <div class="row" style="grid-template-columns:repeat(4,1fr);gap:16px;flex:none;">{zrow}</div>
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:36px;flex:none;align-items:start;">
      <ol class="pts big" style="list-style:none;">{rl}</ol>
      <div class="stack" style="gap:16px;">
        <div class="poll" style="font-size:21px;"><b>{t("В чат:", "In chat:")}</b> {t("какой Copilot вы попробуете на этой неделе и для какой задачи?", "which Copilot will you try this week, and for what?")}</div>
        <div class="note" style="--k:var(--amber)"><b>{t("Дальше: L08 — ИИ для анализа данных.", "Next: L08, AI for data analysis.")}</b> {t("Copilot в Excel и агент Analyst — от вопроса до проверенного вывода.", "Copilot in Excel and the Analyst agent: from a question to a checked conclusion.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Пять правил вслух. Потом вопрос в чат: «какой Copilot попробуете на этой неделе и для чего?» Прочитайте 3–4 ответа.",
                      "⏱ 3 min. Five rules out loud. Then the chat question: “which Copilot will you try this week, and for what?” Read 3–4 answers."),
                    t("Следующий урок L08: анализ данных с ИИ. Вернёмся к таблице заказов со слайда 13 и пройдём путь от вопроса до проверенного вывода в Excel и с агентом Analyst.",
                      "Next lesson L08: data analysis with AI. We return to the orders table from slide 13 and go from a question to a checked conclusion in Excel and with the Analyst agent.")))


SLIDES = [s_cover, s_map, s_terms, s_assist_agent, s_models, s_app, s_money, s_you, s_vision, s_windows, s_teams, s_word, s_excel, s_ppt_outlook,
          s_break, s_agents, s_anatomy, s_ab_what, s_ab_how, s_github, s_company, s_game, s_hw, s_summary]
MINUTES = [2, 5, 2, 2, 3, 4, 3, 3, 3, 5, 6, 5, 5, 4, 5, 4, 2, 3, 5, 4, 2, 5, 5, 3]


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
        assert s["min"] == MINUTES[i - 1], (fn.__name__, s["min"])
        minutes += s["min"]
        cls = ("slide " + s.get("cls", "")).strip()
        foot = "" if s.get("cls", "").startswith("cover") else f'\n  <div class="foot"><span>{FOOT[lang]}</span><span>{i:02d} / {total}</span></div>'
        secs.append(f'<!-- SLIDE {i:02d} · {fn.__name__} · {s["min"]} min -->\n<section class="{cls}" data-n="{i}">{s["html"]}{foot}\n'
                    f'  <template class="notes">{s["notes"]}</template>\n</section>')
    assert minutes == 90, minutes
    title = t("Урок 07: Экосистема Microsoft Copilot | GenAI Basics", "Lesson 07: The Microsoft Copilot ecosystem | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    page = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<!-- generated by deck_v3/build.py; edit the generator, not this file -->
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
    OUT[lang].write_text(page, encoding="utf-8")
    print(f"{lang}: {OUT[lang].name}: {total} slides, {minutes} min")
    return OUT[lang]


CHROME = next((c for c in [shutil.which("msedge"), shutil.which("chromium"), shutil.which("google-chrome"),
                           r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                           r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"] if c and Path(c).exists()), None)


def pdf(html):
    out = html.with_suffix(".pdf")
    prof = tempfile.mkdtemp(prefix="pdf_")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--no-margins",
                    "--virtual-time-budget=10000", f"--user-data-dir={prof}", f"--print-to-pdf={out}", html.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    shutil.rmtree(prof, ignore_errors=True)
    print("pdf:", out.name, f"{out.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    for lg in ("ru", "en"):
        h = build(lg)
        if "--no-pdf" not in sys.argv:
            pdf(h)
