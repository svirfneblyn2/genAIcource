# -*- coding: utf-8 -*-
"""Generate the 90-minute instructor scripts (RU + EN) for deck v3 from the deck generator.

    python make_docs.py

The timing table (from MINUTES), slide titles and the speaker text come straight from build.py,
so the script cannot drift from the deck. Only the short "On screen" lines and the header live here.
"""
import html
import re

import build

L07 = build.L07
OUT = {"ru": L07 / "L07_02_Instructor_Script_90MIN_v3.md", "en": L07 / "L07_02_Instructor_Script_90MIN_v3_EN.md"}

SCREEN = {
    "s_terms": ("Наша схема из четырёх ступеней: модель → чат → ассистент → агент. У каждой ступени мини-интерфейс, пример из Copilot и одна строка о том, что она добавляет.",
                "Our four-stage diagram: model → chat → assistant → agent. Each stage has a mini interface, a Copilot example and one line on what it adds."),
    "s_assist_agent": ("Наша схема «ассистент или агент»: слева «вы ведёте» (просьба → ответ в Word → следующий шаг делаете вы), справа «он ведёт, вы утверждаете» (цель → цикл план → действие → проверка через почту, календарь, файлы → ваше подтверждение).",
                       "Our “assistant or agent” diagram: left “you drive” (request → answer in Word → you take the next step), right “it drives, you approve” (goal → loop plan → act → check over email, calendar, files → your approval)."),
    "s_anatomy": ("Наша схема анатомии агента: харнесс вокруг модели с циклом, пять деталей (инструкция, контекст, инструмент, навык, коннектор) и коннекторы к почте, файлам и базе клиентов.",
                  "Our agent anatomy diagram: the harness around the model with its loop, five parts (instruction, context, tool, skill, connector) and connectors to mail, files and the customer database."),
    "s_windows": ("Слева: что можно бесплатно в Windows (чат, голос, Vision, файлы, создание файлов, коннекторы) и кадр Ask Copilot. Справа: официальные лимиты (20 файлов, 50 МБ, 18 месяцев), что не публикуется, функции Copilot+ ПК, как выключить обучение в личном аккаунте, строка про Edge.",
                  "Left: what is free in Windows (chat, voice, Vision, files, file creation, connectors) and the Ask Copilot frame. Right: official limits (20 files, 50 MB, 18 months), what is not published, Copilot+ PC features, how to turn training off in a personal account, a line on Edge."),
    "s_ab_what": ("Четыре части агента (инструкция, знания, навыки, стартовые вопросы), шесть идей агентов, наш снимок стартового экрана Agent Builder в Copilot Chat IT Park.",
                  "The four parts of an agent (instructions, knowledge, skills, starter prompts), six agent ideas, our capture of the Agent Builder start screen in IT Park Copilot Chat."),
    "s_ab_how": ("Четыре наших снимка по шагам: описание → инструкция; знания и стартовые вопросы; тест в Preview ($18.00); агент создан, личный. Внизу наш промпт.",
                 "Four of our captures step by step: description → instructions; knowledge and starter prompts; Preview test ($18.00); agent created, private. Our prompt below."),
    "s_cover": ("Фон: официальная картинка нового Microsoft Copilot (25.09.2026). Заголовок «Copilot — это не кнопка, а семья», план урока, «факты на 13.10.2026», подсказки по клавишам.",
                "Background: the official picture of the new Microsoft Copilot (25 Sep 2026). Title “Copilot is not a button, it is a family”, the lesson plan, “facts as of 13 Oct 2026”, key hints."),
    "s_map": ("Опрос в Teams «какой Copilot у вас уже есть?» и карта из четырёх зон: для себя, для работы, для разработчиков, для компании. В каждой зоне строка «видит» и продукты с цветной точкой доступности; внизу легенда цветов.",
              "Teams poll “which Copilot do you already have?” and a map of four zones: for you, for work, for developers, for the company. Each zone has a “Sees” line and products with an availability dot; the colour legend below."),
    "s_models": ("Лестница из трёх уровней: отвечает → правит документ → делает работу (агент). Две строки про модели (OpenAI GPT, Anthropic Claude, Microsoft MAI, режим Auto). Справа наш снимок меню модели в рабочем Copilot IT Park.",
                 "A three-step ladder: answers → edits the document → does the work (agent). Two lines on models (OpenAI GPT, Anthropic Claude, Microsoft MAI, Auto). On the right our capture of the model menu in the IT Park work Copilot."),
    "s_app": ("Наш снимок переключателя аккаунтов (личный и рабочий IT Park в одном приложении), две карточки «Личный / Рабочий», официальная картинка вкладок Home · Code · Autopilot и словарь имён.",
              "Our capture of the account switcher (personal and IT Park work in one app), two cards “Personal / Work”, the official picture of the Home · Code · Autopilot tabs and the name dictionary."),
    "s_money": ("Четыре столбца цен на 13.10.2026 (США): бесплатно, для дома, для работы, агенты. Плашка «ОКТЯБРЬ 2026» и строка для студентов IT Park. Единственный слайд с ценами.",
                "Four price columns as of 13 Oct 2026 (US): free, home, work, agents. An “OCTOBER 2026” badge and a line for IT Park students. The only slide with prices."),
    "s_you": ("Демо A. Слева наш снимок: бриф по meeting_notes.md в Copilot Chat учебного аккаунта IT Park (без лицензии). Справа наша картинка-анонс из личного Copilot и три шага демо с промптом.",
              "Demo A. Left: our capture of the brief from meeting_notes.md in Copilot Chat on the IT Park school account (no licence). Right: our launch picture from personal Copilot and the three demo steps with the prompt."),
    "s_vision": ("Демо B. Кадр из видео Kevin Stratvert: окно Copilot в Windows с выбором Share screen / Share app. Справа три шага демо с release_checklist.txt и три правила Vision.",
                 "Demo B. A frame from Kevin Stratvert's video: the Copilot window in Windows with the Share screen / Share app choice. Right: the three demo steps with release_checklist.txt and three Vision rules."),
    "s_pc": ("Две колонки. Windows: кадр Microsoft Mechanics с Ask Copilot на панели задач, клавиша Copilot / Win+C, функции Copilot+ ПК. Edge: официальный скриншот поиска по истории, вкладки, Journeys, закрытый Copilot Mode.",
             "Two columns. Windows: a Microsoft Mechanics frame with Ask Copilot on the taskbar, the Copilot key / Win+C, Copilot+ PC features. Edge: the official history-search screenshot, tabs, Journeys, the retired Copilot Mode."),
    "s_teams": ("Официальные скриншоты Microsoft: Facilitator во встрече и вкладка Recap после неё. Три пункта «во время / после / нужна расшифровка» и строка команды: 3 решения, 2 открытых вопроса, 3 задачи.",
                "Official Microsoft screenshots: Facilitator in a meeting and the Recap tab after it. Three points “during / after / needs the transcript” and the team line: 3 decisions, 2 open questions, 3 tasks."),
    "s_word": ("Кадр из официального видео Microsoft: Copilot в Word с промптом по файлу и отчётом «What I updated in the document». Справа три приёма: черновик, правка, проверка.",
               "A frame from an official Microsoft video: Copilot in Word with a prompt that points to a file and the “What I updated in the document” report. Right: three moves: draft, edit, check."),
    "s_excel": ("Слева официальный скриншот трёх режимов Copilot в Excel. Справа наш снимок: бесплатный Copilot Chat по 12 заказам ошибся вне зоны; плашка с правильным ответом (только №1011).",
                "Left: the official screenshot of the three Copilot modes in Excel. Right: our capture: free Copilot Chat on 12 orders got the outside zone wrong; a plaque with the right answer (only #1011)."),
    "s_ppt_outlook": ("Официальные скриншоты: PowerPoint «Visualize this slide» и сводка ветки в Outlook со ссылками [1] [2]. Строка команды: сводка жалоб у Оли, 5 слайдов у Анны.",
                      "Official screenshots: PowerPoint “Visualize this slide” and an Outlook thread summary with citations [1] [2]. The team line: Ola's complaint summary, Anna's 5 slides."),
    "s_break": ("Таймер 5 минут, кнопки «Старт» и «Сброс», строка «дальше».", "5-minute timer, Start and Reset buttons, a “next” line."),
    "s_agents": ("Три картинки: Researcher (кадр Mike Tholfsen, «Generated by GPT — Refined by Claude»), Cowork (кадр Kevin Stratvert: план, письмо ждёт «да», файлы), наш снимок магазина агентов. Внизу четыре агента одной строкой.",
                 "Three pictures: Researcher (Mike Tholfsen frame, “Generated by GPT — Refined by Claude”), Cowork (Kevin Stratvert frame: plan, an email waiting for “yes”, files), our capture of the Agent Store. Four agents in one line each below."),
    "s_build": ("Кадр Microsoft Mechanics: новый экран Copilot Studio (агент / процесс / приложение). Справа «агент = три части» на примере помощника поддержки и разница Agent Builder и Copilot Studio.",
                "A Microsoft Mechanics frame: the new Copilot Studio screen (agent / workflow / app). Right: “agent = three parts” on the support-helper example and the difference between Agent Builder and Copilot Studio."),
    "s_github": ("Официальная картинка GitHub: Copilot-ревью pull request. Справа четыре места GitHub Copilot и наш настоящий diff: 2 строки правила Prime, 7 тестов зелёные.",
                 "The official GitHub picture: Copilot reviewing a pull request. Right: four places of GitHub Copilot and our real diff: the Prime rule in 2 lines, 7 tests green."),
    "s_company": ("Три плитки с кадрами видео: Microsoft Foundry (каталог моделей), Security Copilot (12 из 12), процессы в Copilot Studio. Внизу строка про Dynamics 365, Power BI / Fabric, Dragon Copilot, Agent 365.",
                  "Three tiles with video frames: Microsoft Foundry (model catalogue), Security Copilot (12 of 12), workflows in Copilot Studio. Below a line about Dynamics 365, Power BI / Fabric, Dragon Copilot, Agent 365."),
    "s_game": ("Ключ зон A–D, четыре карточки-вопроса для опроса в Teams и четыре правила безопасности.",
               "The A–D zone key, four question cards for the Teams poll and four safety rules."),
    "s_hw": ("Четыре шага ДЗ, наш снимок учебного аккаунта IT Park в Copilot Chat и рубрика из 6 проверок. Только бесплатный Copilot, только придуманные данные.",
             "The four homework steps, our capture of the IT Park school account in Copilot Chat and the 6-check rubric. Free Copilot only, synthetic data only."),
    "s_summary": ("Четыре картинки-зоны в ряд (для себя, для работы, для кода, для компании), пять правил, вопрос в чат и анонс L08.",
                  "Four zone pictures in a row (for you, for work, for code, for the company), five rules, the chat question and the L08 teaser."),
}

