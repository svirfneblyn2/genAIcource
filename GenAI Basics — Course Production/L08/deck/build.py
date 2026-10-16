# -*- coding: utf-8 -*-
"""Build the L08 decks (RU + EN) and their PDFs.

    python build.py          # HTML + PDF for both languages
    python build.py --no-pdf # HTML only

Same engine as L05/deck_v2: every slide is one function, text is t("ru", "en").
All numbers and charts are computed from ../demo_assets/northstar_sales_messy.csv at build time,
so the slides always match what `reference_analysis.py` and the live demo produce.
Facts: ../L08_08_Source_Notes_Research_2026-10.md. No-code experiment: ../demo_assets/no_code_experiment_2026-10-13.md.
"""
import csv
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
L08 = HERE.parent
NAME = "presentation_L08_AI_for_Data_Analysis"
OUT = {"ru": L08 / f"{NAME}.html", "en": L08 / f"{NAME}_EN.html"}
IMG = "assets/"

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 08 • ИИ для анализа данных", "en": "GenAI Basics • Lesson 08 • AI for Data Analysis"}

# ---------------------------------------------------------------- data (computed, not typed)
RAW = list(csv.DictReader((L08 / "demo_assets" / "northstar_sales_messy.csv").open(encoding="utf-8")))
TRUTH = {r["order_id"]: r for r in csv.DictReader((L08 / "demo_assets" / "northstar_sales_truth.csv").open(encoding="utf-8"))}
_seen, CLEAN = set(), []
for _r in RAW:
    if _r["order_id"] in _seen:
        continue
    _seen.add(_r["order_id"])
    _c = dict(_r)
    _c["region"] = _c["region"].strip() or "UNKNOWN"
    _c["date"] = _c["date"].replace("/", "-")
    CLEAN.append(_c)
MONTHS = sorted({r["date"][:7] for r in CLEAN})
CHANNELS = ["Search", "Social", "Email", "Organic"]
MONTHLY = {m: sum(float(r["revenue"]) for r in CLEAN if r["date"][:7] == m) for m in MONTHS}
BY_CH = {c: sum(float(r["revenue"]) for r in CLEAN if r["channel"] == c) for c in CHANNELS}
SPEND = {c: sum(float(r["ad_spend"]) for r in CLEAN if r["channel"] == c) for c in CHANNELS}
CH_M = defaultdict(float)
for _r in CLEAN:
    CH_M[(_r["channel"], _r["date"][:7])] += float(_r["revenue"])
