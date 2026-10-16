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

L11 = build.L11
OUT = {"ru": L11 / "L11_02_Instructor_Script_90MIN.md", "en": L11 / "L11_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    "s_cover": ("Название урока; справа четыре шага вашей программы: проверить аргументы, спросить человека, выполнить, записать в журнал.",
                "Lesson title; on the right the four steps of your program: check the arguments, ask a human, run, log."),
    "s_hook": ("Слева выдуманный ответ модели без инструментов; справа скриншот AI Studio: вызов get_order_status (фиолетовая рамка), ответ функции (жёлтая) и ответ модели по данным (зелёная).",
               "Left: the model’s invented answer without tools; right: an AI Studio screenshot with the get_order_status call (violet), the function response (amber) and the data-based answer (green)."),
    "s_seen": ("Скриншот Claude: «Searched the web» → «Not conclusive» → «Read 3 pages» → ответ, выноски 1–3 и ✓.",
               "Claude screenshot: “Searched the web” → “Not conclusive” → “Read 3 pages” → answer, callouts 1–3 and ✓."),
    "s_define": ("Скриншот AI Studio «Function declarations»: имя, описание, параметр order_id с выносками.",
                 "AI Studio “Function declarations” screenshot: name, description, order_id parameter with callouts."),
    "s_boundary": ("Схема: модель предлагает вызов, граница доверия, ваша программа проверяет, спрашивает человека, выполняет, записывает в журнал; результат возвращается модели.",
                   "Schematic: the model proposes a call, the trust boundary, your program checks, asks a human, runs, logs; the result goes back to the model."),
    "s_demo_call": ("Скриншот AI Studio: вопрос про заказ 417, блок вызова функции, поле ответа функции.",
                    "AI Studio screenshot: the order 417 question, the function call block, the function response field."),
    "s_demo_done": ("Тот же чат после ответа функции: JSON с данными и ответ модели клиенту.",
                    "The same chat after the function response: the JSON data and the model’s answer to the customer."),
    "s_builtin": ("Панель Tools в AI Studio с выносками и три типа встроенных инструментов.",
                  "The AI Studio Tools panel with callouts and three kinds of built-in tools."),
    "s_describe": ("Две карточки: плохое описание get_data и хорошее get_order_status.",
                   "Two cards: a weak get_data description and a good get_order_status one."),
    "s_loop": ("Схема цикла агента: модель думает → выбирает инструмент → программа выполняет → результат обратно; выход «инструмент не нужен» к финальному ответу; лимит 5 шагов.",
               "Agent loop schematic: the model thinks → picks a tool → the program runs it → result back; the “no tool needed” exit to the final answer; a 5-step limit."),
    "s_code": ("Справочный код на Python (google-genai): функция с docstring передаётся в tools.",
               "Reference Python code (google-genai): a function with a docstring passed in tools."),
    "s_local": ("Модели с поддержкой инструментов в Ollama/LM Studio и предупреждение про маленькие модели.",
                "Tool-capable models in Ollama/LM Studio and a warning about small models."),
    "s_agentbuild": ("Промпт для агента разработки: агент поддержки с двумя функциями, подтверждением, лимитом и журналом.",
                     "Coding-agent prompt: a support agent with two functions, a confirmation, a limit and a log."),
    "s_market": ("Шкала «быстрее начать ↔ больше контроля» и три колонки: агенты в чатах, наборы для разработчиков, свои модели.",
                 "A “quicker to start ↔ more control” strip and three columns: agents in chat apps, developer kits, your own models."),
    "s_break": ("Таймер перерыва 5 минут.", "5-minute break timer."),
    "s_risks": ("Четыре риска (prompt injection, действие без спроса, бесконечный цикл, лишний доступ) и список «Защита — в коде» из пяти пунктов.",
                "Four risks (prompt injection, action without asking, endless loop, too much access) and a five-point “Defences live in code” list."),
    "s_reliability": ("Столбцы «решено с 1 попытки (Pass^1)»: τ²-bench 87,9% и τ³-bench (банк) 55,2%; «≈ 1 из 2».",
                      "Bars “solved in one try (Pass^1)”: τ²-bench 87.9% and τ³-bench (banking) 55.2%; “≈ 1 in 2”."),
    "s_rules": ("Четыре правила (узкие инструменты, проверка в коде, человек подтверждает, лимиты и журнал); это же чек-лист оценки ДЗ.",
                "Four rules (narrow tools, checks in code, a human confirms, limits and a log); also the homework grading checklist."),
    "s_exercise": ("Четыре вопроса клиента со знаком «→ ?»; ответы в заметках спикера.",
                   "Four customer questions marked “→ ?”; the answers are in the speaker notes."),
    "s_hw": ("Пять шагов ДЗ и структура папки сдачи genai-homeworks/L11/.", "Five homework steps and the genai-homeworks/L11/ submission folder layout."),
    "s_summary": ("Четыре вывода урока и анонс L12 (MCP).", "Four takeaways and the L12 (MCP) preview."),
}

