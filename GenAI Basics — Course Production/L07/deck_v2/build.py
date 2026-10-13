# -*- coding: utf-8 -*-
"""Build the L07 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Every slide is one function; text is written as t("ru", "en") side by side so both
languages stay in sync. Slides 11-13 and 18 read their numbers and text from
artifacts.json, produced by make_artifacts.py (a real git diff and a real unittest run).
Facts: ../../L07_08_Source_Notes_Research_2026-10.md + verification of 2026-10-13.
Plan: L07_09_Lesson_Plan_v2.md.
"""
import html as _html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L07 = HERE.parent
NAME = "presentation_L07_Copilot_Ecosystem"
OUT = {"ru": L07 / f"{NAME}_v2.html", "en": L07 / f"{NAME}_EN_v2.html"}
IMG = "assets/v2/img/"
KIT = L07 / "demo_courier_copilot"
ART = json.loads((HERE / "artifacts.json").read_text(encoding="utf-8"))
MEETING = (KIT / "meeting_notes.md").read_text(encoding="utf-8")
CHECKLIST = [ln for ln in (KIT / "release_checklist.txt").read_text(encoding="utf-8").splitlines() if re.match(r"\d\.", ln)]

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 07 • Экосистема Copilot", "en": "GenAI Basics • Lesson 07 • The Copilot Ecosystem"}


# ---------------------------------------------------------------- helpers
def esc(s):
    return _html.escape(s, quote=False)


def head(kicker, title, lead=None, k=None, badge=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    b = f' <span class="badge solid" style="--k:var(--amber)">{badge}</span>' if badge else ""
    s = f'<div class="kicker"{ks}>{kicker}{b}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


def sch():
    return f'<span class="sch">{t("схема", "schematic")}</span>'


def dots(colors=("#ff6b6b", "#fbbf24", "#34d399")):
    return '<span class="dots">' + "".join(f'<i style="background:{c}"></i>' for c in colors) + "</span>"


def diff_block(lines, cls="dif"):
    """Render diff lines (already filtered) as a coloured mono block."""
    out = []
    for ln in lines:
        if ln.startswith("@@"):
            c = "h"
        elif ln.startswith("+"):
            c = "a"
        elif ln.startswith("-"):
            c = "d"
        elif ln.startswith("FILE "):
            c, ln = "f", ln[5:]
        else:
            c = "c"
        out.append(f'<div class="{c}">{esc(ln) or "&nbsp;"}</div>')
    return f'<div class="{cls}">' + "".join(out) + "</div>"


def diff_lines(raw):
    """Keep the real diff text but drop the `index`, `---` and `+++` lines."""
    res = []
    for ln in raw.splitlines():
        if ln.startswith("diff --git"):
            res.append("FILE " + ln.split(" b/")[-1])
        elif ln.startswith(("index ", "--- ", "+++ ")):
            continue
        else:
            res.append(ln)
    return res


def split_files(lines):
    files, cur = {}, None
    for ln in lines:
        if ln.startswith("FILE "):
            cur = ln[5:]
            files[cur] = [ln]
        else:
            files[cur].append(ln)
    return files


DL = diff_lines(ART["diff_u1"])
DF = split_files(DL)
N_TESTS = ART["tests_total"]
N_NEW = ART["tests_new"]
N_LOGIC = ART["logic_added"]
assert ART["tests_ok"] and ART["ok_lines"] == N_TESTS

# synthetic orders for slide 07 (invented; consistent with the rule); the answer is computed
ORDERS = [(1001, "CITY", True, 82.40), (1002, "CITY", False, 76.00), (1003, "OUTSIDE", True, 91.10),
          (1004, "CITY", True, 75.00), (1005, "OUTSIDE", False, 48.30), (1006, "CITY", True, 120.00),
          (1007, "CITY", True, 64.90), (1008, "OUTSIDE", True, 79.50)]
_prime75 = [o for o in ORDERS if o[2] and o[3] >= 75]
TOP_ZONE = max({"CITY", "OUTSIDE"}, key=lambda z: sum(1 for o in _prime75 if o[1] == z))
TOP_N = sum(1 for o in _prime75 if o[1] == TOP_ZONE)
TOP_ALL = len(_prime75)

def strip_data():
  return [  # (day, tool-key, color, RU name, EN name, RU excerpt, EN excerpt)
      (t("Пн", "Mon"), "teams", "cyan", "Teams", "Teams",
       t("«Prime: бесплатная доставка от $75, только город»", "“Prime: free delivery from $75, city only”")),
      (t("Пн", "Mon"), "word", "cyan", "Word", "Word",
       t("Бриф на одну страницу: решения и открытые вопросы", "One-page brief: decisions and open questions")),
      (t("Вт", "Tue"), "issue", "violet", "GitHub issue", "GitHub issue",
       t("#12 Бесплатная доставка для Prime от $75", "#12 Free delivery for Prime from $75")),
      (t("Ср", "Wed"), "code", "violet", "VS Code", "VS Code",
       t(f"+{N_LOGIC} строки логики, +{N_NEW} теста, {N_TESTS} ok", f"+{N_LOGIC} lines of logic, +{N_NEW} tests, {N_TESTS} ok")),
      (t("Чт", "Thu"), "pr", "violet", "Pull request", "Pull request",
       t("Ревью: «тест на 74.99 есть; подумайте про Decimal»", "Review: “74.99 test is there; consider Decimal”")),
      (t("Пт", "Fri"), "win", "green", "Windows", "Windows",
       t("Чек-лист, пункт 6: откатить флаг, если плата вне зоны изменилась", "Checklist item 6: roll back the flag if outside-zone fees change")),
  ]


def glyph(kind, c):
    """Simple 56x56 tool glyph drawn from shapes (no logos)."""
    st = f'fill="none" stroke="var(--{c})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
    g = {
        "teams": f'<rect x="8" y="12" width="40" height="28" rx="5" {st}/><path d="M20 48h16M28 40v8" {st}/><circle cx="20" cy="26" r="4" {st}/><circle cx="34" cy="26" r="4" {st}/>',
        "word": f'<path d="M14 6h20l10 10v34H14z" {st}/><path d="M34 6v10h10M21 26h16M21 33h16M21 40h10" {st}/>',
        "issue": f'<circle cx="28" cy="28" r="19" {st}/><circle cx="28" cy="28" r="3" fill="var(--{c})"/>',
        "code": f'<path d="M20 16 8 28l12 12M36 16l12 12-12 12" {st}/><path d="M32 12 24 44" {st}/>',
        "pr": f'<circle cx="14" cy="12" r="5" {st}/><circle cx="14" cy="44" r="5" {st}/><circle cx="42" cy="44" r="5" {st}/><path d="M14 17v22M42 39V24a8 8 0 0 0-8-8h-6M32 10l-4 6 4 6" {st}/>',
        "win": f'<rect x="6" y="8" width="44" height="32" rx="4" {st}/><path d="M18 48h20M28 40v8" {st}/><path d="M16 18h10v8H16zM30 18h10v8H30z" {st}/>',
    }[kind]
    return f'<svg viewBox="0 0 56 56" width="56" height="56">{g}</svg>'


def strip(small=False):
    cols = []
    for day, key, c, nm, nm_en, ex in strip_data():
        name = nm
        cols.append(f'<div class="st" style="--k:var(--{c})"><span class="day">{day}</span>'
                    f'<div class="ic">{glyph(key, c)}</div><div class="nm">{name}</div>'
                    f'{"" if small else f"<div class=ex>{ex}</div>"}</div>')
    return f'<div class="strip{" sm" if small else ""}"><div class="line"></div>{"".join(cols)}</div>'


# ---------------------------------------------------------------- 01 cover
def s_cover():
    return dict(min=2, cls="cover l07", html=f'''
  <div class="bg"><img src="{IMG}cover_shot2.jpg" alt=""></div>
  <div class="shade"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 07 • Экосистема Copilot", "GenAI Basics • Lesson 07 • The Copilot Ecosystem")}</div>
    <h1>{t("Один Copilot? Нет — семья из трёх", "One Copilot? No: a family of three")}</h1>
    <h2>{t("Как команда за неделю выпускает одну фичу, а Copilot помогает на каждом шаге", "How a team ships one feature in a week, with Copilot helping at every step")}</h2>
    <p>{t("3 Copilot • 1 команда • 1 фича • 1 неделя. Все данные придуманные. Для практики хватит бесплатных уровней.",
          "3 Copilots • 1 team • 1 feature • 1 week. All data is synthetic. Free tiers are enough for practice.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. «Сегодня никто не вызывает API. Мы смотрим, как команда выпускает фичу, а Copilot помогает на каждом шаге.»",
                      "⏱ 2 min. Welcome. “Today nobody calls an API. We watch a team ship a feature, with Copilot at every step.”"),
                    t("Фича одна: подписчики Prime получают бесплатную доставку от $75 внутри города. Команда та же, что в курсе: Анна (продукт), Павел (junior-разработчик), Ола (поддержка). Всё придумано, настоящих клиентов нет.",
                      "One feature: Prime subscribers get free delivery from $75 inside the city. The team: Anna (product), Pavel (junior developer), Ola (support). Everything is made up, there are no real customers."),
                    t("План: 4 слайда о том, что такое семья Copilot, потом по шагам Teams, Word, GitHub, редактор, ревью, затем перерыв и Windows. В конце домашнее задание. Перед занятием пройдите demo_courier_copilot/surface_preflight.md.",
                      "Plan: 4 slides on what the Copilot family is, then step by step Teams, Word, GitHub, the editor, review, then a break and Windows. Homework at the end. Before class, go through demo_courier_copilot/surface_preflight.md.")))


# ---------------------------------------------------------------- 02 journey
def s_week():
    return dict(min=4, html=f'''
  {head(t("Сюжет урока", "The story"), t("Одна фича проходит шесть шагов за неделю", "One feature goes through six steps in a week"),
        t("На каждом шаге на выходе <b>текст, который вы проверяете сами</b>.", "Every step produces <b>a text you check yourself</b>."))}
  <div class="body">
    {strip()}
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «Вот весь урок на одном слайде. Дальше мы по очереди приближаем каждую станцию.»",
                      "⏱ 4 min. “Here is the whole lesson on one slide. Next we zoom into each station.”"),
                    t("Понедельник: встреча в Teams, где решили правило. Потом бриф в Word. Во вторник Анна превращает бриф в задачу на GitHub. В среду Павел в VS Code делает изменение с помощью Copilot. В четверг pull request и ревью. В пятницу релиз, чек-лист на компьютере с Windows.",
                      "Monday: a Teams meeting where the rule is decided. Then a brief in Word. On Tuesday Anna turns the brief into a GitHub task. On Wednesday Pavel makes the change in VS Code with Copilot. On Thursday the pull request and review. On Friday the release, with the checklist on a Windows PC."),
                    t("Обратите внимание на цитаты под значками: это настоящие фрагменты из файлов, которые мы откроем на уроке. И на общее свойство: на каждом шаге Copilot даёт текст, а ответственность за проверку остаётся у человека.",
                      "Look at the quotes under the icons: they are real fragments of the files we open in class. And the common point: at every step Copilot gives a text, and the responsibility for checking stays with the person.")))