TOTAL = sum(float(r["revenue"]) for r in CLEAN)
TOTAL_RAW = sum(float(r["revenue"]) for r in RAW)
DUP_ID = next(r["order_id"] for i, r in enumerate(RAW) if r["order_id"] in {x["order_id"] for x in RAW[:i]})
MISS_ID = next(r["order_id"] for r in RAW if not r["region"].strip())
DATE_ID = next(r["order_id"] for r in RAW if "/" in r["date"])
BAD_ID = next(r["order_id"] for r in RAW if int(r["returns"]) > int(r["orders"]))
ROW = {r["order_id"]: r for r in RAW}
assert abs(sum(MONTHLY.values()) - TOTAL) < 1e-6 and abs(sum(BY_CH.values()) - TOTAL) < 1e-6
GROWTH = (MONTHLY[MONTHS[-1]] / MONTHLY[MONTHS[0]] - 1) * 100
CH_GROWTH = {c: (CH_M[(c, MONTHS[-1])] / CH_M[(c, MONTHS[0])] - 1) * 100 for c in CHANNELS}
ROAS = {c: BY_CH[c] / SPEND[c] for c in CHANNELS if SPEND[c] > 0}
MNAME = {"ru": ["янв", "фев", "мар", "апр", "май", "июн"], "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]}


def money(x, dec=0):
    s = f"{x:,.{dec}f}"
    return "$" + (s.replace(",", "\u202f") if LANG == "ru" else s)


def dec(x, n=1):
    return f"{x:.{n}f}".replace(".", "," if LANG == "ru" else ".")


def k(x):
    return dec(x / 1000) + t("\u00a0тыс.", "k")


def pct(x):
    s = f"{x:+.0f}" + t("\u00a0%", "%")
    return s.replace("-", "−")


# ---------------------------------------------------------------- helpers
def head(kicker, title, lead=None, k=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    s = f'<div class="kicker"{ks}>{kicker}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


ARROW = ('<defs><marker id="{id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0 0 L10 5 L0 10 Z" fill="{c}"/></marker></defs>')

# thin outline icons (stroke = currentColor), 48x48 box
ICON = {
    "person": '<circle cx="24" cy="15" r="8"/><path d="M8 42 c2-10 9-15 16-15 s14 5 16 15"/>',
    "chat": '<path d="M7 10 h34 a3 3 0 0 1 3 3 v18 a3 3 0 0 1 -3 3 H20 l-8 7 v-7 H7 a3 3 0 0 1 -3 -3 V13 a3 3 0 0 1 3 -3 z"/><path d="M13 19 h22 M13 25 h14"/>',
    "term": '<rect x="4" y="8" width="40" height="32" rx="4"/><path d="M11 18 l7 6 l-7 6 M22 31 h12"/>',
    "file": '<path d="M11 4 h18 l10 10 v30 H11 z M29 4 v10 h10"/><path d="M17 36 v-6 M23 36 v-11 M29 36 v-8"/>',
    "check": '<circle cx="24" cy="24" r="19"/><path d="M15 24 l6 6 l12 -13"/>',
    "grid": '<rect x="5" y="7" width="38" height="34" rx="3"/><path d="M5 18 h38 M5 29 h38 M18 7 v34 M31 7 v34"/>',
    "nb": '<rect x="8" y="4" width="32" height="40" rx="3"/><path d="M14 13 h20 M14 21 h12 M14 30 l4 3 l-4 3 M21 36 h10"/>',
    "api": '<path d="M16 14 l-10 10 l10 10 M32 14 l10 10 l-10 10 M27 9 l-6 30"/>',
}


def icon(name, size=48, color="var(--cyan)", extra=""):
    return (f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" {extra}>{ICON[name]}</svg>')


def gicon(name, x, y, size, color):
    s = size / 48
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" stroke-width="{2 / s * 1.3:.2f}" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</g>')


def row_cells(r, bad=()):
    cols = ["order_id", "date", "channel", "category", "region", "orders", "revenue", "ad_spend", "returns"]
    out = []
    for c in cols:
        v = r[c] if r[c] != "" else t("(пусто)", "(empty)")
        cls = ["num"] if c in ("orders", "revenue", "ad_spend", "returns") else []
        if c in bad:
            cls.append("bad")
        if r[c] == "":
            cls.append("dim" if c not in bad else "")
        out.append(f'<td class="{" ".join(x for x in cls if x)}">{v}</td>')
    return "".join(out)


TH = ('<tr><th>order_id</th><th>date</th><th>channel</th><th>category</th><th>region</th>'
      '<th class="num">orders</th><th class="num">revenue</th><th class="num">ad_spend</th><th class="num">returns</th></tr>')


# ---------------------------------------------------------------- charts (static SVG from the data)
def line_chart(w=700, h=400):
    pad_l, pad_r, pad_t, pad_b = 84, 30, 40, 50
    lo, hi = 0, 60000
    xs = [pad_l + i * (w - pad_l - pad_r) / (len(MONTHS) - 1) for i in range(len(MONTHS))]
    ys = [pad_t + (1 - (MONTHLY[m] - lo) / (hi - lo)) * (h - pad_t - pad_b) for m in MONTHS]
    grid = ""
    for v in (0, 20000, 40000, 60000):
        y = pad_t + (1 - (v - lo) / (hi - lo)) * (h - pad_t - pad_b)
        grid += (f'<line x1="{pad_l}" y1="{y:.1f}" x2="{w - pad_r}" y2="{y:.1f}" stroke="#2b3648" stroke-width="1"/>'
                 f'<text x="{pad_l - 12}" y="{y + 6:.1f}" text-anchor="end" font-size="17" fill="#6b7a90">{v // 1000}{t(" тыс.", "k")}</text>')
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    labels = "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#0b0f17" stroke="#38bdf8" stroke-width="3"/>'
        f'<text x="{x:.1f}" y="{y - 16:.1f}" text-anchor="middle" font-size="19" font-weight="700" fill="#f1f5f9">{dec(MONTHLY[m] / 1000)}</text>'
        f'<text x="{x:.1f}" y="{h - pad_b + 30}" text-anchor="middle" font-size="18" fill="#a3b1c4">{MNAME[LANG][i]}</text>'
        for i, (x, y, m) in enumerate(zip(xs, ys, MONTHS)))
    return (f'<svg class="dia" viewBox="0 0 {w} {h}">{grid}<polyline points="{pts}" fill="none" stroke="#38bdf8" stroke-width="4"/>'
            f'{labels}</svg>')


def slope_chart(w=640, h=400):
    pad_t, pad_b, x0, x1 = 30, 50, 150, 400
    lo, hi = 6000, 14500
    def y(v):
        return pad_t + (1 - (v - lo) / (hi - lo)) * (h - pad_t - pad_b)
    col = {"Search": "#fbbf24", "Social": "#5f6e84", "Email": "#5f6e84", "Organic": "#5f6e84"}
    out = (f'<line x1="{x0}" y1="{pad_t - 10}" x2="{x0}" y2="{h - pad_b}" stroke="#2b3648" stroke-width="2"/>'
           f'<line x1="{x1}" y1="{pad_t - 10}" x2="{x1}" y2="{h - pad_b}" stroke="#2b3648" stroke-width="2"/>'
           f'<text x="{x0}" y="{h - pad_b + 32}" text-anchor="middle" font-size="18" fill="#a3b1c4">{MNAME[LANG][0]}</text>'
           f'<text x="{x1}" y="{h - pad_b + 32}" text-anchor="middle" font-size="18" fill="#a3b1c4">{MNAME[LANG][-1]}</text>')
    # label positions: spread end labels so they do not collide
    ends = sorted(CHANNELS, key=lambda c: -CH_M[(c, MONTHS[-1])])
    end_y = {}
    last = -99
    for c in ends:
        yy = max(y(CH_M[(c, MONTHS[-1])]) - 30, last + 28)
        end_y[c] = yy
        last = yy
    starts = sorted(CHANNELS, key=lambda c: -CH_M[(c, MONTHS[0])])
    st_y, last = {}, -99
    for c in starts:
        yy = max(y(CH_M[(c, MONTHS[0])]), last + 26)
        st_y[c] = yy
        last = yy
    for c in sorted(CHANNELS, key=lambda c: c == "Search"):
        a, b = CH_M[(c, MONTHS[0])], CH_M[(c, MONTHS[-1])]
        hl = c == "Search"
        sw = 5 if hl else 3
        out += (f'<line x1="{x0}" y1="{y(a):.1f}" x2="{x1}" y2="{y(b):.1f}" stroke="{col[c]}" stroke-width="{sw}"/>'
                f'<circle cx="{x0}" cy="{y(a):.1f}" r="6" fill="{col[c]}"/><circle cx="{x1}" cy="{y(b):.1f}" r="6" fill="{col[c]}"/>'
                f'<text x="{x0 - 14}" y="{st_y[c] + 6:.1f}" text-anchor="end" font-size="18" fill="{"#fbbf24" if hl else "#a3b1c4"}" font-weight="{700 if hl else 400}">{c} {dec(a / 1000)}</text>'
                f'<text x="{x1 + 14}" y="{end_y[c] + 6:.1f}" font-size="18" fill="{"#fbbf24" if hl else "#a3b1c4"}" font-weight="{700 if hl else 400}">{c} {dec(b / 1000)} '
                f'<tspan font-weight="700">{pct(CH_GROWTH[c])}</tspan></text>')
    return f'<svg class="dia" viewBox="0 0 {w} {h}">{out}</svg>'


def mini(kind):
    c, d, g = "#38bdf8", "#5f6e84", "#2b3648"
    base = f'<line x1="20" y1="140" x2="230" y2="140" stroke="{g}" stroke-width="2"/>'
    if kind == "line":
        b = base + f'<polyline points="30,118 70,108 110,96 150,82 190,64 222,44" fill="none" stroke="{c}" stroke-width="4"/>'
    elif kind == "bar":
        b = base + "".join(f'<rect x="{30 + i * 50}" y="{140 - v}" width="34" height="{v}" rx="3" fill="{c if i == 0 else d}"/>'
                           for i, v in enumerate([104, 86, 64, 40]))
    elif kind == "hist":
        b = base + "".join(f'<rect x="{26 + i * 26}" y="{140 - v}" width="24" height="{v}" fill="{c}"/>'
                           for i, v in enumerate([14, 36, 70, 98, 84, 52, 26, 10]))
    elif kind == "scatter":
        import random
        rnd = random.Random(4)
        pts = [(30 + i * 10 + rnd.randint(-6, 6), 128 - i * 4.6 + rnd.randint(-18, 18)) for i in range(20)]
        b = base + f'<line x1="20" y1="20" x2="20" y2="140" stroke="{g}" stroke-width="2"/>' + "".join(
            f'<circle cx="{x}" cy="{y:.0f}" r="5" fill="{c}"/>' for x, y in pts)
    else:  # stacked 100%
        cols = ["#38bdf8", "#34d399", "#fbbf24", "#c084fc"]
        shares = [[30, 25, 25, 20], [28, 24, 26, 22], [26, 24, 26, 24], [24, 24, 27, 25]]
        b = base
        for i, sh in enumerate(shares):
            yy = 140
            for j, s in enumerate(sh):
                hh = s * 1.15
                yy -= hh
                b += f'<rect x="{34 + i * 50}" y="{yy:.1f}" width="34" height="{hh:.1f}" fill="{cols[j]}" opacity=".85"/>'
    return f'<svg viewBox="0 0 250 160" preserveAspectRatio="xMidYMid meet">{b}</svg>'


# ---------------------------------------------------------------- slides
def s_cover():
    return dict(min=2, cls="cover", html=f'''
  <div class="bg"><img class="full" src="{IMG}l08_cover_hero.png" alt=""></div>
  <div class="shade soft"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 08 • Модуль 3: ИИ-ассистенты в работе", "GenAI Basics • Lesson 08 • Module 3: AI assistants at work")}</div>
    <h1>{t("ИИ для анализа данных", "AI for Data Analysis")}</h1>
    <h2>{t("Чат с таблицей: модель пишет код, песочница считает, вы проверяете", "Chat with a spreadsheet: the model writes code, a sandbox calculates, you check")}</h2>
    <p>{t("Как ChatGPT, Claude, Gemini и Copilot анализируют файлы, где они ошибаются и как получить ответ, которому можно верить. Учебный кейс — продажи интернет-магазина Northstar за январь–июнь 2026.",
           "How ChatGPT, Claude, Gemini and Copilot analyse files, where they go wrong and how to get an answer you can trust. Case study: Northstar online shop sales, January–June 2026.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Приветствие. Сегодня — анализ данных с помощью ИИ: загружаем таблицу в чат и задаём вопросы обычным языком.",
                      "⏱ 2 min. Welcome. Today: data analysis with AI — we upload a spreadsheet to a chat and ask questions in plain language."),
                    t("Главная мысль урока на одной строке: модель пишет код и объясняет, считает песочница (изолированный Python), а проверяете — вы. Весь урок на одном учебном файле: продажи магазина Northstar.",
                      "The lesson in one line: the model writes code and explains, a sandbox (isolated Python) calculates, and you check. The whole lesson uses one practice file: Northstar shop sales.")))


def s_hook():
    bad = ROW[BAD_ID]
    return dict(min=5, html=f'''
  {head(t("Эксперимент • 13.10.2026", "Experiment • 13 Oct 2026"), t("Модель посчитала без кода — и посчитала верно. Почему этого мало?", "The model did the maths without code — and got it right. Why is that not enough?"), k="amber")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.05fr 1fr;gap:48px;align-items:center;">
      <div class="chat">
        <div class="msg u"><div class="who">{t("Вопрос", "Question")}</div>{t("Вот продажи за январь–июнь (73 строки CSV прямо в сообщении). Какая общая выручка? Есть ли проблемы в данных?", "Here are sales for January–June (73 CSV rows pasted into the message). What is total revenue? Any data problems?")}</div>
        <div class="msg a"><div class="who">{t("Claude Haiku 5.5 • без инструментов", "Claude Haiku 5.5 • no tools")}</div>
          {t(f"Общая выручка — <mark class='g'>256 045</mark> (дубль строки {DUP_ID} исключён)…<br>Заказ {BAD_ID}: возвратов {bad['returns']} при {bad['orders']} заказах — <mark>вероятно, опечатка, должно быть 6</mark>.<br><mark>Я проверил расчёт: суммы сходятся.</mark>",
             f"Total revenue is <mark class='g'>256,045</mark> (duplicate row {DUP_ID} excluded)…<br>Order {BAD_ID}: {bad['returns']} returns on {bad['orders']} orders — <mark>probably a typo, should be 6</mark>.<br><mark>I checked the work: the totals match.</mark>")}
        </div>
      </div>
      <div class="verd">
        <div class="vd" style="--k:var(--green)"><div class="ic">✓</div><div><div class="h">{t("Сумма верная", "The total is right")}</div><div class="d">{t("На 73 строках современные модели считают в уме неплохо. Sonnet 5.5 дал ту же сумму.", "On 73 rows modern models do mental maths well. Sonnet 5.5 gave the same total.")}</div></div></div>
        <div class="vd" style="--k:var(--red)"><div class="ic">✗</div><div><div class="h">{t(f"«Вероятно, 6» — в источнике было {TRUTH[BAD_ID]['returns']}", f"“Probably 6” — the source said {TRUTH[BAD_ID]['returns']}")}</div><div class="d">{t("Догадка звучит как факт. Исправлять данные «на глаз» нельзя.", "A guess sounds like a fact. Data must not be fixed by guessing.")}</div></div></div>
        <div class="vd" style="--k:var(--red)"><div class="ic">✗</div><div><div class="h">{t("«Я проверил» — а чем?", "“I checked” — with what?")}</div><div class="d">{t("Ни одного запуска кода. Ход расчёта не виден, повторить его нельзя.", "Not a single code run. You cannot see the working or repeat it.")}</div></div></div>
        <div class="vd" style="--k:var(--amber)"><div class="ic">!</div><div><div class="h">{t("100 000 строк в сообщение не влезут", "100,000 rows will not fit in a message")}</div><div class="d">{t("Реальные таблицы — это <b>файл + код</b>, а не текст в чате.", "Real tables mean <b>a file + code</b>, not text in a chat.")}</div></div></div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Это настоящий эксперимент, сделанный при подготовке урока 13.10.2026. Мы вставили весь учебный CSV (73 строки) прямо в сообщение и запретили модели пользоваться инструментами. Две модели — Claude Haiku 5.5 и Sonnet 5.5 — посчитали общую выручку правильно: 256 045 долларов, и правильно нашли самый быстрорастущий канал. Sonnet при этом честно оговорился: «считал вручную, перепроверьте».",
                      "⏱ 5 min. This is a real experiment run while preparing the lesson on 13 Oct 2026. We pasted the whole practice CSV (73 rows) into a message and did not allow any tools. Two models — Claude Haiku 5.5 and Sonnet 5.5 — got total revenue right ($256,045) and correctly found the fastest-growing channel. Sonnet did add an honest caveat: “computed by hand, please double-check”."),
                    t(f"Так что «модели не умеют считать» — устаревший аргумент. Проблемы в другом. Первое: в строке {BAD_ID} возвратов 66 при 62 заказах — это невозможно. Модель сама «починила»: «вероятно, 6». В исходной системе было {TRUTH[BAD_ID]['returns']}. Второе: «я проверил» — но кода не было, проверить ход расчёта нельзя. Третье: 73 строки помещаются в сообщение, реальная выгрузка на 100 тысяч строк — нет.",
                      f"So “models can’t do maths” is an outdated argument. The problems are elsewhere. First: row {BAD_ID} has 66 returns on 62 orders — impossible. The model “fixed” it itself: “probably 6”. The source system said {TRUTH[BAD_ID]['returns']}. Second: “I checked” — but there was no code, so you cannot inspect the working. Third: 73 rows fit in a message; a real 100,000-row export does not."),
                    t("Вопрос в чат: «Что бы вы сделали со строкой, где возвратов больше, чем заказов?» Соберите 2–3 ответа и переходите к схеме.",
                      "Ask the chat: “What would you do with a row that has more returns than orders?” Collect 2–3 answers and move on to the diagram."),
                    t("Если повторяете эксперимент вживую — ответ может отличаться: модели и запуски разные. Показывайте то, что получилось. Подробности: demo_assets/no_code_experiment_2026-10-13.md.",
                      "If you repeat the experiment live, the answer may differ: models and runs vary. Show whatever you get. Details: demo_assets/no_code_experiment_2026-10-13.md.")))


def s_loop():
    blue, green, amber, grey, fg, mut = "#38bdf8", "#34d399", "#fbbf24", "#5f6e84", "#f1f5f9", "#a3b1c4"
    def node(x, y, w, h, ic, col, title, sub):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#0f1624" stroke="{col}" stroke-width="2"/>'
                + gicon(ic, x + 22, y + 24, 54, col)
                + f'<text x="{x + 94}" y="{y + 52}" font-size="27" font-weight="700" fill="{fg}">{title}</text>'
                + "".join(f'<text x="{x + 94}" y="{y + 84 + i * 26}" font-size="19" fill="{mut}">{s}</text>' for i, s in enumerate(sub)))
    def lab(x, y, s, col=mut, anchor="middle", size=19, weight=600):
        return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{col}">{s}</text>'
    svg = (f'<svg class="dia" viewBox="0 0 1450 520">' + ARROW.format(id="la", c=grey) + ARROW.format(id="lb", c=blue) + ARROW.format(id="lg", c=green)
           + node(0, 175, 300, 150, "person", fg, t("Вы", "You"), [t("вопрос + файл", "question + file"), "CSV / XLSX"])
           + node(470, 20, 420, 160, "chat", blue, t("Языковая модель", "Language model"), [t("понимает вопрос", "understands the question"), t("пишет код · объясняет", "writes code · explains")])
           + node(470, 330, 420, 160, "term", green, t("Песочница Python", "Python sandbox"), [t("читает файл · считает", "reads the file · calculates"), t("рисует графики", "draws charts")])
           + node(1080, 330, 370, 160, "file", amber, t("Файлы-результаты", "Output files"), [t("таблица · график", "table · chart"), t("можно скачать", "downloadable")])
           # you -> model
           + f'<path d="M300 220 C 380 200, 400 120, 466 110" stroke="{grey}" stroke-width="3" fill="none" marker-end="url(#la)"/>'
           + lab(350, 160, t("вопрос", "question"))
           # model -> sandbox (code)
           + f'<path d="M620 182 L620 326" stroke="{blue}" stroke-width="3" fill="none" marker-end="url(#lb)"/>'
           + lab(606, 262, t("код", "code"), blue, "end")
           # sandbox -> model (result)
           + f'<path d="M740 328 L740 184" stroke="{green}" stroke-width="3" fill="none" marker-end="url(#lg)"/>'
           + lab(756, 250, t("результат", "result"), green, "start") + lab(756, 276, t("или ошибка", "or error"), green, "start", 17, 400)
           + f'<path d="M900 300 a 30 30 0 1 0 -2 -60" stroke="{grey}" stroke-width="2.5" fill="none" stroke-dasharray="6 6" marker-end="url(#la)"/>'
           + lab(948, 236, t("правит и", "fixes and"), mut, "start", 18, 400) + lab(948, 258, t("запускает снова", "reruns"), mut, "start", 18, 400)
           # sandbox -> files
           + f'<path d="M890 410 L1076 410" stroke="{amber}" stroke-width="3" fill="none" marker-end="url(#la)"/>'
           # model -> you (answer)
           + f'<path d="M466 150 C 360 175, 330 300, 300 290" stroke="{grey}" stroke-width="3" fill="none" marker-end="url(#la)"/>'
           + lab(392, 262, t("ответ + код", "answer + code"))
           + '</svg>')
    return dict(min=6, html=f'''
  {head(t("Как это устроено", "How it works"), t("Модель — не калькулятор. Считает песочница", "The model is not the calculator. The sandbox is"))}
  <div class="body" style="margin-top:6px;">
    <div class="stack" style="gap:26px;">
      {svg}
      <div class="row" style="grid-template-columns:repeat(3,1fr);gap:30px;flex:none;">
        <div class="note" style="--k:var(--cyan)"><b>{t("Модель", "The model")}</b> {t("решает, <b>что</b> посчитать, и пишет код.", "decides <b>what</b> to calculate and writes the code.")}</div>
        <div class="note" style="--k:var(--green)"><b>{t("Песочница", "The sandbox")}</b> {t("выполняет код и <b>считает</b> точно.", "runs the code and <b>calculates</b> exactly.")}</div>
        <div class="note" style="--k:var(--fg)"><b>{t("Вы", "You")}</b> {t("смотрите код и <b>проверяете</b> вывод.", "look at the code and <b>check</b> the conclusion.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Как устроен «чат с данными» в ChatGPT, Claude, Gemini. Вы загружаете файл и задаёте вопрос. Модель не считает в уме: она пишет небольшую программу на Python. Программа выполняется в песочнице — изолированном компьютере у провайдера, где лежит ваш файл. Результат (или ошибка) возвращается модели; если ошибка, модель правит код и запускает снова. В конце вы получаете ответ, код и файлы: таблицу, график.",
                      "⏱ 6 min. How “chat with data” works in ChatGPT, Claude and Gemini. You upload a file and ask a question. The model does not do the maths in its head: it writes a small Python program. The program runs in a sandbox — an isolated computer at the provider where your file lives. The result (or an error) goes back to the model; on an error, the model fixes the code and reruns it. At the end you get an answer, the code and files: a table, a chart."),
                    t("Почему это важно: числа посчитаны программой — значит, их можно перепроверить, повторить, отдать коллеге. В ChatGPT код открывается кнопкой рядом с ответом, в Claude — блоком анализа, в Gemini — «показать код». Привычка: всегда раскрывайте код хотя бы глазами.",
                      "Why it matters: the numbers come from a program, so they can be rechecked, repeated and shared with a colleague. In ChatGPT the code opens with a button next to the answer, in Claude in the analysis block, in Gemini via “show code”. Habit: always open the code, even just to glance at it.")))


def s_where():
    cols = [
        ("chat", "green", t("Чат с файлом", "Chat with a file"), t("загрузили CSV/XLSX — спросили", "upload CSV/XLSX — ask"),
         [("ChatGPT", t("анализ данных на Python · таблицы до ~50 МБ", "data analysis in Python · sheets up to ~50 MB")),
          ("Claude", t("код и создание файлов · все тарифы · до 30 МБ", "code execution & files · all plans · up to 30 MB")),
          ("Gemini", t("приложение · файлы до 100 МБ", "app · files up to 100 MB"))]),
        ("grid", "cyan", t("Прямо в таблице", "Inside the spreadsheet"), t("панель ИИ рядом с вашими данными", "an AI panel next to your data"),
         [("Copilot " + t("в Excel", "in Excel"), t("«Edit with Copilot», умеет Python", "“Edit with Copilot”, runs Python")),
          (t("ChatGPT и Claude для Excel", "ChatGPT and Claude for Excel"), t("панели в книге; Claude — платные тарифы", "panels in the workbook; Claude — paid plans")),
          ("Gemini " + t("в Google Таблицах", "in Google Sheets"), t("боковая панель: анализ и графики; =AI() — только текст", "side panel: analysis and charts; =AI() — text only"))]),
        ("nb", "violet", t("Ноутбук", "Notebook"), t("код виден и остаётся у вас", "code is visible and stays with you"),
         [("Google Colab + Gemini", t("ассистент пишет и запускает ячейки", "assistant writes and runs cells")),
          ("Jupyter", t("локально или в облаке", "local or cloud"))]),
        ("api", "pink", "API", t("для автоматизации", "for automation"),
         [("OpenAI Code Interpreter", t("код в изолированном контейнере", "code in an isolated container")),
          ("Gemini API", t("code execution · до 30 с на запуск", "code execution · up to 30 s per run")),
          ("Claude API", "code execution")]),
    ]
    html = ""
    for ic, kk, h, sub, prods in cols:
        pr = "".join(f'<span>{n}<small>{d}</small></span>' for n, d in prods)
        html += (f'<div class="tm" style="--k:var(--{kk})">{icon(ic, 64, f"var(--{kk})")}<div class="h">{h}<small>{sub}</small></div>'
                 f'<div class="pr">{pr}</div></div>')
    return dict(min=6, html=f'''
  {head(t("Где это есть • октябрь 2026", "Where to find it • October 2026"), t("Четыре места, где ИИ анализирует данные", "Four places where AI analyses data"))}
  <div class="body">
    <div class="tmap">{html}</div>
    <div class="axis"><div class="ln"></div><div class="hd"></div><span class="l">{t("проще начать", "easier to start")}</span><span class="r">{t("больше контроля и повторяемости", "more control and repeatability")}</span></div>
    <div class="cap" style="margin-top:40px;">{t("Механика везде одна: модель пишет код → он выполняется → вы проверяете. Названия кнопок и лимиты меняются — сверяйтесь с документацией в день занятия.", "The mechanics are the same everywhere: the model writes code → it runs → you check. Button names and limits change — check the docs on the day of class.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Слева направо — от «проще начать» к «больше контроля». Чат с файлом — самый быстрый старт: перетащили CSV, задали вопрос. Прямо в таблице — Copilot в Excel и Gemini в Google Таблицах: удобно, если данные и так живут в таблице и их нельзя выносить. Ноутбук — Colab или Jupyter: код остаётся у вас, его можно перезапустить через месяц. API — когда анализ надо повторять автоматически, например каждую неделю.",
                      "⏱ 6 min. Left to right — from “easier to start” to “more control”. Chat with a file is the fastest start: drop in a CSV, ask. Inside the spreadsheet — Copilot in Excel and Gemini in Google Sheets: handy when the data already lives in a spreadsheet and must not leave it. Notebook — Colab or Jupyter: the code stays with you and can be rerun a month later. API — when the analysis must repeat automatically, e.g. weekly."),
                    t("Сегодня в демо — чат с файлом. Принципы, которые разберём дальше, одинаковы для всех четырёх мест.",
                      "Today’s demo uses chat with a file. The principles we cover next are the same for all four."),
                    t("Свежие изменения, о которых спросят: функцию =COPILOT() в Excel убрали 14.09.2026 (старые формулы дают #NAME?) — теперь это Copilot-панель «Edit with Copilot». ChatGPT for Excel/Google Sheets доступен на всех тарифах с 05.05.2026. Claude for Google Workspace — бета с 06.10.2026. Источники: L08_08_Source_Notes_Research_2026-10.md.",
                      "Recent changes people will ask about: the =COPILOT() function in Excel was retired on 14 Sep 2026 (old formulas show #NAME?) — it is now the Copilot panel “Edit with Copilot”. ChatGPT for Excel/Google Sheets is on all plans since 5 May 2026. Claude for Google Workspace is in beta since 6 Oct 2026. Sources: L08_08_Source_Notes_Research_2026-10.md.")))