HEAD = {
    "ru": """# Сценарий преподавателя • Урок 07 (v3): Экосистема Microsoft Copilot — обзор (90 минут)

**Курс:** GenAI Basics • Урок 07 из 16
**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Аудитория:** студенты IT Park University, новички в GenAI из разных ролей. Простой язык, без формул и без кода.
**Формат:** 24 слайда (`presentation_L07_Copilot_Ecosystem_v3.html` / PDF) • занятие в **Microsoft Teams** • таймер перерыва на слайде 15
**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.
**Источник правды:** `deck_v3/build.py` (текст слайдов, минуты в `MINUTES`, заметки). Этот сценарий сгенерирован из него (`deck_v3/make_docs.py`); если что-то расходится, прав `build.py`.
**Материалы:** набор для демо `demo_courier_copilot/` (`meeting_notes.md`, `release_checklist.txt`, `orders.csv`, `fallback_outputs/`; `sample_repo/` — запасной пример для слайда 20 и мост в L16), runbook `L07_04_Live_Demo_Runbook_v3.md`, ДЗ `L07_05_Homework_v3.md`, шпаргалка `L07_00_Lecture_Cheatsheet_v3.md`, план `L07_11_Lesson_Plan_v3_Ecosystem.md`.
**Факты:** на 13.10.2026, источники в `L07_12_Research_MS_Ecosystem_2026-10-13.md`. Цены только на слайде 7. Список «перепроверить перед записью» — в `README_v3.md`.

> **Перед стартом (Teams):** два живых демо — A (слайд 8, Copilot Chat на учебном аккаунте IT Park + картинка в личном аккаунте) и B (слайд 9, Vision над `release_checklist.txt`). Опросы в Teams на слайдах 2 и 22. Включите демонстрацию **всего экрана**: нужны приложение Copilot и Блокнот. Наш аккаунт IT Park — **Copilot Chat (Basic)**, без лицензии Microsoft 365 Copilot, поэтому Teams, Word и Excel (слайды 11–13) показываем по слайдам. Правило: «кнопка переехала, правило нет», максимум 90 секунд на поиск, потом слайд с готовым результатом.

**Цель урока:** студенты рисуют карту семьи ИИ Microsoft из четырёх зон (для себя, для работы, для разработчиков, для компании) и выбирают зону по вопросу «чья это информация и где она лежит?»; понимают, что внутри те же модели, что в L03, а разница в том, что Copilot видит и что ему разрешено (отвечает → правит документ → агент); отличают бесплатный Copilot Chat от лицензии Microsoft 365 Copilot; сами делают бриф и картинку в бесплатном Copilot и проверяют ответ по источнику; не вставляют в чат пароли, ключи и данные клиентов.
""",
    "en": """# Instructor Script • Lesson 07 (v3): The Microsoft Copilot Ecosystem, an Overview (90 Minutes)

**Course:** GenAI Basics • Lesson 07 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** IT Park University students, GenAI beginners from many roles. Plain language, no formulas, no code.
**Format:** 24 slides (`presentation_L07_Copilot_Ecosystem_EN_v3.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v3/build.py` (slide text, minutes in `MINUTES`, speaker notes). This script is generated from it (`deck_v3/make_docs.py`); if anything differs, `build.py` wins.
**Materials:** the demo kit `demo_courier_copilot/` (`meeting_notes.md`, `release_checklist.txt`, `orders.csv`, `fallback_outputs/`; `sample_repo/` is the backup example for slide 20 and the bridge to L16), runbook `L07_04_Live_Demo_Runbook_v3_EN.md`, homework `L07_05_Homework_v3_EN.md`, cheatsheet `L07_00_Lecture_Cheatsheet_v3_EN.md`, plan `L07_11_Lesson_Plan_v3_Ecosystem.md`.
**Facts:** as of 13 Oct 2026, sources in `L07_12_Research_MS_Ecosystem_2026-10-13.md`. Prices on slide 7 only. The “verify before recording” list is in `README_v3.md`.

> **Before you start (Teams):** two live demos: A (slide 8, Copilot Chat on the IT Park school account + a picture in the personal account) and B (slide 9, Vision over `release_checklist.txt`). Teams polls on slides 2 and 22. Share your **whole screen**: you need the Copilot app and Notepad. Our IT Park account is **Copilot Chat (Basic)**, with no Microsoft 365 Copilot licence, so Teams, Word and Excel (slides 11–13) are shown from the slides. Rule: “the button moved, the rule did not”, at most 90 seconds of searching, then the slide with the ready result.

**Lesson objective:** students draw the map of the Microsoft AI family in four zones (for you, for work, for developers, for the company) and pick a zone by asking “whose information is it and where does it live?”; understand that inside are the same models as in L03 and the difference is what Copilot sees and is allowed to do (answers → edits the document → agent); tell free Copilot Chat from the Microsoft 365 Copilot licence; make a brief and a picture in free Copilot themselves and check the answer against the source; keep passwords, keys and customer data out of the chat.
""",
}


