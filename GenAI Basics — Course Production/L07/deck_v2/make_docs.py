# -*- coding: utf-8 -*-
"""Generate the 90-minute instructor scripts (RU + EN) from the deck generator.

    python make_docs.py

The timing table, slide titles and the speaker text come straight from build.py
(minutes per slide and speaker notes), so the script cannot drift from the deck.
Only the short "On screen" descriptions and the header live here.
"""
import html
import re

import build

L07 = build.L07
OUT = {"ru": L07 / "L07_02_Instructor_Script_90MIN.md", "en": L07 / "L07_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    "s_cover": ("Фон: кадр из шота 2 L05 (курьер под дождём). Заголовок, подзаголовок, «3 Copilot • 1 команда • 1 фича • 1 неделя», подсказки по клавишам.",
                "Background: a frame from L05 shot 2 (the courier in the rain). Title, subtitle, “3 Copilots • 1 team • 1 feature • 1 week”, key hints."),
    "s_week": ("Полоса «понедельник–пятница» с шестью станциями: Teams, Word, GitHub issue, VS Code, pull request, Windows. У каждой станции строка из настоящего результата.",
               "A Monday–Friday strip with six stations: Teams, Word, GitHub issue, VS Code, pull request, Windows. Each station shows a line from the real result."),
    "s_three": ("Три круга: репозиторий (GitHub Copilot), рабочие документы (Copilot в Word и Teams), ваш ПК (Copilot в Windows). В каждом по два артефакта фичи и строка «видит».",
                "Three circles: repository (GitHub Copilot), work documents (Copilot in Word and Teams), your PC (Copilot in Windows). Each has two artifacts of the feature and a “Sees” line."),
    "s_model": ("Схема «вопрос + что он видит (файл, чат, репозиторий, экран) → модель → ответ». В углу вызов из L03 с добавленным текстом файла.",
                "Diagram: question + what it sees (file, chat, repository, screen) → model → answer. In the corner, the L03 call with the file text added."),
    "s_teams": ("Макет окна Teams (схема): встреча «Prime delivery rule», справа панель Copilot Recap: решения, открытые вопросы, задачи. Внизу: нет доступа — вставьте meeting_notes.md в бесплатный Copilot Chat.",
                "Teams window mockup (schematic): meeting “Prime delivery rule”, Copilot Recap pane on the right: decisions, open questions, action items. Below: no access? paste meeting_notes.md into free Copilot Chat."),
    "s_word": ("Макет Word (схема): страница брифа и панель Copilot с промптом. Предложения из заметок и слова Copilot (строка про эффект) отмечены по-разному.",
               "Word mockup (schematic): the brief page and the Copilot pane with the prompt. Sentences from the notes and Copilot’s own words (the effect line) are marked differently."),
    "s_outlook_excel": ("Два макета: ветка Outlook со сводкой и таблица Excel из 8 заказов с ответом Copilot («3 из 5»). Анализ данных будет в L08.",
                        "Two mockups: an Outlook thread with a summary, and an Excel table of 8 orders with a Copilot answer (“3 of 5”). Data analysis comes in L08."),
    "s_money": ("Октябрь 2026, цены в USD. Два кольца: бесплатное (то, что вы показали) и по лицензии (почта, файлы, встречи). Полоса тарифов GitHub Copilot и Microsoft. Единственный слайд с ценами.",
                "October 2026, US prices. Two rings: free (what you give it) and licensed (mail, files, meetings). A strip of GitHub Copilot and Microsoft plans. The only slide with prices."),
    "s_issue": ("Макет страницы GitHub issue #12 (схема): пять пунктов и приёмка, исполнитель Павел, метка feature; кнопка «Assign to Copilot» серая (облачный агент, L16).",
                "GitHub issue #12 page mockup (schematic): five bullets and acceptance, assignee Pavel, label feature; the “Assign to Copilot” button is grey (cloud agent, L16)."),
    "s_editor": ("Макет VS Code (схема): файл delivery_fee.py с серой подсказкой (completion), чат с двумя промптами Павла, терминал. Три способа: подсказка, чат, агент.",
                 "VS Code mockup (schematic): delivery_fee.py with grey ghost text (completion), chat with Pavel’s two prompts, terminal. Three ways: completion, chat, agent."),
    "s_result": ("Настоящий запуск: git diff (2 строки логики и 3 теста) и вывод python -m unittest -v (7 ok). Берётся из deck_v2/artifacts.json.",
                 "A real run: git diff (2 lines of logic and 3 tests) and python -m unittest -v output (7 ok). Taken from deck_v2/artifacts.json."),
    "s_pr": ("Макет pull request #13 (схема): Files changed с настоящим diff, комментарий Copilot-ревью, «Approved: Ola», проверки «tests 7/7».",
             "Pull request #13 mockup (schematic): Files changed with the real diff, a Copilot review comment, “Approved: Ola”, checks “tests 7/7”."),
    "s_instr": ("Файл .github/copilot-instructions.md (5 правил); стрелки к тому месту результата, где каждое правило сработало.",
                "The .github/copilot-instructions.md file (5 rules); arrows to where each rule shows up in the result."),
    "s_doors": ("Карта из четырёх дверей к GitHub Copilot: редактор, github.com, терминал (CLI), облачный агент; метки «Free: да / зависит от тарифа / да / нет».",
                "A map of four doors to GitHub Copilot: editor, github.com, terminal (CLI), cloud agent; tags for what is on Free."),
    "s_break": ("Таймер 5 минут, кнопки «Старт» и «Сброс».", "5-minute timer, Start and Reset buttons."),
    "s_windows": ("Макет рабочего стола Windows (схема): окно с чек-листом, окно Copilot с Vision, клавиатура с подсвеченной клавишей Copilot; пять возможностей. Внизу: рабочие аккаунты открывают веб-чат.",
                  "Windows desktop mockup (schematic): a window with the checklist, the Copilot window with Vision, a keyboard with the Copilot key highlighted; five features. Below: work accounts open the web chat."),
    "s_notepad": ("Макет Блокнота с release_checklist.txt (6 пунктов) и ответ Copilot: пункт 6. Если кнопки нет, вставьте текст в чат.",
                  "Notepad mockup with release_checklist.txt (6 items) and the Copilot answer: item 6. No button? paste the text into the chat."),
    "s_six": ("Чек-лист из 6 проверок с результатом нашей недели ($75 · $100 · $18.00, +2 строки, 7 из 7, 1 комментарий, 3 скриншота). Это рубрика ДЗ.",
              "A 6-check list with the result of our week ($75 · $100 · $18.00, +2 lines, 7 of 7, 1 comment, 3 screenshots). This is the homework rubric."),
    "s_limits": ("Человек с ключом и три ловушки: не тот аккаунт, секрет в чате, «Готово!». Внизу: обучение на данных (рабочие аккаунты нет; личный GitHub с 24 апреля 2026, выключить в настройках).",
                 "A person with a key and three traps: wrong account, a secret in the chat, “Done!”. Below: training on your data (work accounts no; personal GitHub since 24 April 2026, switch it off in settings)."),
    "s_hw": ("Карточка репозитория courier-copilot-week (дерево файлов), фича, инструменты (только бесплатные), оценка по шести проверкам слайда 18.",
             "The courier-copilot-week repository card (file tree), the feature, tools (free only), grading by the six checks of slide 18."),
    "s_summary": ("Сжатая полоса недели, пять правил и плитка L08 (таблица из слайда 7).", "The compressed week strip, five rules and the L08 tile (the table from slide 7)."),
}