def s_data():
    rows = [ROW[i] for i in ("1001", "1002", "1003", "1004", "1005")]
    body = "".join(f"<tr>{row_cells(r)}</tr>" for r in rows)
    th = ('<tr><th class="k" style="--k:var(--amber)">order_id</th><th class="k" style="--k:var(--cyan)">date</th>'
          '<th class="k" style="--k:var(--violet)">channel</th><th class="k" style="--k:var(--violet)">category</th><th class="k" style="--k:var(--violet)">region</th>'
          '<th class="num k" style="--k:var(--green)">orders</th><th class="num k" style="--k:var(--green)">revenue</th><th class="num k" style="--k:var(--green)">ad_spend</th><th class="num k" style="--k:var(--green)">returns</th></tr>')
    cn = [("amber", t("Ключ", "Key"), t("order_id должен быть уникален", "order_id must be unique")),
          ("cyan", t("Время", "Time"), t("один формат даты, январь–июнь", "one date format, January–June")),
          ("violet", t("Разрезы", "Dimensions"), t("канал · категория · регион", "channel · category · region")),
          ("green", t("Числа и единицы", "Numbers and units"), t("$ и штуки; возвратов ≤ заказов", "$ and counts; returns ≤ orders"))]
    cnh = "".join(f'<div class="cn" style="--k:var(--{c})"><b>{h}</b>{d}</div>' for c, h, d in cn)
    return dict(min=5, html=f'''
  {head(t("Учебный файл • northstar_sales_messy.csv", "Practice file • northstar_sales_messy.csv"), t("Сначала паспорт данных, потом вопросы", "First the data passport, then the questions"))}
  <div class="body" style="margin-top:18px;">
    <div class="colnotes" style="grid-template-columns:repeat(4,1fr);">{cnh}</div>
    <table class="tbl big" style="margin-top:10px;">{th}{body}<tr><td class="dim" colspan="9">… {t(f"ещё {len(RAW) - 5} строк", f"{len(RAW) - 5} more rows")}</td></tr></table>
    <div class="plaque" style="margin-top:22px;">{t("<b>Одна строка</b> — продажи одного канала в одной категории за одну дату. Это <b>не заказ и не клиент</b>: если перепутать, все «средние на клиента» будут неверны.", "<b>One row</b> is the sales of one channel in one category on one date. It is <b>not an order and not a customer</b>: mix this up and every “average per customer” is wrong.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Прежде чем спрашивать «какие инсайты?», выясняем, что вообще лежит в файле. Это паспорт данных: что такое одна строка, какое поле должно быть уникальным, за какой период данные, в каких единицах числа и какие значения невозможны.",
                      "⏱ 5 min. Before asking “what are the insights?”, find out what is actually in the file. This is the data passport: what one row is, which field must be unique, what period the data covers, which units the numbers use and which values are impossible."),
                    t("Пройдите по цветам. Жёлтый — ключ order_id. Голубой — дата. Фиолетовый — разрезы, по которым группируем. Зелёный — числа: выручка и рекламный бюджет в долларах, заказы и возвраты в штуках. Правило здравого смысла: возвратов не может быть больше, чем заказов.",
                      "Walk through the colours. Amber — the order_id key. Blue — the date. Violet — the dimensions we group by. Green — numbers: revenue and ad spend in dollars, orders and returns as counts. Common-sense rule: returns cannot exceed orders."),
                    t("Важная оговорка: несмотря на название order_id, одна строка — это агрегат, а не один заказ. В колонке orders, например, 36 заказов. Попросите модель первым делом описать «что такое одна строка» — это ловит половину ошибок.",
                      "Important: despite the name order_id, one row is an aggregate, not one order. The orders column holds e.g. 36 orders. Ask the model first to describe “what one row is” — that catches half the mistakes.")))


def s_profile():
    trs = []
    for oid, bad, tag in [(MISS_ID, ("region",), t("пустой регион", "empty region")),
                          (DUP_ID, ("order_id",), t("дубль", "duplicate")),
                          (DUP_ID, ("order_id",), ""),
                          (DATE_ID, ("date",), t("другой формат даты", "different date format")),
                          (BAD_ID, ("orders", "returns"), t("возвратов > заказов", "returns > orders"))]:
        r = ROW[oid]
        trs.append(f'<tr class="{"dup" if oid == DUP_ID else ""}">{row_cells(r, bad)}<td class="tag">{tag}</td></tr>')
    th = TH.replace("</tr>", "<th></th></tr>")
    stats = [(str(len(RAW)), t("строк в файле", "rows in the file"), "fg"),
             (str(len({r["order_id"] for r in RAW})), t("уникальных order_id", "unique order_ids"), "amber"),
             ("4", t("проблемы спрятаны среди 73 строк", "problems hidden among 73 rows"), "red")]
    st = "".join(f'<div class="stat" style="--k:var(--{c})"><div class="n">{n}</div><div class="d">{d}</div></div>' for n, d, c in stats)
    return dict(min=5, html=f'''
  {head(t("Шаг 1 • профиль", "Step 1 • profile"), t("Профиль данных — до любых выводов", "Profile the data before any conclusions"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:250px 1fr;gap:40px;align-items:center;">
      <div class="stack" style="gap:26px;">{st}</div>
      <div class="stack" style="gap:18px;">
        <div><div class="prompt-label">{t("Промпт", "Prompt")}</div><div class="prompt" style="font-size:19px;">{t("Опиши этот файл: что такое одна строка, сколько строк и уникальных order_id, где пропуски, странные форматы и невозможные значения. <b>Ничего пока не исправляй.</b>", "Describe this file: what one row is, how many rows and unique order_ids, where there are gaps, odd formats and impossible values. <b>Do not fix anything yet.</b>")}</div></div>
        <table class="tbl" style="font-size:18px;">{th}{"".join(trs)}</table>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин. Первый промпт к любому файлу — профиль. Не «найди инсайты», а «опиши, что тут лежит». И отдельная фраза: «ничего пока не исправляй». Иначе модель начнёт молча чистить данные, и вы не узнаете, что она поменяла.",
                      "⏱ 5 min. The first prompt for any file is a profile. Not “find insights” but “describe what is here”. And a separate phrase: “do not fix anything yet”. Otherwise the model starts cleaning silently and you never learn what it changed."),
                    t(f"В нашем файле 4 проблемы, мы их подложили специально: строка {MISS_ID} без региона; строка {DUP_ID} записана дважды; в строке {DATE_ID} дата через слэши; в строке {BAD_ID} 66 возвратов при 62 заказах. Ни одна не видна, если просто пролистать начало таблицы, — поэтому профиль и делают кодом.",
                      f"Our file has 4 planted problems: row {MISS_ID} has no region; row {DUP_ID} appears twice; row {DATE_ID} uses slashes in the date; row {BAD_ID} has 66 returns on 62 orders. None is visible if you just scroll the top of the table — that is why the profile is done with code."),
                    t(f"Обратите внимание на цену дубля: одна лишняя строка добавляет {money(float(ROW[DUP_ID]['revenue']))} к выручке. Итог «как в файле» — {money(TOTAL_RAW)}, правильный — {money(TOTAL)}.",
                      f"Note what the duplicate costs: one extra row adds {money(float(ROW[DUP_ID]['revenue']))} to revenue. The “as in the file” total is {money(TOTAL_RAW)}; the correct one is {money(TOTAL)}.")))


def s_fix():
    tr_date = TRUTH[DATE_ID]["date"]
    safe = [(f"{DUP_ID} ×2", t(f"+{money(float(ROW[DUP_ID]['revenue']))} к выручке", f"+{money(float(ROW[DUP_ID]['revenue']))} to revenue"), t(f"оставить одну строку", "keep one row"), t("записать в журнал", "log it")),
            (t("region: (пусто)", "region: (empty)"), t(f"строка {MISS_ID}", f"row {MISS_ID}"), "region: UNKNOWN", t("не удалять строку", "do not drop the row")),
            (ROW[DATE_ID]["date"], t(f"строка {DATE_ID}", f"row {DATE_ID}"), ROW[DATE_ID]["date"].replace("/", "-"), t(f"формат исправлен, но в источнике день другой ({tr_date}) → в журнал", f"format fixed, but the source has a different day ({tr_date}) → log it"))]
    sh = "".join(f'<div class="fx"><div class="from">{a}<small>{b}</small></div><div class="ar">→</div><div class="to">{c}<small>{d}</small></div></div>' for a, b, c, d in safe)
    bad = ROW[BAD_ID]
    return dict(min=6, html=f'''
  {head(t("Шаг 2 • чистка", "Step 2 • cleaning"), t("Нашли проблему ≠ имеем право её исправить", "Finding a problem ≠ permission to fix it"))}
  <div class="body" style="margin-top:22px;">
    <div class="lanes">
      <div class="lane" style="--k:var(--green)"><div class="lh">{t("Механика — можно исправить", "Mechanics — OK to fix")}<small>{t("смысл данных не меняется; каждое изменение — в журнал чистки", "the meaning does not change; every change goes into the cleaning log")}</small></div>{sh}</div>
      <div class="lane" style="--k:var(--red)"><div class="lh">{t("Смысл — исправлять нельзя", "Meaning — do not fix")}<small>{t("правильное значение знает только источник", "only the source knows the right value")}</small></div>
        <div class="fx"><div class="from">returns {bad['returns']}<small>{t(f"при {bad['orders']} заказах, строка {BAD_ID}", f"on {bad['orders']} orders, row {BAD_ID}")}</small></div><div class="ar">→</div><div class="to" style="border-color:var(--red)">{t("оставить + флаг", "keep + flag")}<small>{t("спросить владельца данных", "ask the data owner")}</small></div></div>
        <div class="verd" style="gap:14px;margin-top:6px;">
          <div class="vd" style="--k:var(--red)"><div class="ic">✗</div><div><div class="h" style="font-size:21px">{t("Модели угадывали: «6», «6 или 2»", "Models guessed: “6”, “6 or 2”")}</div></div></div>
          <div class="vd" style="--k:var(--green)"><div class="ic">✓</div><div><div class="h" style="font-size:21px">{t(f"В источнике было {TRUTH[BAD_ID]['returns']}", f"The source had {TRUTH[BAD_ID]['returns']}")}</div></div></div>
        </div>
      </div>
    </div>
    <div class="plaque g" style="margin-top:30px;">{t("<b>Журнал чистки:</b> что изменили · в каких строках · почему · как это изменило итог. Без журнала чистка — это молчаливая правка данных.", "<b>Cleaning log:</b> what changed · which rows · why · how it moved the total. Without a log, cleaning is a silent edit of the data.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Главная развилка урока. Слева — механические правки: убрать точный дубль, подписать пустой регион как UNKNOWN (а не выкинуть строку с выручкой!), привести дату к одному формату. Смысл данных от этого не меняется, но каждую правку записываем в журнал.",
                      "⏱ 6 min. The key fork of the lesson. On the left — mechanical fixes: remove an exact duplicate, label the empty region UNKNOWN (rather than dropping a row that has revenue!), bring the date to one format. The meaning of the data does not change, but each fix goes into the log."),
                    t(f"Даже «безопасная» правка — допущение. Мы заменили слэши на дефисы и получили 22 апреля, а в исходной системе была дата {tr_date}. На помесячную выручку это не влияет, но именно поэтому нужен журнал: кто-то потом сверит.",
                      f"Even a “safe” fix is an assumption. We replaced slashes with dashes and got 22 April, while the source system says {tr_date}. Monthly revenue is unaffected, but this is exactly why we keep a log: someone can check later."),
                    t(f"Справа — смысловая ошибка: 66 возвратов при 62 заказах. Модели в нашем эксперименте «чинили» на 6 или 2. Правильный ответ знал только источник — там было {TRUTH[BAD_ID]['returns']}. Правило: такую строку не правим и не удаляем, а помечаем и спрашиваем владельца данных. Попросите модель делить правки на эти две группы — она это умеет, если попросить.",
                      f"On the right — a meaning error: 66 returns on 62 orders. In our experiment models “fixed” it to 6 or 2. Only the source knew the answer: {TRUTH[BAD_ID]['returns']}. Rule: do not edit or delete such a row; flag it and ask the data owner. Ask the model to sort fixes into these two groups — it can, if asked.")))


def s_prompt():
    slots = [("cyan", t("вопрос", "question")), ("amber", t("сначала профиль", "profile first")), ("red", t("правила чистки", "cleaning rules")),
             ("green", t("расчёт с кодом", "calculation with code")), ("violet", t("сверка", "reconciliation")), ("pink", t("что вернуть", "what to return"))]
    txt = [
        t("Вопрос: как менялась выручка с января по июнь и какой канал рос быстрее всех?", "Question: how did revenue change from January to June, and which channel grew fastest?"),
        t("Сначала опиши данные: что такое одна строка, сколько строк и уникальных order_id, пропуски, странные значения.", "First describe the data: what one row is, how many rows and unique order_ids, gaps, odd values."),
        t("Механические правки — делай и записывай. Если правка меняет смысл — не исправляй, а спроси меня.", "Mechanical fixes — do them and log them. If a fix changes the meaning — don’t, ask me."),
        t("Посчитай выручку по месяцам и по каналам, покажи код.", "Calculate revenue by month and by channel, show the code."),
        t("Сверь: сумма по месяцам = сумма по каналам = общий итог.", "Reconcile: sum by month = sum by channel = grand total."),
        t("Верни: таблицу, один график, журнал чистки и одну вещь, которую эти данные не доказывают.", "Return: a table, one chart, the cleaning log and one thing this data does not prove."),
    ]
    p = "<br>".join(f'<span data-n="{i + 1}" style="--k:var(--{slots[i][0]})">{s}</span>' for i, s in enumerate(txt))
    sl = "".join(f'<div class="slot" style="--k:var(--{c})"><i>{i + 1}</i>{n}</div>' for i, (c, n) in enumerate(slots))
    return dict(min=6, html=f'''
  {head(t("Шаг 3 • промпт", "Step 3 • prompt"), t("Промпт аналитика: вопрос, правила, доказательства", "An analyst’s prompt: question, rules, evidence"))}
  <div class="body" style="margin-top:18px;">
    <div class="dprompt" style="font-family:var(--body);font-size:26px;line-height:1.8;">{p}</div>
    <div class="slots" style="margin-top:20px;">{sl}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Сравните с промптом «найди интересные инсайты». Здесь шесть частей. Вопрос — конкретный, с периодом. Сначала профиль. Правила чистки — что можно делать самой модели, а где остановиться и спросить. Расчёт — с кодом, чтобы его можно было открыть. Сверка — модель сама сводит итоги двумя способами. И что вернуть — включая честное «чего данные не доказывают».",
                      "⏱ 6 min. Compare it with “find interesting insights”. Here there are six parts. The question — specific, with a period. Profile first. Cleaning rules — what the model may do itself and where to stop and ask. Calculation — with code you can open. Reconciliation — the model totals things two ways itself. And what to return — including an honest “what the data does not prove”."),
                    t("Мы не диктуем модели, как писать код, — мы задаём, какие доказательства хотим увидеть. Этот промпт лежит в шпаргалке, его можно копировать в демо и в домашке.",
                      "We do not dictate how to write the code — we set what evidence we want to see. The prompt is in the cheatsheet; copy it for the demo and homework.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут", "5 minutes")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: живое демо на файле Northstar, графики, проверка результата, «что было» ≠ «что будет, если…» и домашнее задание.", "Next: a live demo on the Northstar file, charts, checking the result, “what happened” ≠ “what will happen if…” and homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт». Во время перерыва откройте чат-ассистента и подготовьте файл northstar_sales_messy.csv к загрузке.",
                              "⏱ 5 min. Press “Start”. During the break open the chat assistant and get northstar_sales_messy.csv ready to upload.")))


