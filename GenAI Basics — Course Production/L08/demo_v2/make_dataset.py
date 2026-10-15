# -*- coding: utf-8 -*-
"""Generate the L08 v2 practice dataset: Northstar online shop, sales 2025 + customer reviews.

    python make_dataset.py

Deterministic (fixed seed). Writes RU and EN variants (same numbers, translated text):
    northstar_2025.xlsx / northstar_2025_EN.xlsx   two sheets: Sales (Excel table), Reviews
    northstar_sales_2025.csv, northstar_reviews_2025[_EN].csv
    northstar_sales_2026-01.csv                     next month, for the "recipe script" slide
    answers.md / answers_EN.md                      reference answers for the instructor

Three stories are planted (totals look normal; the stories show only in a chart or a slice):
  1. Seasonality: November-December peak, January dip.
  2. Social eats budget: from July Social ad spend doubles, revenue does not grow.
  3. Returns in one slice: Electronics x North (warehouse N2) from September ~25% returns vs ~5%;
     reviews for N2 explain why (damaged boxes / cracked screens), with varied wording and noise.
Plus two dirty rows: one exact duplicate and one date stored as text in another format.
"""
import calendar
import csv
import random
from collections import defaultdict
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

HERE = Path(__file__).resolve().parent
rnd = random.Random(2025)

CHANNELS = {"Search": 4200, "Social": 3600, "Email": 2600, "Organic": 3100}
CATEGORIES = {"Electronics": 1.35, "Home": 1.0, "Sports": 0.9, "Books": 0.6}
REGIONS = {"North": 1.0, "South": 1.1, "West": 0.95, "Central": 0.9}
SEASON = [0.74, 0.80, 0.90, 0.95, 1.00, 0.96, 0.92, 0.94, 1.00, 1.10, 1.62, 1.85]
SPEND_SHARE = {"Search": 0.19, "Social": 0.25, "Email": 0.0, "Organic": 0.0}
AVG_ORDER = {"Electronics": 92, "Home": 54, "Sports": 61, "Books": 24}


def warehouse(region, category):
    if region == "North":
        return "N2" if category == "Electronics" else "N1"
    return {"South": "S1", "West": "W1", "Central": "C1"}[region]


def make_month(year, month, season):
    rows = []
    for ch, base in CHANNELS.items():
        for cat, cf in CATEGORIES.items():
            for reg, rf in REGIONS.items():
              parts = rnd.choices([0, 1, 2, 3], weights=[0.05, 0.45, 0.35, 0.15])[0]
              total = base * cf * rf * season * rnd.uniform(0.88, 1.12)
              shares = [rnd.uniform(0.6, 1.4) for _ in range(parts)]
              for sh in shares:
                rev = total * sh / sum(shares) * (1 if parts else 0)
                rev = round(rev / 10) * 10 + rnd.choice([0, 5]) / 10
                orders = max(2, round(rev / AVG_ORDER[cat] * rnd.uniform(0.93, 1.07)))
                share = SPEND_SHARE[ch]
                if ch == "Social" and (year, month) >= (2025, 7):
                    share *= 2.0  # story 2: Social doubles spend, revenue does not follow
                spend = round(rev * share * rnd.uniform(0.92, 1.08), 2) if share else 0
                rr = rnd.uniform(0.035, 0.065)
                if reg == "North" and cat == "Electronics" and (year, month) >= (2025, 9):
                    rr = rnd.uniform(0.22, 0.28)  # story 3: returns spike at warehouse N2
                returns = round(orders * rr)
                day = rnd.randint(1, calendar.monthrange(year, month)[1])
                rows.append({"order_date": date(year, month, day), "channel": ch, "category": cat, "region": reg,
                             "warehouse": warehouse(reg, cat), "orders": orders, "revenue": rev,
                             "ad_spend": spend, "returns": returns})
    rows.sort(key=lambda r: (r["order_date"], r["channel"], r["category"], r["region"]))
    return rows


SALES = []
for m in range(1, 13):
    SALES.extend(make_month(2025, m, SEASON[m - 1]))
TRUTH_SALES = [dict(r) for r in SALES]
# dirty rows: an exact duplicate (March) and one date stored as text in another format (May)
dup_i = next(i for i, r in enumerate(SALES) if r["order_date"].month == 3 and r["channel"] == "Social" and r["category"] == "Home" and r["region"] == "South")
SALES.insert(dup_i + 1, dict(SALES[dup_i]))
txt_i = next(i for i, r in enumerate(SALES) if r["order_date"].month == 5 and r["channel"] == "Email" and r["category"] == "Sports" and r["region"] == "West")
SALES[txt_i] = dict(SALES[txt_i], order_date=SALES[txt_i]["order_date"].strftime("%d/%m/%Y"))
NEXT = make_month(2026, 1, SEASON[0] * 1.06)