# ---------------------------------------------------------------- 03 three places
def s_three():
    def circ(cx, c, icon, title, sub, p1, p2, under1, under2):
        return f'''
    <circle cx="{cx}" cy="262" r="212" fill="var(--{c})" fill-opacity=".10" stroke="var(--{c})" stroke-width="3"/>
    {icon(cx)}
    <text x="{cx}" y="186" text-anchor="middle" class="s30" fill="var(--{c})">{title}</text>
    <text x="{cx}" y="224" text-anchor="middle" class="s23" fill="var(--fg)">{sub}</text>
    <rect x="{cx - 130}" y="274" width="260" height="42" rx="10" fill="var(--surface)" stroke="var(--line)"/>
    <text x="{cx}" y="303" text-anchor="middle" class="s21m" fill="var(--fg)">{p1}</text>
    <rect x="{cx - 130}" y="330" width="260" height="42" rx="10" fill="var(--surface)" stroke="var(--line)"/>
    <text x="{cx}" y="359" text-anchor="middle" class="s21m" fill="var(--fg)">{p2}</text>
    <text x="{cx}" y="522" text-anchor="middle" class="s22" fill="var(--muted)">{under1}</text>
    <text x="{cx}" y="550" text-anchor="middle" class="s22" fill="var(--muted)">{under2}</text>'''
    ic_repo = lambda cx: f'<g transform="translate({cx - 22} 100)" fill="none" stroke="var(--violet)" stroke-width="3.5" stroke-linecap="round"><circle cx="10" cy="8" r="6"/><circle cx="10" cy="48" r="6"/><circle cx="36" cy="22" r="6"/><path d="M10 14v28M36 28c0 12-10 12-26 14"/></g>'
    ic_doc = lambda cx: f'<g transform="translate({cx - 18} 98)" fill="none" stroke="var(--cyan)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 0h24l10 10v46H4z"/><path d="M28 0v10h10M12 24h18M12 33h18M12 42h10"/></g>'
    ic_pc = lambda cx: f'<g transform="translate({cx - 28} 104)" fill="none" stroke="var(--green)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="52" height="34" rx="4"/><path d="M16 50h24M28 36v14"/></g>'
    svg = f'''<svg viewBox="0 0 1448 590" class="fig" style="width:100%;height:auto">
    {circ(250, "violet", ic_repo, t("Репозиторий", "Repository"), "GitHub Copilot", "issue #12", "pull request #13",
          t("Видит: код, историю,", "Sees: code, history,"), t("issue и pull request", "issues and pull requests"))}
    {circ(724, "cyan", ic_doc, t("Рабочие документы", "Work documents"), t("Copilot в Word, Teams", "Copilot in Word, Teams"), t("встреча в Teams", "Teams meeting"), t("бриф в Word", "brief in Word"),
          t("Видит: письма, файлы и встречи,", "Sees: mail, files and meetings"), t("которые открыты вам", "that are open to you"))}
    {circ(1198, "green", ic_pc, t("Ваш компьютер", "Your PC"), t("Copilot в Windows", "Copilot in Windows"), "release_checklist.txt", t("окно на экране", "window on screen"),
          t("Видит: окно, которое вы показали,", "Sees: the window you shared,"), t("и ваши файлы", "and your files"))}
    </svg>'''
    return dict(min=4, html=f'''
  {head(t("Карта", "The map"), t("Три Copilot — три места, где лежит ваша информация", "Three Copilots, three places where your information lives"),
        t("Чтобы выбрать Copilot, ответьте на один вопрос: <b>где лежит нужная информация?</b>", "To pick a Copilot, answer one question: <b>where does the information live?</b>"))}
  <div class="body">{svg}</div>''',
                notes=notes(
                    t("⏱ 4 мин. «Единственный вопрос, который вам нужен: где лежит информация?»",
                      "⏱ 4 min. “The only question you need: where does the information live?”"),
                    t("Если это код и задачи, открывайте GitHub Copilot. Если это письма, документы и встречи, берите Copilot в Word, Teams, Outlook. Если это то, что у вас на экране или в папке на компьютере, берите Copilot в Windows.",
                      "If it is code and tasks, open GitHub Copilot. If it is mail, documents and meetings, use Copilot in Word, Teams, Outlook. If it is what is on your screen or in a folder on your PC, use Copilot in Windows."),
                    t("Наши файлы по неделе легли в три круга: issue и pull request в репозиторий, встреча и бриф в рабочие документы, чек-лист на компьютер. Круги не пересекаются: каждый Copilot видит только своё место.",
                      "This week's files fall into three circles: the issue and pull request into the repository, the meeting and brief into work documents, the checklist onto the PC. The circles do not overlap: each Copilot sees only its own place.")))


# ---------------------------------------------------------------- 04 same model
def s_model():
    def chip(y, label, c):
        return (f'<rect x="20" y="{y}" width="250" height="46" rx="10" fill="var(--surface)" stroke="var(--{c})" stroke-width="2"/>'
                f'<text x="145" y="{y + 31}" text-anchor="middle" class="s23" fill="var(--fg)">{label}</text>')
    chips = "".join(chip(236 + i * 58, lab, c) for i, (lab, c) in enumerate([
        (t("открытый файл", "open file"), "cyan"), (t("чат", "chat"), "violet"), (t("репозиторий", "repository"), "violet"), (t("экран", "screen"), "green")]))
    ar = lambda x1, y, x2: (f'<path d="M{x1} {y}H{x2}" stroke="var(--dim)" stroke-width="3" fill="none"/>'
                            f'<path d="M{x2 - 12} {y - 10}l12 10-12 10" stroke="var(--dim)" stroke-width="3" fill="none"/>')
    svg = f'''<svg viewBox="0 0 900 540" class="fig" style="width:100%;height:auto">
    <rect x="20" y="40" width="250" height="84" rx="12" fill="var(--surface)" stroke="var(--amber)" stroke-width="3"/>
    <text x="145" y="92" text-anchor="middle" class="s26b" fill="var(--amber)">{t("Ваш вопрос", "Your question")}</text>
    <text x="20" y="214" class="s21b" fill="var(--muted)">{t("Контекст: что он видит", "Context: what it sees")}</text>
    {chips}
    {ar(270, 82, 356)}
    <path d="M286 242V454" stroke="var(--dim)" stroke-width="3" fill="none"/>
    {ar(286, 348, 356)}
    <rect x="356" y="40" width="230" height="450" rx="16" fill="var(--cyan)" fill-opacity=".12" stroke="var(--cyan)" stroke-width="3"/>
    <text x="471" y="240" text-anchor="middle" class="s30" fill="var(--cyan)">{t("Модель", "Model")}</text>
    <text x="471" y="280" text-anchor="middle" class="s23" fill="var(--fg)">{t("такая же, как", "the same kind as")}</text>
    <text x="471" y="310" text-anchor="middle" class="s23" fill="var(--fg)">{t("в уроке L03", "in lesson L03")}</text>
    {ar(586, 265, 650)}
    <rect x="650" y="215" width="230" height="100" rx="12" fill="var(--surface)" stroke="var(--green)" stroke-width="3"/>
    <text x="765" y="273" text-anchor="middle" class="s26b" fill="var(--green)">{t("Ответ", "Answer")}</text>
    </svg>'''
    code = ('<span class="cm"># L03</span>\n'
            'resp = client.models.generate_content(\n'
            '    model=MODEL,\n'
            '    contents=question + file_text)')
    return dict(min=4, html=f'''
  {head(t("Как это устроено", "How it works"), t("Внутри та же модель, что в L03; важно, что она видит", "Same model as in L03: what matters is what it sees"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:44px;align-items:center;flex:none;">
      {svg}
      <div class="stack" style="gap:20px;">
        <div class="prompt-label">{t("Вы уже делали так в Colab", "You already did this in Colab")}</div>
        <pre class="code sm">{code}</pre>
        <div class="note" style="--k:var(--amber)">{t("Copilot делает такой вызов сам и <b>подставляет ваш файл</b> в запрос. Больше нужного контекста — лучше ответ.", "Copilot makes this call itself and <b>adds your file</b> to the request. More of the right context, a better answer.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «Вы уже делали это в Colab. Copilot — тот же вызов, только с вашим файлом внутри.»",
                      "⏱ 4 min. “You already did this in Colab. Copilot is that call with your file attached.”"),
                    t("Слева то, что попадает в запрос: ваш вопрос и контекст. Контекст — это всё, что ассистент видит в момент ответа: открытый файл, чат, репозиторий, окно на экране. В центре модель того же типа, которую мы вызывали из Python в L03. Справа ответ.",
                      "On the left is what goes into the request: your question and the context. Context is everything the assistant sees when it answers: the open file, the chat, the repository, the window on screen. In the centre is the same kind of model we called from Python in L03. On the right is the answer."),
                    t("Отсюда простое правило для всего урока: не получилось — покажите ассистенту нужное. Назовите файл, откройте окно, вставьте текст. Модель не ленится и не прячет знания, она просто не видит того, чего ей не показали.",
                      "From this comes a simple rule for the whole lesson: if it did not work, show the assistant the right thing. Name the file, open the window, paste the text. The model is not lazy and does not hide anything; it just cannot see what it was not shown.")))


# ---------------------------------------------------------------- 05 Teams
def s_teams():
    sec = {"ru": ("Решения", "Открытые вопросы", "Задачи"), "en": ("Decisions", "Open questions", "Action items")}[LANG]
    dec = [t("Prime: бесплатная доставка от $75 в городе", "Prime: free delivery from $75 in the city"),
           t("От $100 бесплатно для всех, как раньше", "From $100 free for everyone, as before"),
           t("Вне зоны ничего не меняется", "Nothing changes outside the zone")]
    opn = [t("Кто ведёт запуск флага?", "Who owns the flag rollout?"),
           t("Какое число покажет рост затрат?", "Which number shows costs going up?")]
    act = [t("Павел: правило и тесты", "Pavel: rule and tests"), t("Анна: бриф и issue", "Anna: brief and issue"),
           t("Ола: ответ для поддержки", "Ola: support reply")]
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return dict(min=5, html=f'''
  {head(t("Teams", "Teams"), t("Teams: встреча превращается в решения и задачи", "Teams: a meeting becomes decisions and action items"))}
  <div class="body">
    <div class="mock dk teams">
      <div class="bar">{dots()}<span class="ttl">{t("Prime delivery rule — собрание", "Prime delivery rule — meeting")}</span><span class="rec"><i></i>{t("запись и расшифровка", "recording and transcript")}</span>{sch()}</div>
      <div class="tm-body">
        <div class="call">
          <div class="tiles">
            <div class="tile"><span class="av a1">A</span><b>Anna</b></div>
            <div class="tile"><span class="av a2">P</span><b>Pavel</b></div>
            <div class="tile"><span class="av a3">O</span><b>Ola</b></div>
            <div class="tile you"><span class="av a4">+</span><b>{t("Вы", "You")}</b></div>
          </div>
          <div class="ctl"><span class="c">&#9679;</span><span class="c">&#9632;</span><span class="c">&#9654;</span><span class="c red">{t("выйти", "leave")}</span></div>
        </div>
        <div class="pane">
          <div class="ph"><span class="spark">&#10022;</span> Copilot <small>{t("Итоги встречи", "Recap")}</small></div>
          <h4>{sec[0]}</h4><ul>{li(dec)}</ul>
          <h4>{sec[1]}</h4><ul>{li(opn)}</ul>
          <h4>{sec[2]}</h4><ul>{li(act)}</ul>
          <div class="ask">{t("Что я пропустил?", "What did I miss?")}</div>
        </div>
      </div>
    </div>
    <div class="foot-note">{t("Нужны расшифровка встречи и Copilot с лицензией. Нет доступа: вставьте <code>meeting_notes.md</code> в бесплатный Copilot Chat.",
                              "You need a meeting transcript and licensed Copilot. No access: paste <code>meeting_notes.md</code> into free Copilot Chat.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. «Анна не вела записей. Записи вёл Copilot.»", "⏱ 5 min. “Anna took no notes. Copilot did.”"),
                    t("Панель справа — то, что Copilot собрал по расшифровке: три решения, два открытых вопроса, три задачи с именами. Тот же текст лежит у нас в файле meeting_notes.md. Покажите его студентам, сравните со слайдом.",
                      "The pane on the right is what Copilot builds from the transcript: three decisions, two open questions, three tasks with names. The same text is in our file meeting_notes.md. Show it to the students and compare with the slide."),
                    t("Что важно знать: итоги работают, только если встреча записана и расшифрована, и у вас есть Copilot с лицензией. Без этого берите бесплатный Copilot Chat и вставляйте текст заметок сами. Это тот же приём: показать ассистенту нужное.",
                      "What to know: the recap works only if the meeting is recorded and transcribed and you have licensed Copilot. Without it, use free Copilot Chat and paste the notes yourself. It is the same trick: show the assistant the right thing."),
                    t("Если кнопка не там, где на схеме: «кнопка переехала, правило осталось». Не больше 90 секунд на поиск, дальше вставьте текст в чат.",
                      "If the button is not where the schematic shows it: “the button moved, the rule did not.” No more than 90 seconds of searching, then paste the text into the chat.")))


