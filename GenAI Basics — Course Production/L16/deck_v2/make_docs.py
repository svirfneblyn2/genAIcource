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

L16 = build.L16
OUT = {"ru": L16 / "L16_02_Instructor_Script_90MIN.md", "en": L16 / "L16_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    's_cover': ('Название урока; справа схема: окно терминала и ветка git.',
                'Lesson title; on the right a terminal window and a git branch.'),
    's_hook': ('Две цепочки по 4 шага: чат (вы переносите код) и агент (сам правит и проверяет).',
               'Two 4-step chains: chat (you carry the code) and agent (edits and checks itself).'),
    's_anatomy': ('Схема агента (HTML): модель + чтение, правка, команды, MCP; слева AGENTS.md, справа разрешения.',
                  'Agent diagram: model + read, edit, commands, MCP; AGENTS.md on the left, permissions on the right.'),
    's_landscape': ('Три ценовые полосы (бирюзовая, жёлтая, красная): $0, $10–30, от $100; плашка «начните с бесплатного».',
                    'Three price bands: $0, $10–30, $100+; a “start free” plaque.'),
    's_loop': ('Цикл план → действие → проверка → ревью (HTML), в центре «вы у руля».',
               'The plan → act → verify → review loop (HTML), “you steer” in the centre.'),
    's_task': ('Расплывчатая просьба → TASK.md с целью, границами и командой проверки.',
               'A vague request → TASK.md with a goal, limits and a check command.'),
    's_rules_file': ('Пример AGENTS.md; 60 000+ проектов; какие агенты его читают.',
                     'An AGENTS.md example; 60,000+ projects; which agents read it.'),
    's_permissions': ('Скриншот Claude Code: auto mode по умолчанию; 93% и ~17%; шкала пяти режимов.',
                      'Claude Code screenshot: auto mode is the default; 93% and ~17%; a scale of five modes.'),
    's_verify': ('Настоящий вывод pytest на стартовом проекте ДЗ (1 failed → 3 passed) и 4 шага: тест падает → агент чинит → всё зелёное → вы читаете diff; откат и git.',
                 'Real pytest output on the homework starter (1 failed → 3 passed) and 4 steps: a test fails → the agent fixes → all green → you read the diff; undo and git.'),
    's_metr': ('Столбики METR: ожидали +24%, казалось +20%, измерили −19%.',
               'METR bars: expected +24%, felt +20%, measured −19%.'),
    's_incidents': ('Три случая: 9 секунд (PocketOS), «заморозка» (Replit), 2 349 секретов (Nx); Clinejection.',
                    'Three cases: 9 seconds (PocketOS), code freeze (Replit), 2,349 secrets (Nx); Clinejection.'),
    's_break': ('Таймер перерыва 5 минут.', 'A 5-minute break timer.'),
    's_safe': ('Шесть правил безопасной работы с метками инцидентов; плашка про режим без проверок.', 'Six safe-work rules tagged with incidents; a plaque on the no-checks mode.'),
    's_exercise': ('Просьба «фильтр по приоритету» и 4 шага: TASK.md, AGENTS.md, план, решение.',
                   'The “priority filter” request and 4 steps: TASK.md, AGENTS.md, plan, decision.'),
    's_hw': ('Шесть шагов ДЗ (стартовый проект или свой репозиторий), папка genai-homeworks/L16/, путь для непрограммистов (только README).', 'Six homework steps (starter project or own repo), the genai-homeworks/L16/ folder, a path for non-coders (README only).'),
    's_summary': ('Четыре правила урока и завершение курса.', 'The four rules of the lesson and the end of the course.'),
}

HEAD = {
    "ru": '# Сценарий преподавателя • Урок 16: Агентная разработка — агенты для кода, IDE и CLI (90 минут)\n\n**Курс:** GenAI Basics • Модуль 6 (от идеи к продукту) • Урок 16 из 16 (последний)\n**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Аудитория:** новички в GenAI из разных ролей; часть студентов не программисты. Объясняйте термины (diff, ветка, тест) по ходу.\n**Формат:** 16 слайдов (`presentation_L16_Agentic_Software_Development_v2.html` / PDF) • **Microsoft Teams** • перерыв на слайде 12\n**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.\n**Источник правды:** `deck_v2/build.py`; сценарий сгенерирован из него (`deck_v2/make_docs.py`).\n**Факты:** на 16.10.2026, источники и статус проверки в `L16_08_Source_Notes_Research_2026-10.md`.\n\n> **Перед уроком:** перепроверьте цены и названия тарифов (слайд 4) и режим по умолчанию в Claude Code (слайд 8): они меняются каждый месяц.\n\n**Цель урока:** студенты понимают, чем агент для кода отличается от чата, знают ценовые полосы инструментов, умеют ставить агенту проверяемую задачу (TASK.md) и писать AGENTS.md, выбирают режим разрешений, проверяют результат тестом и diff, знают реальные инциденты и шесть правил безопасной работы.\n',
    "en": '# Instructor Script • Lesson 16: Agentic Software Development — Coding Agents, IDEs and CLIs (90 Minutes)\n\n**Course:** GenAI Basics • Module 6 (Idea to Product) • Lesson 16 of 16 (the last)\n**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Audience:** GenAI beginners from many roles; some students are not programmers. Explain terms (diff, branch, test) as you go.\n**Format:** 16 slides (`presentation_L16_Agentic_Software_Development_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 12\n**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.\n**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).\n**Facts:** as of 16.10.2026, sources and verification status in `L16_08_Source_Notes_Research_2026-10.md`.\n\n> **Before class:** recheck prices and plan names (slide 4) and Claude Code’s default mode (slide 8): they change every month.\n\n**Lesson objective:** students understand how a coding agent differs from a chat, know the tools’ price bands, can give an agent a checkable task (TASK.md) and write AGENTS.md, choose a permission mode, check the result with a test and the diff, know real incidents and the six safe-work rules.\n',
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
        table = (f"## {t('Тайминг (16 слайдов • 90 минут, включая 5 минут перерыва)', 'Timing (16 slides • 90 minutes incl. a 5-minute break)')}\n\n"
                 f"| {t('Слайд', 'Slide')} | {t('Заголовок', 'Title')} | {t('Время', 'Time')} | {t('Мин', 'Min')} |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
        # Part times are computed from the slide minutes, so they cannot drift from the deck.
        mins = [f()["min"] for f in build.SLIDES]
        b = [f.__name__ for f in build.SLIDES].index("s_break")  # 0-based index of the break slide
        n = len(mins)
        p1, br = sum(mins[:b]), sum(mins[:b + 1])
        parts = t(f'Часть 1 (слайды 01–{b:02d}, {mmss(0)}–{mmss(p1)}): чат и агент, устройство агента, цены, цикл работы, задача, AGENTS.md, разрешения, проверка, METR, инциденты. '
                  f'Перерыв (слайд {b + 1:02d}, {mmss(p1)}–{mmss(br)}). Часть 2 (слайды {b + 2:02d}–{n:02d}, {mmss(br)}–{mmss(start)}): правила безопасной работы, практика, ДЗ, итоги курса.',
                  f'Part 1 (slides 01–{b:02d}, {mmss(0)}–{mmss(p1)}): chat vs agent, agent anatomy, prices, the work loop, the task, AGENTS.md, permissions, verification, METR, incidents. '
                  f'Break (slide {b + 1:02d}, {mmss(p1)}–{mmss(br)}). Part 2 (slides {b + 2:02d}–{n:02d}, {mmss(br)}–{mmss(start)}): safe-work rules, practice, homework, course summary.')
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