# ---------------------------------------------------------------- reviews
ITEMS = {  # RU in accusative ("заказывал ...")
    "Electronics": [("наушники", "headphones"), ("колонку", "speaker"), ("планшет", "tablet"), ("ноутбук", "laptop"),
                    ("роутер", "router"), ("смарт-часы", "smartwatch"), ("монитор", "monitor"), ("зарядку", "charger")],
    "Home": [("чайник", "kettle"), ("плед", "blanket"), ("лампу", "lamp"), ("сковороду", "frying pan"), ("набор полотенец", "towel set")],
    "Sports": [("коврик для йоги", "yoga mat"), ("гантели", "dumbbells"), ("кроссовки", "sneakers"), ("рюкзак", "backpack")],
    "Books": [("книгу", "book"), ("набор книг", "book set"), ("ежедневник", "planner"), ("комикс", "comic")],
}
DAMAGE = [
    ("Коробка пришла мятая, внутри трещина на корпусе.", "The box arrived crushed, a crack in the case inside."),
    ("Заказывал {i} — пришло разбитым, оформил возврат.", "Ordered the {i} — arrived broken, I returned it."),
    ("Упаковка порвана, на корпусе царапины.", "Packaging torn, scratches on the case."),
    ("Заказывал {i}, привезли с вмятиной. Очень жаль.", "Ordered the {i}, it came with a dent. Disappointing."),
    ("Коробка будто падала: всё болтается, угол сломан.", "Looks like the box was dropped: everything loose, a corner broken."),
    ("Брал {i} — повреждено при доставке, пришлось вернуть.", "Bought the {i} — damaged in delivery, had to return it."),
    ("Плохо упаковано — ни плёнки, ни пенопласта, всё в царапинах.", "Badly packed — no wrap, no foam, scratched all over."),
    ("Второй раз подряд приходит битая техника.", "Second time in a row the electronics arrive broken."),
    ("Брал {i}: не включается, коробка была смята.", "Bought the {i}: won't turn on, the box was crushed."),
    ("Курьер отдал мокрую рваную коробку.", "Courier handed over a wet, torn box."),
    ("Сам товар хороший, но доставили повреждённым — вернул.", "The product itself is fine but it arrived damaged — returned it."),
    ("Мятая упаковка, на корпусе скол.", "Crushed packaging, a chip on the case."),
    ("Открыл коробку — трещина на экране. Жду замену.", "Opened the box — a cracked screen. Waiting for a replacement."),
    ("Почему так пакуют? Заказывал {i}, пришло битым.", "Why pack it like this? Ordered the {i}, it arrived broken."),
]
LATE = [("Доставка задержалась на {d} дня.", "Delivery was {d} days late."),
        ("Курьер опоздал, но всё целое.", "Courier was late but everything was intact."),
        ("Ждал {i} дольше обещанного.", "Waited for the {i} longer than promised."),
        ("Перенесли доставку два раза.", "Delivery was rescheduled twice.")]
PRICE = [("Дороговато по сравнению с конкурентами.", "A bit pricey compared to competitors."),
         ("Брал {i} — неплохо, но цена кусается.", "Bought the {i} — decent, but the price is steep."),
         ("Взял {i} по скидке — доволен.", "Got the {i} on sale — happy."),
         ("За такие деньги ждал большего.", "Expected more for the money.")]
GOOD = [("Всё отлично, пришло быстро.", "All great, arrived fast."),
        ("Хорошее качество, рекомендую.", "Good quality, recommend."),
        ("Брал {i}, всё работает как надо, спасибо.", "Bought the {i}, all works as expected, thanks."),
        ("Аккуратно упаковано, всё целое.", "Neatly packed, everything intact."),
        ("Удобный сайт, заказ пришёл вовремя.", "Easy website, order arrived on time."),
        ("Брал {i} в подарок — понравилось.", "Bought the {i} as a gift — it was a hit."),
        ("Третий раз заказываю, всё ок.", "Third order here, all fine."),
        ("Товар соответствует описанию.", "The product matches the description."),
        ("Быстро и без проблем.", "Quick and painless.")]
SUPPORT = [("Поддержка долго отвечала про гарантию.", "Support took long to answer about the warranty."),
           ("В чате поддержки помогли быстро.", "Support chat helped quickly."),
           ("Не смог дозвониться в поддержку.", "Couldn't get through to support.")]