# ---------------------------------------------------------------- 06 Word
def s_word():
    prompt = t("Используя только эти заметки, напиши бриф на одну страницу: решения, открытые вопросы, ответственные. В конце перечисли предложения, которые добавил ты.",
               "Using only these notes, write a one-page brief: decisions, open questions, owners. At the end list which sentences are yours.")
    return dict(min=5, html=f'''
  {head(t("Word", "Word"), t("Word: из заметок — бриф на одну страницу", "Word: from notes to a one-page brief"))}
  <div class="body">
    <div class="mock lt word">
      <div class="bar">{dots()}<span class="ttl">brief.docx — Word</span>{sch()}</div>
      <div class="tabs"><span>{t("Файл", "File")}</span><span class="on">{t("Главная", "Home")}</span><span>{t("Вставка", "Insert")}</span><span>{t("Рецензирование", "Review")}</span><span class="cp">&#10022; Copilot</span></div>
      <div class="wd-body">
        <div class="page">
          <h3>{t("Бриф: бесплатная доставка для Prime", "Brief: free delivery for Prime")}</h3>
          <p><span class="src">{t("Подписчики Prime получают бесплатную доставку от заказа $75 внутри города. От $100 бесплатно для всех, как раньше. Вне зоны ничего не меняется.",
                                  "Prime subscribers get free delivery from a $75 order inside the city. From $100 it is free for everyone, as before. Nothing changes outside the zone.")}</span></p>
          <p><span class="src">{t("Павел делает правило за флагом на стейджинге, Ола обновляет ответ для поддержки. Кто ведёт запуск флага — пока открытый вопрос.",
                                  "Pavel builds the rule behind a flag on staging, Ola updates the support reply. Who owns the flag rollout is still open.")}</span></p>
          <p><span class="inv">{t("Ожидаемый эффект: больше повторных заказов.", "Expected effect: more repeat orders.")}</span></p>
          <div class="co c1">{t("из заметок", "from the notes")}</div>
          <div class="co c2">{t("слова Copilot: в заметках этого нет", "Copilot’s words: not in the notes")}</div>
        </div>
        <div class="pane">
          <div class="ph"><span class="spark">&#10022;</span> Copilot</div>
          <div class="me">{prompt}</div>
          <div class="ai">{t("Готово. Добавил я: «Ожидаемый эффект…».", "Done. Added by me: “Expected effect…”.")}</div>
        </div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. «Её запрос заканчивается так: перечисли, какие строки твои.»", "⏱ 5 min. “Her prompt ends with: list which lines are yours.”"),
                    t("Живая часть, 3 минуты: Copilot в Word или бесплатный Copilot Chat в Edge с вставленным meeting_notes.md. Запрос на слайде справа. Три приёма: дать источник, попросить структуру, потребовать пометить придуманное.",
                      "Live part, 3 minutes: Copilot in Word, or free Copilot Chat in Edge with meeting_notes.md pasted in. The prompt is on the right of the slide. Three moves: give the source, ask for a structure, demand a mark on what was invented."),
                    t("Проверка: $75 для Prime, $100 остаётся, вне зоны без изменений, владелец флага открыт. На слайде зелёным помечено то, что есть в заметках, жёлтым то, что добавил Copilot. Последняя строка про повторные заказы — в заметках её нет, её надо удалить или проверить.",
                      "Check: $75 for Prime, $100 stays, nothing changes outside the zone, the flag owner is open. On the slide green marks what is in the notes, yellow what Copilot added. The last line about repeat orders is not in the notes: delete it or verify it."),
                    t("Если нет доступа: покажите fallback_outputs/brief_expected.md. Это заранее подготовленный текст, не ответ ИИ.",
                      "If there is no access: show fallback_outputs/brief_expected.md. It is a prepared text, not AI output.")))


# ---------------------------------------------------------------- 07 Outlook + Excel
def s_outlook_excel():
    mails = [("Ola", t("Клиенты спрашивают, почему некоторые Prime-заказы платят за доставку.", "Customers ask why some Prime orders still pay for delivery.")),
             ("Anna", t("Потому что правило только для города и от $75.", "Because the rule is city only, from $75.")),
             ("Ola", t("Можно это одной фразой в ответ поддержки?", "Can we put that in one sentence in the support reply?"))]
    ml = "".join(f'<div class="mail"><b>{a}</b><span>{b}</span></div>' for a, b in mails)
    rows = "".join(
        f'<tr><td>{o[0]}</td><td>{o[1]}</td><td>{"TRUE" if o[2] else "FALSE"}</td><td class="r">{o[3]:.2f}</td></tr>' for o in ORDERS)
    return dict(min=3, html=f'''
  {head(t("Outlook и Excel", "Outlook and Excel"), t("Outlook и Excel: та же кнопка, другой контекст", "Outlook and Excel: the same button, a different context"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:34px;flex:none;align-items:stretch;">
      <div class="mock lt outlook">
        <div class="bar">{dots()}<span class="ttl">Outlook — {t("ответ поддержки", "support reply")}</span>{sch()}</div>
        <div class="ol-body">{ml}
          <div class="sum"><div class="sh"><span class="spark">&#10022;</span> {t("Кратко", "Summary")}</div>
          {t("Prime: бесплатно от $75, только город. Ола просит одну фразу для ответа. Открыто: кто её отправит.", "Prime: free from $75, city only. Ola wants one sentence for the reply. Open: who sends it.")}</div>
        </div>
      </div>
      <div class="mock lt excel">
        <div class="bar">{dots()}<span class="ttl">orders.xlsx — Excel</span>{sch()}</div>
        <div class="xl-body">
          <table><thead><tr><th>order_id</th><th>zone</th><th>is_prime</th><th class="r">subtotal</th></tr></thead><tbody>{rows}</tbody></table>
          <div class="sum"><div class="sh"><span class="spark">&#10022;</span> Copilot</div>
          {t(f"Больше всего Prime-заказов от $75 в зоне {TOP_ZONE}: {TOP_N} из {TOP_ALL}.", f"Most Prime orders from $75 are in zone {TOP_ZONE}: {TOP_N} of {TOP_ALL}.")}</div>
        </div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. «Та же модель, другое окно. Вторая половина про Excel — это целый урок L08.»", "⏱ 3 min. “Same model, different window. The Excel half is a whole lesson, L08.”"),
                    t("Слева ветка писем из Outlook: Copilot делает краткое содержание. Контекст здесь открытое письмо. Справа таблица из восьми заказов в Excel: Copilot отвечает на вопрос по таблице. Контекст здесь открытый файл.",
                      "On the left is a mail thread in Outlook: Copilot writes a summary. The context here is the open mail. On the right is a table of eight orders in Excel: Copilot answers a question about the table. The context here is the open file."),
                    t(f"Число на слайде посчитано по этим восьми строкам: Prime-заказов от $75 пять, из них {TOP_N} в зоне {TOP_ZONE}. Данные придуманы. Анализ таблиц разберём на следующем уроке.",
                      f"The number on the slide is counted from these eight rows: five Prime orders from $75, {TOP_N} of them in zone {TOP_ZONE}. The data is made up. We cover spreadsheet analysis next lesson.")))


# ---------------------------------------------------------------- 08 free vs paid
def s_money():
    svg = f'''<svg viewBox="0 0 640 600" class="fig" style="width:100%;height:auto">
    <circle cx="320" cy="300" r="290" fill="var(--amber)" fill-opacity=".07" stroke="var(--amber)" stroke-width="3" stroke-dasharray="10 8"/>
    <circle cx="320" cy="290" r="176" fill="var(--green)" fill-opacity=".10" stroke="var(--green)" stroke-width="3"/>
    <circle cx="320" cy="214" r="22" fill="none" stroke="var(--fg)" stroke-width="4"/>
    <path d="M276 270a44 44 0 0 1 88 0" fill="none" stroke="var(--fg)" stroke-width="4" stroke-linecap="round"/>
    <text x="320" y="316" text-anchor="middle" class="s23b" fill="var(--fg)">{t("Вы", "You")}</text>
    <text x="320" y="352" text-anchor="middle" class="s21" fill="var(--muted)">{t("то, что вы вставили", "what you paste")}</text>
    <text x="320" y="378" text-anchor="middle" class="s21" fill="var(--muted)">{t("или открыли", "or open")}</text>
    <text x="320" y="414" text-anchor="middle" class="s23b" fill="var(--green)">{t("бесплатно", "free")}</text>
    <text x="320" y="522" text-anchor="middle" class="s21" fill="var(--muted)">{t("почта, файлы, встречи, чаты", "mail, files, meetings, chats")}</text>
    <text x="320" y="556" text-anchor="middle" class="s23b" fill="var(--amber)">{t("нужна лицензия", "needs a licence")}</text>
    </svg>'''
    gh = [("Free", "$0", t("ограниченное число подсказок и запросов в чат в месяц", "limited completions and chat per month")),
          ("Pro", "$10", t("в месяц", "per month")), ("Pro+", "$39", t("в месяц", "per month")),
          ("Business", "$19", t("за человека в месяц", "per user per month")), ("Enterprise", "$39", t("за человека в месяц", "per user per month"))]
    ghr = "".join(f'<div class="pr"><span class="n">{a}</span><span class="d">{c}</span><span class="v">{b}</span></div>' for a, b, c in gh)
    return dict(min=4, html=f'''
  {head(t("Деньги", "Money"), t("Что бесплатно, а что по подписке", "What is free and what is paid"),
        t("Бесплатно: веб и то, что вы дали сами. По лицензии: ваши почта, файлы и встречи в рамках ваших прав.", "Free: the web and what you give it yourself. Licensed: your mail, files and meetings within your permissions."),
        badge=t("октябрь 2026 · цены США, USD", "October 2026 · US prices, USD"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:.8fr 1.2fr;gap:36px;align-items:center;flex:none;">
      {svg}
      <div class="stack" style="gap:18px;">
        <div class="pbox" style="--k:var(--violet)"><div class="ph">GitHub Copilot</div>{ghr}</div>
        <div class="pbox" style="--k:var(--cyan)"><div class="ph">Microsoft</div>
          <div class="pr"><span class="n">Copilot Chat</span><span class="d">{t("с рабочим аккаунтом Microsoft 365: веб и то, что вы открыли или приложили", "with a Microsoft 365 work account: the web and what you open or attach")}</span><span class="v g">{t("входит", "included")}</span></div>
          <div class="pr"><span class="n">{t("С лицензией", "Licensed")}</span><span class="d">{t("Microsoft 365 Copilot, Enterprise / Business, оплата за год", "Microsoft 365 Copilot, Enterprise / Business, billed yearly")}</span><span class="v">$30 / $23.50</span></div>
        </div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «Если Copilot не нашёл ваш файл, он не сломался. Он просто его не видит.»", "⏱ 4 min. “If it cannot find your file, it is not broken. It just cannot see it.”"),
                    t("Это единственный слайд с ценами и названиями тарифов, поэтому на нём стоит дата: октябрь 2026. Всё остальное в уроке держится на стабильных словах. Перед занятием откройте страницы тарифов и сверьте цифры.",
                      "This is the only slide with prices and plan names, which is why it carries a date: October 2026. Everything else in the lesson uses stable words. Before class, open the plan pages and check the numbers."),
                    t("Внутреннее кольцо: то, что вы вставили или открыли. Это можно получить бесплатно: Copilot Chat с рабочим аккаунтом Microsoft 365 и GitHub Copilot Free. Внешнее кольцо: ваши письма, файлы, встречи и чаты. Для него нужна лицензия, и Copilot увидит только то, к чему доступ есть у вас. Для студентов у GitHub есть отдельный бесплатный план Copilot Student.",
                      "The inner ring: what you paste or open. You can get this for free: Copilot Chat with a Microsoft 365 work account and GitHub Copilot Free. The outer ring: your mail, files, meetings and chats. It needs a licence, and Copilot sees only what you have access to. GitHub also has a separate free plan for verified students, Copilot Student."),
                    t("Про названия: Microsoft переименовывает Microsoft 365 Copilot в Microsoft Copilot, вы будете видеть оба имени. Это не новый продукт. Цены справа: GitHub по тарифам, Microsoft за лицензию при оплате за год, Business $23.50, Enterprise $30.",
                      "About names: Microsoft is renaming Microsoft 365 Copilot to Microsoft Copilot; you will see both names. It is not a new product. Prices on the right: GitHub by plan, Microsoft per licence billed yearly, Business $23.50, Enterprise $30.")))


# ---------------------------------------------------------------- 09 GitHub issue
def s_issue():
    bl = [t("Prime с заказом <b>от $75</b>: бесплатная доставка <b>в городе</b>", "Prime with an order <b>of $75 or more</b>: free delivery <b>in the city</b>"),
          t("Бесплатно <b>от $100</b> для всех, как раньше", "Free <b>from $100</b> for everyone, as before"),
          t("Вне зоны <b>ничего не меняется</b> (плата $18.00)", "Outside the zone <b>nothing changes</b> (fee $18.00)"),
          t("Тесты на границу: 75 и 74.99, и один тест без Prime", "Boundary tests: 75 and 74.99, and one non-Prime test"),
          t("Ошибка при отрицательной сумме остаётся", "The error for a negative subtotal stays")]
    li = "".join(f"<li>{x}</li>" for x in bl)
    return dict(min=3, html=f'''
  {head(t("GitHub", "GitHub"), t("GitHub issue: бриф становится задачей для разработчика", "GitHub issue: the brief becomes a task for the developer"))}
  <div class="body">
    <div class="mock dk gh">
      <div class="bar">{dots()}<span class="ttl">courier-app / Issues</span>{sch()}</div>
      <div class="gh-body">
        <div class="main">
          <h3>{t("Бесплатная доставка для Prime от $75", "Free delivery for Prime customers from $75")} <small>#12</small></h3>
          <div class="st"><span class="open">&#9679; {t("Открыт", "Open")}</span> <span>Anna {t("открыла задачу", "opened this issue")}</span></div>
          <div class="cm"><ul>{li}</ul>
            <div class="acc"><b>{t("Приёмка", "Acceptance")}:</b> {t("все тесты проходят, изменение небольшое.", "all tests pass, the change is small.")}</div></div>
        </div>
        <div class="side">
          <h5>{t("Исполнитель", "Assignees")}</h5><div class="it"><span class="av a2">P</span> Pavel</div>
          <h5>{t("Метки", "Labels")}</h5><div class="it"><span class="lbl">feature</span></div>
          <h5>Copilot</h5><div class="it off">{t("Назначить на Copilot", "Assign to Copilot")}</div>
          <div class="hint">{t("Облачный агент: платные тарифы. Разбор в L16.", "Cloud agent: paid plans. Covered in L16.")}</div>
        </div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. «Эта задача и есть запрос. Copilot прочитает её слово в слово.»", "⏱ 3 min. “This issue is the prompt. Copilot reads it word for word.”"),
                    t("Issue — это задача на GitHub с номером. Анна переписала бриф как задачу: цифры, что не должно измениться, какие тесты нужны. Хорошая задача содержит ровно это: числа, границы и список проверок.",
                      "An issue is a task on GitHub, with a number. Anna rewrote the brief as a task: numbers, what must not change, which tests are needed. A good issue contains exactly this: numbers, boundaries and a list of checks."),
                    t("Справа серая кнопка «Назначить на Copilot». Это облачный агент: он сам берёт задачу и открывает pull request. Он есть на платных тарифах, на Free его нет. Сегодня мы его не используем, подробно в L16.",
                      "On the right is the grey “Assign to Copilot” entry. That is the cloud agent: it takes the task itself and opens a pull request. It is on paid plans, not on Free. We do not use it today; details in L16.")))


# ---------------------------------------------------------------- 10 VS Code
def s_editor():
    import difflib
    base = (KIT / "sample_repo" / "delivery_fee.py").read_text(encoding="utf-8").splitlines()
    sol = (KIT / "sample_repo" / "expected_solution" / "delivery_fee.py").read_text(encoding="utf-8").splitlines()
    added = set()
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, base, sol).get_opcodes():
        if tag == "insert":
            added.update(range(j1, j2))
    first = min(added)
    rows = ""
    for idx in range(10, len(sol)):  # file lines 11..end
        line = sol[idx]
        if idx == first:
            typed = "    if order.zone"
            rows += f'<div class="ln"><i>{idx + 1}</i><span>{esc(typed)}<em>{esc(line[len(typed):])}</em></span></div>'
        elif idx in added:
            rows += f'<div class="ln"><i>{idx + 1}</i><span><em>{esc(line)}</em></span></div>'
        else:
            rows += f'<div class="ln"><i>{idx + 1}</i><span>{esc(line)}</span></div>'
    return dict(min=6, html=f'''
  {head(t("Редактор", "The editor"), t("В редакторе Copilot помогает тремя способами", "In the editor Copilot helps in three ways"),
        t("<b>Подсказка</b> дописывает строку, <b>чат</b> отвечает про открытый файл, <b>агент</b> сам правит файлы и запускает тесты.",
          "<b>Completion</b> finishes your line, <b>chat</b> answers about the open file, an <b>agent</b> edits files and runs tests itself."))}
  <div class="body" style="margin-top:14px;">
    <div class="mock dk vsc">
      <div class="bar">{dots()}<span class="ttl">delivery_fee.py — courier-app — VS Code</span>{sch()}</div>
      <div class="vs-body">
        <div class="act"><i></i><i></i><i></i></div>
        <div class="exp"><h6>{t("ПРОЕКТ", "PROJECT")}</h6><div class="f">ISSUE.md</div><div class="f on">delivery_fee.py</div><div class="f">test_delivery_fee.py</div><div class="f">copilot-instructions.md</div></div>
        <div class="ed"><div class="tab">delivery_fee.py</div>{rows}
          <div class="term"><b>{t("ТЕРМИНАЛ", "TERMINAL")}</b><div>$ python -m unittest -v</div><div class="ok">Ran {N_TESTS} tests ... OK</div></div>
        </div>
        <div class="chat"><div class="ph"><span class="spark">&#10022;</span> Copilot</div>
          <div class="me">{t("Прочитай ISSUE.md и инструкции, предложи план. Не правь.", "Read ISSUE.md and the instructions, propose a plan. Do not edit.")}</div>
          <div class="ai">{t("План: 1) ветка для Prime в городе от 75, 2) правило $100 не трогать, 3) три теста.", "Plan: 1) a Prime branch for the city from 75, 2) leave the $100 rule, 3) three tests.")}</div>
          <div class="me">{t("Сделай и запусти тесты.", "Implement it and run the tests.")}</div>
          <div class="ai">{t(f"Готово: +{N_LOGIC} строки в delivery_fee.py, +{N_NEW} теста. Тесты запущены.", f"Done: +{N_LOGIC} lines in delivery_fee.py, +{N_NEW} tests. Tests ran.")}</div>
        </div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. «Павел печатает <code>if order.zone</code>, и серый текст сам заканчивает правило.»", "⏱ 6 min. “Pavel types <code>if order.zone</code> and the grey text finishes the rule.”"),
                    t("Три способа. Первый: подсказка. Серый текст в строке — предложение редактора, Tab принимает. Второй: чат справа, вы спрашиваете про открытый файл. Третий: агент, он сам правит несколько файлов и запускает команды, а вы проверяете результат. Названия режимов в программе меняются, смотрите на то, что делает кнопка.",
                      "Three ways. First: completion. The grey text in the line is the editor’s proposal; Tab accepts it. Second: the chat on the right, where you ask about the open file. Third: an agent, which edits several files and runs commands itself while you check the result. Mode names in the app change; look at what the button does."),
                    t("Живая часть, 8 минут вместе со следующим слайдом: VS Code и GitHub Copilot Free. Запрос 1 в чат: «Прочитай ISSUE.md и инструкции, предложи план, не правь». Запрос 2: «Сделай, добавь тесты на границу, запусти тесты». Если агента нет, вставьте код из чата вручную.",
                      "Live part, 8 minutes together with the next slide: VS Code and GitHub Copilot Free. Prompt 1 in chat: “Read ISSUE.md and the instructions, propose a plan, do not edit.” Prompt 2: “Implement it, add boundary tests, run the tests.” If there is no agent, paste the code from the chat by hand."),
                    t("Глубина: агенты и редакторы разберём в L16. Сегодня нам нужно одно: видеть, что именно изменилось.", "Depth: agents and editors come in L16. Today we need one thing: to see what exactly changed.")))


# ---------------------------------------------------------------- 11 real result
def s_result():
    tests = "".join(f'<div><span class="nm">{x["name"]}</span> <span class="ok">... {x["result"]}</span></div>' for x in ART["tests"])
    return dict(min=6, html=f'''
  {head(t("Результат", "The result"), t(f"Результат: {N_LOGIC} строки в diff и {N_TESTS} зелёных тестов", f"The result: a {N_LOGIC}-line diff and {N_TESTS} green tests"),
        t("Это настоящий запуск, не рисунок. Смотрите на diff и тесты, а не на слово «готово».", "This is a real run, not a drawing. Look at the diff and the tests, not at the word “done”."))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:36px;align-items:start;flex:none;">
      <div class="stack" style="gap:8px;"><div class="prompt-label">git diff -U1</div>{diff_block(DL)}</div>
      <div class="stack" style="gap:18px;">
        <div><div class="prompt-label">python -m unittest -v</div>
          <div class="tout">{tests}<div class="sep"></div><div>Ran {N_TESTS} tests</div><div class="ok big">OK</div></div></div>
        <div class="stats">
          <div class="stat" style="--k:var(--green)"><div class="n">{N_TESTS}</div><div class="d">{t("тестов ok", "tests ok")}</div></div>
          <div class="stat" style="--k:var(--cyan)"><div class="n">+{N_LOGIC}</div><div class="d">{t("строки логики", "lines of logic")}</div></div>
          <div class="stat" style="--k:var(--amber)"><div class="n">+{N_NEW}</div><div class="d">{t("новых теста", "new tests")}</div></div>
        </div>
        <div class="small">{t("Имена тестов сокращены, остальное без правок. Границы: 75, 74.99, без Prime.", "Test names shortened, the rest untouched. Boundaries: 75, 74.99, non-Prime.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. «Ничего на этом слайде я не писал руками. Это настоящий запуск.»", "⏱ 6 min. “Nothing on this slide was written by me. This is the actual run.”"),
                    t("Diff — это точные строки, которые добавили и удалили. Зелёные плюсы: правило Prime, две строки. Ниже три новых теста. Тест — маленький скрипт, который проверяет одно правило: например, что заказ на 74.99 у Prime платит 7.50.",
                      "A diff is the exact lines that were added and removed. Green pluses: the Prime rule, two lines. Below are three new tests. A test is a small script that checks one rule: for example, that a 74.99 Prime order pays 7.50."),
                    t("Справа результат запуска: семь тестов, все зелёные. Сравните с базой: было четыре. Три новых проверяют границу 75, значение чуть ниже границы и клиента без Prime. Так мы убеждаемся, что остальное не сломалось.",
                      "On the right is the test run: seven tests, all green. Compare with the base: there were four. The three new ones check the 75 boundary, a value just below it, and a customer without Prime. This is how we see that nothing else broke."),
                    t("Это те же числа, что получатся у вас в VS Code с expected_solution. Если Copilot в классе сделает по-другому, сравните его diff с этим.",
                      "These are the same numbers you get in VS Code with expected_solution. If Copilot does it differently in class, compare its diff with this one.")))


# ---------------------------------------------------------------- 12 PR
def s_pr():
    fl = DF["delivery_fee.py"]
    n_t = ART["files"]["test_delivery_fee.py"]["added"]
    return dict(min=5, html=f'''
  {head(t("Ревью", "Review"), t("Pull request: Copilot-ревью — вторая пара глаз, не судья", "Copilot review: a second pair of eyes, not the judge"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.7fr 1fr;gap:30px;flex:none;align-items:stretch;">
      <div class="mock dk gh pr">
        <div class="bar">{dots()}<span class="ttl">courier-app / Pull requests</span>{sch()}</div>
        <div class="pr-body">
          <h3>{t("Бесплатная доставка для Prime от $75", "Free delivery for Prime from $75")} <small>#13</small></h3>
          <div class="tabs2"><span>{t("Обсуждение", "Conversation")}</span><span>{t("Коммиты", "Commits")} 1</span><span class="on">{t("Изменённые файлы", "Files changed")} 2</span></div>
          <div class="fh">{fl[0][5:] if fl[0].startswith("FILE ") else fl[0]} <small>+{ART["files"]["delivery_fee.py"]["added"]} −{ART["files"]["delivery_fee.py"]["removed"]}</small></div>
          {diff_block(fl[1:], "dif nb")}
          <div class="rc"><span class="av a5">&#10022;</span><div><b>Copilot</b> <small>{t("ревью", "review")}</small>
            <div>{t("Тест на границу 74.99 уже есть. Подумайте про <code>Decimal</code> для денег.", "The 74.99 boundary test is already there. Consider <code>Decimal</code> for money.")}</div></div></div>
          <div class="fh2">test_delivery_fee.py <small>+{n_t} −0</small></div>
        </div>
      </div>
      <div class="stack" style="gap:18px;justify-content:center;">
        <div class="status ok"><span class="tick">&#10003;</span><div><b>{t("Одобрено: Ола", "Approved: Ola")}</b><small>{t("человек принимает решение", "a person decides")}</small></div></div>
        <div class="status ok"><span class="tick">&#10003;</span><div><b>{t(f"Проверки: тесты {N_TESTS}/{N_TESTS}", f"Checks: tests {N_TESTS}/{N_TESTS}")}</b><small>{t("тесты — ворота", "tests are the gate")}</small></div></div>
        <div class="status"><span class="tick c">&#10022;</span><div><b>{t("Copilot: 1 комментарий", "Copilot: 1 comment")}</b><small>{t("это совет, не приказ", "a suggestion, not an order")}</small></div></div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. «Copilot нашёл одну вещь, над которой стоит подумать, и одну, которую он уже увидел покрытой.»", "⏱ 5 min. “Copilot found one thing worth thinking about and one thing it already saw covered.”"),
                    t("Pull request — это страница, где изменение показывают, обсуждают и принимают: «пожалуйста, примите моё изменение». Слева настоящий diff со слайда 11. Под изменённой строкой комментарий Copilot: тест на 74.99 уже есть, а деньги лучше считать в Decimal.",
                      "A pull request is the page where a change is shown, discussed and accepted: “please take my change.” On the left is the real diff from slide 11. Under the changed line is Copilot’s comment: the 74.99 test is already there, and money is better counted in Decimal."),
                    t("Справа три статуса. Ола одобрила: решает человек. Проверки зелёные: тесты — ворота. Комментарий Copilot — совет, а не приказ. Ревью Copilot работает на github.com в pull request, не в редакторе. Если платного доступа нет, подойдёт комментарий человека.",
                      "On the right are three statuses. Ola approved: a person decides. Checks are green: tests are the gate. Copilot’s comment is a suggestion, not an order. Copilot review works on github.com in a pull request, not in the editor. Without paid access, a human review comment is fine.")))


# ---------------------------------------------------------------- 13 instructions file
def s_instr():
    rules = (KIT / "sample_repo" / ".github" / "copilot-instructions.md").read_text(encoding="utf-8").splitlines()
    rules = [r[2:] for r in rules if r.startswith("- ")]
    assert len(rules) == 5
    names = {x["name"] for x in ART["tests"]}
    assert "test_prime_below_75_pays" in names and "test_outside_standard" in names
    ev = [t(f"в diff {N_LOGIC} строки логики", f"{N_LOGIC} lines of logic in the diff"),
          t("новых импортов: 0", "new imports: 0"),
          t("<code>test_outside_standard</code>: плата $18.00 как была", "<code>test_outside_standard</code>: fee still $18.00"),
          t("<code>test_prime_below_75_pays</code>: 74.99 платит $7.50", "<code>test_prime_below_75_pays</code>: 74.99 pays $7.50"),
          t("план в чате до правки (слайд 10)", "the plan in chat before the edit (slide 10)")]
    rows = "".join(f'<div class="rr"><span class="no">{i + 1}</span><span class="rl">{r}</span><span class="ar">&#10142;</span><span class="ev">{e}</span></div>'
                   for i, (r, e) in enumerate(zip(rules, ev)))
    return dict(min=3, html=f'''
  {head(t("Правила команды", "Team rules"), t("copilot-instructions.md — README для робота", "copilot-instructions.md: a README for the robot"),
        t("Короткий файл с правилами команды. Copilot читает его каждый раз.", "A short file of team rules. Copilot reads it every time."))}
  <div class="body" style="margin-top:14px;">
    <div class="file">
      <div class="fb">.github/copilot-instructions.md <span>{t("что из этого видно в результате", "where it shows in the result")}</span></div>
      {rows}
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. «Правило 4, “добавляй тесты на границу”, — причина, почему тест на 74.99 вообще существует.»", "⏱ 3 min. “Rule 4, ‘add boundary tests’, is why the 74.99 test exists.”"),
                    t("Это пользовательские инструкции: файл правил, который ассистент читает перед каждым запросом. Лежит в папке .github, в начале проекта. Пять строк слева, а справа то, где каждая видна в нашем результате.",
                      "These are custom instructions: a file of rules the assistant reads before every request. It lives in the .github folder at the start of the project. Five lines on the left, and on the right where each one shows in our result."),
                    t("Совет: файл должен быть коротким. Длинный свод правил никто не соблюдает, ни люди, ни роботы. Пишите правила, которые можно проверить по diff или по тестам.",
                      "Tip: keep the file short. Nobody follows a long rulebook, neither people nor robots. Write rules you can check in the diff or in the tests.")))


