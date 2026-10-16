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

L13 = build.L13
OUT = {"ru": L13 / "L13_02_Instructor_Script_90MIN.md", "en": L13 / "L13_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    's_cover': ('Название урока; справа карточка «Ваш ассистент».',
                'Lesson title; on the right the “Your assistant” card.'),
    's_hook': ('Схема (HTML): инструкции + знания + инструменты + модель = ваш ассистент.',
                'Schematic: instructions + knowledge + tools + model = your assistant.'),
    's_retire': ('Скриншот баннера ChatGPT «Перенесите свои GPT в плагины до 11 декабря», подпись с переводом и три блока: что переносится, что нет, Gems.',
                'Screenshot of the ChatGPT banner “Move your GPTs to plugins by 11 December”, a translated caption and three blocks: what moves, what doesn’t, Gems.'),
    's_claude_project': ('Крупный скриншот проекта Claude «Демо L09» (название и правая панель) с выносками: описание, Instructions, Context, Memory.',
                'Large screenshot of the Claude project “Demo L09” (title and right panel) with callouts: description, Instructions, Context, Memory.'),
    's_instructions': ('Скриншот пяти строк инструкций проекта с выносками: роль, формат, запреты и источник.',
                'Screenshot of the five instruction lines with callouts and English translations: role, format, limits and source.'),
    's_chatgpt_plugin': ('Скриншот ChatGPT «@Plugin Creator, помоги мне создать плагин» с выносками.',
                'Screenshot of ChatGPT “@Plugin Creator, help me create a plugin” with callouts.'),
    's_compare': ('Четыре продукта: Claude, ChatGPT, Gemini, Copilot — название функции и доступность.',
                'Four products: Claude, ChatGPT, Gemini, Copilot — feature name and availability.'),
    's_test': ('Четыре типа тестовых вопросов и предупреждение про файлы знаний.',
                'Four kinds of test questions and a warning about knowledge files.'),
    's_ladder': ('Лестница (HTML): проект/плагин → Responses API → Agents SDK → Agents API, и четыре пояснения.',
                'Ladder (HTML): project/plugin → Responses API → Agents SDK → Agents API, with four side notes.'),
    's_responses': ('Справочный код Responses API с instructions и previous_response_id.',
                'Reference Responses API code with instructions and previous_response_id.'),
    's_sdk': ('Справочный код Agents SDK: три агента, handoff_description и handoffs.',
                'Reference Agents SDK code: three agents, handoff_description and handoffs.'),
    's_cost': ('Столбцы: 1000 вопросов $0,20, с веб-поиском $10,20, подписка $20.',
                'Bars: 1,000 questions $0.20, with web search $10.20, subscription $20.'),
    's_break': ('Таймер перерыва 5 минут.',
                '5-minute break timer.'),
    's_practice': ('Пять шагов практики списком и пример инструкции HR-ассистента.',
                'Five hands-on steps and an HR assistant instruction example.'),
    's_safety': ('Четыре вопроса перед публикацией ассистента и предупреждение: в рабочих планах администратор может видеть чаты.',
                'Four questions before sharing an assistant and a warning: on work plans an admin may see chats.'),
    's_hw': ('Пять шагов ДЗ и структура папки genai-homeworks/L13/.',
                'Five homework steps and the genai-homeworks/L13/ folder layout.'),
    's_summary': ('Четыре вывода и анонс L14.',
                'Four takeaways and the L14 preview.'),
}