TAILS = [("", ""), ("", ""), ("", ""), (" Спасибо.", " Thanks."), (" Буду заказывать ещё.", " Will order again."),
         (" Больше не закажу.", " Won't order again."), (" Оценка честная.", " Honest rating.")]


def pick(pool, cat, neg=None):
    ru, en = rnd.choice(pool)
    item = rnd.choice(ITEMS[cat])
    d = rnd.choice([2, 3, 4])
    tail = rnd.choice(TAILS[:4] + (TAILS[5:6] if neg else TAILS[4:5]))
    ru = ru.format(i=item[0], d=d) + tail[0]
    en = en.format(i=item[1], d=d) + tail[1]
    if rnd.random() < 0.12:
        ru = ru.lower()
    return ru, en


REVIEWS = []
DAMAGE_IDS = set()
rid = 5000
for m in range(1, 13):
    n = round(22 * SEASON[m - 1] * rnd.uniform(0.85, 1.15))
    days = calendar.monthrange(2025, m)[1]
    for _ in range(n):
        reg = rnd.choices(list(REGIONS), weights=[1, 1.1, 0.95, 0.9])[0]
        cat = rnd.choices(list(CATEGORIES), weights=[1.3, 1, 0.9, 0.7])[0]
        r = rnd.random()
        rid += 1
        if r < 0.03:
            txt, rating = pick(DAMAGE, cat, True), rnd.choice([1, 2])  # noise: damage elsewhere
            DAMAGE_IDS.add(rid)
        elif r < 0.18:
            txt, rating = pick(LATE, cat, True), rnd.choice([2, 3, 4])
        elif r < 0.33:
            txt, rating = pick(PRICE, cat), rnd.choice([3, 4])
        elif r < 0.40:
            txt, rating = pick(SUPPORT, cat, True), rnd.choice([2, 4])
        else:
            txt, rating = pick(GOOD, cat), rnd.choice([4, 5, 5])
        REVIEWS.append(dict(review_id=rid, review_date=date(2025, m, rnd.randint(1, days)), region=reg, category=cat,
                            warehouse=warehouse(reg, cat), rating=rating, ru=txt[0], en=txt[1]))
    if m >= 9:  # story 3: extra reviews for N2 electronics, ~70% damage, ~30% neutral/other
        for _ in range(round(14 * SEASON[m - 1] * rnd.uniform(0.85, 1.15))):
            rid += 1
            if rnd.random() < 0.7:
                txt, rating = pick(DAMAGE, "Electronics", True), rnd.choice([1, 1, 2])
                DAMAGE_IDS.add(rid)
            else:
                txt, rating = pick(GOOD + LATE, "Electronics"), rnd.choice([3, 4, 5])
            REVIEWS.append(dict(review_id=rid, review_date=date(2025, m, rnd.randint(1, days)), region="North",
                                category="Electronics", warehouse="N2", rating=rating, ru=txt[0], en=txt[1]))
REVIEWS.sort(key=lambda r: (r["review_date"], r["review_id"]))

# ---------------------------------------------------------------- write files
SALES_COLS = ["order_date", "channel", "category", "region", "warehouse", "orders", "revenue", "ad_spend", "returns"]


def write_csv(path, rows, cols, conv=lambda r: r):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            r = conv(r)
            w.writerow({c: (r[c].isoformat() if isinstance(r[c], date) else r[c]) for c in cols})


def write_xlsx(path, lang):
    wb = Workbook()
    ws = wb.active
    ws.title = "Sales"
    ws.append(SALES_COLS)
    for r in SALES:
        ws.append([r[c] for c in SALES_COLS])
    for row in ws.iter_rows(min_row=2, min_col=1, max_col=1):
        for c in row:
            if isinstance(c.value, date):
                c.number_format = "yyyy-mm-dd"
    for col, wdt in zip("ABCDEFGHI", [12, 10, 12, 10, 11, 9, 11, 11, 9]):
        ws.column_dimensions[col].width = wdt
    for row in ws.iter_rows(min_row=2, min_col=7, max_col=8):
        for c in row:
            c.number_format = "#,##0.00"
    t = Table(displayName="Sales", ref=f"A1:I{len(SALES) + 1}")
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws.add_table(t)
    ws.freeze_panes = "A2"
    rv = wb.create_sheet("Reviews")
    cols = ["review_id", "review_date", "region", "category", "warehouse", "rating", "comment"]
    rv.append(cols)
    for r in REVIEWS:
        rv.append([r["review_id"], r["review_date"], r["region"], r["category"], r["warehouse"], r["rating"], r[lang]])
    for row in rv.iter_rows(min_row=2, min_col=2, max_col=2):
        for c in row:
            c.number_format = "yyyy-mm-dd"
    for col, wdt in zip("ABCDEFG", [10, 12, 10, 12, 11, 7, 70]):
        rv.column_dimensions[col].width = wdt
    t2 = Table(displayName="Reviews", ref=f"A1:G{len(REVIEWS) + 1}")
    t2.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    rv.add_table(t2)
    rv.freeze_panes = "A2"
    wb.save(path)