# ---------------------------------------------------------------- 14 where GitHub Copilot lives
def s_doors():
    def pin(c):
        return (f'<svg viewBox="0 0 48 60" width="48" height="60"><path d="M24 2C12 2 4 11 4 22c0 15 20 36 20 36s20-21 20-36C44 11 36 2 24 2z" fill="var(--{c})"/>'
                f'<circle cx="24" cy="22" r="8" fill="var(--bg)"/></svg>')
    doors = [("violet", t("Редактор", "Editor"), "VS Code, JetBrains, Visual Studio", t("Вы пишете код: подсказка, чат, агент", "You write code: completion, chat, agent"), t("Сегодня", "Today"), t("есть на Free", "on Free"), "green"),
             ("cyan", "github.com", t("issue и pull request", "issues and pull requests"), t("Вы просите ревью на странице изменения", "You ask for a review on the change page"), t("Сегодня", "Today"), t("зависит от тарифа", "depends on the plan"), "amber"),
             ("green", t("Терминал", "Terminal"), "Copilot CLI", t("Вы пишете задачу в командной строке", "You type a task in the command line"), "L16", t("есть на Free", "on Free"), "green"),
             ("amber", t("Облако", "Cloud"), t("облачный агент", "cloud agent"), t("Берёт issue и сам открывает pull request", "Takes an issue and opens a pull request itself"), "L16", t("платные тарифы", "paid plans"), "amber")]
    cols = ""
    for c, h, sub, what, badge, free, fc in doors:
        cols += f'''<div class="door" style="--k:var(--{c})"><div class="pin">{pin(c)}</div><div class="dh">{h}</div><div class="ds">{sub}</div>
          <div class="dw">{what}</div><div class="db"><span class="badge{" solid" if badge == t("Сегодня", "Today") else ""}">{badge}</span></div>
          <div class="df" style="--f:var(--{fc})">{free}</div></div>'''
    return dict(min=3, html=f'''
  {head(t("Карта GitHub Copilot", "GitHub Copilot map"), t("Четыре двери к одному GitHub Copilot; сегодня мы прошли две", "Four doors to one GitHub Copilot; today we used two"))}
  <div class="body"><div class="doors">{cols}</div></div>''',
                notes=notes(
                    t("⏱ 3 мин. «Запомните карту. В L16 мы пройдём по каждой комнате.»", "⏱ 3 min. “Remember the map. In L16 we walk through every room.”"),
                    t("Один и тот же помощник живёт в четырёх местах. Редактор: подсказки, чат, агент. github.com: issue и pull request, там же ревью. Терминал: Copilot CLI. Облако: агент, который сам берёт задачу и открывает pull request. Сегодня мы работали в редакторе и в pull request.",
                      "The same assistant lives in four places. The editor: completion, chat, agent. github.com: issues and pull requests, and the review there. The terminal: Copilot CLI. The cloud: an agent that takes a task itself and opens a pull request. Today we worked in the editor and in a pull request."),
                    t("Что доступно на бесплатном уровне, зависит от тарифа и меняется, поэтому цифр здесь нет. Редактор и терминал есть на Free. Облачного агента на Free нет. Сверяйте со страницей тарифов перед занятием.",
                      "What is available on the free level depends on the plan and changes, so there are no numbers here. The editor and the terminal are on Free. The cloud agent is not on Free. Check the plans page before class.")))


