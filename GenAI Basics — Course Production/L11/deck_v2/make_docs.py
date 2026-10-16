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
    "s_cover": ("Название урока; справа фрагмент схемы «модель предлагает, приложение выполняет».",
                "Lesson title; on the right part of the “model proposes, app executes” schematic."),
    "s_hook": ("Слева выдуманный ответ модели без инструментов; справа скриншот AI Studio: вызов get_order_status и ответ по данным.",
               "Left: the model’s invented answer without tools; right: an AI Studio screenshot with the get_order_status call and the data-based answer."),
    "s_seen": ("Скриншот Claude: «Searched the web» → «Not conclusive» → «Read 3 pages» → ответ, выноски 1–3 и ✓.",
               "Claude screenshot: “Searched the web” → “Not conclusive” → “Read 3 pages” → answer, callouts 1–3 and ✓."),
    "s_define": ("Скриншот AI Studio «Function declarations»: имя, описание, параметр order_id с выносками.",
                 "AI Studio “Function declarations” screenshot: name, description, order_id parameter with callouts."),
    "s_boundary": ("Схема: модель предлагает вызов, граница доверия, приложение проверяет, спрашивает человека, выполняет, логирует.",
                   "Schematic: the model proposes a call, trust boundary, the app checks, asks a human, runs, logs."),
    "s_demo_call": ("Скриншот AI Studio: вопрос про заказ 417, блок вызова функции, поле ответа функции.",
                    "AI Studio screenshot: the order 417 question, the function call block, the function response field."),
    "s_demo_done": ("Тот же чат после ответа функции: JSON с данными и ответ модели клиенту.",
                    "The same chat after the function response: the JSON data and the model’s answer to the customer."),
    "s_builtin": ("Панель Tools в AI Studio с выносками и три типа встроенных инструментов.",
                  "The AI Studio Tools panel with callouts and three kinds of built-in tools."),
    "s_describe": ("Две карточки: плохое описание get_data и хорошее get_order_status.",
                   "Two cards: a weak get_data description and a good get_order_status one."),
    "s_loop": ("Схема цикла агента: думает → выбирает инструмент → приложение выполняет → результат обратно; выход к финальному ответу; лимит 5 шагов.",
               "Agent loop schematic: thinks → picks a tool → the app runs it → result back; exit to the final answer; a 5-step limit."),
    "s_code": ("Справочный код на Python (google-genai): функция с docstring передаётся в tools.",
               "Reference Python code (google-genai): a function with a docstring passed in tools."),
    "s_local": ("Модели с поддержкой инструментов в Ollama/LM Studio и предупреждение про маленькие модели.",
                "Tool-capable models in Ollama/LM Studio and a warning about small models."),
    "s_agentbuild": ("Промпт для агента разработки: агент поддержки с двумя функциями, подтверждением, лимитом и журналом.",
                     "Coding-agent prompt: a support agent with two functions, a confirmation, a limit and a log."),
    "s_market": ("Три колонки: агенты в чатах, наборы для разработчиков, свои модели.",
                 "Three columns: agents in chat apps, developer kits, your own models."),
    "s_break": ("Таймер перерыва 5 минут.", "5-minute break timer."),
    "s_risks": ("Четыре риска (prompt injection, действие без спроса, цикл, лишний доступ) и плашка с защитой.",
                "Four risks (prompt injection, action without asking, loop, too much access) and a defences panel."),
    "s_reliability": ("Столбцы τ²-bench 87,9% и τ³-bench (банк) 55,2%; «≈ 1 из 2».",
                      "Bars: τ²-bench 87.9% and τ³-bench (banking) 55.2%; “≈ 1 in 2”."),
    "s_rules": ("Четыре правила первого агента.", "Four rules for the first agent."),
    "s_exercise": ("Четыре вопроса клиента и правильный инструмент для каждого.",
                   "Four customer questions and the right tool for each."),
    "s_hw": ("Пять шагов ДЗ и структура папки сдачи.", "Five homework steps and the submission folder layout."),
    "s_summary": ("Четыре вывода урока и анонс L12 (MCP).", "Four takeaways and the L12 (MCP) preview."),
}

HEAD = {
    "ru": """# Сценарий преподавателя • Урок 11: Вызов функций и первый агент (90 минут)

**Курс:** GenAI Basics • Модуль 3 (свои модели и агенты) • Урок 11 из 16
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

**Course:** GenAI Basics • Module 3 (Own Models and Agents) • Lesson 11 of 16
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
        parts = t("Часть 1 (слайды 01–14, 00:00–60:00): проблема, инструменты в чатах, описание функции, граница доверия, демо в AI Studio, встроенные инструменты, цикл агента, код, локальные модели, рынок. Перерыв (слайд 15, 60:00–65:00). Часть 2 (слайды 16–21, 65:00–90:00): риски, надёжность, правила, упражнение, ДЗ, итоги.",
                  "Part 1 (slides 01–14, 00:00–60:00): the problem, tools in chat apps, describing a function, the trust boundary, the AI Studio demo, built-in tools, the agent loop, code, local models, market. Break (slide 15, 60:00–65:00). Part 2 (slides 16–21, 65:00–90:00): risks, reliability, rules, exercise, homework, summary.")
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
