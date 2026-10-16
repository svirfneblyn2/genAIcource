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

L14 = build.L14
OUT = {"ru": L14 / "L14_02_Instructor_Script_90MIN.md", "en": L14 / "L14_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    's_cover': ('Название урока; справа набросок окна чата.',
                'Lesson title; a chat-window sketch on the right.'),
    's_hook': ('Схема: идея → прототип (1 день) → отзывы (3 человека) → продукт; скобка «этот урок».',
                'Schematic: idea → prototype (1 day) → feedback (3 people) → product; a “this lesson” bracket.'),
    's_what': ('Фрагмент скриншота официального чата llm-examples.streamlit.app с выносками: поле ключа, сообщения, поле ввода.',
                'Excerpt of the official llm-examples.streamlit.app chat screenshot with callouts: key field, messages, input box.'),
    's_code': ('Справочный код чата на 14 строк (с заглушкой ask_llm, запускается как есть) с выделенными session_state, chat_input, ask_llm.',
                'Reference 14-line chat code (with an ask_llm stub, runs as is) with session_state, chat_input and ask_llm highlighted.'),
    's_rerun': ('Схема цикла: клик → файл выполняется заново → память восстановлена → страница перерисована.',
                'Loop schematic: click → the file reruns → memory restored → page redrawn.'),
    's_three': ('Три карточки: session_state, cache_data, secrets.',
                'Three cards: session_state, cache_data, secrets.'),
    's_agent': ('Промпт для агента разработки: Streamlit-чат по faq.md с демо-режимом и секретами.',
                'Coding-agent prompt: a Streamlit chat over faq.md with a demo mode and secrets.'),
    's_run': ('Четыре шага: установить, запустить, править, показать.',
                'Four steps: install, run, edit, show.'),
    's_deploy': ('Три места публикации и предупреждение «публичная ссылка = публичные данные».',
                'Three places to publish and the warning “a public link = public data”.'),
    's_alternatives': ('Скриншот Google AI Studio Build и три конструктора без кода.',
                'Google AI Studio Build screenshot and three no-code builders.'),
    's_when': ('Сетка 2×2: показать идею / работать с данными × программирую / нет.',
                '2×2 grid: show an idea / work with data × code / no code.'),
    's_break': ('Таймер перерыва 5 минут.',
                '5-minute break timer.'),
    's_practice': ('Пять шагов практики: прототип помощника по FAQ; два пути и тайминг 7 + 3 минуты.',
                'Five hands-on steps: an FAQ helper prototype; two paths and a 7 + 3 minute timing.'),
    's_safety': ('Четыре правила: ключи, данные, деньги, вход.',
                'Four rules: keys, data, money, sign-in.'),
    's_product': ('Сравнение «прототип → продукт» по четырём пунктам.',
                '“Prototype → product” comparison on four points.'),
    's_hw': ('Пять шагов ДЗ и структура папки.',
                'Five homework steps and the folder layout.'),
    's_summary': ('Четыре вывода и анонс L15; заголовок — главная мысль урока.',
                'Four takeaways and the L15 preview; the title is the lesson’s main point.'),
}

HEAD = {
    "ru": '# Сценарий преподавателя • Урок 14: Быстрый прототип ИИ-приложения — Streamlit и конструкторы без кода (90 минут)\n\n**Курс:** GenAI Basics • Модуль 6 (от идеи к продукту) • Урок 14 из 16\n**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Аудитория:** новички в GenAI из разных ролей. Код пишет агент разработки; студенты учатся понимать и проверять его (слайд 4 — справочный).\n**Формат:** 17 слайдов (`presentation_L14_Streamlit_Rapid_Prototyping_v2.html` / PDF) • **Microsoft Teams** • перерыв на слайде 12 • практика 10 минут на слайде 13\n**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.\n**Источник правды:** `deck_v2/build.py`; сценарий сгенерирован из него (`deck_v2/make_docs.py`).\n**Факты:** на 16.10.2026, источники в `L14_08_Source_Notes_Research_2026-10.md`.\n\n> **Перед уроком:** откройте llm-examples.streamlit.app (официальный демо-чат, может «спать» и просыпаться до минуты) и aistudio.google.com/apps (Build). Если показываете Streamlit вживую — Python 3.11+, `pip install streamlit`, `streamlit run app.py`.\n\n**Цель урока:** студенты понимают, зачем нужен быстрый прототип, как устроен Streamlit (Python, перезапуск, session_state, cache, secrets), умеют поставить задачу агенту разработки и запустить прототип, знают, где его опубликовать и чем это рискованно, и когда хватит конструктора без кода.\n',
    "en": '# Instructor Script • Lesson 14: Rapid AI App Prototype — Streamlit and No-Code Builders (90 Minutes)\n\n**Course:** GenAI Basics • Module 6 (Idea to Product) • Lesson 14 of 16\n**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Audience:** GenAI beginners from many roles. A coding agent writes the code; students learn to understand and check it (slide 4 is a reference).\n**Format:** 17 slides (`presentation_L14_Streamlit_Rapid_Prototyping_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 12 • 10-minute hands-on on slide 13\n**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.\n**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).\n**Facts:** as of 16.10.2026, sources in `L14_08_Source_Notes_Research_2026-10.md`.\n\n> **Before class:** open llm-examples.streamlit.app (the official demo chat; it may be asleep and take up to a minute to wake) and aistudio.google.com/apps (Build). If you run Streamlit live — Python 3.11+, `pip install streamlit`, `streamlit run app.py`.\n\n**Lesson objective:** students understand why a rapid prototype helps, how Streamlit works (Python, reruns, session_state, cache, secrets), can brief a coding agent and run the prototype, know where to publish it and the risks, and when a no-code builder is enough.\n',
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
        table = (f"## {t('Тайминг (17 слайдов • 90 минут, включая 5 минут перерыва)', 'Timing (17 slides • 90 minutes incl. a 5-minute break)')}\n\n"
                 f"| {t('Слайд', 'Slide')} | {t('Заголовок', 'Title')} | {t('Время', 'Time')} | {t('Мин', 'Min')} |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
        # part/break times computed from the slide minutes, so they cannot drift from the deck
        mins = [fn()["min"] for fn in build.SLIDES]
        b = [fn.__name__ for fn in build.SLIDES].index("s_break")
        t1, t2, n = sum(mins[:b]), sum(mins[:b + 1]), len(mins)
        parts = t(f'Часть 1 (слайды 01–{b:02d}, 00:00–{mmss(t1)}): зачем прототип, Streamlit, код, перезапуск, память/кэш/секреты, агент, запуск, публикация, конструкторы, выбор. '
                  f'Перерыв (слайд {b + 1:02d}, {mmss(t1)}–{mmss(t2)}). Часть 2 (слайды {b + 2:02d}–{n:02d}, {mmss(t2)}–{mmss(sum(mins))}): практика, безопасность, путь к продукту, ДЗ, итоги.',
                  f'Part 1 (slides 01–{b:02d}, 00:00–{mmss(t1)}): why a prototype, Streamlit, code, reruns, memory/cache/secrets, the agent, running, publishing, builders, choosing. '
                  f'Break (slide {b + 1:02d}, {mmss(t1)}–{mmss(t2)}). Part 2 (slides {b + 2:02d}–{n:02d}, {mmss(t2)}–{mmss(sum(mins))}): hands-on, security, the path to a product, homework, summary.')
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