HEAD = {
    "ru": """# Сценарий преподавателя • Урок 11: Вызов функций и первый агент (90 минут)

**Курс:** GenAI Basics • Модуль 5 (агенты, инструменты и MCP) • Урок 11 из 16
**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Аудитория:** новички в GenAI из разных ролей. Простой язык; код только как один справочный пример (слайд 11).
**Формат:** 21 слайд (`presentation_L11_Function_Calling_First_Agent_v2.html` / PDF) • занятие в **Microsoft Teams** • таймер перерыва на слайде 15
**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.
**Источник правды:** `deck_v2/build.py` (текст слайдов и заметки). Этот сценарий сгенерирован из него (`deck_v2/make_docs.py`); если что-то расходится, прав `build.py`.
**Факты:** на 16.10.2026, источники в `L11_08_Source_Notes_Research_2026-10.md`. Список «перепроверить за сутки» в конце шпаргалки.

> **Перед уроком:** откройте aistudio.google.com, выберите **Gemini 3.8 Flash** (не платную Gemini 4 Argon), включите Run settings → Tools → **Function calling** и заранее заполните функцию `get_order_status` (имя, описание, параметр `order_id`). Держите под рукой JSON-ответ со слайда 7.

**Цель урока:** студенты понимают, почему модель без инструментов выдумывает текущие данные, умеют описать функцию (имя, описание, параметры), видят полный цикл вызова функции в Google AI Studio, понимают, что модель только предлагает вызов, а выполняет и проверяет программа, знают, что такое агент (модель + инструменты + цикл с лимитом), и знают главные риски (prompt injection, действия без подтверждения) и правила защиты.
""",
    "en": """# Instructor Script • Lesson 11: Function Calling and Your First Agent (90 Minutes)

**Course:** GenAI Basics • Module 5 (Agents, Tools and MCP) • Lesson 11 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language; code only as one short reference example (slide 11).
**Format:** 21 slides (`presentation_L11_Function_Calling_First_Agent_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py` (slide text and speaker notes). This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.
**Facts:** as of 16.10.2026, sources in `L11_08_Source_Notes_Research_2026-10.md`. The “recheck within 24 hours” list is at the end of the cheatsheet.

> **Before class:** open aistudio.google.com, pick **Gemini 3.8 Flash** (not the paid Gemini 4 Argon), turn on Run settings → Tools → **Function calling** and fill in the `get_order_status` function (name, description, `order_id` parameter) in advance. Keep the slide 7 JSON response handy.

**Lesson objective:** students understand why a model without tools invents live data, can describe a function (name, description, parameters), see the full function-calling loop in Google AI Studio, understand that the model only proposes a call while the program runs and checks it, know what an agent is (a model + tools + a loop with a limit), and know the main risks (prompt injection, actions without confirmation) and the defences.
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
        for i, fn in enumerate(build.SLIDES, 1):
            s = fn()
            m = s["min"]
            title_m = re.search(r'<h2 class="title">(.*?)</h2>', s["html"]) or re.search(r"<h1>(.*?)</h1>", s["html"])
            title = plain(title_m.group(1))
            span = f"{mmss(start)}–{mmss(start + m)}"
            rows.append(f"| **{i:02d}** | {title} | {span} | {m} |")
            paras = [plain(p) for p in re.findall(r"<p>(.*?)</p>", s["notes"], flags=re.S)]
            paras = [re.sub(r"^⏱\s*\d+\s*(мин|min)\.\s*", "", p) for p in paras]
            speaker = "\n>\n".join(f"> {p}" for p in paras if p)
            body.append(f"### {t('Слайд', 'Slide')} {i:02d} ({span}) • {title}\n\n"
                        f"**{t('На экране', 'On screen')}:** {SCREEN[fn.__name__][0 if lang == 'ru' else 1]}\n\n"
                        f"#### {t('Спикер', 'Speaker')} ({m} {t('мин', 'min')})\n{speaker}\n\n---\n")
            start += m
        table = (f"## {t('Тайминг (21 слайд • 90 минут, включая 5 минут перерыва)', 'Timing (21 slides • 90 minutes incl. a 5-minute break)')}\n\n"
                 f"| {t('Слайд', 'Slide')} | {t('Заголовок', 'Title')} | {t('Время', 'Time')} | {t('Мин', 'Min')} |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
        # Part/break times are computed from the slide minutes, so they cannot drift from the table.
        mins = [fn()["min"] for fn in build.SLIDES]
        b = next(i for i, fn in enumerate(build.SLIDES) if fn.__name__ == "s_break")
        p1, brk_end, total = sum(mins[:b]), sum(mins[:b + 1]), sum(mins)
        n = len(mins)
        parts = t(f"Часть 1 (слайды 01–{b:02d}, {mmss(0)}–{mmss(p1)}): проблема, инструменты в чатах, описание функции, граница доверия, демо в AI Studio, встроенные инструменты, цикл агента, код, локальные модели, рынок. "
                  f"Перерыв (слайд {b + 1:02d}, {mmss(p1)}–{mmss(brk_end)}). Часть 2 (слайды {b + 2:02d}–{n:02d}, {mmss(brk_end)}–{mmss(total)}): риски, надёжность, правила, упражнение, ДЗ, итоги.",
                  f"Part 1 (slides 01–{b:02d}, {mmss(0)}–{mmss(p1)}): the problem, tools in chat apps, describing a function, the trust boundary, the AI Studio demo, built-in tools, the agent loop, code, local models, market. "
                  f"Break (slide {b + 1:02d}, {mmss(p1)}–{mmss(brk_end)}). Part 2 (slides {b + 2:02d}–{n:02d}, {mmss(brk_end)}–{mmss(total)}): risks, reliability, rules, exercise, homework, summary.")
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