write_xlsx(HERE / "northstar_2025.xlsx", "ru")
write_xlsx(HERE / "northstar_2025_EN.xlsx", "en")
write_csv(HERE / "northstar_sales_2025.csv", SALES, SALES_COLS)
write_csv(HERE / "northstar_sales_2026-01.csv", NEXT, SALES_COLS)
for lang, suf in (("ru", ""), ("en", "_EN")):
    write_csv(HERE / f"northstar_reviews_2025{suf}.csv", REVIEWS,
              ["review_id", "review_date", "region", "category", "warehouse", "rating", "comment"],
              conv=lambda r, lang=lang: dict(r, comment=r[lang]))

# ---------------------------------------------------------------- reference answers (from clean data)
M = defaultdict(float)
CH_M = defaultdict(float)
SP_M = defaultdict(float)
RET = defaultdict(lambda: [0, 0])
for r in TRUTH_SALES:
    mo = r["order_date"].month
    M[mo] += r["revenue"]
    CH_M[(r["channel"], mo)] += r["revenue"]
    SP_M[(r["channel"], mo)] += r["ad_spend"]
    k = (r["region"], r["category"], mo >= 9)
    RET[k][0] += r["returns"]
    RET[k][1] += r["orders"]
total = sum(M.values())
raw_total = sum(r["revenue"] for r in SALES)
lines = [
    "# Northstar 2025 — эталонные ответы (генерируется make_dataset.py)", "",
    f"- Строк в Sales: {len(SALES)} (чистых {len(TRUTH_SALES)}: 1 точный дубль + 1 дата текстом `{SALES[txt_i]['order_date']}`)",
    f"- Отзывов: {len(REVIEWS)}",
    f"- Выручка за год (без дубля): ${total:,.2f}; как в файле: ${raw_total:,.2f}",
    "- Выручка по месяцам: " + ", ".join(f"{m:02d}: ${M[m]:,.0f}" for m in range(1, 13)),
    f"- Декабрь к январю: {M[12] / M[1] - 1:+.1%}; декабрь к ноябрю: {M[12] / M[11] - 1:+.1%}; ноябрь+декабрь = {(M[11] + M[12]) / total:.1%} годовой выручки",
    "", "## Выручка на $1 рекламы (Search, Social) по месяцам",
]
for ch in ("Search", "Social"):
    lines.append(f"- {ch}: " + ", ".join(f"{m:02d}: {CH_M[(ch, m)] / SP_M[(ch, m)]:.2f}" for m in range(1, 13)))
s1 = sum(SP_M[("Social", m)] for m in range(1, 7)); s2 = sum(SP_M[("Social", m)] for m in range(7, 13))
r1 = sum(CH_M[("Social", m)] for m in range(1, 7)); r2 = sum(CH_M[("Social", m)] for m in range(7, 13))
lines += [f"- Social: расход H1 ${s1:,.0f} → H2 ${s2:,.0f} ({s2 / s1 - 1:+.0%}); выручка H1 ${r1:,.0f} → H2 ${r2:,.0f} ({r2 / r1 - 1:+.0%})", "",
          "## Возвраты (доля от заказов), сентябрь–декабрь"]
for reg in REGIONS:
    lines.append(f"- {reg}: " + ", ".join(f"{cat} {RET[(reg, cat, True)][0] / RET[(reg, cat, True)][1]:.1%}" for cat in CATEGORIES))
n2 = [r for r in REVIEWS if r["warehouse"] == "N2" and r["review_date"].month >= 9]
lines += ["", "## Отзывы",
          f"- N2, сентябрь–декабрь: {len(n2)} отзывов, из них про повреждение {sum(r['review_id'] in DAMAGE_IDS for r in n2)} ({sum(r['review_id'] in DAMAGE_IDS for r in n2) / len(n2):.0%})",
          f"- Остальные отзывы про повреждение: {sum(r['review_id'] in DAMAGE_IDS for r in REVIEWS if r not in n2)} из {len(REVIEWS) - len(n2)}",
          f"- Уникальных текстов отзывов: {len({r['ru'] for r in REVIEWS})} из {len(REVIEWS)}"]
(HERE / "answers.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