HEAD = {
    "ru": """# Сценарий преподавателя • Урок 07: GitHub, Microsoft 365 и Windows Copilot. Одна фича, три Copilot (90 минут)

**Курс:** GenAI Basics • Урок 07 из 16
**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Аудитория:** новички в GenAI из разных ролей. Простой язык, без формул; код только как короткий пример.
**Формат:** 21 слайд (`presentation_L07_Copilot_Ecosystem_v2.html` / PDF) • занятие в **Microsoft Teams** • таймер перерыва на слайде 15
**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.
**Источник правды:** `deck_v2/build.py` (текст слайдов и заметки). Этот сценарий сгенерирован из него (`deck_v2/make_docs.py`); если что-то расходится, прав `build.py`.
**Материалы:** набор для демо `demo_courier_copilot/` (`sample_repo/`, `meeting_notes.md`, `release_checklist.txt`, `fallback_outputs/`, `surface_preflight.md`), настоящий diff и вывод тестов `deck_v2/artifacts.json` (делает `deck_v2/make_artifacts.py`), runbook `L07_04_Live_Demo_Runbook_READY.md`, ДЗ `L07_05_Homework.md`.
**Факты:** на октябрь 2026, источники в `L07_08_Source_Notes_Research_2026-10.md`. Цены и названия продуктов только на слайде 8. Список «перепроверить за сутки» в конце шпаргалки.

> **Перед стартом (Teams):** в уроке три живых демо (слайды 6, 10–11, 17). Включите демонстрацию **всего экрана**, а не одного окна: нужны браузер, VS Code, терминал и Блокнот. Заранее пройдите `demo_courier_copilot/surface_preflight.md` (10 минут). Если кнопки Copilot нет или интерфейс изменился, правило такое: «кнопка переехала, правило нет», максимум 90 секунд на поиск, потом слайд с готовым результатом.

**Цель урока:** студенты знают, что Copilot бывает трёх видов по месту, где лежит информация (репозиторий, рабочие документы, ваш ПК), понимают, что внутри та же модель, что в L03, а результат зависит от того, что она видит; умеют провести маленькую фичу через встречу, бриф, issue, код, pull request и чек-лист; принимают результат по 6 проверкам (diff и тесты, а не слово «готово»); знают, что бесплатно, и не отправляют в запрос секреты и данные клиентов.
""",
    "en": """# Instructor Script • Lesson 07: GitHub, Microsoft 365 and Windows Copilot. One Feature, Three Copilots (90 Minutes)

**Course:** GenAI Basics • Lesson 07 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language, no formulas; code only as one short example.
**Format:** 21 slides (`presentation_L07_Copilot_Ecosystem_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py` (slide text and speaker notes). This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.
**Materials:** the demo kit `demo_courier_copilot/` (`sample_repo/`, `meeting_notes.md`, `release_checklist.txt`, `fallback_outputs/`, `surface_preflight.md`), the real diff and test output in `deck_v2/artifacts.json` (made by `deck_v2/make_artifacts.py`), runbook `L07_04_Live_Demo_Runbook_READY_EN.md`, homework `L07_05_Homework_EN.md`.
**Facts:** as of October 2026, sources in `L07_08_Source_Notes_Research_2026-10.md`. Prices and product names appear on slide 8 only. The “recheck within 24 hours” list is at the end of the cheatsheet.

> **Before you start (Teams):** the lesson has three live demos (slides 6, 10–11, 17). Share your **whole screen**, not one window: you need a browser, VS Code, a terminal and Notepad. Run through `demo_courier_copilot/surface_preflight.md` beforehand (10 minutes). If a Copilot button is missing or the interface changed, the rule is: “the button moved, the rule did not”, at most 90 seconds of searching, then the slide with the ready result.

**Lesson objective:** students know that Copilot comes in three kinds by the place where the information lives (repository, work documents, your PC), understand that inside is the same model as in L03 and the result depends on what it sees; can take a small feature through a meeting, a brief, an issue, code, a pull request and a checklist; accept the result with 6 checks (the diff and the tests, not the word “done”); know what is free, and keep secrets and customer data out of every request.
""",
}