# ---------------------------------------------------------------- 15 break
def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут: кофе и отдых от экрана", "5 minutes: coffee and a rest from the screen")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: клавиша Copilot в Windows, чек-лист релиза, шесть проверок и домашнее задание.", "Next: the Copilot key in Windows, the release checklist, six checks and homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт». Только отдых, без заданий в чате.", "⏱ 5 min. Press “Start”. Rest only, no chat tasks.")))


# ---------------------------------------------------------------- 16 Windows
def s_windows():
    keys = [("Ctrl", 84, False), ("Win", 84, False), ("Alt", 84, False), ("", 150, False), ("Alt", 84, False), ("", 100, True), ("Ctrl", 84, False)]
    x, ks = 10, ""
    for lab, w, hl in keys:
        if hl:
            ks += (f'<rect x="{x}" y="14" width="{w}" height="64" rx="9" fill="var(--green)" fill-opacity=".25" stroke="var(--green)" stroke-width="4"/>'
                   f'<path d="M{x + 34} 46a16 16 0 1 1 32 0 16 16 0 0 1-32 0z" fill="none" stroke="var(--green)" stroke-width="3.5"/>')
        else:
            ks += (f'<rect x="{x}" y="14" width="{w}" height="64" rx="9" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>'
                   f'<text x="{x + w / 2}" y="54" text-anchor="middle" class="s26" fill="var(--muted)">{lab}</text>')
        x += w + 10
    row2 = "".join(f'<rect x="{10 + i * 98}" y="14" width="88" height="40" rx="8" fill="var(--surface)" fill-opacity=".6" stroke="var(--line)"/>' for i in range(7))
    ks = row2 + f'<g transform="translate(0 58)">{ks}</g>'
    kb = f'<svg viewBox="0 0 {x} 156" class="fig" style="width:100%;height:auto">{ks}</svg>'
    chips = [t("Чат и голос", "Chat and voice"), t("Vision: видит выбранное окно", "Vision: sees the window you pick"),
             t("Поиск по файлам: docx, xlsx, pptx, txt, pdf", "File search: docx, xlsx, pptx, txt, pdf"), t("Скриншоты", "Screenshots")]
    cl = "".join(f"<li>{c}</li>" for c in chips)
    return dict(min=6, html=f'''
  {head(t("Windows", "Windows"), t("Windows: Copilot видит только то окно, которое вы показали", "Windows: Copilot sees only the window you shared"))}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:1.45fr 1fr;gap:36px;flex:none;align-items:center;">
      <div class="mock dk desk">
        <div class="bar">{dots()}<span class="ttl">Windows</span>{sch()}</div>
        <div class="dk-body">
          <div class="np"><div class="nb"><i></i> release_checklist.txt</div><div class="nl">{CHECKLIST[0]}</div><div class="nl">{CHECKLIST[1]}</div><div class="nl">{CHECKLIST[2]}</div><div class="shared">{t("окно показано Copilot", "window shared with Copilot")}</div></div>
          <div class="cpw"><div class="ph"><span class="spark">&#10022;</span> Copilot</div>
            <div class="me">{t("Что в этом окне?", "What is in this window?")}</div>
            <div class="ai">{t("Это чек-лист релиза, шесть пунктов.", "This is a release checklist, six items.")}</div>
            <div class="comp"><span>&#127908;</span><span class="vis">&#9673; Vision</span><span class="in">{t("Спросите о чём угодно", "Ask me anything")}</span></div></div>
        </div>
        <div class="tb"><span class="sb"></span><span class="sr"></span><i></i><i></i><i></i><span class="clk">09:15</span></div>
      </div>
      <div class="stack" style="gap:20px;">
        <div class="kb">{kb}<div class="cap" style="margin-top:6px"><b>{t("Клавиша Copilot", "The Copilot key")}</b> {t("или", "or")} <b>Win+C</b></div></div>
        <ul class="list" style="--k:var(--green)">{cl}</ul>
        <div class="small">{t("Рабочие аккаунты открывают веб-чат вместо приложения.", "Work accounts open the web chat instead of the app.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. «Павел нажимает одну клавишу и спрашивает про окно, которое он смотрит.»", "⏱ 6 min. “Pavel presses one key and asks about the window he is looking at.”"),
                    t("На клавиатуре у многих новых ноутбуков есть клавиша Copilot. Нет её — нажмите Win+C или откройте приложение. Приложение умеет чат и голос, поиск по вашим файлам (docx, xlsx, pptx, txt, pdf), скриншоты и Vision: ассистент смотрит на окно, которое вы сами выбрали.",
                      "Many new laptops have a Copilot key. If yours does not, press Win+C or open the app. The app does chat and voice, search over your files (docx, xlsx, pptx, txt, pdf), screenshots and Vision: the assistant looks at the window you chose yourself."),
                    t("Главное: он видит только то окно, которое вы показали. Не показали — не видит. Рабочие аккаунты Microsoft вместо приложения открывают веб-чат, это нормально. Доступность функций зависит от устройства, региона и версии Windows.",
                      "The main point: it sees only the window you shared. If you did not share it, it does not see it. Microsoft work accounts open the web chat instead of the app, which is normal. Feature availability depends on the device, region and Windows version."),
                    t("Одна строка про Copilot+ PC, не для слайда: часть функций, например Recall, нужна именно такой компьютер. Recall выпускали постепенно с апреля 2025, он выключен по умолчанию. У вас его может не быть, и для нашего урока он не нужен.",
                      "One line on Copilot+ PCs, not for the slide: some features, for example Recall, need exactly such a computer. Recall has been rolled out gradually since April 2025 and is off by default. You may not have it, and our lesson does not need it.")))


# ---------------------------------------------------------------- 17 Notepad
def s_notepad():
    lines = "".join(f'<div class="nl{" hl" if i == 5 else ""}">{esc(x)}</div>' for i, x in enumerate(CHECKLIST))
    return dict(min=3, html=f'''
  {head(t("Релиз", "Release day"), t("День релиза: Copilot читает открытый чек-лист", "Release day: Copilot reads the open checklist"))}
  <div class="body">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:40px;flex:none;align-items:center;">
      <div class="mock lt notepad">
        <div class="bar">{dots()}<span class="ttl">release_checklist.txt — {t("Блокнот", "Notepad")}</span>{sch()}</div>
        <div class="np-body"><div class="nl hd">{t("Курьерское приложение: чек-лист релиза", "Courier app: release checklist")}</div>{lines}</div>
      </div>
      <div class="stack" style="gap:22px;">
        <div class="ask-card">
          <div class="me">{t("Какой пункт поймает изменение платы вне зоны?", "Which item catches an outside-zone fee change?")}</div>
          <div class="ai"><span class="spark">&#10022;</span> {t("Пункт 6: «Откатите флаг, если плата вне зоны неожиданно изменилась».", "Item 6: “Roll back the flag if outside-zone fees change unexpectedly.”")}</div>
        </div>
        <div class="note" style="--k:var(--green)">{t("Файл открыт, значит ответ по файлу. Нет кнопки: <b>вставьте текст в чат</b>.", "The file is open, so the answer is about the file. No button: <b>paste the text into the chat</b>.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. «Какой пункт спасёт нас, если плата вне зоны сломается? Пункт 6, и Copilot его цитирует.»", "⏱ 3 min. “Which item saves us if outside-zone fees break? Item 6, and it quotes it.”"),
                    t("Живая часть, 3 минуты: откройте release_checklist.txt, нажмите клавишу Copilot, покажите окно через Vision или вставьте текст. Вопрос на слайде. Ответ должен цитировать пункт 6.",
                      "Live part, 3 minutes: open release_checklist.txt, press the Copilot key, share the window with Vision or paste the text. The question is on the slide. The answer should quote item 6."),
                    t("Это то же правило, что на слайде 4: локальный файл стал контекстом. Запасной вариант всегда один: вставить текст. Если ничего не открывается, покажите fallback_outputs/checklist_answer.md и идите дальше: кнопка переехала, правило осталось.",
                      "This is the same rule as slide 4: a local file became the context. The fallback is always one thing: paste the text. If nothing opens, show fallback_outputs/checklist_answer.md and move on: the button moved, the rule did not.")))


