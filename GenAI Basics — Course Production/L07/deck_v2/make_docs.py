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

L06 = build.L06
OUT = {"ru": L06 / "L06_02_Instructor_Script_90MIN.md", "en": L06 / "L06_02_Instructor_Script_90MIN_EN.md"}

SCREEN = {
    "s_cover": ("Фон: кадр из шота 2 L05 (курьер под дождём). Заголовок, подзаголовок, состав урока, подсказки по клавишам.",
                "Background: a frame from L05 shot 2 (the courier in the rain). Title, subtitle, lesson scope, key hints."),
    "s_hook": ("Слева озвученный ролик курьера (23 с, со звуком, запуск кликом). Справа три числа: 3 реплики, 3 дорожки, итоговая громкость в LUFS.",
               "Left: the voiced courier video (23 s, with sound, click to play). Right: three numbers: 3 lines, 3 tracks, final loudness in LUFS."),
    "s_layers": ("Три колонки: чат-приложения, веб-студии, API (инструменты, управление, оплата, для чего, с чего начать). Внизу: четвёртый путь, открытые модели.",
                 "Three columns: chat apps, web studios, API (tools, control, billing, use, starting point). Below: the fourth path, open-weight models."),
    "s_tasks": ("Четыре карточки «вход → выход»: синтез речи, распознавание речи, речь в речь, музыка и шумы. Внизу: озвучка использует три из четырёх.",
                "Four input → output cards: text-to-speech, speech-to-text, speech-to-speech, music and sound effects. Below: voicing a video uses three of the four."),
    "s_how": ("Цепочка «текст → модель → аудиотокены → декодер → звук»; реальная форма волны реплики 1; две заметки: объём данных и почему ошибаются числа и имена.",
              "Chain text → model → audio tokens → decoder → waveform; the real waveform of line 1; two notes: data volume and why numbers and names fail."),
    "s_video_audio": ("Два плеера со звуком Veo (шот 1 и неудачный клип L05) и распознанный в них текст. Внизу: что звук видеомодели даёт и чего не даёт.",
                      "Two players with Veo audio (shot 1 and the L05 failure clip) and the text recognised in them. Below: what video-model audio gives and does not give."),
    "s_script": ("Таблица сценария: кадр, время, реплика, слов / длина, шумы. Внизу: измеренный темп речи и правило бюджета слов.",
                 "Script table: frame, time, line, words / length, sound effects. Below: measured speech rate and the word budget rule."),
    "s_text": ("Таблица «сценарий → текст для голоса → почему» для 6:42, 417, 12 мин. Справа пример инструкции стиля и три способа управлять голосом.",
               "Table script → spoken text → why for 6:42, 417, 12 min. Right: a style instruction example and three ways to control the voice."),
    "s_voice": ("Три карточки: готовый голос, голос по описанию, клон; у каждой условие использования. Внизу: проверить сложные слова до выбора голоса.",
                "Three cards: library voice, designed voice, clone, each with its usage condition. Below: test the hard words before choosing a voice."),
    "s_music": ("Плеер музыкальной подложки MusicGen, её промпт и лицензия. Справа таблица: Suno v6, Lyria 3.5, ElevenLabs Music и SFX (длина, коммерческое использование).",
                "Player with the MusicGen bed, its prompt and licence. Right: table of Suno v6, Lyria 3.5, ElevenLabs Music and SFX (length, commercial use)."),
    "s_mix": ("Четыре реальные дорожки (голос, звук Veo, музыка, итог) с громкостью; три правила (приглушение, громкость, пик) и команда ffmpeg.",
              "Four real tracks (voice, Veo audio, music, mix) with loudness; three rules (ducking, loudness, peak) and the ffmpeg command."),
    "s_check": ("Сценарий и то, что услышал Whisper, с подсветкой ошибок; разбор двух ошибок. Справа частота ошибок в словах и число верных критичных слов.",
                "The script and what Whisper heard, with errors highlighted; two errors explained. Right: word error rate and the number of correct critical terms."),
    "s_arch": ("Три дорожки-архитектуры: файл, поток, речь в речь, с задержкой. Внизу: два способа построить голосового агента.",
               "Three architecture lanes: file, stream, speech-to-speech, with latency. Below: two ways to build a voice agent."),
    "s_market": ("Четыре строки задач с моделями; открытые модели в зелёной рамке с лицензией. Внизу: точность распознавания и сроки жизни моделей.",
                 "Four task rows with models; open-weight models in a green border with the licence. Below: transcription accuracy and model lifetimes."),
    "s_break": ("Таймер 5 минут, кнопки «Старт» и «Сброс».", "5-minute timer, Start and Reset buttons."),
    "s_code": ("Код синтеза речи через google-genai (Gemini API) и три строки проверки через faster-whisper.",
               "Text-to-speech code with google-genai (Gemini API) and three lines of checking with faster-whisper."),
    "s_econ": ("Таблица цен: секунда, минута, час для синтеза, распознавания, речи в речь, музыки. Справа: стоимость озвучки нашего ролика и сравнение с видео.",
               "Price table: second, minute, hour for synthesis, transcription, speech-to-speech, music. Right: the cost of voicing our video and a comparison with video."),
    "s_qa": ("Чек-лист из 6 пунктов с реальным результатом нашей версии (✓ / ✗ / !), громкость, причина отказа. Это рубрика ДЗ.",
             "6-item checklist with the real result of our version (✓ / ✗ / !), loudness, the reason for rejection. This is the homework rubric."),
    "s_risks": ("Светофор голосов; как сервисы проверяют согласие на клон; плашка EU AI Act ст. 50, OpenAI, SynthID.",
                "Voice traffic light; how services check consent for a clone; EU AI Act Art. 50, OpenAI, SynthID plaque."),
    "s_hw": ("Карточка «ваш ролик из L05», структура папки genai-homeworks/L06, пять шагов задания, ревьюер и правило согласия.",
             "“Your L05 video” card, the genai-homeworks/L06 folder tree, five homework steps, reviewer and the consent rule."),
    "s_summary": ("Пять правил урока и кадр из ролика; анонс L07.", "Five lesson rules and a frame from the video; L07 preview."),
}

