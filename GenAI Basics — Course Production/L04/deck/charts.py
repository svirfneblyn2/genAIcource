"""Inline-SVG graphics for the L04 deck: radar small multiples, bar chart, loop and pipeline
diagrams, traffic light, folder tree and annotated images. Colors use the deck's CSS tokens."""

import math

FONT = "font-family:Onest,'Segoe UI',Arial,sans-serif"
MONO = "font-family:'JetBrains Mono',Consolas,monospace"


def radar(scores, labels, color, title, size=270):
    """scores: list of 1..3 per axis. Draws grid rings, axis labels and the filled polygon."""
    n = len(labels)
    cx, cy, r = size / 2, size / 2 + 6, size * 0.34
    def pt(i, v):
        a = -math.pi / 2 + 2 * math.pi * i / n
        return cx + r * v * math.cos(a), cy + r * v * math.sin(a)
    rings = "".join(
        f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, k / 3) for i in range(n)))}" fill="none" stroke="rgba(148,163,184,.22)" stroke-width="1"/>'
        for k in (1, 2, 3))
    axes = "".join(f'<line x1="{cx}" y1="{cy}" x2="{pt(i, 1)[0]:.1f}" y2="{pt(i, 1)[1]:.1f}" stroke="rgba(148,163,184,.18)"/>' for i in range(n))
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, s / 3) for i, s in enumerate(scores)))
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>' for x, y in (pt(i, s / 3) for i, s in enumerate(scores)))
    lab = ""
    for i, l in enumerate(labels):
        x, y = pt(i, 1.32)
        anchor = "middle" if abs(x - cx) < 8 else ("start" if x > cx else "end")
        lab += f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="{anchor}" style="{FONT};font-size:17px;fill:#9aa8bc">{l}</text>'
    return (f'<svg viewBox="-60 -14 {size + 120} {size + 34}" style="width:100%;height:100%;overflow:visible">'
            f'{rings}{axes}<polygon points="{poly}" fill="{color}" fill-opacity=".28" stroke="{color}" stroke-width="2.5"/>{dots}{lab}</svg>')


def hbars(items, unit="", max_v=None, width=760, row=64):
    """items: (label, value, color, note). Horizontal bars on one linear scale."""
    max_v = max_v or max(v for _, v, _, _ in items)
    lw, bw = 190, width - 190 - 120
    h = row * len(items)
    out = ""
    for i, (label, v, c, note) in enumerate(items):
        y = i * row
        w = bw * v / max_v
        out += (f'<text x="0" y="{y + row / 2 + 7}" style="{FONT};font-size:25px;font-weight:600;fill:#f1f5f9">{label}</text>'
                f'<rect x="{lw}" y="{y + 14}" width="{bw}" height="{row - 28}" rx="6" fill="rgba(148,163,184,.08)"/>'
                f'<rect x="{lw}" y="{y + 14}" width="{w:.1f}" height="{row - 28}" rx="6" fill="{c}"/>'
                f'<text x="{lw + w + 12:.1f}" y="{y + row / 2 + 8}" style="{MONO};font-size:22px;font-weight:700;fill:{c}">{v}{unit}</text>'
                f'<text x="{lw + w + 60:.1f}" y="{y + row / 2 + 7}" style="{FONT};font-size:16px;fill:#5f6e84">{note}</text>')
    return f'<svg viewBox="0 0 {width} {h}" style="width:100%;height:auto;overflow:visible">{out}</svg>'


def loop(steps, colors, size=430):
    """Circular process: n nodes on a ring with arrows between them; last node loops back."""
    n = len(steps)
    cx, cy, r = size / 2, size / 2, size * 0.36
    pos = [(cx + r * math.cos(-math.pi / 2 + 2 * math.pi * i / n), cy + r * math.sin(-math.pi / 2 + 2 * math.pi * i / n)) for i in range(n)]
    arcs = ""
    for i in range(n):
        a1 = -math.pi / 2 + 2 * math.pi * (i + 0.2) / n
        a2 = -math.pi / 2 + 2 * math.pi * (i + 0.8) / n
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        arcs += f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" fill="none" stroke="rgba(148,163,184,.45)" stroke-width="3" marker-end="url(#ah)"/>'
    nodes = ""
    for i, ((x, y), (h, d), c) in enumerate(zip(pos, steps, colors)):
        nodes += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="34" fill="#0b0f17" stroke="{c}" stroke-width="3"/>'
                  f'<text x="{x:.1f}" y="{y + 8:.1f}" text-anchor="middle" style="{MONO};font-size:22px;font-weight:700;fill:{c}">{i + 1}</text>')
        lx = x + (52 if x > cx + 5 else -52 if x < cx - 5 else 0)
        anchor = "start" if x > cx + 5 else "end" if x < cx - 5 else "middle"
        ly = y + (-72 if (abs(x - cx) <= 5 and y < cy) else 58 if abs(x - cx) <= 5 else -2)
        nodes += (f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" style="{FONT};font-size:30px;font-weight:700;fill:#f1f5f9">{h}</text>'
                  f'<text x="{lx:.1f}" y="{ly + 32:.1f}" text-anchor="{anchor}" style="{FONT};font-size:22px;fill:#9aa8bc">{d}</text>')
    return (f'<svg viewBox="-210 -50 {size + 420} {size + 110}" style="width:100%;height:100%;overflow:visible">'
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="rgba(148,163,184,.7)"/></marker></defs>'
            f'{arcs}{nodes}</svg>')