# ---------------------------------------------------------------- 18 checklist
def s_six():
    items = [(t("Бриф отмечает, что из заметок, а что придумано", "The brief marks what is from the notes and what is invented"), t("строка про эффект помечена", "the effect line is marked")),
             (t("В задаче есть числа и что не должно меняться", "The issue has numbers and what must not change"), "$75 · $100 · $18.00"),
             (t("Изменение маленькое", "The change is small"), t(f"+{N_LOGIC} строки логики", f"+{N_LOGIC} lines of logic")),
             (t("Тесты зелёные и проверяют границу", "Tests are green and check the boundary"), t(f"{N_TESTS} из {N_TESTS} · 75 и 74.99", f"{N_TESTS} of {N_TESTS} · 75 and 74.99")),
             (t("Ревью прочитано и на него ответили", "The review was read and answered"), t("1 комментарий Copilot", "1 Copilot comment")),
             (t("Доказательства сохранены", "Evidence is kept"), t("3 скриншота + checklist.md", "3 screenshots + checklist.md"))]
    rows = "".join(f'<div class="ck"><svg viewBox="0 0 44 44" width="44" height="44"><circle cx="22" cy="22" r="20" fill="var(--green)"/><path d="M12 23l7 7 13-15" fill="none" stroke="#0b0f17" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                   f'<span class="tx2">{a}</span><span class="vl">{b}</span></div>' for a, b in items)
    return dict(min=5, html=f'''
  {head(t("Приёмка", "Acceptance"), t("Шесть проверок одинаковы для любого Copilot", "Six checks are the same for any Copilot"),
        t("Это же рубрика домашнего задания. Справа результаты нашей недели.", "This is also the homework rubric. On the right are the results of our week."))}
  <div class="body" style="margin-top:14px;"><div class="cks">{rows}</div></div>''',
                notes=notes(
                    t("⏱ 5 мин. «Если хоть одной из этих проверок нет, вы не использовали Copilot, вы ему поверили.»", "⏱ 5 min. “If any of these is missing, you did not use Copilot, you trusted it.”"),
                    t("Шесть проверок работают для любого Copilot: в Word, в редакторе, на Windows. Пройдём по списку. Бриф отмечает источники. Задача с числами. Изменение маленькое. Тесты зелёные и проверяют границу. Ревью прочитано. Доказательства сохранены.",
                      "The six checks work for any Copilot: in Word, in the editor, on Windows. Let us go down the list. The brief marks its sources. The issue has numbers. The change is small. Tests are green and check the boundary. The review was read. The evidence is kept."),
                    t(f"В правом столбце результаты нашей недели: плюс {N_LOGIC} строки логики, {N_TESTS} из {N_TESTS} тестов, граница 75 и 74.99. Эти цифры взяты из настоящего запуска со слайда 11. Те же шесть проверок будут рубрикой домашнего задания.",
                      f"The right column shows our week’s results: plus {N_LOGIC} lines of logic, {N_TESTS} of {N_TESTS} tests, the 75 and 74.99 boundary. These numbers come from the real run on slide 11. The same six checks are the homework rubric.")))


# ---------------------------------------------------------------- 19 limits
def s_limits():
    person = '''<svg viewBox="0 0 380 440" class="fig" style="width:100%;height:auto">
    <circle cx="170" cy="190" r="150" fill="var(--cyan)" fill-opacity=".08" stroke="var(--cyan)" stroke-width="3" stroke-dasharray="10 8"/>
    <circle cx="170" cy="110" r="30" fill="none" stroke="var(--fg)" stroke-width="5"/>
    <path d="M108 210a62 62 0 0 1 124 0" fill="none" stroke="var(--fg)" stroke-width="5" stroke-linecap="round"/>
    <g transform="translate(222 160)" fill="none" stroke="var(--amber)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="16" r="14"/><path d="M28 24l66 50M70 60l12-12M82 72l12-12"/></g>
    <text x="170" y="388" text-anchor="middle" class="s23b" fill="var(--cyan)">COPILOT = </text>
    <text x="170" y="420" text-anchor="middle" class="s23b" fill="var(--cyan)">YOU, FASTER</text>
    </svg>'''.replace("COPILOT = ", t("Copilot = это", "Copilot is")).replace("YOU, FASTER", t("вы, но быстрее", "you, but faster"))
    traps = [("red", t("Не тот аккаунт", "Wrong account"), t("Вы вошли не туда, и Copilot видит не те файлы.", "You signed in to the wrong one, and Copilot sees the wrong files.")),
             ("amber", t("Секрет в чате", "A secret in the chat"), t("Пароль, ключ, данные клиента: ничего этого в запрос не вставляем.", "A password, a key, customer data: none of it goes into a request.")),
             ("violet", t("«Готово!»", "“Done!”"), t("Слово ничего не доказывает. Смотрите diff и тесты.", "The word proves nothing. Look at the diff and the tests."))]
    tr = "".join(f'<div class="trap" style="--k:var(--{c})"><div class="th">{h}</div><div class="td">{d}</div></div>' for c, h, d in traps)
    return dict(min=4, html=f'''
  {head(t("Границы", "Limits"), t("Copilot видит только то, что можете открыть вы", "Copilot sees only what you can open"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:.62fr 1.38fr;gap:40px;flex:none;align-items:center;">
      {person}
      <div class="stack" style="gap:16px;">{tr}
        <div class="plaque g"><b>{t("Обучение моделей:", "Model training:")}</b> {t("рабочие аккаунты (Microsoft 365, GitHub Business и Enterprise) не используются. Личный GitHub: с 24 апреля 2026 данные могут использоваться по умолчанию, выключается в настройках Copilot.",
                                                                                 "work accounts (Microsoft 365, GitHub Business and Enterprise) are not used. Personal GitHub: since 24 April 2026 your data may be used by default; switch it off in Copilot settings.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. «Copilot — не коллега с правами администратора. Это вы, только быстрее.»", "⏱ 4 min. “Copilot is not a colleague with admin rights. It is you, faster.”"),
                    t("Права Copilot равны вашим: что можете открыть вы, то он и увидит. Из этого три ловушки. Первая: вошли не в тот аккаунт. Вторая: вставили в чат пароль, ключ или данные клиента. Третья: поверили слову «готово».",
                      "Copilot’s permissions equal yours: what you can open, it can see. Three traps follow. First: you signed in to the wrong account. Second: you pasted a password, a key or customer data into the chat. Third: you believed the word “done”."),
                    t("Про данные. Рабочие аккаунты Microsoft 365 и GitHub Business и Enterprise не используются для обучения моделей. На личных планах GitHub с 24 апреля 2026 взаимодействия могут использоваться для обучения по умолчанию. Это отключается в настройках Copilot: «Allow GitHub to use my data for AI model training». Перед домашним заданием проверьте этот переключатель.",
                      "About data. Microsoft 365 work accounts and GitHub Business and Enterprise are not used to train models. On personal GitHub plans, since 24 April 2026 interactions may be used for training by default. You can turn it off in Copilot settings: “Allow GitHub to use my data for AI model training”. Check this switch before the homework.")))


# ---------------------------------------------------------------- 20 homework
def s_hw():
    tree = f'''courier-copilot-week/
├── brief.md
├── delivery_fee.py
├── test_delivery_fee.py
├── checklist.md
└── README.md   <span class="cm"># {t("3 скриншота", "3 screenshots")}</span>
<span class="cm">+ {t("ссылка на один принятый pull request", "+ a link to one merged pull request")}</span>'''
    bl = [t("<b>Фича:</b> правило Prime или своё, например «дождь: +$2 вне зоны».", "<b>Feature:</b> the Prime rule or your own, for example “rain: +$2 outside the zone”."),
          t("<b>Инструменты:</b> только бесплатные: GitHub Copilot Free в VS Code и Copilot Chat.", "<b>Tools:</b> free ones only: GitHub Copilot Free in VS Code and Copilot Chat."),
          t("<b>Сначала</b> выключите обучение на ваших данных в настройках GitHub.", "<b>First</b> switch off training on your data in GitHub settings."),
          t("<b>Оценка:</b> шесть проверок со слайда 18. Данные только придуманные.", "<b>Grading:</b> the six checks of slide 18. Synthetic data only.")]
    li = "".join(f"<li>{b}</li>" for b in bl)
    return dict(min=7, html=f'''
  {head(t("Практика", "Practice"), t("Домашнее задание: проведите свою фичу через три Copilot", "Homework: take your feature through three Copilots"))}
  <div class="body">
    <div class="row" style="grid-template-columns:.9fr 1.1fr;gap:56px;flex:none;align-items:center;">
      <div class="stack" style="gap:14px;"><div class="prompt-label">{t("Что сдать: публичный репозиторий на GitHub", "What to hand in: a public GitHub repository")}</div><div class="files">{tree}</div></div>
      <ul class="list big" style="--k:var(--cyan);">{li}</ul>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 7 мин. «Та же фича, ваш репозиторий, ваши скриншоты.»", "⏱ 7 min. “Same feature, your repo, your screenshots.”"),
                    t("Задание: публичный репозиторий courier-copilot-week. Внутри бриф, код, тесты, один принятый pull request, чек-лист и README с тремя скриншотами: бриф, Copilot в редакторе, pull request. Правило: ваше число и ваша граница, любое правило по вкусу.",
                      "The task: a public repository courier-copilot-week. Inside: a brief, the code, tests, one merged pull request, a checklist and a README with three screenshots: the brief, Copilot in the editor, the pull request. The rule: your number and your boundary, any rule you like."),
                    t("Инструменты: бесплатный GitHub Copilot Free в VS Code, плюс Copilot Chat в вебе, Edge или приложении Windows. Microsoft 365 по желанию. Ревью Copilot на pull request может быть платным, тогда достаточно комментария человека, на который вы ответили.",
                      "Tools: free GitHub Copilot Free in VS Code, plus Copilot Chat on the web, in Edge or in the Windows app. Microsoft 365 is optional. Copilot review on a pull request may be paid; then a human comment that you answered is enough."),
                    t("Критерии: шесть проверок со слайда 18. Перед началом выключите в личных настройках GitHub обучение на ваших данных. Никаких настоящих данных клиентов.",
                      "Criteria: the six checks of slide 18. Before you start, switch off training on your data in your personal GitHub settings. No real customer data.")))