HEAD = {
    "ru": """# Сценарий преподавателя • Урок 06: Речь и аудио. Озвучка, звук и музыка для ролика (90 минут)

**Курс:** GenAI Basics • Модуль 2 (мультимодальность) • Урок 06 из 16
**Преподаватель:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Аудитория:** новички в GenAI из разных ролей. Простой язык, без формул; код только как один справочный пример.
**Формат:** 21 слайд (`presentation_L06_Speech_and_Audio_v2.html` / PDF) • занятие в **Microsoft Teams** • таймер перерыва на слайде 15
**Управление:** `←/→` листать, `N` заметки спикера, `G` все слайды, `F` полный экран. Видео и аудио запускаются **кликом** и играют **со звуком**.
**Источник правды:** `deck_v2/build.py` (текст слайдов и заметки). Этот сценарий сгенерирован из него (`deck_v2/make_docs.py`); если что-то расходится, прав `build.py`.
**Материалы:** озвученный ролик и дорожки из `assets/v2/` (сделаны `deck_v2/make_audio.py` из ролика L05), отчёт с измерениями `demo_courier_audio/report.json`, ДЗ `L06_05_Homework.md`.
**Факты:** на октябрь 2026, источники в `L06_08_Source_Notes_Research_2026-10.md`. Список «перепроверить за сутки» в конце шпаргалки.

> **Перед стартом (Teams):** в этом уроке звук обязателен. При демонстрации экрана в окне «Поделиться» включите **«Включить звук» (Include sound)**; в старых версиях Teams переключатель называется Include computer sound. Проверьте звук на одном клипе до начала.

**Цель урока:** студенты понимают четыре задачи аудио-ИИ (синтез речи, распознавание речи, речь в речь, музыка и шумы), знают, где их делать (чат, веб-студия, API, открытые модели), умеют озвучить ролик по пайплайну из 6 шагов (сценарий, текст для голоса, голос, шумы и музыка, сведение, проверка), считают стоимость секунды, минуты и часа аудио, принимают результат по чек-листу и соблюдают правила согласия на голос.
""",
    "en": """# Instructor Script • Lesson 06: Speech and Audio AI. Voice-over, Sound and Music for a Video (90 Minutes)

**Course:** GenAI Basics • Module 2 (Multimodality) • Lesson 06 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language, no formulas; code only as one short reference example.
**Format:** 21 slides (`presentation_L06_Speech_and_Audio_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen. Videos and audio start **on click** and play **with sound**.
**Source of truth:** `deck_v2/build.py` (slide text and speaker notes). This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.
**Materials:** the voiced video and tracks in `assets/v2/` (made by `deck_v2/make_audio.py` from the L05 video), the measurement report `demo_courier_audio/report.json`, homework `L06_05_Homework_EN.md`.
**Facts:** as of October 2026, sources in `L06_08_Source_Notes_Research_2026-10.md`. The “recheck within 24 hours” list is at the end of the cheatsheet.

> **Before you start (Teams):** this lesson needs sound. When sharing your screen, turn on **“Include sound”** in the Share window (older Teams versions: “Include computer sound”). Test the sound on one clip before class.

**Lesson objective:** students understand the four audio AI tasks (text-to-speech, speech-to-text, speech-to-speech, music and sound effects), know where to run them (chat, web studio, API, open-weight models), can voice a video with a 6-step pipeline (script, text for the voice, voice, sound effects and music, mix, check), can estimate the cost of a second, a minute and an hour of audio, accept the result with a checklist and follow the voice consent rules.
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
        parts = t("Часть 1 (слайды 01–14, 00:00–58:00): задачи, модели и пайплайн из 6 шагов. Перерыв (слайд 15, 58:00–63:00). Часть 2 (слайды 16–21, 63:00–90:00): код, стоимость, приёмка, риски, ДЗ, итоги.",
                  "Part 1 (slides 01–14, 00:00–58:00): tasks, models and the 6-step pipeline. Break (slide 15, 58:00–63:00). Part 2 (slides 16–21, 63:00–90:00): code, cost, acceptance, risks, homework, summary.")
        OUT[lang].write_text(HEAD[lang] + "\n---\n\n" + table + "\n" + parts + "\n\n---\n\n" + "\n".join(body), encoding="utf-8")
        print(OUT[lang].name, start, "min")


if __name__ == "__main__":
    main()
