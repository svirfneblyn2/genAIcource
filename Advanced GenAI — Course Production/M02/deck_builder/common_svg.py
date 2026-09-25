# Common SVG utilities and defs for Module 02
from .icons import render_icon

def svg_frame(content, viewBox="0 0 1344 470"):
    return f'''<svg class="blueprint-svg" viewBox="{viewBox}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Arrowhead markers -->
    <marker id="arr-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#60a5fa"/>
    </marker>
    <marker id="arr-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#6ee7b7"/>
    </marker>
    <marker id="arr-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#b4a4e5"/>
    </marker>
    <marker id="arr-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#e0c58e"/>
    </marker>
    <marker id="arr-coral" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d98585"/>
    </marker>
    <marker id="arr-dim" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#64748b"/>
    </marker>

    <!-- Linear Gradients -->
    <linearGradient id="grad-active-blue" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e2c42"/>
      <stop offset="100%" stop-color="#141c28"/>
    </linearGradient>
    <linearGradient id="grad-active-purple" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#261e38"/>
      <stop offset="100%" stop-color="#141c28"/>
    </linearGradient>
    <linearGradient id="grad-active-amber" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2d2516"/>
      <stop offset="100%" stop-color="#141c28"/>
    </linearGradient>
    <linearGradient id="grad-active-green" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#162e24"/>
      <stop offset="100%" stop-color="#141c28"/>
    </linearGradient>
    <linearGradient id="grad-active-coral" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2e181c"/>
      <stop offset="100%" stop-color="#141c28"/>
    </linearGradient>
  </defs>

  {content}
</svg>'''

def render_zone_badge(label, x, y, width=140, height=26, color="#60a5fa", bg="#101722"):
    return f'''<g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{width}" height="{height}" rx="4" fill="{bg}" stroke="{color}" stroke-width="1.2"/>
      <circle cx="10" cy="{height/2}" r="3" fill="{color}"/>
      <text x="20" y="{height/2 + 4}" class="text-mono" font-size="10" font-weight="700" fill="{color}">{label}</text>
    </g>'''

def render_step_pill(num, text, x, y, width=150, height=28, color="#60a5fa"):
    return f'''<g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{width}" height="{height}" rx="4" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
      <rect x="2" y="2" width="24" height="{height-4}" rx="3" fill="#1b2434"/>
      <text x="14" y="{height/2 + 4}" text-anchor="middle" class="text-mono" font-size="10.5" font-weight="700" fill="{color}">{num}</text>
      <text x="34" y="{height/2 + 4}" class="text-p" font-size="11" font-weight="600" fill="#e2e8f0">{text}</text>
    </g>'''
