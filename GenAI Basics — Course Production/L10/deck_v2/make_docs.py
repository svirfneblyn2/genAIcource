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

L10 = build.L10
OUT = {"ru": L10 / "L10_02_Instructor_Script_90MIN.md", "en": L10 / "L10_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    "s_cover": ("Название урока, подзаголовок, состав; справа три карточки: облачный API, ваш ноутбук, арендованная видеокарта с их адресами.",
                "Lesson title, subtitle, scope; on the right three cards: cloud API, your laptop, rented GPU with their addresses."),
    "s_hook": ("Схема: ваше приложение отправляет запрос по трём адресам — облачный API, ноутбук (localhost:1234), арендованная видеокарта. Справа легенда 1–3; внизу «меняются только адрес и имя модели».",
               "Schematic: your app sends a request to three addresses — cloud API, laptop (localhost:1234), rented GPU. Legend 1–3 on the right; below, “only the address and model name change”."),
    "s_open": ("Скриншоты Hugging Face: страница granite-4.2-8b-GGUF (автор, лицензия Apache-2.0) и список файлов от Q4_K_M до Q8_0, выноски 1–3.",
               "Hugging Face screenshots: the granite-4.2-8b-GGUF page (publisher, Apache-2.0 licence) and the file list from Q4_K_M to Q8_0, callouts 1–3."),
    "s_why": ("Слева плюсы, минусы и подходящие задачи; справа столбцы индекса Artificial Analysis: 58 / 46 / 34.",
              "Left: pros, cons and good tasks; right: Artificial Analysis index bars: 58 / 46 / 34."),
    "s_layers": ("Схема из пяти частей с иконками: файл модели → движок llama.cpp → железо → сервер localhost:1234 → приложение; над первыми четырьмя скобка «LM Studio или Ollama делают это за вас».",
                 "Five-part schematic with icons: model file → llama.cpp engine → hardware → localhost:1234 server → app; over the first four a bracket “LM Studio or Ollama does this for you”."),
    "s_quant": ("Столбцы размеров файлов Granite 4.2 8B от Q2_K (3,4 ГБ) до BF16 (17,6 ГБ); справа «Q4» и аналогия с JPEG.",
                "Bars of Granite 4.2 8B file sizes from Q2_K (3.4 GB) to BF16 (17.6 GB); on the right “Q4” and the JPEG analogy."),
    "s_fit": ("Столбцы Q4 семи моделей со штриховкой +25% и линии памяти 6 / 16 / 24 ГБ; цвет столбца — наименьшая видеокарта, куда модель влезает; справа «+25%».",
              "Q4 bars of seven models with a hatched +25%, memory lines at 6 / 16 / 24 GB; bar colour = the smallest GPU it fits; on the right “+25%”."),
    "s_speed": ("Столбцы скорости в токенах в секунду: процессор ноутбука, Apple M5, RTX 4050 Laptop, M5 Max, RTX 4090, H100; справа «≥ 20 т/с».",
                "Speed bars in tokens per second: laptop CPU, Apple M5, RTX 4050 Laptop, M5 Max, RTX 4090, H100; on the right “≥ 20 t/s”."),
    "s_lmstudio": ("Официальный скриншот LM Studio (два чата) с выносками; легенда Chat / Discover / выбор модели / Developer.",
                   "Official LM Studio screenshot (two chats) with callouts; legend Chat / Discover / model picker / Developer."),
    "s_demo": ("Пять шагов демо на линии (найти, скачать, загрузить, спросить, посмотреть скорость), промпт с тикетом, образец хорошего ответа в JSON и что замечаем.",
               "Five demo steps on a line (find, download, load, ask, check speed), the ticket prompt, a sample good JSON answer and what to notice."),
    "s_server": ("Код на Python из L03 с выделенными адресом и именем модели; справа три варианта настроек: OpenAI, LM Studio, Ollama.",
                 "The L03 Python code with the address and model name highlighted; on the right three settings: OpenAI, LM Studio, Ollama."),
    "s_agent": ("Промпт для агента разработки (установить Ollama, скачать модель, замерить скорость, только localhost) и три заметки.",
                "Prompt for a coding agent (install Ollama, download a model, measure speed, localhost only) and three notes."),
    "s_private": ("«Светофор» пути данных из четырёх пунктов: модель считает локально, скачивание, плагины, сервер в сети; справа правило урока.",
                  "Four-point data-path traffic light: local compute, downloads, plug-ins, network-exposed server; on the right the class rule."),
    "s_market": ("Три списка моделей с лицензиями под цветными заголовками: видеокарта до 8 ГБ, 16–24 ГБ, сервер.",
                 "Three lists of models with licences under coloured headers: GPU up to 8 GB, 16–24 GB, server."),
    "s_break": ("Таймер перерыва 5 минут.", "5-minute break timer."),
    "s_limits": ("Четыре признака, что ноутбука мало, и решение: та же модель на облачной видеокарте.",
                 "Four signs a laptop is not enough, and the fix: the same model on a cloud GPU."),
    "s_runpod": ("Скриншот цен Runpod Community (выделена RTX 4090 $0.34/ч) и полоса дня: Pod против Serverless; ловушка Stop.",
                 "Runpod Community pricing (RTX 4090 $0.34/h highlighted) and a day timeline: Pod vs Serverless; the Stop trap."),
    "s_cost": ("Столбцы цены за час пяти видеокарт (A100 и H100 — SXM); справа ≈ $0.73 → $7.30 за 1 млн токенов при загрузке 100% и 10% против $0.40–4.50 у облачных моделей.",
               "Hourly price bars for five GPUs (A100 and H100 are SXM); on the right ≈ $0.73 → $7.30 per 1M tokens at 100% vs 10% load versus $0.40–4.50 for cloud models."),
    "s_decide": ("Сетка 2×2 (данные можно отдать / должны остаться × мало / много запросов): облачный API ×2, свой ноутбук, Runpod (Pod или Serverless); заметка про Secure Cloud.",
                 "2×2 grid (data may leave / must stay × few / many requests): cloud API ×2, your laptop, Runpod (Pod or Serverless); a note on Secure Cloud."),
    "s_hw": ("Пять шагов ДЗ, структура папки сдачи genai-homeworks/L10/, подсказка для слабого компьютера.",
             "Five homework steps, the genai-homeworks/L10/ submission folder, a tip for weak computers."),
    "s_summary": ("Четыре правила урока и анонс L11.", "Four lesson rules and the L11 preview."),
}

