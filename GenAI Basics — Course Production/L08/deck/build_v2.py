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
BUFFER = 7  # minutes of slack inside the 90 (demos overrun)

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
    return dict(min=2, cls="cover", html=f'''
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
    return dict(min=3, html=f'''
  {head(t("С чего начинается анализ", "Where analysis starts"), t("Сначала вопрос руководителя, потом файл", "The manager’s question comes first, then the file"), k="amber")}
  <div class="body" style="margin-top:16px;">
    <div class="row" style="grid-template-columns:0.9fr 1.1fr;gap:36px;align-items:stretch;">
      <div class="stack" style="gap:18px;justify-content:center;">
        <div class="plaque" style="font-size:24px;line-height:1.5;">
          <div class="kicker" style="--k:var(--amber);margin-bottom:8px;">{t("Письмо коммерческого директора Анны", "An e-mail from Anna, Commercial Director")}</div>
          <div>{t("Привет! Что у нас с продажами за год? Почему во втором полугодии реклама стала хуже окупаться? И откуда столько возвратов осенью? Нужна одна страница к пятнице.",
                               "Hi! How did sales go this year? Why did advertising pay off worse in the second half? And why so many returns in the autumn? I need one page by Friday.")}</div>
        </div>
        <div class="note" style="--k:var(--amber)">{t("Три вопроса — три графика. «Найди инсайты» здесь не поможет.", "Three questions — three charts. “Find insights” won’t help here.")}</div>
      </div>
      <div class="stack" style="gap:6px;">
        {shot("p2_sales_sheet", t("northstar_2025.xlsx • 1 261 строка", "northstar_2025.xlsx • 1,261 rows"), k="cyan")}
        <div class="scap">{t("Одна строка — продажи одного канала по одной категории, региону и складу за день. Второй лист — 357 отзывов покупателей.", "One row is the sales of one channel for one category, region and warehouse on one day. The second sheet holds 357 customer reviews.")}</div>
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
    return dict(min=4, html=f'''
  {head(t("Шаг 1 • первый промпт", "Step 1 • the first prompt"), t("Первый промпт: опиши файл и предложи 5 вопросов", "First prompt: describe the file and suggest 5 questions"))}
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
    return dict(min=12, html=f'''
  {head(t("Демо 1 • Excel • 12 минут", "Demo 1 • Excel • 12 minutes"), t("Формулу и график можно попросить словами", "You can ask for a formula and a chart in words"), k="green")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:1fr 1fr;gap:24px;align-items:stretch;flex:0 0 auto;">
      <div class="stack" style="gap:12px;">
        {pr(t("Промпт 2", "Prompt 2"), t("Добавь в книгу лист «Отдача рекламы»: по месяцам выручка, рекламный расход и выручка на $1 рекламы для Search и Social. Считай формулами Excel, а не готовыми числами. Построй линейный график и дай скачать .xlsx.",
                                         "Add a sheet “Ad return” to the workbook: by month, revenue, ad spend and revenue per $1 of ads for Search and Social. Use Excel formulas, not pasted numbers. Build a line chart and let me download the .xlsx."), k="green")}
        <div class="note" style="--k:var(--cyan)">{t("Есть Claude или Copilot в Excel? Тот же текст пишем в боковой панели, скачивать ничего не нужно.", "Have Claude or Copilot in Excel? Type the same text in the side panel; nothing to download.")}</div>
      </div>
      <div class="stack" style="gap:6px;">
        {shot("p2_roas_sheet", t("ChatGPT вернул лист: в ячейках числа", "ChatGPT returned a sheet: numbers in the cells"), k="amber", h=200)}
        <div class="scap">{t("Щёлкните ячейку. Видите число — напишите: «замени числа формулами».", "Click a cell. See a number? Write: “replace the numbers with formulas”.")}</div>
      </div>
    </div>
    <div class="stack" style="gap:6px;margin-top:14px;">
      {shot("xl_fx_sumifs", t("Excel: в ячейке формула, её видно в строке fx", "Excel: the cell holds a formula, visible in the fx bar"), k="green", cls="good")}
    </div>
  </div>''',
                notes=notes(
                    t("⏱ 12 мин (2 промпта + открыть книгу). Ведите по ранбуку L08_04. Загрузите northstar_2025.xlsx в ChatGPT. Промпт 1 — описание файла с прошлого слайда. Промпт 2 — на экране.",
                      "⏱ 12 min (2 prompts + open the workbook). Follow runbook L08_04. Upload northstar_2025.xlsx to ChatGPT. Prompt 1 is the file description from the previous slide. Prompt 2 is on screen."),
                    t("Ключевые слова в промпте: «формулами Excel, а не готовыми числами». Без них модель часто вставляет посчитанные значения, и проверить их в книге нельзя. Скачайте файл, откройте в Excel, щёлкните ячейку с отдачей рекламы. В строке формул должно быть деление выручки на расход, например =B2/C2. Выручка и расход тоже должны быть формулами (СУММЕСЛИМН / SUMIFS по листу Sales).",
                      "Key words in the prompt: “Excel formulas, not pasted numbers”. Without them the model often pastes computed values, which can’t be checked in the workbook. Download the file, open it in Excel and click an ad-return cell. The formula bar should show revenue divided by spend, e.g. =B2/C2. Revenue and spend should be formulas too (SUMIFS over the Sales sheet)."),
                    t(f"Что увидим: у Search выручка на $1 рекламы держится около {dec(ROAS['Search'][1], 1)} весь год. У Social с июля падает примерно с 4 до 2. Это вторая история из письма Анны, к ней вернёмся после перерыва.",
                      f"What you will see: Search returns about {dec(ROAS['Search'][1], 1)} per $1 all year. Social drops from about 4 to 2 in July. That is the second story from Anna’s e-mail; we come back to it after the break."),
                    t("Справа вверху реальный лист из книги, которую вернул ChatGPT: в нашем прогоне в ячейках оказались числа, формул не было. Внизу та же таблица в Excel, где выручка посчитана формулой СУММЕСЛИМН по листу Sales, а отдача — делением =B2/C2; рядом график по этим ячейкам. Так должна выглядеть книга после просьбы «замени числа формулами». Эталонная книга: demo_v2/excel_demo/northstar_2025_formulas.xlsx. Если у вас есть Claude for Excel или Copilot, покажите ту же просьбу в боковой панели, 90 секунд. Если сервис думает дольше 90 секунд — показывайте готовые кадры и идите дальше." + EN_SHOTS,
                      "Top right is the real sheet from the workbook ChatGPT returned: in our run the cells held numbers, not formulas. Below is the same table in Excel where revenue is a SUMIFS over the Sales sheet and the return is =B2/C2, with a chart built on those cells. That is how the workbook should look after “replace the numbers with formulas”. Reference workbook: demo_v2/excel_demo/northstar_2025_formulas_EN.xlsx. If you have Claude for Excel or Copilot, show the same request in the side panel, 90 seconds. If the service takes longer than 90 seconds, show the ready frames and move on." + EN_SHOTS)))


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
    return dict(min=4, html=f'''
  {head(t("Графики", "Charts"), t("Пять вопросов — пять графиков. Все из нашего файла", "Five questions, five charts — all from our file"))}
  <div class="body" style="margin-top:16px;">
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;">{m}</div>
    <div class="plaque" style="margin-top:22px;">{t("<b>Просите так:</b> «Построй один график, который отвечает на вопрос …, подпиши оси и единицы». Сначала назовите вопрос, тип графика модель подберёт.", "<b>Ask like this:</b> “Build one chart that answers …, label the axes and units.” Name the question first; the model will pick the chart type.")}</div>
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
            f'{pr(steps[2][2], t("Переделка графика для слайда. Полный текст и результат — на слайде 11.", "Rework the chart for a slide. Full text and result on slide 11."), k="violet")}</div>')
    return dict(min=12, html=f'''
  {head(t("Демо 2 • чат с файлом • 12 минут", "Demo 2 • chat with a file • 12 minutes"), t("За год 6 % возвратов. В одной клетке — 24,8 %", "6% returns for the year. One cell shows 24.8%"), k="violet")}
  <div class="body" style="margin-top:14px;">
    <div class="row" style="grid-template-columns:0.85fr 1.15fr;gap:26px;align-items:start;">{cols}</div>
    <div class="plaque g" style="margin-top:14px;">{t("<b>Задание в чат Teams:</b> какое число на тепловой карте вы бы проверили первым?", "<b>Teams chat task:</b> which number on the heatmap would you check first?")}</div>
  </div>''',
                notes=notes(
                    t("⏱ 12 мин (3 промпта). Тот же чат, файл уже загружен. После каждого ответа раскрывайте код: блок «Анализ завершён» или кнопка кода над графиком.",
                      "⏱ 12 min (3 prompts). Same chat, the file is already uploaded. After each answer open the code: the “Analysis complete” block or the code button above the chart."),
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
    return dict(min=4, html=f'''
  {head(t("Что нашли", "What we found"), t("Две проблемы, которых не видно в итоге за год", "Two problems the annual total doesn’t show"), k="red")}
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
                    t("Вопрос в чат: «Что бы вы предложили Анне по каждой находке?» Ответ «урезать Social» обсудим на слайде 16.",
                      "Ask the chat: “What would you suggest to Anna for each finding?” We’ll discuss “cut Social” on slide 16.")))


def s_makeover():
    return dict(min=4, html=f'''
  {head(t("График для слайда", "A slide-ready chart"), t("График правится словами, как текст", "You edit a chart with words, like text"), k="violet")}
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
    return dict(min=3, html=f'''
  {head(t("Проверка • 60 секунд", "Check • 60 seconds"), t("Три версии графика — три разных числа. Сверяйте после каждой переделки", "Three versions of a chart, three different numbers. Compare after every redo"), k="green")}
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
    return s_db_full() if _db_results() else dict(min=5, html=head(t("Большая база", "A large database"), t("Файл не лезет в чат: модель пишет запрос, база считает", "The file won’t fit in a chat: the model writes a query, the database counts")), notes=notes("⏱ 5"))


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
    return dict(min=5, html=f'''
  {head(t("Большая база • кулинарные YouTube-каналы", "A large database • cooking YouTube channels"), t("База обновляется каждый день: файл не выгружаем, спрашиваем базу", "The database updates daily: don’t export a file, ask the database"), k="amber")}
  <div class="body" style="margin-top:12px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr) 1.2fr;gap:24px;align-items:end;">{stats}
      <div class="cap">{t(f"Для урока — обезличенный срез: <b>{num(smp['channels'])}</b> канала, <b>{num(smp['videos'])}</b> видео. Без e-mail, ссылок и id.", f"For the lesson, an anonymised sample: <b>{num(smp['channels'])}</b> channels, <b>{num(smp['videos'])}</b> videos. No e-mails, links or ids.")}</div>
    </div>
    <div class="row" style="grid-template-columns:0.95fr 1.05fr;gap:32px;margin-top:20px;align-items:stretch;">
      <div class="stack" style="gap:12px;">
        {pr(t("Промпт", "Prompt"), t("В базе таблица videos: длительность и просмотры каждого видео. Напиши SQL-запрос: видео какой длины набирают больше всего просмотров? Объясни каждую строку.", "The database has a videos table: length and views of every video. Write an SQL query: which video length gets the most views? Explain every line."), k="amber")}
        <div class="code">{sql}</div>
      </div>
      <div class="stack" style="gap:6px;">
        <div class="cap" style="font-size:21px;font-weight:700;color:var(--fg);">{t("Типичные просмотры видео по длительности", "Typical views per video by length")}</div>
        {db_bars(q2)}
        <div class="note" style="--k:var(--red)">{t(f"20–40 минут — в {ratio:.0f} раз больше коротких? Сравнили каждое видео с обычными роликами <b>его же канала</b> — всего на {(q4[top['duration_bucket']] - 1) * 100:.0f} % выше обычного. Длинные видео просто чаще снимают большие каналы.",
                                                        f"20–40 minutes gets {ratio:.0f}× more than short videos? Compared with ordinary videos <b>of the same channel</b>, they are only {(q4[top['duration_bucket']] - 1) * 100:.0f}% above usual. Big channels simply make long videos more often.")}</div>
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
    return dict(min=3, html=f'''
  {head(t("Откуда берутся данные", "Where data comes from"), t("Сначала ищите кнопку «Экспорт», потом API. Скрапинг — последний вариант", "Look for an Export button first, then an API. Scraping is the last option"))}
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
        <div class="o">{t("так собрана база каналов со слайда 13", "this is how the slide 13 channel database was collected")}</div></div>
      <div class="door" style="--k:var(--red)">{icon("web", 52, "var(--red)")}<div class="h">{t("3. Скрапинг", "3. Scraping")}</div>
        <div class="w">{t("Программа читает страницы сайта, как человек. Перед этим проверьте:", "A program reads website pages like a person would. Before you do it, check:")}</div>
        <ul class="checklist" style="gap:8px;"><li style="font-size:20px;">{t("условия сайта разрешают", "the site’s terms allow it")}</li><li style="font-size:20px;">{t("нет персональных данных", "no personal data")}</li><li style="font-size:20px;">{t("не нагружаете чужой сайт", "you don’t overload the site")}</li></ul></div>
    </div>
    <div class="plaque" style="margin-top:18px;">{t("<b>Вопрос для ИИ:</b> «Какой официальный экспорт или API есть у системы X, чтобы выгрузить продажи за год?»", "<b>Ask the AI:</b> “What official export or API does system X have to download a year of sales?”")}</div>
  </div>''',
                notes=notes(
                    t("Перед началом слайда отправьте в чат промпт 6 (отчёт и скрипт): ответ идёт 3–4 минуты, к слайду 15 файл будет готов.",
                      "Before you start this slide, send prompt 6 (report and script) to the chat: the answer takes 3–4 minutes and will be ready by slide 15."),
                    t("⏱ 3 мин. Данные для анализа почти всегда уже где-то лежат. Первое, что ищем, — кнопку экспорта: она есть в CRM, 1С, рекламных кабинетах, YouTube Studio. Это самый быстрый и безопасный путь.",
                      "⏱ 3 min. The data you need almost always already sits somewhere. First look for an export button: CRM, accounting software, ad accounts and YouTube Studio all have one. It is the fastest and safest route."),
                    t("Второе — официальный API: программный вход в сервис. Ответ приходит в виде JSON, как в середине слайда. Код писать самим не нужно: ИИ напишет скрипт, который превратит ответ в таблицу. Так, через YouTube Data API, собрана база каналов, которую мы только что видели. Пример JSON на слайде упрощён.",
                      "Second, an official API: a program’s way into the service. The answer comes as JSON, like the middle of the slide. You don’t write the code yourself: AI writes a script that turns the answer into a table. The channel database we just saw was collected this way, through the YouTube Data API. The JSON on the slide is simplified."),
                    t("Третье — скрапинг: программа читает страницы сайта. Это последний вариант. Три проверки: условия сайта разрешают, нет персональных данных, вы не создаёте нагрузку на чужой сервер. Для большинства рабочих задач хватает экспорта.",
                      "Third, scraping: a program reads a site’s pages. It is the last option. Three checks: the site’s terms allow it, no personal data, you don’t put load on someone else’s server. For most work tasks, export is enough.")))


def s_report():
    return dict(min=5, html=f'''
  {head(t("Итог анализа", "The result of the analysis"), t("Руководителю отправляем файл отчёта. Превью в чате может врать", "Send the manager the report file. The chat preview can lie"), k="green")}
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
    return dict(min=2, html=f'''
  {head(t("Данные и приватность", "Data and privacy"), t("Что можно загружать в чат", "What you may upload to a chat"), k="amber")}
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
    return dict(min=4, html=f'''
  {head(t("Практика и домашнее задание", "Practice and homework"), t("Пакет, который можно отправить руководителю", "A pack you can send to a manager"), t("Файл <code>northstar_2025.xlsx</code>. Ответьте Анне на одно письмо: <b>что с продажами за год и что проверить дальше?</b>", "File <code>northstar_2025.xlsx</code>. Answer Anna’s e-mail: <b>how did sales go this year, and what should we check next?</b>"), k="green")}
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
    rules = [("cyan", t("Промпт-опись первым", "The describe prompt first"), t("«опиши файл, предложи 5 вопросов, ничего не меняй»", "“describe the file, suggest 5 questions, change nothing”")),
             ("green", t("Формулы словами", "Formulas in words"), t("«формулами Excel, а не готовыми числами»", "“Excel formulas, not pasted numbers”")),
             ("violet", t("Один график на один вопрос", "One chart per question"), t("заголовок — вывод, один акцентный цвет", "title = finding, one accent colour")),
             ("amber", t("Отчёт файлом", "The report as a file"), t("открыть скачанный файл, приложить рецепт", "open the downloaded file, attach the recipe")),
             ("red", t("60 секунд проверки", "60 seconds of checks"), t("строки, одна точка, процент от чего", "rows, one point, percent of what"))]
    r = "".join(f'<div class="rule" style="--k:var(--{c})"><div class="n">{i + 1}</div><div class="t">{h}<small>{d}</small></div></div>' for i, (c, h, d) in enumerate(rules))
    return dict(min=2, html=f'''
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


SLIDES = [s_cover, s_hook, s_first, s_doors, s_demo1, s_season, s_charts, s_break, s_demo2, s_found,
          s_makeover, s_check, s_db, s_sources, s_report, s_causal, s_privacy, s_hw, s_summary]


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
