# -*- coding: utf-8 -*-
"""Demo data for L09 (RU + EN): the made-up courier-support tickets CSV used in the live demo.

The v1/v2 HTML builders below are kept only as an offline example; the deck now uses real claude.ai screenshots.

    python make_demo.py

Writes ../demo_assets/tickets_{ru,en}.csv, ../demo_assets/artifact_v{1,2,3}_{ru,en}.html
and ../assets/img/demo_v{1,2,3}_{ru,en}.png (first screen, 1280x800 = "above the fold").

v1 = what Claude made from the weak prompt, v2 = from the strong brief, v3 = after one
targeted revision. Prompts are in ../demo_assets/prompts_{ru,en}.md.
"""
import csv
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
L09 = HERE.parent
DEMO = L09 / "demo_assets"
IMG = L09 / "assets" / "img"

# id, email, area, severity, age_days, status, owner, summary
ROWS = {
    "ru": [
        ("T-101", "k.ivanova@mail.example", "Доставка", "P1", 4, "Открыт", "Марта", "Заказ оплачен, но не доставлен 4 дня"),
        ("T-102", "d.saidov@mail.example", "Адрес", "P2", 3, "Открыт", "Олег", "Курьер не может найти адрес второй раз"),
        ("T-103", "n.park@mail.example", "Упаковка", "P3", 1, "Ждём клиента", "Аня", "Просим фото повреждённой упаковки"),
        ("T-104", "a.khan@mail.example", "Оплата", "P1", 1, "Открыт", "Рави", "Двойное списание за один заказ"),
        ("T-105", "m.lee@mail.example", "Возврат", "P2", 6, "Открыт", "", "Нет ответственного после смены очереди"),
        ("T-106", "s.orlova@mail.example", "Приложение курьера", "P1", 5, "Открыт", "Марта", "Курьеры не могут отметить доставку"),
        ("T-107", "j.novak@mail.example", "Чек", "P2", 2, "Закрыт", "Олег", "Неверный адрес в чеке — исправлено"),
        ("T-108", "r.aliev@mail.example", "Уведомления", "P3", 8, "Открыт", "Аня", "Опечатка в push-уведомлении"),
        ("T-109", "t.kim@mail.example", "Приложение курьера", "P2", 5, "Открыт", "Рави", "Приложение вылетает при съёмке фото"),
        ("T-110", "e.petrova@mail.example", "Безопасность", "P1", 2, "Открыт", "", "Клиент видит чужие заказы в профиле"),
        ("T-111", "b.usmanov@mail.example", "Промокоды", "P2", 1, "Ждём разработку", "Марта", "Промокод не применяется в приложении"),
        ("T-112", "l.grin@mail.example", "Зоны", "P3", 4, "Открыт", "Олег", "Курьер просит сменить зону доставки"),
    ],
    "en": [
        ("T-101", "k.ivanova@mail.example", "Delivery", "P1", 4, "Open", "Marta", "Order paid but not delivered for 4 days"),
        ("T-102", "d.saidov@mail.example", "Address", "P2", 3, "Open", "Oleg", "Courier can't find the address, second time"),
        ("T-103", "n.park@mail.example", "Packaging", "P3", 1, "Waiting customer", "Anya", "Asked for a photo of the damaged package"),
        ("T-104", "a.khan@mail.example", "Payment", "P1", 1, "Open", "Ravi", "Charged twice for one order"),
        ("T-105", "m.lee@mail.example", "Refund", "P2", 6, "Open", "", "No owner after the queue was changed"),
        ("T-106", "s.orlova@mail.example", "Courier app", "P1", 5, "Open", "Marta", "Couriers can't mark orders as delivered"),
        ("T-107", "j.novak@mail.example", "Receipt", "P2", 2, "Closed", "Oleg", "Wrong address on the receipt — fixed"),
        ("T-108", "r.aliev@mail.example", "Notifications", "P3", 8, "Open", "Anya", "Typo in a push notification"),
        ("T-109", "t.kim@mail.example", "Courier app", "P2", 5, "Open", "Ravi", "App crashes when taking a photo"),
        ("T-110", "e.petrova@mail.example", "Security", "P1", 2, "Open", "", "Customer sees other people's orders"),
        ("T-111", "b.usmanov@mail.example", "Promo codes", "P2", 1, "Waiting engineering", "Marta", "Promo code doesn't apply in the app"),
        ("T-112", "l.grin@mail.example", "Zones", "P3", 4, "Open", "Oleg", "Courier asks to change delivery zone"),
    ],
}
HEAD = {
    "ru": ["id", "email", "тема", "приоритет", "дней", "статус", "ответственный", "суть"],
    "en": ["id", "email", "area", "priority", "days", "status", "owner", "summary"],
}
CLOSED = {"Закрыт", "Closed"}