HEAD = {
    "ru": """# Сценарий преподавателя • Урок 10: Открытые модели. Свой ноутбук и арендованная видеокарта (90 минут)

**Курс:** GenAI Basics • Модуль 4 (открытые модели) • Урок 10 из 16
**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Аудитория:** новички в GenAI из разных ролей. Простой язык; код только как один справочный пример (слайд 11).
**Формат:** 21 слайд (`presentation_L10_Open_Models_Local_and_RunPod_v2.html` / PDF) • занятие в **Microsoft Teams** • таймер перерыва на слайде 15
**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран.
**Источник правды:** `deck_v2/build.py` (текст слайдов и заметки). Этот сценарий сгенерирован из него (`deck_v2/make_docs.py`); если что-то расходится, прав `build.py`.
**Факты:** на 16.10.2026, источники в `L10_08_Source_Notes_Research_2026-10.md`. Список «перепроверить за сутки» в конце шпаргалки.

> **Перед уроком:** поставьте LM Studio (обычную, не Bionic) и заранее скачайте `granite-4.2-3b` в Q4_K_M (2,2 ГБ) для демо на слайде 10. Runpod показываем на скриншотах; живой запуск платный и по желанию.

**Цель урока:** студенты понимают, что такое открытая модель (файл + лицензия), умеют оценить, влезет ли модель в их компьютер и с какой скоростью будет работать, запускают модель в LM Studio или Ollama и подключают её к коду через локальный сервер, понимают, когда нужна арендованная видеокарта (Runpod Pod или Serverless), сколько это стоит и как выбрать между облачным API, ноутбуком и арендой.
""",
    "en": """# Instructor Script • Lesson 10: Open Models. Your Laptop and a Rented GPU (90 Minutes)

**Course:** GenAI Basics • Module 4 (Open Models) • Lesson 10 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language; code only as one short reference example (slide 11).
**Format:** 21 slides (`presentation_L10_Open_Models_Local_and_RunPod_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py` (slide text and speaker notes). This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.
**Facts:** as of 16.10.2026, sources in `L10_08_Source_Notes_Research_2026-10.md`. The “recheck within 24 hours” list is at the end of the cheatsheet.

> **Before class:** install LM Studio (the classic app, not Bionic) and download `granite-4.2-3b` at Q4_K_M (2.2 GB) in advance for the slide 10 demo. Runpod is shown on screenshots; a live launch is paid and optional.

**Lesson objective:** students understand what an open model is (a file plus a licence), can estimate whether a model fits their computer and how fast it will run, run a model in LM Studio or Ollama and connect it to code through a local server, and understand when a rented GPU is needed (Runpod Pod or Serverless), what it costs and how to choose between a cloud API, a laptop and renting.
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
        mins = [fn()["min"] for fn in build.SLIDES]
        bi = build.SLIDES.index(build.s_break)  # 0-based index of the break slide
        p1, br = sum(mins[:bi]), mins[bi]
        n = len(mins)
        parts = t(f"Часть 1 (слайды 01–{bi:02d}, 00:00–{mmss(p1)}): открытые модели, память и скорость, LM Studio, локальный сервер, агент, безопасность, рынок. "
                  f"Перерыв (слайд {bi + 1}, {mmss(p1)}–{mmss(p1 + br)}). Часть 2 (слайды {bi + 2}–{n}, {mmss(p1 + br)}–{mmss(sum(mins))}): предел ноутбука, Runpod, цена, выбор, ДЗ, итоги.",
                  f"Part 1 (slides 01–{bi:02d}, 00:00–{mmss(p1)}): open models, memory and speed, LM Studio, the local server, an agent, security, market. "
                  f"Break (slide {bi + 1}, {mmss(p1)}–{mmss(p1 + br)}). Part 2 (slides {bi + 2}–{n}, {mmss(p1 + br)}–{mmss(sum(mins))}): laptop limits, Runpod, price, choosing, homework, summary.")
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
