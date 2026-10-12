# -*- coding: utf-8 -*-
"""Build the L05 v2/v3 decks (RU + EN) and their PDFs.

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
    <h2>{t("От ключевого кадра к ролику из нескольких шотов", "From a key frame to a multi-shot video")}</h2>
    <p>{t("Как видеомодель генерирует движение, почему один длинный промпт ломается и как собрать историю из коротких шотов. Veo, Gemini Omni, Kling, Seedance, Runway, Leonardo. Данные на октябрь 2026.",
           "How a video model generates motion, why one long prompt fails, and how to build a story from short shots. Veo, Gemini Omni, Kling, Seedance, Runway, Leonardo. Data as of October 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. Сегодня второй урок модуля «мультимодальность»: в L04 мы делали картинки, сегодня оживляем их — делаем видео.",
                      "⏱ 2 min. Welcome. This is the second lesson of the multimodality module: in L04 we made images, today we bring them to life as video."),
                    t("План простой: смотрим готовый ролик, разбираем, как модель делает видео, на живом провале видим типичные ошибки, а потом шаг за шагом собираем ролик правильно. После перерыва — рынок, немного кода, деньги, приёмка и риски.",
                      "The plan: watch a finished clip, see how a model makes video, look at typical mistakes on a real failure, then build the clip properly step by step. After the break: the market, a little code, money, quality checks and risks."),
                    t("Перед стартом: " + TEAMS["ru"], "Before you start: " + TEAMS["en"])))


def s_hook():
    return dict(min=3, html=f'''
  {head(t("Пример", "Example"), t("Ролик 23 секунды из трёх шотов по 8 секунд", "A 23-second video built from three 8-second shots"), k="amber")}
  <div class="body">
    <div class="row" style="grid-template-columns:1.75fr 1fr;gap:48px;align-items:center;">
      {video("final", "poster_final")}
      <div class="stack" style="gap:30px;">
        <div class="stat" style="--k:var(--cyan)"><div class="n">3 {t("шота", "shots")}</div><div class="d">{t("каждый сделан из <b>готового ключевого кадра</b> (image-to-video)", "each generated from an <b>approved key frame</b> (image-to-video)")}</div></div>
        <div class="stat" style="--k:var(--green)"><div class="n">8+8+8 → 23 {t("с", "s")}</div><div class="d">{t("склейка с двумя переходами по 0,5 с", "joined with two 0.5 s transitions")}</div></div>
        <div class="stat" style="--k:var(--amber)"><div class="n">≈ $10</div><div class="d">{t("3 × 8 с × $0.40, прайс <b>Veo 3.1</b>, 720p, без учёта дублей", "3 × 8 s × $0.40, <b>Veo 3.1</b> list price, 720p, retakes not included")}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:26px;--k:var(--amber)">{t("Дальше: где генерировать, как работает модель, почему один промпт на всю историю ломается, и пайплайн из 5 шагов.", "Next: where to generate, how the model works, why one prompt for the whole story fails, and a 5-step pipeline.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Запустите ролик кликом (23 секунды), можно показать два раза. Спросите в чат: что здесь видно, сколько было «съёмок», где склейки?",
                      "⏱ 3 min. Start the clip with a click (23 seconds); you may play it twice. Ask the chat: what do you see, how many “takes” were there, where are the cuts?"),
                    t("Ответ: три отдельных клипа по 8 секунд из Veo 3.1, каждый сделан из заранее подготовленной картинки. Потом их склеили с переходами — получилось 23 секунды. По прайсу это около $10 без учёта неудачных попыток.",
                      "Answer: three separate 8-second clips from Veo 3.1, each made from a prepared image. Then they were joined with transitions into 23 seconds. At list price that is about $10, not counting failed attempts."),
                    t("Про звук одной фразой: клипы на самом деле со звуком — современные модели генерируют его сами. Сегодня смотрим без звука, звук подробно разберём в L06.",
                      "One sentence on sound: the clips have audio, because current models generate it themselves. Today we watch muted; sound is covered in L06."),
                    teams()))


def s_how():
    def pile(prefix, k, grid=False):
        imgs = "".join(f'<img src="{IMG}{prefix}_{i}.jpg" alt="">' for i in (2, 1, 0))
        ov = '<div class="grid-ov"></div>' if grid else ""
        return f'<div class="pile">{imgs}{ov}<div class="tax">{t("время →", "time →")}</div></div>'
    return dict(min=4, html=f'''
  {head(t("Принцип работы", "How it works"), t("Как диффузионная модель генерирует кадры видео", "How a diffusion model generates video frames"), k="violet")}
  <div class="body">
    <div class="how">
      <div class="st" style="--k:var(--dim)">{pile("how_noise", "dim")}<div class="sh">{t("1. Шум", "1. Noise")}</div><div class="sd">{t("Старт: случайный шум сразу <b>на все кадры</b> клипа", "Start: random noise for <b>all frames</b> of the clip at once")}</div></div>
      <div class="ar">→</div>
      <div class="st" style="--k:var(--cyan)">{pile("how_half", "cyan", grid=True)}<div class="sh">{t("2. Очистка шагами", "2. Step-by-step cleanup")}</div><div class="sd">{t("Видео режется на кусочки «место в кадре × момент времени». Десятки шагов убирают шум; текст и первый кадр подсказывают на каждом шаге", "The video is cut into pieces “place in frame × moment in time”. Dozens of steps remove noise; the text and the first frame guide every step")}</div></div>
      <div class="ar">→</div>
      <div class="st" style="--k:var(--green)">{pile("how_clean", "green")}<div class="sh">{t("3. Кадры", "3. Frames")}</div><div class="sd">{t("24 кадра в секунду, согласованные между собой, поэтому движение плавное", "24 frames per second that are consistent with each other, so motion looks smooth")}</div></div>
    </div>
    <div class="plaque" style="margin-top:34px;"><b>{t("Физического движка внутри нет.", "There is no physics engine inside.")}</b> {t("Модель видела миллионы видео и знает, как движение <i>обычно выглядит</i>. Поэтому ошибается там, где нужны точные правила: <b>руки и предметы в контакте, текст, длинные сцены</b>.", "The model has seen millions of videos and knows what motion <i>usually looks like</i>. So it fails where exact rules matter: <b>hands and objects in contact, text, long scenes</b>.")}</div>
    <div class="small" style="margin-top:10px;">{t("Схема: кадры из нашего шота 2, шум добавлен для иллюстрации.", "Schematic: frames from our shot 2, noise added for illustration.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Связь с L04: картинка там тоже рождалась из шума за десятки шагов. Видео — то же самое, только модель чистит от шума сразу пачку кадров, а не один. Поэтому соседние кадры согласованы и движение плавное.",
                      "⏱ 4 min. Link to L04: there, an image was also born from noise in dozens of steps. Video is the same, but the model cleans a whole stack of frames at once instead of one. That is why neighbouring frames agree and motion is smooth."),
                    t("Чтобы было удобно считать, видео режут на маленькие кусочки — «вот этот угол кадра в этот момент времени». Текстовый промпт и, если есть, первый кадр подсказывают модели на каждом шаге.",
                      "Internally the video is split into small patches: “this region of the frame at this moment”. The text prompt and, if given, the first frame guide the model at every step."),
                    t("Главная мысль: модель не считает физику. Она видела много видео с паром, дождём, брызгами и научилась рисовать похоже. Исследования (например, Physics-IQ, 2025) показывают: красиво — не значит физически верно. Поэтому ждём ошибок в контактах (руки, пакет, руль), в тексте и в длинных сценах.",
                      "Key point: the model does not compute physics. It has seen many videos of steam, rain and splashes and learned to draw them convincingly. Research (e.g. Physics-IQ, 2025) shows that realistic-looking is not the same as physically correct. So expect errors in contacts (hands, a bag, handlebars), in text and in long scenes.")))


def s_fails():
    items = [
        ("fail_02_4", "00:02", t("Действие пропущено", "Action skipped"),
         t("пакет остался на стойке, в рюкзак его так и не положили", "the bag stays on the counter and never goes into the backpack"), ""),
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
    return dict(min=5, html=f'''
  {head(t("Антипаттерн", "Anti-pattern"), t("Text-to-video, вся история в одном промпте: 4 типа ошибок", "Text-to-video, the whole story in one prompt: 4 failure types"), k="red")}
  <div class="body" style="margin-top:20px;">
    <div class="row" style="grid-template-columns:1fr 1.05fr;gap:36px;align-items:center;">
      <div class="stack" style="gap:14px;">
        <div class="vlabel"><span class="badge" style="--k:var(--red)">text-to-video</span>{t("Veo 3.1 • 8 с • только текст", "Veo 3.1 • 8 s • text only")}</div>
        {video("trainwreck", "poster_trainwreck")}
        <div><div class="prompt-label">{t("Промпт (сокращён)", "Prompt (shortened)")}</div><div class="prompt">Our friendly Glovo delivery courier enters a cozy Scandinavian cafe, … picks up a brown paper food delivery bag, puts it securely inside her turquoise backpack, <span style="color:var(--amber)">then cuts to</span> her riding a city bicycle through the rainy avenue at dusk … <span style="color:var(--amber)">and then</span> camera zooms in to a smartphone map …</div></div>
      </div>
      <div class="fails">{cards}</div>
    </div>
    <div class="note" style="margin-top:18px;--k:var(--red)">{t("Причина: на 8 секунд модели дали <b>3 сцены и 5 действий</b>.", "Root cause: <b>3 scenes and 5 actions</b> requested in 8 seconds.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Покажите клип кликом (8 секунд), затем пройдитесь по четырём кадрам. Промпт написан так, как пишут задание человеку: всё подряд в одном абзаце.",
                      "⏱ 5 min. Play the clip with a click (8 seconds), then walk through the four frames. The prompt is written the way you brief a person: everything in one paragraph."),
                    t("1) Действие пропущено: пакет в рюкзак так и не попал. 2) После склейки поплыли детали: надпись на коробе другая. Заодно видно, как модель портит бренд — «Glono» вместо названия; в коммерческом ролике это брак. 3) Пространство ломается: вместо нормальной смены плана руль с телефоном просто наезжает на кадр. 4) Текст на экране телефона — псевдобуквы.",
                      "1) Action skipped: the bag never goes into the backpack. 2) Details drift after the cut: the box logo changes. It also shows how a model damages a brand: “Glono” instead of the name. In a commercial clip that is a reject. 3) Space breaks: instead of a clean cut, the handlebars just slide over the shot. 4) The phone screen shows pseudo-letters."),
                    t("Вывод: модель не умеет «монтировать» по просьбе в тексте. Один клип — одна сцена и одно действие. Glovo здесь — название учебного кейса (как в ДЗ L04), логотип в клипе — пример того, как не надо.",
                      "Takeaway: a model cannot “edit” a film because the text asks it to. One clip = one scene and one action. Glovo is just the name of the training case (as in L04 homework); the logo in the clip is an example of what not to do."),
                    teams()))


def s_t2v_i2v():
    return dict(min=5, html=f'''
  {head(t("Два режима генерации", "Two generation modes"), t("Text-to-video и image-to-video", "Text-to-video vs image-to-video"), k="green")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;">
      <div class="stack" style="gap:12px;">
        <div class="vlabel"><span class="badge" style="--k:var(--red)">text-to-video</span>{t("на входе только текст", "input: text only")}</div>
        {video("trainwreck", "poster_trainwreck")}
        <div class="flow" style="--k:var(--red)"><div class="box">{t("Текст", "Text")}</div><div class="arr">→</div><div class="box hl">{t("Модель решает <b>что в кадре</b><br>и <b>как оно движется</b>", "The model decides <b>what is in frame</b><br>and <b>how it moves</b>")}</div><div class="arr">→</div><div class="res">{t("✗ две задачи сразу", "✗ two tasks at once")}</div></div>
      </div>
      <div class="stack" style="gap:12px;">
        <div class="vlabel"><span class="badge" style="--k:var(--green)">image-to-video</span>{t("на входе кадр + текст", "input: key frame + text")}</div>
        {video("shot1", "poster_shot1")}
        <div class="flow" style="--k:var(--green)"><div class="box">{t("Кадр ✓<br><small>+ текст о движении</small>", "Frame ✓<br><small>+ text about motion</small>")}</div><div class="arr">→</div><div class="box hl">{t("Модель решает<br>только <b>как оно движется</b>", "The model decides<br>only <b>how it moves</b>")}</div><div class="arr">→</div><div class="res">{t("✓ одна задача", "✓ one task")}</div></div>
      </div>
    </div>
    <div class="plaque g" style="margin-top:22px;"><b>{t("Правило:", "Rule:")}</b> {t("внешность, свет и композицию фиксируем в картинке (навык из L04). Видеомодель отвечает только за движение.", "fix appearance, light and composition in an image (the L04 skill). The video model handles only the motion.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Запустите оба клипа по очереди. Слева — только текст, справа — тот же курьерский сюжет, но модель получила готовую первую картинку.",
                      "⏱ 5 min. Play both clips one after another. Left: text only. Right: the same courier story, but the model got a ready first image."),
                    t("Простое объяснение: в T2V модель одновременно придумывает, как всё выглядит, и как оно движется — две неизвестные сразу. В I2V первая задача уже решена: картинка одобрена. Модели остаётся только движение, поэтому ошибок меньше и они предсказуемее.",
                      "Simple explanation: in text-to-video the model has to decide both how everything looks and how it moves, two unknowns at once. In image-to-video the first one is already solved by the approved image. Only motion is left, so there are fewer errors and they are more predictable."),
                    t("Термины: T2V = text-to-video, I2V = image-to-video. Дальше в уроке используем эти сокращения.",
                      "Terms: text-to-video means the input is only text; image-to-video means the input is a key frame plus text. Some tools abbreviate them as T2V and I2V."),
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
    return dict(min=3, html=f'''
  {head(t("Шаг 1 • референсы", "Step 1 • references"), t("Лист персонажа как референс для всех шотов", "Character sheet as the reference for every shot"))}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:1.6fr 1fr;gap:40px;align-items:center;">
      <div>{svg}</div>
      <div class="stack" style="gap:22px;">
        <ul class="list">
          <li>{t("Референс <b>сужает выбор</b> модели: меньше вариантов внешности.", "A reference <b>narrows the model’s choices</b> for appearance.")}</li>
          <li>{t("<b>Veo 3.1:</b> до 3 картинок-референсов. <b>Kling 3.0:</b> Elements, 2–4 картинки.", "<b>Veo 3.1:</b> up to 3 reference images. <b>Kling 3.0:</b> Elements, 2–4 images.")}</li>
          <li>{t("Стабильнее, но <b>не гарантировано</b>: каждый шот проверяем глазами.", "More stable, <b>not guaranteed</b>: review every shot.")}</li>
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
                    t("⏱ 3 мин. Этот лист персонажа мы делали в L04: один человек в четырёх ракурсах. Выноски — «якоря», по которым зритель узнаёт героя: лицо и причёска, жёлтая куртка с полосой, бирюзовый короб, чёрные брюки и белые кроссовки.",
                      "⏱ 3 min. We made this character sheet in L04: one person from four angles. The callouts are “anchors” viewers recognise the hero by: face and hair, yellow jacket with a stripe, turquoise box backpack, black trousers and white sneakers."),
                    t("Референс не делает чудо, он просто сужает выбор модели. Где это есть: Veo 3.1 принимает до трёх картинок-референсов, Kling 3.0 — функция Elements (2–4 картинки). Результат стабильнее, но не гарантирован, поэтому в конце урока будет чек-лист приёмки.",
                      "A reference is not magic; it just narrows the model’s choices. Where it exists: Veo 3.1 takes up to three reference images, Kling 3.0 has Elements (2–4 images). Results are more stable but not guaranteed, which is why we end with a checklist."),
                    t("Внизу справа — кадры из наших шотов 1 и 2: курьер узнаваем.", "Bottom right: frames from our shots 1 and 2. The courier is recognisable.")))


def s_keyframe():
    return dict(min=4, html=f'''
  {head(t("Шаг 2 • ключевой кадр", "Step 2 • key frame"), t("Ключевой кадр правим в image-чате, до генерации видео", "Fix the key frame in an image chat before generating video"))}
  <div class="body">
    <div class="kf">
      <figure><img src="{IMG}knight_sprite.jpg" alt="" style="width:170px;align-self:center"><figcaption><b>{t("Спрайт", "Sprite")}</b>: {t("исходник из игры", "game source art")}</figcaption></figure>
      <div class="ar">→</div>
      <figure><img src="{IMG}knight_draft.jpg" alt=""><div class="bub">{t("«Сделай реалистичный кадр 16:9 по этому спрайту»", "“Make a realistic 16:9 frame from this sprite”")}</div><figcaption><b>{t("Черновик", "Draft")}</b>: {t("не тот шлем и накидка", "wrong helmet and tabard")}</figcaption></figure>
      <div class="ar">→</div>
      <figure><img src="{IMG}knight_approved.jpg" alt=""><div class="bub">{t("«Руки без защиты, накидка в бело-синие прямоугольники, шлем в форме плоского „котелка“»", "“Bare hands, tabard in white and blue rectangles, a flat ‘kettle’ helmet”")}</div><figcaption><b style="color:var(--green)">{t("Одобрено ✓", "Approved ✓")}</b>: {t("первый кадр для видео", "first frame for the video")}</figcaption></figure>
    </div>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:36px;">
      <div class="stat" style="--k:var(--green)"><div class="n">{t("секунды, центы", "seconds, cents")}</div><div class="d">{t("одна правка <b>картинки</b> в чате", "one <b>image</b> edit in chat")}</div></div>
      <div class="stat" style="--k:var(--red)"><div class="n">{t("минуты, $0.40/с", "minutes, $0.40/s")}</div><div class="d">{t("одна перегенерация <b>видео</b> (Veo 3.1, 720p)", "one <b>video</b> regeneration (Veo 3.1, 720p)")}</div></div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Короткий пример из L04: из маленького игрового спрайта получаем реалистичный кадр. Первый вариант почти хорош, но шлем и накидка не те. Одна точная правка словами — и кадр одобрен.",
                      "⏱ 4 min. A short example in the style of L04: from a small game sprite we get a realistic frame. The first version is close, but the helmet and tabard are wrong. One precise text edit, and the frame is approved."),
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
  {head(t("Шаг 3 • промпт", "Step 3 • prompt"), t("Структура видеопромпта: 6 слотов", "Video prompt structure: 6 slots"))}
  <div class="body" style="margin-top:20px;">
    <div class="slots">{legend}</div>
    <div class="row" style="grid-template-columns:1.9fr 1fr;gap:32px;flex:none;margin-top:18px;align-items:start;">
      <div><div class="prompt-label">{t("Промпт шота 2 (Veo 3.1, image-to-video)", "Shot 2 prompt (Veo 3.1, image-to-video)")}</div><div class="dprompt">{text}</div></div>
      <div class="stack" style="gap:10px;">
        {video("shot2", "poster_shot2")}
        <div class="cap">{t("Результат: шот 2", "Output: shot 2")}</div>
      </div>
    </div>
    <ul class="list" style="margin-top:26px;">
      <li>{t("<b>Глаголы движения</b> (pedals, spinning, tracks): модели нужно знать, что меняется.", "<b>Motion verbs</b> (pedals, spinning, tracks): the model needs to know what changes.")}</li>
      <li>{t("<b>Не пересказывайте кадр:</b> он уже на входе. Для внешности хватит одной приметы.", "<b>Do not describe the frame again:</b> it is already the input. One identifying detail is enough.")}</li>
      <li>{t("<b>Пишите, что должно происходить.</b> Поле negative prompt есть не везде (есть в Kling, Wan).", "<b>Describe what should happen.</b> A negative prompt field exists only in some tools (Kling, Wan).")}</li>
    </ul>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Это настоящий промпт, которым сделан шот 2. Разберите его по цветам: 1 — камера, 2 — кто, 3 — действие, 4 — где и когда, 5 — детали движения, 6 — свет. В L04 у картинки тоже было 6 слотов; в видео главное — камера, действие и детали движения.",
                      "⏱ 6 min. This is the actual prompt used for shot 2. Walk through the colours: 1 camera, 2 who, 3 action, 4 where and when, 5 motion details, 6 light. In L04 images also had 6 slots; in video the key ones are camera, action and motion details."),
                    t("Три правила. Первое — глаголы движения: модель должна понять, что меняется во времени. Второе — в I2V не описывайте заново всё, что видно на картинке; достаточно короткой приметы героя. Третье — формулируйте позитивно: что должно происходить. Отдельное поле «чего не должно быть» есть, например, в Kling и Wan; в Veo лучше писать позитивно.",
                      "Three rules. First, motion verbs: the model must understand what changes over time. Second, in image-to-video do not describe again everything visible in the image; one identifying detail is enough. Third, phrase it positively: what should happen. A separate “what not to show” field exists in Kling and Wan, for example; in Veo positive phrasing works better."),
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
    return dict(min=4, html=f'''
  {head(t("Шаг 3 • камера", "Step 3 • camera"), t("Движения камеры и термины для промпта", "Camera moves and the prompt terms for them"))}
  <div class="body" style="margin-top:18px;">
    <div class="cams">{cards}</div>
    <div class="note" style="margin-top:20px;">{t("Модели видели видео с подписями, поэтому понимают <b>операторские термины</b>. В чат-приложениях камеру задают только словами; в видеостудиях есть и отдельные настройки (Runway, Kling, Luma).", "Models were trained on captioned video, so they understand <b>camera terms</b>. In chat apps you set the camera with words only; video studios also have dedicated controls (Runway, Kling, Luma).")}</div>
    <div class="small" style="margin-top:8px;">{t("Схемы: вид сверху (Pan, Dolly, Tracking, Orbit) и сбоку (Static, Tilt, Crane). Камера голубая, объект жёлтый, движение показано зелёной стрелкой.", "Diagrams: top view (Pan, Dolly, Tracking, Orbit) and side view (Static, Tilt, Crane). Camera in blue, subject in yellow, motion as a green arrow.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Восемь базовых движений — словарь оператора. Пройдитесь по схемам: голубая — камера, жёлтый — объект, зелёная стрелка — куда движется камера. Под каждой схемой — готовая фраза для промпта на английском.",
                      "⏱ 4 min. Eight basic moves from standard camera vocabulary. Walk through the diagrams: blue is the camera, yellow is the subject, the green arrow shows how the camera moves. Under each diagram is a ready English phrase for the prompt."),
                    t("Почему модели это понимают: они учились на видео с текстовыми описаниями, где такие слова встречались. Магии нет — это просто знакомые модели слова. Совет: одно движение камеры на шот; «pan + dolly + orbit» в одном клипе часто превращается в кашу.",
                      "Why models understand this: they learned from videos with text descriptions that used these words. These are simply words the model has seen in training data. Tip: one camera move per shot; “pan + dolly + orbit” in one clip often turns to mush."),
                    t("В чатах (Gemini, Flow) камеру задают словами. В видеостудиях есть отдельные настройки: в Runway — направление и сила движения по осям, в Kling — параметры камеры, в Luma — готовые «концепты» движений.",
                      "In chats (Gemini, Flow) you set the camera with words. Video studios have dedicated controls: Runway has direction and strength per axis, Kling has camera parameters, Luma has preset motion “concepts”.")))


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
    return dict(min=3, html=f'''
  {head(t("Шаг 4 • контроль", "Step 4 • control"), t("Управление кроме промпта: кадры, продление, референсы", "Controls beyond the prompt: frames, extension, references"))}
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
        {tile("green", s2, t("Продление клипа", "Extend a clip"), t("<b>Veo 3.1:</b> +7 с за шаг, до 148 с (720p, не Lite)<br><b>Gemini Omni:</b> +10 с за шаг, до 40 с", "<b>Veo 3.1:</b> +7 s per step, up to 148 s (720p, not Lite)<br><b>Gemini Omni:</b> +10 s per step, up to 40 s"))}
        {tile("amber", s3, t("Референсы героя", "Hero references"), t("<b>Veo 3.1 / Fast:</b> до 3 картинок, клип 8 с<br><b>Kling 3.0 Elements:</b> 2–4 картинки", "<b>Veo 3.1 / Fast:</b> up to 3 images, 8 s clip<br><b>Kling 3.0 Elements:</b> 2–4 images"))}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Слова — не единственный руль. Слева — идея локального контроля: выделяем кистью части кадра и рисуем стрелку, куда они двигаются; фон помечаем статичной зоной. Так это устроено в Motion Brush у Kling (до 6 элементов, стрелки на плоскости кадра). Честно: это функция старших моделей Kling 1.x–2.x, в описании Kling 3.0 её нет.",
                      "⏱ 3 min. Words are not the only steering wheel. On the left is the idea of local control: brush over parts of the frame and draw an arrow for where they move; mark the background as a static zone. That is how Kling’s Motion Brush works (up to 6 elements, arrows drawn on the image). To be honest, it belongs to Kling 1.x–2.x models; Kling 3.0’s description doesn’t list it."),
                    t("Справа — что реально массово есть в 2026: первый и последний кадр (модель сама строит путь между двумя картинками), продление клипа шагами (Veo 3.1 — по 7 секунд до 148, Gemini Omni — по 10 до 40) и референсы героя.",
                      "On the right is what is widely available in 2026: first and last frame (the model builds the path between two images), extending a clip in steps (Veo 3.1: 7 s at a time up to 148 s; Gemini Omni: 10 s up to 40 s) and hero references."),
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
  {head(t("Шаг 5 • монтаж", "Step 5 • editing"), t("Монтаж: три шота в один ролик на 23 секунды", "Editing: three shots into one 23-second video"), k="green")}
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
    <p>{t("Дальше: код, стоимость, приёмка, риски и домашнее задание.", "Next: code, cost, acceptance, risks and homework.")}</p>
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
        ("Kling 3.0", "Kuaishou", 15, t("4.0 Flash: до 20 с (бета)", "4.0 Flash: 20 s (beta)"), {"a", "i", "p"}, ""),
        ("Seedance 2.5", "ByteDance", 30, "", {"a", "i", "p"}, ""),
        ("Wan 3.0", "Alibaba", 30, "", {"a", "i", "p"}, t("#1 Artificial Analysis", "#1 Artificial Analysis")),
        ("Hailuo H3", "MiniMax", 15, "", {"a", "i", "p"}, ""),
        ("Ray3.2", "Luma", 10, "", {"i", "p"}, ""),
        ("LTX-2", "Lightricks", 20, "", {"a", "i", "p", "o"}, ""),
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
            f'{t("закрыта: приложение 26.04.2026, API 24.09.2026, замены нет", "shut down: app 26.04.2026, API 24.09.2026, no replacement")}</div></div><div></div></div>')
    return dict(min=5, html=f'''
  {head(t("Рынок • октябрь 2026", "Market • October 2026"), t("Видеомодели: максимальная длина клипа и возможности", "Video models: maximum clip length and capabilities"), k="amber")}
  <div class="body" style="margin-top:6px;">
    <div class="mkt">{head_row}{"".join(body)}{sora}</div>
    <div class="small" style="margin-top:8px;">{t("Полоса: максимум за одну генерацию. Подсвеченный значок: есть; серый: нет или не подтверждено. * Звук у Omni по сторонним обзорам. Рейтинги: LMArena (21.09.2026), Artificial Analysis со звуком (октябрь 2026).", "Bar: maximum per generation. Highlighted chip: yes; grey: no or not confirmed. * Omni audio per third-party reviews. Rankings: LMArena (21.09.2026), Artificial Analysis with audio (October 2026).")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Как читать: полоса — сколько секунд даёт одна генерация; справа — что модель умеет. Что изменилось за год: звук стал нормой почти у всех, а типичная длина клипа выросла с 5–10 до 10–30 секунд.",
                      "⏱ 5 min. How to read it: the bar is how many seconds one generation gives; on the right, what the model can do. What changed in a year: audio became standard for almost everyone, and typical clip length grew from 5–10 to 10–30 seconds."),
                    t("Лидеры: у Google сейчас главная модель — Gemini Omni 1.1 Flash (№1 на LMArena 21.09.2026). Veo 3.1, которым сделаны наши клипы, по-прежнему работает в API и умеет продлевать клип до 148 секунд. На рейтинге Artificial Analysis со звуком первое место у Wan 3.0. Рейтинги расходятся и меняются каждый месяц — всегда смотрите дату.",
                      "Leaders: Google’s main model is now Gemini Omni 1.1 Flash (#1 on LMArena, 21.09.2026). Veo 3.1, which made our clips, still runs in the API and can extend a clip to 148 seconds. On the Artificial Analysis board with audio, Wan 3.0 is first. Boards disagree and change monthly, so always check the date."),
                    t("Открытые веса (можно запустить у себя): Wan 2.2 и LTX-2. Новые Wan 2.5–3.0 — только через API. Sora от OpenAI закрыта: приложение — с 26 апреля, API — с 24 сентября 2026, замены нет; ChatGPT видео не делает.",
                      "Open weights (you can run them yourself): Wan 2.2 and LTX-2. Newer Wan 2.5–3.0 are API-only. OpenAI’s Sora is shut down: the app since 26 April, the API since 24 September 2026, with no replacement; ChatGPT does not make video."),
                    t("Kling 4.0 Flash (до 20 с, 720p) — ранний доступ с 28.09; полная 4.0 (до 30 с) анонсирована на октябрь — проверьте перед занятием, вышла ли.", "Kling 4.0 Flash (up to 20 s, 720p) has been in early access since 28 Sep. Full 4.0 (up to 30 s) is announced for October; check before class whether it has shipped.")))


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
  {head(t("Для справки • google-genai", "Reference • google-genai"), t("Gemini API: видео из картинки на Python", "Gemini API: image-to-video in Python"), k="violet")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.45fr 1fr;gap:40px;align-items:center;">
      <pre class="code">{code}</pre>
      <div class="stack" style="gap:24px;">
        <div class="stat" style="--k:var(--fg)"><div class="d" style="font-size:21px">{t("Асинхронная операция: <b>отправить → опрашивать статус → скачать</b>. Генерация занимает от секунд до минут.", "Long-running operation: <b>submit → poll status → download</b>. Generation takes seconds to minutes.")}</div></div>
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
    # (model, where, $ per second, note)
    rows = [
        ("Gemini Omni 1.1 Flash", t("Runway API, от", "Runway API, from"), 0.034),
        ("Veo 3.1 Lite", "Gemini API", 0.05),
        ("Veo 3.1 Fast", "Gemini API", 0.10),
        ("Runway Gen-4.5", "Runway API", 0.12),
        ("Seedance 2.5", t("Runway API, от", "Runway API, from"), 0.20),
        ("Veo 3.1", "Gemini API", 0.40),
    ]
    def money(v):
        return f"${v:,.0f}" if v >= 100 else f"${v:,.2f}"
    trs = "".join(
        f'<tr><td class="m">{n}<small>{w}</small></td><td>{("$%.3f" % v) if round(v, 2) != v else ("$%.2f" % v)}</td>'
        f'<td>{money(v * 8)}</td><td>{money(v * 60)}</td><td class="h">{money(v * 3600)}</td><td class="h3">{money(v * 3600 * 3)}</td></tr>'
        for n, w, v in rows)
    return dict(min=5, html=f'''
  {head(t("Стоимость", "Cost"), t("Стоимость генерации: клип, минута, час видео", "Generation cost: per clip, per minute, per hour of video"), t("Цена считается за секунду сгенерированного видео, 720p. Час готового ролика = 3600 с = <b>450 шотов по 8 секунд</b>.", "Priced per second of generated video, 720p. One hour of finished video = 3600 s = <b>450 shots of 8 seconds</b>."), k="amber")}
  <div class="body" style="margin-top:14px;">
    <table class="cost">
      <thead><tr><th>{t("Модель", "Model")}</th><th>{t("$ за секунду", "$ per second")}</th><th>{t("Клип 8 с", "8 s clip")}</th><th>{t("1 минута", "1 minute")}</th><th>{t("1 час", "1 hour")}</th><th>{t("1 час, 3 дубля на шот", "1 hour, 3 takes per shot")}</th></tr></thead>
      <tbody>{trs}</tbody>
    </table>
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;flex:none;margin-top:22px;">
      <div class="note" style="--k:var(--amber)">{t("<b>Дубли умножают бюджет.</b> При 3 попытках на каждый принятый шот генерируется 3 часа видео ради 1 часа результата.", "<b>Retakes multiply the budget.</b> With 3 attempts per accepted shot you generate 3 hours of video to keep 1 hour.")}</div>
      <div class="note" style="--k:var(--green)">{t("<b>Kling (веб):</b> 3.0, 1080p со звуком = 12 кредитов/с, то есть 43 200 кредитов за час. Черновики делайте на Veo 3.1 Lite или Fast.", "<b>Kling (web):</b> 3.0, 1080p with audio = 12 credits/s, i.e. 43,200 credits per hour. Run drafts on Veo 3.1 Lite or Fast.")}</div>
    </div>
    <div class="small" style="margin-top:12px;">{t("Цены: Gemini API и Runway API, октябрь 2026; оплачиваются только успешные генерации. Не включены: картинки для ключевых кадров, монтаж, звук, работа людей. 3 дубля на шот: допущение для оценки.", "Prices: Gemini API and Runway API, October 2026; only successful generations are billed. Not included: key frame images, editing, audio, people’s time. 3 takes per shot is an assumption for the estimate.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Здесь главное масштаб. Секунда видео стоит центы, но час готового ролика это 450 шотов по 8 секунд. На Veo 3.1 это $1 440 без дублей и $4 320, если на каждый принятый шот уходит 3 попытки.",
                      "⏱ 5 min. The point here is scale. One second costs cents, but an hour of finished video is 450 shots of 8 seconds. On Veo 3.1 that is $1,440 with no retakes and $4,320 if each accepted shot takes 3 attempts."),
                    t("Дешёвые модели (Lite, Fast, Omni через Runway) годятся для черновиков. Финальные шоты делаем на модели, которая проходит приёмку. Kling в веб-интерфейсе считает в кредитах: 12 кредитов за секунду 1080p со звуком.",
                      "Cheaper models (Lite, Fast, Omni on Runway) are fine for drafts. Final shots go to whichever model passes acceptance. Kling’s web app bills in credits: 12 credits per second of 1080p with audio."),
                    t("Сюда не входят картинки для ключевых кадров, монтаж, звук и время людей. Цены меняются, проверяйте прайс перед занятием.",
                      "Not included: key frame images, editing, audio and people’s time. Prices change; check the price lists before class.")))


def s_layers():
    def col(k, h, sub, tools, ctrl, pay, use):
        chips = "".join(f'<span class="tchip">{x}</span>' for x in tools)
        return (f'<div class="layer" style="--k:var(--{k})"><div class="lh">{h}</div><div class="ls">{sub}</div>'
                f'<div class="tchips">{chips}</div>'
                f'<dl><dt>{t("Управление", "Control")}</dt><dd>{ctrl}</dd><dt>{t("Оплата", "Billing")}</dt><dd>{pay}</dd><dt>{t("Для чего", "Use for")}</dt><dd>{use}</dd></dl></div>')
    c1 = col("cyan", t("Чат-приложения", "Chat apps"), t("видео прямо в чате", "video inside a chat"),
             ["Gemini app", "Google Flow", "Grok Imagine"],
             t("только текст промпта; в Flow ещё первый/последний кадр и продление", "prompt text only; Flow adds first/last frame and extension"),
             t("подписка", "subscription"), t("идеи, быстрые черновики", "ideas, quick drafts"))
    c2 = col("green", t("Веб-студии", "Web studios"), t("интерфейс для видео", "dedicated video UI"),
             ["Kling", "Leonardo", t("Dreamina / CapCut (Seedance)", "Dreamina / CapCut (Seedance)"), "Runway", "Luma", "Hailuo"],
             t("настройки камеры, первый/последний кадр, референсы, multi-shot", "camera settings, first/last frame, references, multi-shot"),
             t("кредиты; у Kling есть ежедневные бесплатные", "credits; Kling has free daily credits"), t("отдельные ролики, ДЗ", "individual videos, homework"))
    c3 = col("violet", "API", t("код и автоматизация", "code and automation"),
             ["Gemini API / Vertex AI", "Kling API", "Runway API", "xAI API"],
             t("всё как параметры запроса; пакетная генерация", "everything as request parameters; batch jobs"),
             t("за секунду видео", "per second of video"), t("пайплайны, продукты", "pipelines, products"))
    return dict(min=4, html=f'''
  {head(t("Где генерировать", "Where to generate"), t("Три уровня доступа к видеомоделям: чат, веб-студия, API", "Three access layers for video models: chat, web studio, API"), k="cyan")}
  <div class="body" style="margin-top:16px;">
    <div class="layers">{c1}{c2}{c3}</div>
    <div class="note" style="margin-top:20px;">{t("Одна модель часто доступна на всех трёх уровнях: Veo есть в Gemini app, во Flow, в Leonardo, в Runway и в Gemini API. <b>ChatGPT видео не генерирует</b>: Sora закрыта.", "One model is often available on all three layers: Veo is in the Gemini app, Flow, Leonardo, Runway and the Gemini API. <b>ChatGPT does not generate video</b>: Sora has been shut down.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Та же схема, что в L04 для картинок. Чат-приложения: Gemini app (Gemini Omni, Veo 3.1), Google Flow (сцены, первый/последний кадр, продление), Grok Imagine от xAI. Камера задаётся только словами.",
                      "⏱ 4 min. Same structure as the image layers in L04. Chat apps: Gemini app (Gemini Omni, Veo 3.1), Google Flow (scenes, first/last frame, extension), Grok Imagine from xAI. Camera is set with words only."),
                    t("Веб-студии: Kling (3.0, Elements, multi-shot, ежедневные бесплатные кредиты), Leonardo (собственная Motion 2.0 и чужие модели: Veo, Kling, Seedance, Hailuo), Dreamina и CapCut от ByteDance с моделью Seedance, Runway (Gen-4.5 и чужие модели), Luma Ray3.2, Hailuo. Здесь есть настройки камеры и референсы.",
                      "Web studios: Kling (3.0, Elements, multi-shot, free daily credits), Leonardo (its own Motion 2.0 plus hosted Veo, Kling, Seedance, Hailuo), ByteDance’s Dreamina and CapCut with Seedance, Runway (Gen-4.5 plus hosted models), Luma Ray3.2, Hailuo. These have camera settings and references."),
                    t("API: Gemini API и Vertex AI (Veo 3.1, Gemini Omni), Kling API, Runway API (через него доступны Seedance, Veo, Wan, Hailuo), xAI API для Grok Imagine. Оплата за секунду видео. ChatGPT видео не делает: Sora закрыта (приложение в апреле, API 24 сентября 2026).",
                      "API: Gemini API and Vertex AI (Veo 3.1, Gemini Omni), Kling API, Runway API (also serves Seedance, Veo, Wan, Hailuo), xAI API for Grok Imagine. Billed per second of video. ChatGPT does not make video: Sora was shut down (app in April, API on 24 September 2026).")))


def s_storyboard():
    shots = [
        ("tl_shot1", "1", "0–8 s", t("Курьер забирает пакет у бариста и поворачивается к выходу", "Courier takes the bag from the barista and turns to the exit"),
         t("средний план, медленный наезд", "medium shot, slow push-in"), "shot1_cafe_pickup.png"),
        ("tl_shot2", "2", "8–16 s", t("Едет на велосипеде по мокрой улице в сумерках", "Rides a bicycle down a wet street at dusk"),
         t("tracking рядом с курьером, низкий ракурс", "tracking alongside, low angle"), "shot2_bike_rain.png"),
        ("tl_shot3", "3", "16–23 s", t("Маршрут на карте прорисовывается до точки доставки", "The route on the map draws itself to the destination pin"),
         t("цифровой наезд и лёгкий наклон", "digital push-in, slight tilt"), "shot3_map_route.png"),
    ]
    trs = "".join(
        f'<tr><td class="n">{n}</td><td class="im"><img src="{IMG}{img}.jpg" alt=""></td><td class="tm">{tm.replace(" s", " " + t("с", "s"))}</td>'
        f'<td>{act}</td><td>{cam}</td><td class="f"><code>{kf}</code></td></tr>'
        for img, n, tm, act, cam, kf in shots)
    cols = ["Shot / timing", "Visual", "Voice-over", "Image prompt", "Video prompt", "SFX", "Music"]
    colchips = "".join(f'<span class="tchip">{c}</span>' for c in cols)
    return dict(min=5, html=f'''
  {head(t("Шаг 0 • сториборд", "Step 0 • storyboard"), t("Сториборд: вся история до первой генерации", "Storyboard: the whole story before the first generation"), t("История разбивается на шоты по 4–8 секунд. Каждая строка = один ключевой кадр + один промпт + одна генерация.", "The story is split into shots of 4–8 seconds. Each row = one key frame + one prompt + one generation."), k="cyan")}
  <div class="body" style="margin-top:12px;">
    <table class="sb">
      <thead><tr><th>#</th><th>{t("Кадр", "Frame")}</th><th>{t("Время", "Time")}</th><th>{t("Действие", "Action")}</th><th>{t("Камера", "Camera")}</th><th>{t("Ключевой кадр", "Key frame")}</th></tr></thead>
      <tbody>{trs}</tbody>
    </table>
    <div class="row" style="grid-template-columns:auto 1fr;gap:18px;flex:none;margin-top:18px;align-items:center;">
      <div class="prompt-label" style="margin:0">{t("Полный шаблон (Creator Tools)", "Full template (Creator Tools)")}</div>
      <div class="tchips">{colchips}</div>
    </div>
    <div class="small" style="margin-top:8px;">{t("1 минута ≈ 8 шотов по 8 с; 1 час ≈ 450 шотов. Сториборд ведут в таблице (Google Sheets, Excel): это план работ, бюджет и чек-лист приёмки одновременно.", "1 minute ≈ 8 shots of 8 s; 1 hour ≈ 450 shots. Keep the storyboard in a spreadsheet (Google Sheets, Excel): it is the work plan, the budget and the acceptance list at the same time.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. До генерации история раскладывается на шоты. Наш ролик это три строки: кафе, поездка, карта. Для каждой строки есть время, действие, движение камеры и файл ключевого кадра.",
                      "⏱ 5 min. Before generating anything, the story is split into shots. Our video is three rows: cafe, ride, map. Each row has timing, action, camera move and a key frame file."),
                    t("Полный производственный шаблон из Creator Tools (серия Giant Stories) имеет 7 колонок: шот и время, визуал, закадровый текст, промпт картинки, промпт видео, шумы, музыка. Звук разберём в L06.",
                      "The full production template from Creator Tools (the Giant Stories series) has 7 columns: shot and timing, visual, voice-over, image prompt, video prompt, SFX, music. Audio is covered in L06."),
                    t("Масштаб: минута это примерно 8 шотов, час это около 450. Поэтому сториборд в таблице: по нему считают бюджет (следующие слайды) и делают приёмку.",
                      "Scale: a minute is about 8 shots, an hour about 450. That is why the storyboard lives in a spreadsheet: it drives the budget (later slides) and the acceptance review.")))


def s_qa():
    return dict(min=5, html=f'''
  {head(t("Приёмка", "Acceptance"), t("Чек-лист приёмки сгенерированного клипа", "Acceptance checklist for a generated clip"), t("Даже удачный image-to-video клип смотрим покадрово. Дефекты из <b>наших</b> шотов 2 и 3:", "Even a good image-to-video clip gets a frame-by-frame review. Defects from <b>our</b> shots 2 and 3:"), k="green")}
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
          <div class="cap">{t("<b>Шот 2:</b> вывеска «THABIK» из случайных букв.", "<b>Shot 2:</b> the “THABIK” sign is random letters.")}</div>
        </div>
      </div>
      <div class="stack" style="gap:14px;">
        <div class="prompt-label">{t("Чек-лист приёмки", "Acceptance checklist")}</div>
        <ol class="checklist">
          <li><span>{t("<b>Руки и предметы</b> в контакте: не слипаются, не исчезают", "<b>Hands and objects</b> in contact: no merging or vanishing")}</span></li>
          <li><span>{t("<b>Текст и цифры</b>: читаются и не меняются", "<b>Text and numbers</b>: readable and stable")}</span></li>
          <li><span>{t("<b>Лицо и одежда</b>: как на референсе", "<b>Face and clothes</b>: match the reference")}</span></li>
          <li><span>{t("<b>Движение</b>: скорость и направление (колёса вперёд)", "<b>Motion</b>: speed and direction (wheels forward)")}</span></li>
          <li><span>{t("<b>Первый кадр</b>: совпадает с одобренным", "<b>First frame</b>: matches the approved one")}</span></li>
          <li><span>{t("<b>Стык шотов</b>: свет и цвет совпадают", "<b>Shot joins</b>: light and colour match")}</span></li>
        </ol>
        <div class="note" style="--k:var(--green)">{t("Этот же чек-лист используется как <b>рубрика ДЗ</b>.", "The same checklist is the <b>homework rubric</b>.")}</div>
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
  {head(t("Риски", "Risks"), t("Права, маркировка и происхождение видео", "Rights, labelling and provenance"), k="red")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1fr 1.55fr;gap:40px;align-items:center;flex:none;">
      <div class="light" style="gap:18px">
        <div class="lrow" style="--k:var(--green)"><div class="dot"></div><div><div class="h">{t("Свои кадры и персонажи", "Your own frames and characters")}</div><div class="d">{t("можно, с пометкой «создано ИИ»", "allowed, with an “AI-generated” label")}</div></div></div>
        <div class="lrow" style="--k:var(--amber)"><div class="dot"></div><div><div class="h">{t("Чужие бренды, логотипы, стили", "Other brands, logos, styles")}</div><div class="d">{t("только с разрешения и после юристов компании", "only with permission and after company lawyers review")}</div></div></div>
        <div class="lrow" style="--k:var(--red)"><div class="dot"></div><div><div class="h">{t("Реальные люди без согласия", "Real people without consent")}</div><div class="d">{t("сотрудники, клиенты, публичные лица: только с письменного согласия", "employees, clients, public figures: only with written consent")}</div></div></div>
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
        <div class="note" style="--k:var(--green);font-size:20px">{t("<b>Проверка SynthID:</b> загрузить видео в приложение Gemini (до 100 МБ, 90 с). Находит только SynthID, видео других сервисов может не распознать.", "<b>SynthID check:</b> upload the video to the Gemini app (up to 100 MB, 90 s). It detects SynthID only; videos from other services may not be recognised.")}</div>
      </div>
    </div>
    <div class="plaque" style="margin-top:40px;font-size:22px;"><b>EU AI Act, {t("ст. 50", "Art. 50")}:</b> {t("с 2 августа 2026. <b>50(4)</b>: дипфейк помечает тот, кто публикует. <b>50(2)</b>: машиночитаемую метку ставит провайдер модели (для систем, выпущенных раньше, с 2 декабря 2026). Штраф до €15 млн или 3% оборота.", "since 2 August 2026. <b>50(4)</b>: whoever publishes a deepfake must label it. <b>50(2)</b>: the model provider adds a machine-readable mark (systems released earlier: from 2 December 2026). Fines up to €15M or 3% of turnover.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Слева — светофор. Зелёный: свои сгенерированные кадры и персонажи, помечаем как созданные ИИ. Жёлтый: чужие бренды и логотипы — только с разрешения, решают юристы компании (вспомните «Glono» из провала). Красный: реальные люди — коллеги, клиенты, знаменитости — только с письменного согласия.",
                      "⏱ 6 min. On the left is a traffic light. Green: your own generated frames and characters, labelled as AI-made. Amber: other brands and logos, only with permission and a review by company lawyers (remember “Glono” from the failure). Red: real people (colleagues, clients, celebrities), only with written consent."),
                    t("Справа — как узнать, что видео сделано ИИ. У Google все видео Veo получают SynthID — невидимую метку прямо в пикселях. Она переживает сжатие и обрезку. C2PA — это подпись в метаданных файла; её легко потерять при пересохранении или скриншоте. Проверить SynthID можно, загрузив видео в приложение Gemini (до 100 МБ и 90 секунд). Важно: проверка находит только SynthID, поэтому видео других сервисов она может не распознать.",
                      "On the right: how to tell a video is AI-made. Google adds SynthID, an invisible mark in the pixels, to every Veo video. It survives compression and cropping. C2PA is a signature in the file metadata; it is easily lost on re-save or screenshot. You can check SynthID by uploading a video to the Gemini app (up to 100 MB and 90 seconds). Note: the check only finds SynthID, so videos from other services may not be recognised."),
                    t("Закон: в ЕС действует статья 50 AI Act — с 2 августа 2026 дипфейки нужно помечать, штраф до €15 млн или 3% оборота. В США с мая 2026 платформы обязаны удалять интимные дипфейки за 48 часов (TAKE IT DOWN Act).",
                      "Law: in the EU, Article 50 of the AI Act applies since 2 August 2026. Under 50(4) whoever publishes a deepfake must label it; under 50(2) the model provider adds a machine-readable mark. Fines up to €15M or 3% of turnover. In the US, since May 2026 platforms must remove intimate deepfakes within 48 hours (TAKE IT DOWN Act).")))


def s_hw():
    return dict(min=5, html=f'''
  {head(t("Практика", "Practice"), t("Домашнее задание 5: анимировать ключевой кадр из L04", "Homework 5: animate your L04 key frame"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:44px;align-items:center;">
      <div class="stack" style="gap:20px;">
        <div class="track" style="--k:var(--cyan)"><img class="contain" src="{IMG}packshot.jpg" alt=""><div><div class="h"><span class="mark">{t("Трек А", "Track A")}</span> · {t("товар", "product")}</div><div class="d">{t("5 секунд промо: облёт или наезд камеры. Форма и надписи товара не меняются.", "5-second promo: orbit or dolly-in. Product shape and text stay stable.")}</div></div></div>
        <div class="track" style="--k:var(--green)"><img src="{IMG}poster_shot2.jpg" alt=""><div><div class="h"><span class="mark">{t("Трек Б", "Track B")}</span> · {t("курьер", "courier")}</div><div class="d">{t("Шот поездки: камера едет рядом. Лицо и форма как на референсе.", "Riding shot: the camera tracks alongside. Face and uniform match the reference.")}</div></div></div>
      </div>
      <div class="stack" style="gap:16px;">
        <ol class="checklist">
          <li style="font-size:23px"><span>{t("<b>Text-to-video</b> одним промптом, для сравнения", "<b>Text-to-video</b> with one prompt, as a baseline")}</span></li>
          <li style="font-size:23px"><span>{t("<b>Image-to-video</b> с кадром из L04 в <b>двух сервисах</b>", "<b>Image-to-video</b> from your L04 frame in <b>two services</b>")}</span></li>
          <li style="font-size:23px"><span>{t("Промпты и настройки → <code>video_spec.md</code>", "Prompts and settings → <code>video_spec.md</code>")}</span></li>
          <li style="font-size:23px"><span>{t("Приёмка по чек-листу со слайда 18 → <code>video_qa.md</code>", "Review with the slide 18 checklist → <code>video_qa.md</code>")}</span></li>
        </ol>
        <div class="files">genai-homeworks/L05/
├── videos/  <span class="cm"># 01_text_to_video, 02/03_image_to_video</span>
├── video_spec.md
└── video_qa.md</div>
        <div class="small" style="font-size:18px">{t("Ревьюер: <b>ihar_rubanovich@epam.com</b>. Бесплатные кредиты: у Kling ежедневные; остальные сервисы проверьте перед стартом (см. файл ДЗ).", "Reviewer: <b>ihar_rubanovich@epam.com</b>. Free credits: Kling gives daily credits; check the other services before you start (see the homework file).")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Два трека на выбор. А — оживить товар (пакшот из L04): короткий промо-ролик с облётом или наездом камеры. Б — продолжить историю курьера: шот поездки с камерой сбоку.",
                      "⏱ 5 min. Two tracks to choose from. Track A: animate a product (the L04 packshot) as a short promo with an orbit or dolly-in. Track B: continue the courier story with a riding shot, camera alongside."),
                    t("Обязательная часть: сначала честная попытка T2V одним промптом, потом I2V с вашим кадром в двух разных сервисах, промпты в video_spec.md и приёмка по чек-листу с прошлого слайда в video_qa.md. Оцениваем не красоту, а осознанность: видно ли, что вы понимаете, где и почему модель ошиблась.",
                      "Required: first an honest text-to-video attempt with one prompt, then image-to-video from your frame in two different services, prompts in video_spec.md and a check against the checklist in video_qa.md. We grade awareness, not beauty: can you show where and why the model went wrong."),
                    t("Подробности и шаблоны — в файле домашнего задания L05.", "Details and templates are in the L05 homework file.")))


def s_summary():
    rules = [
        ("cyan", t("Сначала кадр, потом движение", "Frame first, motion second"), t("image-to-video из одобренного кадра", "image-to-video from an approved frame")),
        ("green", t("Один шот, одно действие", "One shot, one action"), t("4–8 секунд; историю собираем по сториборду и монтажом", "4–8 seconds; the story comes from the storyboard and editing")),
        ("violet", t("Структурированный промпт", "Structured prompt"), t("камера + действие + детали движения", "camera + action + motion details")),
        ("amber", t("Приёмка и бюджет", "Acceptance and budget"), t("чек-лист на каждый клип; цена считается за секунду", "a checklist for every clip; cost is per second")),
    ]
    rr = "".join(f'<div class="rule" style="--k:var(--{k})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>'
                 for i, (k, h, d) in enumerate(rules))
    return dict(min=3, html=f'''
  {head(t("Итоги", "Summary"), t("Итоги урока", "Lesson summary"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.35fr 1fr;gap:56px;align-items:center;">
      <div class="rules">{rr}</div>
      <div class="stack" style="gap:16px;">
        <img src="{IMG}poster_final.jpg" alt="" style="width:100%;border-radius:12px;border:1px solid var(--line)">
        <div class="note" style="--k:var(--violet)"><b>{t("Урок 06: звук и речь.", "Lesson 06: sound and speech.")}</b> {t("Современные видеомодели генерируют звук сами. Как им управлять, разберём в L06.", "Current video models generate audio themselves. Controlling it is covered in L06.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Четыре правила одной строкой: сначала кадр, потом движение; один шот — одно действие; промпт режиссёра; приёмка по чек-листу и счёт секунд.",
                      "⏱ 3 min. Four points: frame first, motion second; one shot, one action; a structured prompt; acceptance checklist and per-second budget."),
                    t("Тизер: наши клипы на самом деле со звуком — Veo 3.1 сделал его сам. Как управлять звуком и речью — в следующем уроке, L06. Вопросы.",
                      "Teaser: our clips have sound, generated by Veo 3.1 itself. How to control sound and speech is the next lesson, L06. Questions.")))


SLIDES = [s_cover, s_hook, s_layers, s_how, s_fails, s_t2v_i2v, s_storyboard, s_refs, s_keyframe, s_prompt,
          s_camera, s_control, s_montage, s_market, s_break, s_code, s_econ, s_qa, s_risks, s_hw, s_summary]


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
