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
_CL = L06 / "demo_courier_audio" / "clone_report.json"
CLONE = json.loads(_CL.read_text(encoding="utf-8")) if _CL.exists() else None

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


def steps(cur=0):
    """The 6-step pipeline strip; the current step is highlighted."""
    names = [t("Сценарий", "Script"), t("Текст для голоса", "Spoken text"), t("Голос", "Voice"),
             t("Шумы и музыка", "Effects and music"), t("Сведение", "Mix"), t("Проверка", "Check")]
    return '<div class="steps">' + "".join(
        f'<span class="{"on" if i == cur else ""}"><i>{i}</i>{n}</span>' for i, n in enumerate(names, 1)) + "</div>"


def head(kicker, title, lead=None, k=None):
    import re
    m = re.match(r"(?:Шаг|Step) (\d)", kicker)
    ks = f' style="--k:var(--{k})"' if k else ""
    top = steps(int(m.group(1))) if m else f'<div class="kicker"{ks}>{kicker}</div>'
    s = f'{top}\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


TEAMS = {
    "ru": "Teams: в этом уроке звук обязателен. В окне «Поделиться» включите «Включить звук» (Include sound; в старых версиях Include computer sound). Перед стартом проверьте звук на одном клипе.",
    "en": "Teams: this lesson needs sound. In Share, turn on “Include sound” (older versions: “Include computer sound”). Test the sound on one clip before you start.",
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
    <h1>{t("Речь и аудио", "Speech and Audio")}</h1>
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
        <div class="stat" style="--k:var(--cyan)"><div class="n">3 {t("реплики", "lines")}</div><div class="d">{t(f"{num(secs)} с речи; голос из <b>открытой модели</b> синтеза речи (скачивается и работает локально) на обычном ноутбуке", f"{num(secs)} s of speech from an <b>open-weight</b> text-to-speech model (downloadable, runs locally) on an ordinary laptop")}</div></div>
        <div class="stat" style="--k:var(--green)"><div class="n">3 {t("дорожки", "tracks")}</div><div class="d">{t("голос + звук, который Veo сгенерировал вместе с видео + музыка", "voice + the sound Veo generated with the video + music")}</div></div>
        <div class="stat" style="--k:var(--amber)"><div class="n">{num(mix["lufs"])} LUFS</div><div class="d">{t("громкость в единицах Loudness Units relative to Full Scale (LUFS), как её слышит ухо: 0 = максимум, −14 = норма стриминговых сервисов, −23 = ТВ", "loudness in Loudness Units relative to Full Scale (LUFS), as the ear hears it: 0 = maximum, −14 = streaming norm, −23 = TV")}</div></div>
      </div>
    </div>
    <div style="margin-top:26px;display:flex;align-items:center;gap:18px;"><div class="prompt-label" style="margin:0">{t("Пайплайн урока", "Lesson pipeline")}</div><div class="steps big" style="margin:0">{steps().replace('<div class="steps">', '').replace('</div>', '')}</div></div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Запустите ролик кликом, со звуком (23 секунды). Это тот же ролик из L05: три шота Veo 3.1. Спросите в чат: что вы слышите, сколько слоёв звука?",
                      "⏱ 3 min. Start the clip with a click, with sound (23 seconds). It is the same L05 video: three Veo 3.1 shots. Ask the chat: what do you hear, how many layers of sound?"),
                    t(f"Ответ: три слоя. Голос диктора: три реплики, {num(secs)} секунды речи, сделаны открытой моделью синтеза речи прямо на ноутбуке (Kokoro для английского, Piper для русского). Звук, который Veo сгенерировал вместе с видео: кафе, дождь. И музыкальная подложка из открытой модели MusicGen. Всё сведено к громкости −14 LUFS (Loudness Units relative to Full Scale, единицы громкости): это уровень, к которому Spotify приводит треки.",
                      f"Answer: three layers. The narrator: three lines, {num(secs)} seconds of speech from an open-weight text-to-speech model running on a laptop (Kokoro for English, Piper for Russian). The sound Veo generated with the video: cafe, rain. And a music bed from the open MusicGen model. Everything is mixed to −14 LUFS (Loudness Units relative to Full Scale, a loudness measure), the level Spotify normalises tracks to."),
                    t("Результат не идеален: и в уроке мы найдём ошибки этой озвучки с помощью распознавания речи. Это и есть главный навык сегодня: сделать и проверить.",
                      "The result is not perfect: later in the lesson we find its errors with speech-to-text. That is today’s main skill: produce, then check."),
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
    c2 = col("green", t("Веб-студии", "Web studios"), t("интерфейс для звука", "dedicated audio interface"),
             ["ElevenLabs", "Suno", "Google AI Studio"],
             t("библиотека голосов, настройки, звуковые эффекты, музыка, дубляж", "voice library, settings, sound effects, music, dubbing"),
             t("кредиты; бесплатный лимит небольшой", "credits; small free allowance"), t("озвучка ролика, домашнее задание", "voicing a video, homework"), "ElevenLabs")
    c3 = col("violet", "API", t("код и автоматизация", "code and automation"),
             ["OpenAI Audio", "Gemini API", "Google Cloud / Azure Speech", "ElevenLabs API", "Deepgram / AssemblyAI"],
             t("всё как параметры запроса; пакетная обработка, живой звук", "everything as request parameters; batch jobs, live audio"),
             t("за символ, токен или минуту", "per character, token or minute"), t("пайплайны, продукты, агенты", "pipelines, products, agents"), "Gemini API")
    return dict(min=4, html=f'''
  {head(t("Где генерировать", "Where to generate"), t("Три уровня доступа к аудиомоделям: чат, веб-студия, программный интерфейс (API)", "Three access layers for audio models: chat app, web studio, application programming interface (API)"), k="cyan")}
  <div class="body" style="margin-top:16px;">
    <div class="layers">{c1}{c2}{c3}</div>
    <div class="note" style="margin-top:20px;--k:var(--green)">{t("<b>Четвёртый путь: открытые модели</b> (файлы модели скачиваются и запускаются на своём компьютере). Whisper (распознавание), Kokoro и Piper (синтез речи), MusicGen (музыка). $0 за минуту, но железо, установка и лицензии на вас. Наш пример сделан так.", "<b>A fourth path: open-weight models</b> (model files you download and run on your own machine). Whisper (speech recognition), Kokoro and Piper (speech synthesis), MusicGen (music). $0 per minute, but hardware, setup and licences are yours. Our example was made this way.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Та же схема, что в L04 и L05. Чат-приложения: голосовой режим ChatGPT, Gemini app с Gemini Live, и в Gemini app с сентября 2026 есть музыка на модели Lyria 3.5. Удобно попробовать, но голос, темп и длину почти не настроить.",
                      "⏱ 4 min. Same structure as in L04 and L05. Chat apps: ChatGPT voice mode, the Gemini app with Gemini Live; since September 2026 the Gemini app also makes music with Lyria 3.5. Good for trying things, but you barely control the voice, pace and length."),
                    t("Веб-студии: ElevenLabs (голоса, клонирование, звуковые эффекты, музыка, дубляж), Suno (песни), Google AI Studio (площадка для синтеза речи и музыки Gemini). Здесь делается домашнее задание.",
                      "Web studios: ElevenLabs (voices, cloning, sound effects, music, dubbing), Suno (songs), Google AI Studio (playground for Gemini speech and music). This is where the homework happens."),
                    t("Программные интерфейсы, API: OpenAI (синтез, распознавание, Realtime), Gemini API (синтез речи, Live, Lyria), Google Cloud и Azure Speech, ElevenLabs API, Deepgram и AssemblyAI для распознавания. Оплата за символ текста, за аудиотокен или за минуту звука; сравним на слайде стоимости.",
                      "Application programming interfaces (APIs): OpenAI (speech synthesis, transcription, Realtime), Gemini API (speech generation, Live, Lyria), Google Cloud and Azure Speech, ElevenLabs API, Deepgram and AssemblyAI for transcription. Billed per character of text, per audio token or per minute of audio; we compare them on the cost slide."),
                    t("Открытые модели: наш пример целиком сделан ими на ноутбуке без видеокарты. Это бесплатно за минуту, но у каждой модели своя лицензия; MusicGen, например, только для некоммерческого использования.",
                      "Open weights: our whole example was made with them on a laptop without a graphics card. Free per minute, but each model has its own licence; MusicGen, for example, is non-commercial only.")))


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
      {task("amber", t("голос", "voice"), t("голос", "voice"), t("Речь в речь (speech-to-speech)", "Speech-to-speech"), t("голосовые агенты, синхронный перевод, дубляж. Отвечает в реальном времени.", "voice agents, live translation, dubbing. Replies in real time."))}
      {task("violet", t("текст", "text"), t("музыка, шумы", "music, effects"), t("Музыка и звуковые эффекты", "Music and sound effects (SFX)"), t("подложка, джинглы, шумы. Плюс звук, который <b>видеомодель</b> делает сама (L05).", "beds, jingles, effects. Plus the sound a <b>video model</b> makes by itself (L05)."))}
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Слова «аудио-ИИ» прячут четыре разные задачи. Смотрим на вход и выход. Текст в голос: синтез речи, сокращённо TTS. Голос в текст: распознавание речи, STT или ASR, это синонимы. Голос в голос: голосовые агенты и перевод. Текст в музыку и шумы.",
                      "⏱ 4 min. “Audio AI” hides four different tasks. Look at input and output. Text to voice: text-to-speech, TTS. Voice to text: speech-to-text, STT, also called automatic speech recognition, ASR; same thing. Voice to voice: voice agents and translation. Text to music and sound effects."),
                    t("Разные задачи решают разные модели с разными ценами: синтез считают за символы, распознавание за минуты, голосовых агентов за минуты разговора, музыку за трек.",
                      "Different tasks use different models and different prices: synthesis is billed per character, transcription per minute, voice agents per minute of conversation, music per track."),
                    t("Озвучка ролика использует три из четырёх задач: синтез речи для голоса, музыку и шумы для фона, распознавание для проверки. Голосовых агентов разберём на уровне архитектуры, их строят в модуле про агентов.",
                      "Voicing a video uses three of the four tasks: text-to-speech for the voice, music and effects for the background, speech-to-text for the check. Voice agents get one architecture slide; you build agents in module 4.")))


def s_how():
    line = R()["lines"][0]
    env = ENV["vo_" + LANG + "_fine"]
    x0, x1 = line["start"] / 23.0, (line["end"] + 0.2) / 23.0
    return dict(min=4, html=f'''
  {head(t("Принцип работы", "How it works"), t("Как модель синтеза речи превращает текст в звук", "How a text-to-speech model turns text into sound"), k="violet")}
  <div class="body">
    <div class="flow" style="--k:var(--violet);justify-content:center;gap:16px;">
      <div class="box">{t("Текст", "Text")}<small>{t("«", "“")}{line["spoken"].split(".")[0]}.{t("»", "”")}</small></div><div class="arr">→</div>
      <div class="box hl">{t("Модель", "Model")}<small>{t("предсказывает аудиотокены", "predicts audio tokens")}</small></div><div class="arr">→</div>
      <div class="box">{t("Аудиотокены", "Audio tokens")}<small>{t("12–50 в секунду", "12–50 per second")}</small></div><div class="arr">→</div>
      <div class="box hl">{t("Декодер", "Decoder")}<small>{t("токены → отсчёты", "tokens → samples")}</small></div><div class="arr">→</div>
      <div class="box">{t("Звук", "Sound")}<small>{t("24 000–48 000 чисел в секунду", "24,000–48,000 numbers per second")}</small></div>
    </div>
    <div style="margin-top:30px;">
      <div class="prompt-label">{t("Реплика 1 нашего сценария, реальная форма волны", "Line 1 of our script, real waveform")} · {num(line["end"] - line["start"])} {t("с", "s")}</div>
      {wave(env, h=170, w=1440, color="var(--cyan)", gain=1.0, x0=x0, x1=x1)}
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:26px;">
      <div class="note" style="--k:var(--cyan)">{t("<b>Сколько данных:</b> секунда звука в студийном качестве = 48 000 чисел (Gemini отдаёт 24 000). Модель работает со сжатым видом: Gemini считает <b>25 аудиотокенов в секунду</b>, MusicGen <b>50 шагов</b>.", "<b>How much data:</b> one second of studio-quality audio is 48,000 numbers (Gemini returns 24,000). Models work with a compressed form: Gemini bills <b>25 audio tokens per second</b>, MusicGen takes <b>50 steps</b>.")}</div>
      <div class="note" style="--k:var(--amber)">{t("<b>Чего нет внутри:</b> словаря правил чтения. Модель выучила, как текст обычно звучит. Поэтому ошибается на <b>числах, именах, сокращениях</b>.", "<b>What is not inside:</b> a rulebook for reading. The model learned how text usually sounds, so it most often errs on <b>numbers, names and abbreviations</b>.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Связь с L03 и L05: языковая модель предсказывает текстовые токены, видеомодель чистит от шума кадры. Модель синтеза речи предсказывает аудиотокены: сжатые кусочки звука. Декодер (его ещё называют вокодером) превращает их обратно в волну.",
                      "⏱ 4 min. Link to L03 and L05: a language model predicts text tokens, a video model denoises frames. A speech model predicts audio tokens, compressed chunks of sound. A decoder (also called a vocoder) turns them back into a waveform."),
                    t("Масштаб: в секунде звука 48 000 чисел при качестве 48 кГц. Модель так не работает, она видит сжатое представление. Два реальных числа: Gemini тарифицирует синтез по 25 аудиотокенов на секунду; MusicGen, которым сделана наша музыка, делает 50 шагов в секунду (по 4 токена на шаг). Внутреннее устройство моделей разное, принцип общий.",
                      "Scale: at 48 kHz one second of audio is 48,000 numbers. The model does not work at that level; it sees a compressed representation. Two real numbers: Gemini bills speech at 25 audio tokens per second; MusicGen, which made our music, takes 50 steps per second (4 tokens per step). Architectures differ; the principle is the same."),
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
        {aud("veo_trainwreck", t("Неудачный клип из L05", "The L05 failure clip"), t("в промпте тоже нет реплик", "prompt has no dialogue either"), "red", "veo_trainwreck")}
        <div class="tx" style="font-size:22px;"><small>{t("Распознано в звуке Veo", "Heard in Veo’s audio")}</small>“{tw}”</div>
      </div>
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;flex:none;margin-top:40px;">
      <div class="note" style="--k:var(--green)">{t("<b>Даёт:</b> шум улицы, дождь, шаги, синхронно с картинкой. Но платим за него: Veo 3.1 в Vertex AI со звуком $0.40/с, без звука $0.20/с.", "<b>Provides:</b> street noise, rain, footsteps, in sync with the picture. But you pay for it: Veo 3.1 on Vertex AI is $0.40/s with audio, $0.20/s without.")}</div>
      <div class="note" style="--k:var(--red)">{t("<b>Не даёт:</b> точный текст, один голос на все шоты, отдельные дорожки. Реплики модель <b>придумывает сама</b>.", "<b>Does not provide:</b> exact words, one voice across shots, separate tracks. The model <b>makes up lines</b> by itself.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Включите оба звука. Слева шот 1 из L05: в промпте не было ни одной реплики, а Veo озвучил бариста и курьера: «Here’s your order. Thank you. Have a good day». Справа неудачный клип из L05: в промпте карта навигатора, и Veo сам добавил голос навигатора «Continue straight for 200 meters». Мы это не слышали, пока не прогнали звук через распознавание речи.",
                      "⏱ 4 min. Play both. Left: shot 1 from L05. The prompt had no dialogue, yet Veo voiced the barista and the courier: “Here’s your order. Thank you. Have a good day.” Right: the L05 failure clip. The prompt mentions a navigation map, and Veo added a navigator voice: “Continue straight for 200 meters”. We did not notice this until we ran the audio through speech-to-text."),
                    t("Вывод. Звук видеомодели хорош как фон: шумы, дождь, шаги, синхронно с картинкой. Но он не бесплатный: в Vertex AI (теперь Gemini Enterprise Agent Platform) звук у Veo 3.1 выключается параметром generateAudio, и тогда секунда стоит $0.20 вместо $0.40; у других сервисов, например Kling 3.0, звук тоже стоит дополнительно. В документации Gemini API параметра для отключения звука у Veo нет. И главное: точный текст, один и тот же голос в трёх шотах и отдельные дорожки для монтажа видеомодель не даёт. Реплики она придумывает.",
                      "Takeaway. A video model’s audio works as background: noise, rain, footsteps, in sync with the picture. It is not free: on Vertex AI (now Gemini Enterprise Agent Platform) the generateAudio parameter turns Veo 3.1 audio off, and a second then costs $0.20 instead of $0.40; on other services such as Kling 3.0, audio also costs extra. The Gemini API documents no switch to turn Veo audio off. And the main point: a video model does not give exact words, the same voice across three shots or separate tracks for editing. It makes up lines."),
                    t("Правило: если нужны точные слова, голос делаем отдельно (синтез речи), а звук видеомодели используем как фон или выключаем. В официальном руководстве по промптам Veo реплики пишут в кавычках, шумы после «SFX:», фон после «Ambient noise:»; это помогает, но не гарантирует.",
                      "Rule: when you need exact words, generate the voice separately with text-to-speech, and use the video model’s audio as background or mute it. Google’s Veo prompting guide puts dialogue in quotes, sound effects after “SFX:” and background after “Ambient noise:”; that helps but guarantees nothing.")))


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
                f'<td>{t("«", "“")}{ln["display"]}{t("»", "”")}</td><td class="tm">{w} / {num(d)} {t("с", "s")}</td><td>{sfx}</td></tr>')
    words, secs, _ = voice_words()
    return dict(min=5, html=f'''
  {head(t("Шаг 1 • сценарий", "Step 1 • script"), t("Сценарий озвучки: текст, время и бюджет слов на каждый шот", "Voice-over script: text, timing and a word budget for each shot"), k="cyan")}
  <div class="body" style="margin-top:12px;">
    <table class="sb">
      <thead><tr><th>{t("Шот", "Shot")}</th><th>{t("Время", "Time")}</th><th>{t("Закадровый текст", "Voice-over")}</th><th>{t("Слов / длина", "Words / length")}</th><th>{t("Шумы", "Sound effects")}</th></tr></thead>
      <tbody>{trs}<tr><td colspan="5" style="color:var(--muted)">{t("Музыка: одна подложка на все шоты, лоу-фай, без вокала", "Music: one bed for all shots, lo-fi, no vocals")}</td></tr></tbody>
    </table>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:22px;">
      <div class="stat" style="--k:var(--cyan)"><div class="n">≈ {num(words / secs)} {t("слова/с", "words/s")}</div><div class="d">{t("измерено на нашей озвучке; планируйте <b>2–2,5 слова в секунду</b>, чтобы осталась пауза", "measured on our voice-over; plan for <b>2–2.5 words per second</b> to leave a pause")}</div></div>
      <div class="note" style="--k:var(--amber)">{t("<b>Шот 8 с ≈ 6 с речи</b> (по секунде тишины у склеек) <b>× 2–2,5 слова/с = 12–15 слов.</b> На русском планируйте 1,8–2,2 слова/с. Не влезает: сокращаем текст, голос не ускоряем.", "<b>An 8 s shot ≈ 6 s of speech</b> (about 1 s of silence at each cut) <b>× 2–2.5 words/s = 12–15 words.</b> If it does not fit, cut the text; do not speed up the voice.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. На слайде 7 L05 был полный шаблон сториборда из 7 колонок; в ДЗ L05 вы заполняли только видео-часть. Сегодня добавляем три звуковые колонки: закадровый текст, шумы, музыка. Одна строка = один шот = одна реплика.",
                      "⏱ 5 min. L05 slide 7 showed the full 7-column storyboard template; in the L05 homework you filled in only the video part. Today we add the three audio columns: voice-over, sound effects, music. One row = one shot = one line."),
                    t(f"Бюджет слов. Наш голос говорит примерно {num(words / secs)} слова в секунду. Для плана берите 2–2,5 слова в секунду, а на русском 1,8–2,2: слова длиннее. И оставьте по секунде тишины у каждой склейки: в 8-секундном шоте около 6 секунд речи, то есть 12–15 слов. Если текст не влезает, сокращаем текст. Ускорять голос плохая идея: звучит неестественно.",
                      f"Word budget. Our voice speaks about {num(words / secs)} words per second. Plan with 2–2.5 words per second (Russian: 1.8–2.2, the words are longer) and leave about a second of silence at each cut: an 8-second shot has about 6 seconds of speech, so 12–15 words. If the text does not fit, cut the text. Speeding up the voice sounds unnatural."),
                    t("Упражнение (1 мин, в чат): напишите реплику для шота 4 «курьер у двери» не длиннее 12 слов.",
                      "Exercise (1 min, chat): write the line for shot 4, “courier at the door”, in 12 words or fewer.")))


def s_text():
    if LANG == "ru":
        rows = [("6:42", "Шесть сорок две", "время: «шесть сорок две» или «восемнадцать сорок две»?"),
                ("417", "четыреста семнадцать", "решаем заранее: число или номер по цифрам «четыре один семь»"),
                ("12 мин", "двенадцать минут", "сокращения модель может прочитать по буквам")]
    else:
        rows = [("6:42", "Six forty-two", "a time, a score or a ratio?"),
                ("417", "four one seven", "an order ID: digit by digit, not “four hundred seventeen”"),
                ("12 min", "twelve minutes", "abbreviations may be read letter by letter")]
    trs = "".join(f'<tr><td class="tm" style="font-size:30px;padding:22px 12px">{a}</td><td style="font-size:26px;color:var(--green);white-space:nowrap">{b}</td><td style="font-size:21px">{c}</td></tr>' for a, b, c in rows)
    return dict(min=5, html=f'''
  {head(t("Шаг 2 • текст для голоса", "Step 2 • spoken text"), t("Текст для голоса: числа словами, стиль отдельной инструкцией", "Spoken text: numbers as words, style as a separate instruction"), k="cyan")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:40px;align-items:center;flex:none;">
      <div class="stack" style="gap:14px;">
        <div class="prompt-label">{t("Что видит зритель → что читает модель", "What the viewer sees → what the model reads")}</div>
        <table class="sb"><thead><tr><th>{t("Сценарий", "Script")}</th><th>{t("Текст для голоса", "Spoken text")}</th><th>{t("Почему", "Why")}</th></tr></thead><tbody>{trs}</tbody></table>
      </div>
      <div class="stack" style="gap:16px;">
        <div class="prompt-label">{t("Стиль задаётся отдельной инструкцией", "Style goes in a separate instruction")}</div>
        <div class="prompt">{t("Инструкция:", "Instruction:")} <span style="color:var(--amber)">{t("Спокойный, дружелюбный диспетчер. Средний темп. Короткая пауза после каждой фразы.", "Calm, friendly dispatcher. Medium pace. Short pause after each sentence.")}</span><br>{t("Текст:", "Text:")} {R()["lines"][0]["spoken"]}</div>
        <ul class="list">
          <li>{t("<b>OpenAI:</b> отдельное поле <code>instructions</code>; <b>Gemini 3.8:</b> отдельное поле <code>style</code>, короткие звуки тегами: <code>&lt;sigh&gt;</code>.", "<b>OpenAI:</b> a separate <code>instructions</code> field; <b>Gemini 3.8:</b> a separate <code>style</code> field, short sounds as tags: <code>&lt;sigh&gt;</code>.")}</li>
          <li>{t("<b>ElevenLabs v3:</b> теги в тексте, например <code>[whispers]</code>.", "<b>ElevenLabs v3:</b> tags inside the text, e.g. <code>[whispers]</code>.")}</li>
          <li>{t("<b>Словарь произношений</b> для имён и терминов (ElevenLabs, Google, Azure).", "<b>Pronunciation dictionary</b> for names and terms (ElevenLabs, Google, Azure).")}</li>
        </ul>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Сценарий пишем для зрителя: «6:42», «417». Модели синтеза речи даём отдельную колонку «текст для голоса»: словами. Иначе модель угадывает: 6:42 это время, счёт матча или пропорция? 417 это число или номер заказа, который читают по цифрам?",
                      "⏱ 5 min. The script is written for the viewer: “6:42”, “417”. The speech model gets a separate “spoken text” column with everything written out as words. Otherwise the model guesses: is 6:42 a time, a score or a ratio? Is 417 a number or an order ID read digit by digit?"),
                    t("Стиль голоса — отдельная инструкция, не часть текста. У OpenAI и Gemini это фраза на естественном языке: «спокойный, дружелюбный диспетчер». В ElevenLabs v3 теги прямо в тексте, например [whispers]. Для имён и терминов у ElevenLabs, Google и Azure есть словари произношений.",
                      "Voice style is a separate instruction, not part of the text. In OpenAI and Gemini it is a natural-language phrase: “calm, friendly dispatcher”. ElevenLabs v3 uses tags inside the text, such as [whispers]. For names and terms, ElevenLabs, Google and Azure offer pronunciation dictionaries."),
                    t("Как читать 417, решаете вы в сценарии, а не модель. Даже с правильным текстом голос может ошибиться, особенно на редких языках и в открытых моделях. Это проверим на шаге 6.",
                      "Who decides how 417 is read? You do, in the script, not the model. Even with correct text the voice can still get it wrong, especially in less common languages and open models. We check that in step 6.")))


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
    <div class="note" style="margin-top:26px;--k:var(--red)">{t("<b>Перед выбором:</b> прогоните через голос самые сложные слова сценария (имена, числа). Голос, который их искажает, отклоняем.", "<b>Before you commit:</b> run the hardest words of the script (names, numbers) through the voice. Reject a voice that mispronounces them.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Три источника голоса. Готовый голос из библиотеки: лицензия уже покрыта сервисом. У Gemini 30 готовых голосов, у OpenAI 13. В нашем примере английский голос Kokoro af_heart и русский Piper dmitri.",
                      "⏱ 4 min. Three sources of a voice. A library voice: the service’s licence already covers it. Gemini has 30 prebuilt voices, OpenAI 13. Our example uses Kokoro af_heart for English and Piper dmitri for Russian."),
                    t("Технически: одна реплика = один файл (line1.wav, line2.wav…). В редакторе ставим каждый файл на время старта из сценария и проверяем, что он не длиннее окна речи шота. Голос по описанию: пишете текстом, какой нужен голос, сервис генерирует новый. Есть в ElevenLabs (Voice Design) и в Gemini API. Проверьте, что результат не похож на известного человека.",
                      "Technically: one line = one file (line1.wav, line2.wav…). In the editor, place each file at the start time from the script and check it is not longer than the shot’s speech window. Designed voice: describe the voice in text and the service generates a new one. Available in ElevenLabs (Voice Design) and the Gemini API. Check that the result does not sound like a known person."),
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
        <div class="note" style="--k:var(--red)">{t("Веса MusicGen: лицензия <b>Creative Commons «с указанием авторства, некоммерческая» (CC BY-NC 4.0)</b>. Для урока можно, для клиента нет.", "MusicGen weights: <b>Creative Commons Attribution-NonCommercial (CC BY-NC 4.0)</b> licence. Fine for a lesson, not for a client.")}</div>
      </div>
      <table class="cost lic">
        <thead><tr><th>{t("Сервис", "Service")}</th><th>{t("Длина", "Length")}</th><th>{t("Коммерческое использование", "Commercial use")}</th></tr></thead>
        <tbody>
          <tr><td class="m">Suno v6<small>{t("песни", "songs")}</small></td><td>{t("песня", "song")}</td><td style="font-family:var(--body);font-size:20px">{t("только платные тарифы", "paid plans only")}</td></tr>
          <tr><td class="m">Lyria 3.5<small>Gemini app, Gemini API</small></td><td>{t("пара минут", "~2 min")}</td><td style="font-family:var(--body);font-size:20px">{t("не указано; метка SynthID на каждом треке", "not stated; SynthID watermark on every track")}</td></tr>
          <tr><td class="m">ElevenLabs Music<small>{t("музыка", "music")}</small></td><td>3 {t("с", "s")} – 5 {t("мин", "min")}</td><td style="font-family:var(--body);font-size:20px">{t("«почти любое», по тарифу", "“nearly all”, per plan")}</td></tr>
          <tr><td class="m">ElevenLabs Sound Effects<small>{t("шумы", "sound effects")}</small></td><td>≤ 30 {t("с", "s")}</td><td style="font-family:var(--body);font-size:20px">{t("по тарифу", "per plan")}</td></tr>
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
            ("mix_" + LANG, t("Сведение", "Mix"), f'{num(R()["mix"]["lufs"])} LUFS · {num(R()["mix"]["true_peak_dbfs"])} dBTP', "var(--amber)", None)]
    stems = "".join(f'<div class="stem" style="--k:{c}"><div class="lab">{lab}<small>{sub}</small></div>{wave(ENV[k], h=62, w=span, color=c)}</div>'
                    for k, lab, sub, c, _ in rows)
    cmd = ('ffmpeg -i voice.wav -i veo.wav -i music.wav -filter_complex \\\n'
           ' "[1][2]amix[bed];[bed][0]sidechaincompress[duck];\n'
           '  [0][duck]amix,loudnorm=I=-14:TP=-1.5" mix.wav')
    return dict(min=5, html=f'''
  {head(t("Шаг 5 • сведение", "Step 5 • mix"), t("Сведение: голос сверху, фон приглушён", "Mixing: voice on top, background ducked, loudness normalised"), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="stems">{stems}</div>
    <div class="row" style="grid-template-columns:1fr 1.15fr;gap:36px;flex:none;margin-top:20px;align-items:start;">
      <ul class="list">
        <li>{t("<b>Приглушение (ducking):</b> фон автоматически тише, пока звучит голос.", "<b>Ducking:</b> the background drops automatically while the voice speaks.")}</li>
        <li>{t("<b>Громкость:</b> −14 Loudness Units relative to Full Scale (LUFS) для Spotify и других стриминговых сервисов, −23 LUFS для эфира (стандарт Европейского вещательного союза EBU R128).", "<b>Loudness:</b> −14 Loudness Units relative to Full Scale (LUFS) for Spotify-style streaming, −23 LUFS for broadcast (European Broadcasting Union standard EBU R128).")}</li>
        <li>{t("<b>Пик:</b> истинный пик (true peak), самая высокая точка волны, включая промежутки между отсчётами; не выше −1 дБ (dBTP), иначе сжатие в MP3 или AAC даст искажения.", "<b>Peak:</b> true peak, the highest point of the wave including between samples; no higher than −1 decibel (dBTP), otherwise MP3 or AAC encoding distorts it.")}</li>
      </ul>
      <div class="stack" style="gap:8px;"><div class="nocode">{t("<b>Без кода, Audacity (бесплатно):</b> 1) импорт звука ролика, музыки и реплик; 2) фон: <i>Effect › Auto Duck</i>; 3) <i>Mix and Render</i> → <i>Loudness Normalization</i> −14 LUFS → <i>Limiter</i> −1 dB; 4) WAV в CapCut или Clipchamp, звук клипа выключить.", "<b>No code, Audacity (free):</b> 1) import the video sound, music and lines; 2) background: <i>Effect › Auto Duck</i>; 3) <i>Mix and Render</i> → <i>Loudness Normalization</i> −14 LUFS → <i>Limiter</i> −1 dB; 4) WAV into CapCut or Clipchamp, mute the clip’s own sound.")}</div><div class="small">{t("С кодом: ffmpeg (sidechaincompress + loudnorm), полная команда в make_audio.py.", "With code: ffmpeg (sidechaincompress + loudnorm), full command in make_audio.py.")}</div></div>
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 5 мин. Это реальные дорожки нашего ролика. Голос сам по себе {num(R()['voice_only']['lufs'])} LUFS, звук Veo {num(REPORT['veo_native']['lufs'])} LUFS, ниже музыка и итог. Видно, как фон проседает там, где говорит голос: это приглушение, по-английски ducking.",
                      f"⏱ 5 min. These are the real tracks of our video. The voice alone is {num(R()['voice_only']['lufs'])} LUFS, Veo’s audio {num(REPORT['veo_native']['lufs'])} LUFS, then music and the final mix. You can see the background drop where the voice speaks: that is ducking."),
                    t("LUFS — единица громкости, как её слышит человек. Стриминговые платформы приводят треки к своему уровню: Spotify к −14 LUFS, Apple Podcasts к −16. Стандарт эфира Европейского вещательного союза EBU R128: −23. Если ролик тише, платформа его поднимет вместе с шумом; если громче, опустит. Второе число — истинный пик, true peak: не выше −1 dBTP, иначе после сжатия в MP3 или AAC появится хрип.",
                      "LUFS is a loudness unit that follows human hearing. Streaming platforms normalise tracks to their level: Spotify to −14 LUFS, Apple Podcasts to −16. The European Broadcasting Union broadcast standard EBU R128 is −23. A quieter video gets raised together with its noise; a louder one gets turned down. The second number is true peak: no higher than −1 dBTP, otherwise MP3 or AAC encoding adds distortion."),
                    t("Наш первый проход нормализации дал пик −0,6 dBTP на русской версии, то есть не прошёл. Исправили двухпроходной нормализацией и лимитером, теперь −1,1. Без кода: Audacity, шаги справа. Нет Auto Duck — просто опустите фон на 10–15 дБ там, где звучит голос. Музыкальная подложка (bed) — тихая музыка под голосом. С кодом то же делает ffmpeg: фильтр sidechaincompress (голос управляет тем, насколько приглушить фон) и loudnorm.",
                      "Our first normalisation pass gave a −0.6 dBTP peak on the Russian version, which fails the −1 dBTP limit. Two-pass normalisation plus a limiter fixed it: now −1.1. No code: Audacity, steps on the right. Without Auto Duck, simply lower the background by 10–15 dB wherever the voice speaks. A music bed is quiet music under the voice. With code, ffmpeg does the same: the sidechaincompress filter (the voice controls how much the background drops) and loudnorm."),
                    teams()))


def s_check():
    rr = R()
    crit = rr["critical_terms"]
    ok = sum(c["ok"] for c in crit)
    heard = diff_markup(" ".join(x["display"] for x in rr["lines"]), " ".join(x["text"] for x in rr["transcript"]),
                        [c["term"] for c in crit if c["ok"]])
    if LANG == "ru":
        diag = [("red", "«Часть 42» вместо «Шесть сорок две»", "причина в голосе: проглатывает «ш»"), ("red", "«Оно» вместо «Анна»", "причина в голосе: неверно читает имя")]
    else:
        diag = [("red", "“Here’s your order.”", "the mix: Veo’s invented line leaks through"), ("amber", "“642” instead of “6:42”", "speech-to-text formatting; the voice said it correctly")]
    listened = {"en": len(crit), "ru": ok}[LANG]  # after listening: EN "642" is the transcriber's format; RU errors are real
    script = " ".join(x["display"] for x in rr["lines"])
    diags = "".join(f'<li style="--k:var(--{k})"><b>{a}</b>: {b}</li>' for k, a, b in diag)
    return dict(min=6, html=f'''
  {head(t("Шаг 6 • проверка", "Step 6 • check"), t("Проверка озвучки распознаванием речи", "Checking the voice-over with speech-to-text"), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.45fr 1fr;gap:36px;align-items:center;flex:none;">
      <div class="stack" style="gap:16px;">
        <div class="tx"><small>{t("Сценарий", "Script")}</small>{script}<small style="margin-top:14px">{t("Что услышал Whisper (small, на ноутбуке)", "What Whisper heard (small model, laptop)")}</small>{heard}</div>
        <ul class="list">{diags}</ul>
      </div>
      <div class="stack" style="gap:24px;">
        <div class="tx" style="display:flex;flex-direction:column;gap:18px;"><div class="stat" style="--k:var(--amber)"><div class="n">{num(rr["wer_vs_display"] * 100, 1)}%</div><div class="d">{t("частота ошибок в словах (word error rate, WER) = (замены + пропуски + вставки) / слов в сценарии", "word error rate (WER) = (substitutions + deletions + insertions) / words in the script")}</div></div>
        <div class="stat" style="--k:var(--red)"><div class="n">{ok} / {len(crit)} → {listened} / {len(crit)}</div><div class="d">{t("критичных слов верно: автоматически → после прослушивания (время, номер, минуты, имя)", "critical terms correct: automatic → after listening (time, order number, minutes, name)")}</div></div></div>
        <div class="nocode">{t("<b>Без кода:</b> ElevenLabs Speech to Text, Google AI Studio (промпт «Transcribe verbatim. Do not correct mistakes.»), Buzz (Whisper для компьютера).", "<b>No code:</b> ElevenLabs Speech to Text, Google AI Studio (prompt “Transcribe verbatim. Do not correct mistakes.”), Buzz (Whisper desktop app).")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Как проверить озвучку, не вслушиваясь десять раз: прогоняем итоговый звук через распознавание речи и сравниваем с исходным сценарием. Мы использовали открытую модель Whisper small прямо на ноутбуке. Живая демонстрация (2 мин): перетащите mix_ru.mp3 в Google AI Studio с промптом «Transcribe verbatim. Do not correct mistakes. Write numbers as you hear them.». Никогда не вставляйте сценарий в промпт распознавания: языковая модель «исправит» текст под сценарий и спрячет ошибки.",
                      "⏱ 6 min. How to check a voice-over without listening ten times: run the final audio through speech-to-text and compare with the script. We used the open Whisper small model on a laptop. Live demo (2 min): drop mix_en.mp3 into Google AI Studio with the prompt “Transcribe verbatim. Do not correct mistakes. Write numbers as you hear them.” Never paste your script into the transcription prompt: a language model will correct the transcript towards the script and hide the errors."),
                    t("Частота ошибок в словах, WER: замены плюс пропуски плюс вставки, делённые на число слов сценария. Чем ниже, тем лучше. Но одна цифра прячет главное: ошибка в номере заказа важнее десяти ошибок в предлогах. Поэтому отдельно проверяем список критичных слов: время, номер, минуты, имя. И перед подсчётом приведите числа к одному виду в обоих текстах: «6:42» и «шесть сорок две» иначе считаются ошибкой.",
                      "Word error rate, WER: substitutions plus deletions plus insertions, divided by the number of words in the script. Lower is better. But one number hides the important part: an error in the order number matters more than ten errors in articles. So we check a separate list of critical terms: time, order number, minutes, name. Before counting, write numbers the same way in both texts, otherwise “6:42” and “six forty-two” count as an error."),
                    t("Что нашли в английской версии: в начале распознано «Here’s your order», это реплика, которую придумал Veo (слайд 6), она пробивается через сведение. Значит, звук шота 1 нужно вырезать или заглушить в начале. «642» вместо «6:42»: послушали — голос сказал верно, это формат записи у распознавания. Ошибка проверки, а не озвучки.",
                      "What we found in English: the transcript starts with “Here’s your order”, the line Veo made up (slide 6), leaking through the mix. So the shot 1 audio needs to be cut or muted at the start. “642” instead of “6:42”: we listened, and the voice said it correctly; this is the transcriber’s formatting. A checking artefact, not a voice error."),
                    t("В русской версии: «Часть 42» вместо «Шесть сорок две» и «Оно» вместо «Анна». Послушали: это голос, открытая русская модель Piper читает эти слова плохо. Исправление: другой голос или переписать реплику. Это реальные результаты, ничего не подстроено.",
                      "In Russian: “Часть 42” (“part 42”) instead of “Шесть сорок две” (“six forty-two”) and “Оно” (“it”) instead of “Анна” (Anna). We listened: it is the voice; the open Russian Piper model reads these words badly. Fix: a different voice or a rewritten line. These are real results, nothing staged.")))


def s_local():
    cl = CLONE or {"load_seconds": 0, "lines": [{"real_time_factor": 0}]}
    rtf = max(x["real_time_factor"] for x in cl["lines"])
    rows = [
        ("Kokoro-82M", t("синтез речи", "text-to-speech"), "0,36 ГБ" if LANG == "ru" else "0.36 GB", t("процессор ноутбука", "laptop processor"), t("наш голос EN", "our EN voice")),
        ("Whisper small", t("распознавание", "speech-to-text"), "0,5 ГБ" if LANG == "ru" else "0.5 GB", t("процессор ноутбука", "laptop processor"), t("наша проверка", "our check")),
        ("Qwen3-TTS 0.6B", t("синтез + клон", "text-to-speech + cloning"), "2,5 ГБ" if LANG == "ru" else "2.5 GB", t(f"процессор: ≈{num(rtf, 0)}× медленнее реального времени", f"processor: ≈{num(rtf, 0)}× slower than real time"), t("слайд 16", "slide 16")),
        ("Qwen3-TTS 1.7B", t("синтез + клон", "text-to-speech + cloning"), "4,5 ГБ" if LANG == "ru" else "4.5 GB", t("видеокарта от 8 ГБ памяти", "graphics card with 8 GB or more"), t("лучше качество", "better quality")),
    ]
    trs = "".join(f'<tr><td class="m">{a}<small>{b}</small></td><td style="white-space:nowrap">{c}</td><td style="font-family:var(--body);font-size:21px">{d}</td><td style="font-family:var(--body);font-size:20px;color:var(--muted)">{e}</td></tr>'
                  for a, b, c, d, e in rows)
    flow = '<div class="arr">→</div>'.join(f'<div class="box">{x}</div>' for x in [
        t("Hugging Face<small>карточка модели и файлы весов</small>", "Hugging Face<small>model card and weight files</small>"),
        t("Ваш диск<small>~/.cache/huggingface</small>", "Your disk<small>~/.cache/huggingface</small>"),
        t("Python-пакет<small>qwen-tts, kokoro-onnx</small>", "Python package<small>qwen-tts, kokoro-onnx</small>"),
        t("Процессор или видеокарта<small>считает звук</small>", "Processor (CPU) or graphics card (GPU)<small>computes the audio</small>"),
        t("WAV-файл<small>ничего не уходит в интернет</small>", "WAV file<small>nothing leaves the machine</small>")])
    return dict(min=4, html=f'''
  {head(t("Локальные модели", "Local models"), t("Открытые аудиомодели на своём компьютере: где лежат, что нужно, сколько стоят", "Open-weight audio models on your own computer: where they live, what they need, what they cost"), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="flow" style="--k:var(--green);gap:12px;">{flow}</div>
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:36px;flex:none;margin-top:26px;align-items:center;">
      <table class="cost lic"><thead><tr><th>{t("Модель", "Model")}</th><th>{t("Файлы", "Files")}</th><th>{t("Где запускать", "Runs on")}</th><th>{t("У нас", "In this lesson")}</th></tr></thead><tbody>{trs}</tbody></table>
      <div class="stack" style="gap:22px;">
        <div class="stat" style="--k:var(--green)"><div class="n">$0 {t("за минуту", "per minute")}</div><div class="d">{t("нет оплаты за символы и минуты, но вы платите <b>железом, электричеством и временем на установку</b>", "no per-character or per-minute bill, but you pay with <b>hardware, electricity and setup time</b>")}</div></div>
        <div class="note" style="--k:var(--amber)">{t("Зачем: <b>данные не уходят</b> из компьютера, нет лимитов, работает без интернета. Цена: качество ниже лучших сервисов, обновления и лицензии на вас.", "Why: <b>data stays on the machine</b>, no quotas, works offline. Cost: quality below the best services; updates and licences are your job.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 4 мин. Открытая модель — это файлы весов, которые любой может скачать. Почти все они лежат на Hugging Face: у каждой модели есть страница (карточка) с описанием, лицензией и примером кода. Python-пакет скачивает файлы один раз в папку кэша на вашем диске, дальше всё работает без интернета. Считает процессор или видеокарта; запись голоса и текст никуда не отправляются.",
                      f"⏱ 4 min. An open-weight model is a set of weight files anyone can download. Almost all of them live on Hugging Face: each model has a page (model card) with a description, licence and code example. A Python package downloads the files once into a cache folder on your disk; after that it works offline. The CPU or GPU does the computing; your voice recording and text go nowhere."),
                    t(f"Сколько нужно железа. Маленькие модели работают на обычном ноутбуке: Kokoro (0,36 ГБ) и Whisper small сделали нашу озвучку и проверку без видеокарты. Qwen3-TTS 0.6B (файлы 2,5 ГБ) на процессоре тоже работает, но медленно: в нашем замере примерно в {num(rtf, 0)} раз медленнее реального времени, то есть секунда звука считается {num(rtf, 0)} секунд. Для Qwen3-TTS 1.7B (4,5 ГБ) нужна видеокарта; по сторонним замерам комфортно от 8 ГБ видеопамяти. Плюс место на диске и Python 3.10 или новее.",
                      f"How much hardware. Small models run on an ordinary laptop: Kokoro (0.36 GB) and Whisper small made our voice-over and check without a GPU. Qwen3-TTS 0.6B (2.5 GB of files) also runs on a CPU, but slowly: in our measurement about {num(rtf, 0)} times slower than real time, so one second of audio takes {num(rtf, 0)} seconds. Qwen3-TTS 1.7B (4.5 GB) needs a GPU; third-party measurements say 8 GB of video memory is comfortable. Plus disk space and Python 3.10 or newer."),
                    t("Как это влияет на стоимость. Счёта за символы нет, но час речи на процессоре — это много часов работы компьютера, а видеокарта стоит денег или аренды. Локально выгодно, когда данные нельзя отдавать наружу, когда объём большой и постоянный, или для экспериментов. Для разовой озвучки ролика сервис за $0.08 в минуту дешевле вашего времени на установку.",
                      "How this affects cost. There is no per-character bill, but an hour of speech on a CPU means many hours of computer time, and a GPU costs money to buy or rent. Local makes sense when data must not leave the company, when volume is large and steady, or for experiments. For a one-off voice-over, a service at $0.08 per minute costs less than your setup time."),
                    t("Про архитектуры речевых систем (файл, поток, голосовой агент) коротко: распознавание бывает пакетное (файл целиком) и потоковое (черновой текст сразу, итоговый потом); голосовой агент — это цепочка «распознавание → языковая модель → синтез» или одна модель речь-в-речь. Строим агентов в модуле 4.",
                      "On speech system architectures (file, stream, voice agent), briefly: transcription is batch (whole file) or streaming (partial text at once, final text later); a voice agent is a chain speech-to-text → language model → text-to-speech, or one speech-to-speech model. We build agents in module 4.")))


def s_market():
    rows = [
        ("cyan", t("Синтез речи (TTS)", "Text-to-speech (TTS)"), t("текст → голос", "text → voice"),
         [("ElevenLabs v4 / v3", ""), ("Gemini 3.8 Flash TTS", ""), (t("OpenAI gpt-4o-mini-tts (до 06.01.2027)", "OpenAI gpt-4o-mini-tts (until 6 Jan 2027)"), "")],
         [("Kokoro-82M", "Apache-2.0"), ("Qwen3-TTS", "Apache-2.0")]),
        ("green", t("Распознавание речи (STT, ASR)", "Speech-to-text (STT, ASR)"), t("голос → текст", "voice → text"),
         [("OpenAI gpt-transcribe", ""), ("ElevenLabs Scribe v2", ""), ("AssemblyAI Universal-3.5 Pro", "")],
         [("Whisper large-v3-turbo", "MIT"), ("Qwen3-ASR", "Apache-2.0")]),
        ("amber", t("Речь в речь", "Speech-to-speech"), t("голосовые агенты, перевод", "voice agents, translation"),
         [("OpenAI gpt-realtime-2.1", ""), ("Gemini Live API", ""), ("ElevenLabs Agents", "")],
         []),
        ("violet", t("Музыка и шумы", "Music and sound effects"), t("текст → музыка, шумы", "text → music, effects"),
         [("Suno v6", ""), ("Lyria 3.5", ""), ("ElevenLabs Music / Sound Effects", "")],
         [("MusicGen", "CC BY-NC")]),
    ]
    cells = ""
    for k, h, sub, closed, open_ in rows:
        chips = "".join(f'<span class="mchip">{n}</span>' for n, _ in closed)
        chips += "".join(f'<span class="mchip ow">{n}<small>{lic}</small></span>' for n, lic in open_)
        cells += f'<div class="task-h" style="--k:var(--{k})">{h}<small>{sub}</small></div><div class="ms">{chips}</div>'
    return dict(min=4, html=f'''
  {head(t("Рынок • октябрь 2026", "Market • October 2026"), t("Аудиомодели по задачам: коммерческие и открытые", "Audio models by task: commercial and open-weight"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div class="mk">{cells}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:36px;flex:none;margin-top:18px;">
      <div class="note" style="--k:var(--green)">{t("<b>Точность распознавания (английский):</b> лучшие коммерческие ≈ 4–5% ошибок в словах, лучшие открытые ≈ 5–6%, Whisper large-v3 ≈ 7,8%. Open ASR Leaderboard, 09.10.2026.", "<b>Speech-to-text accuracy (English):</b> best commercial ≈ 4–5% word error rate, best open ≈ 5–6%, Whisper large-v3 ≈ 7.8%. Hugging Face Open ASR Leaderboard, 9 October 2026.")}</div>
      <div class="note" style="--k:var(--amber)">{t("<b>Срок жизни моделей короткий:</b> OpenAI отключает tts-1 и gpt-4o-mini-tts 06.01.2027, whisper-1 и gpt-4o-transcribe 26.02.2027. Имя модели держим в настройках.", "<b>Model lifetimes are short:</b> OpenAI shuts down tts-1 and gpt-4o-mini-tts on 6 January 2027, and whisper-1 and gpt-4o-transcribe on 26 February 2027. Keep the model name in configuration, not in code.")}</div>
    </div>
    <div class="small" style="margin-top:10px;color:var(--muted)">{t("Зелёная рамка: открытая модель и её лицензия. <b>MIT, Apache-2.0:</b> можно в коммерции, сохраняя текст лицензии. <b>CC BY:</b> можно в коммерции с указанием автора. <b>CC BY-NC:</b> только некоммерческое. У голосов и датасетов бывают свои лицензии.", "Green border: open-weight model and its licence. <b>MIT, Apache-2.0:</b> commercial use allowed, keep the licence notice. <b>CC BY:</b> commercial use with credit. <b>CC BY-NC:</b> non-commercial only. Voices and datasets can have their own licences.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Карта по четырём задачам, по три коммерческих примера на строку; полный список с ценами в L06_08. Слева коммерческие модели, в зелёной рамке открытые, с лицензией. Что изменилось за год: у OpenAI новое поколение распознавания (gpt-transcribe) и голосовых моделей (gpt-realtime-2.1, gpt-live-1), у ElevenLabs v4, у Google Gemini 3.8 TTS и музыка Lyria 3.5, у Suno v6.",
                      "⏱ 4 min. A map by the four tasks, three commercial examples per row; the full list with prices is in L06_08. Commercial models on the left, open-weight ones in a green border with their licence. What changed in a year: OpenAI has a new generation of transcription (gpt-transcribe) and voice models (gpt-realtime-2.1, gpt-live-1), ElevenLabs has v4, Google has Gemini 3.8 TTS and Lyria 3.5 music, Suno has v6."),
                    t("Точность распознавания: на открытом рейтинге Hugging Face Open ASR Leaderboard (обновлён 09.10.2026) лучшие коммерческие системы дают около 4–5% ошибок в словах на английском, лучшие открытые около 5–6%, Whisper large-v3 около 7,8%. На русском и на шумной записи цифры хуже; проверяйте на своих данных.",
                      "Accuracy: on the Hugging Face Open ASR Leaderboard (updated 09.10.2026) the best commercial systems are around 4–5% English word error rate, the best open ones around 5–6%, Whisper large-v3 around 7.8%. Other languages and noisy recordings score worse; test on your own data."),
                    t("И про срок жизни: OpenAI уже объявила отключение tts-1 и gpt-4o-mini-tts 6 января 2027 (замена: gpt-realtime-2.1-mini), whisper-1 и gpt-4o-transcribe 26 февраля 2027. Поэтому имя модели выносим в настройки. Названия моделей меняются каждые несколько месяцев; перепроверьте перед занятием.",
                      "On lifetimes: OpenAI has announced that tts-1 and gpt-4o-mini-tts shut down on 6 January 2027 (replacement: gpt-realtime-2.1-mini), and whisper-1 and gpt-4o-transcribe on 26 February 2027. So keep the model name in configuration. Model names change every few months; recheck before class.")))


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


def s_agent():
    cl = CLONE or {"load_seconds": 0, "reference": {"seconds": 0}, "lines": []}
    by = {x["name"]: x for x in cl["lines"]}
    prompt = t(
        "Установи на этот компьютер открытую модель синтеза речи Qwen3-TTS (Qwen/Qwen3-TTS-12Hz-0.6B-Base, лицензия Apache-2.0) и склонируй МОЙ голос.\n"
        "1. Проверь железо: видеокарта и её память, оперативная память, свободный диск (нужно ~5 ГБ). Скажи, что подойдёт: 0.6B или 1.7B, видеокарта или процессор.\n"
        "2. Создай отдельное окружение Python в ./qwen-tts-demo, установи qwen-tts и soundfile.\n"
        "3. Скачай модель с Hugging Face и покажи, где лежат файлы.\n"
        "4. Напиши clone.py: вход my_voice.wav (10 с моего голоса) и my_voice.txt (точная расшифровка), выход line1.wav с фразой из script.md.\n"
        "5. Запусти, замерь время, ничего не загружай в интернет.",
        "Install the open-weight text-to-speech model Qwen3-TTS (Qwen/Qwen3-TTS-12Hz-0.6B-Base, Apache-2.0 licence) on this computer and clone MY voice.\n"
        "1. Check the hardware: graphics card and its memory, system memory, free disk (~5 GB needed). Tell me what fits: 0.6B or 1.7B, graphics card or processor.\n"
        "2. Create a separate Python environment in ./qwen-tts-demo; install qwen-tts and soundfile.\n"
        "3. Download the model from Hugging Face and show where the files are.\n"
        "4. Write clone.py: input my_voice.wav (10 s of my voice) and my_voice.txt (exact transcript); output line1.wav with the line from script.md.\n"
        "5. Run it, report the time, upload nothing to the internet.")
    ru = by.get("ru_3", {})
    en = by.get("en_1", {})
    return dict(min=4, html=f'''
  {head(t("Практика с агентом", "Hands-on with an agent"), t("Агент ставит Qwen3-TTS локально и клонирует голос", "A coding agent installs Qwen3-TTS locally and clones a voice"), k="violet")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:32px;align-items:center;flex:none;">
      <div class="stack" style="gap:8px;">
        <div class="prompt-label">{t("Промпт для Claude Code, Antigravity или Codex", "Prompt for Claude Code, Antigravity or Codex")}</div>
        <pre class="code" style="font-size:19px;line-height:1.55;padding:18px 20px;white-space:pre-wrap;">{prompt}</pre>
      </div>
      <div class="stack" style="gap:14px;">
        <div class="flow" style="--k:var(--violet);flex-wrap:wrap;gap:8px;"><div class="box">{t("Образец 3–10 с<small>+ его точный текст</small>", "3–10 s sample<small>+ its exact transcript</small>")}</div><div class="arr">+</div><div class="box">{t("Новый текст<small>+ язык</small>", "New text<small>+ language</small>")}</div><div class="arr">→</div><div class="box hl">{t("Новая речь<small>этим голосом</small>", "New speech<small>in that voice</small>")}</div></div>
        {aud("clone_reference", t("Образец", "Sample"), t(f"синтетический голос Kokoro, {num(cl['reference']['seconds'])} с", f"synthetic Kokoro voice, {num(cl['reference']['seconds'])} s"), "cyan")}
        {aud("clone_ru_3" if LANG == "ru" else "clone_en_1", t("Клон", "Clone"), t(f"Qwen3-TTS 0.6B на процессоре, {num(ru.get('generation_seconds', 0), 0)} с счёта", f"Qwen3-TTS 0.6B on a processor, {num(en.get('generation_seconds', 0), 0)} s of compute"), "violet")}
        <div class="note" style="--k:var(--red)">{t("<b>Только свой голос.</b> Модель ничего не проверяет: согласие — ваша ответственность (слайд 19).", "<b>Your own voice only.</b> The model checks nothing: consent is your responsibility (slide 19).")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Слева готовый промпт для агента разработки: Claude Code, Antigravity или Codex в ChatGPT. Агент сам проверит железо, создаст отдельное окружение Python, скачает модель с Hugging Face, напишет скрипт и запустит его. Вам остаётся записать 10 секунд своего голоса и точно расшифровать их.",
                      "⏱ 4 min. On the left is a ready prompt for a coding agent: Claude Code, Antigravity or Codex in ChatGPT. The agent checks the hardware, creates a separate Python environment, downloads the model from Hugging Face, writes the script and runs it. You only record 10 seconds of your voice and transcribe them exactly."),
                    t(f"Что делает модель. Base-версия Qwen3-TTS получает образец голоса на 3–10 секунд и его точный текст; по ним она запоминает тембр и манеру. Потом получает новый текст и язык и генерирует речь этим голосом. В коде это одна функция generate_voice_clone(text, language, ref_audio, ref_text). Есть режим без расшифровки (x_vector_only), но качество ниже.",
                      f"What the model does. The Base version of Qwen3-TTS takes a 3–10 second voice sample and its exact transcript; from them it captures the timbre and manner. Then it takes new text and a language and generates speech in that voice. In code this is one function, generate_voice_clone(text, language, ref_audio, ref_text). There is a mode without a transcript (x_vector_only), but quality is lower."),
                    t(f"Наш реальный прогон: образцом был синтетический голос Kokoro, а не живой человек, поэтому вопроса согласия нет. Модель 0.6B на процессоре контейнера без видеокарты загружалась {num(cl['load_seconds'], 0)} с. Русская реплика «{ru.get('text', '')}» считалась {num(ru.get('generation_seconds', 0), 0)} с; Whisper услышал: «{ru.get('whisper', '')}». Английская: {num(en.get('generation_seconds', 0), 0)} с, Whisper: «{en.get('whisper', '')}». Обратите внимание: голос клонирован с английского образца, а говорит по-русски; «Анна» теперь произнесена верно, в отличие от Piper. Но первую русскую реплику Whisper записал как «Shaste Sort 2»: клон перенёс английский акцент образца. Образец лучше записывать на том же языке, на котором будет озвучка.",
                      f"Our real run: the sample was a synthetic Kokoro voice, not a living person, so there is no consent question. The 0.6B model on a container CPU without a GPU took {num(cl['load_seconds'], 0)} s to load. The English line took {num(en.get('generation_seconds', 0), 0)} s; Whisper heard: “{en.get('whisper', '')}”. The Russian line took {num(ru.get('generation_seconds', 0), 0)} s; Whisper heard: “{ru.get('whisper', '')}”. Note that the voice was cloned from an English sample and speaks Russian; “Анна” is now pronounced correctly, unlike with Piper. But Whisper wrote the first Russian line as “Shaste Sort 2”: the clone carried over the sample’s English accent. Record the sample in the same language as the voice-over."),
                    t("Справочный код синтеза через Gemini API (было на этом слайде раньше) лежит в README урока. Для ДЗ код не нужен; локальная модель — вариант по желанию, только со своим голосом.",
                      "The reference Gemini API synthesis code (previously on this slide) is in the lesson README. The homework needs no code; a local model is optional, with your own voice only.")))


def s_econ():
    # (task, model, where, $ per minute, billed as)
    rows = [
        (t("Синтез", "Text-to-speech"), "Gemini 3.8 Flash TTS", t("$9 / 1 млн аудиотокенов", "$9 / 1M audio tokens"), 0.0135),
        (t("Синтез", "Text-to-speech"), "ElevenLabs v3 / v4", t("$0.08 / 1000 символов", "$0.08 / 1K characters"), 0.08),
        (t("Распознавание", "Speech-to-text"), "OpenAI gpt-transcribe", t("$0.0045 / мин", "$0.0045 / min"), 0.0045),
        (t("Распознавание", "Speech-to-text"), "ElevenLabs Scribe v2", t("$0.22 / час", "$0.22 / hour"), 0.22 / 60),
        (t("Речь в речь", "Speech-to-speech"), "OpenAI gpt-live-1", t("$0.05 / мин + модель", "$0.05 / min + model"), 0.05),
        (t("Музыка", "Music"), "ElevenLabs Music", t("$0.15 / мин", "$0.15 / min"), 0.15),
    ]

    def money(v):
        if v >= 0.1:
            return f"${v:,.2f}"
        if v >= 0.01:
            return f"${v:.4f}".rstrip("0")
        return f"${v:.5f}".rstrip("0")
    trs = "".join(
        f'<tr><td class="m">{m}<small>{task} · {unit}</small></td><td>{money(v / 60)}</td><td>{money(v)}</td><td class="h">{money(v * 60)}</td></tr>'
        for task, m, unit, v in rows)
    _, _, chars = voice_words()
    return dict(min=4, html=f'''
  {head(t("Стоимость", "Cost"), t("Стоимость аудио: секунда, минута, час", "Audio cost: per second, per minute, per hour"), t("Пересчёт: <b>1 минута речи ≈ 1000 символов</b> (так считает ElevenLabs). Списочные цены на 12.10.2026.", "Conversion: <b>1 minute of speech ≈ 1,000 characters</b> (ElevenLabs’ own rule). List prices as of 12 October 2026."), k="amber")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:36px;align-items:start;">
      <table class="cost tight">
        <thead><tr><th>{t("Модель · как считают", "Model · billed as")}</th><th>{t("1 с", "1 s")}</th><th>{t("1 мин", "1 min")}</th><th>{t("1 час", "1 hour")}</th></tr></thead>
        <tbody>{trs}</tbody>
      </table>
      <div class="stack" style="gap:20px;">
        <div class="stat" style="--k:var(--green)"><div class="n">{t("≈ 1 цент", "≈ 1 cent")}</div><div class="d">{t(f"озвучка нашего ролика: {chars} символов на ElevenLabs v3; у нас $0 на открытых моделях", f"voicing our video: {chars} characters on ElevenLabs v3; $0 for us on open models")}</div></div>
        <div class="stat" style="--k:var(--amber)"><div class="n">$4.80 = 12 {t("с", "s")}</div><div class="d">{t("час голоса ElevenLabs стоит как 12 секунд видео Veo 3.1 (L05: $0.40/с)", "an hour of ElevenLabs voice costs as much as 12 seconds of Veo 3.1 video (L05: $0.40/s)")}</div></div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Сначала единицы. Синтез речи считают за символы текста (Google Cloud, ElevenLabs) или за аудиотокены (Gemini). Распознавание, голосовые агенты и музыку ElevenLabs — за минуту. Чтобы сравнивать, пересчитываем всё в секунду, минуту и час, приняв 1000 символов за минуту речи; так считает сам ElevenLabs.",
                      "⏱ 4 min. Units first. Speech synthesis is billed per character of text (Google Cloud, ElevenLabs) or per audio token (Gemini). Transcription, voice agents and ElevenLabs music are billed per minute. To compare, we convert everything to second, minute and hour, using 1,000 characters per minute of speech, ElevenLabs’ own rule."),
                    t("Главная мысль: звук на порядки дешевле видео. Час голоса на ElevenLabs стоит $4.80, на Gemini 3.8 Flash TTS меньше доллара. Час видео Veo 3.1 в L05 стоил $1 440. Распознавание часа записи стоит от 22 до 27 центов. Озвучка нашего ролика: около 150 символов, на ElevenLabs это примерно 1 цент.",
                      "Key point: audio is orders of magnitude cheaper than video. An hour of voice costs $4.80 on ElevenLabs and under a dollar on Gemini 3.8 Flash TTS. An hour of Veo 3.1 video in L05 cost $1,440. Transcribing an hour of recording costs 22 to 27 cents. Voicing our video: about 150 characters, roughly 1 cent on ElevenLabs."),
                    t("Подписки: ElevenLabs от $6 в месяц (30 тыс. кредитов ≈ 30 минут), Suno Pro $8 в месяц при оплате за год. В таблицу не входят дубли, сведение и работа людей. Пример для ДЗ: 3 реплики ≈ 150 символов × 2 сервиса × 3 дубля ≈ 900 символов ≈ $0.07 по прайсу; на бесплатном тарифе $0. Где деньги на самом деле уходят: голосовые агенты (минуты разговора плюс языковая модель за ними) и дубли озвучки. И подписки веб-студий: в ДЗ бесплатного лимита ElevenLabs (10 тыс. кредитов ≈ 10 минут) хватит, но коммерческой лицензии на бесплатном тарифе нет. Цены меняются: у Gemini 3.8 TTS цена удваивается с 1 января 2027.",
                      "Subscriptions: ElevenLabs from $6 a month (30K credits ≈ 30 minutes), Suno Pro $8 a month billed yearly. The table excludes retakes, mixing and people’s time. Homework example: 3 lines ≈ 150 characters × 2 services × 3 retakes ≈ 900 characters ≈ $0.07 at list price; $0 on a free tier. Where the money goes: voice agents (conversation minutes plus the language model behind them) and voice retakes. And web studio subscriptions: the ElevenLabs free allowance (10K credits ≈ 10 minutes) is enough for the homework, but the free plan has no commercial licence. Prices change: Gemini 3.8 TTS doubles on 1 January 2027.")))


def s_qa():
    rr = R()
    mix = rr["mix"]
    items = [
        (t("<b>Слова</b> совпадают со сценарием: распознавание + список критичных слов", "<b>Words</b> match the script: speech-to-text + critical terms list"), "red"),
        (t("<b>Произношение</b> имён, чисел, терминов: проверено на слух", "<b>Pronunciation</b> of names, numbers, terms: checked by ear"), "red" if LANG == "ru" else "green"),
        (t("<b>Тайминг:</b> реплика влезает в шот, не режется склейкой", "<b>Timing:</b> each line fits its shot and is not cut by a transition"), "green"),
        (t("<b>Сведение:</b> голос разборчив, фон приглушён, нет чужой речи", "<b>Mix:</b> voice is clear, background ducked, no stray speech"), "red"),
        (t("<b>Громкость</b> −14 ± 1 LUFS; истинный пик ≤ −1 дБ (dBTP)", "<b>Loudness</b> −14 ± 1 LUFS; true peak ≤ −1 dB (dBTP)"), "green"),
        (t("<b>Права:</b> лицензия голоса и музыки, согласие, пометка «создано ИИ»", "<b>Rights:</b> voice and music licence, consent, “AI-generated” label"), "amber"),
    ]
    lis = "".join(f'<li><span>{h}</span></li>' for h, _ in items)
    marks = {"green": "✓", "red": "✗", "amber": "!"}
    res = "".join(f'<div style="font-size:28px;font-weight:800;color:var(--{k});height:58px;display:flex;align-items:center;">{marks[k]}</div>' for _, k in items)
    return dict(min=5, html=f'''
  {head(t("Приёмка", "Acceptance"), t("Чек-лист приёмки озвучки", "Acceptance checklist for a voice-over"), t("Это же критерии оценки домашнего задания. Справа реальный результат нашей версии.", "The same items are the homework rubric. On the right, the real result for our version."), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:40px;align-items:center;">
      <div class="row" style="grid-template-columns:1fr 50px;gap:10px;flex:none;align-items:start;">
        <ol class="checklist" style="gap:0">{lis.replace("<li>", '<li style="height:58px;align-items:center;font-size:23px">')}</ol>
        <div class="stack" style="gap:0">{res}</div>
      </div>
      <div class="stack" style="gap:22px;">
        <div class="stat" style="--k:var(--green)"><div class="n">{num(mix["lufs"])} LUFS</div><div class="d">{t(f"пик {num(mix['true_peak_dbfs'])} dBTP. Без кода: Youlean Loudness Meter или измеритель громкости в DaVinci Resolve, смотрим Integrated и True Peak", f"peak {num(mix['true_peak_dbfs'])} dBTP. No code: Youlean Loudness Meter or the DaVinci Resolve loudness meter; read Integrated and True Peak")}</div></div>
        <div class="note" style="--k:var(--red)">{t("<b>Не принято:</b> голос искажает «Анна» и «шесть сорок две»; в начале слышна английская реплика Veo, которую распознавание на русском пропустило. Исправление: другой голос, звук шота 1 заглушить на 0–3 с.", "<b>Rejected:</b> Veo’s line “Here’s your order” leaks into the start. Fix: mute the shot 1 audio for 0–3 s, then repeat item 1.")}</div>
        <div class="small" style="font-size:18px;color:var(--muted)">{t("Доказательства в ДЗ: 1 → transcript.txt и таблица критичных слов · 2, 4 → заметки на слух с таймкодами · 3 → script.md · 5 → скриншот измерителя · 6 → таблица лицензий и пометка «создано ИИ»", "Homework evidence: 1 → transcript.txt and critical-terms table · 2, 4 → by-ear notes with timecodes · 3 → script.md · 5 → meter screenshot · 6 → licence table and “AI-generated” label")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Шесть пунктов приёмки. Первый: слова совпадают со сценарием, проверяем распознаванием и списком критичных слов. Второй: произношение имён, чисел и терминов, только на слух. Третий: тайминг, реплика влезает в шот. Четвёртый: сведение, голос разборчив, фон приглушён, нет посторонней речи. Пятый: громкость −14 LUFS плюс-минус 1 и пик не выше −1 dBTP. Шестой: права, то есть лицензия голоса и музыки, согласие владельца голоса и пометка «создано ИИ».",
                      "⏱ 5 min. Six acceptance items. One: the words match the script, checked with speech-to-text and the critical terms list. Two: pronunciation of names, numbers and terms, by ear only. Three: timing, each line fits its shot. Four: mix, the voice is clear, the background is ducked, no stray speech. Five: loudness −14 LUFS plus or minus 1 and a peak no higher than −1 dBTP. Six: rights, meaning the voice and music licence, the voice owner’s consent and an “AI-generated” label."),
                    t("Справа реальный результат. Громкость и пик проходят. Русская версия не принята: голос искажает «Анна» и «шесть сорок две». И пункт 4: в начале слышна английская реплика Veo «Here’s your order», а распознавание, настроенное на русский, её не услышало. Вывод: распознавание на одном языке не слышит чужую речь на другом; первые и последние секунды слушаем ушами. Английская тоже не принята: в начале слышна реплика, которую придумал Veo. Пункт 6 с восклицательным знаком: MusicGen некоммерческий, для урока можно, для клиента нет.",
                      "On the right is the measured result. Loudness and peak pass. The Russian version is rejected: the voice breaks “Анна” and “шесть сорок две”. The English version is rejected too: Veo’s invented line is audible at the start. Item 6 has an exclamation mark: MusicGen is non-commercial; fine for a lesson, not for a client."),
                    t("Этот же чек-лист — критерии оценки домашнего задания; для каждого пункта внизу указано, чем его подтвердить. Оценивается разбор ошибок, а не идеальный звук.",
                      "The same checklist is the homework rubric; the line at the bottom says what evidence each item needs. Grading is based on the error analysis, not on perfect sound.")))


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
          <li>{t("<b>Открытые модели</b> (Qwen3-TTS, Chatterbox): клон по 3–10 с, <b>без проверок</b>.", "<b>Open-weight models</b> (Qwen3-TTS, Chatterbox): clone from 3–10 s, <b>no checks at all</b>.")}</li>
        </ul>
      </div>
    </div>
    <div class="plaque" style="margin-top:28px;font-size:21px;"><b>EU AI Act, {t("ст. 50", "Art. 50")}:</b> {t("с 2 августа 2026 синтетический звук и дипфейки нужно помечать; штраф до €15 млн или 3% оборота. <b>OpenAI</b> требует сообщать слушателю, что голос сгенерирован. <b>Google</b> ставит невидимую метку SynthID во весь звук своих моделей.", "from 2 August 2026, synthetic audio and deepfakes must be labelled; fines up to €15M or 3% of turnover. <b>OpenAI</b> requires telling listeners the voice is AI-generated. <b>Google</b> embeds an invisible SynthID watermark in audio from its own models.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Для ДЗ: в конце ролика титр «Голос и музыка: сгенерированы ИИ (сервисы)». Слева светофор для голоса. Зелёный: готовый голос из библиотеки или придуманный по описанию, по лицензии сервиса и с пометкой «создано ИИ». Жёлтый: ваш собственный голос или клон коллеги, только с письменным согласием, где сказано, для чего, где, как долго и как отозвать согласие. Красный: голос клиента, руководителя, публичного человека; без письменного согласия и юристов нельзя. Голосовые клоны используют для мошенничества: звонок «от директора» с просьбой срочно перевести деньги.",
                      "⏱ 4 min. For the homework: an end caption “Voice and music: AI-generated (services)”. On the left is a traffic light for voices. Green: a library voice or one designed from a description, under the service licence and with an “AI-generated” label. Amber: your own voice or a colleague’s clone, only with written consent that says the purpose, where, how long and how to withdraw. Red: a client’s, a manager’s or a public figure’s voice; not without written consent and legal review. Voice clones are used for fraud: a call “from the CEO” asking for an urgent transfer."),
                    t("Справа как сервисы проверяют согласие. OpenAI даёт клоны только одобренным клиентам, Google Cloud — по списку допуска; в Gemini API клонировать может любой разработчик, но только с записанной фразой согласия владельца голоса. ElevenLabs для профессионального клона просит владельца прочитать проверочный текст, для быстрого клона только галочку «у меня есть согласие». Azure выдаёт клоны по заявке и может сверить запись согласия с голосом. Открытые модели клонируют по нескольким секундам записи и ничего не проверяют. Значит, проверка согласия — ваша ответственность, а не сервиса.",
                      "On the right: how services check consent. OpenAI limits custom voices to eligible customers and Google Cloud to allow-listed ones; in the Gemini API any developer can replicate a voice, but only with the owner’s recorded consent phrase. ElevenLabs asks the owner to read a verification text for a professional clone, and only a checkbox for an instant clone. Azure grants clones on application and may match the consent recording to the voice. Open models clone from a few seconds and check nothing. So checking consent is your responsibility, not the service’s."),
                    t("Закон: статья 50 EU AI Act применяется с 2 августа 2026: синтетический звук и дипфейки нужно помечать, штраф до €15 млн или 3% оборота. OpenAI в правилах использования требует явно сообщать слушателю, что голос сгенерирован. Google ставит SynthID во весь звук своих моделей (Lyria, синтез речи Gemini), проверить можно в Gemini app, но только для контента Google. Для систем, уже выведенных на рынок, обязанность машиночитаемой маркировки по ст. 50(2) отложена до 2 декабря 2026. Риск мошенничества реален: по сообщениям прессы, в феврале 2026 итальянский банк Fideuram перевёл около €95 млн после звонка, в котором клонировали голос настоящего юриста.",
                      "Law: Article 50 of the EU AI Act applies from 2 August 2026: synthetic audio and deepfakes must be labelled, with fines up to €15M or 3% of turnover. OpenAI’s usage policies require a clear disclosure to listeners that the voice is AI-generated. Google embeds SynthID in all audio from its models (Lyria, Gemini speech); the Gemini app can check it, but only for Google content. For systems already on the market, the Art. 50(2) machine-readable marking obligation has a grace period to 2 December 2026. The fraud risk is real: according to press reports, in February 2026 the Italian bank Fideuram wired about €95M after a call in which a real lawyer’s voice was cloned.")))


def s_hw():
    return dict(min=7, html=f'''
  {head(t("Практика", "Practice"), t("Домашнее задание 6: озвучить свой ролик из L05", "Homework 6: voice your L05 video"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:44px;align-items:center;">
      <div class="stack" style="gap:18px;">
        <div class="track" style="--k:var(--cyan)"><img src="{IMG}poster_final.jpg" alt=""><div><div class="h">{t("Ваш ролик из L05", "Your L05 video")}</div><div class="d">{t("Трек А (товар) или Б (курьер, кейс Glovo). Нет ролика: возьмите курьерский ролик урока. В ролике нет звука: фон из шумов или музыки.", "Track A (product) or B (courier, Glovo case). If you have no video, use the lesson’s courier video. No sound in your video: build the background from effects or music.")}</div></div></div>
        <div class="files">genai-homeworks/L06/
├── script.md      <span class="cm"># {t("текст, текст для голоса, время", "text, spoken text, timing")}</span>
├── audio/         <span class="cm"># {t("реплики, подложка, сведение", "lines, bed, mix")}</span>
├── final_voiced.mp4
├── transcript.txt <span class="cm"># {t("распознанный текст", "speech-to-text output")}</span>
├── audio_spec.md
└── audio_qa.md</div>
      </div>
      <div class="stack" style="gap:14px;">
        <ol class="checklist">
          <li style="font-size:20px"><span>{t("<b>Сценарий</b>: 3 реплики, бюджет слов, критичные слова → <code>script.md</code>", "<b>Script</b>: 3 lines, word budget, critical terms → <code>script.md</code>")}</span></li>
          <li style="font-size:20px"><span>{t("<b>Текст для голоса</b>: числа и имена словами, инструкция стиля", "<b>Spoken text</b>: numbers and names as words, a style instruction")}</span></li>
          <li style="font-size:20px"><span>{t("<b>Голос</b> в двух сервисах без кода (например, ElevenLabs и Google AI Studio), выбрать лучший", "<b>Voice</b> in two no-code services (e.g. ElevenLabs and Google AI Studio), keep the better one")}</span></li>
          <li style="font-size:20px"><span>{t("<b>Фон</b>: звук видеомодели, шумы или музыка, с лицензией", "<b>Background</b>: video model audio, effects or music, with its licence")}</span></li>
          <li style="font-size:20px"><span>{t("<b>Сведение</b> в <code>final_voiced.mp4</code>: −14 ± 1 LUFS, скриншот измерителя", "<b>Mix</b> into <code>final_voiced.mp4</code>: −14 ± 1 LUFS, a meter screenshot")}</span></li>
          <li style="font-size:20px"><span>{t("<b>Проверка</b>: <code>transcript.txt</code>, чек-лист слайда 18 → <code>audio_qa.md</code>, стоимость → <code>audio_spec.md</code>", "<b>Check</b>: <code>transcript.txt</code>, slide 18 checklist → <code>audio_qa.md</code>, cost → <code>audio_spec.md</code>")}</span></li>
        </ol>
        <div class="small" style="font-size:18px">{t("Ревьюер: <b>ihar_rubanovich@epam.com</b>. Только свой голос или голоса из библиотек; чужие голоса не клонируем.", "Reviewer: <b>ihar_rubanovich@epam.com</b>. Your own voice or library voices only; do not clone anyone else’s voice.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. ДЗ повторяет пайплайн урока на вашем ролике из L05. Трек А — товар, трек Б — курьер. Если ролика нет, возьмите курьерский ролик урока из папки L05.",
                      "⏱ 7 min. The homework repeats the lesson pipeline on your L05 video. Track A: product, track B: courier. If you have no video, use the lesson’s courier video from the L05 folder."),
                    t("Шесть пунктов = шесть шагов урока. Порядок: сценарий на 3 реплики с бюджетом слов и колонкой «текст для голоса»; голос в двух сервисах без кода, например ElevenLabs и Google AI Studio (API или открытая модель по желанию), выбрать лучший по пунктам 1–2 чек-листа; фон: звук видеомодели, шумы или музыка, и указать лицензию; сведение в final_voiced.mp4 на −14 LUFS плюс-минус 1; прогнать итог через распознавание речи и сохранить transcript.txt; приёмка по чек-листу слайда 18 в audio_qa.md; сервисы, настройки и стоимость в audio_spec.md.",
                      "Six items = the six lesson steps. Order: a 3-line script with a word budget and a spoken-text column; the voice in two no-code services, for example ElevenLabs and Google AI Studio (an API or open model is optional), keep the better one by checklist items 1–2; a background: the video model’s audio, effects or music, with its licence; a mix into final_voiced.mp4 at −14 LUFS plus or minus 1; run the result through speech-to-text and save transcript.txt; the slide 18 checklist in audio_qa.md; services, settings and cost in audio_spec.md."),
                    t("Пометка: в конце ролика титр «Голос и музыка: сгенерированы ИИ (названия сервисов)» и та же строка в audio_spec.md. Правило согласия: только свой голос или голоса из библиотек. Голоса коллег, родственников и знаменитостей не клонируем даже «для теста». Оценивается разбор ошибок, а не идеальный звук. Подробности и шаблоны в файле ДЗ L06.",
                      "Label: an end caption “Voice and music: AI-generated (service names)” and the same line in audio_spec.md. Consent rule: your own voice or library voices only. Do not clone colleagues, relatives or celebrities, not even “for a test”. Grading is based on the error analysis, not on perfect sound. Details and templates are in the L06 homework file.")))


def s_summary():
    rules = [
        ("cyan", t("Сценарий с бюджетом слов", "Script with a word budget"), t("2–2,5 слова в секунду, по секунде тишины у склеек", "2–2.5 words per second, a second of silence at each cut")),
        ("green", t("Текст для голоса отдельно", "Spoken text kept separate"), t("числа, время, имена словами; стиль отдельной инструкцией", "numbers, times, names as words; style as a separate instruction")),
        ("amber", t("Голос с лицензией и согласием", "A voice with a licence and consent"), t("клон только с письменного согласия владельца", "a clone only with the owner’s written consent")),
        ("pink", t("Фон с известной лицензией", "Background with a known licence"), t("звук видео, шумы или музыка; MusicGen и бесплатный Suno некоммерческие", "video audio, effects or music; MusicGen and free Suno are non-commercial")),
        ("violet", t("Сведение к −14 LUFS", "Mix to −14 LUFS"), t("голос сверху, фон приглушён, истинный пик ≤ −1 дБ (dBTP)", "voice on top, background ducked, true peak ≤ −1 dB (dBTP)")),
        ("red", t("Проверка распознаванием и на слух", "Check with speech-to-text and by ear"), t("частота ошибок + критичные слова", "word error rate + critical terms")),
    ]
    rr = "".join(f'<div class="rule" style="--k:var(--{k})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>'
                 for i, (k, h, d) in enumerate(rules))
    return dict(min=3, html=f'''
  {head(t("Итоги", "Summary"), t("Итоги урока", "Lesson summary"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.4fr 1fr;gap:56px;align-items:center;">
      <div class="rules" style="gap:16px">{rr}</div>
      <div class="stack" style="gap:16px;">
        <img src="{IMG}poster_final.jpg" alt="" style="width:100%;border-radius:12px;border:1px solid var(--line)">
        <div class="note" style="--k:var(--violet)"><b>{t("Урок 07: GitHub, Microsoft 365 и Copilot.", "Lesson 07: GitHub, Microsoft 365 and Copilot.")}</b> {t("Из генерации контента переходим к ИИ в рабочих инструментах.", "From generating content to AI inside everyday work tools.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Шесть правил, по одному на шаг: сценарий с бюджетом слов; текст для голоса отдельно, числа и имена словами; голос с лицензией и согласием; фон с известной лицензией; сведение к −14 LUFS; проверка распознаванием и на слух.",
                      "⏱ 3 min. Six rules, one per step: a script with a word budget; spoken text kept separate, numbers and names as words; a voice with a licence and consent; a background with a known licence; mix to −14 LUFS; check with speech-to-text and by ear."),
                    t("Этим уроком закрываем модуль мультимодальности: картинка, видео, звук. Следующий урок, L07: GitHub, Microsoft 365 и Copilot. Вопросы.",
                      "This closes the multimodality module: image, video, sound. Next lesson, L07: GitHub, Microsoft 365 and Copilot. Questions.")))


SLIDES = [s_cover, s_hook, s_layers, s_tasks, s_how, s_video_audio, s_script, s_text, s_voice, s_music,
          s_mix, s_check, s_local, s_market, s_break, s_agent, s_econ, s_qa, s_risks, s_hw, s_summary]


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
    title = t("Урок 06: Речь и аудио | GenAI Basics", "Lesson 06: Speech and Audio | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<!-- generated by deck_v2/build.py; edit the generator, not this file -->
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
    print(f"{lang}: {OUT[lang].name}: {total} slides, {minutes} min")
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