def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def strip_timer(p):
    """Drop the leading '⏱ N мин.' / '⏱ N min,' marker (the minutes are in the heading)."""
    m = re.match(r"^⏱\s*\d+\s*(мин|min)\s*([.,])\s*", p)
    if not m:
        return p
    rest = p[m.end():]
    return rest[:1].upper() + rest[1:] if m.group(2) == "," else rest


def mmss(m):
    return f"{m:02d}:00"


def main():
    assert len(build.SLIDES) == len(build.MINUTES)
    for lang in ("ru", "en"):
        build.LANG = lang
        t = build.t
        rows, body, start = [], [], 0
        brk = {}
        for i, (fn, m) in enumerate(zip(build.SLIDES, build.MINUTES), 1):
            s = fn()
            assert s["min"] == m, (fn.__name__, s["min"], m)
            title_m = re.search(r'<h2 class="title">(.*?)</h2>', s["html"]) or re.search(r"<h1>(.*?)</h1>", s["html"])
            title = plain(title_m.group(1))
            span = f"{mmss(start)}–{mmss(start + m)}"
            if fn.__name__ == "s_break":
                brk = {"n": i, "start": start, "end": start + m}
            rows.append(f"| **{i:02d}** | {title} | {span} | {m} |")
            paras = [strip_timer(plain(p)) for p in re.findall(r"<p>(.*?)</p>", s["notes"], flags=re.S)]
            speaker = "\n>\n".join(f"> {p}" for p in paras if p)
            body.append(f"### {t('Слайд', 'Slide')} {i:02d} ({span}) • {title}\n\n"
                        f"**{t('На экране', 'On screen')}:** {SCREEN[fn.__name__][0 if lang == 'ru' else 1]}\n\n"
                        f"#### {t('Спикер', 'Speaker')} ({m} {t('мин', 'min')})\n{speaker}\n\n---\n")
            start += m
        n = len(build.SLIDES)
        table = (f"## {t(f'Тайминг ({n} слайдов • {start} минут, включая 5 минут перерыва)', f'Timing ({n} slides • {start} minutes incl. a 5-minute break)')}\n\n"
                 f"| {t('Слайд', 'Slide')} | {t('Заголовок', 'Title')} | {t('Время', 'Time')} | {t('Мин', 'Min')} |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
        b0, b1, nb = mmss(brk["start"]), mmss(brk["end"]), brk["n"]
        parts = t(f"Часть 1 (слайды 01–{nb-1:02d}, 00:00–{b0}): карта семьи, новые слова (модель, чат, ассистент, агент), уровни, одно приложение, цены, обзор приложения Copilot, Vision, Copilot в Windows (лимиты), Teams и Word вживую, Excel, PowerPoint и Outlook. Перерыв (слайд {nb}, {b0}–{b1}). Часть 2 (слайды {nb+1}–{n}, {b1}–{mmss(start)}): агенты, свой агент, GitHub Copilot, Copilot для компании, игра и правила, ДЗ, итоги.",
                  f"Part 1 (slides 01–{nb-1:02d}, 00:00–{b0}): the family map, new words (model, chat, assistant, agent), levels, one app, prices, Copilot app overview, Vision, Copilot in Windows (limits), Teams and Word live, Excel, PowerPoint and Outlook. Break (slide {nb}, {b0}–{b1}). Part 2 (slides {nb+1}–{n}, {b1}–{mmss(start)}): agents, your own agent, GitHub Copilot, Copilot for the company, game and rules, homework, summary.")
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