HEAD = {
    "ru": '# Сценарий преподавателя • Урок 13: Свой ИИ-ассистент — проекты, плагины, Responses API, Agents SDK (90 минут)\n\n**Курс:** GenAI Basics • Модуль 5 (агенты, инструменты и MCP) • Урок 13 из 16\n**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Аудитория:** новички в GenAI из разных ролей. Простой язык; код только как справочный пример (слайды 10–11).\n**Формат:** 17 слайдов (`presentation_L13_Custom_Assistants_and_Agents_SDK_v2.html` / PDF) • **Microsoft Teams** • перерыв на слайде 13 • практика 10 минут на слайде 14\n**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.\n**Источник правды:** `deck_v2/build.py`; сценарий сгенерирован из него (`deck_v2/make_docs.py`).\n**Факты:** на 16.10.2026, источники в `L13_08_Source_Notes_Research_2026-10.md`.\n\n> **Важно:** урок был про Custom GPTs, но OpenAI отключает GPTs 11 декабря 2026 (перенос в плагины), а Gems в Gemini становятся навыками (личные аккаунты — с 17 ноября 2026, Workspace — с марта 2027). Урок учит общий принцип «инструкции + знания + инструменты + модель». Перед занятием проверьте, не изменились ли пути в ChatGPT (Плагины → Добавить → Создать плагин; проверено на Business, на Free/Plus этого пути может не быть — тогда Claude) и в Claude (Projects).\n\n**Цель урока:** студенты собирают своего ассистента без кода в Claude или ChatGPT, пишут короткие и проверяемые инструкции, тестируют ассистента четырьмя типами вопросов, понимают риски публикации и знают, как то же самое делается в коде (Responses API, Agents SDK).\n',
    "en": '# Instructor Script • Lesson 13: Your Own AI Assistant — Projects, Plugins, Responses API, Agents SDK (90 Minutes)\n\n**Course:** GenAI Basics • Module 5 (Agents, Tools and MCP) • Lesson 13 of 16\n**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Audience:** GenAI beginners from many roles. Plain language; code only as reference (slides 10–11).\n**Format:** 17 slides (`presentation_L13_Custom_Assistants_and_Agents_SDK_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 13 • 10-minute hands-on on slide 14\n**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.\n**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).\n**Facts:** as of 16.10.2026, sources in `L13_08_Source_Notes_Research_2026-10.md`.\n\n> **Important:** the lesson used to be about Custom GPTs, but OpenAI retires GPTs on 11 December 2026 (moving them to plugins), and Gemini Gems become skills (personal accounts from 17 November 2026, Workspace from March 2027). The lesson teaches the general principle “instructions + knowledge + tools + model”. Before class check the paths in ChatGPT (Plugins → Add → Create plugin; checked on Business, may be missing on Free/Plus — then use Claude) and Claude (Projects).\n\n**Lesson objective:** students build their own assistant without code in Claude or ChatGPT, write short, testable instructions, test the assistant with four kinds of questions, understand the risks of sharing, and know how the same is done in code (Responses API, Agents SDK).\n',
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
        # Part/break times computed from the slide minutes, so they cannot drift from the deck
        names = [f.__name__ for f in build.SLIDES]
        mins = [f()["min"] for f in build.SLIDES]
        b = names.index("s_break")
        t0, t1, n = sum(mins[:b]), sum(mins[:b + 1]), len(names)
        parts = t(f'Часть 1 (слайды 01–{b:02d}, {mmss(0)}–{mmss(t0)}): зачем свой ассистент, GPTs уходят, Claude-проекты, инструкции, плагины ChatGPT, сравнение, тесты, лестница, Responses API, Agents SDK, цена. '
                  f'Перерыв (слайд {b + 1:02d}, {mmss(t0)}–{mmss(t1)}). Часть 2 (слайды {b + 2:02d}–{n:02d}, {mmss(t1)}–{mmss(sum(mins))}): практика, безопасность, ДЗ, итоги.',
                  f'Part 1 (slides 01–{b:02d}, {mmss(0)}–{mmss(t0)}): why your own assistant, GPTs retire, Claude projects, instructions, ChatGPT plugins, comparison, tests, the ladder, Responses API, Agents SDK, price. '
                  f'Break (slide {b + 1:02d}, {mmss(t0)}–{mmss(t1)}). Part 2 (slides {b + 2:02d}–{n:02d}, {mmss(t1)}–{mmss(sum(mins))}): hands-on, security, homework, summary.')
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