def s_demo():
    steps = [("cyan", t("Профиль", "Profile"), t("Опиши файл. Ничего не исправляй.", "Describe the file. Fix nothing."), t("<b>Ищем:</b> 73 строки, 72 ключа, 4 проблемы", "<b>Look for:</b> 73 rows, 72 keys, 4 problems")),
             ("amber", t("Правки", "Fixes"), t("Раздели правки: механика / смысл. Что предлагаешь?", "Split the fixes: mechanics / meaning. What do you suggest?"), t("<b>Ищем:</b> строку 1055 не «чинит»", "<b>Look for:</b> row 1055 is not “fixed”")),
             ("green", t("Расчёт и график", "Calculation and chart"), t("Выручка по месяцам и каналам, один график, сверка итогов.", "Revenue by month and channel, one chart, reconcile totals."), t(f"<b>Ищем:</b> итог {money(TOTAL)}, код открыт", f"<b>Look for:</b> total {money(TOTAL)}, code opened")),
             ("red", t("Ловушка", "The trap"), t("Какому каналу дать больше бюджета в июле?", "Which channel should get more budget in July?"), t("<b>Ищем:</b> скажет ли модель «по этим данным не доказать»", "<b>Look for:</b> will the model say “this data can’t prove it”"))]
    st = "".join(f'<div class="step" style="--k:var(--{c})"><div class="no">{t("ШАГ", "STEP")} {i + 1}</div><div class="h">{h}</div><div class="p">{p}</div><div class="w">{w}</div></div>'
                 for i, (c, h, p, w) in enumerate(steps))
    return dict(min=10, html=f'''
  {head(t("Живое демо • 10 минут", "Live demo • 10 minutes"), t("От грязного CSV к проверенному ответу", "From a messy CSV to a checked answer"), k="green")}
  <div class="body" style="margin-top:22px;">
    <div class="steps">{st}</div>
    <div class="plaque g" style="margin-top:40px;font-size:24px;">{t("<b>Задание зрителям — в чат Teams:</b> ① одна правка, которую сделала модель · ② одна проблема, которую она оставила · ③ одна проверка итогов.", "<b>Audience task — in the Teams chat:</b> ① one fix the model made · ② one problem it left alone · ③ one check of the totals.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 10 мин. Ведите по ранбуку L08_04. Загрузите northstar_sales_messy.csv в ChatGPT, Claude или Gemini — в тот, что открыт у вас в рабочем пространстве. Четыре коротких промпта, по одному на шаг. После каждого ответа раскройте код.",
                      "⏱ 10 min. Follow runbook L08_04. Upload northstar_sales_messy.csv to ChatGPT, Claude or Gemini — whichever your workspace has. Four short prompts, one per step. After each answer, open the code."),
                    t("Шаг 2: если модель всё-таки «починила» 1055, не прячьте — это лучший момент урока. Спросите: «Откуда ты знаешь правильное значение?» Шаг 4 — ловушка: если модель уверенно советует перенести бюджет, спросите, какое допущение она делает. Разберём на слайде 14.",
                      "Step 2: if the model still “fixes” 1055, don’t hide it — it is the best moment of the lesson. Ask: “How do you know the right value?” Step 4 is a trap: if the model confidently advises moving budget, ask which assumption it is making. We cover it on slide 14."),
                    t("Teams: делитесь окном браузера, а не всем экраном; увеличьте масштаб страницы до 125–150%, чтобы таблицы читались.",
                      "Teams: share the browser window, not the whole screen; zoom the page to 125–150% so the tables are readable."),
                    t("Запасной путь: если сервис думает дольше 90 секунд — терминал, python reference_analysis.py, готовые файлы и графики в fallback_outputs/.",
                      "Fallback: if the service thinks for more than 90 seconds — terminal, python reference_analysis.py, ready files and charts in fallback_outputs/.")))


def s_results():
    org = max(BY_CH, key=BY_CH.get)
    fast = max(CH_GROWTH, key=CH_GROWTH.get)
    return dict(min=5, html=f'''
  {head(t("Результат демо", "Demo result"), t("Один график — один вывод", "One chart — one claim"))}
  <div class="body" style="margin-top:20px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:48px;">
      <div class="stack" style="gap:6px;">
        <div class="vlabel" style="font-size:22px;font-weight:700;">{t("Выручка по месяцам, $ тыс.", "Revenue by month, $k")}</div>
        {line_chart()}
        <div class="note" style="--k:var(--cyan)">{t(f"<b>Вывод:</b> выручка выросла на {dec(GROWTH)}\u00a0% — с ${k(MONTHLY[MONTHS[0]])} в январе до ${k(MONTHLY[MONTHS[-1]])} в июне.", f"<b>Claim:</b> revenue grew {GROWTH:.1f}% — from ${k(MONTHLY[MONTHS[0]])} in January to ${k(MONTHLY[MONTHS[-1]])} in June.")}</div>
      </div>
      <div class="stack" style="gap:6px;">
        <div class="vlabel" style="font-size:22px;font-weight:700;">{t("Выручка канала: январь → июнь, $ тыс.", "Channel revenue: January → June, $k")}</div>
        {slope_chart()}
        <div class="note" style="--k:var(--amber)">{t(f"<b>Вывод:</b> быстрее всех рос {fast} ({pct(CH_GROWTH[fast])}) — но с самой низкой базы. Больше всех за полгода принёс {org} — {money(BY_CH[org])}.", f"<b>Claim:</b> {fast} grew fastest ({pct(CH_GROWTH[fast])}) — but from the lowest base. {org} brought the most over six months — {money(BY_CH[org])}.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 5 мин. Это реальные цифры из файла после чистки. Слева — тренд: линия, потому что важен порядок во времени. Справа — сравнение начала и конца по каналам. Каждый график подписан одним выводом, и вывод проверяется по самому графику.",
                      f"⏱ 5 min. These are real numbers from the file after cleaning. Left — the trend: a line, because order in time matters. Right — start vs end per channel. Each chart carries one claim, and the claim can be checked on the chart itself."),
                    t(f"Обратите внимание: «какой канал главный?» — это два разных вопроса. Кто больше всех принёс — {org}. Кто быстрее всех рос — {fast}. Модель ответит на тот вопрос, который вы задали, поэтому вопрос формулируем точно.",
                      f"Note: “which channel matters most?” is two different questions. Who brought the most — {org}. Who grew fastest — {fast}. The model answers the question you asked, so phrase it precisely.")))