T = {
    "ru": dict(
        v1_title="Дашборд обращений", v1_sub="Служба поддержки • 12 обращений",
        k_total="Всего обращений", k_open="Открыто", k_p1="Приоритет P1", k_age="Средний возраст, дн.",
        by_sev="По приоритету", by_status="По статусу", all="Все обращения",
        v2_title="Утренний разбор поддержки", v2_sub="Понедельник • 3 минуты до планёрки",
        first="Сделать первым", first_why="Срочные (P1) обращения старше 2 дней",
        days="дн.", owner="ответственный", no_owner="нет ответственного",
        load="Нагрузка на людей", open_tickets="открытые обращения", table="Открытые обращения",
        filter="Фильтр:", f_all="все", hidden_closed="Закрытые скрыты (1).",
        missing_small="Без ответственного: T-105, T-110",
        why3_110="Клиент видит чужие заказы — это утечка данных. Ответственного нет, поэтому сначала назначьте человека.",
        why3_106="Курьеры не могут закрыть доставки — копятся жалобы.",
        why3_101="Деньги взяты, заказа нет уже 4 дня.",
        assign="Назначить",
        checks="Проверки", c1="Все P1 старше 2 дней — на первом экране",
        c2="Обращения без ответственного отмечены явно", c3="Нет email и личных данных клиентов",
        c4="Понятно за 3 минуты, что делать первым", c5="Закрытые обращения не мешают",
        privacy="Email клиентов не показываем",
        cols=["ID", "Приоритет", "Дней", "Статус", "Ответственный", "Суть"],
        cols_v1=["ID", "Email", "Тема", "Приоритет", "Дней", "Статус", "Ответственный", "Суть"],
    ),
    "en": dict(
        v1_title="Support Tickets Dashboard", v1_sub="Customer support • 12 tickets",
        k_total="Total tickets", k_open="Open", k_p1="Priority P1", k_age="Average age, days",
        by_sev="By priority", by_status="By status", all="All tickets",
        v2_title="Morning support check", v2_sub="Monday • 3 minutes before stand-up",
        first="Act on first", first_why="Urgent (P1) tickets older than 2 days",
        days="d", owner="owner", no_owner="no owner",
        load="Workload per person", open_tickets="open tickets", table="Open tickets",
        filter="Filter:", f_all="all", hidden_closed="Closed tickets hidden (1).",
        missing_small="No owner: T-105, T-110",
        why3_110="A customer sees other people's orders — a data leak. Nobody owns it, so assign someone first.",
        why3_106="Couriers can't close deliveries — complaints pile up.",
        why3_101="Money taken, no order for 4 days.",
        assign="Assign",
        checks="Checks", c1="Every P1 older than 2 days is on the first screen",
        c2="Tickets without an owner are clearly marked", c3="No customer emails or personal data",
        c4="In 3 minutes it is clear what to do first", c5="Closed tickets stay out of the way",
        privacy="Customer emails are hidden",
        cols=["ID", "Priority", "Days", "Status", "Owner", "Summary"],
        cols_v1=["ID", "Email", "Area", "Priority", "Days", "Status", "Owner", "Summary"],
    ),
}

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif;background:#f6f7f9;color:#1f2430;padding:28px 36px;font-size:15px}
h1{font-size:26px;font-weight:700} .sub{color:#6b7280;margin-top:4px;font-size:15px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:20px}
.kpi{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:14px 16px}
.kpi .n{font-size:30px;font-weight:700} .kpi .l{color:#6b7280;font-size:13px;margin-top:2px}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:16px 18px;margin-top:16px}
.card h2{font-size:16px;font-weight:600;margin-bottom:12px}
table{width:100%;border-collapse:collapse;font-size:14px} th{text-align:left;color:#6b7280;font-weight:600;padding:7px 8px;border-bottom:1px solid #e5e7eb}
td{padding:7px 8px;border-bottom:1px solid #f0f1f3}
.pill{display:inline-block;font-size:12px;font-weight:700;border-radius:6px;padding:2px 7px}
.P1{background:#fee2e2;color:#b91c1c}.P2{background:#fef3c7;color:#92400e}.P3{background:#e0f2fe;color:#075985}
"""


def rows(lang):
    return [dict(zip(["id", "email", "area", "sev", "age", "status", "owner", "summary"], r)) for r in ROWS[lang]]


def page(lang, title, css, body):
    return (f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><title>{title}</title>'
            f'<style>{BASE_CSS}{css}</style></head><body>{body}</body></html>')


def v1(lang):
    s, rs = T[lang], rows(lang)
    sev = {k: sum(r["sev"] == k for r in rs) for k in ("P1", "P2", "P3")}
    st = {}
    for r in rs:
        st[r["status"]] = st.get(r["status"], 0) + 1
    avg = sum(r["age"] for r in rs) / len(rs)
    open_n = sum(r["status"] in ("Открыт", "Open") for r in rs)
    colors = {"P1": "#ef4444", "P2": "#f59e0b", "P3": "#0ea5e9"}
    bars = "".join(f'<div class="b"><span>{k}</span><i style="width:{v * 60}px;background:{colors[k]}"></i><b>{v}</b></div>' for k, v in sev.items())
    stc = ["#6366f1", "#a5b4fc", "#c7d2fe", "#e0e7ff"]
    sbars = "".join(f'<div class="b"><span>{k}</span><i style="width:{v * 30}px;background:{stc[i % 4]}"></i><b>{v}</b></div>' for i, (k, v) in enumerate(st.items()))
    trs = "".join(f'<tr><td>{r["id"]}</td><td>{r["email"]}</td><td>{r["area"]}</td><td><span class="pill {r["sev"]}">{r["sev"]}</span></td>'
                  f'<td>{r["age"]}</td><td>{r["status"]}</td><td>{r["owner"]}</td><td>{r["summary"]}</td></tr>' for r in rs)
    css = (".charts{display:grid;grid-template-columns:1fr 1fr;gap:16px}.charts .card{margin-top:16px}"
           ".b{display:grid;grid-template-columns:150px 1fr 30px;align-items:center;gap:10px;margin:8px 0;font-size:14px}"
           ".b i{display:block;height:16px;border-radius:4px}.b b{text-align:right}"
           "body{background:linear-gradient(180deg,#eef2ff,#f6f7f9 260px)}")
    body = (f'<h1>{s["v1_title"]}</h1><div class="sub">{s["v1_sub"]}</div>'
            f'<div class="kpis"><div class="kpi"><div class="n">{len(rs)}</div><div class="l">{s["k_total"]}</div></div>'
            f'<div class="kpi"><div class="n">{open_n}</div><div class="l">{s["k_open"]}</div></div>'
            f'<div class="kpi"><div class="n">{sev["P1"]}</div><div class="l">{s["k_p1"]}</div></div>'
            f'<div class="kpi"><div class="n">{avg:.1f}</div><div class="l">{s["k_age"]}</div></div></div>'
            f'<div class="charts"><div class="card"><h2>{s["by_sev"]}</h2>{bars}</div><div class="card"><h2>{s["by_status"]}</h2>{sbars}</div></div>'
            f'<div class="card"><h2>{s["all"]}</h2><table><tr>{"".join(f"<th>{c}</th>" for c in s["cols_v1"])}</tr>{trs}</table></div>')
    return page(lang, s["v1_title"], css, body)


V2_CSS = """
.top{display:grid;grid-template-columns:1.55fr 1fr;gap:16px;margin-top:18px}
.first{background:#fff;border:2px solid #ef4444;border-radius:12px;padding:16px 18px}
.first h2{font-size:18px;color:#b91c1c}.first .why{color:#6b7280;font-size:13px;margin:2px 0 10px}
.item{display:grid;grid-template-columns:62px 40px 1fr auto;gap:10px;align-items:center;padding:9px 0;border-top:1px solid #f3f4f6}
.item .id{font-weight:700}.item .s{font-size:14px}.item .ex{grid-column:3/5;color:#4b5563;font-size:13px;margin-top:-4px}
.own{font-size:13px;color:#374151;white-space:nowrap}.own.miss{color:#b91c1c;font-weight:700;background:#fee2e2;border-radius:6px;padding:2px 8px}
.load .r{display:grid;grid-template-columns:150px 1fr 24px;gap:8px;align-items:center;margin:9px 0;font-size:14px}
.load i{display:block;height:14px;border-radius:4px;background:#6366f1}.load i.hot{background:#ef4444}
.mini{color:#9ca3af;font-size:12px;margin-top:10px}
.flt{display:flex;gap:6px;align-items:center;font-size:13px;color:#6b7280;margin-bottom:8px}.flt span{border:1px solid #d1d5db;border-radius:999px;padding:2px 10px;color:#374151}.flt span.on{background:#1f2430;color:#fff;border-color:#1f2430}
.priv{font-size:12px;color:#047857;background:#d1fae5;border-radius:6px;padding:3px 8px;margin-left:auto}
.checks{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}.checks div{font-size:13px;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:8px}.checks b{color:#15803d}
.btn{font-size:12px;font-weight:700;color:#fff;background:#b91c1c;border-radius:6px;padding:3px 9px}
"""


def v2(lang, fixed=False):
    s, rs = T[lang], rows(lang)
    op = [r for r in rs if r["status"] not in CLOSED]
    stale = sorted([r for r in op if r["sev"] == "P1" and r["age"] > 2], key=lambda r: -r["age"])
    first = stale
    if fixed:
        first = [r for r in op if r["sev"] == "P1" and not r["owner"]] + stale
    why = {"T-110": s["why3_110"], "T-106": s["why3_106"], "T-101": s["why3_101"]}

    def item(r):
        own = f'<span class="own miss">{s["no_owner"]}</span>' if not r["owner"] else f'<span class="own">{r["owner"]}</span>'
        ex = f'<div class="ex">{why[r["id"]]}</div>' if fixed else ""
        return (f'<div class="item"><span class="id">{r["id"]}</span><span class="pill P1">P1</span>'
                f'<span class="s">{r["summary"]} · <b>{r["age"]} {s["days"]}</b></span>{own}{ex}</div>')

    load = {}
    for r in op:
        load[r["owner"] or "—"] = load.get(r["owner"] or "—", 0) + 1
    lr = "".join(f'<div class="r"><span>{k if k != "—" else s["no_owner"]}</span><i class="{"hot" if k in ("Марта", "Marta", "—") else ""}" style="width:{v * 46}px"></i><b>{v}</b></div>'
                 for k, v in sorted(load.items(), key=lambda kv: -kv[1]))
    sevorder = {"P1": 0, "P2": 1, "P3": 2}
    trs = "".join(f'<tr><td>{r["id"]}</td><td><span class="pill {r["sev"]}">{r["sev"]}</span></td><td>{r["age"]}</td><td>{r["status"]}</td>'
                  f'<td>{r["owner"] or (("<b style=color:#b91c1c>" + s["no_owner"] + "</b>") if fixed else "<span style=color:#9ca3af>—</span>")}</td><td>{r["summary"]}</td></tr>'
                  for r in sorted(op, key=lambda r: (sevorder[r["sev"]], -r["age"])))
    mini = "" if fixed else f'<div class="mini">{s["missing_small"]}</div>'
    checks = ""
    if fixed:
        checks = (f'<div class="card"><h2>{s["checks"]}</h2><div class="checks">' +
                  "".join(f'<div><b>✓</b> {s[c]}</div>' for c in ("c1", "c2", "c3", "c4", "c5")) + "</div></div>")
    body = (f'<h1>{s["v2_title"]}</h1><div class="sub">{s["v2_sub"]}</div>'
            f'<div class="top"><div class="first"><h2>{s["first"]}</h2><div class="why">{s["first_why"]}'
            f'{(" + " + s["no_owner"]) if fixed else ""}</div>{"".join(item(r) for r in first)}</div>'
            f'<div class="card" style="margin-top:0"><h2>{s["load"]}</h2><div class="load">{lr}</div>{mini}</div></div>'
            f'<div class="card"><div class="flt"><b style="color:#1f2430;font-size:16px;margin-right:10px">{s["table"]}</b>{s["filter"]}'
            f'<span class="on">{s["f_all"]}</span><span>P1</span><span>P2</span><span>P3</span>{("<span>" + s["no_owner"] + "</span>") if fixed else ""}'
            f'<span class="priv">🔒 {s["privacy"]}</span></div>'
            f'<table><tr>{"".join(f"<th>{c}</th>" for c in s["cols"])}</tr>{trs}</table>'
            f'<div class="mini">{s["hidden_closed"]}</div></div>{checks}')
    return page(lang, s["v2_title"], V2_CSS, body)


EDGE = next((c for c in [shutil.which("msedge"),
                         r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                         r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"] if c and Path(c).exists()), None)


def shot(html, png, w=1280, h=800):
    prof = tempfile.mkdtemp(prefix="edgeshot_")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
                    "--virtual-time-budget=3000", f"--user-data-dir={prof}", f"--screenshot={png}", html.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    shutil.rmtree(prof, ignore_errors=True)


if __name__ == "__main__":
    DEMO.mkdir(exist_ok=True)
    IMG.mkdir(parents=True, exist_ok=True)
    for lang in ("ru", "en"):
        with open(DEMO / f"tickets_{lang}.csv", "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(HEAD[lang])
            w.writerows(ROWS[lang])
        print("ok", f"tickets_{lang}.csv")
