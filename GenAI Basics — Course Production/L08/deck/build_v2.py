# -*- coding: utf-8 -*-
"""Build the L08 decks (RU + EN) and their PDFs — version 2 (2026-10-17).

    python build_v2.py          # HTML + PDF for both languages
    python build_v2.py --no-pdf # HTML only

Same engine as L05/deck_v2: every slide is one function, text is t("ru", "en").
Numbers and charts are computed at build time from ../demo_v2/northstar_sales_2025.csv
(truth: ../demo_v2/answers.md) and ../demo_v2/channels/results/*.csv (channel database sample).
Real screenshots: ../assets/v2/chat/ (ChatGPT run on the Northstar 2025 workbook, Oct 2026), cropped by make_shots.py.
Slide map and reasoning: ../L08_11_Method_Review_2026-10-17.md. v1 (73-row CSV deck) is in git history.
"""
import csv
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
L08 = HERE.parent
NAME = "presentation_L08_AI_for_Data_Analysis"
OUT = {"ru": L08 / f"{NAME}_v2.html", "en": L08 / f"{NAME}_EN_v2.html"}
IMG = "assets/"
SHOT = "assets/v2/shots/"
BUFFER = 0  # 85 min of content + 5 min break

LANG = "ru"


def t(ru, en):
    return ru if LANG == "ru" else en


FOOT = {"ru": "GenAI Basics • Урок 08 • ИИ для анализа данных", "en": "GenAI Basics • Lesson 08 • AI for Data Analysis"}

# ---------------------------------------------------------------- data (computed, not typed)
RAW = list(csv.DictReader((L08 / "demo_v2" / "northstar_sales_2025.csv").open(encoding="utf-8")))


def _date(d):
    if "-" in d:
        return d
    dd, mm, yy = d.split("/")
    return f"{yy}-{mm}-{dd}"


_seen, SALES = set(), []
for _r in RAW:
    _k = tuple(_r.values())
    if _k in _seen:
        continue
    _seen.add(_k)
    _c = dict(_r)
    _c["m"] = int(_date(_c["order_date"])[5:7])
    for _f in ("orders", "revenue", "ad_spend", "returns"):
        _c[_f] = float(_c[_f] or 0)
    SALES.append(_c)
TEXT_DATE = next(r["order_date"] for r in RAW if "-" not in r["order_date"])
M12 = list(range(1, 13))
CHANNELS = ["Search", "Social", "Email", "Organic"]
CATS = ["Electronics", "Home", "Sports", "Books"]
REGIONS = ["North", "South", "West", "Central"]
MONTHLY = {m: sum(r["revenue"] for r in SALES if r["m"] == m) for m in M12}
TOTAL = sum(MONTHLY.values())
TOTAL_RAW = sum(float(r["revenue"]) for r in RAW)
REV = defaultdict(float)
SPEND = defaultdict(float)
for _r in SALES:
    REV[(_r["channel"], _r["m"])] += _r["revenue"]
    SPEND[(_r["channel"], _r["m"])] += _r["ad_spend"]
ROAS = {c: {m: REV[(c, m)] / SPEND[(c, m)] for m in M12} for c in ("Search", "Social")}
SOC_SP_H1 = sum(SPEND[("Social", m)] for m in range(1, 7))
SOC_SP_H2 = sum(SPEND[("Social", m)] for m in range(7, 13))
SOC_RV_H1 = sum(REV[("Social", m)] for m in range(1, 7))
SOC_RV_H2 = sum(REV[("Social", m)] for m in range(7, 13))


def _rr(rows):
    o = sum(r["orders"] for r in rows)
    return sum(r["returns"] for r in rows) / o * 100 if o else 0


RET = {(g, c): _rr([r for r in SALES if r["m"] >= 9 and r["region"] == g and r["category"] == c]) for g in REGIONS for c in CATS}
N2_M = {m: _rr([r for r in SALES if r["m"] == m and r["warehouse"] == "N2"]) for m in M12}
REST_M = {m: _rr([r for r in SALES if r["m"] == m and r["warehouse"] != "N2"]) for m in M12}
CAT_REV = {c: sum(r["revenue"] for r in SALES if r["category"] == c) for c in CATS}
QSHARE = {q: {c: sum(REV[(c, m)] for m in range(q * 3 - 2, q * 3 + 1)) for c in CHANNELS} for q in (1, 2, 3, 4)}
ROW_RR = [r["returns"] / r["orders"] * 100 for r in SALES if r["orders"] > 0]
DEC_JAN = (MONTHLY[12] / MONTHLY[1] - 1) * 100
DEC_NOV = (MONTHLY[12] / MONTHLY[11] - 1) * 100
ND_SHARE = (MONTHLY[11] + MONTHLY[12]) / TOTAL * 100
# guard rails: the slides must agree with demo_v2/answers.md
assert len(RAW) == 1261 and len(SALES) == 1260, (len(RAW), len(SALES))
assert round(TOTAL) == 2520078 and round(TOTAL_RAW, 1) == 2523968.5, (TOTAL, TOTAL_RAW)
assert round(DEC_JAN, 1) == 161.7 and round(DEC_NOV, 1) == 15.1, (DEC_JAN, DEC_NOV)
assert round(RET[("North", "Electronics")], 1) == 24.8, RET[("North", "Electronics")]