def s_charts():
    items = [("line", t("Как менялось во времени?", "How did it change over time?"), t("линия", "line"), t("порядок месяцев важен", "month order matters")),
             ("bar", t("Кто больше?", "Who is bigger?"), t("столбцы", "bars"), t("сортируйте; ось от нуля", "sort; axis from zero")),
             ("hist", t("Как распределены значения?", "How are values spread?"), t("гистограмма", "histogram"), t("видно выбросы", "shows outliers")),
             ("scatter", t("Связаны ли два числа?", "Are two numbers related?"), t("точки", "scatter"), t("связь ≠ причина", "related ≠ cause")),
             ("stack", t("Из чего состоит целое?", "What makes up the whole?"), t("столбцы 100%", "100% bars"), t("не больше 4–5 частей", "no more than 4–5 parts"))]
    m = "".join(f'<div class="mini" style="--k:var(--cyan)">{mini(kd)}<div class="q">{q}</div><div class="c">{c}</div><div class="w">{w}</div></div>' for kd, q, c, w in items)
    return dict(min=4, html=f'''
  {head(t("Графики", "Charts"), t("Тип графика выбирает вопрос, а не красота", "The question picks the chart type, not looks"))}
  <div class="body">
    <div class="minis">{m}</div>
    <div class="plaque" style="margin-top:40px;">{t("<b>Просите так:</b> «Построй один график, который отвечает на вопрос …, подпиши оси и единицы». Не «сделай красивый дашборд».", "<b>Ask like this:</b> “Build one chart that answers …, label the axes and units.” Not “make a nice dashboard”.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Пять вопросов — пять типов графика. Тренд — линия. Сравнение — столбцы, отсортированные, с осью от нуля (иначе маленькая разница выглядит огромной). Распределение — гистограмма. Связь — точки, и помним: связь не значит причину. Доли — столбцы 100%, не больше 4–5 частей.",
                      "⏱ 4 min. Five questions — five chart types. Trend — line. Comparison — bars, sorted, axis from zero (otherwise a small gap looks huge). Distribution — histogram. Relationship — scatter, and remember: related is not cause. Shares — 100% bars, no more than 4–5 parts."),
                    t("ИИ охотно делает «дашборд из шести графиков». Просите один график под один вопрос — его проще проверить.",
                      "AI happily makes a “six-chart dashboard”. Ask for one chart per question — it is easier to check.")))


def s_verify():
    m_sum, c_sum = sum(MONTHLY.values()), sum(BY_CH.values())
    blue, green, mut, fg = "#38bdf8", "#34d399", "#a3b1c4", "#f1f5f9"
    def path_row(y, label, n):
        return (f'<text x="0" y="{y + 8}" font-size="26" font-weight="700" fill="{fg}">{label}</text>'
                f'<text x="0" y="{y + 40}" font-size="21" fill="{mut}">{n}</text>'
                f'<path d="M300 {y + 10} C 420 {y + 10}, 440 150, 536 150" stroke="{blue}" stroke-width="3" fill="none" marker-end="url(#va)"/>')
    svg = (f'<svg class="dia" viewBox="0 0 800 300">' + ARROW.format(id="va", c=blue)
           + path_row(30, t("Сумма по месяцам", "Sum by month"), t(f"{len(MONTHS)} чисел", f"{len(MONTHS)} numbers"))
           + path_row(135, t("Сумма по каналам", "Sum by channel"), t(f"{len(CHANNELS)} числа", f"{len(CHANNELS)} numbers"))
           + path_row(240, t("Сумма по строкам", "Sum of rows"), t(f"{len(CLEAN)} строки после чистки", f"{len(CLEAN)} rows after cleaning"))
           + f'<rect x="545" y="100" width="250" height="100" rx="14" fill="#0f1624" stroke="{green}" stroke-width="2.5"/>'
           + f'<text x="670" y="163" text-anchor="middle" font-size="38" font-weight="800" fill="{green}">{money(TOTAL)}</text>'
           + f'<text x="670" y="236" text-anchor="middle" font-size="20" fill="{mut}">{t("три пути — одно число ✓", "three paths — one number ✓")}</text>'
           + '</svg>')
    assert abs(m_sum - c_sum) < 1e-6
    sp = ROW["1063"]
    checks = [t(f"<b>Строки:</b> было {len(RAW)}, удалён 1 дубль, осталось {len(CLEAN)}", f"<b>Rows:</b> {len(RAW)} before, 1 duplicate removed, {len(CLEAN)} left"),
              t("<b>Итоги</b> сходятся тремя путями (схема слева)", "<b>Totals</b> match three ways (diagram on the left)"),
              t(f"<b>Ручная точка:</b> найдите строку 1063 глазами — {sp['channel']}, июнь, {money(float(sp['revenue']))}", f"<b>Spot check:</b> find row 1063 by eye — {sp['channel']}, June, {money(float(sp['revenue']))}"),
              t("<b>База процента:</b> от какого числа и за какой период", "<b>Base of a %:</b> from which number and over which period"),
              t("<b>График = таблица:</b> точки на графике совпадают с числами", "<b>Chart = table:</b> points on the chart match the numbers")]
    return dict(min=6, html=f'''
  {head(t("Шаг 4 • проверка", "Step 4 • checking"), t("Проверяем числа, а не текст ответа", "Check the numbers, not the wording"), k="green")}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:56px;align-items:center;">
      {svg}
      <ol class="checklist" style="gap:20px;">{"".join(f"<li><span>{c}</span></li>" for c in checks)}</ol>
    </div>
    <div class="plaque" style="margin-top:22px;">{t("Перечитать ответ модели — <b>не проверка</b>. Проверка — это когда то же число получено другим путём.", "Rereading the model’s answer is <b>not a check</b>. A check means getting the same number another way.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 6 мин. Проверка — это часть анализа, а не вежливость. Пять проверок, каждая ловит свой тип ошибки. Количество строк ловит дубли и потерянные строки. Сверка итогов тремя путями ловит ошибки группировки. Ручная точка — одна строка, которую вы находите глазами в исходном файле. Знаменатель — «рост на 64%» от чего и за какой период? График и таблица должны совпадать.",
                      "⏱ 6 min. Checking is part of the analysis, not politeness. Five checks, each catches a different kind of error. Row counts catch duplicates and lost rows. Reconciling totals three ways catches grouping mistakes. A spot check is one row you find by eye in the source file. Denominator — “64% growth” from what and over which period? Chart and table must match."),
                    t("Самое удобное: попросите модель саму сделать эти проверки кодом и показать результат. Но одну проверку — ручную точку — делайте сами.",
                      "Most convenient: ask the model to run these checks in code and show the result. But do one check yourself — the spot check."),
                    t("Почему это не паранойя: на бенчмарке DABstep (2025) лучший ИИ-агент решил лишь 14,55% сложных многошаговых задач анализа данных, на DSBench (2024) — 34%. На простых задачах модели хороши, на сложных — ошибаются часто и уверенно.",
                      "Why this is not paranoia: on the DABstep benchmark (2025) the best AI agent solved only 14.55% of hard multi-step data-analysis tasks; on DSBench (2024), 34%. Models are good at simple tasks and often confidently wrong on hard ones.")))


