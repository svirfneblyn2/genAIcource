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

L12 = build.L12
OUT = {"ru": L12 / "L12_02_Instructor_Script_90MIN.md", "en": L12 / "L12_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    's_cover': ('Название урока; справа фрагмент схемы «MCP — один разъём».',
                'Lesson title; on the right part of the “MCP — one plug” schematic.'),
    's_hook': ('Схема «без MCP 3 × 3 = 9 связок, с MCP 3 + 3 = 6».',
                'Schematic “without MCP 3 × 3 = 9 links, with MCP 3 + 3 = 6”.'),
    's_hub': ('Схема-хаб: приложения слева, MCP в центре, серверы справа; определение MCP.',
                'Hub schematic: apps on the left, MCP in the centre, servers on the right; the MCP definition.'),
    's_roles': ('Три карточки хост → клиент → сервер и три вида того, что даёт сервер.',
                'Three cards host → client → server and the three things a server offers.'),
    's_connectors': ('Скриншот меню коннекторов Claude с выносками 1–3.',
                'Screenshot of Claude’s connectors menu with callouts 1–3.'),
    's_permission': ('Скриншот запроса разрешения Claude для инструмента Figma с выносками 1–3.',
                'Screenshot of Claude’s permission prompt for the Figma tool with callouts 1–3.'),
    's_hosts': ('Где подключать серверы: Claude, ChatGPT, агенты разработки, LM Studio.',
                'Where to connect servers: Claude, ChatGPT, coding agents, LM Studio.'),
    's_registry': ('Скриншот официального реестра MCP и число ≈ 44 000.',
                'Screenshot of the official MCP registry and the ≈ 44,000 count.'),
    's_code': ('Справочный код мини-сервера MCP на Python (MCPServer, @mcp.tool()).',
                'Reference Python code for a mini MCP server (MCPServer, @mcp.tool()).'),
    's_connect': ('Файл настроек mcpServers и три понятия: локальный, удалённый сервер, MCP Inspector.',
                'The mcpServers settings file and three ideas: local server, remote server, MCP Inspector.'),
    's_agentbuild': ('Промпт для агента разработки: MCP-сервер курьерской службы.',
                'Coding-agent prompt: a courier-service MCP server.'),
    's_security': ('Четыре риска MCP и плашка с правилами.',
                'Four MCP risks and a rules panel.'),
    's_layers': ('Три слоя: вызов функций, MCP, фреймворк агентов.',
                'Three layers: function calling, MCP, agent framework.'),
    's_adoption': ('Три числа: загрузки SDK, число серверов, передача в Linux Foundation.',
                'Three numbers: SDK downloads, server count, the Linux Foundation donation.'),
    's_break': ('Таймер перерыва 5 минут.',
                '5-minute break timer.'),
    's_frameworks': ('Список фреймворков агентов с версиями, лицензиями и назначением.',
                'Agent frameworks with versions, licences and purpose.'),
    's_when': ('Лестница сложности: функции → MCP → фреймворк → A2A.',
                'Complexity ladder: functions → MCP → framework → A2A.'),
    's_a2a': ('Сравнение MCP и A2A.',
                'MCP vs A2A.'),
    's_exercise': ('Четыре рабочие задачи: какие серверы, права, подтверждения.',
                'Four work tasks: which servers, permissions, confirmations.'),
    's_hw': ('Пять шагов ДЗ и структура папки сдачи.',
                'Five homework steps and the submission folder layout.'),
    's_summary': ('Четыре вывода и анонс L13.',
                'Four takeaways and the L13 preview.'),
}

HEAD = {
    "ru": '# Сценарий преподавателя • Урок 12: MCP и фреймворки агентов (90 минут)\n\n**Курс:** GenAI Basics • Модуль 3 (свои модели и агенты) • Урок 12 из 16\n**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Аудитория:** новички в GenAI из разных ролей. Простой язык; код только как справочный пример (слайды 9–10).\n**Формат:** 21 слайд (`presentation_L12_MCP_and_Agent_Frameworks_v2.html` / PDF) • занятие в **Microsoft Teams** • таймер перерыва на слайде 15\n**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.\n**Источник правды:** `deck_v2/build.py`. Этот сценарий сгенерирован из него (`deck_v2/make_docs.py`); если что-то расходится, прав `build.py`.\n**Факты:** на 16.10.2026, источники в `L12_08_Source_Notes_Research_2026-10.md`.\n\n> **Перед уроком:** откройте claude.ai и проверьте меню коннекторов и запрос разрешения (подписи кнопок могли измениться). Код со слайда 9 справочный: перед показом поставьте `pip install mcp` (Python 3.11+) и проверьте сервер в MCP Inspector.\n\n**Цель урока:** студенты понимают, зачем нужен стандарт MCP, знают роли хоста, клиента и сервера и что сервер даёт (инструменты, ресурсы, промпты), умеют подключить коннектор и читать запрос разрешения, знают риски сторонних серверов и правила доступа, отличают вызов функций, MCP и фреймворк агентов и понимают, когда нужен фреймворк.\n',
    "en": '# Instructor Script • Lesson 12: MCP and Agent Frameworks (90 Minutes)\n\n**Course:** GenAI Basics • Module 3 (Own Models and Agents) • Lesson 12 of 16\n**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Audience:** GenAI beginners from many roles. Plain language; code only as reference (slides 9–10).\n**Format:** 21 slides (`presentation_L12_MCP_and_Agent_Frameworks_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15\n**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.\n**Source of truth:** `deck_v2/build.py`. This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.\n**Facts:** as of 16.10.2026, sources in `L12_08_Source_Notes_Research_2026-10.md`.\n\n> **Before class:** open claude.ai and check the connectors menu and the permission prompt (button labels may have changed). The slide 9 code is a reference: before showing it, `pip install mcp` (Python 3.11+) and test the server in MCP Inspector.\n\n**Lesson objective:** students understand why the MCP standard exists, know the host, client and server roles and what a server offers (tools, resources, prompts), can connect a connector and read a permission prompt, know the risks of third-party servers and the access rules, tell function calling, MCP and an agent framework apart, and know when a framework is needed.\n',
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
        parts = t('Часть 1 (слайды 01–14, 00:00–60:00): проблема, MCP, роли, коннекторы, разрешения, хосты, реестр, свой сервер, подключение, безопасность, слои, масштаб. Перерыв (слайд 15, 60:00–65:00). Часть 2 (слайды 16–21, 65:00–90:00): фреймворки, когда что, A2A, упражнение, ДЗ, итоги.',
                  'Part 1 (slides 01–14, 00:00–60:00): the problem, MCP, roles, connectors, permissions, hosts, registry, your own server, connecting, security, layers, scale. Break (slide 15, 60:00–65:00). Part 2 (slides 16–21, 65:00–90:00): frameworks, when to use what, A2A, exercise, homework, summary.')
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
