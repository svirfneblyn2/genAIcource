# -*- coding: utf-8 -*-
"""Build the L06 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. Audio and video come from ../assets/v2/ (see make_audio.py);
measured numbers (loudness, transcripts, word error rate) come from
../demo_courier_audio/report.json and waveforms from envelopes.json.
Facts: ../L06_08_Source_Notes_Research_2026-10.md. Graph: ../L06_10_Lesson_Graph.md.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L06 = HERE.parent
NAME = "presentation_L06_Speech_and_Audio"
OUT = {"ru": L06 / f"{NAME}_v2.html", "en": L06 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"
VID = "assets/v2/video/"
AUD = "assets/v2/audio/"
REPORT = json.loads((L06 / "demo_courier_audio" / "report.json").read_text(encoding="utf-8"))
ENV = json.loads((HERE / "envelopes.json").read_text(encoding="utf-8"))

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


def R():
    return REPORT["langs"][LANG]


FOOT = {"ru": "GenAI Basics • Урок 06 • Речь и аудио", "en": "GenAI Basics • Lesson 06 • Speech and Audio"}


# ---------------------------------------------------------------- helpers
def num(x, d=1):
    s = f"{x:.{d}f}"
    return s.replace(".", ",") if LANG == "ru" else s


def video(name, poster, extra=""):
    label = t("▶ видео со звуком в HTML-версии", "▶ video with sound in the HTML version")
    return (f'<div class="vid" {extra}><video src="{VID}{name}.mp4" poster="{IMG}{poster}.jpg" playsinline '
            f'preload="metadata" controls></video><img class="pp" src="{IMG}{poster}.jpg" alt="">'
            f'<span class="pl">{label}</span></div>')


def wave(env, h=56, w=900, color=None, gain=1.0, x0=0.0, x1=1.0):
    """Mirrored bar waveform from an RMS envelope (list of floats)."""
    a, b = int(len(env) * x0), int(len(env) * x1)
    e = env[a:b]
    peak = max(max(env), 1e-6)
    n = len(e)
    bw = w / n
    mid = h / 2
    parts = []
    for i, v in enumerate(e):
        y = max(0.8, min(mid - 1, (v / peak) * gain * (mid - 2)))
        parts.append(f"M{i * bw:.1f} {mid - y:.1f}h{max(bw * 0.7, 0.8):.1f}v{2 * y:.1f}h-{max(bw * 0.7, 0.8):.1f}Z")
    st = f' style="--k:{color}"' if color else ""
    return f'<svg class="wave" viewBox="0 0 {w} {h}" preserveAspectRatio="none"{st}><path d="{"".join(parts)}"/></svg>'


def aud(name, title, sub="", k="cyan", env=None):
    w = wave(ENV[env]) if env else ""
    return (f'<div class="aud" style="--k:var(--{k})"><div class="ah">{title}<small>{sub}</small></div>{w}'
            f'<audio src="{AUD}{name}.mp3" preload="metadata" controls></audio>'
            f'<div class="pl">{t("▶ звук в HTML-версии", "▶ audio in the HTML version")}</div></div>')


def head(kicker, title, lead=None, k=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    s = f'<div class="kicker"{ks}>{kicker}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


TEAMS = {
    "ru": "Teams: в этом уроке звук обязателен. При демонстрации экрана включите «Включить звук компьютера» (Include computer sound) и «Оптимизировать для движения и видео». Перед стартом проверьте звук на одном клипе.",
    "en": "Teams: this lesson needs sound. When sharing your screen, turn on “Include computer sound” and “Optimize for motion and video”. Test the sound on one clip before you start.",
}


def teams():
    return TEAMS[LANG]


def voice_words():
    lines = R()["lines"]
    words = sum(len(x["spoken"].split()) for x in lines)
    secs = sum(x["end"] - x["start"] for x in lines)
    chars = sum(len(x["spoken"]) for x in lines)
    return words, secs, chars


def diff_markup(ref, hyp, ok_terms):
    """Colour the transcript: words not in the script in red, correctly heard critical terms in green."""
    import difflib
    import re
    def key(w):
        return re.sub(r"[^\w:]", "", w.lower().replace("ё", "е"))
    hw = hyp.split()
    sm = difflib.SequenceMatcher(a=[key(w) for w in ref.split()], b=[key(w) for w in hw], autojunk=False)
    okw = {key(w) for term in ok_terms for w in term.split()}
    out = []
    for op, _, _, j1, j2 in sm.get_opcodes():
        for w in hw[j1:j2]:
            if op == "equal":
                out.append(f'<span class="ok">{w}</span>' if key(w) in okw else w)
            else:
                out.append(f'<span class="bad">{w}</span>')
    return " ".join(out)


# ---------------------------------------------------------------- slides
def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg"><img src="{IMG}cover_shot2.jpg" alt=""></div>
  <div class="shade"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 06 • Модуль 2: мультимодальность", "GenAI Basics • Lesson 06 • Module 2: multimodality")}</div>
    <h1>{t("Речь и аудио", "Speech and Audio AI")}</h1>
    <h2>{t("Озвучка, звук и музыка для ролика и проверка результата", "Voice-over, sound and music for a video, and how to check the result")}</h2>
    <p>{t("Синтез речи, распознавание речи, голосовые агенты, музыка. ElevenLabs, OpenAI, Google, Suno, открытые модели. Данные на октябрь 2026.",
           "Text-to-speech, speech-to-text, voice agents, music. ElevenLabs, OpenAI, Google, Suno, open-weight models. Data as of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. Третий урок модуля «мультимодальность»: в L04 делали картинки, в L05 из них видео, сегодня даём ролику голос, звук и музыку.",
                      "⏱ 2 min. Welcome. Third lesson of the multimodality module: in L04 we made images, in L05 we turned them into video, today we add voice, sound and music."),
                    t("План: готовый озвученный ролик, где генерировать, четыре задачи аудио-ИИ, как модель работает со звуком, что умеет звук внутри видеомоделей, затем пайплайн из 6 шагов, архитектуры распознавания речи и рынок. После перерыва: код, стоимость, приёмка, риски и согласие на голос, домашнее задание.",
                      "Plan: a finished voiced video, where to generate, four audio tasks, how a model handles sound, what audio inside video models can do, then a 6-step pipeline, speech recognition architectures and the market. After the break: code, cost, acceptance, risks and voice consent, homework."),
                    t("Перед стартом: " + TEAMS["ru"], "Before you start: " + TEAMS["en"])))


def s_hook():
    words, secs, _ = voice_words()
    mix = R()["mix"]
    return dict(min=3, html=f'''
  {head(t("Пример", "Example"), t("Ролик курьера из L05 с озвучкой, звуком и музыкой", "The L05 courier video with voice-over, sound and music"), k="amber")}
  <div class="body">
    <div class="row" style="grid-template-columns:1.75fr 1fr;gap:48px;align-items:center;">
      {video("courier_voiced_" + LANG, "poster_final")}
      <div class="stack" style="gap:30px;">
        <div class="stat" style="--k:var(--cyan)"><div class="n">3 {t("реплики", "lines")}</div><div class="d">{t(f"{num(secs)} с речи; голос из <b>открытой модели</b> синтеза речи на обычном ноутбуке", f"{num(secs)} s of speech from an <b>open-weight</b> text-to-speech model on a laptop CPU")}</div></div>
        <div class="stat" style="--k:var(--green)"><div class="n">3 {t("дорожки", "tracks")}</div><div class="d">{t("голос + звук, который Veo сгенерировал вместе с видео + музыка", "voice + the sound Veo generated with the video + music")}</div></div>
        <div class="stat" style="--k:var(--amber)"><div class="n">{num(mix["lufs"])} LUFS</div><div class="d">{t("громкость под стриминг: цель −14 LUFS (единицы громкости, Loudness Units relative to Full Scale)", "streaming loudness: target −14 LUFS (Loudness Units relative to Full Scale)")}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:24px;--k:var(--amber)">{t("Дальше: где генерировать, как модель работает со звуком, почему звук видеомодели не заменяет озвучку, и пайплайн из 6 шагов.", "Next: where to generate, how a model handles sound, why the video model’s audio does not replace a voice-over, and a 6-step pipeline.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Запустите ролик кликом, со звуком (23 секунды). Это тот же ролик из L05: три шота Veo 3.1. Спросите в чат: что вы слышите, сколько слоёв звука?",
                      "⏱ 3 min. Start the clip with a click, with sound (23 seconds). It is the same L05 video: three Veo 3.1 shots. Ask the chat: what do you hear, how many layers of sound?"),
                    t(f"Ответ: три слоя. Голос диктора: три реплики, {num(secs)} секунды речи, сделаны открытой моделью синтеза речи прямо на ноутбуке (Kokoro для английского, Piper для русского). Звук, который Veo сгенерировал вместе с видео: кафе, дождь. И музыкальная подложка из открытой модели MusicGen. Всё сведено к громкости −14 LUFS: это уровень, к которому Spotify приводит треки.",
                      f"Answer: three layers. The narrator: three lines, {num(secs)} seconds of speech from an open-weight text-to-speech model running on a laptop (Kokoro for English, Piper for Russian). The sound Veo generated with the video: cafe, rain. And a music bed from the open MusicGen model. Everything is mixed to −14 LUFS, the level Spotify normalises tracks to."),
                    t("Честно: результат не идеален, и в уроке мы найдём ошибки этой озвучки с помощью распознавания речи. Это и есть главный навык сегодня: сделать и проверить.",
                      "To be clear, the result is not perfect: later in the lesson we find its errors with speech-to-text. That is today’s main skill: produce, then check."),
                    teams()))


def s_layers():
    def col(k, h, sub, tools, ctrl, pay, use, start):
        chips = "".join(f'<span class="tchip">{x}</span>' for x in tools)
        return (f'<div class="layer" style="--k:var(--{k})"><div class="lh">{h}</div><div class="ls">{sub}</div>'
                f'<div class="tchips">{chips}</div>'
                f'<dl><dt>{t("Управление", "Control")}</dt><dd>{ctrl}</dd><dt>{t("Оплата", "Billing")}</dt><dd>{pay}</dd><dt>{t("Для чего", "Use for")}</dt><dd>{use}</dd><dt>{t("Начать с", "Start with")}</dt><dd><b>{start}</b></dd></dl></div>')
    c1 = col("cyan", t("Чат-приложения", "Chat apps"), t("голос и музыка прямо в чате", "voice and music inside a chat"),
             ["ChatGPT", "Gemini app"],
             t("голосовой режим и промпт; голос и длину почти не настроить", "voice mode and a prompt; little control over voice and length"),
             t("подписка", "subscription"), t("попробовать, черновик музыки", "trying things, music drafts"), "Gemini app (Lyria 3.5)")
    c2 = col("green", t("Веб-студии", "Web studios"), t("интерфейс для звука", "dedicated audio UI"),
             ["ElevenLabs", "Suno", "Google AI Studio"],
             t("библиотека голосов, настройки, звуковые эффекты, музыка, дубляж", "voice library, settings, sound effects, music, dubbing"),
             t("кредиты; бесплатный лимит небольшой", "credits; small free allowance"), t("озвучка ролика, ДЗ", "voicing a video, homework"), "ElevenLabs")
    c3 = col("violet", "API", t("код и автоматизация", "code and automation"),
             ["OpenAI Audio", "Gemini API", "Google Cloud / Azure Speech", "ElevenLabs API", "Deepgram / AssemblyAI"],
             t("всё как параметры запроса; пакетная обработка, живой звук", "everything as request parameters; batch jobs, live audio"),
             t("за символ, токен или минуту", "per character, token or minute"), t("пайплайны, продукты, агенты", "pipelines, products, agents"), "Gemini API")
    return dict(min=4, html=f'''
  {head(t("Где генерировать", "Where to generate"), t("Три уровня доступа к аудиомоделям: чат, веб-студия, API", "Three access layers for audio models: chat, web studio, API"), k="cyan")}
  <div class="body" style="margin-top:16px;">
    <div class="layers">{c1}{c2}{c3}</div>
    <div class="note" style="margin-top:20px;--k:var(--green)">{t("<b>Четвёртый путь: открытые модели на своём компьютере.</b> Whisper (распознавание), Kokoro и Piper (синтез речи), MusicGen (музыка). $0 за минуту, но железо, установка и лицензии на вас. Наш пример сделан так.", "<b>A fourth path: open-weight models on your own machine.</b> Whisper (speech recognition), Kokoro and Piper (speech synthesis), MusicGen (music). $0 per minute, but hardware, setup and licences are yours. Our example was made this way.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Та же схема, что в L04 и L05. Чат-приложения: голосовой режим ChatGPT, Gemini app с Gemini Live, и в Gemini app с сентября 2026 есть музыка на модели Lyria 3.5. Удобно попробовать, но голос, темп и длину почти не настроить.",
                      "⏱ 4 min. Same structure as in L04 and L05. Chat apps: ChatGPT voice mode, the Gemini app with Gemini Live; since September 2026 the Gemini app also makes music with Lyria 3.5. Good for trying things, but you barely control the voice, pace and length."),
                    t("Веб-студии: ElevenLabs (голоса, клонирование, звуковые эффекты, музыка, дубляж), Suno (песни), Google AI Studio (площадка для синтеза речи и музыки Gemini). Здесь делается домашнее задание.",
                      "Web studios: ElevenLabs (voices, cloning, sound effects, music, dubbing), Suno (songs), Google AI Studio (playground for Gemini speech and music). This is where the homework happens."),
                    t("API: OpenAI (синтез, распознавание, Realtime), Gemini API (синтез речи, Live, Lyria), Google Cloud и Azure Speech, ElevenLabs API, Deepgram и AssemblyAI для распознавания. Оплата за символ текста, за аудиотокен или за минуту звука; сравним на слайде стоимости.",
                      "API: OpenAI (speech synthesis, transcription, Realtime), Gemini API (speech generation, Live, Lyria), Google Cloud and Azure Speech, ElevenLabs API, Deepgram and AssemblyAI for transcription. Billed per character of text, per audio token or per minute of audio; we compare them on the cost slide."),
                    t("Открытые модели: наш пример целиком сделан ими на ноутбуке без видеокарты. Это бесплатно за минуту, но у каждой модели своя лицензия; MusicGen, например, только для некоммерческого использования.",
                      "Open weights: our whole example was made with them on a laptop without a GPU. Free per minute, but each model has its own licence; MusicGen, for example, is non-commercial only.")))


def s_tasks():
    def task(k, a, b, h, d):
        return (f'<div class="task" style="--k:var(--{k})"><div class="io"><span>{a}</span><i>→</i><span>{b}</span></div>'
                f'<div><div class="h">{h}</div><div class="d">{d}</div></div></div>')
    return dict(min=4, html=f'''
  {head(t("Карта задач", "Task map"), t("Четыре задачи аудио-ИИ: что на входе и что на выходе", "Four audio AI tasks: what goes in and what comes out"), k="violet")}
  <div class="body">
    <div class="tasks">
      {task("cyan", t("текст", "text"), t("голос", "voice"), t("Синтез речи (text-to-speech, TTS)", "Text-to-speech (TTS)"), t("озвучка роликов, уведомления, аудиокниги. <b>Сегодня: голос курьера.</b>", "video voice-over, notifications, audiobooks. <b>Today: the courier narration.</b>"))}
      {task("green", t("голос", "voice"), t("текст", "text"), t("Распознавание речи (speech-to-text, STT)", "Speech-to-text (STT)"), t("субтитры, протоколы встреч, поиск по звонкам. Второе название: automatic speech recognition (ASR). <b>Сегодня: проверка озвучки.</b>", "subtitles, meeting notes, call search. Also called automatic speech recognition (ASR). <b>Today: checking the voice-over.</b>"))}
      {task("amber", t("голос", "voice"), t("голос", "voice"), t("Речь в речь (speech-to-speech)", "Speech-to-speech"), t("голосовые агенты, синхронный перевод, дубляж. Отвечает за доли секунды.", "voice agents, live translation, dubbing. Responds within a fraction of a second."))}
      {task("violet", t("текст", "text"), t("музыка, шумы", "music, SFX"), t("Музыка и звуковые эффекты", "Music and sound effects (SFX)"), t("подложка, джинглы, шумы. Плюс звук, который <b>видеомодель</b> делает сама (L05).", "beds, jingles, effects. Plus the sound a <b>video model</b> makes by itself (L05)."))}
    </div>
    <div class="plaque g" style="margin-top:30px;"><b>{t("Озвучка ролика использует три из четырёх:", "Voicing a video uses three of the four:")}</b> {t("синтез речи для голоса, музыку и эффекты для фона, распознавание речи для проверки.", "text-to-speech for the voice, music and effects for the background, speech-to-text for the check.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Слова «аудио-ИИ» прячут четыре разные задачи. Смотрим на вход и выход. Текст в голос: синтез речи, сокращённо TTS. Голос в текст: распознавание речи, STT или ASR, это синонимы. Голос в голос: голосовые агенты и перевод. Текст в музыку и шумы.",
                      "⏱ 4 min. “Audio AI” hides four different tasks. Look at input and output. Text to voice: text-to-speech, TTS. Voice to text: speech-to-text, STT, also called automatic speech recognition, ASR; same thing. Voice to voice: voice agents and translation. Text to music and sound effects."),
                    t("Разные задачи решают разные модели с разными ценами: синтез считают за символы, распознавание за минуты, голосовых агентов за минуты разговора, музыку за трек.",
                      "Different tasks use different models and different prices: synthesis is billed per character, transcription per minute, voice agents per minute of conversation, music per track."),
                    t("Наш урок держится на озвучке ролика, она использует три задачи. Голосовых агентов разберём на уровне архитектуры, их строят в модуле про агентов.",
                      "The lesson is built around voicing a video, which uses three tasks. Voice agents get one architecture slide; you build agents later in the agents module.")))


def s_how():
    line = R()["lines"][0]
    env = ENV["vo_" + LANG + "_fine"]
    x0, x1 = line["start"] / 23.0, (line["end"] + 0.2) / 23.0
    return dict(min=4, html=f'''
  {head(t("Принцип работы", "How it works"), t("Как модель синтеза речи превращает текст в звук", "How a speech model turns text into sound"), k="violet")}
  <div class="body">
    <div class="flow" style="--k:var(--violet);justify-content:center;gap:16px;">
      <div class="box">{t("Текст", "Text")}<small>“{line["spoken"].split(".")[0]}.”</small></div><div class="arr">→</div>
      <div class="box hl">{t("Модель", "Model")}<small>{t("предсказывает аудиотокены", "predicts audio tokens")}</small></div><div class="arr">→</div>
      <div class="box">{t("Аудиотокены", "Audio tokens")}<small>{t("25–50 в секунду", "25–50 per second")}</small></div><div class="arr">→</div>
      <div class="box hl">{t("Декодер", "Decoder")}<small>{t("токены → отсчёты", "tokens → samples")}</small></div><div class="arr">→</div>
      <div class="box">{t("Звук", "Waveform")}<small>{t("48 000 чисел в секунду", "48,000 numbers per second")}</small></div>
    </div>
    <div style="margin-top:30px;">
      <div class="prompt-label">{t("Наша реплика 1, реальная форма волны", "Our line 1, real waveform")} · {num(line["end"] - line["start"])} {t("с", "s")}</div>
      {wave(env, h=170, w=1440, color="var(--cyan)", gain=1.0, x0=x0, x1=x1)}
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:26px;">
      <div class="note" style="--k:var(--cyan)">{t("<b>Сколько данных:</b> секунда звука = 48 000 чисел. Модель работает со сжатым видом: Gemini считает <b>25 аудиотокенов в секунду</b>, MusicGen <b>50</b>.", "<b>How much data:</b> one second of audio is 48,000 numbers. Models work with a compressed form: Gemini bills <b>25 audio tokens per second</b>, MusicGen uses <b>50</b>.")}</div>
      <div class="note" style="--k:var(--amber)">{t("<b>Чего нет внутри:</b> словаря правил чтения. Модель выучила, как текст обычно звучит. Поэтому ошибается на <b>числах, именах, сокращениях</b>.", "<b>What is not inside:</b> a rulebook for reading. The model learned how text usually sounds, so it fails on <b>numbers, names and abbreviations</b>.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Связь с L03 и L05: языковая модель предсказывает текстовые токены, видеомодель чистит от шума кадры. Модель синтеза речи предсказывает аудиотокены: сжатые кусочки звука. Декодер (его ещё называют вокодером) превращает их обратно в волну.",
                      "⏱ 4 min. Link to L03 and L05: a language model predicts text tokens, a video model denoises frames. A speech model predicts audio tokens, compressed chunks of sound. A decoder (also called a vocoder) turns them back into a waveform."),
                    t("Масштаб: в секунде звука 48 000 чисел при качестве 48 кГц. Модель так не работает, она видит сжатое представление. Два реальных числа: Gemini тарифицирует синтез по 25 аудиотокенов на секунду; MusicGen, которым сделана наша музыка, работает с 50 токенами в секунду. Внутреннее устройство моделей разное, принцип общий.",
                      "Scale: at 48 kHz one second of audio is 48,000 numbers. The model does not work at that level; it sees a compressed representation. Two real numbers: Gemini bills speech at 25 audio tokens per second; MusicGen, which made our music, works with 50 tokens per second. Architectures differ, the principle is the same."),
                    t("Главное: внутри нет правил вроде «417 читай как четыреста семнадцать». Модель видела много пар «текст и звук» и угадывает. Поэтому числа, имена и сокращения — самые частые ошибки. Это тема шага 2.",
                      "Key point: there is no rule inside like “read 417 as four hundred seventeen”. The model has seen many text and audio pairs and guesses. That is why numbers, names and abbreviations are the most common errors. This is step 2.")))


def s_video_audio():
    s1 = " ".join(x["text"] for x in REPORT["veo_shot1"]["transcript"])
    tw = " ".join(x["text"] for x in REPORT["veo_trainwreck"]["transcript"])
    return dict(min=4, html=f'''
  {head(t("Мост из L05", "Bridge from L05"), t("Звук внутри видеомодели: что Veo 3.1 сгенерировал сам", "Audio inside a video model: what Veo 3.1 generated by itself"), k="red")}
  <div class="body">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;flex:none;">
      <div class="stack" style="gap:12px;">
        {aud("veo_shot1", t("Шот 1, кафе", "Shot 1, cafe"), t("промпт без реплик", "prompt has no dialogue"), "red", "veo_shot1")}
        <div class="tx" style="font-size:22px;"><small>{t("Распознано в звуке Veo", "Heard in Veo’s audio")}</small>“{s1}”</div>
      </div>
      <div class="stack" style="gap:12px;">
        {aud("veo_trainwreck", t("Неудачный клип из L05", "The L05 failure clip"), t("промпт без голоса", "prompt asks for no voice"), "red", "veo_trainwreck")}
        <div class="tx" style="font-size:22px;"><small>{t("Распознано в звуке Veo", "Heard in Veo’s audio")}</small>“{tw}”</div>
      </div>
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;flex:none;margin-top:40px;">
      <div class="note" style="--k:var(--green)">{t("<b>Даёт:</b> шум улицы, дождь, шаги, синхронно с картинкой. Но платим за него: Veo 3.1 в Vertex AI со звуком $0.40/с, без звука $0.20/с.", "<b>Gives:</b> street noise, rain, footsteps, in sync with the picture. But you pay for it: Veo 3.1 on Vertex AI is $0.40/s with audio, $0.20/s without.")}</div>
      <div class="note" style="--k:var(--red)">{t("<b>Не даёт:</b> точный текст, один голос на все шоты, отдельные дорожки. Реплики модель <b>придумывает сама</b>.", "<b>Does not give:</b> exact words, one voice across shots, separate tracks. The model <b>makes up lines</b> by itself.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Включите оба звука. Слева шот 1 из L05: в промпте не было ни одной реплики, а Veo озвучил бариста и курьера: «Here’s your order. Thank you. Have a good day». Справа неудачный клип из L05: в промпте карта навигатора, и Veo сам добавил голос навигатора «Continue straight for 200 meters». Мы это не слышали, пока не прогнали звук через распознавание речи.",
                      "⏱ 4 min. Play both. Left: shot 1 from L05. The prompt had no dialogue, yet Veo voiced the barista and the courier: “Here’s your order. Thank you. Have a good day.” Right: the L05 failure clip. The prompt mentions a navigation map, and Veo added a navigator voice: “Continue straight for 200 meters”. We did not notice this until we ran the audio through speech-to-text."),
                    t("Вывод. Звук видеомодели хорош как фон: шумы, дождь, шаги, синхронно с картинкой. Но он не бесплатный: в Vertex AI звук у Veo 3.1 выключается параметром generateAudio, и тогда секунда стоит $0.20 вместо $0.40; у Kling 3.0 звук добавляет к цене около 50%. В Gemini API Veo всегда со звуком. И главное: точный текст, один и тот же голос в трёх шотах и отдельные дорожки для монтажа видеомодель не даёт. Реплики она придумывает.",
                      "Takeaway. A video model’s audio works as background: noise, rain, footsteps, in sync with the picture. It is not free: on Vertex AI the generateAudio parameter turns Veo 3.1 audio off, and a second then costs $0.20 instead of $0.40; on Kling 3.0 audio adds about 50% to the price. In the Gemini API Veo always generates audio. And the main point: a video model does not give exact words, the same voice across three shots or separate tracks for editing. It makes up lines."),
                    t("Правило: если нужны точные слова, голос делаем отдельно (синтез речи), а звук видеомодели используем как фон или выключаем. В официальном руководстве по промптам Veo реплики пишут в кавычках, шумы после «SFX:», фон после «Ambient noise:»; можно написать «No dialogue». Это помогает, но не гарантирует.",
                      "Rule: when you need exact words, generate the voice separately with text-to-speech, and use the video model’s audio as background or mute it. Google’s Veo prompting guide puts dialogue in quotes, sound effects after “SFX:” and background after “Ambient noise:”; you can also write “No dialogue”. That helps but guarantees nothing.")))


def s_script():
    lines = R()["lines"]
    shots = [("tl_shot1", "0–8", t("кафе: шум зала, чашки", "cafe: room noise, cups")),
             ("tl_shot2", "7,5–15,5" if LANG == "ru" else "7.5–15.5", t("дождь, шины по лужам", "rain, tyres on puddles")),
             ("tl_shot3", "15–23", t("тихий интерфейсный звук", "soft UI sound"))]
    trs = ""
    for (img, tm, sfx), ln in zip(shots, lines):
        w = len(ln["spoken"].split())
        d = ln["end"] - ln["start"]
        trs += (f'<tr><td class="im"><img src="{IMG}{img}.jpg" alt=""></td><td class="tm">{tm} {t("с", "s")}</td>'
                f'<td>“{ln["display"]}”</td><td class="tm">{w} / {num(d)} {t("с", "s")}</td><td>{sfx}</td></tr>')
    words, secs, _ = voice_words()
    return dict(min=5, html=f'''
  {head(t("Шаг 1 • сценарий", "Step 1 • script"), t("Сценарий озвучки: текст, время и бюджет слов на каждый шот", "Voice-over script: text, timing and a word budget for each shot"), k="cyan")}
  <div class="body" style="margin-top:12px;">
    <table class="sb">
      <thead><tr><th>{t("Шот", "Shot")}</th><th>{t("Время", "Time")}</th><th>{t("Голос за кадром", "Voice-over")}</th><th>{t("Слов / длина", "Words / length")}</th><th>{t("Шумы", "Sound effects")}</th></tr></thead>
      <tbody>{trs}</tbody>
    </table>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:22px;">
      <div class="stat" style="--k:var(--cyan)"><div class="n">≈ {num(words / secs)} {t("слова/с", "words/s")}</div><div class="d">{t("измерено на нашей озвучке; планируйте <b>2–2,5 слова в секунду</b>, чтобы осталась пауза", "measured on our voice-over; plan for <b>2–2.5 words per second</b> to leave a pause")}</div></div>
      <div class="note" style="--k:var(--amber)">{t("<b>Шот 8 с ≈ 12–16 слов максимум.</b> Не влезает: сокращаем текст, а не ускоряем голос. Это колонки «закадровый текст» и «шумы» из сториборда L05.", "<b>An 8 s shot fits 12–16 words at most.</b> If it does not fit, cut the text, do not speed up the voice. These are the voice-over and sound-effects columns of the L05 storyboard.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. В L05 у сториборда было 7 колонок, и три из них мы оставили на потом: закадровый текст, шумы, музыка. Сегодня их заполняем. Одна строка = один шот = одна реплика.",
                      "⏱ 5 min. The L05 storyboard had 7 columns, and we left three for later: voice-over, sound effects, music. Today we fill them in. One row = one shot = one line."),
                    t(f"Бюджет слов. Наш голос говорит примерно {num(words / secs)} слова в секунду. Для плана берите 2–2,5 слова в секунду: реплике нужна пауза перед склейкой. Значит, на 8-секундный шот 12–16 слов максимум. Если текст не влезает, сокращаем текст. Ускорять голос плохая идея: звучит неестественно.",
                      f"Word budget. Our voice speaks about {num(words / secs)} words per second. Plan with 2–2.5 words per second: a line needs a pause before the cut. So an 8-second shot fits 12–16 words at most. If the text does not fit, cut the text. Speeding up the voice sounds unnatural."),
                    t("Упражнение (1 мин, в чат): напишите реплику для шота 4 «курьер у двери» не длиннее 12 слов.",
                      "Exercise (1 min, chat): write the line for shot 4, “courier at the door”, in 12 words or fewer.")))


def s_text():
    if LANG == "ru":
        rows = [("6:42", "Шесть сорок две", "время: «шесть сорок две» или «восемнадцать сорок две»?"),
                ("417", "четыреста семнадцать", "число или номер «четыре один семь»?"),
                ("12 мин", "двенадцать минут", "сокращения модель может прочитать по буквам")]
    else:
        rows = [("6:42", "Six forty-two", "a time, a score or a ratio?"),
                ("417", "four one seven", "a number or an ID: “four hundred seventeen”?"),
                ("12 min", "twelve minutes", "abbreviations may be read letter by letter")]
    trs = "".join(f'<tr><td class="tm" style="font-size:30px;padding:22px 12px">{a}</td><td style="font-size:26px;color:var(--green)">{b}</td><td style="font-size:21px">{c}</td></tr>' for a, b, c in rows)
    return dict(min=5, html=f'''
  {head(t("Шаг 2 • текст для голоса", "Step 2 • text for the voice"), t("Текст для голоса: числа словами, стиль инструкцией", "Text for the voice: numbers as words, style as an instruction"), k="cyan")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="stack" style="gap:14px;">
        <div class="prompt-label">{t("Что видит зритель → что читает модель", "What the viewer sees → what the model reads")}</div>
        <table class="sb"><thead><tr><th>{t("Сценарий", "Script")}</th><th>{t("Текст для голоса", "Spoken text")}</th><th>{t("Почему", "Why")}</th></tr></thead><tbody>{trs}</tbody></table>
      </div>
      <div class="stack" style="gap:16px;">
        <div class="prompt-label">{t("Стиль: инструкция, а не часть текста", "Style: an instruction, not part of the text")}</div>
        <div class="prompt">{t("Инструкция:", "Instruction:")} <span style="color:var(--amber)">{t("Спокойный, дружелюбный диспетчер. Средний темп. Короткая пауза после каждой фразы.", "Calm, friendly dispatcher. Medium pace. Short pause after each sentence.")}</span><br>{t("Текст:", "Text:")} {R()["lines"][0]["spoken"]}</div>
        <ul class="list">
          <li>{t("<b>OpenAI, Gemini:</b> стиль описывают словами в инструкции.", "<b>OpenAI, Gemini:</b> describe the style in words in an instruction.")}</li>
          <li>{t("<b>ElevenLabs v3:</b> теги в тексте, например <code>[whispers]</code>.", "<b>ElevenLabs v3:</b> tags inside the text, e.g. <code>[whispers]</code>.")}</li>
          <li>{t("<b>Словарь произношений</b> для имён и терминов (ElevenLabs, Google, Azure).", "<b>Pronunciation dictionary</b> for names and terms (ElevenLabs, Google, Azure).")}</li>
        </ul>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Сценарий пишем для зрителя: «6:42», «417». Модели синтеза речи даём отдельную колонку «как произнести»: словами. Иначе модель угадывает: 6:42 это время, счёт матча или пропорция? 417 это число или номер заказа, который читают по цифрам?",
                      "⏱ 5 min. The script is written for the viewer: “6:42”, “417”. The speech model gets a separate “spoken text” column with everything written out as words. Otherwise the model guesses: is 6:42 a time, a score or a ratio? Is 417 a number or an order ID read digit by digit?"),
                    t("Стиль голоса — отдельная инструкция, не часть текста. У OpenAI и Gemini это фраза на естественном языке: «спокойный, дружелюбный диспетчер». В ElevenLabs v3 теги прямо в тексте, например [whispers]. Для имён и терминов у ElevenLabs, Google и Azure есть словари произношений.",
                      "Voice style is a separate instruction, not part of the text. In OpenAI and Gemini it is a natural-language phrase: “calm, friendly dispatcher”. ElevenLabs v3 uses tags inside the text, such as [whispers]. For names and terms, ElevenLabs, Google and Azure offer pronunciation dictionaries."),
                    t("Даже с правильным текстом голос может ошибиться, особенно на редких языках и в открытых моделях. Это проверим на шаге 6.",
                      "Even with correct text the voice can still get it wrong, especially in less common languages and open models. We check that in step 6.")))


def s_voice():
    def opt(k, h, src, gate, ex):
        return (f'<div class="vopt" style="--k:var(--{k})"><div class="h">{h}</div><div class="in">{src}</div>'
                f'<div class="gate">{gate}</div><div class="ex">{ex}</div></div>')
    return dict(min=4, html=f'''
  {head(t("Шаг 3 • голос", "Step 3 • voice"), t("Три источника голоса: библиотека, описание, клон", "Three sources of a voice: library, description, clone"), k="cyan")}
  <div class="body" style="margin-top:18px;">
    <div class="vopts">
      {opt("green", t("Готовый голос", "Library voice"), t("<b>Вход:</b> выбрать из библиотеки сервиса", "<b>Input:</b> pick from the service’s library"), t("✓ лицензия сервиса", "✓ covered by the service licence"), t("Gemini: 30 голосов; OpenAI: 13; наш пример: Kokoro <code>af_heart</code>, Piper <code>dmitri</code>", "Gemini: 30 voices; OpenAI: 13; our example: Kokoro <code>af_heart</code>, Piper <code>dmitri</code>"))}
      {opt("amber", t("Голос по описанию", "Designed voice"), t("<b>Вход:</b> текст «молодой голос, лёгкая хрипотца, быстрый темп»", "<b>Input:</b> a text description: “young voice, slightly husky, fast pace”"), t("! проверить похожесть на известных людей", "! check it does not resemble a real person"), t("ElevenLabs Voice Design, Gemini API voice design", "ElevenLabs Voice Design, Gemini API voice design"))}
      {opt("red", t("Клон голоса", "Cloned voice"), t("<b>Вход:</b> запись реального человека, от 3–10 с до 30+ мин", "<b>Input:</b> recordings of a real person, from 3–10 s to 30+ min"), t("✗ только с письменного согласия владельца", "✗ only with the owner’s written consent"), t("сервисы требуют запись фразы согласия или проверку голосом", "services require a recorded consent phrase or a voice check"))}
    </div>
    <div class="note" style="margin-top:26px;--k:var(--red)">{t("<b>Перед выбором:</b> прогоните через голос самые сложные слова сценария (имена, числа). Голос, который их портит, не подходит, каким бы красивым он ни был.", "<b>Before you commit:</b> run the hardest words of the script (names, numbers) through the voice. A voice that breaks them is the wrong voice, however good it sounds.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Три источника голоса. Готовый голос из библиотеки: лицензия уже покрыта сервисом. У Gemini 30 готовых голосов, у OpenAI 13. В нашем примере английский голос Kokoro af_heart и русский Piper dmitri.",
                      "⏱ 4 min. Three sources of a voice. A library voice: the service’s licence already covers it. Gemini has 30 prebuilt voices, OpenAI 13. Our example uses Kokoro af_heart for English and Piper dmitri for Russian."),
                    t("Голос по описанию: пишете текстом, какой нужен голос, сервис генерирует новый. Есть в ElevenLabs (Voice Design) и в Gemini API. Проверьте, что результат не похож на известного человека.",
                      "Designed voice: describe the voice in text and the service generates a new one. Available in ElevenLabs (Voice Design) and the Gemini API. Check that the result does not sound like a known person."),
                    t("Клон: голос реального человека по записям. ElevenLabs Instant: 1–2 минуты записи, Professional: от 30 минут. Открытые модели вроде Qwen3-TTS клонируют по 3 секундам. Поэтому крупные сервисы требуют доказательство согласия: OpenAI и Google просят записать фиксированную фразу согласия, Azure пускает к функции только по заявке, ElevenLabs для профессионального клона просит владельца прочитать проверочный текст. Подробно на слайде рисков.",
                      "Clone: a real person’s voice from recordings. ElevenLabs Instant needs 1–2 minutes of audio, Professional 30 minutes or more. Open models such as Qwen3-TTS clone from 3 seconds. That is why the big services ask for proof of consent: OpenAI and Google require a recorded fixed consent phrase, Azure gives access only on application, and ElevenLabs asks the voice owner to read a verification text for a professional clone. Details on the risk slide.")))


def s_music():
    prompt = REPORT.get("music_prompt", "calm lo-fi hip hop beat, soft electric piano, light rain mood, 85 bpm, no vocals")
    return dict(min=4, html=f'''
  {head(t("Шаг 4 • шумы и музыка", "Step 4 • sound effects and music"), t("Шумы и музыка: промпт, длина и лицензия трека", "Sound effects and music: prompt, length and the track licence"), k="cyan")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="stack" style="gap:14px;">
        {aud("music_bed", t("Наша музыкальная подложка", "Our music bed"), "MusicGen-small · 23 " + t("с", "s"), "violet", "music")}
        <div><div class="prompt-label">{t("Промпт", "Prompt")}</div><div class="prompt">{prompt}</div></div>
        <div class="note" style="--k:var(--red)">{t("Веса MusicGen: лицензия <b>CC-BY-NC 4.0</b>, только некоммерческое использование. Для урока можно, для клиента нет.", "MusicGen weights: <b>CC-BY-NC 4.0</b> licence, non-commercial use only. Fine for a lesson, not for a client.")}</div>
      </div>
      <table class="cost lic">
        <thead><tr><th>{t("Сервис", "Service")}</th><th>{t("Длина", "Length")}</th><th>{t("Коммерческое использование", "Commercial use")}</th></tr></thead>
        <tbody>
          <tr><td class="m">Suno v6<small>{t("песни", "songs")}</small></td><td>{t("песня", "song")}</td><td style="font-family:var(--body);font-size:20px">{t("только платные тарифы", "paid plans only")}</td></tr>
          <tr><td class="m">Lyria 3.5<small>Gemini app, Gemini API</small></td><td>{t("пара минут", "~2 min")}</td><td style="font-family:var(--body);font-size:20px">{t("метка SynthID на каждом треке", "SynthID mark on every track")}</td></tr>
          <tr><td class="m">ElevenLabs Music<small>{t("музыка", "music")}</small></td><td>3 {t("с", "s")} – 5 {t("мин", "min")}</td><td style="font-family:var(--body);font-size:20px">{t("«почти любое», по тарифу", "“nearly all”, per plan")}</td></tr>
          <tr><td class="m">ElevenLabs SFX<small>{t("шумы", "sound effects")}</small></td><td>≤ 30 {t("с", "s")}</td><td style="font-family:var(--body);font-size:20px">{t("по тарифу", "per plan")}</td></tr>
        </tbody>
      </table>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Включите подложку. Её сделала открытая модель MusicGen-small по промпту слева, прямо на ноутбуке, 23 секунды под длину ролика. Промпт музыки как промпт картинки: жанр, инструменты, настроение, темп, «без вокала».",
                      "⏱ 4 min. Play the bed. The open MusicGen-small model made it from the prompt on the left, on a laptop, 23 seconds to match the video. A music prompt works like an image prompt: genre, instruments, mood, tempo, “no vocals”."),
                    t("Главное здесь не качество, а лицензия. Веса MusicGen под CC-BY-NC: для урока можно, в коммерческий ролик нельзя. У сервисов права зависят от тарифа на момент генерации: в Suno права на коммерческое использование есть только на платных тарифах, на бесплатном песни принадлежат Suno; апгрейд позже не даёт прав задним числом. Lyria 3.5 от Google есть в Gemini app и Gemini API, каждый трек получает невидимую метку SynthID. ElevenLabs Music: от 3 секунд до 5 минут, «разрешено почти для любого коммерческого использования» по их условиям. Шумы ElevenLabs: до 30 секунд за генерацию.",
                      "The point here is the licence, not the quality. MusicGen weights are CC-BY-NC: fine for a lesson, not for a commercial video. For services, rights depend on your plan at the moment of generation: Suno gives commercial rights only on paid plans; on the free plan Suno owns the songs, and upgrading later does not grant rights retroactively. Google’s Lyria 3.5 is in the Gemini app and the Gemini API, and every track carries an invisible SynthID mark. ElevenLabs Music: 3 seconds to 5 minutes, “cleared for nearly all commercial uses” under their terms. ElevenLabs sound effects: up to 30 seconds per generation."),
                    t("Шумы для ролика часто уже есть: это звук самой видеомодели из L05 (кафе, дождь). Его мы и используем как фон.",
                      "Often the sound effects already exist: the video model’s own audio from L05 (cafe, rain). We use it as the background.")))


def s_mix():
    span = 1440
    rows = [("vo_" + LANG, t("Голос", "Voice"), t("синтез речи", "text-to-speech"), "var(--cyan)", R()["voice_only"]["lufs"]),
            ("veo", t("Звук Veo", "Veo audio"), t("шумы из видео, приглушается под голосом", "video sound, ducked under the voice"), "var(--green)", REPORT["veo_native"]["lufs"]),
            ("music", t("Музыка", "Music"), "MusicGen", "var(--violet)", None),
            ("mix_" + LANG, t("Итог", "Mix"), f'{num(R()["mix"]["lufs"])} LUFS · {num(R()["mix"]["true_peak_dbfs"])} dBTP', "var(--amber)", None)]
    stems = "".join(f'<div class="stem" style="--k:{c}"><div class="lab">{lab}<small>{sub}</small></div>{wave(ENV[k], h=70, w=span, color=c)}</div>'
                    for k, lab, sub, c, _ in rows)
    cmd = ('ffmpeg -i voice.wav -i veo.wav -i music.wav -filter_complex \\\n'
           ' "[1][2]amix[bed];[bed][0]sidechaincompress[duck];\n'
           '  [0][duck]amix,loudnorm=I=-14:TP=-1.5" mix.wav')
    return dict(min=6, html=f'''
  {head(t("Шаг 5 • сведение", "Step 5 • mix"), t("Сведение: голос сверху, фон тише, −14 LUFS", "Mixing: voice on top, background ducked, −14 LUFS"), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="stems">{stems}</div>
    <div class="row" style="grid-template-columns:1fr 1.15fr;gap:36px;flex:none;margin-top:20px;align-items:start;">
      <ul class="list">
        <li>{t("<b>Приглушение (ducking):</b> фон автоматически тише, пока звучит голос.", "<b>Ducking:</b> the background drops automatically while the voice speaks.")}</li>
        <li>{t("<b>Громкость:</b> −14 LUFS для YouTube и Spotify, −23 LUFS для эфира (EBU R128).", "<b>Loudness:</b> −14 LUFS for Spotify-style streaming, −23 LUFS for broadcast (EBU R128).")}</li>
        <li>{t("<b>Пик:</b> не выше −1 dBTP (true peak, истинный пик), иначе хрип после сжатия.", "<b>Peak:</b> no higher than −1 dBTP (decibels true peak), otherwise distortion after encoding.")}</li>
      </ul>
      <pre class="code" style="font-size:17px;padding:14px 18px;white-space:pre-wrap;">{cmd}</pre>
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 6 мин. Это реальные дорожки нашего ролика. Голос сам по себе {num(R()['voice_only']['lufs'])} LUFS, звук Veo {num(REPORT['veo_native']['lufs'])} LUFS, ниже музыка и итог. Видно, как фон проседает там, где говорит голос: это приглушение, по-английски ducking.",
                      f"⏱ 6 min. These are the real tracks of our video. The voice alone is {num(R()['voice_only']['lufs'])} LUFS, Veo’s audio {num(REPORT['veo_native']['lufs'])} LUFS, then music and the final mix. You can see the background drop where the voice speaks: that is ducking."),
                    t("LUFS — единица громкости, как её слышит человек. Стриминговые платформы приводят треки к своему уровню: Spotify к −14 LUFS, Apple Podcasts к −16. Эфирный стандарт EBU R128 −23. Если ролик тише, платформа его поднимет вместе с шумом; если громче, опустит. Второе число — истинный пик, true peak: не выше −1 dBTP, иначе после сжатия в MP3 или AAC появится хрип.",
                      "LUFS is a loudness unit that follows human hearing. Streaming platforms normalise tracks to their level: Spotify to −14 LUFS, Apple Podcasts to −16. Broadcast standard EBU R128 is −23. A quieter video gets raised together with its noise; a louder one gets turned down. The second number is true peak: no higher than −1 dBTP, otherwise MP3 or AAC encoding adds distortion."),
                    t("Наш первый проход нормализации дал пик −0,6 dBTP на русской версии, то есть не прошёл. Исправили двухпроходной нормализацией и лимитером, теперь −1,1. Сводить можно в CapCut, Audacity, DaVinci Resolve или одной командой ffmpeg справа (полная версия в make_audio.py).",
                      "Our first normalisation pass gave a −0.6 dBTP peak on the Russian version, a fail. Two-pass normalisation plus a limiter fixed it: now −1.1. You can mix in CapCut, Audacity, DaVinci Resolve or with the ffmpeg command on the right (full version in make_audio.py)."),
                    teams()))


def s_check():
    rr = R()
    crit = rr["critical_terms"]
    ok = sum(c["ok"] for c in crit)
    heard = diff_markup(" ".join(x["display"] for x in rr["lines"]), " ".join(x["text"] for x in rr["transcript"]),
                        [c["term"] for c in crit if c["ok"]])
    if LANG == "ru":
        diag = [("red", "«Часть 42» вместо «Шесть сорок две»", "голос: проглатывает «ш»"), ("red", "«Оно» вместо «Анна»", "голос: неверно читает имя")]
    else:
        diag = [("red", "“Here’s your order.”", "mix: Veo’s invented line leaks through"), ("amber", "“642” instead of “6:42”", "transcriber format: the voice said it right")]
    script = " ".join(x["display"] for x in rr["lines"])
    diags = "".join(f'<li style="--k:var(--{k})"><b>{a}</b>: {b}</li>' for k, a, b in diag)
    return dict(min=5, html=f'''
  {head(t("Шаг 6 • проверка", "Step 6 • check"), t("Проверка озвучки распознаванием речи", "Checking the voice-over with speech-to-text"), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.45fr 1fr;gap:36px;align-items:center;flex:none;">
      <div class="stack" style="gap:16px;">
        <div class="tx"><small>{t("Сценарий", "Script")}</small>{script}</div>
        <div class="tx"><small>{t("Что услышал Whisper (small, на ноутбуке)", "What Whisper heard (small model, laptop)")}</small>{heard}</div>
        <ul class="list">{diags}</ul>
      </div>
      <div class="stack" style="gap:24px;">
        <div class="stat" style="--k:var(--amber)"><div class="n">{num(rr["wer_vs_display"] * 100, 0)}%</div><div class="d">{t("частота ошибок в словах (word error rate, WER) = (замены + пропуски + вставки) / слов в сценарии", "word error rate (WER) = (substitutions + deletions + insertions) / words in the script")}</div></div>
        <div class="stat" style="--k:var(--red)"><div class="n">{ok} / {len(crit)}</div><div class="d">{t("критичных слов распознано верно: время, номер заказа, минуты, имя", "critical terms heard correctly: time, order number, minutes, name")}</div></div>
        <div class="note" style="--k:var(--green)">{t("Ошибка найдена → <b>слушаем это место</b>: виноват голос, сведение или распознавание?", "Error found → <b>listen to that spot</b>: is it the voice, the mix or the transcriber?")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Как проверить озвучку, не вслушиваясь десять раз: прогоняем итоговый звук через распознавание речи и сравниваем с исходным сценарием. Мы использовали открытую модель Whisper small прямо на ноутбуке.",
                      "⏱ 5 min. How to check a voice-over without listening ten times: run the final audio through speech-to-text and compare with the script. We used the open Whisper small model on a laptop."),
                    t("Частота ошибок в словах, WER: замены плюс пропуски плюс вставки, делённые на число слов сценария. Чем ниже, тем лучше. Но одна цифра прячет главное: ошибка в номере заказа важнее десяти ошибок в артиклях. Поэтому отдельно проверяем список критичных слов: время, номер, минуты, имя.",
                      "Word error rate, WER: substitutions plus deletions plus insertions, divided by the number of words in the script. Lower is better. But one number hides the important part: an error in the order number matters more than ten errors in articles. So we check a separate list of critical terms: time, order number, minutes, name."),
                    t("Что нашли в английской версии: в начале распознано «Here’s your order», это реплика, которую придумал Veo (слайд 6), она пробивается через сведение. Значит, звук шота 1 нужно вырезать или заглушить в начале. «642» вместо «6:42»: послушали — голос сказал верно, это формат записи у распознавания. Ошибка проверки, а не озвучки.",
                      "What we found in English: the transcript starts with “Here’s your order”, the line Veo made up (slide 6), leaking through the mix. So the shot 1 audio needs to be cut or muted at the start. “642” instead of “6:42”: we listened, and the voice said it correctly; this is the transcriber’s formatting. A checking artefact, not a voice error."),
                    t("В русской версии: «Часть 42» вместо «Шесть сорок две» и «Оно» вместо «Анна». Послушали: это голос, открытая русская модель Piper читает эти слова плохо. Исправление: другой голос или переписать реплику. Это реальные результаты, ничего не подстроено.",
                      "In Russian: “Часть 42” instead of “Шесть сорок две” and “Оно” instead of “Анна”. We listened: it is the voice; the open Russian Piper model reads these words badly. Fix: a different voice or a rewritten line. These are real results, nothing staged.")))


def s_arch():
    def lane(k, h, sub, steps, lat, latsub):
        fl = '<div class="arr">→</div>'.join(f'<div class="box">{s}</div>' for s in steps)
        return (f'<div class="lane" style="--k:var(--{k})"><div class="h">{h}<small>{sub}</small></div>'
                f'<div class="flow" style="--k:var(--{k})">{fl}</div><div class="lat">{lat}<small>{latsub}</small></div></div>')
    return dict(min=5, html=f'''
  {head(t("Архитектура", "Architecture"), t("Три архитектуры распознавания речи: файл, поток, голосовой агент", "Three speech architectures: file, stream, voice agent"), k="violet")}
  <div class="body" style="margin-top:18px;">
    <div class="arch">
      {lane("cyan", t("Файл (batch)", "File (batch)"), t("субтитры, протоколы, наша проверка", "subtitles, meeting notes, our check"), [t("запись", "recording"), t("распознавание", "transcription"), t("текст с таймкодами", "text with timecodes")], t("секунды–минуты", "seconds–minutes"), t("ждать можно", "waiting is fine"))}
      {lane("green", t("Поток (streaming)", "Stream (streaming)"), t("живые субтитры, заметки на встрече", "live captions, meeting notes"), [t("микрофон", "microphone"), t("кусочки 0,1–0,25 с", "chunks of 0.1–0.25 s"), t("черновой текст → итоговый", "partial → final text")], t("доли секунды", "under a second"), t("черновик может измениться", "partial text may change"))}
      {lane("amber", t("Речь в речь (realtime)", "Speech-to-speech (realtime)"), t("голосовой агент, перевод", "voice agent, translation"), [t("голос", "voice"), t("конец фразы?", "end of turn?"), t("модель + инструменты", "model + tools"), t("голос", "voice")], t("≈ 1 с на ответ", "≈ 1 s per reply"), t("перебивание, тишина, задержка", "interruptions, silence, latency"))}
    </div>
    <div class="note" style="margin-top:22px;--k:var(--violet)">{t("<b>Голосовой агент двумя способами:</b> цепочка «распознавание → языковая модель → синтез» (проще отлаживать) или одна модель «речь в речь» (быстрее, естественнее). Строим агентов в модуле 4.", "<b>A voice agent, two ways:</b> a chain “speech-to-text → language model → text-to-speech” (easier to debug) or one speech-to-speech model (faster, more natural). We build agents in module 4.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Распознавание речи бывает в трёх архитектурах, и это разные продукты, а не «быстрее или медленнее». Файл: отдали запись, получили текст с таймкодами через секунды или минуты. Так работает наша проверка и любые субтитры.",
                      "⏱ 5 min. Speech recognition comes in three architectures, and they are different products, not just faster or slower. File: send a recording, get text with timecodes in seconds or minutes. That is our check and any subtitle job."),
                    t("Поток: звук с микрофона отправляют кусочками по 0,1–0,25 секунды, сервис сразу возвращает черновой текст и потом исправляет его в итоговый. Поэтому в живых субтитрах слова иногда меняются на глазах. Хранить надо итоговый текст.",
                      "Stream: microphone audio goes out in chunks of 0.1–0.25 seconds; the service immediately returns partial text and later replaces it with final text. That is why words in live captions sometimes change as you watch. Store the final text."),
                    t("Речь в речь: голосовой агент. Самое трудное здесь не модель, а разговор: понять, что человек закончил фразу, дать себя перебить, не молчать слишком долго. Есть два способа: цепочка из трёх моделей или одна модель речь-в-речь, например gpt-realtime у OpenAI или Gemini Live у Google. Подробно строим агентов в модуле 4.",
                      "Speech-to-speech: a voice agent. The hard part is not the model but the conversation: detecting that the person finished, letting them interrupt, not staying silent too long. Two ways to build it: a chain of three models, or one speech-to-speech model such as OpenAI’s gpt-realtime or Google’s Gemini Live. We build agents in module 4.")))


def s_market():
    rows = [
        ("cyan", t("Синтез речи", "Text-to-speech"), t("текст → голос", "text → voice"),
         [("ElevenLabs v4 / v3", ""), ("Gemini 3.8 Flash TTS", ""), ("OpenAI gpt-4o-mini-tts", ""), ("Azure Neural HD", ""), ("Google Chirp 3 HD", "")],
         [("Kokoro-82M", "Apache-2.0"), ("Qwen3-TTS", "Apache-2.0"), ("Chatterbox", "MIT")]),
        ("green", t("Распознавание речи", "Speech-to-text"), t("голос → текст", "voice → text"),
         [("OpenAI gpt-transcribe", ""), ("ElevenLabs Scribe v2", ""), ("AssemblyAI Universal-3.5 Pro", ""), ("Deepgram Nova-3", ""), ("Google Chirp 3", "")],
         [("Whisper large-v3-turbo", "MIT"), ("Qwen3-ASR", "Apache-2.0"), ("Parakeet", "CC-BY-4.0")]),
        ("amber", t("Речь в речь", "Speech-to-speech"), t("голосовые агенты, перевод", "voice agents, translation"),
         [("OpenAI gpt-realtime-2.1", ""), ("OpenAI gpt-live-1", ""), ("Gemini Live API", ""), ("ElevenLabs Agents", ""), ("Azure Voice Live", "")],
         []),
        ("violet", t("Музыка и шумы", "Music and SFX"), t("текст → музыка, шумы", "text → music, effects"),
         [("Suno v6", ""), ("Lyria 3.5", ""), ("ElevenLabs Music / SFX", "")],
         [("Stable Audio 3.0", t("частично", "partly")), ("MusicGen", "CC-BY-NC")]),
    ]
    cells = ""
    for k, h, sub, closed, open_ in rows:
        chips = "".join(f'<span class="mchip">{n}</span>' for n, _ in closed)
        chips += "".join(f'<span class="mchip ow">{n}<small>{lic}</small></span>' for n, lic in open_)
        cells += f'<div class="task-h" style="--k:var(--{k})">{h}<small>{sub}</small></div><div class="ms">{chips}</div>'
    return dict(min=3, html=f'''
  {head(t("Рынок • октябрь 2026", "Market • October 2026"), t("Аудиомодели по задачам: коммерческие и открытые", "Audio models by task: commercial and open-weight"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div class="mk">{cells}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;flex:none;margin-top:18px;">
      <div class="note" style="--k:var(--green)">{t("<b>Точность распознавания (английский):</b> лучшие коммерческие ≈ 4–5% ошибок в словах, лучшие открытые ≈ 5–6%, Whisper large-v3 ≈ 7,8%. Open ASR Leaderboard, 09.10.2026.", "<b>Transcription accuracy (English):</b> best commercial ≈ 4–5% word error rate, best open ≈ 5–6%, Whisper large-v3 ≈ 7.8%. Open ASR Leaderboard, 09.10.2026.")}</div>
      <div class="note" style="--k:var(--amber)">{t("<b>Срок жизни моделей короткий:</b> OpenAI отключает whisper-1 и gpt-4o-transcribe 26.02.2027. Имя модели держим в настройке, не в коде.", "<b>Model lifetimes are short:</b> OpenAI shuts down whisper-1 and gpt-4o-transcribe on 26.02.2027. Keep the model name in config, not in code.")}</div>
    </div>
    <div class="small" style="margin-top:8px;">{t("Зелёная рамка: открытые веса и лицензия. Списки не рейтинг. Источники и даты: L06_08.", "Green border: open weights and licence. Lists are not rankings. Sources and dates: L06_08.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Карта по четырём задачам. Слева коммерческие модели, в зелёной рамке открытые, с лицензией. Что изменилось за год: у OpenAI новое поколение распознавания (gpt-transcribe) и голосовых моделей (gpt-realtime-2.1, gpt-live-1), у ElevenLabs v4, у Google Gemini 3.8 TTS и музыка Lyria 3.5, у Suno v6.",
                      "⏱ 3 min. A map by the four tasks. Commercial models on the left, open-weight ones in a green border with their licence. What changed in a year: OpenAI has a new generation of transcription (gpt-transcribe) and voice models (gpt-realtime-2.1, gpt-live-1), ElevenLabs has v4, Google has Gemini 3.8 TTS and Lyria 3.5 music, Suno has v6."),
                    t("Точность распознавания: на открытом рейтинге Hugging Face Open ASR Leaderboard (обновлён 09.10.2026) лучшие коммерческие системы дают около 4–5% ошибок в словах на английском, лучшие открытые около 5–6%, Whisper large-v3 около 7,8%. На русском и на шумной записи цифры хуже; проверяйте на своих данных.",
                      "Accuracy: on the Hugging Face Open ASR Leaderboard (updated 09.10.2026) the best commercial systems are around 4–5% English word error rate, the best open ones around 5–6%, Whisper large-v3 around 7.8%. Other languages and noisy recordings score worse; test on your own data."),
                    t("И про срок жизни: OpenAI уже объявила отключение whisper-1 и gpt-4o-transcribe 26 февраля 2027. Поэтому имя модели выносим в настройки. Названия моделей меняются каждые несколько месяцев; перепроверьте перед занятием.",
                      "On lifetimes: OpenAI has announced that whisper-1 and gpt-4o-transcribe shut down on 26 February 2027. So keep the model name in configuration. Model names change every few months; recheck before class.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут на кофе и отдых для ушей", "5 minutes for coffee and resting your ears")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: код, стоимость, приёмка, риски и домашнее задание.", "Next: code, cost, acceptance, risks and homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт». Только отдых, без заданий в чате.", "⏱ 5 min. Press “Start”. Rest only, no chat tasks.")))


def s_code():
    code = (
        '<span class="kw">import</span> wave\n'
        '<span class="kw">from</span> google <span class="kw">import</span> genai\n'
        '<span class="kw">from</span> google.genai <span class="kw">import</span> types\n\n'
        f'client = genai.<span class="fn">Client</span>()  <span class="cm"># {t("ключ из GEMINI_API_KEY", "key from GEMINI_API_KEY")}</span>\n'
        'r = client.models.<span class="fn">generate_content</span>(\n'
        '    model=<span class="str">"gemini-3.8-flash-tts"</span>,\n'
        '    contents=<span class="str">"Say calmly: Six forty-two. Order four one seven."</span>,\n'
        '    config=types.<span class="fn">GenerateContentConfig</span>(\n'
        '        response_modalities=[<span class="str">"AUDIO"</span>],\n'
        '        speech_config=types.<span class="fn">SpeechConfig</span>(\n'
        '            voice_config=types.<span class="fn">VoiceConfig</span>(\n'
        '                prebuilt_voice_config=types.<span class="fn">PrebuiltVoiceConfig</span>(\n'
        '                    voice_name=<span class="str">"Kore"</span>)))))\n'
        'pcm = r.candidates[0].content.parts[0].inline_data.data\n'
        '<span class="kw">with</span> wave.<span class="fn">open</span>(<span class="str">"line1.wav"</span>, <span class="str">"wb"</span>) <span class="kw">as</span> f:\n'
        '    f.<span class="fn">setnchannels</span>(1); f.<span class="fn">setsampwidth</span>(2)\n'
        '    f.<span class="fn">setframerate</span>(24000); f.<span class="fn">writeframes</span>(pcm)')
    stt = ('<span class="kw">from</span> faster_whisper <span class="kw">import</span> WhisperModel\n'
           'segs, _ = <span class="fn">WhisperModel</span>(<span class="str">"small"</span>).<span class="fn">transcribe</span>(<span class="str">"mix.wav"</span>)\n'
           '<span class="fn">print</span>(<span class="str">" "</span>.<span class="fn">join</span>(s.text <span class="kw">for</span> s <span class="kw">in</span> segs))')
    return dict(min=3, html=f'''
  {head(t("Для справки • google-genai + Whisper", "Reference • google-genai + Whisper"), t("Синтез через Gemini API и проверка через Whisper", "Gemini API text-to-speech and a Whisper check"), k="violet")}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:36px;align-items:center;">
      <pre class="code" style="font-size:18px;line-height:1.5;padding:18px 22px;">{code}</pre>
      <div class="stack" style="gap:20px;">
        <div class="note" style="--k:var(--cyan)">{t("<b>Синтез:</b> тот же вызов, что в L03, но ответ — звук: 16-бит, 24 кГц, моно. Стиль голоса пишется прямо в тексте запроса.", "<b>Synthesis:</b> the same call as in L03, but the response is audio: 16-bit, 24 kHz, mono. The voice style goes into the request text.")}</div>
        <div><div class="prompt-label">{t("Проверка, локально и бесплатно", "Check, local and free")}</div><pre class="code" style="font-size:16px;padding:14px 16px;white-space:pre-wrap;">{stt}</pre></div>
        <div class="small">{t("Gemini API, октябрь 2026. Полный пайплайн урока: <code>deck_v2/make_audio.py</code>.", "Gemini API, October 2026. The full lesson pipeline: <code>deck_v2/make_audio.py</code>.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Слайд для справки, построчно не разбираем. Слева синтез речи через библиотеку google-genai, ту же, что в L03: обычный generate_content, но просим ответ в виде звука и указываем готовый голос. Ответ — сырые отсчёты 16 бит, 24 кГц, моно; заворачиваем их в WAV.",
                      "⏱ 3 min. A reference slide; do not go line by line. Left: text-to-speech with the google-genai library from L03. A normal generate_content call, but we ask for an audio response and name a prebuilt voice. The response is raw 16-bit, 24 kHz mono samples; we wrap them in a WAV file."),
                    t("Справа проверка: открытый Whisper через библиотеку faster-whisper, три строки, работает на ноутбуке без интернета. Весь пайплайн нашего примера (голос, сведение, проверка) лежит в make_audio.py рядом с презентацией.",
                      "Right: the check with the open Whisper model through the faster-whisper library, three lines, runs on a laptop offline. The full pipeline of our example (voice, mix, check) is in make_audio.py next to the deck."),
                    t("Перед занятием проверьте имя модели синтеза в документации Gemini API: модели переименовываются часто.",
                      "Before class, check the speech model ID in the Gemini API docs: models get renamed often.")))


def s_econ():
    # (task, model, where, $ per minute, billed as)
    rows = [
        (t("Синтез", "TTS"), "Gemini 3.8 Flash TTS", t("$9 / 1 млн аудиотокенов", "$9 / 1M audio tokens"), 0.0135),
        (t("Синтез", "TTS"), "OpenAI tts-1", t("$15 / 1 млн символов", "$15 / 1M characters"), 0.015),
        (t("Синтез", "TTS"), "ElevenLabs v3 / v4", t("$0.08 / 1000 символов", "$0.08 / 1K characters"), 0.08),
        (t("Распознавание", "STT"), "OpenAI gpt-transcribe", t("$0.0045 / мин", "$0.0045 / min"), 0.0045),
        (t("Распознавание", "STT"), "ElevenLabs Scribe v2", t("$0.22 / час", "$0.22 / hour"), 0.22 / 60),
        (t("Речь в речь", "Speech-to-speech"), "OpenAI gpt-live-1", t("$0.05 / мин + модель", "$0.05 / min + model"), 0.05),
        (t("Речь в речь", "Speech-to-speech"), "ElevenLabs Agents", t("$0.08 / мин", "$0.08 / min"), 0.08),
        (t("Музыка", "Music"), "ElevenLabs Music", t("$0.15 / мин", "$0.15 / min"), 0.15),
    ]

    def money(v):
        if v >= 0.1:
            return f"${v:,.2f}"
        if v >= 0.01:
            return f"${v:.3f}".rstrip("0")
        return f"${v:.5f}".rstrip("0")
    trs = "".join(
        f'<tr><td class="m">{m}<small>{task} · {unit}</small></td><td>{money(v / 60)}</td><td>{money(v)}</td><td class="h">{money(v * 60)}</td></tr>'
        for task, m, unit, v in rows)
    _, _, chars = voice_words()
    return dict(min=5, html=f'''
  {head(t("Стоимость", "Cost"), t("Стоимость аудио: секунда, минута, час", "Audio cost: per second, per minute, per hour"), t("Пересчёт: <b>1 минута речи ≈ 1000 символов</b> (так считает ElevenLabs).", "Conversion: <b>1 minute of speech ≈ 1,000 characters</b> (ElevenLabs’ own rule)."), k="amber")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:36px;align-items:start;">
      <table class="cost tight">
        <thead><tr><th>{t("Модель · как считают", "Model · billed as")}</th><th>{t("1 с", "1 s")}</th><th>{t("1 мин", "1 min")}</th><th>{t("1 час", "1 hour")}</th></tr></thead>
        <tbody>{trs}</tbody>
      </table>
      <div class="stack" style="gap:20px;">
        <div class="stat" style="--k:var(--green)"><div class="n">{t("≈ 1 цент", "≈ 1 cent")}</div><div class="d">{t(f"озвучка нашего ролика: {chars} символов на ElevenLabs v3; у нас $0 на открытых моделях", f"voicing our video: {chars} characters on ElevenLabs v3; $0 for us on open models")}</div></div>
        <div class="stat" style="--k:var(--amber)"><div class="n">$4.80 = 12 {t("с", "s")}</div><div class="d">{t("час голоса ElevenLabs стоит как 12 секунд видео Veo 3.1 (L05: $0.40/с)", "an hour of ElevenLabs voice costs as much as 12 seconds of Veo 3.1 video (L05: $0.40/s)")}</div></div>
        <div class="note" style="--k:var(--violet)">{t("Подписки: ElevenLabs от $6/мес (30 тыс. кредитов ≈ 30 мин), Suno Pro $8/мес при оплате за год.", "Subscriptions: ElevenLabs from $6/month (30K credits ≈ 30 min), Suno Pro $8/month billed yearly.")}</div>
      </div>
    </div>
    <div class="small" style="margin-top:10px;">{t("Списочные цены на 12.10.2026. Gemini 3.8 Flash TTS: цена до 31.12.2026, с 01.01.2027 вдвое выше. Не включены: дубли, сведение, работа людей.", "List prices as of 12.10.2026. Gemini 3.8 Flash TTS: price until 31.12.2026, doubles from 01.01.2027. Not included: retakes, mixing, people’s time.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Сначала единицы. Синтез речи считают за символы текста (OpenAI tts-1, Google, ElevenLabs) или за аудиотокены (Gemini). Распознавание, голосовые агенты и музыку ElevenLabs — за минуту. Чтобы сравнивать, пересчитываем всё в секунду, минуту и час, приняв 1000 символов за минуту речи; так считает сам ElevenLabs.",
                      "⏱ 5 min. Units first. Speech synthesis is billed per character of text (OpenAI tts-1, Google, ElevenLabs) or per audio token (Gemini). Transcription, voice agents and ElevenLabs music are billed per minute. To compare, we convert everything to second, minute and hour, using 1,000 characters per minute of speech, ElevenLabs’ own rule."),
                    t("Главная мысль: звук на порядки дешевле видео. Час голоса на ElevenLabs стоит $4.80, на Gemini 3.8 Flash TTS меньше доллара. Час видео Veo 3.1 в L05 стоил $1 440. Распознавание часа записи стоит от 22 до 27 центов. Озвучка нашего ролика: около 150 символов, на ElevenLabs это примерно 1 цент.",
                      "Key point: audio is orders of magnitude cheaper than video. An hour of voice costs $4.80 on ElevenLabs and under a dollar on Gemini 3.8 Flash TTS. An hour of Veo 3.1 video in L05 cost $1,440. Transcribing an hour of recording costs 22 to 27 cents. Voicing our video: about 150 characters, roughly 1 cent on ElevenLabs."),
                    t("Где деньги реально утекают: голосовые агенты (минуты разговора плюс языковая модель за ними) и дубли озвучки. И подписки веб-студий: в ДЗ бесплатного лимита ElevenLabs (10 тыс. кредитов ≈ 10 минут) хватит, но коммерческой лицензии на бесплатном тарифе нет. Цены меняются: у Gemini 3.8 TTS цена удваивается с 1 января 2027.",
                      "Where money actually goes: voice agents (conversation minutes plus the language model behind them) and voice retakes. And web studio subscriptions: the ElevenLabs free allowance (10K credits ≈ 10 minutes) is enough for the homework, but the free plan has no commercial licence. Prices change: Gemini 3.8 TTS doubles on 1 January 2027.")))


def s_qa():
    rr = R()
    mix = rr["mix"]
    items = [
        (t("<b>Слова</b> совпадают со сценарием: распознавание + список критичных слов", "<b>Words</b> match the script: speech-to-text + critical terms list"), "red"),
        (t("<b>Произношение</b> имён, чисел, терминов: проверено на слух", "<b>Pronunciation</b> of names, numbers, terms: checked by ear"), "red" if LANG == "ru" else "green"),
        (t("<b>Тайминг:</b> реплика влезает в шот, не режется склейкой", "<b>Timing:</b> each line fits its shot and is not cut by a transition"), "green"),
        (t("<b>Сведение:</b> голос разборчив, фон приглушён, нет чужой речи", "<b>Mix:</b> voice is clear, background ducked, no stray speech"), "red" if LANG == "en" else "green"),
        (t("<b>Громкость</b> −14 LUFS ± 1, пик ≤ −1 dBTP", "<b>Loudness</b> −14 LUFS ± 1, peak ≤ −1 dBTP"), "green"),
        (t("<b>Права:</b> лицензия голоса и музыки, согласие, пометка «создано ИИ»", "<b>Rights:</b> voice and music licence, consent, “AI-generated” label"), "amber"),
    ]
    lis = "".join(f'<li><span>{h}</span></li>' for h, _ in items)
    marks = {"green": "✓", "red": "✗", "amber": "!"}
    res = "".join(f'<div style="font-size:28px;font-weight:800;color:var(--{k});height:58px;display:flex;align-items:center;">{marks[k]}</div>' for _, k in items)
    return dict(min=5, html=f'''
  {head(t("Приёмка", "Acceptance"), t("Чек-лист приёмки озвучки", "Acceptance checklist for a voice-over"), t("Проверяем на нашем ролике. Справа реальный результат этой версии.", "Applied to our video. On the right, the real result for this version."), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:40px;align-items:center;">
      <div class="row" style="grid-template-columns:1fr 50px;gap:10px;flex:none;align-items:start;">
        <ol class="checklist" style="gap:0">{lis.replace("<li>", '<li style="height:58px;align-items:center;font-size:23px">')}</ol>
        <div class="stack" style="gap:0">{res}</div>
      </div>
      <div class="stack" style="gap:22px;">
        <div class="stat" style="--k:var(--green)"><div class="n">{num(mix["lufs"])} LUFS</div><div class="d">{t(f"пик {num(mix['true_peak_dbfs'])} dBTP; измерено ffmpeg (фильтр ebur128)", f"peak {num(mix['true_peak_dbfs'])} dBTP; measured with ffmpeg (ebur128 filter)")}</div></div>
        <div class="note" style="--k:var(--red)">{t("<b>Не принято:</b> «Анна» и «шесть» читаются неверно. Исправление: другой голос, затем повторить пункты 1–2.", "<b>Rejected:</b> Veo’s line “Here’s your order” leaks into the start. Fix: mute shot 1 audio for 0–3 s, then repeat item 1.")}</div>
        <div class="note" style="--k:var(--green)">{t("Этот же чек-лист — <b>рубрика ДЗ</b>.", "The same checklist is the <b>homework rubric</b>.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Шесть пунктов приёмки. Первый: слова совпадают со сценарием, проверяем распознаванием и списком критичных слов. Второй: произношение имён, чисел и терминов, только на слух. Третий: тайминг, реплика влезает в шот. Четвёртый: сведение, голос разборчив, фон приглушён, нет посторонней речи. Пятый: громкость −14 LUFS плюс-минус 1 и пик не выше −1 dBTP. Шестой: права, то есть лицензия голоса и музыки, согласие владельца голоса и пометка «создано ИИ».",
                      "⏱ 5 min. Six acceptance items. One: the words match the script, checked with speech-to-text and the critical terms list. Two: pronunciation of names, numbers and terms, by ear only. Three: timing, each line fits its shot. Four: mix, the voice is clear, the background is ducked, no stray speech. Five: loudness −14 LUFS plus or minus 1 and a peak no higher than −1 dBTP. Six: rights, meaning the voice and music licence, the voice owner’s consent and an “AI-generated” label."),
                    t("Справа честный результат. Громкость и пик проходят. Русская версия не принята: голос портит «Анна» и «шесть сорок две». Английская тоже не принята: в начале слышна реплика, которую придумал Veo. Пункт 6 с восклицательным знаком: MusicGen некоммерческий, для урока можно, для клиента нет.",
                      "On the right is the honest result. Loudness and peak pass. The Russian version is rejected: the voice breaks “Анна” and “шесть сорок две”. The English version is rejected too: Veo’s invented line is audible at the start. Item 6 has an exclamation mark: MusicGen is non-commercial; fine for a lesson, not for a client."),
                    t("Этот же чек-лист — рубрика домашнего задания. Оценивается разбор ошибок, а не идеальный звук.",
                      "The same checklist is the homework rubric. Grading is based on the error analysis, not on perfect sound.")))


def s_risks():
    return dict(min=4, html=f'''
  {head(t("Риски", "Risks"), t("Риски и согласие на голос: клонирование, маркировка, закон", "Risks and voice consent: cloning, labelling, law"), k="red")}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:1fr 1.2fr;gap:40px;align-items:start;flex:none;">
      <div class="light" style="gap:16px">
        <div class="lrow" style="--k:var(--green)"><div class="dot"></div><div><div class="h">{t("Готовый или придуманный голос", "Library or designed voice")}</div><div class="d">{t("можно, по лицензии сервиса, с пометкой «создано ИИ»", "allowed under the service licence, with an “AI-generated” label")}</div></div></div>
        <div class="lrow" style="--k:var(--amber)"><div class="dot"></div><div><div class="h">{t("Свой голос, клон коллеги", "Your own voice, a colleague’s clone")}</div><div class="d">{t("письменное согласие: для чего, где, как долго, как отозвать", "written consent: purpose, where, how long, how to withdraw")}</div></div></div>
        <div class="lrow" style="--k:var(--red)"><div class="dot"></div><div><div class="h">{t("Голос клиента, руководителя, публичного лица", "A client’s, manager’s or public figure’s voice")}</div><div class="d">{t("нельзя без письменного согласия и юристов; голосом обманывают", "not without written consent and legal review; voices are used for fraud")}</div></div></div>
      </div>
      <div class="stack" style="gap:14px;">
        <div class="prompt-label">{t("Как сервисы проверяют согласие на клон", "How services check consent for a clone")}</div>
        <ul class="list">
          <li>{t("<b>OpenAI, Google:</b> владелец голоса записывает фиксированную фразу согласия.", "<b>OpenAI, Google:</b> the voice owner records a fixed consent phrase.")}</li>
          <li>{t("<b>ElevenLabs Professional:</b> владелец читает проверочный текст; Instant: только галочка.", "<b>ElevenLabs Professional:</b> the owner reads a verification text aloud; Instant: a checkbox only.")}</li>
          <li>{t("<b>Azure:</b> доступ к клонам только по заявке, запись согласия сверяют с голосом.", "<b>Azure:</b> clones by application only; the consent recording is matched to the voice.")}</li>
          <li>{t("<b>Открытые модели</b> (Qwen3-TTS, Chatterbox): клон по 3–10 с, <b>без проверок</b>.", "<b>Open models</b> (Qwen3-TTS, Chatterbox): clone from 3–10 s, <b>no checks at all</b>.")}</li>
        </ul>
      </div>
    </div>
    <div class="plaque" style="margin-top:28px;font-size:21px;"><b>EU AI Act, {t("ст. 50", "Art. 50")}:</b> {t("с 2 августа 2026 синтетический звук и дипфейки нужно помечать; штраф до €15 млн или 3% оборота. <b>OpenAI</b> требует сообщать слушателю, что голос сгенерирован. <b>Google</b> ставит невидимую метку SynthID во весь сгенерированный звук.", "from 2 August 2026, synthetic audio and deepfakes must be labelled; fines up to €15M or 3% of turnover. <b>OpenAI</b> requires telling listeners the voice is AI-generated. <b>Google</b> embeds an invisible SynthID mark in all generated audio.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Слева светофор для голоса. Зелёный: готовый голос из библиотеки или придуманный по описанию, по лицензии сервиса и с пометкой «создано ИИ». Жёлтый: ваш собственный голос или клон коллеги, только с письменным согласием, где сказано, для чего, где, как долго и как отозвать согласие. Красный: голос клиента, руководителя, публичного человека; без письменного согласия и юристов нельзя. Голосовые клоны используют для мошенничества: звонок «от директора» с просьбой срочно перевести деньги.",
                      "⏱ 4 min. On the left is a traffic light for voices. Green: a library voice or one designed from a description, under the service licence and with an “AI-generated” label. Amber: your own voice or a colleague’s clone, only with written consent that says the purpose, where, how long and how to withdraw. Red: a client’s, a manager’s or a public figure’s voice; not without written consent and legal review. Voice clones are used for fraud: a call “from the CEO” asking for an urgent transfer."),
                    t("Справа как сервисы проверяют согласие. OpenAI и Google требуют записать фиксированную фразу согласия голосом владельца, и доступ к клонам у них ограничен. ElevenLabs для профессионального клона просит владельца прочитать проверочный текст, для быстрого клона только галочку «у меня есть согласие». Azure выдаёт клоны по заявке и может сверить запись согласия с голосом. Открытые модели клонируют по нескольким секундам записи и ничего не проверяют. Значит, проверка согласия — ваша ответственность, а не сервиса.",
                      "On the right: how services check consent. OpenAI and Google require the voice owner to record a fixed consent phrase, and clone access is limited. ElevenLabs asks the owner to read a verification text for a professional clone, and only a checkbox for an instant clone. Azure grants clones on application and may match the consent recording to the voice. Open models clone from a few seconds and check nothing. So checking consent is your responsibility, not the service’s."),
                    t("Закон: статья 50 EU AI Act применяется с 2 августа 2026: синтетический звук и дипфейки нужно помечать, штраф до €15 млн или 3% оборота. OpenAI в правилах использования требует явно сообщать слушателю, что голос сгенерирован. Google ставит SynthID во весь звук своих моделей (Lyria, синтез речи Gemini), проверить можно в Gemini app, но только для контента Google. В США с февраля 2024 голоса ИИ в автоматических звонках считаются «искусственными» по закону о телефонных звонках TCPA (решение FCC). Мошенничество реально: по сообщениям прессы, в 2026 году итальянский банк Fideuram перевёл около €95 млн после звонка с клонированным голосом юриста.",
                      "Law: Article 50 of the EU AI Act applies from 2 August 2026: synthetic audio and deepfakes must be labelled, with fines up to €15M or 3% of turnover. OpenAI’s usage policies require a clear disclosure to listeners that the voice is AI-generated. Google embeds SynthID in all audio from its models (Lyria, Gemini speech); the Gemini app can check it, but only for Google content. In the US, since February 2024 AI voices in robocalls count as “artificial” under the TCPA telephone law (FCC ruling). The fraud risk is real: according to press reports, in 2026 the Italian bank Fideuram wired about €95M after a call with a cloned lawyer’s voice.")))


def s_hw():
    return dict(min=7, html=f'''
  {head(t("Практика", "Practice"), t("Домашнее задание 6: озвучить свой ролик из L05", "Homework 6: voice your L05 video"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:44px;align-items:center;">
      <div class="stack" style="gap:18px;">
        <div class="track" style="--k:var(--cyan)"><img src="{IMG}poster_final.jpg" alt=""><div><div class="h">{t("Ваш ролик из L05", "Your L05 video")}</div><div class="d">{t("Трек А (товар) или Б (курьер). Нет ролика: возьмите курьерский ролик урока.", "Track A (product) or B (courier). No video? Use the lesson’s courier video.")}</div></div></div>
        <div class="files">genai-homeworks/L06/
├── script.md      <span class="cm"># {t("текст, текст для голоса, время", "text, spoken text, timing")}</span>
├── audio/         <span class="cm"># {t("реплики, подложка, mix", "lines, bed, mix")}</span>
├── final_voiced.mp4
├── transcript.txt <span class="cm"># {t("распознанный текст", "speech-to-text output")}</span>
├── audio_spec.md
└── audio_qa.md</div>
      </div>
      <div class="stack" style="gap:14px;">
        <ol class="checklist">
          <li style="font-size:21px"><span>{t("<b>Сценарий</b> на 3 реплики с бюджетом слов → <code>script.md</code>", "<b>Script</b>, 3 lines with a word budget → <code>script.md</code>")}</span></li>
          <li style="font-size:21px"><span>{t("<b>Голос</b> в двух сервисах (веб-студия + API или открытая модель), выбрать один", "<b>Voice</b> in two services (web studio + API or open model), pick one")}</span></li>
          <li style="font-size:21px"><span>{t("<b>Фон:</b> звук видеомодели, шумы или музыка, с лицензией", "<b>Background:</b> video model audio, effects or music, with its licence")}</span></li>
          <li style="font-size:21px"><span>{t("<b>Сведение</b> в <code>final_voiced.mp4</code>, −14 LUFS ± 1", "<b>Mix</b> into <code>final_voiced.mp4</code>, −14 LUFS ± 1")}</span></li>
          <li style="font-size:21px"><span>{t("<b>Проверка</b> распознаванием → <code>transcript.txt</code>; приёмка по слайду 18 → <code>audio_qa.md</code>; стоимость → <code>audio_spec.md</code>", "<b>Check</b> with speech-to-text → <code>transcript.txt</code>; slide 18 review → <code>audio_qa.md</code>; cost → <code>audio_spec.md</code>")}</span></li>
        </ol>
        <div class="small" style="font-size:18px">{t("Ревьюер: <b>ihar_rubanovich@epam.com</b>. Только свой голос или голоса из библиотек; чужие голоса не клонируем.", "Reviewer: <b>ihar_rubanovich@epam.com</b>. Your own voice or library voices only; do not clone anyone else’s voice.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. ДЗ повторяет пайплайн урока на вашем ролике из L05. Трек А — товар, трек Б — курьер. Если ролика нет, возьмите курьерский ролик урока из папки L05.",
                      "⏱ 7 min. The homework repeats the lesson pipeline on your L05 video. Track A: product, track B: courier. If you have no video, use the lesson’s courier video from the L05 folder."),
                    t("Порядок: сценарий на 3 реплики с бюджетом слов и колонкой «текст для голоса»; голос в двух сервисах, например ElevenLabs и Gemini API или открытая модель, выбрать лучший по чек-листу; фон: звук видеомодели, шумы или музыка, и указать лицензию; сведение в final_voiced.mp4 на −14 LUFS плюс-минус 1; прогнать итог через распознавание речи и сохранить transcript.txt; приёмка по чек-листу слайда 18 в audio_qa.md; сервисы, настройки и стоимость в audio_spec.md.",
                      "Order: a 3-line script with a word budget and a spoken-text column; the voice in two services, for example ElevenLabs and the Gemini API or an open model, keep the better one by the checklist; a background: the video model’s audio, effects or music, with its licence; a mix into final_voiced.mp4 at −14 LUFS plus or minus 1; run the result through speech-to-text and save transcript.txt; the slide 18 checklist in audio_qa.md; services, settings and cost in audio_spec.md."),
                    t("Правило согласия: только свой голос или голоса из библиотек. Голоса коллег, родственников и знаменитостей не клонируем даже «для теста». Оценивается разбор ошибок, а не идеальный звук. Подробности и шаблоны в файле ДЗ L06.",
                      "Consent rule: your own voice or library voices only. Do not clone colleagues, relatives or celebrities, not even “for a test”. Grading is based on the error analysis, not on perfect sound. Details and templates are in the L06 homework file.")))


def s_summary():
    rules = [
        ("cyan", t("Сначала сценарий с бюджетом слов", "Script with a word budget first"), t("2–2,5 слова в секунду; не влезает — сокращаем текст", "2–2.5 words per second; if it does not fit, cut the text")),
        ("green", t("Текст для голоса отдельно от текста для зрителя", "Spoken text separate from on-screen text"), t("числа, время, имена словами; стиль инструкцией", "numbers, times, names as words; style as an instruction")),
        ("amber", t("Голос с лицензией и согласием", "A voice with a licence and consent"), t("клон только с письменного согласия владельца", "a clone only with the owner’s written consent")),
        ("violet", t("Сведение к −14 LUFS", "Mix to −14 LUFS"), t("голос сверху, фон приглушён, пик ≤ −1 dBTP", "voice on top, background ducked, peak ≤ −1 dBTP")),
        ("red", t("Проверка распознаванием и на слух", "Check with speech-to-text and by ear"), t("частота ошибок + критичные слова", "word error rate + critical terms")),
    ]
    rr = "".join(f'<div class="rule" style="--k:var(--{k})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>'
                 for i, (k, h, d) in enumerate(rules))
    return dict(min=3, html=f'''
  {head(t("Итоги", "Summary"), t("Итоги урока", "Lesson summary"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.4fr 1fr;gap:56px;align-items:center;">
      <div class="rules" style="gap:24px">{rr}</div>
      <div class="stack" style="gap:16px;">
        <img src="{IMG}poster_final.jpg" alt="" style="width:100%;border-radius:12px;border:1px solid var(--line)">
        <div class="note" style="--k:var(--violet)"><b>{t("Урок 07: GitHub, Microsoft 365 и Copilot.", "Lesson 07: GitHub, Microsoft 365 and Copilot.")}</b> {t("Из генерации контента переходим к ИИ в рабочих инструментах.", "From generating content to AI inside everyday work tools.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Пять правил одной строкой: сценарий с бюджетом слов; текст для голоса отдельно, числа и имена словами; голос с лицензией и согласием; сведение к −14 LUFS; проверка распознаванием и на слух.",
                      "⏱ 3 min. Five rules: a script with a word budget; spoken text separate, numbers and names as words; a voice with a licence and consent; mix to −14 LUFS; check with speech-to-text and by ear."),
                    t("Этим уроком закрываем модуль мультимодальности: картинка, видео, звук. Следующий урок, L07: GitHub, Microsoft 365 и Copilot. Вопросы.",
                      "This closes the multimodality module: image, video, sound. Next lesson, L07: GitHub, Microsoft 365 and Copilot. Questions.")))


SLIDES = [s_cover, s_hook, s_layers, s_tasks, s_how, s_video_audio, s_script, s_text, s_voice, s_music,
          s_mix, s_check, s_arch, s_market, s_break, s_code, s_econ, s_qa, s_risks, s_hw, s_summary]


# ---------------------------------------------------------------- page
def build(lang):
    global LANG
    LANG = lang
    css = (HERE / "style.css").read_text(encoding="utf-8")
    js = (HERE / "deck.js").read_text(encoding="utf-8")
    total = len(SLIDES)
    secs, minutes = [], 0
    for i, fn in enumerate(SLIDES, 1):
        s = fn()
        minutes += s["min"]
        cls = ("slide " + s.get("cls", "")).strip()
        foot = "" if s.get("cls") == "cover" else f'\n  <div class="foot"><span>{FOOT[lang]}</span><span>{i:02d} / {total}</span></div>'
        secs.append(f'<!-- SLIDE {i:02d} · {fn.__name__} · {s["min"]} min -->\n<section class="{cls}" data-n="{i}">{s["html"]}{foot}\n'
                    f'  <template class="notes">{s["notes"]}</template>\n</section>')
    assert minutes == 90, minutes
    assert total == 21 and SLIDES[14] is s_break and SLIDES[19] is s_hw
    title = t("Урок 06: Речь и аудио | GenAI Basics", "Lesson 06: Speech and Audio AI | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<!-- generated by deck_v2/build.py — edit the generator, not this file -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
{css}</style>
</head>
<body>
<main class="stage" id="stage">

{chr(10).join(secs)}

</main>

<aside class="drawer" id="drawer"><div class="hd"></div><div class="tx"></div></aside>
<div class="grid" id="grid"></div>

<script>
const T = {tconst};
{js}</script>
</body>
</html>
'''
    OUT[lang].write_text(html, encoding="utf-8")
    print(f"{lang}: {OUT[lang].name} — {total} slides, {minutes} min")
    return OUT[lang]


EDGE = next((c for c in [shutil.which("msedge"),
                         r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                         r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"] if c and Path(c).exists()), None)


def pdf(html):
    out = html.with_suffix(".pdf")
    prof = tempfile.mkdtemp(prefix="edgepdf_")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=10000",
                    f"--user-data-dir={prof}", f"--print-to-pdf={out}", html.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    shutil.rmtree(prof, ignore_errors=True)
    print("pdf:", out.name, f"{out.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    for lg in ("ru", "en"):
        h = build(lg)
        if "--no-pdf" not in sys.argv:
            pdf(h)
