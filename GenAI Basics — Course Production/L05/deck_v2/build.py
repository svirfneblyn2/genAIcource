# -*- coding: utf-8 -*-
"""Build the L05 v2 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. Media come from ../assets/v2/ (see make_media.py).
Facts: ../L05_08_Source_Notes_Research_2026-10.md. Plan: ../L05_09_Deck_Fix_Plan_v2.md.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L05 = HERE.parent
NAME = "presentation_L05_Video_Generation"
OUT = {"ru": L05 / f"{NAME}_v2.html", "en": L05 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"
VID = "assets/v2/video/"

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 05 • Генерация видео", "en": "GenAI Basics • Lesson 05 • Video Generation"}


# ---------------------------------------------------------------- helpers
def video(name, poster, extra=""):
    label = t("▶ видео в HTML-версии", "▶ video in the HTML version")
    return (f'<div class="vid" {extra}><video src="{VID}{name}.mp4" poster="{IMG}{poster}.jpg" muted playsinline '
            f'preload="metadata" controls></video><img class="pp" src="{IMG}{poster}.jpg" alt="">'
            f'<span class="pl">{label}</span></div>')


def head(kicker, title, lead=None, k=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    s = f'<div class="kicker"{ks}>{kicker}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


TEAMS = {
    "ru": "Teams: при демонстрации экрана включите «Оптимизировать для движения и видео» (Optimize for motion and video), иначе видео пойдёт рывками. Ролик запускаем кликом, без звука.",
    "en": "Teams: when sharing your screen, turn on “Optimize for motion and video”, otherwise the clip will stutter. Start the clip with a click; it plays muted.",
}


def teams():
    return TEAMS[LANG]


# ---------------------------------------------------------------- camera schematics (static SVG)
def _cam(x, y, rot=0, ghost=False):
    st = 'stroke="#5f6e84"' if ghost else 'stroke="#38bdf8"'
    fill = "#5f6e84" if ghost else "#38bdf8"
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect x="-18" y="-12" width="26" height="24" rx="4" '
            f'fill="#0b0f17" {st} stroke-width="2.5"/><path d="M8 -7 L22 -13 L22 13 L8 7 Z" fill="{fill}"/></g>')


def _person_side(x, ground=118):
    return (f'<circle cx="{x}" cy="{ground - 40}" r="8" fill="#fbbf24"/>'
            f'<rect x="{x - 7}" y="{ground - 30}" width="14" height="30" rx="6" fill="#fbbf24"/>')


def _person_top(x, y):
    return f'<circle cx="{x}" cy="{y}" r="14" fill="#fbbf24"/><circle cx="{x}" cy="{y}" r="6" fill="#0b0f17" opacity=".35"/>'


def _ground():
    return '<line x1="10" y1="118" x2="230" y2="118" stroke="#2b3648" stroke-width="2"/>'


def cam_svg(kind, i):
    m = f"ah{i}"
    defs = (f'<defs><marker id="{m}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 Z" fill="#34d399"/></marker></defs>')
    a = f'stroke="#34d399" stroke-width="4" fill="none" marker-end="url(#{m})"'
    dash = 'stroke="#5f6e84" stroke-width="2" stroke-dasharray="5 5" fill="none"'
    if kind == "static":
        body = (_ground() + '<path d="M60 92 L46 118 M60 92 L60 118 M60 92 L74 118" stroke="#5f6e84" stroke-width="3"/>'
                + _cam(62, 78) + _person_side(178)
                + '<rect x="52" y="38" width="20" height="16" rx="3" fill="none" stroke="#34d399" stroke-width="3"/>'
                + '<path d="M56 38 v-6 a6 6 0 0 1 12 0 v6" fill="none" stroke="#34d399" stroke-width="3"/>')
    elif kind == "pan":
        body = (_cam(70, 70) + f'<line x1="92" y1="70" x2="210" y2="22" {dash}/><line x1="92" y1="70" x2="210" y2="118" {dash}/>'
                + f'<path d="M100 34 A 42 42 0 0 1 100 106" {a}/>'
                + '<circle cx="200" cy="40" r="7" fill="#fbbf24"/><circle cx="210" cy="72" r="7" fill="#fbbf24"/><circle cx="200" cy="102" r="7" fill="#fbbf24"/>')
    elif kind == "tilt":
        body = (_ground() + _cam(70, 96, -20) + f'<path d="M108 96 A 40 40 0 0 0 92 60" {a}/>'
                + '<rect x="160" y="20" width="44" height="98" rx="3" fill="none" stroke="#fbbf24" stroke-width="3"/>'
                + '<line x1="160" y1="45" x2="204" y2="45" stroke="#fbbf24" stroke-width="2"/><line x1="160" y1="70" x2="204" y2="70" stroke="#fbbf24" stroke-width="2"/>')
    elif kind == "dolly":
        body = (_cam(50, 62) + f'<line x1="80" y1="62" x2="158" y2="62" {a}/>' + _person_top(195, 62)
                + f'<line x1="150" y1="100" x2="80" y2="100" stroke="#5f6e84" stroke-width="3" stroke-dasharray="6 5" marker-end="url(#{m})"/>')
    elif kind == "track":
        body = (_person_top(95, 38) + f'<line x1="118" y1="38" x2="190" y2="38" stroke="#fbbf24" stroke-width="4"/>'
                + '<path d="M190 30 L204 38 L190 46 Z" fill="#fbbf24"/>'
                + _cam(95, 104, -90) + f'<line x1="120" y1="104" x2="196" y2="104" {a}/>'
                + f'<line x1="95" y1="84" x2="95" y2="56" {dash}/>')
    elif kind == "orbit":
        body = (f'<ellipse cx="118" cy="70" rx="78" ry="46" {dash}/>' + _person_top(118, 70)
                + _cam(196, 70, 180) + f'<path d="M190 46 A 78 46 0 0 0 126 24.5" {a}/>')
    elif kind == "crane":
        body = (_ground() + _person_side(190) + _cam(56, 100, 0, ghost=True)
                + f'<path d="M66 82 Q 70 38 112 32" {a}/>' + _cam(130, 34, 30))
    else:  # handheld
        body = (_cam(78, 66, 4) + '<path d="M50 34 l6 -6 l6 6 l6 -6 l6 6" fill="none" stroke="#38bdf8" stroke-width="2.5"/>'
                + '<path d="M86 30 l6 -6 l6 6 l6 -6" fill="none" stroke="#38bdf8" stroke-width="2.5"/>'
                + f'<path d="M40 108 q 12 -14 24 0 t 24 0 t 24 0 t 24 0" {a}/>' + _person_top(198, 66))
    return f'<svg viewBox="0 0 240 136" xmlns="http://www.w3.org/2000/svg">{defs}{body}</svg>'


# ---------------------------------------------------------------- slides
def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg"><img src="{IMG}cover_shot2.jpg" alt=""></div>
  <div class="shade"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 05 • Модуль 2: мультимодальность", "GenAI Basics • Lesson 05 • Module 2: multimodality")}</div>
    <h1>{t("Генерация видео", "Video Generation")}</h1>
    <h2>{t("От ключевого кадра к готовому ролику", "From a key frame to a finished clip")}</h2>
    <p>{t("Как видеомодель делает движение, почему «всё одним промптом» ломается и как собрать ролик из коротких шотов. Veo, Gemini Omni, Kling, Runway, Luma, Wan — по состоянию на октябрь 2026.",
           "How a video model creates motion, why “everything in one prompt” breaks, and how to build a clip from short shots. Veo, Gemini Omni, Kling, Runway, Luma, Wan — as of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. Сегодня второй урок модуля «мультимодальность»: в L04 мы делали картинки, сегодня оживляем их — делаем видео.",
                      "⏱ 2 min. Welcome. This is the second lesson of the multimodality module: in L04 we made images, today we bring them to life as video."),
                    t("План простой: смотрим готовый ролик, разбираем, как модель делает видео, на живом провале видим типичные ошибки, а потом шаг за шагом собираем ролик правильно. После перерыва — рынок, немного кода, деньги, приёмка и риски.",
                      "The plan: watch a finished clip, see how a model makes video, look at typical mistakes on a real failure, then build the clip properly step by step. After the break: the market, a little code, money, quality checks and risks."),
                    t("Перед стартом: " + TEAMS["ru"], "Before you start: " + TEAMS["en"])))


def s_hook():
    return dict(min=4, html=f'''
  {head(t("Начнём с результата", "Start with the result"), t("Этот ролик собран из трёх 8-секундных клипов", "This clip was built from three 8-second clips"), k="amber")}
  <div class="body">
    <div class="row" style="grid-template-columns:1.75fr 1fr;gap:48px;align-items:center;">
      {video("final", "poster_final")}
      <div class="stack" style="gap:30px;">
        <div class="stat" style="--k:var(--cyan)"><div class="n">3 {t("шота", "shots")}</div><div class="d">{t("каждый сделан из <b>готового кадра</b> (image-to-video)", "each made from a <b>ready key frame</b> (image-to-video)")}</div></div>
        <div class="stat" style="--k:var(--green)"><div class="n">8+8+8 → 23 {t("с", "s")}</div><div class="d">{t("склейка с двумя переходами по 0,5 с", "joined with two 0.5 s transitions")}</div></div>
        <div class="stat" style="--k:var(--amber)"><div class="n">≈ $10</div><div class="d">{t("3 × 8 с × $0.40 — прайс <b>Veo 3.1</b>, 720p, без учёта дублей", "3 × 8 s × $0.40 — <b>Veo 3.1</b> list price, 720p, retries not counted")}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:26px;--k:var(--amber)">{t("Сегодня разберём каждый шаг. И начнём с провала: что будет, если попросить всё это <b>одним промптом</b>.", "Today we take it apart step by step. And we start with a failure: what happens if you ask for all of it in <b>one prompt</b>.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Запустите ролик кликом (23 секунды), можно показать два раза. Спросите в чат: что здесь видно, сколько было «съёмок», где склейки?",
                      "⏱ 4 min. Start the clip with a click (23 seconds); you may play it twice. Ask the chat: what do you see, how many “takes” were there, where are the cuts?"),
                    t("Ответ: три отдельных клипа по 8 секунд из Veo 3.1, каждый сделан из заранее подготовленной картинки. Потом их склеили с переходами — получилось 23 секунды. По прайсу это около $10 без учёта неудачных попыток.",
                      "Answer: three separate 8-second clips from Veo 3.1, each made from a prepared image. Then they were joined with transitions — 23 seconds. At list price that is about $10, not counting failed attempts."),
                    t("Про звук одной фразой: клипы на самом деле со звуком — современные модели генерируют его сами. Сегодня смотрим без звука, звук подробно разберём в L06.",
                      "One sentence on sound: the clips actually have audio — modern models generate it themselves. Today we watch muted; sound is covered in L06."),
                    teams()))


def s_how():
    def pile(prefix, k, grid=False):
        imgs = "".join(f'<img src="{IMG}{prefix}_{i}.jpg" alt="">' for i in (2, 1, 0))
        ov = '<div class="grid-ov"></div>' if grid else ""
        return f'<div class="pile">{imgs}{ov}<div class="tax">{t("время →", "time →")}</div></div>'
    return dict(min=5, html=f'''
  {head(t("Под капотом • без формул", "Under the hood • no formulas"), t("Как модель делает видео", "How a model makes a video"), k="violet")}
  <div class="body">
    <div class="how">
      <div class="st" style="--k:var(--dim)">{pile("how_noise", "dim")}<div class="sh">{t("1. Шум", "1. Noise")}</div><div class="sd">{t("Старт — случайный шум сразу <b>на все кадры</b> клипа", "Start: random noise for <b>all frames</b> of the clip at once")}</div></div>
      <div class="ar">→</div>
      <div class="st" style="--k:var(--cyan)">{pile("how_half", "cyan", grid=True)}<div class="sh">{t("2. Очистка шагами", "2. Step-by-step cleanup")}</div><div class="sd">{t("Видео режется на кусочки «место в кадре × момент времени». Десятки шагов убирают шум; текст и первый кадр подсказывают на каждом шаге", "The video is cut into pieces “place in frame × moment in time”. Dozens of steps remove noise; the text and the first frame guide every step")}</div></div>
      <div class="ar">→</div>
      <div class="st" style="--k:var(--green)">{pile("how_clean", "green")}<div class="sh">{t("3. Кадры", "3. Frames")}</div><div class="sd">{t("24 кадра в секунду, согласованных между собой — поэтому движение плавное", "24 frames per second that agree with each other — that is why motion looks smooth")}</div></div>
    </div>
    <div class="plaque" style="margin-top:34px;"><b>{t("Физического движка внутри нет.", "There is no physics engine inside.")}</b> {t("Модель видела миллионы видео и знает, как движение <i>обычно выглядит</i>. Поэтому ошибается там, где нужны точные правила: <b>руки и предметы в контакте, текст, длинные сцены</b>.", "The model has seen millions of videos and knows what motion <i>usually looks like</i>. So it fails where exact rules matter: <b>hands and objects in contact, text, long scenes</b>.")}</div>
    <div class="small" style="margin-top:10px;">{t("Схема: кадры из нашего шота 2, шум добавлен для иллюстрации.", "Schematic: frames from our shot 2, noise added for illustration.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Связь с L04: картинка там тоже рождалась из шума за десятки шагов. Видео — то же самое, только модель чистит от шума сразу пачку кадров, а не один. Поэтому соседние кадры согласованы и движение плавное.",
                      "⏱ 5 min. Link to L04: there, an image was also born from noise in dozens of steps. Video is the same, but the model cleans a whole stack of frames at once instead of one. That is why neighbouring frames agree and motion is smooth."),
                    t("Чтобы было удобно считать, видео режут на маленькие кусочки — «вот этот угол кадра в этот момент времени». Текстовый промпт и, если есть, первый кадр подсказывают модели на каждом шаге.",
                      "To make the work manageable, the video is cut into small pieces — “this corner of the frame at this moment”. The text prompt and, if given, the first frame guide the model at every step."),
                    t("Главная мысль: модель не считает физику. Она видела много видео с паром, дождём, брызгами и научилась рисовать похоже. Исследования (например, Physics-IQ, 2025) показывают: красиво — не значит физически верно. Поэтому ждём ошибок в контактах (руки, пакет, руль), в тексте и в длинных сценах.",
                      "Key point: the model does not compute physics. It has seen many videos of steam, rain and splashes and learned to draw them convincingly. Research (e.g. Physics-IQ, 2025) shows that realistic-looking is not the same as physically correct. So expect errors in contacts (hands, a bag, handlebars), in text and in long scenes.")))


def s_fails():
    items = [
        ("fail_02_4", "00:02", t("Действие пропущено", "Action skipped"),
         t("пакет остался на стойке — в рюкзак его так и не положили", "the bag stays on the counter — it never goes into the backpack"), ""),
        ("fail_02_6_pair", "00:03", t("Детали поплыли после склейки", "Details drift after the cut"),
         t("надпись на коробе меняется: «Glono» → «Glovo»", "the logo on the box changes: “Glono” → “Glovo”"), "contain"),
        ("fail_05_0", "00:05", t("Пространство сломалось", "Space breaks"),
         t("руль с телефоном «въезжает» в кадр, а курьер всё ещё едет впереди", "handlebars with a phone slide in while the courier is still riding ahead"), ""),
        ("fail_07_0", "00:07", t("Псевдотекст", "Pseudo-text"),
         t("«Delivery Admest» вместо «Delivery Address»", "“Delivery Admest” instead of “Delivery Address”"), ""),
    ]
    cards = "".join(
        f'<div class="fail"><div class="im"><img class="{c}" src="{IMG}{f}.jpg" alt=""><span class="tc">{tc}</span></div>'
        f'<div class="ft">{h}</div><div class="fd">{d}</div></div>' for f, tc, h, d, c in items)
    return dict(min=6, html=f'''
  {head(t("Кейс • провал", "Case • failure"), t("Всё одним промптом: 4 типичные ошибки", "Everything in one prompt: 4 typical failures"), k="red")}
  <div class="body" style="margin-top:20px;">
    <div class="row" style="grid-template-columns:1fr 1.05fr;gap:36px;align-items:center;">
      <div class="stack" style="gap:14px;">
        <div class="vlabel"><span class="badge" style="--k:var(--red)">text-to-video</span>{t("Veo 3.1 • 8 с • только текст", "Veo 3.1 • 8 s • text only")}</div>
        {video("trainwreck", "poster_trainwreck")}
        <div><div class="prompt-label">{t("Промпт (сокращён)", "Prompt (shortened)")}</div><div class="prompt">Our friendly Glovo delivery courier enters a cozy Scandinavian cafe, … picks up a brown paper food delivery bag, puts it securely inside her turquoise backpack, <span style="color:var(--amber)">then cuts to</span> her riding a city bicycle through the rainy avenue at dusk … <span style="color:var(--amber)">and then</span> camera zooms in to a smartphone map …</div></div>
      </div>
      <div class="fails">{cards}</div>
    </div>
    <div class="note" style="margin-top:18px;--k:var(--red)">{t("Причина одна: на 8 секунд модели дали <b>3 сцены и 5 действий</b>.", "One cause: the model got <b>3 scenes and 5 actions</b> for 8 seconds.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Покажите клип кликом (8 секунд), затем пройдитесь по четырём кадрам. Промпт написан так, как пишут задание человеку: всё подряд в одном абзаце.",
                      "⏱ 6 min. Play the clip with a click (8 seconds), then walk through the four frames. The prompt is written the way you brief a person: everything in one paragraph."),
                    t("1) Действие пропущено: пакет в рюкзак так и не попал. 2) После склейки поплыли детали: надпись на коробе другая. Заодно видно, как модель портит бренд — «Glono» вместо названия; в коммерческом ролике это брак. 3) Пространство ломается: вместо нормальной смены плана руль с телефоном просто наезжает на кадр. 4) Текст на экране телефона — псевдобуквы.",
                      "1) Action skipped: the bag never goes into the backpack. 2) Details drift after the cut: the box logo changes. It also shows how a model damages a brand — “Glono” instead of the name; in a commercial clip that is a reject. 3) Space breaks: instead of a clean cut, the handlebars just slide over the shot. 4) The phone screen shows pseudo-letters."),
                    t("Вывод: модель не умеет «монтировать» по просьбе в тексте. Один клип — одна сцена и одно действие. Glovo здесь — название учебного кейса (как в ДЗ L04), логотип в клипе — пример того, как не надо.",
                      "Takeaway: a model cannot “edit” a film because the text asks it to. One clip = one scene and one action. Glovo is just the name of the training case (as in L04 homework); the logo in the clip is an example of what not to do."),
                    teams()))


def s_t2v_i2v():
    return dict(min=6, html=f'''
  {head(t("Главный приём урока", "The key technique"), t("Сначала кадр, потом движение", "First the frame, then the motion"), k="green")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;">
      <div class="stack" style="gap:12px;">
        <div class="vlabel"><span class="badge" style="--k:var(--red)">T2V</span>{t("Text-to-video: только текст", "Text-to-video: text only")}</div>
        {video("trainwreck", "poster_trainwreck")}
        <div class="flow" style="--k:var(--red)"><div class="box">{t("Текст", "Text")}</div><div class="arr">→</div><div class="box hl">{t("Модель решает <b>что в кадре</b><br>и <b>как оно движется</b>", "The model decides <b>what is in frame</b><br>and <b>how it moves</b>")}</div><div class="arr">→</div><div class="res">{t("✗ две задачи сразу", "✗ two tasks at once")}</div></div>
      </div>
      <div class="stack" style="gap:12px;">
        <div class="vlabel"><span class="badge" style="--k:var(--green)">I2V</span>{t("Image-to-video: готовый кадр + текст", "Image-to-video: ready frame + text")}</div>
        {video("shot1", "poster_shot1")}
        <div class="flow" style="--k:var(--green)"><div class="box">{t("Кадр ✓<br><small>+ текст о движении</small>", "Frame ✓<br><small>+ text about motion</small>")}</div><div class="arr">→</div><div class="box hl">{t("Модель решает<br>только <b>как оно движется</b>", "The model decides<br>only <b>how it moves</b>")}</div><div class="arr">→</div><div class="res">{t("✓ одна задача", "✓ one task")}</div></div>
      </div>
    </div>
    <div class="plaque g" style="margin-top:22px;"><b>{t("Правило:", "Rule:")}</b> {t("внешность, свет и композицию фиксируем в картинке (это навык L04). Видеомодели оставляем только движение.", "lock appearance, light and composition in an image (the L04 skill). Leave only motion to the video model.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Запустите оба клипа по очереди. Слева — только текст, справа — тот же курьерский сюжет, но модель получила готовую первую картинку.",
                      "⏱ 6 min. Play both clips one after another. Left: text only. Right: the same courier story, but the model got a ready first image."),
                    t("Простое объяснение: в T2V модель одновременно придумывает, как всё выглядит, и как оно движется — две неизвестные сразу. В I2V первая задача уже решена: картинка одобрена. Модели остаётся только движение, поэтому ошибок меньше и они предсказуемее.",
                      "Simple explanation: in T2V the model invents both how everything looks and how it moves — two unknowns at once. In I2V the first one is already solved: the image is approved. Only motion is left, so there are fewer errors and they are more predictable."),
                    t("Термины: T2V = text-to-video, I2V = image-to-video. Дальше в уроке используем эти сокращения.",
                      "Terms: T2V = text-to-video, I2V = image-to-video. We use these abbreviations for the rest of the lesson."),
                    teams()))


def s_refs():
    fs = 28
    def callout(x, y, txt, px, py, _w):
        w = int(len(txt) * t(15.6, 14.2) + 36)
        return (f'<line x1="{px}" y1="{py}" x2="{x + 30}" y2="{y + 24}" stroke="#38bdf8" stroke-width="3"/>'
                f'<circle cx="{px}" cy="{py}" r="8" fill="#38bdf8"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="50" rx="10" fill="#0b0f17" stroke="#38bdf8" stroke-width="2"/>'
                f'<text x="{x + 16}" y="{y + 35}" font-size="{fs}" font-weight="600" fill="#f1f5f9" font-family="Onest, Segoe UI, sans-serif">{txt}</text>')
    a = callout(20, 6, t("лицо, короткие кудри", "face, short curly hair"), 168, 160, t(330, 360))
    b = callout(760, 6, t("бирюзовый короб-рюкзак", "turquoise box backpack"), 925, 356, t(380, 370))
    c = callout(20, 864, t("жёлтая куртка, светоотражающая полоса", "yellow jacket, reflective stripe"), 165, 366, t(560, 470))
    d = callout(680, 864, t("чёрные брюки, белые кроссовки", "black trousers, white sneakers"), 500, 776, t(470, 460))
    svg = (f'<svg viewBox="0 0 1376 920" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block;">'
           f'<image href="{IMG}courier_sheet.jpg" x="0" y="76" width="1376" height="768"/>{a}{b}{c}{d}</svg>')
    return dict(min=4, html=f'''
  {head(t("Шаг 1 • референсы", "Step 1 • references"), t("Лист персонажа держит героя одинаковым", "A character sheet keeps the hero consistent"))}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:1.6fr 1fr;gap:40px;align-items:center;">
      <div>{svg}</div>
      <div class="stack" style="gap:22px;">
        <ul class="list">
          <li>{t("Референс <b>сужает выбор</b> модели: меньше места для «фантазии» о внешности.", "A reference <b>narrows the model’s choices</b>: less room to “invent” the look.")}</li>
          <li>{t("<b>Veo 3.1</b> — до 3 картинок-референсов; <b>Kling 3.0</b> — Elements, 2–4 картинки.", "<b>Veo 3.1</b> — up to 3 reference images; <b>Kling 3.0</b> — Elements, 2–4 images.")}</li>
          <li>{t("Стабильнее, но <b>не гарантировано</b> — каждый шот проверяем глазами.", "More stable, but <b>not guaranteed</b> — check every shot by eye.")}</li>
        </ul>
        <div class="row" style="grid-template-columns:1fr 1fr;gap:12px;flex:none;">
          <img src="{IMG}tl_shot1.jpg" alt="" style="width:100%;border-radius:8px;border:1px solid var(--line)">
          <img src="{IMG}tl_shot2.jpg" alt="" style="width:100%;border-radius:8px;border:1px solid var(--line)">
        </div>
        <div class="cap">{t("Результат: <b>тот же курьер</b> в шотах 1 и 2.", "Result: <b>the same courier</b> in shots 1 and 2.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Этот лист персонажа мы делали в L04: один человек в четырёх ракурсах. Выноски — «якоря», по которым зритель узнаёт героя: лицо и причёска, жёлтая куртка с полосой, бирюзовый короб, чёрные брюки и белые кроссовки.",
                      "⏱ 4 min. We made this character sheet in L04: one person from four angles. The callouts are “anchors” viewers recognise the hero by: face and hair, yellow jacket with a stripe, turquoise box backpack, black trousers and white sneakers."),
                    t("Референс не делает чудо, он просто сужает выбор модели. Где это есть: Veo 3.1 принимает до трёх картинок-референсов, Kling 3.0 — функция Elements (2–4 картинки). Результат стабильнее, но не гарантирован, поэтому в конце урока будет чек-лист приёмки.",
                      "A reference is not magic; it just narrows the model’s choices. Where it exists: Veo 3.1 takes up to three reference images, Kling 3.0 has Elements (2–4 images). Results are more stable but not guaranteed, which is why we end with a checklist."),
                    t("Внизу справа — кадры из наших шотов 1 и 2: курьер узнаваем.", "Bottom right: frames from our shots 1 and 2 — the courier is recognisable.")))


def s_keyframe():
    return dict(min=4, html=f'''
  {head(t("Шаг 2 • ключевой кадр", "Step 2 • key frame"), t("Ключевой кадр доводим в чате, а не в видео", "Perfect the key frame in chat, not in video"))}
  <div class="body">
    <div class="kf">
      <figure><img src="{IMG}knight_sprite.jpg" alt="" style="width:170px;align-self:center"><figcaption><b>{t("Спрайт", "Sprite")}</b> — {t("исходник из игры", "game source art")}</figcaption></figure>
      <div class="ar">→</div>
      <figure><img src="{IMG}knight_draft.jpg" alt=""><div class="bub">{t("«Сделай реалистичный кадр 16:9 по этому спрайту»", "“Make a realistic 16:9 frame from this sprite”")}</div><figcaption><b>{t("Черновик", "Draft")}</b> — {t("не тот шлем и накидка", "wrong helmet and tabard")}</figcaption></figure>
      <div class="ar">→</div>
      <figure><img src="{IMG}knight_approved.jpg" alt=""><div class="bub">{t("«Руки без защиты, накидка в бело-синие прямоугольники, шлем — плоский „котелок“»", "“Bare hands, tabard in white and blue rectangles, a flat ‘kettle’ helmet”")}</div><figcaption><b style="color:var(--green)">{t("Одобрено ✓", "Approved ✓")}</b> — {t("это первый кадр для видео", "the first frame for video")}</figcaption></figure>
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:36px;">
      <div class="stat" style="--k:var(--green)"><div class="n">{t("секунды · центы", "seconds · cents")}</div><div class="d">{t("одна правка <b>картинки</b> в чате", "one <b>image</b> edit in chat")}</div></div>
      <div class="stat" style="--k:var(--red)"><div class="n">{t("минуты · $0.40/с", "minutes · $0.40/s")}</div><div class="d">{t("одна перегенерация <b>видео</b> (Veo 3.1, 720p)", "one <b>video</b> regeneration (Veo 3.1, 720p)")}</div></div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Короткий пример из L04: из маленького игрового спрайта получаем реалистичный кадр. Первый вариант почти хорош, но шлем и накидка не те. Одна точная правка словами — и кадр одобрен.",
                      "⏱ 4 min. A short example in the style of L04: from a small game sprite we get a realistic frame. The first version is close, but the helmet and tabard are wrong. One precise text edit — and the frame is approved."),
                    t("Почему это важно для видео: каждую ошибку дешевле исправить в картинке. Правка картинки — секунды и центы. Перегенерация видео — минуты ожидания и, например, $0.40 за каждую секунду в Veo 3.1. Так что сначала доводим картинку до «да», потом анимируем.",
                      "Why this matters for video: every mistake is cheaper to fix in the image. An image edit costs seconds and cents. A video regeneration costs minutes of waiting and, for example, $0.40 per second in Veo 3.1. So get the image to “yes” first, then animate it.")))


def s_prompt():
    slots = [
        ("cyan", "1", t("Камера", "Camera"), "Dynamic tracking shot moving forward alongside the courier."),
        ("amber", "2", t("Кто", "Who"), "The same courier with short cropped curly hair"),
        ("green", "3", t("Действие", "Action"), "pedals her bicycle forward"),
        ("violet", "4", t("Где и когда", "Where & when"), "through the rain-slicked city avenue at twilight."),
        ("pink", "5", t("Детали движения", "Motion details"), "Wheels spinning smoothly forward with water spray cutting through shallow puddles."),
        ("red", "6", t("Свет", "Light"), "Wet cobblestones reflecting warm shop lights and streetlamps."),
    ]
    text = " ".join(f'<span style="--k:var(--{k})" data-n="{n}">{s}</span>' for k, n, _, s in slots)
    legend = "".join(f'<div class="slot" style="--k:var(--{k})"><i>{n}</i>{name}</div>' for k, n, name, _ in slots)
    return dict(min=6, html=f'''
  {head(t("Шаг 3 • промпт", "Step 3 • prompt"), t("Промпт режиссёра: 6 слотов движения", "The director’s prompt: 6 motion slots"))}
  <div class="body" style="margin-top:20px;">
    <div class="slots">{legend}</div>
    <div class="row" style="grid-template-columns:1.9fr 1fr;gap:32px;flex:none;margin-top:18px;align-items:start;">
      <div><div class="prompt-label">{t("Реальный промпт шота 2 (Veo 3.1, I2V)", "Actual prompt of shot 2 (Veo 3.1, I2V)")}</div><div class="dprompt">{text}</div></div>
      <div class="stack" style="gap:10px;">
        {video("shot2", "poster_shot2")}
        <div class="cap">{t("Результат — шот 2", "Result — shot 2")}</div>
      </div>
    </div>
    <ul class="list" style="margin-top:26px;">
      <li>{t("<b>Глаголы движения:</b> pedals, spinning, tracks — модели нужно знать, что меняется.", "<b>Motion verbs:</b> pedals, spinning, tracks — the model needs to know what changes.")}</li>
      <li>{t("<b>Не пересказывайте кадр:</b> он уже есть. Внешность — одной короткой приметой, чтобы не «уплыла».", "<b>Don’t retell the frame:</b> it is already there. Appearance — one short anchor so it doesn’t drift.")}</li>
      <li>{t("<b>Пишите, что должно быть.</b> Отдельное поле negative prompt есть не везде (есть в Kling, Wan).", "<b>Say what should happen.</b> A separate negative prompt field exists only in some tools (Kling, Wan).")}</li>
    </ul>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Это настоящий промпт, которым сделан шот 2. Разберите его по цветам: 1 — камера, 2 — кто, 3 — действие, 4 — где и когда, 5 — детали движения, 6 — свет. В L04 у картинки тоже было 6 слотов; в видео главное — камера, действие и детали движения.",
                      "⏱ 6 min. This is the actual prompt used for shot 2. Walk through the colours: 1 camera, 2 who, 3 action, 4 where and when, 5 motion details, 6 light. In L04 images also had 6 slots; in video the key ones are camera, action and motion details."),
                    t("Три правила. Первое — глаголы движения: модель должна понять, что меняется во времени. Второе — в I2V не описывайте заново всё, что видно на картинке; достаточно короткой приметы героя. Третье — формулируйте позитивно: что должно происходить. Отдельное поле «чего не должно быть» есть, например, в Kling и Wan; в Veo лучше писать позитивно.",
                      "Three rules. First, motion verbs: the model must understand what changes over time. Second, in I2V don’t describe again everything visible in the image; a short anchor for the hero is enough. Third, phrase it positively: what should happen. A separate “what not to show” field exists in Kling and Wan, for example; in Veo positive phrasing works better."),
                    teams()))


def s_camera():
    cams = [
        ("static", "Static", t("Статичная камера", "Locked-off camera"), "static camera, locked-off shot"),
        ("pan", "Pan", t("Поворот на месте", "Turn in place"), "slow pan left across the street"),
        ("tilt", "Tilt", t("Наклон вверх / вниз", "Tilt up / down"), "tilt up to the rooftops"),
        ("dolly", "Dolly in / out", t("Наезд / отъезд", "Move closer / away"), "slow dolly in to her face"),
        ("track", "Tracking", t("Едем рядом с героем", "Move alongside the hero"), "tracking shot alongside the courier"),
        ("orbit", "Orbit", t("Облёт вокруг объекта", "Circle around the subject"), "slow orbit around the mug"),
        ("crane", "Crane", t("Подъём камеры вверх", "Camera rises up"), "crane up over the street"),
        ("hand", "Handheld", t("С рук, лёгкая тряска", "Handheld, slight shake"), "handheld, slight shake"),
    ]
    cards = "".join(
        f'<div class="cam">{cam_svg(k, i)}<div class="ct">{ru}<span>{en}</span></div><div class="cp">“{p}”</div></div>'
        for i, (k, en, ru, p) in enumerate(cams))
    return dict(min=5, html=f'''
  {head(t("Шаг 3 • камера", "Step 3 • camera"), t("8 движений камеры, которые понимают модели", "8 camera moves that models understand"))}
  <div class="body" style="margin-top:18px;">
    <div class="cams">{cards}</div>
    <div class="note" style="margin-top:20px;">{t("Модели видели видео с подписями, поэтому понимают <b>операторские термины</b>. В чат-приложениях камеру задают только словами; в видеостудиях есть и отдельные настройки (Runway, Kling, Luma).", "Models were trained on captioned video, so they understand <b>camera terms</b>. In chat apps you set the camera with words only; video studios also have dedicated controls (Runway, Kling, Luma).")}</div>
    <div class="small" style="margin-top:8px;">{t("Схемы: вид сверху (Pan, Dolly, Tracking, Orbit) и сбоку (Static, Tilt, Crane). Камера — голубая, объект — жёлтый, движение — зелёная стрелка.", "Diagrams: top view (Pan, Dolly, Tracking, Orbit) and side view (Static, Tilt, Crane). Camera is blue, subject is yellow, motion is the green arrow.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Восемь базовых движений — словарь оператора. Пройдитесь по схемам: голубая — камера, жёлтый — объект, зелёная стрелка — куда движется камера. Под каждой схемой — готовая фраза для промпта на английском.",
                      "⏱ 5 min. Eight basic moves — a camera operator’s vocabulary. Walk through the diagrams: blue is the camera, yellow is the subject, the green arrow shows how the camera moves. Under each diagram is a ready English phrase for the prompt."),
                    t("Почему модели это понимают: они учились на видео с текстовыми описаниями, где такие слова встречались. Магии нет — это просто знакомые модели слова. Совет: одно движение камеры на шот; «pan + dolly + orbit» в одном клипе часто превращается в кашу.",
                      "Why models understand this: they learned from videos with text descriptions that used these words. No magic — just words the model has seen. Tip: one camera move per shot; “pan + dolly + orbit” in one clip often turns to mush."),
                    t("В чатах (Gemini, Flow) камеру задают словами. В видеостудиях есть отдельные настройки: в Runway — направление и сила движения по осям, в Kling — параметры камеры, в Luma — готовые «концепты» движений.",
                      "In chats (Gemini, Flow) you set the camera with words. Video studios have dedicated controls: Runway — direction and strength per axis, Kling — camera parameters, Luma — ready-made motion “concepts”.")))


def s_control():
    m = "mbA"
    ov = (f'<svg class="ov" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg"><defs><marker id="{m}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#34d399"/></marker></defs>'
          f'<path d="M800 230 L1080 230" stroke="#34d399" stroke-width="10" fill="none" marker-end="url(#{m})"/>'
          f'<path d="M560 640 Q 520 560 470 540" stroke="#34d399" stroke-width="8" fill="none" marker-end="url(#{m})"/>'
          f'<path d="M840 640 Q 900 570 960 560" stroke="#34d399" stroke-width="8" fill="none" marker-end="url(#{m})"/>'
          '<rect x="20" y="30" width="380" height="370" rx="14" fill="rgba(248,113,113,.12)" stroke="#f87171" stroke-width="5" stroke-dasharray="16 10"/></svg>')
    def tile(k, svg, h, d):
        return f'<div class="ctrl" style="--k:var(--{k})">{svg}<div><div class="h">{h}</div><div class="d">{d}</div></div></div>'
    s1 = ('<svg viewBox="0 0 150 84"><rect x="4" y="22" width="48" height="34" rx="4" fill="#16314a" stroke="#38bdf8" stroke-width="2"/>'
          '<rect x="98" y="22" width="48" height="34" rx="4" fill="#16314a" stroke="#38bdf8" stroke-width="2"/>'
          '<path d="M54 39 Q 75 6 96 39" stroke="#34d399" stroke-width="3" stroke-dasharray="5 4" fill="none"/>'
          '<text x="28" y="45" font-size="16" fill="#f1f5f9" text-anchor="middle" font-family="JetBrains Mono, monospace">A</text>'
          '<text x="122" y="45" font-size="16" fill="#f1f5f9" text-anchor="middle" font-family="JetBrains Mono, monospace">B</text></svg>')
    s2 = ('<svg viewBox="0 0 150 84"><rect x="4" y="28" width="40" height="28" rx="3" fill="#38bdf8"/>'
          '<rect x="48" y="28" width="30" height="28" rx="3" fill="rgba(56,189,248,.55)"/>'
          '<rect x="82" y="28" width="30" height="28" rx="3" fill="rgba(56,189,248,.3)"/>'
          '<rect x="116" y="28" width="30" height="28" rx="3" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/></svg>')
    s3 = ('<svg viewBox="0 0 150 84"><rect x="6" y="6" width="26" height="20" rx="3" fill="#fbbf24"/>'
          '<rect x="6" y="32" width="26" height="20" rx="3" fill="#34d399"/><rect x="6" y="58" width="26" height="20" rx="3" fill="#c084fc"/>'
          '<path d="M40 42 L80 42" stroke="#5f6e84" stroke-width="3"/><path d="M78 35 L90 42 L78 49 Z" fill="#5f6e84"/>'
          '<rect x="96" y="20" width="50" height="44" rx="4" fill="#16314a" stroke="#38bdf8" stroke-width="2"/></svg>')
    return dict(min=4, html=f'''
  {head(t("Шаг 4 • точный контроль", "Step 4 • precise control"), t("Что можно задать точнее, чем словами", "What you can control more precisely than with words"))}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:36px;align-items:center;">
      <div class="stack" style="gap:10px;">
        <div class="anno"><img src="{IMG}motion_brush.jpg" alt="">{ov}
          <div class="callout" style="--k:var(--green);right:2%;top:38%;">{t("стрелка-траектория:<br>куда едет курьер", "trajectory arrow:<br>where the courier goes")}</div>
          <div class="callout" style="--k:var(--green);left:2%;bottom:4%;">{t("брызги из лужи", "splashes from the puddle")}</div>
          <div class="callout" style="--k:var(--red);left:4%;top:58%;">{t("статичная зона:<br>фон не двигается", "static zone:<br>background stays still")}</div>
        </div>
        <div class="cap">{t("<b>Motion Brush</b> (Kling): до 6 выделенных элементов, у каждого своя стрелка + статичная зона. Есть в моделях Kling 1.x–2.x; в списке функций Kling 3.0 его нет.", "<b>Motion Brush</b> (Kling): up to 6 selected elements, each with its own arrow, plus a static zone. Available on Kling 1.x–2.x models; not in the Kling 3.0 feature list.")}</div>
      </div>
      <div class="stack" style="gap:16px;">
        {tile("cyan", s1, t("Первый + последний кадр", "First + last frame"), t("Модель достраивает движение между двумя картинками. <b>Veo 3.1, Gemini Omni, Kling 3.0</b>", "The model fills in the motion between two images. <b>Veo 3.1, Gemini Omni, Kling 3.0</b>"))}
        {tile("green", s2, t("Продление клипа", "Extend a clip"), t("<b>Veo 3.1:</b> +7 с за шаг, до 148 с<br><b>Gemini Omni:</b> +10 с за шаг, до 40 с", "<b>Veo 3.1:</b> +7 s per step, up to 148 s<br><b>Gemini Omni:</b> +10 s per step, up to 40 s"))}
        {tile("amber", s3, t("Референсы героя", "Hero references"), t("<b>Veo 3.1:</b> до 3 картинок<br><b>Kling 3.0 Elements:</b> 2–4 картинки", "<b>Veo 3.1:</b> up to 3 images<br><b>Kling 3.0 Elements:</b> 2–4 images"))}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Слова — не единственный руль. Слева — идея локального контроля: выделяем кистью части кадра и рисуем стрелку, куда они двигаются; фон помечаем статичной зоной. Так это устроено в Motion Brush у Kling (до 6 элементов, стрелки на плоскости кадра). Честно: это функция старших моделей Kling 1.x–2.x, в описании Kling 3.0 её нет.",
                      "⏱ 4 min. Words are not the only steering wheel. On the left is the idea of local control: brush over parts of the frame and draw an arrow for where they move; mark the background as a static zone. That is how Kling’s Motion Brush works (up to 6 elements, arrows drawn on the image). To be honest, it belongs to Kling 1.x–2.x models; Kling 3.0’s description doesn’t list it."),
                    t("Справа — что реально массово есть в 2026: первый и последний кадр (модель сама строит путь между двумя картинками), продление клипа шагами (Veo 3.1 — по 7 секунд до 148, Gemini Omni — по 10 до 40) и референсы героя.",
                      "On the right is what is widely available in 2026: first and last frame (the model builds the path between two images), extending a clip in steps (Veo 3.1 — 7 s at a time up to 148 s, Gemini Omni — 10 s up to 40 s) and hero references."),
                    t("Схема на картинке — иллюстрация идеи, а не скриншот интерфейса.", "The overlay is an illustration of the idea, not an interface screenshot.")))


def s_montage():
    x0, x1, dur = 70, 1400, 23.0
    sc = (x1 - x0) / dur
    X = lambda s: x0 + s * sc  # noqa: E731
    lanes = [(0, 8, "tl_shot1", t("Шот 1 · кафе", "Shot 1 · cafe"), "#38bdf8"),
             (7.5, 15.5, "tl_shot2", t("Шот 2 · дождь", "Shot 2 · rain"), "#34d399"),
             (15.0, 23.0, "tl_shot3", t("Шот 3 · карта", "Shot 3 · map"), "#c084fc")]
    g = []
    for i, (a, b, img, lab, col) in enumerate(lanes):
        y = 20 + i * 78
        g.append(f'<rect x="{X(a):.1f}" y="{y}" width="{(b - a) * sc:.1f}" height="64" rx="8" fill="{col}" fill-opacity=".18" stroke="{col}" stroke-width="2.5"/>')
        g.append(f'<clipPath id="cp{i}"><rect x="{X(a) + 4:.1f}" y="{y + 4}" width="100" height="56" rx="5"/></clipPath>')
        g.append(f'<image href="{IMG}{img}.jpg" x="{X(a) + 4:.1f}" y="{y + 4}" width="100" height="56" preserveAspectRatio="xMidYMid slice" clip-path="url(#cp{i})"/>')
        g.append(f'<text x="{X(a) + 118:.1f}" y="{y + 40}" font-size="22" font-weight="700" fill="#f1f5f9" font-family="Onest, Segoe UI, sans-serif">{lab} · 8 {t("с", "s")}</text>')
    for a, lab in [(7.5, t("переход 0,5 с", "0.5 s transition")), (15.0, t("переход 0,5 с", "0.5 s transition"))]:
        g.append(f'<rect x="{X(a):.1f}" y="10" width="{0.5 * sc:.1f}" height="244" fill="#fbbf24" fill-opacity=".35"/>')
        g.append(f'<text x="{X(a + 0.25):.1f}" y="276" font-size="18" fill="#fbbf24" text-anchor="middle" font-family="Onest, Segoe UI, sans-serif">{lab}</text>')
    g.append(f'<line x1="{x0}" y1="300" x2="{x1}" y2="300" stroke="#5f6e84" stroke-width="2"/>')
    for s in [0, 4, 8, 12, 16, 20, 23]:
        g.append(f'<line x1="{X(s):.1f}" y1="294" x2="{X(s):.1f}" y2="306" stroke="#5f6e84" stroke-width="2"/>')
        g.append(f'<text x="{X(s):.1f}" y="330" font-size="18" fill="#9aa8bc" text-anchor="middle" font-family="JetBrains Mono, monospace">{s} {t("с", "s")}</text>')
    svg = f'<svg viewBox="0 0 1460 340" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block;">{"".join(g)}</svg>'
    return dict(min=5, html=f'''
  {head(t("Шаг 5 • монтаж", "Step 5 • editing"), t("Короткие шоты + склейка вместо одного длинного дубля", "Short shots + editing instead of one long take"), k="green")}
  <div class="body" style="margin-top:14px;">
    {svg}
    <div class="row" style="grid-template-columns:1.25fr 1fr;gap:40px;flex:none;margin-top:18px;align-items:center;">
      <div class="stack" style="gap:16px;">
        <div class="stat" style="--k:var(--green)"><div class="n">8 + 8 + 8 − {t("0,5 − 0,5", "0.5 − 0.5")} = 23 {t("с", "s")}</div><div class="d">{t("три клипа Veo 3.1 и два перехода: шторка и затемнение", "three Veo 3.1 clips and two transitions: a wipe and a fade through black")}</div></div>
        <div class="note" style="--k:var(--green)">{t("Склеить можно в любом редакторе (CapCut, DaVinci Resolve) или одной командой <code>ffmpeg</code>. Монтаж делает человек, а не модель.", "You can join clips in any editor (CapCut, DaVinci Resolve) or with one <code>ffmpeg</code> command. A person does the editing, not the model.")}</div>
      </div>
      {video("final", "poster_final")}
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Таймлайн нашего итогового ролика по реальным файлам: три клипа по 8 секунд, переходы по полсекунды накладываются на края клипов. Поэтому 8 + 8 + 8 даёт не 24, а 23 секунды.",
                      "⏱ 5 min. The timeline of our final clip from the real files: three 8-second clips, half-second transitions overlap the clip edges. That is why 8 + 8 + 8 gives 23 seconds, not 24."),
                    t("Мысль урока: модель хорошо делает один короткий план. Историю из нескольких планов собирает человек в монтаже. Короткие шоты стабильнее длинных, и если один шот не удался, переделываем только его.",
                      "The lesson’s point: a model is good at one short shot. A person builds a multi-shot story in editing. Short shots are more stable than long ones, and if one shot fails, you redo only that one."),
                    t("Справа можно ещё раз запустить итог. " + TEAMS["ru"], "You can replay the final clip on the right. " + TEAMS["en"])))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут на кофе и отдых для глаз", "5 minutes for coffee and resting your eyes")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: рынок моделей, как это выглядит в коде, сколько стоит, как принимать видео и какие риски.", "Next: the model market, what it looks like in code, what it costs, how to check video and what the risks are.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт». Только отдых, без заданий в чате.", "⏱ 5 min. Press “Start”. Rest only, no chat tasks.")))


def s_market():
    def chips(on):
        names = [("a", t("звук", "audio")), ("i", t("кадр→видео", "image→video")), ("p", "API"), ("o", t("открытые веса", "open weights"))]
        return '<div class="chipset">' + "".join(
            f'<span class="chip{" ow" if c == "o" else ""}{" on" if c in on else ""}">{n}{"*" if c == "a" and "a*" in on else ""}</span>'
            for c, n in names) + "</div>"
    rows = [
        ("Gemini Omni 1.1 Flash", "Google", 10, t("+ продление до 40 с", "+ extend to 40 s"), {"a", "a*", "i", "p"}, "#1 LMArena"),
        ("Veo 3.1", "Google", 8, t("+ продление до 148 с · наши клипы", "+ extend to 148 s · our clips"), {"a", "i", "p"}, ""),
        ("Kling 3.0", "Kuaishou", 15, t("4.0 до 30 с — ранний доступ", "4.0 up to 30 s — early access"), {"a", "i", "p"}, ""),
        ("Seedance 2.5", "ByteDance", 30, "", {"a", "i", "p"}, ""),
        ("Wan 3.0", "Alibaba", 30, "", {"a", "i", "p"}, t("#1 AA со звуком", "#1 AA with audio")),
        ("Hailuo H3", "MiniMax", 15, "", {"a", "i", "p"}, ""),
        ("Ray3.2", "Luma", 10, "", {"i", "p"}, ""),
        ("LTX-2", "Lightricks", 20, "", {"a", "o"}, ""),
        ("Wan 2.2", "Alibaba", 5, "", {"i", "o"}, ""),
    ]
    def pct(s):
        return s / 32 * 100
    head_row = ('<div class="mrow head"><div class="small">' + t("Модель", "Model") + '</div><div class="ticks">'
                + "".join(f'<span style="left:{pct(s):.2f}%">{s} {t("с", "s")}</span>' for s in (0, 10, 20, 30))
                + '</div><div class="small">' + t("Что умеет", "Capabilities") + '</div></div>')
    body = []
    for nm, v, sec, ext, on, rk in rows:
        gl = "".join(f'<i class="gridl" style="left:{pct(s):.2f}%"></i>' for s in (10, 20, 30))
        rk_html = f'<span class="rk">{rk}</span>' if rk else ""
        inside = sec >= 25
        pos = f"calc({pct(sec):.2f}% - 10px)" if inside else f"calc({pct(sec):.2f}% + 10px)"
        body.append(f'<div class="mrow"><div class="nm">{nm}<small>{v}</small>{rk_html}</div><div class="track">{gl}'
                    f'<div class="bar" style="width:{pct(sec):.2f}%"></div><div class="bv{" in" if inside else ""}" style="left:{pos}">'
                    f'{sec} {t("с", "s")}<small>{ext}</small></div></div>{chips(on)}</div>')
    sora = (f'<div class="mrow closed"><div class="nm">Sora 2<small>OpenAI</small></div><div class="track"><div class="bv" style="left:0;color:var(--red)">'
            f'{t("закрыта: приложение — 26.04.2026, API — 24.09.2026, замены нет", "shut down: app 26.04.2026, API 24.09.2026, no replacement")}</div></div><div></div></div>')
    return dict(min=7, html=f'''
  {head(t("Рынок • октябрь 2026", "Market • October 2026"), t("Видеомодели: длина одного клипа и что они умеют", "Video models: length of one clip and what they can do"), k="amber")}
  <div class="body" style="margin-top:6px;">
    <div class="mkt">{head_row}{"".join(body)}{sora}</div>
    <div class="small" style="margin-top:8px;">{t("Полоса — максимум за одну генерацию. Подсвеченный значок — есть; серый — нет или не подтверждено. * звук у Omni — по сторонним обзорам. Рейтинги: LMArena от 21.09.2026, Artificial Analysis (со звуком) — октябрь 2026. Runway и Leonardo — площадки, где доступны многие из этих моделей.", "Bar = maximum per generation. Highlighted chip = yes; grey = no or not confirmed. * Omni audio — per third-party reviews. Rankings: LMArena 21.09.2026, Artificial Analysis (with audio) — October 2026. Runway and Leonardo are platforms that host many of these models.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. Как читать: полоса — сколько секунд даёт одна генерация; справа — что модель умеет. Что изменилось за год: звук стал нормой почти у всех, а типичная длина клипа выросла с 5–10 до 10–30 секунд.",
                      "⏱ 7 min. How to read it: the bar is how many seconds one generation gives; on the right, what the model can do. What changed in a year: audio became standard for almost everyone, and typical clip length grew from 5–10 to 10–30 seconds."),
                    t("Лидеры: у Google сейчас главная модель — Gemini Omni 1.1 Flash (№1 на LMArena 21.09.2026). Veo 3.1, которым сделаны наши клипы, по-прежнему работает в API и умеет продлевать клип до 148 секунд. На рейтинге Artificial Analysis со звуком первое место у Wan 3.0. Рейтинги расходятся и меняются каждый месяц — всегда смотрите дату.",
                      "Leaders: Google’s main model is now Gemini Omni 1.1 Flash (#1 on LMArena, 21.09.2026). Veo 3.1, which made our clips, still runs in the API and can extend a clip to 148 seconds. On the Artificial Analysis board with audio, Wan 3.0 is first. Boards disagree and change monthly — always check the date."),
                    t("Открытые веса (можно запустить у себя): Wan 2.2 и LTX-2. Новые Wan 2.5–3.0 — только через API. Sora от OpenAI закрыта: приложение — с 26 апреля, API — с 24 сентября 2026, замены нет; ChatGPT видео не делает.",
                      "Open weights (you can run them yourself): Wan 2.2 and LTX-2. Newer Wan 2.5–3.0 are API-only. OpenAI’s Sora is shut down: the app since 26 April, the API since 24 September 2026, with no replacement; ChatGPT does not make video."),
                    t("Перед занятием проверьте: вышел ли полный Kling 4.0 (план — октябрь 2026).", "Before class, check whether the full Kling 4.0 has shipped (planned for October 2026).")))


def s_code():
    code = (
        '<span class="kw">import</span> time\n'
        '<span class="kw">from</span> google <span class="kw">import</span> genai\n'
        '<span class="kw">from</span> google.genai <span class="kw">import</span> types\n\n'
        f'client = genai.<span class="fn">Client</span>()  <span class="cm"># {t("ключ из GEMINI_API_KEY", "key from GEMINI_API_KEY")}</span>\n'
        'op = client.models.<span class="fn">generate_videos</span>(\n'
        '    model=<span class="str">"veo-3.1-fast-generate-preview"</span>,\n'
        '    prompt=<span class="str">"Tracking shot alongside the courier"</span>,\n'
        '    image=types.Image.<span class="fn">from_file</span>(location=<span class="str">"shot2.png"</span>),\n)\n'
        f'<span class="kw">while not</span> op.done:  <span class="cm"># {t("ждём: от ~11 с до ~6 мин", "wait: ~11 s to ~6 min")}</span>\n'
        '    time.<span class="fn">sleep</span>(10)\n'
        '    op = client.operations.<span class="fn">get</span>(op)\n'
        'video = op.response.generated_videos[0].video\n'
        'client.files.<span class="fn">download</span>(file=video)\n'
        'video.<span class="fn">save</span>(<span class="str">"shot2.mp4"</span>)')
    bars = [("Veo 3.1", 0.40, "$3.20", "cyan"), ("Veo 3.1 Fast", 0.10, "$0.80", "green"), ("Veo 3.1 Lite", 0.05, "$0.40", "violet")]
    hb = "".join(
        f'<div class="hb" style="--k:var(--{k})"><div class="lab">{n}</div><div class="tr"><div class="b" style="width:{v / 0.4 * 42:.1f}%"></div>'
        f'<div class="v" style="left:calc({v / 0.4 * 42:.1f}% + 12px)">${v:.2f}<small>{t("8 с", "8 s")} = {c}</small></div></div></div>'
        for n, v, c, k in bars)
    return dict(min=3, html=f'''
  {head(t("Для справки • google-genai", "For reference • google-genai"), t("Как это выглядит в коде", "What it looks like in code"), k="violet")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.45fr 1fr;gap:40px;align-items:center;">
      <pre class="code">{code}</pre>
      <div class="stack" style="gap:24px;">
        <div class="stat" style="--k:var(--fg)"><div class="d" style="font-size:21px">{t("Три шага: <b>отправил → подождал → скачал</b>. Видео делается долго, поэтому ответ приходит не сразу.", "Three steps: <b>send → wait → download</b>. Video takes a while, so the answer does not come back immediately.")}</div></div>
        <div><div class="prompt-label">{t("Цена за секунду, 720p", "Price per second, 720p")}</div><div class="hbars sm">{hb}</div></div>
        <div class="small">{t("Gemini API, октябрь 2026. Бесплатного тарифа для Veo нет; платим только за успешные видео.", "Gemini API, October 2026. No free tier for Veo; you pay only for successful videos.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Слайд для справки, код не разбираем построчно. Идея: через Python-библиотеку google-genai (её мы использовали в L03 и L04) отправляем картинку и промпт, ждём, пока видео будет готово, и скачиваем файл.",
                      "⏱ 3 min. A reference slide; don’t go through the code line by line. The idea: with the google-genai Python library (used in L03 and L04) we send an image and a prompt, wait until the video is ready and download the file."),
                    t("Отличие от картинок: видео делается от десятков секунд до нескольких минут, поэтому сервис сразу возвращает «квитанцию», а мы раз в 10 секунд спрашиваем, готово ли. Цена — за секунду видео: Veo 3.1 — $0.40, Fast — $0.10, Lite — $0.05 при 720p. 8-секундный клип стоит $3.20, $0.80 или $0.40.",
                      "The difference from images: video takes from tens of seconds to several minutes, so the service immediately returns a “ticket” and we ask every 10 seconds whether it is ready. Price is per second of video: Veo 3.1 $0.40, Fast $0.10, Lite $0.05 at 720p. An 8-second clip costs $3.20, $0.80 or $0.40.")))


def s_econ():
    rows = [
        (t("Перебор T2V", "T2V trial and error"), t("10 попыток на шот × 3 шота × $3.20", "10 tries per shot × 3 shots × $3.20"), 96.0, "red"),
        (t("Кадр в чате + I2V", "Frame in chat + I2V"), t("3 попытки на шот × 3 шота × $3.20", "3 tries per shot × 3 shots × $3.20"), 28.8, "amber"),
        (t("То же на Veo 3.1 Fast", "Same on Veo 3.1 Fast"), t("3 попытки × 3 шота × $0.80", "3 tries × 3 shots × $0.80"), 7.2, "green"),
    ]
    hb = "".join(
        f'<div class="hb" style="--k:var(--{k})"><div class="lab">{n}<small>{f}</small></div><div class="tr"><div class="b" style="width:{v / 96 * 74:.1f}%"></div>'
        f'<div class="v" style="left:calc({v / 96 * 74:.1f}% + 14px)">${v:.2f}</div></div></div>' for n, f, v, k in rows)
    return dict(min=5, html=f'''
  {head(t("Экономика", "Economics"), t("Считаем секунды, а не попытки", "Count seconds, not attempts"), t("Ролик как наш: <b>3 шота по 8 секунд</b>, Veo 3.1, 720p.", "A clip like ours: <b>3 shots of 8 seconds</b>, Veo 3.1, 720p."), k="amber")}
  <div class="body">
    <div class="hbars">{hb}</div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:40px;">
      <div class="note" style="--k:var(--green)">{t("<b>Деньги экономит одобренный кадр:</b> меньше попыток на шот. Картинки для кадров стоят центы.", "<b>The approved frame saves money:</b> fewer tries per shot. Images for key frames cost cents.")}</div>
      <div class="note" style="--k:var(--violet)">{t("<b>Черновик — на дешёвой модели:</b> Veo 3.1 Lite — $0.05/с, Gemini Omni 360p — около трети цены 720p.", "<b>Drafts on a cheap model:</b> Veo 3.1 Lite — $0.05/s, Gemini Omni 360p — about a third of the 720p price.")}</div>
    </div>
    <div class="small" style="margin-top:14px;">{t("Число попыток — допущение для оценки. Цены Gemini API на октябрь 2026; оплачиваются только успешные генерации.", "The number of tries is an assumption for the estimate. Gemini API prices as of October 2026; only successful generations are billed.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Посчитаем на пальцах. В видео платят за секунду, поэтому каждая неудачная попытка — это деньги. Если перебирать T2V по 10 раз на шот, ролик из трёх 8-секундных шотов на Veo 3.1 обойдётся примерно в $96.",
                      "⏱ 5 min. Let’s do simple maths. In video you pay per second, so every failed attempt costs money. If you try T2V 10 times per shot, a clip of three 8-second shots on Veo 3.1 costs about $96."),
                    t("Если сначала довести кадр в чате (центы) и делать I2V, обычно хватает 2–3 попыток — около $29. А черновые попытки и вовсе можно делать на Fast или Lite: тот же объём на Fast — $7.20. Числа попыток — наше допущение, а цены — реальные из прайса Gemini API.",
                      "If you first perfect the frame in chat (cents) and use I2V, 2–3 attempts are usually enough — about $29. Drafts can run on Fast or Lite: the same volume on Fast is $7.20. The attempt counts are our assumption; the prices are real Gemini API prices.")))


def s_qa():
    return dict(min=5, html=f'''
  {head(t("Приёмка", "Quality check"), t("Приёмка видео — отдельный шаг", "Checking a video is a separate step"), t("Даже хороший I2V-клип надо смотреть покадрово. Ошибки из <b>наших же</b> шотов 2 и 3:", "Even a good I2V clip needs a frame-by-frame look. Defects from <b>our own</b> shots 2 and 3:"), k="green")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:36px;align-items:center;">
      <div class="stack" style="gap:14px;">
        <div class="row" style="grid-template-columns:1fr 1fr;gap:12px;flex:none;">
          <div class="qa-shot"><img src="{IMG}qa_shot3_a.jpg" alt=""><div class="ring" style="left:46%;top:8%;width:52%;height:50%"></div></div>
          <div class="qa-shot"><img src="{IMG}qa_shot3_b.jpg" alt=""><div class="ring" style="left:46%;top:8%;width:52%;height:50%"></div></div>
        </div>
        <div class="cap">{t("<b>Шот 3, 1,5 секунды разницы:</b> таймер прыгает 0:28 → 0:45, «Mep» вместо «Map», на иконке мопед, а курьер на велосипеде.", "<b>Shot 3, 1.5 seconds apart:</b> the timer jumps 0:28 → 0:45, “Mep” instead of “Map”, the icon is a moped while the courier rides a bicycle.")}</div>
        <div class="row" style="grid-template-columns:1fr 1fr;gap:12px;flex:none;align-items:center;">
          <div class="qa-shot"><img src="{IMG}qa_shot2_sign.jpg" alt=""><div class="ring" style="left:80%;top:2%;width:20%;height:14%"></div></div>
          <div class="cap">{t("<b>Шот 2:</b> вывеска «THABIK» — случайные буквы.", "<b>Shot 2:</b> the “THABIK” sign is random letters.")}</div>
        </div>
      </div>
      <div class="stack" style="gap:14px;">
        <div class="prompt-label">{t("Чек-лист приёмки", "Acceptance checklist")}</div>
        <ol class="checklist">
          <li><span>{t("<b>Руки и предметы</b> в контакте — не слипаются, не исчезают", "<b>Hands and objects</b> in contact — don’t merge or vanish")}</span></li>
          <li><span>{t("<b>Текст и цифры</b> — читаются и не прыгают", "<b>Text and numbers</b> — readable and stable")}</span></li>
          <li><span>{t("<b>Лицо и одежда</b> — как на референсе", "<b>Face and clothes</b> — match the reference")}</span></li>
          <li><span>{t("<b>Движение</b> — нужная скорость и направление (колёса вперёд)", "<b>Motion</b> — right speed and direction (wheels forward)")}</span></li>
          <li><span>{t("<b>Первый кадр</b> — совпадает с одобренным", "<b>First frame</b> — matches the approved one")}</span></li>
          <li><span>{t("<b>Стык шотов</b> — свет и цвет совпадают", "<b>Shot joins</b> — light and colour match")}</span></li>
        </ol>
        <div class="note" style="--k:var(--green)">{t("Этот же чек-лист — <b>рубрика домашнего задания</b>.", "This checklist is also the <b>homework rubric</b>.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Важный момент честности: наш «хороший» ролик тоже не идеален. В шоте 3 цифры таймера скачут, вместо Map написано Mep, а на иконке мопед, хотя курьер на велосипеде. В шоте 2 вывеска магазина — набор букв. Зритель может и не заметить, но заказчик заметит.",
                      "⏱ 5 min. An honest moment: our “good” clip is not perfect either. In shot 3 the timer digits jump, it says Mep instead of Map, and the icon is a moped although the courier rides a bicycle. In shot 2 the shop sign is random letters. Viewers may not notice, but a client will."),
                    t("Поэтому приёмка — отдельный шаг. Шесть пунктов чек-листа: руки и предметы, текст и цифры, лицо и одежда, движение, первый кадр, стык шотов. Смотрим на паузе и покадрово. Брак — переделываем только этот шот.",
                      "So checking is a separate step. Six checklist items: hands and objects, text and numbers, face and clothes, motion, first frame, shot joins. Watch paused and frame by frame. If something fails, redo only that shot."),
                    t("Совет: текст и цифры на экранах лучше добавлять при монтаже, а не просить у модели.", "Tip: add on-screen text and numbers during editing rather than asking the model for them.")))


def s_risks():
    return dict(min=6, html=f'''
  {head(t("Риски и происхождение", "Risks and provenance"), t("Кто сделал это видео — и можно ли это проверить", "Who made this video — and can you prove it"), k="red")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1fr 1.55fr;gap:40px;align-items:center;flex:none;">
      <div class="light" style="gap:18px">
        <div class="lrow" style="--k:var(--green)"><div class="dot"></div><div><div class="h">{t("Свои кадры и персонажи", "Your own frames and characters")}</div><div class="d">{t("можно — с пометкой «создано ИИ»", "OK — with an “AI-generated” label")}</div></div></div>
        <div class="lrow" style="--k:var(--amber)"><div class="dot"></div><div><div class="h">{t("Чужие бренды, логотипы, стили", "Other brands, logos, styles")}</div><div class="d">{t("только с разрешения и после юристов компании", "only with permission and after company lawyers review")}</div></div></div>
        <div class="lrow" style="--k:var(--red)"><div class="dot"></div><div><div class="h">{t("Реальные люди без согласия", "Real people without consent")}</div><div class="d">{t("нельзя: сотрудники, клиенты, публичные лица — только с письменного согласия", "no: employees, clients, public figures — only with written consent")}</div></div></div>
      </div>
      <div class="stack" style="gap:14px;">
        <div class="prompt-label">{t("Как метка переживает пересохранение", "How a mark survives re-saving")}</div>
        <div class="prov2">
          <div class="pb" style="grid-column:1;grid-row:1 / span 2">{t("Видео из Veo", "Video from Veo")}<small>{t("и других моделей Google", "and other Google models")}</small></div>
          <div class="arr" style="grid-column:2;grid-row:1 / span 2">→</div>
          <div class="pb k" style="--k:var(--green);grid-column:3;grid-row:1"><b>SynthID</b><small>{t("невидимый знак в самих пикселях", "invisible mark in the pixels")}</small></div>
          <div class="arr" style="grid-column:4;grid-row:1 / span 2">→</div>
          <div class="pb" style="border-style:dashed;grid-column:5;grid-row:1 / span 2">{t("Перекодирование, обрезка, скриншот", "Re-encoding, cropping, screenshot")}</div>
          <div class="arr" style="grid-column:6;grid-row:1 / span 2">→</div>
          <div class="res" style="--k:var(--green);grid-column:7;grid-row:1">{t("✓ обычно выживает", "✓ usually survives")}</div>
          <div class="pb k" style="--k:var(--cyan);grid-column:3;grid-row:2"><b>C2PA</b><small>{t("подпись в метаданных файла", "signature in the file metadata")}</small></div>
          <div class="res" style="--k:var(--red);grid-column:7;grid-row:2">{t("✗ легко теряется", "✗ easily lost")}</div>
        </div>
        <div class="note" style="--k:var(--green);font-size:20px">{t("<b>Проверка SynthID:</b> загрузить видео в приложение Gemini (до 100 МБ / 90 с). Находит только SynthID — видео других сервисов может не распознать.", "<b>SynthID check:</b> upload the video to the Gemini app (up to 100 MB / 90 s). It only finds SynthID — videos from other services may go unrecognised.")}</div>
      </div>
    </div>
    <div class="plaque" style="margin-top:40px;font-size:22px;"><b>EU AI Act, {t("ст. 50", "Art. 50")}:</b> {t("с 2 августа 2026 дипфейки нужно помечать; машиночитаемая маркировка для систем, выпущенных раньше, — с 2 декабря 2026. Штраф — до €15 млн или 3% оборота.", "since 2 August 2026 deepfakes must be labelled; machine-readable marking for systems released earlier — from 2 December 2026. Fines up to €15M or 3% of turnover.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Слева — светофор. Зелёный: свои сгенерированные кадры и персонажи, помечаем как созданные ИИ. Жёлтый: чужие бренды и логотипы — только с разрешения, решают юристы компании (вспомните «Glono» из провала). Красный: реальные люди — коллеги, клиенты, знаменитости — только с письменного согласия.",
                      "⏱ 6 min. On the left is a traffic light. Green: your own generated frames and characters, labelled as AI-made. Amber: other brands and logos — only with permission, decided by company lawyers (remember “Glono” from the failure). Red: real people — colleagues, clients, celebrities — only with written consent."),
                    t("Справа — как узнать, что видео сделано ИИ. У Google все видео Veo получают SynthID — невидимую метку прямо в пикселях. Она переживает сжатие и обрезку. C2PA — это подпись в метаданных файла; её легко потерять при пересохранении или скриншоте. Проверить SynthID можно, загрузив видео в приложение Gemini (до 100 МБ и 90 секунд). Важно: проверка находит только SynthID, поэтому видео других сервисов она может не распознать.",
                      "On the right: how to tell a video is AI-made. Google gives every Veo video SynthID — an invisible mark in the pixels. It survives compression and cropping. C2PA is a signature in the file metadata; it is easily lost on re-save or screenshot. You can check SynthID by uploading a video to the Gemini app (up to 100 MB and 90 seconds). Note: the check only finds SynthID, so videos from other services may not be recognised."),
                    t("Закон: в ЕС действует статья 50 AI Act — с 2 августа 2026 дипфейки нужно помечать, штраф до €15 млн или 3% оборота. В США с мая 2026 платформы обязаны удалять интимные дипфейки за 48 часов (TAKE IT DOWN Act).",
                      "Law: in the EU, Article 50 of the AI Act — since 2 August 2026 deepfakes must be labelled, fines up to €15M or 3% of turnover. In the US, since May 2026 platforms must remove intimate deepfakes within 48 hours (TAKE IT DOWN Act).")))


def s_hw():
    return dict(min=5, html=f'''
  {head(t("Практика • домашнее задание №5", "Practice • homework #5"), t("Оживить кадр из L04", "Bring an L04 frame to life"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:44px;align-items:center;">
      <div class="stack" style="gap:20px;">
        <div class="track" style="--k:var(--cyan)"><img class="contain" src="{IMG}packshot.jpg" alt=""><div><div class="h"><span class="mark">{t("Трек А", "Track A")}</span> · {t("товар", "product")}</div><div class="d">{t("5 секунд промо: облёт или наезд камеры. Форма и надписи товара не «плывут».", "5-second promo: an orbit or dolly-in. The product’s shape and text don’t drift.")}</div></div></div>
        <div class="track" style="--k:var(--green)"><img src="{IMG}poster_shot2.jpg" alt=""><div><div class="h"><span class="mark">{t("Трек Б", "Track B")}</span> · {t("курьер", "courier")}</div><div class="d">{t("Шот поездки: камера едет рядом. Лицо и форма — как на референсе.", "A riding shot: the camera moves alongside. Face and uniform match the reference.")}</div></div></div>
      </div>
      <div class="stack" style="gap:16px;">
        <ol class="checklist">
          <li style="font-size:23px"><span>{t("<b>T2V</b> одним промптом — для сравнения", "<b>T2V</b> in one prompt — for comparison")}</span></li>
          <li style="font-size:23px"><span>{t("<b>I2V</b> с кадром из L04 в <b>двух сервисах</b>", "<b>I2V</b> with your L04 frame in <b>two services</b>")}</span></li>
          <li style="font-size:23px"><span>{t("Промпты и настройки → <code>video_spec.md</code>", "Prompts and settings → <code>video_spec.md</code>")}</span></li>
          <li style="font-size:23px"><span>{t("Приёмка по чек-листу со слайда 16 → <code>video_qa.md</code>", "Check against the slide 16 checklist → <code>video_qa.md</code>")}</span></li>
        </ol>
        <div class="files">genai-homeworks/L05/
├── videos/  <span class="cm"># 01_t2v_trap, 02/03_i2v</span>
├── video_spec.md
└── video_qa.md</div>
        <div class="small" style="font-size:18px">{t("Ревьюер: <b>ihar_rubanovich@epam.com</b>. Бесплатных кредитов сервисов достаточно.", "Reviewer: <b>ihar_rubanovich@epam.com</b>. Free service credits are enough.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Два трека на выбор. А — оживить товар (пакшот из L04): короткий промо-ролик с облётом или наездом камеры. Б — продолжить историю курьера: шот поездки с камерой сбоку.",
                      "⏱ 5 min. Two tracks to choose from. A — animate a product (the L04 packshot): a short promo with an orbit or dolly-in. B — continue the courier story: a riding shot with the camera alongside."),
                    t("Обязательная часть: сначала честная попытка T2V одним промптом, потом I2V с вашим кадром в двух разных сервисах, промпты в video_spec.md и приёмка по чек-листу с прошлого слайда в video_qa.md. Оцениваем не красоту, а осознанность: видно ли, что вы понимаете, где и почему модель ошиблась.",
                      "Required: first an honest T2V attempt in one prompt, then I2V with your frame in two different services, prompts in video_spec.md and a check against the checklist in video_qa.md. We grade awareness, not beauty: can you show where and why the model went wrong."),
                    t("Подробности и шаблоны — в файле домашнего задания L05.", "Details and templates are in the L05 homework file.")))


def s_summary():
    rules = [
        ("cyan", t("Сначала кадр, потом движение", "First the frame, then the motion"), t("I2V с одобренной картинкой вместо T2V", "I2V with an approved image instead of T2V")),
        ("green", t("Один шот — одно действие", "One shot — one action"), t("4–8 секунд; историю собираем монтажом", "4–8 seconds; the story is built in editing")),
        ("violet", t("Промпт режиссёра", "The director’s prompt"), t("камера + действие + детали движения", "camera + action + motion details")),
        ("amber", t("Принимаем и считаем", "Check and count"), t("чек-лист на каждый клип; платим за секунды", "a checklist for every clip; you pay per second")),
    ]
    rr = "".join(f'<div class="rule" style="--k:var(--{k})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>'
                 for i, (k, h, d) in enumerate(rules))
    return dict(min=3, html=f'''
  {head(t("Итоги • мост к L06", "Summary • bridge to L06"), t("Четыре правила видео", "Four rules of video"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:56px;align-items:center;">
      <div class="rules">{rr}</div>
      <div class="stack" style="gap:16px;">
        <img src="{IMG}poster_final.jpg" alt="" style="width:100%;border-radius:12px;border:1px solid var(--line)">
        <div class="note" style="--k:var(--violet)"><b>{t("Урок 06: звук и речь.", "Lesson 06: sound and speech.")}</b> {t("Современные видеомодели уже генерируют звук сами — как им управлять, разберём в L06.", "Modern video models already generate sound themselves — how to control it is in L06.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Четыре правила одной строкой: сначала кадр, потом движение; один шот — одно действие; промпт режиссёра; приёмка по чек-листу и счёт секунд.",
                      "⏱ 3 min. Four rules in one line each: first the frame, then the motion; one shot — one action; the director’s prompt; check every clip and count seconds."),
                    t("Тизер: наши клипы на самом деле со звуком — Veo 3.1 сделал его сам. Как управлять звуком и речью — в следующем уроке, L06. Вопросы.",
                      "Teaser: our clips actually have sound — Veo 3.1 made it itself. How to control sound and speech is the next lesson, L06. Questions.")))


SLIDES = [s_cover, s_hook, s_how, s_fails, s_t2v_i2v, s_refs, s_keyframe, s_prompt, s_camera, s_control,
          s_montage, s_break, s_market, s_code, s_econ, s_qa, s_risks, s_hw, s_summary]


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
    title = t("Урок 05: Генерация видео | GenAI Basics", "Lesson 05: Video Generation | GenAI Basics")
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