def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def mmss(m):
    return f"{m:02d}:00"


def main():
    for lang in ("ru", "en"):
        build.LANG = lang
        t = build.t
        rows, body, start = [], [], 0
        brk = {}
        for i, fn in enumerate(build.SLIDES, 1):
            s = fn()
            m = s["min"]
            title_m = re.search(r'<h2 class="title">(.*?)</h2>', s["html"]) or re.search(r"<h1>(.*?)</h1>", s["html"])
            title = plain(title_m.group(1))
            span = f"{mmss(start)}–{mmss(start + m)}"
            if fn.__name__ == "s_break":
                brk = {"n": i, "start": start, "end": start + m}
            rows.append(f"| **{i:02d}** | {title} | {span} | {m} |")
            paras = [plain(p) for p in re.findall(r"<p>(.*?)</p>", s["notes"], flags=re.S)]
            paras = [re.sub(r"^⏱\s*\d+\s*(мин|min)\.\s*", "", p) for p in paras]
            speaker = "\n>\n".join(f"> {p}" for p in paras if p)
            body.append(f"### {t('Слайд', 'Slide')} {i:02d} ({span}) • {title}\n\n"
                        f"**{t('На экране', 'On screen')}:** {SCREEN[fn.__name__][0 if lang == 'ru' else 1]}\n\n"
                        f"#### {t('Спикер', 'Speaker')} ({m} {t('мин', 'min')})\n{speaker}\n\n---\n")
            start += m
        n = len(build.SLIDES)
        table = (f"## {t(f'Тайминг ({n} слайдов • {start} минут, включая 5 минут перерыва)', f'Timing ({n} slides • {start} minutes incl. a 5-minute break)')}\n\n"
                 f"| {t('Слайд', 'Slide')} | {t('Заголовок', 'Title')} | {t('Время', 'Time')} | {t('Мин', 'Min')} |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
        b0, b1, nb = mmss(brk["start"]), mmss(brk["end"]), brk["n"]
        parts = t(f"Часть 1 (слайды 01–{nb-1:02d}, 00:00–{b0}): три места, как работает Copilot, Teams, Word, Outlook и Excel, цены, issue, редактор, результат, pull request, инструкции, двери GitHub Copilot. Перерыв (слайд {nb}, {b0}–{b1}). Часть 2 (слайды {nb+1}–{n}, {b1}–{mmss(start)}): Windows, чек-лист релиза, шесть проверок, границы, ДЗ, итоги.",
                  f"Part 1 (slides 01–{nb-1:02d}, 00:00–{b0}): three places, how Copilot works, Teams, Word, Outlook and Excel, prices, issue, editor, result, pull request, instructions, doors of GitHub Copilot. Break (slide {nb}, {b0}–{b1}). Part 2 (slides {nb+1}–{n}, {b1}–{mmss(start)}): Windows, release checklist, six checks, limits, homework, summary.")
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