def s_causal():
    rs = sorted(ROAS, key=ROAS.get, reverse=True)
    hb = "".join(
        f'<div class="hb" style="--k:var(--{"amber" if c == rs[0] else "cyan"})"><div class="lab">{c}<small>{t("$ выручки на $1 рекламы", "$ revenue per $1 of ads")}</small></div>'
        f'<div class="tr" style="height:56px"><div class="b" style="width:{ROAS[c] / 6 * 75:.1f}%"></div><div class="v" style="left:calc({ROAS[c] / 6 * 75:.1f}% + 14px)">{dec(ROAS[c], 2)}'
        + '</div></div></div>' for c in rs)
    grey, mut, fg, red, amber = "#5f6e84", "#a3b1c4", "#f1f5f9", "#f87171", "#fbbf24"
    fac = [t("сезон", "season"), t("кому показывали", "who was targeted"), t("известность бренда", "brand demand"), t("правила атрибуции", "attribution rules")]
    svg = f'<svg class="dia" viewBox="0 0 620 330">' + ARROW.format(id="ca", c=grey) + ARROW.format(id="cr", c=red)
    for i, f in enumerate(fac):
        x = 10 + (i % 2) * 310
        yb = 0 if i < 2 else 66
        svg += (f'<rect x="{x}" y="{yb}" width="290" height="54" rx="10" fill="#0f1624" stroke="{grey}" stroke-width="1.5" stroke-dasharray="5 4"/>'
                f'<text x="{x + 145}" y="{yb + 35}" text-anchor="middle" font-size="21" fill="{mut}">{f}</text>')
    svg += (f'<circle cx="310" cy="138" r="5" fill="{grey}"/>'
            f'<path d="M310 124 L 310 133" stroke="{grey}" stroke-width="2"/>'
            f'<path d="M310 138 L 160 194" stroke="{grey}" stroke-width="2" fill="none" marker-end="url(#ca)"/>'
            f'<path d="M310 138 L 460 194" stroke="{grey}" stroke-width="2" fill="none" marker-end="url(#ca)"/>'
            f'<text x="310" y="178" text-anchor="middle" font-size="18" fill="{mut}">{t("влияют на оба", "affect both")}</text>')
    svg += (f'<rect x="40" y="200" width="220" height="70" rx="12" fill="#0f1624" stroke="{amber}" stroke-width="2"/>'
            f'<text x="150" y="243" text-anchor="middle" font-size="22" font-weight="700" fill="{fg}">{t("бюджет", "ad budget")}</text>'
            f'<rect x="360" y="200" width="220" height="70" rx="12" fill="#0f1624" stroke="{amber}" stroke-width="2"/>'
            f'<text x="470" y="243" text-anchor="middle" font-size="22" font-weight="700" fill="{fg}">{t("выручка", "revenue")}</text>'
            f'<path d="M264 235 L 354 235" stroke="{red}" stroke-width="3" fill="none" stroke-dasharray="8 6" marker-end="url(#cr)"/>'
            f'<text x="309" y="300" text-anchor="middle" font-size="19" font-weight="700" fill="{red}">{t("причина? не доказано", "cause? not proven")}</text></svg>')
    return dict(min=6, html=f'''
  {head(t("Шаг 5 • граница вывода", "Step 5 • the limit of a claim"), t("«Что было» ≠ «что будет, если…»", "“What happened” ≠ “what will happen if…”"), t("Вопрос-ловушка из демо: <b>перенести бюджет из Social в Search?</b>", "The trap question from the demo: <b>move budget from Social to Search?</b>"), k="red")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:50px;align-items:center;">
      <div class="stack" style="gap:18px;">
        <div class="hbars" style="gap:22px;--lw:250px;">{hb}</div>
        <div class="cap">{t("Email и Organic: рекламы нет — окупаемость не считается.", "Email and Organic: no ad spend — return on ads is not computed.")}</div>
        <div class="plaque g">{t("<b>Честный ответ:</b> данные описывают прошлое. Чтобы узнать эффект — <b>тест</b>: перенести часть бюджета в одном регионе на 2–4 недели и сравнить.", "<b>Honest answer:</b> the data describes the past. To learn the effect — <b>a test</b>: shift part of the budget in one region for 2–4 weeks and compare.")}</div>
      </div>
      {svg}
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 6 мин. Окупаемость рекламы (ROAS) — выручка на доллар рекламы. У Search {ROAS['Search']:.2f}, у Social {ROAS['Social']:.2f}. Соблазн: «переносим деньги в Search». Модель, кстати, часто так и советует.",
                      f"⏱ 6 min. Return on ad spend (ROAS) is revenue per dollar of advertising. Search has {ROAS['Search']:.2f}, Social {ROAS['Social']:.2f}. Temptation: “move the money to Search”. Models often advise exactly that."),
                    t("Но эти числа описывают прошлое. Справа — почему нельзя делать вывод о причине: на бюджет и на выручку одновременно влияют сезон, то, кому показывали рекламу, известность бренда, правила, по которым продажу приписали каналу. Возможно, Search просто ловит тех, кто и так собирался купить.",
                      "But these numbers describe the past. On the right — why we cannot claim a cause: season, who saw the ads, brand demand and the rules that credit a sale to a channel all affect both budget and revenue. Search may simply catch people who were going to buy anyway."),
                    t("Хороший ответ ИИ: «по этим данным нельзя сказать, что перенос бюджета увеличит выручку; предлагаю тест». Если модель так не ответила — спросите: «Какое допущение ты делаешь?»",
                      "A good AI answer: “this data cannot show that moving budget will increase revenue; I suggest a test”. If the model did not say so, ask: “What assumption are you making?”")))


def s_code():
    code = (
        '<span class="kw">import</span> pandas <span class="kw">as</span> pd\n'
        'df = pd.<span class="fn">read_csv</span>(<span class="str">"northstar_sales_messy.csv"</span>)\n\n'
        f'<span class="fn">print</span>(<span class="fn">len</span>(df), df[<span class="str">"order_id"</span>].<span class="fn">nunique</span>())   <span class="cm"># 73 72</span>\n'
        f'<span class="fn">print</span>(df[df[<span class="str">"returns"</span>] &gt; df[<span class="str">"orders"</span>]])  <span class="cm"># {t("строка", "row")} 1055</span>\n\n'
        'df = df.<span class="fn">drop_duplicates</span>(<span class="str">"order_id"</span>)\n'
        'df[<span class="str">"region"</span>] = df[<span class="str">"region"</span>].<span class="fn">fillna</span>(<span class="str">"UNKNOWN"</span>)\n'
        'df[<span class="str">"date"</span>] = pd.<span class="fn">to_datetime</span>(df[<span class="str">"date"</span>].str.<span class="fn">replace</span>(<span class="str">"/"</span>, <span class="str">"-"</span>))\n\n'
        'month = df[<span class="str">"date"</span>].dt.<span class="fn">to_period</span>(<span class="str">"M"</span>)\n'
        'monthly = df.<span class="fn">groupby</span>(month)[<span class="str">"revenue"</span>].<span class="fn">sum</span>()\n'
        'by_channel = df.<span class="fn">groupby</span>(<span class="str">"channel"</span>)[<span class="str">"revenue"</span>].<span class="fn">sum</span>()\n'
        f'<span class="kw">assert</span> monthly.<span class="fn">sum</span>() == by_channel.<span class="fn">sum</span>()   <span class="cm"># {t("сверка", "reconcile")}</span>')
    return dict(min=3, html=f'''
  {head(t("Для справки • pandas", "For reference • pandas"), t("Что модель пишет «под капотом»", "What the model writes under the hood"), t("<b>pandas</b> — библиотека Python для работы с таблицами. Её используют почти все ИИ-анализаторы.", "<b>pandas</b> is a Python library for working with tables. Almost every AI analyser uses it."), k="violet")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.6fr 1fr;gap:40px;align-items:center;">
      <pre class="code" style="font-size:21px;">{code}</pre>
      <div class="stack" style="gap:24px;">
        <div class="note" style="--k:var(--violet)">{t("Это <b>примерно то</b>, что вы увидите, раскрыв код в ChatGPT, Claude или Gemini. Учить синтаксис не нужно.", "This is <b>roughly what</b> you see when you open the code in ChatGPT, Claude or Gemini. No need to learn the syntax.")}</div>
        <div class="note" style="--k:var(--green)">{t("Читайте <b>смысл строк</b>: что удалили, чем заполнили пропуск, по чему сгруппировали.", "Read <b>what each line means</b>: what was removed, what filled the gap, what it grouped by.")}</div>
        <div class="cap">{t(f"Код проверен на нашем файле: итог {money(TOTAL)}.", f"Code verified on our file: total {money(TOTAL)}.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Слайд для справки, построчно не разбираем. Покажите, что код читается почти как текст: прочитали файл, посчитали строки и уникальные ключи, нашли невозможные возвраты, удалили дубли, заполнили пропуск, привели дату, сгруппировали по месяцам и каналам, сверили.",
                      "⏱ 3 min. A reference slide; don’t go line by line. Show that the code reads almost like text: read the file, count rows and unique keys, find impossible returns, drop duplicates, fill the gap, fix the date, group by month and channel, reconcile."),
                    t("Навык, который нужен новичку, — не писать такой код, а узнавать в нём решения: «ага, здесь модель удалила строки — сколько и почему?»",
                      "The skill a beginner needs is not writing this code but spotting the decisions in it: “aha, here the model dropped rows — how many and why?”")))


def s_privacy():
    rows = [("green", t("Можно: учебные, открытые, обезличенные данные", "OK: practice, public, anonymised data"), t("как наш Northstar; любой сервис", "like our Northstar; any service")),
            ("amber", t("Осторожно: внутренние данные компании", "Careful: internal company data"), t("только рабочий аккаунт компании (ChatGPT Business/Enterprise, Claude Team/Enterprise, Google Workspace) — там данные не идут на обучение", "only the company work account (ChatGPT Business/Enterprise, Claude Team/Enterprise, Google Workspace) — data is not used for training there")),
            ("red", t("Нельзя без разрешения: клиенты, сотрудники, финансы, здоровье", "Not without approval: customers, staff, finance, health"), t("персональные данные — только в одобренной среде и с согласия владельца данных", "personal data — only in an approved environment and with the data owner’s consent"))]
    lr = "".join(f'<div class="lrow" style="--k:var(--{c})"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for c, h, d in rows)
    return dict(min=4, html=f'''
  {head(t("Данные и приватность", "Data and privacy"), t("Что можно загружать в чат", "What you may upload to a chat"), k="amber")}
  <div class="body" style="margin-top:20px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:44px;align-items:center;">
      <div class="light">{lr}</div>
      <div class="stack" style="gap:20px;">
        <div class="note" style="--k:var(--amber)">{t("В личных аккаунтах обучение на ваших данных <b>зависит от настроек</b>: ChatGPT — «Improve the model for everyone», Gemini — «Keep Activity», Claude — только если вы сами разрешили.", "In personal accounts, training on your data <b>depends on settings</b>: ChatGPT — “Improve the model for everyone”, Gemini — “Keep Activity”, Claude — only if you allowed it.")}</div>
        <div class="note" style="--k:var(--cyan)">{t("Перед загрузкой: <b>уберите лишние колонки</b> (имена, телефоны, e-mail). Для анализа продаж они не нужны.", "Before uploading: <b>remove unneeded columns</b> (names, phones, e-mails). Sales analysis does not need them.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Светофор. Зелёный — учебные и открытые данные, как наш файл. Жёлтый — внутренние данные компании: только в рабочем аккаунте, где по умолчанию данные не идут на обучение. Красный — персональные данные клиентов и сотрудников, финансы, здоровье: только в одобренной компанией среде.",
                      "⏱ 4 min. A traffic light. Green — practice and public data, like our file. Amber — internal company data: only in the work account where, by contract, data is not used for training. Red — personal data of customers and staff, finance, health: only in an environment approved by the company."),
                    t("Простое правило: перед загрузкой удалите колонки, которые не нужны для вопроса. Для анализа продаж по каналам не нужны ни имена, ни телефоны.",
                      "Simple rule: before uploading, delete columns the question does not need. Sales-by-channel analysis needs neither names nor phone numbers."),
                    t("Где настройки (октябрь 2026): ChatGPT — «Improve the model for everyone»; Claude — потребительские чаты идут на обучение, только если вы это разрешили; Gemini — обучение связано с настройкой «Keep Activity». Бизнес-тарифы (ChatGPT Business/Enterprise, Claude Team/Enterprise/API, Google Workspace) по умолчанию на обучение не используются.",
                      "Where the settings are (October 2026): ChatGPT — “Improve the model for everyone”; Claude — consumer chats are used for training only if you allowed it; Gemini — training is tied to the “Keep Activity” setting. Business plans (ChatGPT Business/Enterprise, Claude Team/Enterprise/API, Google Workspace) are not used for training by default.")))


def s_hw():
    files = (f'verified_analysis_pack/\n'
             f'  cleaning_log.md     <span class="cm"># {t("строки до/после, каждая правка", "rows before/after, every fix")}</span>\n'
             f'  analysis_brief.md   <span class="cm"># {t("3–5 выводов с периодом и базой", "3–5 claims with period and base")}</span>\n'
             f'  chart.png           <span class="cm"># {t("один график = один вывод", "one chart = one claim")}</span>\n'
             f'  cleaned_data.csv    <span class="cm"># {t("или скрипт чистки", "or the cleaning script")}</span>\n'
             f'  verification.md     <span class="cm"># {t("3+ проверки + 1 «данные этого не доказывают»", "3+ checks + 1 “the data does not prove this”")}</span>')
    return dict(min=4, html=f'''
  {head(t("Практика и домашнее задание", "Practice and homework"), t("Проверенный пакет анализа", "A verified analysis pack"), t("Файл <code>northstar_sales_messy.csv</code>. Вопрос руководства: <b>что изменилось в продажах с января по июнь и что проверить дальше?</b>", "File <code>northstar_sales_messy.csv</code>. Management asks: <b>what changed in sales from January to June, and what should we check next?</b>"), k="green")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.2fr 1fr;gap:40px;align-items:center;">
      <div class="files">{files}</div>
      <div class="stack" style="gap:22px;">
        <div class="note" style="--k:var(--green)">{t("<b>В парах:</b> один ведёт чат с ИИ, второй проверяет. На середине — поменяйтесь.", "<b>In pairs:</b> one drives the AI chat, the other checks. Swap halfway.")}</div>
        <div class="note" style="--k:var(--red)">{t("<b>Обязательно:</b> одно утверждение, которое звучит правдоподобно, но данные его не доказывают.", "<b>Required:</b> one statement that sounds plausible but the data does not prove.")}</div>
        <div class="cap">{t("Шаблоны и критерии — в файле задания L08_05_Homework.", "Templates and rubric — in the task file L08_05_Homework.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Результат домашки — не «ответ из чата», а пакет из пяти файлов, который другой человек проверит за 5 минут. Журнал чистки, краткий отчёт, один график, очищенные данные или скрипт, файл проверок.",
                      "⏱ 4 min. The homework result is not “an answer from the chat” but a five-file pack another person can check in 5 minutes. Cleaning log, short brief, one chart, cleaned data or script, and the checks file."),
                    t("Самый важный пункт — отказ: напишите одно утверждение, которое напрашивается, но данными не подтверждается. Например, «реклама в Search окупится лучше, если удвоить бюджет». Шаблоны лежат в demo_assets/student_starter.",
                      "The most important item is the refusal: write one statement that suggests itself but is not supported by the data. For example, “Search ads will pay off better if we double the budget”. Templates are in demo_assets/student_starter.")))


def s_summary():
    rules = [("cyan", t("Сначала профиль, потом вопросы", "Profile first, then questions"), t("что такое строка, ключ, период, единицы", "what a row is, key, period, units")),
             ("red", t("Механику чиним, смысл — нет", "Fix mechanics, not meaning"), t("невозможное значение — флаг и вопрос источнику", "impossible value — flag it and ask the source")),
             ("violet", t("Числа считает код", "Code does the numbers"), t("раскрывайте код и читайте решения в нём", "open the code and read the decisions in it")),
             ("green", t("Проверка = то же число другим путём", "A check = the same number another way"), t("строки, итоги, одна ручная точка", "rows, totals, one spot check")),
             ("amber", t("«Что было» ≠ «что будет, если…»", "“What happened” ≠ “what will happen if…”"), t("для решений о бюджете — тест", "budget decisions need a test"))]
    r = "".join(f'<div class="rule" style="--k:var(--{c})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>' for i, (c, h, d) in enumerate(rules))
    return dict(min=2, html=f'''
  {head(t("Итоги", "Summary"), t("Пять правил анализа с ИИ", "Five rules for analysis with AI"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:50px;align-items:center;">
      <div class="rules" style="gap:24px;">{r}</div>
      <div class="plaque">{t("<b>Следующий урок — L09:</b> экосистема Claude и артефакты — как превратить анализ в интерактивную страницу или мини-приложение.", "<b>Next lesson — L09:</b> the Claude ecosystem and artifacts — turning an analysis into an interactive page or mini app.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 2 мин. Пять правил — это и есть урок. ИИ делает анализ разговорным, но не отменяет дисциплину: вопрос, профиль, код, проверка и честная граница вывода.",
                      "⏱ 2 min. Five rules — that is the lesson. AI makes analysis conversational but does not remove discipline: question, profile, code, checking and an honest limit to the claim."),
                    t("Тизер L09: в Claude результат анализа можно сразу превратить в артефакт — интерактивный дашборд, который открывается по ссылке. Вопросы.",
                      "L09 teaser: in Claude the analysis result can become an artifact — an interactive dashboard you open by link. Questions.")))


SLIDES = [s_cover, s_hook, s_loop, s_where, s_data, s_profile, s_fix, s_prompt, s_break, s_demo,
          s_results, s_charts, s_verify, s_causal, s_code, s_privacy, s_hw, s_summary]


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
    title = t("Урок 08: ИИ для анализа данных | GenAI Basics", "Lesson 08: AI for Data Analysis | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<!-- generated by deck/build.py — edit the generator, not this file -->
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
