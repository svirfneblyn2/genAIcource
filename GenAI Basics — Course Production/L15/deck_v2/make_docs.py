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

L15 = build.L15
OUT = {"ru": L15 / "L15_02_Instructor_Script_90MIN.md", "en": L15 / "L15_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    's_cover': ('Название урока и миниатюра карты рисков (четыре цветные точки).',
                'Lesson title and a miniature of the risk map (four coloured dots).'),
    's_hook': ('Карта рисков: как часто × ущерб, четыре риска; рядом — когда и сколько стоит каждый.',
                'Risk map: how often × damage, four risks; beside it, when each happens and what it costs.'),
    's_halluc': ('Три числа: 45% (EBU/BBC), 2 190 решений, штраф $5 000.',
                'Three numbers: 45% (EBU/BBC), 2,190 decisions, a $5,000 fine.'),
    's_leak': ('Светофор данных; случаи Samsung и Grok.',
                'The data traffic light; the Samsung and Grok cases.'),
    's_plans': ('Личные и рабочие тарифы (три строки): кто учится на данных по умолчанию.',
                'Personal vs business plans: who trains on data by default.'),
    's_deepfake': ('Arup $25 млн и вертикальный стоп-список из четырёх шагов: звонок, срочно и тайно, стоп, перезвоните сами.',
                'Arup $25M and a vertical four-step stop list: the call, urgent and secret, stop, call back yourself.'),
    's_agents': ('PocketOS (9 секунд) и Replit; цепочка инцидента; правила для агентов.',
                'PocketOS (9 seconds) and Replit; rules for agents.'),
    's_owasp': ('Четыре риска OWASP Top 10 для LLM: LLM01, LLM02, LLM06, LLM09.',
                'Four OWASP LLM Top 10 risks: LLM01, LLM02, LLM06, LLM09.'),
    's_bias': ('Столбцы исследования резюме: 85% / 9% / 52% / 11%.',
                'CV study bars: 85% / 9% / 52% / 11%.'),
    's_labels': ('SynthID, C2PA, «нет метки ≠ человек»; где маркировка уже обязательна (Россия — спорно).',
                'SynthID, C2PA, “no mark ≠ human”; where labelling is already required (Russia — disputed).'),
    's_euact': ('Шкала времени EU AI Act и штрафы.',
                'EU AI Act timeline and fines.'),
    's_region': ('Узбекистан, Казахстан, Россия, США/Великобритания — по одной строке.',
                'Uzbekistan, Kazakhstan, Russia, US/UK — one line each.'),
    's_break': ('Таймер перерыва 5 минут.',
                '5-minute break timer.'),
    's_rules': ('Четыре пункта правил ИИ для команды.',
                'Four points of team AI rules.'),
    's_exercise': ('Четыре рабочие ситуации и крупный ключ ответов: да / да, но… / нет.',
                'Four work situations and a large answer key: yes / yes, but… / no.'),
    's_hw': ('Пять шагов ДЗ: правила ИИ для команды.',
                'Five homework steps: team AI rules.'),
    's_summary': ('Четыре правила (те же цвета, что на слайде 14) и анонс L16.',
                'Four rules and the L16 preview.'),
}

HEAD = {
    "ru": '# Сценарий преподавателя • Урок 15: Ответственный ИИ — ошибки, утечки, дипфейки и законы (90 минут)\n\n**Курс:** GenAI Basics • Модуль 6 (от идеи к продукту) • Урок 15 из 16\n**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Аудитория:** новички в GenAI из разных ролей и стран (Узбекистан, СНГ, ЕС). Спокойный, фактический тон; это обзор, а не юридическая консультация.\n**Формат:** 17 слайдов (`presentation_L15_Responsible_AI_Security_Regulation_v2.html` / PDF) • **Microsoft Teams** • перерыв на слайде 13\n**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.\n**Источник правды:** `deck_v2/build.py`; сценарий сгенерирован из него (`deck_v2/make_docs.py`).\n**Факты:** на 16.10.2026, источники и статус проверки (подтверждено / по вторичным источникам) в `L15_08_Source_Notes_Research_2026-10.md`.\n\n> **Перед уроком:** перепроверьте даты законов (EU AI Act, Узбекистан, Казахстан, Россия) и свежие случаи. Если студенты спрашивают о конкретной ситуации своей компании — отправляйте к юристам и службе безопасности.\n\n**Цель урока:** студенты знают четыре главных риска ИИ на работе на реальных примерах, умеют классифицировать данные по светофору, отличают личные и рабочие тарифы, знают, как защититься от дипфейк-мошенничества и ограничить агентов, понимают требования маркировки и основные законы (ЕС, Узбекистан, Казахстан, Россия) и составляют правила ИИ для своей команды.\n',
    "en": '# Instructor Script • Lesson 15: Responsible AI — Errors, Leaks, Deepfakes and Laws (90 Minutes)\n\n**Course:** GenAI Basics • Module 6 (Idea to Product) • Lesson 15 of 16\n**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems\n**Audience:** GenAI beginners from many roles and countries (Uzbekistan, CIS, EU). A calm, factual tone; an overview, not legal advice.\n**Format:** 17 slides (`presentation_L15_Responsible_AI_Security_Regulation_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 13\n**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.\n**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).\n**Facts:** as of 16.10.2026, sources and verification status (verified / secondary) in `L15_08_Source_Notes_Research_2026-10.md`.\n\n> **Before class:** recheck the law dates (EU AI Act, Uzbekistan, Kazakhstan, Russia) and recent cases. If students ask about their own company’s situation, refer them to their lawyers and security team.\n\n**Lesson objective:** students know the four main AI risks at work from real cases, can classify data with the traffic light, tell personal and business plans apart, know how to guard against deepfake fraud and limit agents, understand labelling requirements and the main laws (EU, Uzbekistan, Kazakhstan, Russia), and draft AI rules for their own team.\n',
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
        # Parts line computed from SLIDES minutes, so it can never drift from the deck.
        names = [f.__name__ for f in build.SLIDES]
        mins = [f()["min"] for f in build.SLIDES]
        bi = names.index("s_break")
        n = len(names)
        p1, br = sum(mins[:bi]), sum(mins[:bi + 1])
        parts = t(f'Часть 1 (слайды 01–{bi:02d}, 00:00–{mmss(p1)}): карта рисков, выдумки, утечки, тарифы, дипфейки, агенты, OWASP, предвзятость, маркировка, EU AI Act, наш регион. '
                  f'Перерыв (слайд {bi + 1:02d}, {mmss(p1)}–{mmss(br)}). Часть 2 (слайды {bi + 2:02d}–{n:02d}, {mmss(br)}–{mmss(start)}): правила команды, упражнение, ДЗ, итоги.',
                  f'Part 1 (slides 01–{bi:02d}, 00:00–{mmss(p1)}): the risk map, made-up facts, leaks, plans, deepfakes, agents, OWASP, bias, labelling, the EU AI Act, our region. '
                  f'Break (slide {bi + 1:02d}, {mmss(p1)}–{mmss(br)}). Part 2 (slides {bi + 2:02d}–{n:02d}, {mmss(br)}–{mmss(start)}): team rules, exercise, homework, summary.')
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
