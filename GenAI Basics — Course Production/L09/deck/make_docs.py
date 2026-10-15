# -*- coding: utf-8 -*-
"""90-minute instructor scripts (RU + EN) generated from the deck's speaker notes.

    python make_docs.py
"""
import html
import re

import build

HEAD = {
    "ru": ("# L09 — Экосистема Claude и артефакты: сценарий на 90 минут",
           "Сгенерировано из заметок спикера (`deck/build.py`, клавиша N в презентации). Правьте заметки в генераторе, затем `python make_docs.py`.",
           "Перед занятием: в claude.ai → Settings → Capabilities включены Artifacts (и AI-powered artifacts для слайда 14); открыть новый чат, `demo_assets/tickets_ru.csv` и `demo_assets/prompts_ru.md`; в Teams — показ окна браузера, без личной истории на экране. Если живое демо тормозит — на слайдах реальные результаты.",
           "Слайд", "мин", "Итого"),
    "en": ("# L09 — Claude Ecosystem and Artifacts: 90-minute script",
           "Generated from the speaker notes (`deck/build.py`, key N in the deck). Edit the notes in the generator, then run `python make_docs.py`.",
           "Before class: in claude.ai → Settings → Capabilities make sure Artifacts (and AI-powered artifacts for slide 14) are on; open a new chat, `demo_assets/tickets_en.csv` and `demo_assets/prompts_en.md`; in Teams share the browser window, with no personal history on screen. If the live demo is slow, the slides show the real results.",
           "Slide", "min", "Total"),
}


def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def title_of(h):
    m = re.search(r'<h2 class="title">(.*?)</h2>', h, re.S) or re.search(r"<h1>(.*?)</h1>", h, re.S) or re.search(r"<h2>(.*?)</h2>", h, re.S)
    return plain(m.group(1)) if m else ""


for lang in ("ru", "en"):
    build.LANG = lang
    h1, intro, prep, sl, mn, tot = HEAD[lang]
    out = [h1, "", intro, "", prep, ""]
    t0 = 0
    for i, fn in enumerate(build.SLIDES, 1):
        s = fn()
        out.append(f"## {sl} {i:02d} · {t0}–{t0 + s['min']} {mn} · {title_of(s['html'])}")
        out.append("")
        for p in re.findall(r"<p>(.*?)</p>", s["notes"], re.S):
            out.append(plain(p))
            out.append("")
        t0 += s["min"]
    out.append(f"**{tot}: {t0} {mn}.**")
    name = "L09_02_Instructor_Script_90MIN" + ("" if lang == "ru" else "_EN") + ".md"
    (build.L09 / name).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(name)