def pipeline(nodes, width=1440, h=150):
    """Left-to-right boxes with arrows. nodes: (title, subtitle, color)."""
    n = len(nodes)
    gap = 60
    bw = (width - gap * (n - 1)) / n
    out = '<defs><marker id="pa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#5f6e84"/></marker></defs>'
    for i, (t, s, c) in enumerate(nodes):
        x = i * (bw + gap)
        out += (f'<rect x="{x:.1f}" y="10" width="{bw:.1f}" height="{h - 20}" rx="14" fill="#121a28" stroke="{c}" stroke-width="2"/>'
                f'<text x="{x + bw / 2:.1f}" y="{h / 2 - 2}" text-anchor="middle" style="{FONT};font-size:28px;font-weight:700;fill:#f1f5f9">{t}</text>'
                f'<text x="{x + bw / 2:.1f}" y="{h / 2 + 28}" text-anchor="middle" style="{MONO};font-size:18px;fill:{c}">{s}</text>')
        if i < n - 1:
            out += f'<line x1="{x + bw + 6:.1f}" y1="{h / 2}" x2="{x + bw + gap - 8:.1f}" y2="{h / 2}" stroke="#5f6e84" stroke-width="3" marker-end="url(#pa)"/>'
    return f'<svg viewBox="0 0 {width} {h}" style="width:100%;height:auto;overflow:visible">{out}</svg>'


def traffic(zones):
    """Vertical traffic light with a label block per lamp. zones: (title, text, color)."""
    out = '<rect x="0" y="0" width="120" height="420" rx="40" fill="#121a28" stroke="rgba(148,163,184,.25)" stroke-width="2"/>'
    for i, (t, d, c) in enumerate(zones):
        y = 70 + i * 140
        out += (f'<circle cx="60" cy="{y}" r="44" fill="{c}"/>'
                f'<text x="160" y="{y - 8}" style="{MONO};font-size:19px;font-weight:700;letter-spacing:.06em;fill:{c}">{t}</text>'
                f'<foreignObject x="160" y="{y + 2}" width="560" height="80"><div xmlns="http://www.w3.org/1999/xhtml" style="{FONT};font-size:22px;line-height:1.35;color:#f1f5f9">{d}</div></foreignObject>')
    return f'<svg viewBox="0 0 720 420" style="width:100%;height:100%;overflow:visible">{out}</svg>'


def tree(lines):
    """Folder tree: lines of (depth, name, comment, color)."""
    out, y = "", 34
    for depth, name, comment, c in lines:
        x = 20 + depth * 40
        if depth:
            out += f'<path d="M{x - 26},{y - 34} V{y - 8} H{x - 8}" fill="none" stroke="#2b3648" stroke-width="2"/>'
        out += (f'<text x="{x}" y="{y}" style="{MONO};font-size:28px;font-weight:700;fill:{c}">{name}</text>'
                f'<text x="{x + len(name) * 17 + 20}" y="{y}" style="{FONT};font-size:22px;fill:#9aa8bc">{comment}</text>')
        y += 52
    return f'<svg viewBox="0 0 760 {y - 10}" style="width:100%;height:auto;overflow:visible">{out}</svg>'


def annotated(src, w, h, marks):
    """Image with numbered callouts. marks: (x%, y%, label, color) in image percentage coords."""
    out = f'<image href="{src}" x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/>'
    for i, (px, py, label, c) in enumerate(marks, 1):
        x, y = w * px / 100, h * py / 100
        tw = len(label) * 18 + 80
        lx = x + 38 if x + tw + 44 < w else x - tw - 38
        out += (f'<circle cx="{x:.0f}" cy="{y:.0f}" r="28" fill="{c}" stroke="#0b0f17" stroke-width="4"/>'
                f'<text x="{x:.0f}" y="{y + 9:.0f}" text-anchor="middle" style="{MONO};font-size:26px;font-weight:700;fill:#0b0f17">{i}</text>'
                f'<rect x="{lx:.0f}" y="{y - 28:.0f}" width="{tw}" height="56" rx="10" fill="rgba(11,15,23,.86)"/>'
                f'<text x="{lx + 18:.0f}" y="{y + 9:.0f}" style="{FONT};font-size:31px;font-weight:600;fill:#f1f5f9">{label}</text>')
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;height:100%;border-radius:12px" preserveAspectRatio="xMidYMid meet">{out}</svg>'
