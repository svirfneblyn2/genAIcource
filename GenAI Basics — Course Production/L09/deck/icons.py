# -*- coding: utf-8 -*-
"""Thin outline icons (24x24 grid) for the L09 schematics — drawn by hand, no external set."""

P = {
    "chat": '<path d="M4 5h16v11H10l-6 4z"/><path d="M8 9h8M8 12h5"/>',
    "doc": '<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h7M9 16h7"/>',
    "slides": '<path d="M3 5h18v12H3z"/><path d="M12 17v3M8 20h8M7 9h6M7 12h9"/>',
    "design": '<path d="M4 20l1-4L16 5l3 3L8 19z"/><path d="M14 7l3 3"/>',
    "dash": '<path d="M4 4v16h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
    "motion": '<circle cx="12" cy="12" r="9"/><path d="M10 8.5l5.5 3.5-5.5 3.5z"/>',
    "app": '<path d="M3 5h18v14H3z"/><path d="M3 9h18M6 7h1M9 7h1"/>',
    "diagram": '<path d="M4 4h6v5H4zM14 15h6v5h-6z"/><path d="M7 9v4h10v2"/>',
    "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 5l-3 14"/>',
    "terminal": '<path d="M3 5h18v14H3z"/><path d="M7 10l3 2-3 2M12 15h5"/>',
    "folder": '<path d="M3 6h6l2 2h10v11H3z"/>',
    "plug": '<path d="M9 3v5M15 3v5"/><path d="M6 8h12v3a6 6 0 0 1-12 0z"/><path d="M12 17v4"/>',
    "skill": '<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>',
    "memory": '<path d="M12 3a9 9 0 1 0 9 9"/><path d="M12 7v5l3 2M17 3h4v4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3.5 3.5 3.5 14.5 0 18M12 3c-3.5 3.5-3.5 14.5 0 18"/>',
    "lock": '<path d="M6 11h12v9H6z"/><path d="M8.5 11V8a3.5 3.5 0 0 1 7 0v3"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.2A5 5 0 0 1 21 19"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "x": '<path d="M6 6l12 12M18 6L6 18"/>',
    "db": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v12c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/>',
    "chip": '<path d="M7 7h10v10H7z"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>',
    "monitor": '<path d="M3 4h18v12H3z"/><path d="M8 20h8M12 16v4"/>',
    "phone": '<path d="M8 3h8v18H8z"/><path d="M11 18h2"/>',
    "sheet": '<path d="M4 4h16v16H4z"/><path d="M4 10h16M4 15h16M10 4v16"/>',
    "search": '<circle cx="11" cy="11" r="6"/><path d="M16 16l5 5"/>',
    "edit": '<path d="M4 20l1-4L16 5l3 3L8 19z"/>',
    "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "mail": '<path d="M3 6h18v12H3z"/><path d="M3 6l9 7 9-7"/>',
    "calendar": '<path d="M4 6h16v14H4z"/><path d="M4 10h16M8 3v5M16 3v5"/>',
    "cloud": '<path d="M7 18h10a4 4 0 0 0 .4-8A6 6 0 0 0 6 11a3.5 3.5 0 0 0 1 7z"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3M14 9l2 2"/>',
    "cursor": '<path d="M5 3l14 7-6 2-2 6z"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6h1M4 12h1M4 18h1"/>',
    "share": '<circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.2 10.8l7.6-3.6M8.2 13.2l7.6 3.6"/>',
    "github": '<path d="M9 19c-4 1.5-4-2-6-2.5M15 21v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.3 4.3 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12 12 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.3 4.3 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
    "warn": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><circle cx="12" cy="12" r="3"/>',
    "loop": '<path d="M20 12a8 8 0 1 1-2.3-5.7"/><path d="M20 4v4h-4"/>',
}


def ico(name, x=0, y=0, s=48, color="#c9d4e3", sw=1.6):
    """Icon as an SVG <g> placed at (x, y) with size s."""
    k = s / 24
    return (f'<g transform="translate({x},{y}) scale({k})" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{P[name]}</g>')


def ico_svg(name, s=64, color="#c9d4e3", sw=1.6):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}">{ico(name, 0, 0, 24, color, sw)}</svg>'
