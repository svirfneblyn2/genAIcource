# -*- coding: utf-8 -*-
"""Chart makeover pair for the L08 v2 deck: a typical default chart vs the same data after one prompt.

    python make_makeover.py   ->  ../assets/v2/makeover_before[_EN].png, makeover_after[_EN].png

Data: Northstar 2025 (clean rows), revenue per $1 of advertising by month for Search and Social.
"""
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "assets" / "v2"
OUT.mkdir(parents=True, exist_ok=True)

rev, spend = defaultdict(float), defaultdict(float)
seen = set()
for r in csv.DictReader((HERE / "northstar_sales_2025.csv").open(encoding="utf-8")):
    key = tuple(r.values())
    if key in seen:
        continue
    seen.add(key)
    d = r["order_date"]
    m = int(d[5:7]) if "-" in d else int(d.split("/")[1])
    rev[(r["channel"], m)] += float(r["revenue"])
    spend[(r["channel"], m)] += float(r["ad_spend"])
MONTHS = list(range(1, 13))
roas = {ch: [rev[(ch, m)] / spend[(ch, m)] for m in MONTHS] for ch in ("Search", "Social")}

TXT = {
    "ru": dict(mn=["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"],
               t_before="Chart 1", t_after="С июля Social приносит вдвое меньше на каждый $1 рекламы",
               sub="Выручка на $1 рекламы, 2025", jul="июль: бюджет Social ×2"),
    "en": dict(mn=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
               t_before="Chart 1", t_after="Since July Social returns half as much per $1 of ads",
               sub="Revenue per $1 of advertising, 2025", jul="July: Social budget ×2"),
}

for lang, suf in (("ru", ""), ("en", "_EN")):
    T = TXT[lang]
    # BEFORE: what a default request often gives — 3D-ish colours, legend far away, no title meaning, grid clutter
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
    x = range(12)
    w = 0.4
    ax.bar([i - w / 2 for i in x], roas["Search"], w, label="Search", color="#4472C4")
    ax.bar([i + w / 2 for i in x], roas["Social"], w, label="Social", color="#ED7D31")
    ax.set_xticks(list(x))
    ax.set_xticklabels([f"2025-{m:02d}" for m in MONTHS], rotation=45, fontsize=8)
    ax.set_ylim(1.5, 6)
    ax.grid(True, which="both", color="#cccccc")
    ax.set_title(T["t_before"], fontsize=10)
    ax.set_ylabel("value")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / f"makeover_before{suf}.png")
    plt.close(fig)

    # AFTER: line (time), headline = the finding, direct labels, one accent colour, axis from zero, annotation
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
    fig.patch.set_facecolor("white")
    ax.plot(MONTHS, roas["Search"], color="#9aa5b4", lw=2.5)
    ax.plot(MONTHS, roas["Social"], color="#e8590c", lw=3.5)
    ax.text(12.2, roas["Search"][-1], "Search", va="center", fontsize=12, color="#6b7685")
    ax.text(12.2, roas["Social"][-1], "Social", va="center", fontsize=12, color="#e8590c", weight="bold")
    ax.axvline(6.5, color="#adb5bd", lw=1, ls="--")
    ax.text(6.6, 5.9, T["jul"], fontsize=10, color="#495057")
    ax.set_xticks(MONTHS)
    ax.set_xticklabels(T["mn"], fontsize=10)
    ax.set_ylim(0, 6.3)
    ax.set_xlim(0.6, 13.2)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.yaxis.grid(True, color="#eeeeee")
    ax.set_axisbelow(True)
    ax.tick_params(colors="#495057")
    fig.suptitle(T["t_after"], x=0.06, ha="left", fontsize=14, weight="bold", color="#212529")
    ax.set_title(T["sub"], loc="left", fontsize=11, color="#6b7685")
    fig.tight_layout()
    fig.savefig(OUT / f"makeover_after{suf}.png")
    plt.close(fig)
print("ok", {k: [round(v, 2) for v in vs] for k, vs in roas.items()})