# ---------------------------------------------------------------- 21 summary
def s_summary():
    rules = [("cyan", t("Сначала спросите: где лежит информация?", "First ask: where does the information live?")),
             ("green", t("Copilot видит только то, что открыто вам.", "Copilot sees only what is open to you.")),
             ("amber", t("Смотрите diff и тесты, а не слово «готово».", "Look at the diff and the tests, not at “done”.")),
             ("violet", t("Копите доказательства: скриншоты, чек-лист.", "Keep evidence: screenshots, a checklist.")),
             ("red", t("Секреты и данные клиентов в запрос не вставляем.", "No secrets or customer data in a request."))]
    rr = "".join(f'<div class="rule" style="--k:var(--{k})"><div class="n">{i + 1}</div><div class="t">{h}</div></div>' for i, (k, h) in enumerate(rules))
    return dict(min=3, html=f'''
  {head(t("Итоги", "Summary"), t("Итог: три места, одна привычка — проверять результат", "Summary: three places, one habit: check the result"))}
  <div class="body" style="margin-top:6px;">
    {strip(True)}
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:48px;align-items:center;flex:none;margin-top:26px;">
      <div class="rules" style="gap:20px">{rr}</div>
      <div class="next">
        <div class="kicker" style="--k:var(--amber)">{t("Дальше: урок 08", "Next: lesson 08")}</div>
        <div class="nh">{t("ИИ для анализа данных", "AI for data analysis")}</div>
        <div class="mini"><span>order_id</span><span>zone</span><span>is_prime</span><span>subtotal</span><span>1001</span><span>CITY</span><span>TRUE</span><span>82.40</span><span>1002</span><span>CITY</span><span>FALSE</span><span>76.00</span></div>
        <div class="nd">{t("Copilot открывает таблицу из слайда 7, и мы считаем по-настоящему.", "Copilot opens the table from slide 7 and we do real analysis.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. «На следующей неделе Copilot открывает таблицу, и мы делаем настоящий анализ.»", "⏱ 3 min. “Next week Copilot opens a spreadsheet and we do real analysis.”"),
                    t("Сверху наша неделя целиком: Teams, Word, issue, редактор, pull request, Windows. Пять правил. Спросите, где лежит информация. Copilot видит только то, что открыто вам. Смотрите diff и тесты. Копите доказательства. Не вставляйте секреты.",
                      "At the top is our whole week: Teams, Word, issue, editor, pull request, Windows. Five rules. Ask where the information lives. Copilot sees only what is open to you. Look at the diff and the tests. Keep evidence. Do not paste secrets."),
                    t("Следующий урок, L08: анализ данных с ИИ. Возьмём ту самую таблицу из слайда 7 и пройдём путь от вопроса до проверенного вывода. Вопросы.",
                      "Next lesson, L08: data analysis with AI. We take that table from slide 7 and go from a question to a checked conclusion. Questions.")))


SLIDES = [s_cover, s_week, s_three, s_model, s_teams, s_word, s_outlook_excel, s_money, s_issue, s_editor, s_result,
          s_pr, s_instr, s_doors, s_break, s_windows, s_notepad, s_six, s_limits, s_hw, s_summary]
MINUTES = [2, 4, 4, 4, 5, 5, 3, 4, 3, 6, 6, 5, 3, 3, 5, 6, 3, 5, 4, 7, 3]


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
        assert s["min"] == MINUTES[i - 1], (fn.__name__, s["min"])
        minutes += s["min"]
        cls = ("slide " + s.get("cls", "")).strip()
        foot = "" if s.get("cls", "").startswith("cover") else f'\n  <div class="foot"><span>{FOOT[lang]}</span><span>{i:02d} / {total}</span></div>'
        secs.append(f'<!-- SLIDE {i:02d} · {fn.__name__} · {s["min"]} min -->\n<section class="{cls}" data-n="{i}">{s["html"]}{foot}\n'
                    f'  <template class="notes">{s["notes"]}</template>\n</section>')
    assert minutes == 90, minutes
    assert total == 21 and SLIDES[14] is s_break and SLIDES[19] is s_hw
    title = t("Урок 07: Экосистема Copilot | GenAI Basics", "Lesson 07: The Copilot Ecosystem | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    page = f'''<!DOCTYPE html>
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
    OUT[lang].write_text(page, encoding="utf-8")
    print(f"{lang}: {OUT[lang].name}: {total} slides, {minutes} min")
    return OUT[lang]


CHROME = next((c for c in [shutil.which("msedge"), shutil.which("chromium"), shutil.which("google-chrome"),
                           *sorted(Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome")),
                           r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                           r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"] if c and Path(c).exists()), None)


def pdf(html):
    out = html.with_suffix(".pdf")
    prof = tempfile.mkdtemp(prefix="pdf_")
    extra = ["--no-sandbox"] if sys.platform.startswith("linux") else []
    subprocess.run([CHROME, "--headless", "--disable-gpu", *extra, "--no-pdf-header-footer", "--no-margins",
                    "--virtual-time-budget=10000", f"--user-data-dir={prof}", f"--print-to-pdf={out}", html.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    shutil.rmtree(prof, ignore_errors=True)
    print("pdf:", out.name, f"{out.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    for lg in ("ru", "en"):
        h = build(lg)
        if "--no-pdf" not in sys.argv:
            pdf(h)