MN = {"ru": ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"],
      "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}

# channel database sample (demo_v2/channels/) — filled in by s_db from its results files
DB = L08 / "demo_v2" / "channels"


def money(x, d=0):
    s = f"{x:,.{d}f}"
    return "$" + (s.replace(",", "\u202f") if LANG == "ru" else s)


def dec(x, n=1):
    return f"{x:.{n}f}".replace(".", "," if LANG == "ru" else ".")


def num(x):
    s = f"{x:,.0f}"
    return s.replace(",", "\u202f") if LANG == "ru" else s


def kk(x):
    return dec(x / 1000, 0) + t("\u00a0тыс.", "k")


def pc(x, n=1, sign=False):
    s = (f"{x:+.{n}f}" if sign else f"{x:.{n}f}").replace("-", "−")
    s = s.replace(".", ",") if LANG == "ru" else s
    return s + t("\u00a0%", "%")


# ---------------------------------------------------------------- helpers
def head(kicker, title, lead=None, k=None):
    ks = f' style="--k:var(--{k})"' if k else ""
    s = f'<div class="kicker"{ks}>{kicker}</div>\n  <h2 class="title">{title}</h2>'
    if lead:
        s += f'\n  <div class="lead">{lead}</div>'
    return s


def notes(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


def shot(name, label=None, k="cyan", cls="", style="", h=None):
    lb = f'<div class="lbl" style="--k:var(--{k})">{label}</div>' if label else ""
    ims = f' style="max-height:{h}px"' if h else ""
    return f'<div class="shot {cls}" style="--k:var(--{k});{style}">{lb}<img src="{SHOT}{name}.jpg" alt=""{ims}></div>'


def pr(no, text, k="cyan", cls=""):
    n = f'<span class="no">{no}</span>' if no else ""
    return f'<div class="pr {cls}" style="--k:var(--{k})">{n}{text}</div>'


EN_SHOTS = t("", " Screens are from the Russian-language run; the English file gives the same result.")

ARROW = ('<defs><marker id="{id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0 0 L10 5 L0 10 Z" fill="{c}"/></marker></defs>')
ICON = {
    "grid": '<rect x="5" y="7" width="38" height="34" rx="3"/><path d="M5 18 h38 M5 29 h38 M18 7 v34 M31 7 v34"/>',
    "chat": '<path d="M7 10 h34 a3 3 0 0 1 3 3 v18 a3 3 0 0 1 -3 3 H20 l-8 7 v-7 H7 a3 3 0 0 1 -3 -3 V13 a3 3 0 0 1 3 -3 z"/><path d="M13 19 h22 M13 25 h14"/>',
    "db": '<ellipse cx="24" cy="10" rx="16" ry="5"/><path d="M8 10 v28 c0 3 7 5 16 5 s16-2 16-5 V10 M8 24 c0 3 7 5 16 5 s16-2 16-5"/>',
    "sheet": '<path d="M11 4 h18 l10 10 v30 H11 z M29 4 v10 h10"/><path d="M16 24 h18 M16 31 h18 M16 38 h18 M25 20 v22"/>',
    "export": '<path d="M24 6 v24 M14 20 l10 10 l10 -10"/><path d="M8 32 v8 h32 v-8"/>',
    "api": '<path d="M16 14 l-10 10 l10 10 M32 14 l10 10 l-10 10 M27 9 l-6 30"/>',
    "web": '<circle cx="24" cy="24" r="18"/><path d="M6 24 h36 M24 6 c-8 8 -8 28 0 36 M24 6 c8 8 8 28 0 36"/>',
}


def icon(name, size=48, color="var(--cyan)"):
    return (f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>')


# ---------------------------------------------------------------- charts (static SVG from the data)
GRID, AX, MUT, FG = "#2b3648", "#6b7a90", "#a3b1c4", "#f1f5f9"
C = {"cyan": "#38bdf8", "green": "#34d399", "amber": "#fbbf24", "red": "#f87171", "violet": "#c084fc", "grey": "#5f6e84"}


def line_chart(series, w, h, ymax, ticks, tickfmt, pad=(70, 24, 30, 40), labels=True, fs=17):
    """series: list of (values by month list, colour, width, label at end or None)."""
    pl, pr_, pt, pb = pad
    xs = [pl + i * (w - pl - pr_) / 11 for i in range(12)]

    def y(v):
        return pt + (1 - v / ymax) * (h - pt - pb)
    out = ""
    for v in ticks:
        out += (f'<line x1="{pl}" y1="{y(v):.1f}" x2="{w - pr_}" y2="{y(v):.1f}" stroke="{GRID}" stroke-width="1"/>'
                f'<text x="{pl - 10}" y="{y(v) + 6:.1f}" text-anchor="end" font-size="{fs}" fill="{AX}">{tickfmt(v)}</text>')
    if labels:
        out += "".join(f'<text x="{x:.1f}" y="{h - pb + 26}" text-anchor="middle" font-size="{fs}" fill="{MUT}">{MN[LANG][i]}</text>'
                       for i, x in enumerate(xs))
    for vals, col, sw, _ in series:
        pts = " ".join(f"{x:.1f},{y(v):.1f}" for x, v in zip(xs, vals))
        out += f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"/>'
        out += "".join(f'<circle cx="{x:.1f}" cy="{y(v):.1f}" r="{sw + 1}" fill="#0b0f17" stroke="{col}" stroke-width="{max(2, sw - 1)}"/>'
                       for x, v in zip(xs, vals))
    return out, xs, y


def s6_chart(w=1000, h=520):
    vals = [MONTHLY[m] for m in M12]
    out, xs, y = line_chart([(vals, C["cyan"], 4, None)], w, h, 400000, [0, 100000, 200000, 300000, 400000],
                            lambda v: f"{v // 1000:.0f}" + t(" тыс.", "k"), pad=(96, 60, 40, 44))
    for i, dx, anc in ((0, 0, "start"), (11, -6, "end")):
        out += (f'<text x="{xs[i] + dx:.1f}" y="{y(vals[i]) - 18:.1f}" text-anchor="{anc}" font-size="21" font-weight="700" fill="{FG}">'
                f'{money(vals[i] / 1000)}{t(" тыс.", "k")}</text>')
    # Jan -> Dec: dashed amber baseline from January; Nov -> Dec: thick green segment
    yj, yd, yn = y(vals[0]), y(vals[11]), y(vals[10])
    out += (f'<line x1="{xs[0]:.1f}" y1="{yj:.1f}" x2="{xs[11]:.1f}" y2="{yj:.1f}" stroke="{C["amber"]}" stroke-width="2" stroke-dasharray="7 6"/>'
            f'<line x1="{xs[11] + 22:.1f}" y1="{yj:.1f}" x2="{xs[11] + 22:.1f}" y2="{yd:.1f}" stroke="{C["amber"]}" stroke-width="3"/>'
            f'<text x="{xs[7]:.1f}" y="{yj + 34:.1f}" text-anchor="middle" font-size="24" font-weight="800" fill="{C["amber"]}">{pc(DEC_JAN, sign=True)} {t("от уровня января", "from the January level")}</text>'
            f'<line x1="{xs[10]:.1f}" y1="{yn:.1f}" x2="{xs[11]:.1f}" y2="{yd:.1f}" stroke="{C["green"]}" stroke-width="7" stroke-linecap="round"/>'
            f'<text x="{xs[10] - 18:.1f}" y="{yn - 4:.1f}" text-anchor="end" font-size="24" font-weight="800" fill="{C["green"]}">{pc(DEC_NOV, sign=True)} {t("к ноябрю", "vs November")}</text>')
    return f'<svg class="dia" viewBox="0 0 {w} {h}">{out}</svg>'


def mini_line(w=300, h=250):
    vals = [MONTHLY[m] for m in M12]
    out, xs, y = line_chart([(vals, C["cyan"], 3, None)], w, h, 400000, [0, 200000, 400000],
                            lambda v: f"{v // 1000:.0f}" + t("т", "k"), pad=(44, 8, 10, 24), labels=False, fs=14)
    out += (f'<text x="{xs[0]:.1f}" y="{h - 6}" text-anchor="start" font-size="15" fill="{MUT}">{MN[LANG][0]}</text>'
            f'<text x="{xs[11]:.1f}" y="{h - 6}" text-anchor="end" font-size="15" fill="{MUT}">{MN[LANG][11]}</text>')
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def mini_bar(w=300, h=250):
    cats = sorted(CATS, key=CAT_REV.get, reverse=True)
    mx = max(CAT_REV.values())
    out = f'<line x1="10" y1="{h - 30}" x2="{w - 6}" y2="{h - 30}" stroke="{GRID}" stroke-width="2"/>'
    bw = (w - 30) / 4
    for i, c in enumerate(cats):
        bh = CAT_REV[c] / mx * (h - 56)
        x = 16 + i * bw
        col = C["cyan"] if i == 0 else C["grey"]
        out += (f'<rect x="{x:.1f}" y="{h - 30 - bh:.1f}" width="{bw - 16:.1f}" height="{bh:.1f}" rx="3" fill="{col}"/>'
                f'<text x="{x + (bw - 16) / 2:.1f}" y="{h - 34 - bh:.1f}" text-anchor="middle" font-size="13" fill="{FG}">{kk(CAT_REV[c])}</text>'
                f'<text x="{x + (bw - 16) / 2:.1f}" y="{h - 10}" text-anchor="middle" font-size="14" fill="{MUT}">{ {"Electronics": "Electr."}.get(c, c)}</text>')
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def mini_hist(w=300, h=250):
    edges = list(range(0, 40, 2))
    cnt = [sum(1 for v in ROW_RR if a <= v < a + 2) for a in edges]
    cnt[-1] += sum(1 for v in ROW_RR if v >= edges[-1] + 2)
    mx = max(cnt)
    bw = (w - 20) / len(cnt)
    out = f'<line x1="10" y1="{h - 26}" x2="{w - 6}" y2="{h - 26}" stroke="{GRID}" stroke-width="2"/>'
    for i, n in enumerate(cnt):
        bh = max(2, n / mx * (h - 50)) if n else 0
        col = C["red"] if edges[i] >= 14 else C["cyan"]
        out += f'<rect x="{12 + i * bw:.1f}" y="{h - 26 - bh:.1f}" width="{bw - 3:.1f}" height="{bh:.1f}" fill="{col}"/>'
    out += (f'<text x="12" y="{h - 6}" font-size="13" fill="{MUT}">0%</text>'
            f'<text x="{w - 8}" y="{h - 6}" text-anchor="end" font-size="13" fill="{MUT}">40%+</text>')
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def mini_scatter(w=300, h=250):
    pts = [(SPEND[("Search", m)], REV[("Search", m)], C["grey"]) for m in M12]
    pts += [(SPEND[("Social", m)], REV[("Social", m)], C["cyan"] if m <= 6 else C["amber"]) for m in M12]
    mx_x, mx_y = 55000, 125000
    out = (f'<line x1="30" y1="{h - 24}" x2="{w - 6}" y2="{h - 24}" stroke="{GRID}" stroke-width="2"/>'
           f'<line x1="30" y1="8" x2="30" y2="{h - 24}" stroke="{GRID}" stroke-width="2"/>')
    for x, y, col in pts:
        out += f'<circle cx="{30 + x / mx_x * (w - 40):.1f}" cy="{h - 24 - y / mx_y * (h - 36):.1f}" r="5" fill="{col}"/>'
    out += (f'<text x="{w - 6}" y="{h - 6}" text-anchor="end" font-size="13" fill="{MUT}">{t("расход →", "spend →")}</text>'
            f'<text x="36" y="20" font-size="13" fill="{MUT}">{t("выручка", "revenue")}</text>')
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def mini_stack(w=300, h=250):
    cols = {"Search": C["cyan"], "Social": C["amber"], "Email": C["green"], "Organic": C["violet"]}
    out = ""
    bw = (w - 30) / 4
    for i, q in enumerate((1, 2, 3, 4)):
        tot = sum(QSHARE[q].values())
        yy = h - 26
        for c in CHANNELS:
            hh = QSHARE[q][c] / tot * (h - 40)
            yy -= hh
            out += f'<rect x="{16 + i * bw:.1f}" y="{yy:.1f}" width="{bw - 18:.1f}" height="{hh:.1f}" fill="{cols[c]}" opacity=".9"/>'
        out += f'<text x="{16 + i * bw + (bw - 18) / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="13" fill="{MUT}">Q{q}</text>'
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def bars_month(vals, col_fn, w, h, ymax, fmt, hl_label=None):
    out = f'<line x1="10" y1="{h - 30}" x2="{w - 6}" y2="{h - 30}" stroke="{GRID}" stroke-width="2"/>'
    bw = (w - 20) / 12
    for i, v in enumerate(vals):
        bh = v / ymax * (h - 60)
        x = 12 + i * bw
        out += (f'<rect x="{x:.1f}" y="{h - 30 - bh:.1f}" width="{bw - 8:.1f}" height="{bh:.1f}" rx="3" fill="{col_fn(i)}"/>'
                f'<text x="{x + (bw - 8) / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="15" fill="{MUT}">{MN[LANG][i]}</text>')
        if i in (0, 6, 11):
            out += f'<text x="{x + (bw - 8) / 2:.1f}" y="{h - 36 - bh:.1f}" text-anchor="middle" font-size="16" font-weight="700" fill="{FG}">{fmt(v)}</text>'
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def n2_chart(w=660, h=300):
    out, xs, y = line_chart([([REST_M[m] for m in M12], C["grey"], 3, None), ([N2_M[m] for m in M12], C["red"], 4, None)],
                            w, h, 30, [0, 10, 20, 30], lambda v: f"{v:.0f}%", pad=(56, 20, 16, 36), fs=15)
    out += (f'<text x="{xs[8] - 12:.1f}" y="{y(25):.1f}" text-anchor="end" font-size="18" font-weight="700" fill="{C["red"]}">{t("склад N2", "warehouse N2")}</text>'
            f'<text x="{xs[11]:.1f}" y="{y(REST_M[12]) - 12:.1f}" text-anchor="end" font-size="17" fill="{MUT}">{t("остальные склады", "other warehouses")}</text>')
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


# ---------------------------------------------------------------- slides
def s_cover():
    return dict(min=1, cls="cover", html=f'''
  <div class="bg"><img class="full" src="{IMG}l08_cover_hero.png" alt=""></div>
  <div class="shade soft"></div>
  <div class="txt">
    <div class="kicker">{t("GenAI Basics • Урок 08 • Модуль 3: ИИ-ассистенты в работе", "GenAI Basics • Lesson 08 • Module 3: AI assistants at work")}</div>
    <h1>{t("ИИ для анализа данных", "AI for Data Analysis")}</h1>
    <h2>{t("Таблица → ответ → график → страница отчёта", "Spreadsheet → answer → chart → one-page report")}</h2>
    <p>{t("Формулы, сводные и графики по просьбе обычными словами — в Excel, Google Таблицах или в чате с файлом. Учебный кейс — продажи интернет-магазина Northstar за 2025 год.",
           "Formulas, pivots and charts on request in plain words — in Excel, Google Sheets or a chat with a file. Case study: Northstar online shop sales for 2025.")}</p>
  </div>
  <div class="keys">{t("← → листать • N заметки спикера • G все слайды • F полный экран", "← → navigate • N speaker notes • G all slides • F fullscreen")}</div>''',
                notes=notes(
                    t("⏱ 2 мин. Сегодня берём обычную таблицу продаж и за урок получаем из неё формулы, сводную, три графика и страницу отчёта для руководителя. Делаем это в тех инструментах, что у вас уже есть.",
                      "⏱ 2 min. Today we take an ordinary sales spreadsheet and turn it into formulas, a pivot, three charts and a one-page report for a manager — using tools you already have."),
                    t("Весь урок на одном файле: продажи вымышленного магазина Northstar за 2025 год, 1 261 строка и лист отзывов. В конце — короткий пример с большой базой YouTube-каналов, которая в Excel уже не помещается.",
                      "The whole lesson uses one file: sales of a made-up shop, Northstar, for 2025 — 1,261 rows plus a reviews sheet. Near the end, a short example with a large YouTube channel database that no longer fits in Excel.")))


def s_hook():
    return dict(min=2, html=f'''
  {head(t("Часть 2 • Excel и первый вопрос", "Part 2 • Excel and the first question"), t("Три вопроса письма — три части урока", "Three questions in the e-mail — three parts of the lesson"), k="amber")}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:0.85fr 1.15fr;gap:36px;align-items:center;">
      <div class="stack" style="gap:16px;">
        <div class="chk" style="--k:var(--green)"><div class="n">1</div><div class="t">{t("Что с продажами за год?", "How did sales go this year?")}<small>{t("Часть 2: Excel, формулы, сезонность", "Part 2: Excel, formulas, seasonality")}</small></div></div>
        <div class="chk" style="--k:var(--amber)"><div class="n">2</div><div class="t">{t("Почему реклама хуже окупается?", "Why does advertising pay off worse?")}<small>{t("Часть 2–3: отдача Search и Social", "Parts 2–3: Search and Social return")}</small></div></div>
        <div class="chk" style="--k:var(--red)"><div class="n">3</div><div class="t">{t("Откуда возвраты осенью?", "Why the autumn returns?")}<small>{t("Часть 3: таблица + текст отзывов", "Part 3: the table + review text")}</small></div></div>
      </div>
      <div class="stack" style="gap:6px;">
        {shot("p2_sales_sheet", t("northstar_2025.xlsx • 1 261 строка • лист Reviews: 357 отзывов", "northstar_2025.xlsx • 1,261 rows • Reviews sheet: 357 reviews"), k="cyan", h=470)}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Так анализ выглядит в жизни: письмо с вопросами и файл-выгрузка. Справа настоящий файл урока, открытый в ChatGPT: 1 261 строка продаж за 2025 год и лист с отзывами.",
                      "⏱ 3 min. This is what analysis looks like at work: an e-mail with questions and an exported file. On the right is the real lesson file opened in ChatGPT: 1,261 sales rows for 2025 and a reviews sheet."),
                    t("В письме три конкретных вопроса: год в целом, отдача рекламы во втором полугодии, возвраты осенью. Каждый вопрос потом станет одним графиком. Мы весь урок отвечаем Анне.",
                      "The e-mail has three specific questions: the year overall, ad return in the second half, autumn returns. Each will become one chart. We spend the lesson answering Anna."),
                    t("Вопрос в чат Teams: «Какой вопрос из письма вы бы проверили первым и почему?» Соберите 2–3 ответа.",
                      "Ask the Teams chat: “Which question from the e-mail would you check first, and why?” Collect 2–3 answers.")))


def s_first():
    return dict(min=2, html=f'''
  {head(t("Часть 2 • ответ на промпт 1", "Part 2 • the answer to prompt 1"), t("Что ответила модель: что верно, что нет и какой вопрос берём", "What the model answered: what is right, what isn’t, which question we take"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:26px;align-items:stretch;">
      <div class="stack" style="gap:14px;">
        {pr(t("Промпт", "Prompt"), t("Опиши этот файл: что такое одна строка, сколько строк, какой период, какие проблемы в данных. Предложи 5 вопросов, которые задал бы руководитель. Ничего пока не меняй.",
                                       "Describe this file: what one row is, how many rows, what period, what data problems. Suggest 5 questions a manager would ask. Don’t change anything yet."), cls="lg")}
        {shot("p1_problems", t("Ответ ChatGPT • часть 1", "ChatGPT answer • part 1"), k="cyan")}
      </div>
      <div class="stack" style="gap:14px;">
        {shot("p1_questions", t("Ответ ChatGPT • часть 2", "ChatGPT answer • part 2"), k="cyan")}
        <div class="note" style="--k:var(--green)">{t("Модель нашла дубль и период и сказала: <b>«Файл не изменял»</b>. А нули в рекламе приняла за пропуски — это первый вопрос владельцу данных.", "The model found the duplicate and the period and said: <b>“I did not change the file”</b>. But it took zero ad spend for missing values — that is the first question for the data owner.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Берём вопрос 1 про каналы с учётом рекламы — он совпадает с письмом. Его и считаем в демо.", "We take question 1, channels including ad spend — it matches the e-mail. That is what the demo computes.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Это первый промпт к любому файлу. Он делает две вещи: модель описывает, что лежит в таблице, и предлагает вопросы. Фраза «ничего пока не меняй» важна: без неё модель может молча удалить дубли или заполнить пустые ячейки, и вы не узнаете, что она поменяла.",
                      "⏱ 4 min. This is the first prompt for any file. It does two things: the model describes what is in the table and suggests questions. “Don’t change anything yet” matters: without it the model may quietly drop duplicates or fill blanks, and you won’t know what it changed."),
                    t("Слева реальный ответ: 1 261 строка, период с 1 января по 31 декабря 2025, одна полностью повторяющаяся строка. Справа пять вопросов руководителя. Первый, про каналы с учётом рекламных расходов, совпадает с письмом Анны: его считаем в демо 1. Третий, про возвраты, — в демо 2.",
                      "Left: the real answer — 1,261 rows, 1 Jan to 31 Dec 2025, one fully duplicated row. Right: five manager questions. The first, about channels including ad spend, matches Anna’s e-mail: Demo 1 computes it. The third, about returns, is Demo 2."),
                    t("Модель ошиблась: написала «отсутствуют 632 значения ad_spend». В файле там нули: у Email и Organic рекламы нет. Ещё она не заметила дату текстом 10/05/2025. Переспросите: «Это пропуски или нули? Есть ли даты в другом формате?» Что значат нули, знает владелец данных." + EN_SHOTS,
                      "The model got it wrong: it said “632 ad_spend values are missing”. The file has zeros there: Email and Organic have no advertising. It also missed the text date 10/05/2025. Ask back: “Are these missing or zeros? Any dates in another format?” The data owner knows what the zeros mean." + EN_SHOTS)))


def s_doors():
    doors = [("green", "grid", t("Excel", "Excel"), t("Данные уже в книге. ИИ пишет <b>формулы и сводные</b> — их видно в ячейках.", "Data already lives in a workbook. AI writes <b>formulas and pivots</b> you can see in the cells."), t("Claude / Copilot в Excel или файл из чата", "Claude / Copilot in Excel, or a file from a chat")),
             ("cyan", "sheet", t("Google Таблицы", "Google Sheets"), t("Файл живёт в Google Диске. Gemini в боковой панели строит <b>сводные и графики</b>.", "The file lives in Google Drive. Gemini in the side panel builds <b>pivots and charts</b>."), t("Gemini в Таблицах", "Gemini in Sheets")),
             ("violet", "chat", t("Чат с файлом", "Chat with a file"), t("Загрузили CSV или XLSX. Модель пишет <b>код на Python</b>, программа считает, вы видите код.", "Upload a CSV or XLSX. The model writes <b>Python code</b>, a program runs it, and you see the code."), t("ChatGPT · Claude · Gemini", "ChatGPT · Claude · Gemini")),
             ("amber", "db", t("База данных", "Database"), t("Миллионы строк, в чат не влезут. Модель пишет <b>запрос SQL</b>, база считает сама.", "Millions of rows that won’t fit in a chat. The model writes <b>an SQL query</b>, the database does the counting."), t("SQL + ИИ-ассистент", "SQL + an AI assistant"))]
    d = "".join(f'<div class="door" style="--k:var(--{k})">{icon(ic, 52, f"var(--{k})")}<div class="h">{h}</div><div class="w">{w}</div><div class="o">{o}</div></div>' for k, ic, h, w, o in doors)
    return dict(min=4, html=f'''
  {head(t("Где анализировать", "Where to analyse"), t("Выбирайте инструмент по тому, где лежат данные", "Pick the tool by where the data lives"), t("Внутри всегда одно и то же: модель пишет формулу, код или запрос, а считает программа. Поэтому ход расчёта можно открыть и проверить.", "Inside it is always the same: the model writes a formula, code or a query, and a program does the counting. That is why you can open and check the working."))}
  <div class="body" style="margin-top:10px;">
    <div class="doors">{d}</div>
    <div class="flow" style="margin-top:30px;justify-content:center;gap:16px;">
      <div class="box">{t("ваш вопрос", "your question")}<small>{t("обычными словами", "in plain words")}</small></div><div class="arr">→</div>
      <div class="box k" style="--k:var(--violet)">{t("модель пишет", "the model writes")}<small>{t("формулу · код · SQL", "formula · code · SQL")}</small></div><div class="arr">→</div>
      <div class="box k" style="--k:var(--green)">{t("программа считает", "a program counts")}<small>{t("Excel · Python · база", "Excel · Python · database")}</small></div><div class="arr">→</div>
      <div class="box hl" style="--k:var(--amber)">{t("вы открываете и проверяете", "you open and check")}<small>{t("ячейку · код · запрос", "the cell · code · query")}</small></div>
    </div>
    <div class="cap" style="margin-top:18px;text-align:center;">{t("Сегодня в демо: Excel и чат с файлом. Пример с базой каналов — на слайде 13.", "In today’s demos: Excel and a chat with a file. The channel database example is on slide 13.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Четыре места, где ИИ помогает с данными. Выбор простой: где лежит файл и что нужно на выходе.",
                      "⏱ 4 min. Four places where AI helps with data. The choice is simple: where does the file live, and what do you need at the end?"),
                    t("Excel: если данные уже в книге и коллеги будут её открывать. ИИ пишет формулы, их видно в строке формул. Панели ИИ: Claude for Excel (платные тарифы Claude), Copilot в Excel (лицензия Microsoft 365 Copilot), ChatGPT for Excel. Если панели нет, работает обходной путь из демо: файл в чат, книгу с формулами скачиваем обратно.",
                      "Excel: when the data is already in a workbook that colleagues open. AI writes formulas you can see in the formula bar. AI panels: Claude for Excel (paid Claude plans), Copilot in Excel (Microsoft 365 Copilot licence), ChatGPT for Excel. Without a panel, the demo workaround works: upload the file to a chat and download a workbook with formulas."),
                    t("Google Таблицы: Gemini в боковой панели умеет сводные, графики и формулы, если у компании Google Workspace с Gemini. Чат с файлом: самый быстрый старт, виден код. База данных: когда строк миллионы. Её покажем на слайде 13.",
                      "Google Sheets: Gemini in the side panel does pivots, charts and formulas if the company has Google Workspace with Gemini. Chat with a file: the fastest start, and you see the code. Database: when there are millions of rows — slide 13."),
                    t("Как узнать, есть ли у вас Copilot в Excel: на вкладке «Главная» справа есть кнопка Copilot. Названия кнопок и тарифы меняются, сверяйтесь в день занятия.",
                      "To check whether you have Copilot in Excel: look for the Copilot button on the right of the Home tab. Button names and plans change, so check on the day.")))


def s_demo1():
    return dict(min=5, html=f'''
  {head(t("Демо 1 вживую • 5 минут", "Demo 1 live • 5 minutes"), t("Повторяем всё вживую: от файла до формулы в ячейке", "We do it live: from the file to a formula in a cell"), k="green")}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:1.15fr 1fr;gap:36px;align-items:center;">
      <ol class="checklist lg">
        <li><span>{t("<b>Загрузить</b> northstar_2025.xlsx в ChatGPT", "<b>Upload</b> northstar_2025.xlsx to ChatGPT")}</span></li>
        <li><span>{t("<b>Промпт 1</b> — опись файла (слайд 11)", "<b>Prompt 1</b> — describe the file (slide 11)")}</span></li>
        <li><span>{t("<b>Промпт 2</b> — лист «Отдача рекламы» (слайд 13)", "<b>Prompt 2</b> — the “Ad return” sheet (slide 13)")}</span></li>
        <li><span>{t("<b>Скачать</b> книгу и открыть в Excel", "<b>Download</b> the workbook and open it in Excel")}</span></li>
        <li><span>{t("<b>Щёлкнуть</b> ячейку с отдачей: число → «замени числа формулами»", "<b>Click</b> an ad-return cell: a number → “replace the numbers with formulas”")}</span></li>
        <li><span>{t("<b>Не успели?</b> Показываем готовые кадры со слайда 14", "<b>Out of time?</b> Show the ready frames from slide 14")}</span></li>
      </ol>
      <div class="stack" style="gap:16px;">
        <div class="plaque g">{t("<b>Что должно получиться:</b> у Search около 5 долларов выручки на доллар рекламы весь год, у Social с июля около 2.", "<b>What you should get:</b> Search earns about $5 per ad dollar all year; Social drops to about $2 from July.")}</div>
        <div class="note" style="--k:var(--cyan)">{t("Есть Claude или Copilot в Excel? Тот же промпт 2 — в боковой панели, без скачивания.", "Have Claude or Copilot in Excel? The same prompt 2 in the side panel, no download.")}</div>
        <div class="note" style="--k:var(--amber)">{t("Ответ дольше 90 секунд — показываем кадр и идём дальше.", "Answer takes over 90 seconds — show the frame and move on.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин (2 промпта + открыть книгу; разбор был на слайдах 11–14). Ведите по ранбуку L08_04. Загрузите northstar_2025.xlsx в ChatGPT. Шаги на слайде, тексты промптов — в ранбуке и на слайдах 11 и 13.",
                      "⏱ 5 min (2 prompts + open the workbook; the walkthrough was slides 11–14). Follow runbook L08_04. Upload northstar_2025.xlsx to ChatGPT. Steps are on the slide; prompt texts are in the runbook and on slides 11 and 13."),
                    t("Ключевые слова в промпте: «формулами Excel, а не готовыми числами». Без них модель часто вставляет посчитанные значения, и проверить их в книге нельзя. Скачайте файл, откройте в Excel, щёлкните ячейку с отдачей рекламы. В строке формул должно быть деление выручки на расход, например =B2/C2. Выручка и расход тоже должны быть формулами (СУММЕСЛИМН / SUMIFS по листу Sales).",
                      "Key words in the prompt: “Excel formulas, not pasted numbers”. Without them the model often pastes computed values, which can’t be checked in the workbook. Download the file, open it in Excel and click an ad-return cell. The formula bar should show revenue divided by spend, e.g. =B2/C2. Revenue and spend should be formulas too (SUMIFS over the Sales sheet)."),
                    t(f"Что увидим: у Search выручка на $1 рекламы держится около {dec(ROAS['Search'][1], 1)} весь год. У Social с июля падает примерно с 4 до 2. Это вторая история из письма Анны, к ней вернёмся после перерыва.",
                      f"What you will see: Search returns about {dec(ROAS['Search'][1], 1)} per $1 all year. Social drops from about 4 to 2 in July. That is the second story from Anna’s e-mail; we come back to it after the break."),
                    t("Готовые кадры для запасного пути — на слайде 14. Там реальный лист из книги, которую вернул ChatGPT: в нашем прогоне в ячейках оказались числа, формул не было. Внизу та же таблица в Excel, где выручка посчитана формулой СУММЕСЛИМН по листу Sales, а отдача — делением =B2/C2; рядом график по этим ячейкам. Так должна выглядеть книга после просьбы «замени числа формулами». Эталонная книга: demo_v2/excel_demo/northstar_2025_formulas.xlsx. Если у вас есть Claude for Excel или Copilot, покажите ту же просьбу в боковой панели, 90 секунд. Если сервис думает дольше 90 секунд — показывайте готовые кадры и идите дальше." + EN_SHOTS,
                      "Ready fallback frames are on slide 14: the real sheet from the workbook ChatGPT returned: in our run the cells held numbers, not formulas. Below is the same table in Excel where revenue is a SUMIFS over the Sales sheet and the return is =B2/C2, with a chart built on those cells. That is how the workbook should look after “replace the numbers with formulas”. Reference workbook: demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx. If you have Claude for Excel or Copilot, show the same request in the side panel, 90 seconds. If the service takes longer than 90 seconds, show the ready frames and move on." + EN_SHOTS)))


def s_season():
    return dict(min=3, html=f'''
  {head(t("Что увидели • сезонность", "What we saw • seasonality"), t(f"Рост за год: {pc(DEC_JAN, sign=True)} или {pc(DEC_NOV, sign=True)}? Зависит от базы", f"Growth this year: {pc(DEC_JAN, sign=True)} or {pc(DEC_NOV, sign=True)}? It depends on the base"), k="amber")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.55fr 1fr;gap:34px;align-items:center;">
      <div class="stack" style="gap:4px;">
        <div class="cap" style="font-size:21px;font-weight:700;color:var(--fg);">{t("Выручка Northstar по месяцам, 2025", "Northstar revenue by month, 2025")}</div>
        {s6_chart()}
      </div>
      <div class="stack" style="gap:20px;">
        <div class="stat" style="--k:var(--amber)"><div class="n">{pc(DEC_JAN, sign=True)}</div><div class="d">{t("декабрь к январю. Январь — самый слабый месяц года", "December vs January. January is the weakest month")}</div></div>
        <div class="stat" style="--k:var(--green)"><div class="n">{pc(DEC_NOV, sign=True)}</div><div class="d">{t("декабрь к ноябрю. Пик уже начался в ноябре", "December vs November. The peak already started in November")}</div></div>
        <div class="stat" style="--k:var(--cyan)"><div class="n">{pc(ND_SHARE)}</div><div class="d">{t("годовой выручки — в ноябре и декабре", "of annual revenue came in November and December")}</div></div>
        <div class="plaque">{t("<b>Спрашивайте:</b> процент от какого месяца и за какой период?", "<b>Ask:</b> a percentage of which month, over what period?")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 3 мин. Первая история файла: сезонность. Если сравнить декабрь с январём, рост {pc(DEC_JAN, sign=True)}. Если с ноябрём — {pc(DEC_NOV, sign=True)}. Оба числа верные, но звучат совсем по-разному.",
                      f"⏱ 3 min. The file’s first story: seasonality. December vs January: {pc(DEC_JAN, sign=True)}. December vs November: {pc(DEC_NOV, sign=True)}. Both numbers are right, but they sound very different."),
                    t("Модель охотно пишет «рост на 160 %». Ваша задача — спросить, от какой базы. Январь после праздников — самый слабый месяц, ноябрь и декабрь — распродажи. Это видно только на графике по месяцам, итог за год этого не покажет.",
                      "Models happily write “160% growth”. Your job is to ask: from what base? January after the holidays is the weakest month; November and December are sales season. Only the monthly chart shows this; the annual total doesn’t."),
                    t("График построен из файла урока при сборке колоды, числа совпадают с demo_v2/answers.md.",
                      "The chart is built from the lesson file when the deck is generated; numbers match demo_v2/answers.md.")))


def s_charts():
    soc_h1 = sum(ROAS["Social"][m] for m in range(1, 7)) / 6
    items = [(mini_line(), t("Как менялось во времени?", "How did it change over time?"), t("линия", "line"), t("пик в ноябре–декабре", "peak in Nov–Dec")),
             (mini_bar(), t("Кто больше?", "Which is bigger?"), t("столбцы по убыванию", "sorted bars"), t(f"{max(CAT_REV, key=CAT_REV.get)} — лидер по выручке", f"{max(CAT_REV, key=CAT_REV.get)} leads revenue")),
             (mini_hist(), t("Как распределены значения?", "How are values spread?"), t("гистограмма", "histogram"), t(f"красный хвост: {sum(1 for v in ROW_RR if v >= 14)} строк с возвратами от 14 %", f"red tail: {sum(1 for v in ROW_RR if v >= 14)} rows with 14%+ returns")),
             (mini_scatter(), t("Связаны ли два числа?", "Are two numbers related?"), t("точки", "scatter"), t("<b style=\"color:#5f6e84\">●</b> Search <b style=\"color:#38bdf8\">●</b> Social янв–июн <b style=\"color:#fbbf24\">●</b> Social июл–дек: расход вырос, выручка нет", "<b style=\"color:#5f6e84\">●</b> Search <b style=\"color:#38bdf8\">●</b> Social Jan–Jun <b style=\"color:#fbbf24\">●</b> Social Jul–Dec: spend up, revenue not")),
             (mini_stack(), t("Из чего состоит целое?", "What makes up the whole?"), t("столбцы 100 %", "100% bars"), t("доли выручки по кварталам: <b style=\"color:#38bdf8\">●</b> Search <b style=\"color:#fbbf24\">●</b> Social <b style=\"color:#34d399\">●</b> Email <b style=\"color:#c084fc\">●</b> Organic", "revenue shares by quarter: <b style=\"color:#38bdf8\">●</b> Search <b style=\"color:#fbbf24\">●</b> Social <b style=\"color:#34d399\">●</b> Email <b style=\"color:#c084fc\">●</b> Organic"))]
    m = "".join(f'<div class="chartbox"><div class="q">{q}</div><div class="c">{c}</div>{svg}<div class="f">{f}</div></div>' for svg, q, c, f in items)
    return dict(min=3, html=f'''
  {head(t("Часть 2 • графики", "Part 2 • charts"), t("Пять вопросов — пять графиков. Все из нашего файла", "Five questions, five charts — all from our file"))}
  <div class="body" style="margin-top:16px;">
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;">{m}</div>
    <div class="plaque" style="margin-top:22px;">{t("<b>Просите так:</b> «Построй один график, который отвечает на вопрос …, подпиши оси и единицы». Тип графика назовите сами, если знаете; иначе модель предложит.", "<b>Ask like this:</b> “Build one chart that answers …, label the axes and units.” Name the chart type if you know it; otherwise the model will suggest one.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Пять типовых вопросов и пять графиков к ним, все построены из файла Northstar. Время — линия: видно пик в конце года. Сравнение — столбцы по убыванию, ось от нуля. Распределение — гистограмма: у большинства строк возвраты 2–8 %, но есть хвост от 14 % и выше, это склад N2. Связь — точки: каждая точка — месяц одного канала, жёлтые точки Social со второго полугодия ушли вправо (расход больше), но не вверх. Доли — столбцы 100 %, не больше 4–5 частей.",
                      "⏱ 4 min. Five typical questions and a chart for each, all built from the Northstar file. Time — line: the year-end peak is visible. Comparison — sorted bars, axis from zero. Distribution — histogram: most rows have 2–8% returns, but there is a tail at 14% and above; that is warehouse N2. Relationship — scatter: each dot is one channel-month; Social’s amber second-half dots moved right (more spend) but not up. Shares — 100% bars, no more than 4–5 parts."),
                    t("ИИ охотно делает «дашборд из шести графиков». Просите один график под один вопрос, его проще проверить и показать.",
                      "AI happily makes a “six-chart dashboard”. Ask for one chart per question; it is easier to check and to present.")))


def s_break():
    return dict(min=5, html=f'''
  <div class="brk">
    <div class="kicker" style="--k:var(--amber)">{t("Перерыв", "Break")}</div>
    <h2 class="title">{t("5 минут", "5 minutes")}</h2>
    <div class="clock" id="clock">05:00</div>
    <div style="display:flex;gap:14px;"><button class="btn primary" id="timerStart">{t("СТАРТ 5 МИН", "START 5 MIN")}</button><button class="btn" id="timerReset">{t("СБРОС", "RESET")}</button></div>
    <p>{t("Дальше: демо в чате с файлом — возвраты, отзывы, график для слайда. Потом большая база, отчёт на одну страницу и домашнее задание.", "Next: a demo in a chat with a file — returns, reviews, a slide-ready chart. Then a large database, a one-page report and homework.")}</p>
  </div>''',
                notes=notes(t("⏱ 5 мин. Нажмите «Старт». Чат не закрывайте: после перерыва работаем в нём же, промпт 6 опирается на графики из демо 1 и 2.",
                              "⏱ 5 min. Press “Start”. Keep the chat open: after the break we continue in it, because prompt 6 builds on the charts from demos 1 and 2.")))


def s_demo2():
    steps = [("p3_heatmap", "violet", t("Промпт 3", "Prompt 3"), t("Посчитай долю возвратов по регионам и категориям за сентябрь–декабрь и покажи тепловой картой.", "Compute the return rate by region and category for September–December and show it as a heatmap.")),
             ("p3_themes_before", "violet", t("Промпт 4", "Prompt 4"), t("Для склада с самой высокой долей возвратов разложи отзывы на темы и сравни с остальными складами. Покажи 5 примеров отзывов.", "For the warehouse with the highest return rate, sort the reviews into themes and compare it with the other warehouses. Show 5 example reviews.")),
             ("p4_themes_after", "violet", t("Промпт 5", "Prompt 5"), t("Переделай этот график для слайда: заголовок — вывод, столбцы отсортированы, подписи значений на столбцах, без легенды и сетки, один акцентный цвет для N2, остальное серым. Объясни в 3 пунктах, что поменял.", "Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed."))]
    cols = (f'<div class="stack" style="gap:10px;">{pr(steps[0][2], steps[0][3], k="violet")}{shot(steps[0][0], t("тепловая карта", "heatmap"), k="violet", h=420)}</div>'
            f'<div class="stack" style="gap:10px;">{pr(steps[1][2], steps[1][3], k="violet")}{shot(steps[1][0], t("темы отзывов", "review themes"), k="violet")}'
            f'{pr(steps[2][2], t("Переделка графика для слайда. Полный текст и результат — на слайде 23.", "Rework the chart for a slide. Full text and result on slide 23."), k="violet")}</div>')
    return dict(min=4, html=f'''
  {head(t("Часть 3 • демо 2 • чат с файлом", "Part 3 • demo 2 • chat with a file"), t("За год 6 % возвратов. В одной клетке — 24,8 %", "6% returns for the year. One cell shows 24.8%"), k="violet")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:0.85fr 1.15fr;gap:26px;align-items:start;">{cols}</div>
    <div class="plaque g" style="margin-top:14px;">{t("<b>Задание в чат Teams:</b> какое число на тепловой карте вы бы проверили первым?", "<b>Teams chat task:</b> which number on the heatmap would you check first?")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин (результаты промптов 3 и 4; промпт 5 — на слайде 23). Тот же чат, файл уже загружен. После каждого ответа раскрывайте код: блок «Анализ завершён» или кнопка кода над графиком.",
                      "⏱ 4 min (results of prompts 3 and 4; prompt 5 is slide 23). Same chat, the file is already uploaded. After each answer open the code: the “Analysis complete” block or the code button above the chart."),
                    t(f"Промпт 3: тепловая карта. Общая доля возвратов около 6 %, но одна клетка горит: North × Electronics — {pc(RET[('North', 'Electronics')])}. Остальные около 5 %. По итогу за год этого не видно.",
                      f"Prompt 3: the heatmap. The overall return rate is about 6%, but one cell lights up: North × Electronics — {pc(RET[('North', 'Electronics')])}. The rest are about 5%. The annual total hides it."),
                    t("Промпт 4: отзывы. Модель сама выбрала склад N2 и разложила отзывы на темы. Тема «упаковка / повреждения» у N2 — 49 %, у остальных — 12 %. Текст объясняет цифру: посылки приходят повреждёнными.",
                      "Prompt 4: reviews. The model picked warehouse N2 by itself and sorted reviews into themes. “Packaging / damage” is 49% at N2 and 12% elsewhere. The text explains the number: parcels arrive damaged."),
                    t("Промпт 5: график для слайда. Подробно разберём через слайд. Если любой промпт думает дольше 90 секунд — показывайте готовый кадр с экрана и идите дальше." + EN_SHOTS,
                      "Prompt 5: a slide-ready chart, covered in detail two slides on. If any prompt takes longer than 90 seconds, show the ready frame and move on." + EN_SHOTS)))


def s_found():
    soc_sp = [SPEND[("Social", m)] for m in M12]
    soc_rv = [REV[("Social", m)] for m in M12]
    amber = lambda i: C["amber"] if i >= 6 else C["grey"]
    return dict(min=3, html=f'''
  {head(t("Часть 3 • что нашли", "Part 3 • what we found"), t("Две проблемы, которых не видно в итоге за год", "Two problems the annual total doesn’t show"), k="red")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:40px;align-items:stretch;">
      <div class="stack" style="gap:6px;">
        <div class="cap" style="font-size:22px;font-weight:700;color:var(--fg);">{t("1. Social: расход вырос, выручка — нет", "1. Social: spend went up, revenue didn’t")}</div>
        <div class="cap">{t("Расход на рекламу Social по месяцам, $", "Social ad spend by month, $")}</div>
        {bars_month(soc_sp, amber, 660, 170, 55000, kk)}
        <div class="cap">{t("Выручка Social по месяцам, $", "Social revenue by month, $")}</div>
        {bars_month(soc_rv, amber, 660, 170, 110000, kk)}
        <div class="note" style="--k:var(--amber)">{t(f"Второе полугодие к первому: расход <b>{pc((SOC_SP_H2 / SOC_SP_H1 - 1) * 100, 0, True)}</b>, выручка <b>{pc((SOC_RV_H2 / SOC_RV_H1 - 1) * 100, 0, True)}</b>. Выручка на $1 рекламы: 4 → 2.",
                                                        f"Second half vs first: spend <b>{pc((SOC_SP_H2 / SOC_SP_H1 - 1) * 100, 0, True)}</b>, revenue <b>{pc((SOC_RV_H2 / SOC_RV_H1 - 1) * 100, 0, True)}</b>. Revenue per $1 of ads: 4 → 2.")}</div>
      </div>
      <div class="stack" style="gap:8px;">
        <div class="cap" style="font-size:22px;font-weight:700;color:var(--fg);">{t("2. Склад N2: возвраты и жалобы на повреждения", "2. Warehouse N2: returns and damage complaints")}</div>
        <div class="cap">{t("Доля возвратов по месяцам, %", "Return rate by month, %")}</div>
        {n2_chart()}
        <div class="note" style="--k:var(--red)">{t(f"С сентября возвраты N2 — около {pc(N2_M[11], 0)}, у остальных — около {pc(REST_M[11], 0)}. В отзывах N2 почти половина — про повреждённые посылки.",
                                                      f"From September N2 returns are about {pc(N2_M[11], 0)}, others about {pc(REST_M[11], 0)}. Almost half of N2 reviews are about damaged parcels.")}</div>
        <div class="plaque">{t("<b>Цифра показывает где, текст объясняет почему.</b> Отзывы — тоже данные.", "<b>The number shows where; the text explains why.</b> Reviews are data too.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 4 мин. Две находки из демо, перерисованные из данных. Слева Social: с июля расход на рекламу вырос почти втрое (первое полугодие {money(SOC_SP_H1)}, второе {money(SOC_SP_H2)}), а выручка — на {pc((SOC_RV_H2 / SOC_RV_H1 - 1) * 100, 0)}. Каждый доллар рекламы стал приносить вдвое меньше. Итог за год при этом выглядит нормально: выручка растёт.",
                      f"⏱ 4 min. Two findings from the demo, redrawn from the data. Left, Social: from July ad spend nearly tripled (first half {money(SOC_SP_H1)}, second {money(SOC_SP_H2)}) while revenue grew {pc((SOC_RV_H2 / SOC_RV_H1 - 1) * 100, 0)}. Each ad dollar now brings half as much. The annual total looks fine: revenue grows."),
                    t("Справа склад N2: до августа возвраты как у всех, с сентября — около четверти заказов. Отзывы объясняют причину: коробки приходят мятыми, экраны разбитыми. Цифры говорят, где проблема, текст — почему.",
                      "Right, warehouse N2: until August returns match everyone else; from September about a quarter of orders. Reviews explain why: crushed boxes, broken screens. The numbers say where; the text says why."),
                    t("Чтобы не запутаться: склад N2 — это и есть клетка North × Electronics с тепловой карты. В клетке 24,8 % за сентябрь–декабрь, на графике по месяцам — около 26 % в отдельные месяцы.",
                      "To avoid confusion: warehouse N2 is the North × Electronics cell from the heatmap. The cell shows 24.8% for September–December; the monthly line is about 26% in some months."),
                    t("Вопрос в чат: «Что бы вы предложили Анне по каждой находке?» Ответ «урезать Social» разберём на слайде 23.",
                      "Ask the chat: “What would you suggest to Anna for each finding?” We cover “cut Social” on slide 23.")))


def s_makeover():
    return dict(min=3, html=f'''
  {head(t("Часть 3 • график для слайда", "Part 3 • a slide-ready chart"), t("График правится словами, как текст", "You edit a chart with words, like text"), k="violet")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:0.75fr 1.25fr;gap:26px;align-items:center;">
      <div class="stack" style="gap:12px;">
        {shot("p3_themes_before", t("Было: график по умолчанию", "Before: the default chart"), k="red")}
        {pr(t("Промпт", "Prompt"), t("Переделай этот график для слайда: заголовок — вывод, столбцы отсортированы, подписи значений на столбцах, без легенды и сетки, один акцентный цвет для N2, остальное серым. Объясни в 3 пунктах, что поменял.", "Rework this chart for a slide: the title states the finding, bars sorted, value labels on the bars, no legend and no gridlines, one accent colour for N2, everything else grey. Explain in 3 points what you changed."), k="violet")}
      </div>
      <div class="stack" style="gap:10px;">
        {shot("p4_themes_after", t("Стало: через 36 секунд", "After: 36 seconds later"), k="green", cls="good")}
        <div class="big3">
          <div class="note" style="--k:var(--green)">{t("<b>Заголовок = вывод.</b> «Почти в 9 раз больше» вместо «Темы отзывов».", "<b>Title = finding.</b> “Almost 9× more” instead of “Review themes”.")}</div>
          <div class="note" style="--k:var(--green)">{t("<b>Один цвет.</b> N2 синий, остальное серое — глаз сразу видит главное.", "<b>One colour.</b> N2 blue, the rest grey — the eye finds the point at once.")}</div>
          <div class="note" style="--k:var(--green)">{t("<b>Подписи на столбцах</b>, без легенды и сетки.", "<b>Values on the bars</b>, no legend or grid.")}</div>
        </div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Это промпт 5 из демо. Слева график, который модель строит по умолчанию: заголовок-тема, легенда, два ярких цвета, мелкие подписи. Справа тот же график после одного промпта. На слайд руководителю идёт правый.",
                      "⏱ 4 min. This is prompt 5 from the demo. Left: the chart the model builds by default — a topic title, a legend, two bright colours, small labels. Right: the same chart after one prompt. The right one goes into a manager’s slide."),
                    t("Пять правил из промпта годятся для любого графика: заголовок — вывод; сортировка; подписи прямо на столбцах; без лишнего (легенды, сетки); один акцентный цвет. Сохраните промпт себе, он в шпаргалке.",
                      "The five rules in the prompt work for any chart: title = finding; sorted; labels on the bars; nothing extra (legend, grid); one accent colour. Save the prompt; it is in the cheatsheet."),
                    t("Внимательно посмотрите на числа: было 49 %, стало 46 %. Об этом следующий слайд." + EN_SHOTS,
                      "Look closely at the numbers: 49% became 46%. That is the next slide." + EN_SHOTS)))


def s_check():
    return dict(min=4, html=f'''
  {head(t("Часть 3 • проверка за 60 секунд", "Part 3 • a 60-second check"), t("Три версии графика — три разных числа. Сверяйте после каждой переделки", "Three versions of a chart, three different numbers. Compare after every redo"), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.15fr 1fr;gap:36px;align-items:stretch;">
      <div class="stack" style="gap:10px;">
        <div class="cap" style="font-size:21px;font-weight:700;color:var(--fg);">{t("Доля отзывов N2 про повреждения, сентябрь–декабрь", "Share of N2 reviews about damage, September–December")}</div>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
          <div class="stat" style="--k:var(--amber)"><div class="n">49 %</div><div class="d">{t("первый график", "first chart")}</div></div>
          <div class="stat" style="--k:var(--amber)"><div class="n">46 %</div><div class="d">{t("после перекраски", "after restyling")}</div></div>
          <div class="stat" style="--k:var(--amber)"><div class="n">44 %</div><div class="d">{t("в отчёте Word", "in the Word report")}</div></div>
          <div class="stat" style="--k:var(--green)"><div class="n">61 %</div><div class="d">{t("по разметке, из которой собран файл", "by the labels the file was built from")}</div></div>
        </div>
        {shot("p4_what_changed", t("Модель объясняет, что поменяла", "The model explains what it changed"), k="amber", h=330)}
      </div>
      <div class="stack" style="gap:22px;justify-content:center;">
        <div class="chk" style="--k:var(--green)"><div class="n">1</div><div class="t">{t("Строки до и после", "Rows before and after")}<small>{t("1 261 в файле → 1 260 после удаления дубля. Сколько удалили и почему?", "1,261 in the file → 1,260 after the duplicate is removed. How many were dropped, and why?")}</small></div></div>
        <div class="chk" style="--k:var(--green)"><div class="n">2</div><div class="t">{t("Одна точка: с исходником и с прошлой версией", "One point: against the source and the previous version")}<small>{t("Найдите одно число с графика в файле и в прошлом ответе. Совпало?", "Find one number from the chart in the file and in the previous answer. Does it match?")}</small></div></div>
        <div class="chk" style="--k:var(--green)"><div class="n">3</div><div class="t">{t("Процент от чего", "Percent of what")}<small>{t("От какого месяца и за какой период? +161 % и +15 % — оба верны.", "From which month, over what period? +161% and +15% are both right.")}</small></div></div>
        <div class="plaque g">{t("<b>Темы отзывов</b> проверяйте чтением: откройте 10 отзывов и посчитайте сами.", "<b>Check review themes by reading:</b> open 10 reviews and count yourself.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Мы просили только поменять оформление. А модель заодно пересчитала темы: похвалу упаковке («аккуратно упаковано») перенесла из темы «повреждения» в «товар в порядке». Доля стала 46 %, в итоговом отчёте — 44 %. По разметке, из которой мы собирали учебный файл, про повреждения 53 отзыва из 87, то есть 61 %. Модель ищет по ключевым словам и пропускает жалобы, написанные своими словами.",
                      "⏱ 3 min. We only asked for a new look. The model also re-classified the themes: praise of packaging (“neatly packed”) moved from “damage” to “product OK”. The share became 46%, and 44% in the final report. By the labels we used to build the practice file, 53 of 87 reviews are about damage — 61%. The model searches by keywords and misses complaints written in other words."),
                    t("Если спросят про «остальных»: в первом графике у остальных складов 12 %, после перекраски 5 %. Модель пересчитала обе группы.",
                      "If asked about “the others”: the other warehouses were 12% in the first chart and 5% after restyling. The model re-counted both groups."),
                    t("Вывод про склад N2 от этого не меняется: жалоб на повреждения там во много раз больше, чем у остальных. Меняется число, которое уйдёт руководителю. Поэтому после каждой переделки сверяйте пару чисел с прошлой версией, а темы отзывов проверяйте выборочным чтением.",
                      "The N2 conclusion doesn’t change: there are many times more damage complaints there than elsewhere. What changes is the number that goes to the manager. So after every redo compare a couple of numbers with the previous version, and check review themes by reading a sample."),
                    t("Проверка за 60 секунд, три шага. Строки: сколько было, сколько стало. Одна точка: одно число с графика находите глазами в исходном файле. База процента: от какого месяца и за какой период.",
                      "A 60-second check in three steps. Rows: how many before, how many after. One point: find one number from the chart in the source file by eye. Percent base: from which month, over what period."),
                    t("Для любопытных, эксперимент из подготовки урока: на маленькой таблице модели без кода посчитали сумму правильно, но строку с 66 возвратами при 62 заказах «починили» на 6, хотя в источнике было 4. Догадку модели надо отличать от данных. Подробности: demo_assets/no_code_experiment_2026-10-13.md." + EN_SHOTS,
                      "For the curious, an experiment from lesson prep: on a small table, models without code got the sum right but “fixed” a row with 66 returns on 62 orders to 6, while the source said 4. Tell the model’s guess apart from the data. Details: demo_assets/no_code_experiment_2026-10-13.md." + EN_SHOTS)))


def _db_results():
    """Read the channel-sample results produced by demo_v2/channels (see its README)."""
    res = DB / "results"
    if not res.exists():
        return None
    out = {}
    for f in sorted(res.glob("*.csv")):
        out[f.stem] = list(csv.DictReader(f.open(encoding="utf-8")))
    return out


def s_db():
    # filled in once demo_v2/channels/ exists — see s_db_full
    return s_db_full() if _db_results() else dict(min=2, html=head(t("Большая база", "A large database"), t("Файл не лезет в чат: модель пишет запрос, база считает", "The file won’t fit in a chat: the model writes a query, the database counts")), notes=notes("⏱ 5"))


def db_bars(rows, w=700, h=330):
    vals = [float(r["median_views"]) for r in rows]
    labs = [r["duration_bucket"].split(": ", 1)[1] for r in rows]
    en = {"до 1 мин": "< 1 min", "1-5 мин": "1–5 min", "5-10 мин": "5–10 min", "10-20 мин": "10–20 min", "20-40 мин": "20–40 min", "40+ мин": "40+ min"}
    mx = max(vals)
    bw = (w - 20) / len(vals)
    out = f'<line x1="10" y1="{h - 40}" x2="{w - 6}" y2="{h - 40}" stroke="{GRID}" stroke-width="2"/>'
    for i, (v, lb) in enumerate(zip(vals, labs)):
        bh = v / mx * (h - 90)
        x = 14 + i * bw
        col = C["amber"] if v == mx else C["grey"]
        out += (f'<rect x="{x:.1f}" y="{h - 40 - bh:.1f}" width="{bw - 18:.1f}" height="{bh:.1f}" rx="4" fill="{col}"/>'
                f'<text x="{x + (bw - 18) / 2:.1f}" y="{h - 48 - bh:.1f}" text-anchor="middle" font-size="20" font-weight="700" fill="{FG}">{num(v)}</text>'
                f'<text x="{x + (bw - 18) / 2:.1f}" y="{h - 12}" text-anchor="middle" font-size="17" fill="{MUT}">{t(lb.replace("-", "–"), en[lb])}</text>')
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def db_ratio(rows, w=700, h=330):
    vals = [float(r["median_vs_own_channel"]) for r in rows]
    labs = [r["duration_bucket"].split(": ", 1)[1] for r in rows]
    en = {"до 1 мин": "< 1 min", "1-5 мин": "1–5 min", "5-10 мин": "5–10 min", "10-20 мин": "10–20 min", "20-40 мин": "20–40 min", "40+ мин": "40+ min"}
    bw = (w - 20) / len(vals)
    y1 = h - 40 - 1.0 / 1.4 * (h - 90)
    out = (f'<line x1="10" y1="{h - 40}" x2="{w - 6}" y2="{h - 40}" stroke="{GRID}" stroke-width="2"/>'
           f'<line x1="10" y1="{y1:.1f}" x2="{w - 6}" y2="{y1:.1f}" stroke="{C["green"]}" stroke-width="2" stroke-dasharray="7 6"/>')
    for i, (v, lb) in enumerate(zip(vals, labs)):
        bh = v / 1.4 * (h - 90)
        x = 14 + i * bw
        out += (f'<rect x="{x:.1f}" y="{h - 40 - bh:.1f}" width="{bw - 18:.1f}" height="{bh:.1f}" rx="4" fill="{C["grey"]}"/>'
                f'<text x="{x + (bw - 18) / 2:.1f}" y="{h - 48 - bh:.1f}" text-anchor="middle" font-size="20" font-weight="700" fill="{FG}">{dec(v, 2)}</text>'
                f'<text x="{x + (bw - 18) / 2:.1f}" y="{h - 12}" text-anchor="middle" font-size="17" fill="{MUT}">{t(lb.replace("-", "–"), en[lb])}</text>')
    return f'<svg viewBox="0 0 {w} {h}">{out}</svg>'


def s_db_full():
    import json
    res = _db_results()
    meta = json.loads((DB / "sample_meta.json").read_text(encoding="utf-8"))
    full, smp = meta["full_db"], meta["sample"]
    q2 = res["q2_views_by_duration"]
    q4 = {r["duration_bucket"]: float(r["median_vs_own_channel"]) for r in res["q4_duration_vs_own_channel"]}
    top = max(q2, key=lambda r: float(r["median_views"]))
    short = float(q2[1]["median_views"])
    ratio = float(top["median_views"]) / short
    sql = t('''<span class="cm">-- Видео какой длины набирают больше просмотров?</span>
<span class="kw">SELECT</span> duration_bucket,            <span class="cm">-- длительность</span>
       <span class="kw">COUNT</span>(*)      <span class="kw">AS</span> videos,   <span class="cm">-- сколько видео</span>
       <span class="kw">MEDIAN</span>(views) <span class="kw">AS</span> typical   <span class="cm">-- типичные просмотры</span>
<span class="kw">FROM</span> videos
<span class="kw">GROUP BY</span> duration_bucket;''', '''<span class="cm">-- Which video length gets the most views?</span>
<span class="kw">SELECT</span> duration_bucket,            <span class="cm">-- length</span>
       <span class="kw">COUNT</span>(*)      <span class="kw">AS</span> videos,   <span class="cm">-- how many videos</span>
       <span class="kw">MEDIAN</span>(views) <span class="kw">AS</span> typical   <span class="cm">-- typical views</span>
<span class="kw">FROM</span> videos
<span class="kw">GROUP BY</span> duration_bucket;''')
    stats = (f'<div class="stat" style="--k:var(--amber)"><div class="n">{num(full["channels"])}</div><div class="d">{t("каналов: название, подписчики, страна", "channels: name, subscribers, country")}</div></div>'
             f'<div class="stat" style="--k:var(--amber)"><div class="n">{num(full["videos"])}</div><div class="d">{t("видео: длительность, дата, канал", "videos: length, date, channel")}</div></div>'
             f'<div class="stat" style="--k:var(--amber)"><div class="n">{num(full["video_stat_observations"])}</div><div class="d">{t("замеров просмотров по дням", "daily view measurements")}</div></div>')
    return dict(min=2, html=f'''
  {head(t("Часть 4 • результат и ловушка", "Part 4 • the result and the trap"), t("Длинные видео в 12 раз популярнее? Нет: их снимают большие каналы", "Long videos 12× more popular? No: big channels make them"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:32px;margin-top:10px;align-items:stretch;">
      <div class="stack" style="gap:6px;">
        <div class="cap" style="font-size:21px;font-weight:700;color:var(--fg);">{t("Первый запрос: типичные просмотры по длительности", "First query: typical views by length")}</div>
        {db_bars(q2)}
        <div class="note" style="--k:var(--red)">{t(f"20–40 минут — в {ratio:.0f} раз больше коротких? Сравнили каждое видео с обычными роликами <b>его же канала</b> — всего на {(q4[top['duration_bucket']] - 1) * 100:.0f} % выше обычного. Длинные видео просто чаще снимают большие каналы.",
                                                        f"20–40 minutes gets {ratio:.0f}× more than short videos? Compared with ordinary videos <b>of the same channel</b>, they are only {(q4[top['duration_bucket']] - 1) * 100:.0f}% above usual. Big channels simply make long videos more often.")}</div>
      </div>
      <div class="stack" style="gap:6px;">
        <div class="cap" style="font-size:21px;font-weight:700;color:var(--fg);">{t("Второй запрос: видео против обычного видео своего канала", "Second query: a video vs its own channel’s usual video")}</div>
        {db_ratio(res["q4_duration_vs_own_channel"])}
        <div class="note" style="--k:var(--green)">{t("1,0 — как обычное видео этого же канала. Все длительности около 1,0.", "1.0 means the same as the channel’s usual video. Every length is about 1.0.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t(f"⏱ 5 мин (готовые кадры, вживую не запускаем). Это рабочая база автора курса: кулинарные YouTube-каналы, собранные через официальный API. {num(full['channels'])} каналов, {num(full['videos'])} видео, {num(full['video_stat_observations'])} замеров просмотров. Данные лежат в трёх связанных таблицах и обновляются каждый день, поэтому выгружать их в файл ради каждого вопроса неудобно.",
                      f"⏱ 5 min (ready frames, not run live). This is the course author’s working database: cooking YouTube channels collected via the official API. {num(full['channels'])} channels, {num(full['videos'])} videos, {num(full['video_stat_observations'])} view measurements. The data sits in three linked tables and updates daily, so exporting a file for every question is impractical."),
                    t("Приём тот же, что с Excel: вы описываете таблицу и задаёте вопрос словами, модель пишет запрос на языке SQL, база считает сама за секунду. SQL читается почти как английский: выбрать длительность, посчитать видео, взять типичные просмотры, из таблицы видео, сгруппировать по длительности. MEDIAN — типичное значение: половина видео выше, половина ниже. Среднее портят редкие вирусные хиты.",
                      "Same move as with Excel: you describe the table and ask in words, the model writes an SQL query, the database counts in a second. SQL reads almost like English: select the length, count the videos, take typical views, from the videos table, grouped by length. MEDIAN is the typical value: half the videos above, half below. Rare viral hits spoil the average."),
                    t(f"Первый ответ соблазнительный: видео на 20–40 минут набирают в {ratio:.0f} раз больше коротких. Но длинные видео чаще снимают большие каналы, у которых и так много зрителей. Второй запрос сравнивает каждое видео с обычными видео его же канала, и разница почти исчезает. Вывод «снимайте длинные видео» эти данные не доказывают. Тот же случай, что со Social.",
                      f"The first answer is tempting: 20–40-minute videos get {ratio:.0f}× more views than short ones. But big channels, which already have many viewers, make long videos more often. A second query compares each video with ordinary videos of its own channel, and the gap nearly disappears. This data does not prove “make long videos”. Same story as with Social."),
                    t("Срез обезличен: убраны описания, ссылки, телефоны и id YouTube, e-mail в выборке нет. Файлы целиком студентам не раздаём, показываем только графики. Запросы и ответы: demo_v2/channels/queries.sql и results/answers.md.",
                      "The sample is anonymised: descriptions, links, phone numbers and YouTube ids removed; no e-mails in the sample. We don’t hand the files to students, only show the charts. Queries and answers: demo_v2/channels/queries.sql and results/answers.md.")))


def s_sources():
    return dict(min=2, html=f'''
  {head(t("Часть 4 • откуда берутся данные", "Part 4 • where data comes from"), t("Сначала ищите кнопку «Экспорт», потом API. Скрапинг — последний вариант", "Look for an Export button first, then an API. Scraping is the last option"))}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1fr 1.25fr 1fr;gap:22px;align-items:center;">
      <div class="door" style="--k:var(--green)">{icon("export", 52, "var(--green)")}<div class="h">{t("1. Экспорт", "1. Export")}</div>
        <div class="w">{t("Кнопка «Выгрузить в Excel / CSV» есть почти везде: CRM, 1С, рекламный кабинет, YouTube Studio, Google Analytics.", "An “Export to Excel / CSV” button exists almost everywhere: CRM, accounting, ad accounts, YouTube Studio, Google Analytics.")}</div>
        <div class="o">{t("быстро · законно · без кода", "fast · legal · no code")}</div></div>
      <div class="door" style="--k:var(--cyan)">{icon("api", 52, "var(--cyan)")}<div class="h">{t("2. Официальный API", "2. Official API")}</div>
        <div class="code" style="font-size:18px;line-height:1.5;padding:12px 14px;">{{ <span class="st">"title"</span>: <span class="st">"Kitchen Basics"</span>,
  <span class="st">"subscriberCount"</span>: <span class="nm">"184000"</span>,
  <span class="st">"videoCount"</span>: <span class="nm">"412"</span> }}</div>
        <div class="w">{t("Программа спрашивает сервис и получает ответ вот в таком виде. ИИ пишет скрипт, который превращает это в строки таблицы.", "A program asks the service and gets an answer like this. AI writes a script that turns it into table rows.")}</div>
        <div class="o">{t("так собрана база каналов со слайда 24", "this is how the slide 24 channel database was collected")}</div></div>
      <div class="door" style="--k:var(--red)">{icon("web", 52, "var(--red)")}<div class="h">{t("3. Скрапинг", "3. Scraping")}</div>
        <div class="w">{t("Программа читает страницы сайта, как человек. Перед этим проверьте:", "A program reads website pages like a person would. Before you do it, check:")}</div>
        <ul class="checklist" style="gap:8px;"><li style="font-size:20px;">{t("условия сайта разрешают", "the site’s terms allow it")}</li><li style="font-size:20px;">{t("нет персональных данных", "no personal data")}</li><li style="font-size:20px;">{t("не нагружаете чужой сайт", "you don’t overload the site")}</li></ul></div>
    </div>
    <div class="plaque" style="margin-top:18px;">{t("<b>Вопрос для ИИ:</b> «Какой официальный экспорт или API есть у системы X, чтобы выгрузить продажи за год?»", "<b>Ask the AI:</b> “What official export or API does system X have to download a year of sales?”")}</div>
  </div>''',
                notes=notes(
                    t("Перед началом слайда отправьте в чат промпт 6 (отчёт и скрипт): ответ идёт 3–4 минуты, к слайду 28 файл будет готов.",
                      "Before you start this slide, send prompt 6 (report and script) to the chat: the answer takes 3–4 minutes and will be ready by slide 28."),
                    t("⏱ 3 мин. Данные для анализа почти всегда уже где-то лежат. Первое, что ищем, — кнопку экспорта: она есть в CRM, 1С, рекламных кабинетах, YouTube Studio. Это самый быстрый и безопасный путь.",
                      "⏱ 3 min. The data you need almost always already sits somewhere. First look for an export button: CRM, accounting software, ad accounts and YouTube Studio all have one. It is the fastest and safest route."),
                    t("Второе — официальный API: программный вход в сервис. Ответ приходит в виде JSON, как в середине слайда. Код писать самим не нужно: ИИ напишет скрипт, который превратит ответ в таблицу. Так, через YouTube Data API, собрана база каналов, которую мы только что видели. Пример JSON на слайде упрощён.",
                      "Second, an official API: a program’s way into the service. The answer comes as JSON, like the middle of the slide. You don’t write the code yourself: AI writes a script that turns the answer into a table. The channel database we just saw was collected this way, through the YouTube Data API. The JSON on the slide is simplified."),
                    t("Третье — скрапинг: программа читает страницы сайта. Это последний вариант. Три проверки: условия сайта разрешают, нет персональных данных, вы не создаёте нагрузку на чужой сервер. Для большинства рабочих задач хватает экспорта.",
                      "Third, scraping: a program reads a site’s pages. It is the last option. Three checks: the site’s terms allow it, no personal data, you don’t put load on someone else’s server. For most work tasks, export is enough.")))


def s_report():
    return dict(min=3, html=f'''
  {head(t("Часть 5 • ответ Анне", "Part 5 • the answer to Anna"), t("Руководителю отправляем файл отчёта. Превью в чате может врать", "Send the manager the report file. The chat preview can lie"), k="green")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:0.95fr 1fr 0.85fr;gap:22px;align-items:center;">
      <div class="stack" style="gap:8px;">
        {shot("p5_fake_preview", t("✗ превью в чате", "✗ preview in the chat"), k="red", cls="bad")}
        <div class="scap">{t("Картинка-заглушка: «Series A», выдуманные числа. Нашего анализа тут нет.", "A placeholder picture: “Series A”, invented numbers. None of our analysis is here.")}</div>
      </div>
      <div class="stack" style="gap:8px;">
        {shot("p5_report_top", t("✓ скачанный .docx", "✓ the downloaded .docx"), k="green", cls="good", h=500)}
        <div class="scap">{t("Настоящий файл: вопрос, три графика, три вывода, «чего данные не доказывают».", "The real file: the question, three charts, three findings, “what the data does not prove”.")}</div>
      </div>
      <div class="stack" style="gap:10px;">
        {pr(t("Промпт 6", "Prompt 6"), t("Собери одностраничный отчёт для руководителя в Word: вопрос, 3 графика (выручка по месяцам, отдача рекламы, жалобы N2), 3 вывода и один пункт «чего эти данные не доказывают». И дай короткий Python-скрипт, который построит те же 3 графика по файлу следующего месяца.", "Build a one-page report for a manager in Word: the question, 3 charts (revenue by month, ad return, N2 complaints), 3 findings and one point on “what this data does not prove”. And give me a short Python script that builds the same 3 charts from next month’s file."), k="green")}
        {shot("p5_script", t("рецепт на следующий месяц", "recipe for next month"), k="cyan")}
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 5 мин (1 живой промпт). Итог анализа — файл, который можно переслать, а не скриншот чата. Промпт 6 просит две вещи: страницу отчёта и скрипт-рецепт.",
                      "⏱ 5 min (1 live prompt). The result of an analysis is a file you can forward, not a chat screenshot. Prompt 6 asks for two things: a report page and a recipe script."),
                    t("Слева то, что ChatGPT показал в чате как превью отчёта: стоковая картинка с «Series A–E» и чужими числами. В центре — тот же отчёт, скачанный и открытый: всё на месте, числа наши. Вывод простой: превью не проверяем, проверяем открытый файл.",
                      "Left: what ChatGPT showed in the chat as the report preview — a stock picture with “Series A–E” and someone else’s numbers. Centre: the same report downloaded and opened — everything is there, with our numbers. Simple rule: don’t judge the preview, check the opened file."),
                    t("Справа рецепт: скрипт, который строит те же три графика из файла следующего месяца. В январе не нужно повторять весь диалог: кладёте новый файл и запускаете скрипт, в Colab или через чат: «запусти этот скрипт на новом файле». Оговорка: скрипт ждёт книгу с листами Sales и Reviews. На учебном demo_v2/northstar_sales_2026-01.csv (только продажи, один месяц) график отзывов не построится, а на графике по месяцам будет одна точка. Это нормально: скажите студентам заранее." + EN_SHOTS,
                      "Right: the recipe — a script that builds the same three charts from next month’s file. In January you don’t repeat the whole conversation: drop in the new file and run the script, in Colab or by asking the chat: “run this script on the new file”. Caveat: the script expects a workbook with Sales and Reviews sheets. On the practice demo_v2/northstar_sales_2026-01.csv (sales only, one month) the reviews chart won’t build and the monthly chart has one point. That is fine: tell students in advance." + EN_SHOTS)))


def s_causal():
    grey, mut, fg, red, amber = "#5f6e84", "#a3b1c4", "#f1f5f9", "#f87171", "#fbbf24"
    fac = [t("сезон распродаж", "sales season"), t("кому показывали рекламу", "who saw the ads"), t("новые креативы", "new ad creatives"), t("кому засчитали продажу", "which channel got credit")]
    svg = f'<svg class="dia" viewBox="0 0 620 330">' + ARROW.format(id="ca", c=grey) + ARROW.format(id="cr", c=red)
    for i, f in enumerate(fac):
        x = 10 + (i % 2) * 310
        yb = 0 if i < 2 else 66
        svg += (f'<rect x="{x}" y="{yb}" width="290" height="54" rx="10" fill="#0f1624" stroke="{grey}" stroke-width="1.5" stroke-dasharray="5 4"/>'
                f'<text x="{x + 145}" y="{yb + 35}" text-anchor="middle" font-size="21" fill="{mut}">{f}</text>')
    svg += (f'<path d="M310 124 L 310 133" stroke="{grey}" stroke-width="2"/>'
            f'<path d="M310 138 L 160 194" stroke="{grey}" stroke-width="2" fill="none" marker-end="url(#ca)"/>'
            f'<path d="M310 138 L 460 194" stroke="{grey}" stroke-width="2" fill="none" marker-end="url(#ca)"/>'
            f'<text x="310" y="178" text-anchor="middle" font-size="18" fill="{mut}">{t("влияют на оба", "affect both")}</text>'
            f'<rect x="40" y="200" width="220" height="70" rx="12" fill="#0f1624" stroke="{amber}" stroke-width="2"/>'
            f'<text x="150" y="243" text-anchor="middle" font-size="22" font-weight="700" fill="{fg}">{t("бюджет Social", "Social budget")}</text>'
            f'<rect x="360" y="200" width="220" height="70" rx="12" fill="#0f1624" stroke="{amber}" stroke-width="2"/>'
            f'<text x="470" y="243" text-anchor="middle" font-size="22" font-weight="700" fill="{fg}">{t("выручка", "revenue")}</text>'
            f'<path d="M264 235 L 354 235" stroke="{red}" stroke-width="3" fill="none" stroke-dasharray="8 6" marker-end="url(#cr)"/>'
            f'<text x="309" y="300" text-anchor="middle" font-size="19" font-weight="700" fill="{red}">{t("причина? не доказано", "cause? not proven")}</text></svg>')
    return dict(min=2, html=f'''
  {head(t("После находки", "After the finding"), t("Таблица говорит, что было. Что будет после урезания бюджета, покажет только тест", "The table says what happened. Only a test shows what a budget cut will do"), t("Соблазн после демо: <b>урезать рекламу Social вдвое?</b>", "The temptation after the demo: <b>cut Social ads in half?</b>"), k="red")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:50px;align-items:center;">
      <div class="stack" style="gap:20px;">
        <div class="note" style="--k:var(--amber)">{t("Данные показывают: с июля Social тратит вдвое больше на каждый доллар выручки.", "The data shows: since July Social spends twice as much per dollar of revenue.")}</div>
        <div class="note" style="--k:var(--red)">{t("Данные не показывают: сколько выручки пропадёт, если рекламу урезать.", "The data doesn’t show: how much revenue disappears if ads are cut.")}</div>
        <div class="plaque g">{t("<b>Как узнать:</b> урезать бюджет в одном регионе на 2–4 недели и сравнить с остальными.", "<b>How to find out:</b> cut the budget in one region for 2–4 weeks and compare with the others.")}</div>
      </div>
      {svg}
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 2 мин. После находки про Social хочется сразу урезать бюджет. Модель часто так и советует. Но таблица описывает прошлое. На бюджет и на выручку одновременно влияют сезон, аудитория, креативы и то, какому каналу засчитали продажу.",
                      "⏱ 2 min. After the Social finding it is tempting to cut the budget at once. Models often advise exactly that. But the table describes the past. Season, audience, creatives and the rules that credit a sale to a channel all affect both budget and revenue."),
                    t("Хороший ответ ИИ звучит так: «по этим данным нельзя сказать, сколько выручки пропадёт; предлагаю тест». Если модель так не ответила, спросите: «Какое допущение ты делаешь?»",
                      "A good AI answer sounds like: “this data can’t say how much revenue would be lost; I suggest a test”. If the model didn’t say so, ask: “What assumption are you making?”")))


def s_privacy():
    rows = [("green", t("Можно: учебные, открытые, обезличенные данные", "OK: practice, public, anonymised data"), t("как Northstar; любой сервис", "like Northstar; any service")),
            ("amber", t("Осторожно: внутренние данные компании", "Careful: internal company data"), t("только в рабочем аккаунте (ChatGPT Business/Enterprise, Claude Team/Enterprise, Google Workspace) — там данные не идут на обучение", "only in the work account (ChatGPT Business/Enterprise, Claude Team/Enterprise, Google Workspace) — data is not used for training there")),
            ("red", t("Нельзя без разрешения: клиенты, сотрудники, финансы, здоровье", "Not without approval: customers, staff, finance, health"), t("персональные данные — только в одобренной среде и с согласия владельца данных", "personal data — only in an approved environment with the data owner’s consent"))]
    lr = "".join(f'<div class="lrow" style="--k:var(--{c})"><div class="dot"></div><div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for c, h, d in rows)
    return dict(min=1, html=f'''
  {head(t("Часть 5 • данные и приватность", "Part 5 • data and privacy"), t("Что можно загружать в чат", "What you may upload to a chat"), k="amber")}
  <div class="body" style="margin-top:20px;">
    <div class="row" style="grid-template-columns:1.3fr 1fr;gap:44px;align-items:center;">
      <div class="light">{lr}</div>
      <div class="stack" style="gap:20px;">
        <div class="note" style="--k:var(--cyan)">{t("Перед загрузкой <b>удалите лишние колонки</b>: имена, телефоны, e-mail. Для анализа продаж они не нужны.", "Before uploading, <b>delete unneeded columns</b>: names, phones, e-mails. Sales analysis doesn’t need them.")}</div>
        <div class="note" style="--k:var(--amber)">{t("В личных аккаунтах обучение на ваших данных <b>зависит от настроек</b>: ChatGPT — «Improve the model for everyone», Gemini — «Keep Activity», Claude — только если вы разрешили.", "In personal accounts, training on your data <b>depends on settings</b>: ChatGPT — “Improve the model for everyone”, Gemini — “Keep Activity”, Claude — only if you allowed it.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 2 мин. Светофор. Зелёный — учебные и открытые данные, как наш файл. Жёлтый — внутренние данные компании, только в рабочем аккаунте. Красный — персональные данные клиентов и сотрудников, финансы, здоровье: только в одобренной компанией среде.",
                      "⏱ 2 min. A traffic light. Green — practice and public data, like our file. Amber — internal company data, only in the work account. Red — personal data of customers and staff, finance, health: only in a company-approved environment."),
                    t("Настройки на октябрь 2026: бизнес-тарифы (ChatGPT Business/Enterprise, Claude Team/Enterprise/API, Google Workspace) по умолчанию на обучение не используются. В личных аккаунтах смотрите настройки, названия на слайде.",
                      "Settings as of October 2026: business plans (ChatGPT Business/Enterprise, Claude Team/Enterprise/API, Google Workspace) are not used for training by default. In personal accounts check the settings named on the slide.")))


def s_hw():
    files = (f'analysis_pack/\n'
             f'  analysis.xlsx   <span class="cm"># {t("формула от ИИ + сводная + график", "AI formula + pivot + chart")}</span>\n'
             f'  charts/         <span class="cm"># {t("3 графика, один — «было / стало»", "3 charts, one as before / after")}</span>\n'
             f'  report.docx     <span class="cm"># {t("1 страница: вопрос, 3 вывода", "1 page: question, 3 findings")}</span>\n'
             f'  recipe.md       <span class="cm"># {t("промпт + скрипт на январь", "prompt + script for January")}</span>\n'
             f'  checks.md       <span class="cm"># {t("60 секунд + «не доказывают»", "60 seconds + “does not prove”")}</span>')
    return dict(min=2, html=f'''
  {head(t("Часть 5 • домашнее задание", "Part 5 • homework"), t("Пакет, который можно отправить руководителю", "A pack you can send to a manager"), t("Файл <code>northstar_2025.xlsx</code>. Ответьте Анне на одно письмо: <b>что с продажами за год и что проверить дальше?</b>", "File <code>northstar_2025.xlsx</code>. Answer Anna’s e-mail: <b>how did sales go this year, and what should we check next?</b>"), k="green")}
  <div class="body" style="margin-top:18px;">
    <div class="row" style="grid-template-columns:1.2fr 1fr;gap:40px;align-items:center;">
      <div class="files">{files}</div>
      <div class="stack" style="gap:22px;">
        <div class="note" style="--k:var(--green)">{t("<b>Без платного ИИ в Excel:</b> файл в чат → книга с формулами обратно → открыть в Excel.", "<b>No paid AI in Excel needed:</b> file to a chat → a workbook with formulas back → open in Excel.")}</div>
        <div class="note" style="--k:var(--red)">{t("<b>Обязательно:</b> одно утверждение, которое звучит правдоподобно, но данные его не доказывают.", "<b>Required:</b> one statement that sounds plausible but the data does not prove.")}</div>
        <div class="cap">{t("Шаблоны и критерии — в L08_05_Homework и demo_v2/student_starter.", "Templates and rubric — in L08_05_Homework and demo_v2/student_starter.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Результат домашки — пакет из пяти частей, который другой человек откроет и поймёт за 5 минут. Книга Excel с формулой, которую написал ИИ, сводной и графиком. Три графика, один из них в паре «было / стало». Отчёт на одну страницу. Рецепт: промпт и скрипт, который строит графики по файлу января. Файл проверок.",
                      "⏱ 4 min. The homework result is a five-part pack another person can open and understand in 5 minutes. An Excel workbook with an AI-written formula, a pivot and a chart. Three charts, one as a before/after pair. A one-page report. A recipe: the prompt and a script that builds the charts from the January file. A checks file."),
                    t("Платная лицензия не нужна: путь через чат и скачанную книгу работает у всех. Свои рабочие данные — только обезличенные и с разрешения, по светофору. Отдельный пункт — одно утверждение, которое напрашивается, но данными не подтверждается. Например, «если урезать бюджет Social, выручка не упадёт».",
                      "No paid licence needed: the chat-and-download route works for everyone. Your own work data only if anonymised and allowed, per the traffic light. One required item: a statement that suggests itself but the data doesn’t support. For example, “if we cut the Social budget, revenue won’t drop”.")))


def s_summary():
    rules = [("cyan", t("✓ Опись файла", "✓ Describe a file"), t("«опиши файл, предложи 5 вопросов, ничего не меняй»", "“describe the file, suggest 5 questions, change nothing”")),
             ("green", t("✓ Формула словами", "✓ A formula in words"), t("«формулами Excel, а не готовыми числами» + щёлкнуть ячейку", "“Excel formulas, not pasted numbers” + click a cell")),
             ("violet", t("✓ График для слайда", "✓ A slide-ready chart"), t("один вопрос — один график, заголовок — вывод", "one question, one chart, title = finding")),
             ("amber", t("✓ Отчёт на страницу", "✓ A one-page report"), t("открыть скачанный файл, приложить рецепт", "open the downloaded file, attach the recipe")),
             ("red", t("✓ Проверка за минуту", "✓ A one-minute check"), t("строки, одна точка, процент от чего", "rows, one point, percent of what"))]
    r = "".join(f'<div class="rule" style="--k:var(--{c})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>' for i, (c, h, d) in enumerate(rules))
    return dict(min=1, html=f'''
  {head(t("Итоги", "Summary"), t("Что забрать с урока", "What to take away"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1.5fr 1fr;gap:50px;align-items:center;">
      <div class="rules" style="gap:24px;">{r}</div>
      <div class="plaque">{t("<b>Следующий урок — L09:</b> экосистема Claude и артефакты. Тот же анализ станет интерактивной страницей, которую открывают по ссылке.", "<b>Next lesson — L09:</b> the Claude ecosystem and artifacts. The same analysis becomes an interactive page opened by a link.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 2 мин. Пять приёмов, которые можно применить уже в понедельник на своей таблице: промпт-опись, формулы словами, один график на вопрос, отчёт файлом с рецептом и 60 секунд проверки.",
                      "⏱ 2 min. Five moves you can use on your own spreadsheet on Monday: the describe prompt, formulas in words, one chart per question, the report as a file with a recipe, and 60 seconds of checks."),
                    t("Тизер L09: в Claude результат анализа можно сразу превратить в артефакт — интерактивную страницу с графиками, которую коллеги открывают по ссылке. Вопросы.",
                      "L09 teaser: in Claude an analysis can become an artifact — an interactive page with charts that colleagues open by link. Questions.")))



# ---------------------------------------------------------------- v2.1 (2026-10-17 evening): data concepts, prompt anatomy, bad / good
REV_RU = list(csv.DictReader((L08 / "demo_v2" / "northstar_reviews_2025.csv").open(encoding="utf-8")))
REV_EN = list(csv.DictReader((L08 / "demo_v2" / "northstar_reviews_2025_EN.csv").open(encoding="utf-8")))


def anatomy(lines, k_default="cyan"):
    """Prompt split into lines; each line gets a number, a colour and a plain-language 'why'."""
    rows = ""
    for i, (txt, why, k) in enumerate(lines, 1):
        rows += (f'<div class="an-row" style="--k:var(--{k or k_default})"><div class="an-n">{i}</div>'
                 f'<div class="an-t">{txt}</div><div class="an-w">{why}</div></div>')
    return f'<div class="an">{rows}</div>'


def badgood(bad_q, bad_shots, good_q, good_shots, bad_note, good_note):
    def col(kind, q, shots, note):
        k = "amber" if kind == "bad" else "green"
        lab = t("Быстро", "Quick") if kind == "bad" else t("✓ Под контролем", "✓ Under control")
        sh = "".join(shot(n, None, k=k, cls=("" if kind == "bad" else "good"), h=h) for n, h in shots)
        return (f'<div class="stack" style="gap:8px;"><div class="bg-q" style="--k:var(--{k})"><span class="badge solid" style="--k:var(--{k})">{lab}</span> {q}</div>'
                f'{sh}<div class="note" style="--k:var(--{k})">{note}</div></div>')
    return f'<div class="row" style="grid-template-columns:1fr 1fr;gap:28px;align-items:start;">{col("bad", bad_q, bad_shots, bad_note)}{col("good", good_q, good_shots, good_note)}</div>'


def s_outcomes():
    items = [("cyan", t("Опись файла", "Describe a file"), t("за минуту понять, что лежит в таблице", "understand what is in a table in a minute")),
             ("green", t("Формула словами", "A formula in words"), t("попросить формулу и сводную в Excel", "ask for a formula and a pivot in Excel")),
             ("violet", t("График для слайда", "A slide-ready chart"), t("тип под вопрос, заголовок — вывод", "the type fits the question, the title states the finding")),
             ("amber", t("Отчёт на страницу", "A one-page report"), t("файл, который можно переслать", "a file you can forward")),
             ("red", t("Проверка за минуту", "A one-minute check"), t("строки, одна точка, процент от чего", "rows, one point, percent of what"))]
    r = "".join(f'<div class="rule" style="--k:var(--{c})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>' for i, (c, h, d) in enumerate(items))
    return dict(min=2, html=f'''
  {head(t("О чём урок", "What this lesson gives you"), t("Пять навыков, которые вы унесёте сегодня", "Five skills you take away today"))}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1.1fr 1fr;gap:44px;align-items:center;">
      <div class="rules" style="gap:22px;">{r}</div>
      <div class="stack" style="gap:16px;">
        <div class="plaque" style="font-size:23px;line-height:1.5;">
          <div class="kicker" style="--k:var(--amber);margin-bottom:8px;">{t("Задача, на которой учимся", "The task we learn on")}</div>
          {t("Письмо коммерческого директора: «Что у нас с продажами за год? Почему во втором полугодии реклама стала хуже окупаться? И откуда столько возвратов осенью? Нужна одна страница к пятнице».", "An e-mail from the commercial director: “How did sales go this year? Why did advertising pay off worse in the second half? And why so many returns in the autumn? I need one page by Friday.”")}
        </div>
        <div class="note" style="--k:var(--cyan)">{t("Весь урок отвечаем на это письмо. В конце у нас готова страница отчёта.", "We spend the lesson answering this e-mail. At the end we have the report page.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 2 мин. Расскажите, с чем студенты уйдут: пять навыков на слайде. Каждый мы покажем на живом примере, и почти к каждому будет пара «быстро / под контролем» из настоящих ответов ChatGPT.",
                      "⏱ 2 min. Say what students will leave with: the five skills on the slide. We show each on a live example, and almost each one gets a “quick / under control” pair from real ChatGPT answers."),
                    t("Справа задача: письмо Анны, коммерческого директора магазина Northstar. На неё мы отвечаем весь урок. Магазин и данные вымышленные, поэтому файл можно спокойно загружать в любой чат.",
                      "On the right is the task: an e-mail from Anna, commercial director of the Northstar shop. We answer it throughout the lesson. The shop and data are made up, so the file can go into any chat.")))


def s_data_where():
    tiles = [("green", "grid", t("Таблицы", "Spreadsheets"), t("Excel, Google Таблицы: продажи, бюджет, план", "Excel, Google Sheets: sales, budget, plan"), t("ИИ пишет формулы и сводные", "AI writes formulas and pivots")),
             ("cyan", "export", t("Выгрузки", "Exports"), t("CSV из CRM, 1С, рекламного кабинета, YouTube Studio", "CSV from a CRM, accounting, ad accounts, YouTube Studio"), t("файл в чат, ИИ пишет код", "file into a chat, AI writes code")),
             ("amber", "db", t("Базы данных", "Databases"), t("CRM, сайт, склад: миллионы строк, обновляются каждый день", "CRM, website, warehouse: millions of rows, updated daily"), t("ИИ пишет SQL-запрос", "AI writes an SQL query")),
             ("violet", "chat", t("Тексты", "Text"), t("отзывы, письма, чаты поддержки, опросы", "reviews, e-mails, support chats, surveys"), t("ИИ читает и раскладывает на темы", "AI reads and sorts into themes")),
             ("red", "sheet", t("Документы", "Documents"), t("PDF-счета, договоры, отчёты партнёров", "PDF invoices, contracts, partner reports"), t("ИИ достаёт цифры в таблицу", "AI pulls the numbers into a table")),
             ("green", "api", t("События и логи", "Events and logs"), t("клики, заказы по минутам, звонки", "clicks, orders by the minute, calls"), t("обычно считает аналитик по базе", "usually an analyst queries the database"))]
    d = "".join(f'<div class="door" style="--k:var(--{k})">{icon(ic, 44, f"var(--{k})")}<div class="h">{h}</div><div class="w">{w}</div><div class="o">{o}</div></div>' for k, ic, h, w, o in tiles)
    return dict(min=3, html=f'''
  {head(t("Часть 1 • что такое данные", "Part 1 • what data is"), t("Где на работе лежат данные", "Where data lives at work"))}
  <div class="body" style="margin-top:14px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">{d}</div>
    <div class="plaque" style="margin-top:16px;">{t("<b>Чаще всего у вас таблица или выгрузка.</b> Иногда текст. Реже база. Сегодня разберём все три.", "<b>Most often you have a spreadsheet or an export.</b> Sometimes text. Less often a database. Today we cover all three.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Прежде чем загружать файлы в чат, договоримся, что такое данные. Это любые записи, из которых можно что-то посчитать или прочитать: таблицы, выгрузки из систем, базы, тексты, документы, логи.",
                      "⏱ 3 min. Before uploading files to a chat, let’s agree what data is: any records you can count or read something from — spreadsheets, system exports, databases, text, documents, logs."),
                    t("В нижней строке каждой плитки — как с этим работает ИИ. Это главное: с таблицей ИИ пишет формулу или код, с текстом читает, с базой пишет запрос. Спросите в чат: «Какие из этих данных есть у вас на работе?»",
                      "The bottom line of each tile says how AI works with it. That’s the key: with a table AI writes a formula or code, with text it reads, with a database it writes a query. Ask the chat: “Which of these do you have at work?”")))


def s_table_text():
    rows = "".join(f'<tr><td>{r["order_date"]}</td><td>{r["channel"]}</td><td>{r["category"]}</td><td>{r["region"]}</td><td class="num">{int(float(r["orders"]))}</td><td class="num">{float(r["revenue"]):,.0f}</td></tr>' for r in RAW[:6])
    rev = REV_RU if LANG == "ru" else REV_EN
    picks = [rev[1], rev[2]] + [x for x in rev if x["warehouse"] == "N2" and x["review_date"] >= "2025-09" and x["rating"] in ("1", "2")][:2]
    rv = "".join(f'<div class="rv"><span class="rv-s">{"★" * int(x["rating"])}</span> {x["comment"]}<small>{x["warehouse"]} · {x["review_date"]}</small></div>' for x in picks)
    return dict(min=3, html=f'''
  {head(t("Часть 1 • два вида данных", "Part 1 • two kinds of data"), t("Таблица и текст: ИИ работает с ними по-разному", "Table and text: AI handles them differently"))}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:32px;align-items:start;">
      <div class="stack" style="gap:10px;">
        <div class="cap" style="font-size:22px;font-weight:700;color:var(--fg);">{t("Лист Sales: числа, даты, категории", "Sales sheet: numbers, dates, categories")}</div>
        <table class="tbl"><tr><th>date</th><th>channel</th><th>category</th><th>region</th><th class="num">orders</th><th class="num">revenue</th></tr>{rows}</table>
        <div class="note" style="--k:var(--cyan)">{t("<b>ИИ считает:</b> пишет формулу или код, программа складывает и делит. Ошибка — неверная формула.", "<b>AI counts:</b> it writes a formula or code, a program adds and divides. The typical error is a wrong formula.")}</div>
      </div>
      <div class="stack" style="gap:10px;">
        <div class="cap" style="font-size:22px;font-weight:700;color:var(--fg);">{t("Лист Reviews: живые фразы покупателей", "Reviews sheet: customers’ own words")}</div>
        <div class="rvs">{rv}</div>
        <div class="note" style="--k:var(--violet)">{t("<b>ИИ читает:</b> относит каждый отзыв к теме и считает темы. Ошибка — не та тема.", "<b>AI reads:</b> it assigns each review to a theme and counts themes. The typical error is the wrong theme.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Слева настоящие первые строки листа Sales, справа настоящие отзывы из листа Reviews того же файла. Это два разных мира.",
                      "⏱ 3 min. Left: the real first rows of the Sales sheet. Right: real reviews from the Reviews sheet of the same file. These are two different worlds."),
                    t("С таблицей ИИ сам ничего не складывает в уме: он пишет формулу или код, считает программа. Ошибка обычно в формуле — не тот столбец, не тот период. С текстом наоборот: ИИ сам читает каждый отзыв и решает, о чём он. Ошибка — неверная тема. Через полчаса мы увидим именно такую ошибку.",
                      "With a table, AI doesn’t add in its head: it writes a formula or code, a program counts. Errors are usually in the formula — wrong column, wrong period. With text it’s the opposite: AI reads each review and decides what it is about. The error is a wrong theme. In half an hour we’ll see exactly that error.")))


def s_anatomy_row():
    r = RAW[11]
    cells = [("order_date", r["order_date"], "cyan", t("дата", "date")), ("channel", r["channel"], "violet", t("категория", "category")),
             ("category", r["category"], "violet", t("категория", "category")), ("region", r["region"], "violet", t("категория", "category")),
             ("warehouse", r["warehouse"], "violet", t("категория", "category")), ("orders", r["orders"], "green", t("число, шт.", "number, pcs")),
             ("revenue", r["revenue"], "amber", t("число, $", "number, $")), ("ad_spend", r["ad_spend"], "amber", t("число, $", "number, $")),
             ("returns", r["returns"], "green", t("число, шт.", "number, pcs"))]
    head_row = "".join(f'<th style="border-bottom:4px solid var(--{k})">{c}</th>' for c, _, k, _ in cells)
    val_row = "".join(f'<td class="big">{v}</td>' for _, v, _, _ in cells)
    typ_row = "".join(f'<td class="typ" style="color:var(--{k})">{ty}</td>' for _, _, k, ty in cells)
    return dict(min=3, html=f'''
  {head(t("Часть 1 • из чего состоит таблица", "Part 1 • what a table is made of"), t("Одна строка: что это за запись и что в ней измеряют", "One row: what the record is and what it measures"))}
  <div class="body" style="margin-top:14px;">
    <table class="tbl rowx"><tr>{head_row}</tr><tr>{val_row}</tr><tr>{typ_row}</tr></table>
    <div class="row" style="grid-template-columns:repeat(3,1fr);gap:20px;margin-top:26px;flex:0 0 auto;">
      <div class="note" style="--k:var(--cyan)">{t("<b>Строка</b> — продажи одного канала по одной категории, региону и складу за день. Не заказ и не клиент.", "<b>A row</b> is the sales of one channel for one category, region and warehouse on one day. Not an order, not a customer.")}</div>
      <div class="note" style="--k:var(--violet)">{t("<b>Категории</b> — то, по чему режем: канал, регион, склад. По ним строят разрезы.", "<b>Categories</b> are what we slice by: channel, region, warehouse. Breakdowns are built on them.")}</div>
      <div class="note" style="--k:var(--amber)">{t("<b>Числа</b> — то, что складываем и делим. У каждого свои единицы: доллары или штуки.", "<b>Numbers</b> are what we add and divide. Each has its unit: dollars or pieces.")}</div>
    </div>
    <div class="plaque" style="margin-top:20px;">{t("<b>Первый вопрос к любому файлу:</b> что такое одна строка? Если перепутать, все «средние на клиента» будут неверны.", "<b>First question for any file:</b> what is one row? Get it wrong and every “average per customer” is wrong.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Одна настоящая строка файла крупно. Пройдите по цветам: голубой — дата, фиолетовый — категории, по которым режем, зелёный и жёлтый — числа со своими единицами.",
                      "⏱ 3 min. One real row of the file, enlarged. Walk through the colours: blue is the date, violet the categories we slice by, green and amber the numbers with their units."),
                    t(f"Вопрос в чат: «Что такое одна строка в этом файле?» Частый ответ — «заказ». Неверно: в этой строке {r["orders"]} заказов. Это продажи канала за день в одном разрезе. Модель тоже может ошибиться, поэтому первый промпт урока просит её описать строку.",
                      f"Ask the chat: “What is one row in this file?” A common answer is “an order”. Wrong: this row holds {r["orders"]} orders. It is a channel’s sales for a day in one slice. The model can get this wrong too, so the first prompt of the lesson asks it to describe a row.")))


def s_scale():
    steps = [(73, t("десятки строк", "dozens of rows"), t("можно вставить прямо в сообщение", "can be pasted into a message"), "green"),
             (1261, t("тысячи строк", "thousands of rows"), t("наш файл Northstar: загружаем файлом", "our Northstar file: upload as a file"), "cyan"),
             (46132, t("десятки тысяч", "tens of thousands"), t("срез базы каналов: файл ещё работает", "channel DB sample: a file still works"), "violet"),
             (416809, t("сотни тысяч и больше", "hundreds of thousands+"), t("вся база видео: спрашиваем базу запросом", "the whole video DB: ask the database with a query"), "amber")]
    import math
    mx = math.log10(416809)
    hb = "".join(f'<div class="hb" style="--k:var(--{k})"><div class="lab">{lab}<small>{d}</small></div>'
                 f'<div class="tr" style="height:52px"><div class="b" style="width:{math.log10(n) / mx * 62:.1f}%"></div>'
                 f'<div class="v" style="left:calc({math.log10(n) / mx * 62:.1f}% + 14px);font-size:38px;">{num(n)}</div></div></div>' for n, lab, d, k in steps)
    return dict(min=3, html=f'''
  {head(t("Часть 1 • сколько данных", "Part 1 • how much data"), t("От размера данных зависит, куда их нести", "Size decides where the data goes"))}
  <div class="body" style="margin-top:16px;">
    <div class="hbars" style="gap:26px;">{hb}</div>
    <div class="cap" style="margin-top:14px;">{t("Шкала логарифмическая: каждая ступень примерно в 10 раз больше предыдущей.", "Log scale: each step is roughly 10× the previous one.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Четыре ступени. Десятки строк можно вставить текстом прямо в сообщение. Тысячи, как наш файл, загружаем файлом. Десятки тысяч, как срез базы каналов, файл ещё выдерживает. Сотни тысяч и миллионы, да ещё обновляемые каждый день, в файл не выгружают: базу спрашивают запросом.",
                      "⏱ 3 min. Four steps. Dozens of rows can be pasted as text into a message. Thousands, like our file, go in as a file. Tens of thousands, like the channel DB sample, a file still handles. Hundreds of thousands and millions, updated daily, aren’t exported to a file: you ask the database with a query."),
                    t("Шкала логарифмическая, иначе первые три полоски были бы не видны. На практике чат начинает заметно тормозить от нескольких десятков тысяч строк.",
                      "The scale is logarithmic, otherwise the first three bars would be invisible. In practice a chat slows down noticeably from a few tens of thousands of rows.")))


def s_ai_data():
    g, mut, fg = "#5f6e84", "#a3b1c4", "#f1f5f9"
    c = {"cy": "#38bdf8", "gr": "#34d399", "am": "#fbbf24", "vi": "#c084fc"}

    def box(x, y, w, h, col, title, sub):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#0f1624" stroke="{col}" stroke-width="2.5"/>'
                f'<text x="{x + w / 2}" y="{y + 38}" text-anchor="middle" font-size="24" font-weight="700" fill="{fg}">{title}</text>'
                f'<text x="{x + w / 2}" y="{y + 68}" text-anchor="middle" font-size="18" fill="{mut}">{sub}</text>')
    svg = '<svg class="dia" viewBox="0 0 1440 470">' + ARROW.format(id="ad", c=g)
    svg += (f'<text x="20" y="40" font-size="20" font-weight="700" fill="{c["gr"]}">{t("ДАННЫЕ", "DATA")}</text>'
            f'<text x="20" y="300" font-size="20" font-weight="700" fill="{c["vi"]}">{t("ИИ", "AI")}</text>'
            f'<line x1="20" y1="230" x2="1420" y2="230" stroke="{g}" stroke-dasharray="6 6"/>')
    svg += box(120, 60, 300, 100, c["gr"], t("файл или база", "file or database"), t("1 261 строка остаётся там", "1,261 rows stay there"))
    svg += box(560, 60, 320, 100, c["gr"], t("программа считает", "a program counts"), t("Excel · Python · база", "Excel · Python · database"))
    svg += box(1020, 60, 300, 100, c["gr"], t("результат", "result"), t("таблица · график · файл", "table · chart · file"))
    svg += box(120, 320, 300, 100, c["cy"], t("ваш вопрос", "your question"), t("обычными словами", "in plain words"))
    svg += box(560, 320, 320, 100, c["vi"], t("модель пишет", "the model writes"), t("формулу · код · SQL", "formula · code · SQL"))
    svg += box(1020, 320, 300, 100, c["vi"], t("модель объясняет", "the model explains"), t("словами, с числами", "in words, with numbers"))
    for x1, y1, x2, y2 in ((420, 370, 552, 370), (720, 320, 720, 168), (880, 110, 1012, 110), (1170, 160, 1170, 312), (420, 110, 552, 110)):
        svg += f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{g}" stroke-width="3" fill="none" marker-end="url(#ad)"/>'
    svg += (f'<text x="736" y="250" font-size="18" fill="{mut}">{t("код уходит к данным", "code goes to the data")}</text>'
            f'<circle cx="270" cy="440" r="0"/>'
            f'<text x="1180" y="250" font-size="18" fill="{mut}">{t("ответ возвращается", "the answer comes back")}</text>')
    svg += '</svg>'
    return dict(min=3, html=f'''
  {head(t("Часть 1 • главная схема урока", "Part 1 • the key diagram"), t("Данные остаются в файле. ИИ пишет инструкцию, считает программа", "Data stays in the file. AI writes instructions, a program counts"), k="violet")}
  <div class="body" style="margin-top:6px;">
    {svg}
    <div class="row" style="grid-template-columns:1fr 1fr;gap:24px;flex:0 0 auto;">
      <div class="plaque">{t("<b>Вы в двух точках:</b> задаёте вопрос и проверяете результат.", "<b>You stand at two points:</b> asking the question and checking the result.")}</div>
      <div class="plaque g">{t("<b>Правило:</b> если ИИ называет число, спросите, какой программой оно посчитано.", "<b>Rule:</b> when AI states a number, ask which program computed it.")}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Это главная схема урока, к ней будем возвращаться. Верхняя дорожка — данные: файл или база, программа, которая считает, результат. Нижняя — ИИ: он читает ваш вопрос и названия колонок, пишет формулу, код или запрос. Эта инструкция уходит к данным, программа выполняет её, а модель пересказывает результат словами.",
                      "⏱ 3 min. This is the key diagram; we’ll come back to it. Top lane — data: the file or database, the program that counts, the result. Bottom lane — AI: it reads your question and the column names, writes a formula, code or a query. That instruction goes to the data, the program runs it, and the model retells the result in words."),
                    t("Отсюда простое правило: число из ответа ИИ должно быть посчитано программой. Если модель «просто знает» число, это догадка. Вы стоите в двух точках: в начале задаёте вопрос, в конце проверяете.",
                      "Hence a simple rule: a number in an AI answer should be computed by a program. If the model “just knows” a number, it’s a guess. You stand at two points: you ask at the start and check at the end.")))


def s_data_problems():
    dup = next(r for i, r in enumerate(RAW) if tuple(r.values()) in {tuple(x.values()) for x in RAW[:i]})
    items = [("red", t("Дубль строки", "A duplicated row"), f'{dup["order_date"]} · {dup["channel"]} · {dup["category"]} · {float(dup["revenue"]):,.1f} ×2', t("выручка завышена на эту сумму", "revenue is inflated by this amount")),
             ("amber", t("Дата текстом", "A date as text"), f'{TEXT_DATE}  ←  2025-05-10?', t("10 мая или 5 октября? Зависит от формата", "10 May or 5 October? Depends on the format")),
             ("violet", t("Ноль или пропуск?", "Zero or missing?"), "Email · ad_spend = 0", t("у Email рекламы нет. Модель назвала такие нули «пропусками»", "Email has no ads. The model called these zeros “missing”")),
             ("cyan", t("Разные единицы", "Mixed units"), t("1 200 (руб.) и 15 ($) в одной колонке", "1,200 (RUB) and 15 ($) in one column"), t("пример из жизни: сложить их нельзя", "a real-life example: they can’t be added"))]
    d = "".join(f'<div class="door" style="--k:var(--{k})"><div class="h">{h}</div><div class="code" style="font-size:18px;padding:10px 12px;white-space:normal;">{c}</div><div class="w">{w}</div></div>' for k, h, c, w in items)
    return dict(min=3, html=f'''
  {head(t("Часть 1 • живые данные", "Part 1 • real data"), t("Четыре ловушки в живых данных, три — из нашего файла", "Four traps in real data, three of them in our file"), k="red")}
  <div class="body" style="margin-top:16px;">
    <div class="doors">{d}</div>
    <div class="plaque" style="margin-top:20px;">{t("<b>Модель такие вещи часто находит, но не всегда правильно понимает.</b> Что значит ноль и какая дата верная, знает владелец данных.", "<b>The model often finds these, but doesn’t always understand them.</b> The data owner knows what a zero means and which date is right.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. В учебный файл мы специально положили несколько типичных проблем. Дубль: одна строка продаж записана дважды, выручка завышена. Дата текстом 10/05/2025: это 10 мая или 5 октября? Нули в рекламе у Email и Organic: рекламы там просто нет. Разные единицы — пример из жизни, его в нашем файле нет.",
                      "⏱ 3 min. We deliberately put a few typical problems into the practice file. A duplicate: one sales row written twice, revenue inflated. A text date 10/05/2025: is it 10 May or 5 October? Zeros in ad spend for Email and Organic: they simply have no ads. Mixed units is a real-life example, not in our file."),
                    t("Почему это важно: в нашем прогоне ChatGPT сам нашёл дубль, но нули назвал «пропусками», а дату текстом не заметил. Модель видит странности, но смысл знает только владелец данных.",
                      "Why it matters: in our run ChatGPT found the duplicate itself, but called the zeros “missing” and missed the text date. The model sees oddities, but only the data owner knows the meaning.")))


def s_nocode():
    return dict(min=3, html=f'''
  {head(t("Часть 1 • эксперимент", "Part 1 • experiment"), t("73 строки прямо в сообщении: модель посчитала верно. Почему так всё равно не делаем", "73 rows pasted into a message: the model got it right. Why we still don’t do it"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:0.75fr 1fr;gap:26px;align-items:start;">
      <div class="stack" style="gap:8px;">
        {shot("b0_paste", t("запрос: 73 строки CSV, «без инструментов и кода»", "prompt: 73 CSV rows, “no tools or code”"), k="amber", h=330)}
      </div>
      <div class="stack" style="gap:10px;">
        {shot("b0_answer", t("ответ ChatGPT, 17.10.2026", "ChatGPT answer, 17 Oct 2026"), k="green", cls="good", h=300)}
        <div class="big3">
          <div class="note" style="--k:var(--green)">{t("<b>Сумма верная</b>, дубль и пустой регион найдены.", "<b>The total is right</b>; the duplicate and blank region found.")}</div>
          <div class="note" style="--k:var(--red)">{t("<b>Хода расчёта не видно.</b> Повторить и проверить нечем.", "<b>No visible working.</b> Nothing to repeat or check.")}</div>
          <div class="note" style="--k:var(--amber)">{t("<b>1 261 строку</b> так уже не вставишь. Нужен файл и код.", "<b>1,261 rows</b> won’t paste like this. You need a file and code.")}</div>
        </div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Настоящий прогон 17 октября 2026: мы вставили 73 строки учебного CSV прямо в сообщение и попросили не пользоваться инструментами. ChatGPT посчитал выручку верно (256 045 без дубля) и нашёл все четыре проблемы. Про строку с 66 возвратами при 62 заказах написал «требует проверки».",
                      "⏱ 3 min. A real run on 17 Oct 2026: we pasted 73 rows of the practice CSV into a message and asked for no tools. ChatGPT got revenue right (256,045 without the duplicate) and found all four problems. For the row with 66 returns on 62 orders it said “needs checking”."),
                    t("Для сравнения: 13 октября на том же файле другие модели без кода «починили» эту строку: «вероятно, 6», хотя в источнике было 4. Модели стали аккуратнее. Но хода расчёта не видно, и реальный файл на тысячи строк в сообщение не поместится. Поэтому дальше работаем с файлом и смотрим, какой код написала модель.",
                      "For comparison: on 13 Oct, on the same file, other models without code “fixed” that row to “probably 6”, while the source said 4. Models have become more careful. But the working is invisible, and a real file of thousands of rows won’t fit in a message. So from here on we work with the file and look at the code the model wrote.")))


def s_p1_anatomy():
    lines = [(t("Опиши этот файл: что такое одна строка,", "Describe this file: what one row is,"), t("сначала понять данные, а не считать", "understand the data first, not compute"), "cyan"),
             (t("сколько строк, какой период,", "how many rows, what period,"), t("числа, которые вы потом сверите", "numbers you’ll check later"), "green"),
             (t("какие проблемы в данных.", "what data problems."), t("дубли и странности — до расчётов", "duplicates and oddities — before any maths"), "amber"),
             (t("Предложи 5 вопросов, которые задал бы руководитель.", "Suggest 5 questions a manager would ask."), t("план работы: выбираем вопрос из письма", "a work plan: pick the question from the e-mail"), "violet"),
             (t("Ничего пока не меняй.", "Don’t change anything yet."), t("иначе модель молча «почистит» файл", "or the model quietly “cleans” the file"), "red")]
    return dict(min=3, html=f'''
  {head(t("Часть 2 • промпт 1 по строкам", "Part 2 • prompt 1 line by line"), t("Первый промпт к любому файлу: опись, а не «найди инсайты»", "The first prompt for any file: a description"))}
  <div class="body" style="margin-top:16px;">
    {anatomy(lines)}
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Разберите промпт по строкам. Первая строка заставляет модель сначала понять, что лежит в файле. Вторая даёт числа для сверки: 1 261 строка, 2025 год. Третья просит найти проблемы до расчётов. Четвёртая превращает ответ в план: пять вопросов руководителя. Пятая запрещает молча править файл.",
                      "⏱ 3 min. Go through the prompt line by line. Line 1 makes the model understand the file first. Line 2 gives numbers to check: 1,261 rows, 2025. Line 3 asks for problems before any maths. Line 4 turns the answer into a plan: five manager questions. Line 5 forbids silent edits."),
                    t("Промпт целиком лежит в шпаргалке. Студентам его можно копировать для любого своего файла.",
                      "The full prompt is in the cheatsheet. Students can copy it for any file of their own.")))


def s_bg_insights():
    return dict(min=4, html=f'''
  {head(t("Быстро / под контролем #1", "Quick / under control #1"), t("«Найди инсайты» тоже работает. Но вопросы выбирает модель", "“Find insights” works too. But the model picks the questions"), k="amber")}
  <div class="body" style="margin-top:10px;">
    {badgood(t("«Вот файл. Найди интересные инсайты.»", "“Here is the file. Find interesting insights.”"), [("b1_top", 360), ("b1_dup", 80)],
             t("Промпт 1: опись + 5 вопросов + ничего не меняй", "Prompt 1: description + 5 questions + change nothing"), [("p1_questions", 330)],
             t("Модель нашла Social и N2. Но сравнения выбрала сама (кварталы), а дубль <b>оставила в расчётах</b>.", "The model found Social and N2. But it chose the comparisons itself (quarters) and <b>kept the duplicate in the maths</b>."),
             t("✓ 1 261 строка, период, дубль · ✗ 632 нуля в рекламе назвала «пропусками» · ✗ дату текстом не заметила. <b>Берём вопрос 1.</b>", "✓ 1,261 rows, period, duplicate · ✗ called 632 zero ad-spend values “missing” · ✗ missed the text date. <b>We take question 1.</b>"))}
  </div>''',
                notes=notes(
                    t("⏱ 4 мин. Результат 17 октября: на «найди интересные инсайты» ChatGPT за полторы минуты нашёл обе главные истории — падение отдачи Social и возвраты на складе N2. Модели стали сильными.",
                      "⏱ 4 min. An honest result from 17 Oct: on “find interesting insights” ChatGPT found both main stories in a minute and a half — Social’s falling return and N2 returns. Models have become strong."),
                    t("Справа ответ на промпт 1. Отметьте вслух, что верно: 1 261 строка, период, дубль. И что нет: «отсутствуют 632 значения ad_spend» — это нули, у Email и Organic рекламы нет; дату текстом 10/05/2025 модель не заметила. Переспросите: «Это пропуски или нули?» Из пяти вопросов берём первый, про каналы с учётом рекламы, — он совпадает с письмом.",
                      "On the right: the answer to prompt 1. Say aloud what is right: 1,261 rows, period, duplicate. And what isn’t: “632 ad_spend values missing” — they are zeros, Email and Organic have no ads; the model missed the text date 10/05/2025. Ask back: “Missing or zeros?” Of the five questions we take the first, channels including ad spend — it matches the e-mail."),
                    t("Но посмотрите внимательнее. Сравнения модель выбрала сама: кварталы, полугодия. Дубль нашла, но написала «расчёты сохраняют исходные строки» — то есть дубль остался в цифрах. На вопрос Анны «что с продажами за год» прямого ответа нет. Промпт-опись даёт план и оставляет выбор вам.",
                      "But look closer. The model chose the comparisons itself: quarters, half-years. It found the duplicate but wrote “calculations keep the original rows” — so the duplicate stayed in the numbers. Anna’s question “how did sales go this year” has no direct answer. The description prompt gives a plan and leaves the choice to you.")))


def s_p2_anatomy():
    lines = [(t("Добавь в книгу лист «Отдача рекламы»:", "Add a sheet “Ad return” to the workbook:"), t("где появится результат", "where the result appears"), "cyan"),
             (t("по месяцам … для Search и Social.", "by month … for Search and Social."), t("разрез: время и каналы", "the breakdown: time and channels"), "violet"),
             (t("выручка, рекламный расход и выручка на $1 рекламы.", "revenue, ad spend and revenue per $1 of ads."), t("метрика: выручка ÷ расход", "the metric: revenue ÷ spend"), "amber"),
             (t("Считай формулами Excel, а не готовыми числами.", "Use Excel formulas, not pasted numbers."), t("чтобы проверить и пересчитать", "so you can check and recalculate"), "green"),
             (t("Построй линейный график", "Build a line chart"), t("тип под вопрос «как менялось»", "the type for “how did it change”"), "violet"),
             (t("и дай скачать .xlsx.", "and let me download the .xlsx."), t("результат — файл, а не текст в чате", "the result is a file, not chat text"), "cyan")]
    return dict(min=3, html=f'''
  {head(t("Часть 2 • промпт 2 по строкам", "Part 2 • prompt 2 line by line"), t("Формула словами: каждая строка промпта за что-то отвечает", "A formula in words: each line has a job"), k="green")}
  <div class="body" style="margin-top:16px;">
    {anatomy(lines, "green")}
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Это вопрос 1 из ответа модели: какие каналы выгоднее с учётом рекламы. Разбираем промпт. Где результат — новый лист. Разрез — месяцы и два рекламных канала. Метрика — выручка на доллар рекламы, то есть выручка, делённая на расход. Формулы, а не числа — иначе проверить нечего. Линейный график — потому что вопрос «как менялось во времени». И файл на выходе.",
                      "⏱ 3 min. This is question 1 from the model’s answer: which channels pay off including ad spend. Line by line: where the result goes — a new sheet; the breakdown — months and two ad channels; the metric — revenue per ad dollar, i.e. revenue divided by spend; formulas, not numbers — otherwise nothing to check; a line chart — because the question is “how did it change over time”; and a file as output."),))


def s_bg_formulas():
    return dict(min=3, html=f'''
  {head(t("Быстро / под контролем #2", "Quick / under control #2"), t("Числа в ячейках проверить нельзя. Формулы — можно", "Numbers in cells can’t be checked. Formulas can"), k="green")}
  <div class="body" style="margin-top:10px;gap:12px;">
    <div class="row" style="grid-template-columns:330px 1fr;gap:20px;align-items:center;flex:0 0 auto;">
      <div class="stack" style="gap:8px;"><div class="bg-q" style="--k:var(--amber)"><span class="badge solid" style="--k:var(--amber)">{t("Быстро", "Quick")}</span> {t("Лист из ChatGPT: в ячейках готовые числа", "Sheet from ChatGPT: plain numbers in the cells")}</div>
        <div class="note" style="--k:var(--amber)">{t("Откуда 5,39 — не видно. Поменяли файл — числа не пересчитались.", "Where 5.39 comes from is invisible. Change the file — numbers don’t update.")}</div></div>
      {shot("p2_roas_sheet", None, k="amber", h=300)}
    </div>
    <div class="row" style="grid-template-columns:330px 1fr;gap:20px;align-items:center;flex:0 0 auto;margin-top:14px;">
      <div class="stack" style="gap:8px;"><div class="bg-q" style="--k:var(--green)"><span class="badge solid" style="--k:var(--green)">{t("✓ Под контролем", "✓ Under control")}</span> {t("Excel: в строке fx формула СУММЕСЛИМН", "Excel: a SUMIFS formula in the fx bar")}</div>
        <div class="note" style="--k:var(--green)">{t("Видно, какие столбцы сложены и за какой месяц. Исправление одной фразой: «замени числа формулами».", "You can see which columns are summed for which month. The fix is one phrase: “replace the numbers with formulas”.")}</div></div>
      {shot("xl_fx_sumifs", None, k="green", cls="good")}
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Слева реальный лист, который вернул ChatGPT в нашем прогоне: в ячейках числа. Справа та же таблица в Excel, где выручка посчитана формулой СУММЕСЛИМН по листу Sales, а отдача — делением =B2/C2. Числа совпадают, но проверить можно только правую.",
                      "⏱ 3 min. Left: the real sheet ChatGPT returned in our run — numbers in the cells. Right: the same table in Excel, revenue as SUMIFS over the Sales sheet and return as =B2/C2. The numbers match, but only the right one can be checked."),
                    t("Правило: щёлкните любую ячейку с результатом. Видите число — попросите «замени числа формулами». Эталонная книга: demo_v2/excel_demo/northstar_2025_formulas.xlsx.",
                      "Rule: click any result cell. See a number — ask “replace the numbers with formulas”. Reference workbook: demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx.")))


def s_bg_growth():
    return dict(min=4, html=f'''
  {head(t("Плохо / хорошо • сезонность", "Weak / good • seasonality"), t("«Одно число для слайда» — и модель выбрала самое громкое", "“One number for the slide” — and the model picked the loudest"), k="amber")}
  <div class="body" style="margin-top:10px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:28px;align-items:start;">
      <div class="stack" style="gap:8px;">
        <div class="bg-q" style="--k:var(--red)"><span class="badge solid" style="--k:var(--red)">{t("✗ Так себе", "✗ Weak")}</span> {t("«Насколько выросли продажи за год? Одним числом для слайда.»", "“How much did sales grow this year? One number for the slide.”")}</div>
        {shot("b3_bad", None, k="red", cls="bad", h=120)}
        <div class="note" style="--k:var(--red)">{t("+161,7 % — декабрь к январю. Январь — самый слабый месяц, декабрь — распродажи. Звучит как рост бизнеса, а это сезон.", "+161.7% is December vs January. January is the weakest month, December is sales season. It sounds like growth; it’s the season.")}</div>
        <div class="cap" style="font-size:20px;font-weight:700;color:var(--fg);margin-top:6px;">{t("Выручка по месяцам", "Revenue by month")}</div>
        {s6_chart(1000, 380)}
      </div>
      <div class="stack" style="gap:8px;">
        <div class="bg-q" style="--k:var(--green)"><span class="badge solid" style="--k:var(--green)">{t("✓ Хорошо", "✓ Good")}</span> {t("«Посчитай рост тремя способами, для каждого укажи базу и период. Какое число на слайд и почему?»", "“Compute growth three ways, give the base and period for each. Which number goes on the slide and why?”")}</div>
        {shot("b3_table", None, k="green", cls="good", h=420)}
        <div class="note" style="--k:var(--green)">{t("Три числа с базой и вывод: на слайд — «второе полугодие примерно на 40 % выше первого».", "Three numbers with their base and a verdict: “the second half is about 40% above the first”.")}</div>
      </div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Настоящий прогон 17 октября. На просьбу дать «одно число для слайда» модель ответила: «+161,7 % — рост выручки декабря к январю». Число верное, но январь после праздников — самый слабый месяц, а декабрь — распродажи. Руководитель прочтёт это как рост бизнеса в два с половиной раза.",
                      "⏱ 3 min. A real run from 17 Oct. Asked for “one number for the slide”, the model said: “+161.7% — December revenue vs January”. The number is right, but January after the holidays is the weakest month and December is sales season. A manager will read it as the business growing 2.5×."),
                    t("Хороший запрос просит три способа и базу для каждого. Модель сама предложила число, которое не вводит в заблуждение: второе полугодие к первому, около 40 %, и оговорилась, что данных за 2024 год нет, поэтому «год к году» сказать нельзя. Слева внизу график из нашего файла, на нём видны обе базы.",
                      "The good prompt asks for three ways and the base for each. The model itself proposed the fair number: second half vs first, about 40%, and noted there is no 2024 data, so “year over year” can’t be claimed. Bottom left: the chart from our file showing both bases."),
                    t("Текст первого запроса на слайде набран заново: в окне чата он при вводе задвоился, ответ от этого не зависит.",
                      "The first prompt’s text on the slide is retyped: in the chat window it got duplicated while typing; the answer doesn’t depend on it.")))


def s_p34_anatomy():
    l3 = [(t("Посчитай долю возвратов", "Compute the return rate"), t("метрика: возвраты ÷ заказы", "metric: returns ÷ orders"), "amber"),
          (t("по регионам и категориям", "by region and category"), t("разрез: две оси таблицы", "breakdown: two axes"), "violet"),
          (t("за сентябрь–декабрь", "for September–December"), t("период, о котором спросила Анна", "the period Anna asked about"), "cyan"),
          (t("и покажи тепловой картой.", "and show it as a heatmap."), t("тип: аномалия видна цветом", "type: the outlier shows as colour"), "green")]
    l4 = [(t("Для склада с самой высокой долей возвратов", "For the warehouse with the highest return rate"), t("модель сама находит разрез", "the model finds the slice"), "amber"),
          (t("разложи отзывы на темы", "sort the reviews into themes"), t("текст → категории", "text → categories"), "violet"),
          (t("и сравни с остальными складами.", "and compare with the other warehouses."), t("база сравнения", "the base for comparison"), "cyan"),
          (t("Покажи 5 примеров отзывов.", "Show 5 example reviews."), t("проверка глазами", "a check by eye"), "green")]
    return dict(min=5, html=f'''
  {head(t("Часть 3 • демо 2 • промпты 3 и 4", "Part 3 • demo 2 • prompts 3 and 4"), t("За год 6 % возвратов. В одной клетке — 24,8 %", "6% returns for the year. One cell shows 24.8%"), k="violet")}
  <div class="body" style="margin-top:12px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:26px;align-items:start;">
      <div class="stack" style="gap:8px;"><div class="cap" style="font-size:21px;font-weight:700;color:var(--fg);">{t("Промпт 3 — таблица", "Prompt 3 — the table")}</div>{anatomy(l3)}{shot("p3_heatmap", t("результат: 24,8 % в одной клетке", "result: 24.8% in one cell"), k="violet", h=260)}</div>
      <div class="stack" style="gap:8px;"><div class="cap" style="font-size:21px;font-weight:700;color:var(--fg);">{t("Промпт 4 — текст", "Prompt 4 — the text")}</div>{anatomy(l4)}{shot("p3_themes_before", t("результат: темы отзывов N2 и остальных · промпт 5 → слайд 21", "result: N2 vs other review themes · prompt 5 → slide 21"), k="violet", h=260)}</div>
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Третий вопрос письма — возвраты осенью. Промпт 3 работает с таблицей: метрика, разрез, период, тип графика. Промпт 4 работает с текстом: модель сама находит склад с худшей долей, раскладывает отзывы на темы и сравнивает с остальными. «Покажи 5 примеров» — чтобы вы могли проверить темы глазами.",
                      "⏱ 3 min. The e-mail’s third question is autumn returns. Prompt 3 works with the table: metric, breakdown, period, chart type. Prompt 4 works with text: the model finds the worst warehouse, sorts reviews into themes and compares with the rest. “Show 5 examples” lets you check the themes by eye."),
                    t("Демо: тот же чат, файл уже загружен. После каждого ответа раскройте код (блок «Анализ завершён» или кнопка кода над графиком). Под разбором — реальные результаты: на тепловой карте одна клетка горит, North × Electronics — 24,8 % против примерно 5 %. Это и есть склад N2. Темы отзывов: «упаковка / повреждения» у N2 — 49 %, у остальных 12 %. Ответ дольше 90 секунд — показываем кадр." + EN_SHOTS,
                      "Demo: same chat, the file is already uploaded. Open the code after each answer (the “Analysis complete” block or the code button above the chart). Under the breakdown are the real results: one heatmap cell lights up, North × Electronics at 24.8% vs about 5%. That is warehouse N2. Review themes: “packaging / damage” is 49% at N2 and 12% elsewhere. Answer over 90 seconds — show the frame." + EN_SHOTS)))


def s_sql_anatomy():
    lines = [("SELECT duration_bucket,", t("что показать: длительность", "what to show: length"), "cyan"),
             ("COUNT(*) AS videos,", t("сколько видео в группе", "how many videos in the group"), "green"),
             ("MEDIAN(views) AS typical", t("типичные просмотры: половина выше, половина ниже", "typical views: half above, half below"), "amber"),
             ("FROM videos", t("из какой таблицы", "from which table"), "violet"),
             ("GROUP BY duration_bucket;", t("по какому признаку собрать группы", "what to group by"), "cyan")]
    return dict(min=3, html=f'''
  {head(t("Часть 4 • SQL по строкам", "Part 4 • SQL line by line"), t("SQL читается почти как обычная фраза", "SQL reads almost like a plain sentence"), k="amber")}
  <div class="body" style="margin-top:14px;">
    {pr(t("Промпт", "Prompt"), t("В базе таблица videos: длительность и просмотры каждого видео. Напиши SQL-запрос: видео какой длины набирают больше всего просмотров? Объясни каждую строку.", "The database has a videos table: length and views of every video. Write an SQL query: which video length gets the most views? Explain every line."), k="amber")}
    <div style="margin-top:14px;">{anatomy(lines, "amber")}</div>
    <div class="note" style="--k:var(--amber);margin-top:14px;">{t("<b>Опишите таблицы в промпте.</b> Без описания модель угадывает названия колонок, и запрос падает с ошибкой.", "<b>Describe the tables in the prompt.</b> Without it the model guesses column names and the query fails.")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. Разберите запрос как фразу: выбрать длительность, посчитать видео, взять типичные просмотры, из таблицы видео, собрать группы по длительности. Писать SQL студентам не нужно, нужно уметь прочитать, что посчитала база. MEDIAN есть не во всех базах (в PostgreSQL это PERCENTILE_CONT) — модель подберёт нужную функцию, если назвать вашу базу.",
                      "⏱ 3 min. Read the query as a sentence: select the length, count the videos, take typical views, from the videos table, group by length. Students don’t need to write SQL; they need to read what the database computed. MEDIAN isn’t in every database (PostgreSQL uses PERCENTILE_CONT) — the model picks the right function if you name your database."),
                    t("Про описание таблиц: если модель не видит схему, она придумывает названия колонок. В нашем прогоне ChatGPT вместо этого сам подтянул схему настоящей базы автора из подключённых источников — поэтому тот кадр мы не показываем. На работе так и делайте: давайте модели названия таблиц и колонок, без самих данных.",
                      "On describing tables: if the model can’t see the schema, it invents column names. In our run ChatGPT instead pulled the real schema of the author’s database from connected sources — which is why we don’t show that frame. At work do it on purpose: give the model the table and column names, not the data.")))


def s_db_schema():
    import json
    meta = json.loads((DB / "sample_meta.json").read_text(encoding="utf-8"))
    full = meta["full_db"]
    tables = [("channels", num(full["channels"]), t("один канал", "one channel"), ["title", "subscriber_count", "country", "language"], "cyan"),
              ("videos", num(full["videos"]), t("одно видео", "one video"), ["channel_id → channels", "published_at", "duration_seconds", "tags"], "violet"),
              ("video_stat_observations", num(full["video_stat_observations"]), t("один замер просмотров", "one view measurement"), ["video_id → videos", "observed_at", "views"], "amber")]
    tb = "".join(f'<div class="door" style="--k:var(--{k})"><div class="h" style="font-family:var(--mono);font-size:22px;">{n}</div><div class="stat" style="--k:var(--{k})"><div class="n" style="font-size:40px;">{c}</div><div class="d">{t("строк · строка = ", "rows · row = ")}{one}</div></div>'
                 f'<div class="code" style="font-size:17px;padding:10px 12px;">{"<br>".join(cols)}</div></div>' for n, c, one, cols, k in tables)
    return dict(min=2, html=f'''
  {head(t("Часть 4 • большая база", "Part 4 • a large database"), t("База каналов: три связанные таблицы, обновляются каждый день", "The channel database: three linked tables, updated daily"), k="amber")}
  <div class="body" style="margin-top:14px;">
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;">{tb}</div>
    <div class="flow" style="margin-top:20px;justify-content:center;gap:14px;"><div class="box">channels</div><div class="arr">→</div><div class="box">videos</div><div class="arr">→</div><div class="box">video_stat_observations</div></div>
    <div class="cap" style="margin-top:12px;text-align:center;">{t("Стрелка — связь: у видео есть номер канала, у замера — номер видео. Для урока взят обезличенный срез: 1 943 канала, 46 132 видео.", "An arrow is a link: a video holds its channel id, a measurement holds its video id. For the lesson: an anonymised sample of 1,943 channels and 46,132 videos.")}</div>
  </div>''',
                notes=notes(
                    t(f"⏱ 2 мин. Рабочая база автора курса: кулинарные YouTube-каналы, собранные через официальный API. Три таблицы: каналы ({num(full['channels'])}), видео ({num(full['videos'])}) и замеры просмотров по дням ({num(full['video_stat_observations'])}). Таблицы связаны: у каждого видео есть номер канала, у каждого замера — номер видео.",
                      f"⏱ 2 min. The course author’s working database: cooking YouTube channels collected via the official API. Three tables: channels ({num(full['channels'])}), videos ({num(full['videos'])}) and daily view measurements ({num(full['video_stat_observations'])}). They are linked: each video holds its channel id, each measurement its video id."),
                    t("Почему не файл: таблиц три, они связаны и обновляются каждый день. Выгружать их ради каждого вопроса неудобно. Проще спросить базу запросом, это следующий слайд.",
                      "Why not a file: there are three linked tables updated daily. Exporting them for every question is impractical. It’s simpler to ask the database with a query — the next slide.")))


def s_bg_social():
    return dict(min=3, html=f'''
  {head(t("Часть 3 • быстро / под контролем #3", "Part 3 • quick / under control #3"), t("Первая строка ответа — сценарий, а не прогноз. Читайте допущения", "The first line is a scenario, not a forecast. Read the assumptions"), k="red")}
  <div class="body" style="margin-top:10px;">
    {badgood(t("Первая строка ответа на «Если с января урезать бюджет Social вдвое, сколько мы сэкономим и сколько потеряем выручки за квартал?»", "The first line of the answer to “If we cut the Social budget in half from January, how much do we save and how much revenue do we lose per quarter?”"), [("b5_top", 290)],
             t("Тот же ответ, абзацы ниже", "The same answer, paragraphs below"), [("b5_reco", 330)],
             t("«Потеря выручки — 122,5 тыс.» в первой строке. Это расчёт <b>при условии</b>, что выручка падает вместе с бюджетом.", "“Revenue loss — 122.5k” in the first line. That assumes revenue falls <b>together with</b> the budget."),
             t("Модель сама пишет: точную потерю файл не покажет, нужен тест с контрольной группой.", "The model itself says: the file can’t show the real loss; you need a test with a control group."))}
  </div>''',
                notes=notes(
                    t("⏱ 3 мин. После находки про Social хочется сразу урезать бюджет. Мы спросили модель прямо. Ответ хороший, если дочитать: в первой строке «потеря выручки 122,5 тыс.», но это сценарий «если выручка падает пропорционально бюджету». Ниже модель сама пишет, что фактическую потерю файл не покажет, и предлагает тест на части аудитории.",
                      "⏱ 3 min. After the Social finding it’s tempting to cut the budget at once. We asked the model directly. The answer is good if you read to the end: the first line says “revenue loss 122.5k”, but that is a scenario “if revenue falls in proportion to the budget”. Further down the model says the file can’t show the real loss and suggests a test on part of the audience."),
                    t("Урок: руководитель читает первую строку. Перед тем как нести число дальше, найдите в ответе слова «при условии», «если», «допущение». Таблица говорит, что было. Что будет, покажет только тест.",
                      "The lesson: a manager reads the first line. Before passing a number on, find the words “assuming”, “if”, “scenario” in the answer. The table says what happened. Only a test shows what will happen.")))


SLIDES = [s_cover, s_outcomes, s_data_where, s_table_text, s_anatomy_row, s_scale, s_ai_data, s_data_problems, s_nocode,
          s_hook, s_p1_anatomy, s_bg_insights, s_p2_anatomy, s_bg_formulas, s_demo1, s_bg_growth, s_charts, s_break,
          s_p34_anatomy, s_found, s_makeover, s_check, s_bg_social,
          s_db_schema, s_sql_anatomy, s_db, s_sources, s_report, s_privacy, s_hw, s_summary]


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
        s["notes"] = re.sub(r"⏱ \d+ (мин|min)", lambda m_: f"⏱ {s['min']} {m_.group(1)}", s["notes"], count=1)
        cls = ("slide " + s.get("cls", "")).strip()
        foot = "" if s.get("cls") == "cover" else f'\n  <div class="foot"><span>{FOOT[lang]}</span><span>{i:02d} / {total}</span></div>'
        secs.append(f'<!-- SLIDE {i:02d} · {fn.__name__} · {s["min"]} min -->\n<section class="{cls}" data-n="{i}">{s["html"]}{foot}\n'
                    f'  <template class="notes">{s["notes"]}</template>\n</section>')
    assert minutes + BUFFER == 90, minutes
    title = t("Урок 08: ИИ для анализа данных | GenAI Basics", "Lesson 08: AI for Data Analysis | GenAI Basics")
    tconst = t("{start: 'СТАРТ 5 МИН', pause: 'ПАУЗА', done: 'ВРЕМЯ ВЫШЛО', notes: 'ЗАМЕТКИ СПИКЕРА'}",
               "{start: 'START 5 MIN', pause: 'PAUSE', done: 'TIME IS UP', notes: 'SPEAKER NOTES'}")
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<!-- generated by deck/build_v2.py — edit the generator, not this file -->
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
    print(f"{lang}: {OUT[lang].name} — {total} slides, {minutes} min + {BUFFER} buffer")
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
