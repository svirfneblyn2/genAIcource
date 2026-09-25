import os

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
COURSE_DIR = os.path.dirname(TOOLS_DIR)
icons_path = os.path.join(COURSE_DIR, "M02", "deck_builder", "icons.py")
logos_path = os.path.join(COURSE_DIR, "M02", "deck_builder", "logos.py")
common_svg_path = os.path.join(COURSE_DIR, "M02", "deck_builder", "common_svg.py")

icons_content = "# Outline Icons from Visual Asset Library for Module 02
# Clean, outline-only, 24x24 viewBox, stroke-width=1.7, stroke=currentColor, fill=none

ICONS = {
    'agent': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><rect x=5 y=8 width=14 height=11 rx=3/><path d=M12 4v4/><circle cx=12 cy=3 r=1/><circle cx=9 cy=13 r=1/><circle cx=15 cy=13 r=1/><path d=M9 16h6/></g>',
    'state_machine': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=6 cy=12 r=3/><circle cx=18 cy=6 r=3/><circle cx=18 cy=18 r=3/><path d=M8.7 10.7l6.6-3.4M8.7 13.3l6.6 3.4M18 9v6/></g>',
    'cycle': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M21 12a9 9 0 0 0-15.5-6.4L3 8/><path d=M3 3v5h5/><path d=M3 12a9 9 0 0 0 15.5 6.4L21 16/><path d=M21 21v-5h-5/></g>',
    'checkpoint': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z/><polyline points=17 21 17 13 7 13 7 21/><polyline points=7 3 7 8 15 8/></g>',
    'database': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><ellipse cx=12 cy=5 rx=7 ry=3/><path d=M5 5v6c0 1.7 3.1 3 7 3s7-1.3 7-3V5/><path d=M5 11v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6/></g>',
    'memory': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><rect x=4 y=4 width=16 height=16 rx=2/><rect x=9 y=9 width=6 height=6/><path d=M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3/></g>',
    'branch': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><line x1=6 y1=3 x2=6 y2=15/><circle cx=18 cy=6 r=3/><circle cx=6 cy=18 r=3/><path d=M18 9a9 9 0 0 1-9 9/></g>',
    'fork': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=12 cy=18 r=3/><circle cx=6 cy=6 r=3/><circle cx=18 cy=6 r=3/><path d=M18 9v2a3 3 0 0 1-3 3h-6a3 3 0 0 1-3-3V9/><path d=M12 12v3/></g>',
    'tool': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M14 4a4 4 0 0 0-5 5L3 15l6 6 6-6a4 4 0 0 0 5-5l-4 2-2-2z/></g>',
    'sandbox': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><rect x=3 y=3 width=18 height=18 rx=3/><path d=M3 9h18M9 21V9/><circle cx=6 cy=6 r=1 fill=currentColor/></g>',
    'shield': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M12 3l7 3v5c0 4.8-2.8 8.1-7 10-4.2-1.9-7-5.2-7-10V6z/><path d=M9 12l2 2 4-4/></g>',
    'alert': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M12 3l10 18H2z/><path d=M12 9v5M12 18h.01/></g>',
    'approval': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=12 cy=12 r=9/><path d=M8 12l2.5 2.5L16 9 stroke=currentColor/></g>',
    'circuit_breaker': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><rect x=4 y=4 width=16 height=16 rx=2/><path d=M8 12h3M13 12h3/><circle cx=12 cy=7 r=1 fill=currentColor/><circle cx=12 cy=17 r=1 fill=currentColor/></g>',
    'router': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><rect x=3 y=7 width=18 height=10 rx=2/><circle cx=6.5 cy=12 r=1 fill=currentColor/><circle cx=10 cy=12 r=1 fill=currentColor/><path d=M17 10l2 2-2 2M7 4v3M17 4v3/></g>',
    'supervisor': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=12 cy=7 r=4/><path d=M5 21v-2a7 7 0 0 1 14 0v2/><circle cx=12 cy=7 r=1/><path d=M9 3l3-2 3 2/></g>',
    'swarm': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=6 cy=6 r=2.5/><circle cx=18 cy=6 r=2.5/><circle cx=12 cy=18 r=2.5/><path d=M8 7.5l2.5 7M16 7.5l-2.5 7M8.5 6h7 stroke-dasharray=2 2/></g>',
    'hierarchy': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><rect x=9 y=3 width=6 height=4 rx=1/><rect x=3 y=15 width=5 height=4 rx=1/><rect x=10 y=15 width=5 height=4 rx=1/><rect x=17 y=15 width=5 height=4 rx=1/><path d=M12 7v4M5.5 15v-2a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v2M12.5 11v4/></g>',
    'timeline': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=5 cy=12 r=2/><circle cx=12 cy=12 r=2/><circle cx=19 cy=12 r=2/><path d=M7 12h3M14 12h3/><path d=M5 6v4M12 6v4M19 6v4/></g>',
    'trace': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M3 6h18M7 12h14M11 18h10/><circle cx=4 cy=12 r=1.5 fill=currentColor/><circle cx=8 cy=18 r=1.5 fill=currentColor/></g>',
    'search': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=10.5 cy=10.5 r=6/><path d=M15 15l5 5/></g>',
    'document': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M6 2h8l4 4v16H6z/><path d=M14 2v5h5/><path d=M9 11h6M9 15h6M9 19h4/></g>',
    'clock': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=12 cy=12 r=9/><polyline points=12 7 12 12 15 15/></g>',
    'cost': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=12 cy=12 r=8/><path d=M14.5 8.5c-.8-.7-1.7-1-2.8-1-1.7 0-3 1-3 2.3 0 1.4 1.1 2 3.2 2.6 2 .6 3 1.2 3 2.6 0 1.5-1.4 2.6-3.4 2.6-1.2 0-2.4-.4-3.3-1.2M12 6v12/></g>',
    'metric': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M4 19V11M9 19V7M14 19V13M19 19V4/><path d=M3 19h18/></g>',
    'network': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=6 cy=6 r=2/><circle cx=18 cy=6 r=2/><circle cx=12 cy=18 r=2/><path d=M8 7l3 8M16 7l-3 8M8 6h8/></g>',
    'code': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><polyline points=16 18 22 12 16 6/><polyline points=8 6 2 12 8 18/></g>',
    'ticket': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><path d=M4 7h16v4a2 2 0 0 0 0 4v4H4v-4a2 2 0 0 0 0-4z/><path d=M12 9v6/></g>',
    'pipeline': '<g stroke=currentColor stroke-width=inherit fill=none stroke-linecap=round stroke-linejoin=round><circle cx=5 cy=12 r=2/><circle cx=12 cy=12 r=2/><circle cx=19 cy=12 r=2/><path d=M7 12h3M14 12h3/></g>'
}

def render_icon(name, x, y, size=24, color=#60a5fa, stroke_width=1.7):
    inner = ICONS.get(name, ")
 if not inner:
 return 
 scale = size / 24.0
 return f'<g transform=translate({x}, {y}) scale({scale}) color={color} stroke={color} stroke-width={stroke_width} fill=none>{inner}</g>'
"

logos_content = "# Vector SVG Logos for Frameworks and Platforms in Module 02
# Scalable inline SVGs for 24x24 viewBox

LOGOS = {
 # LangGraph: Hexagonal state graph with directed cyclic nodes
 'langgraph': (
 '<g fill=currentColor>'
 '<circle cx=6 cy=7 r=2.5/>'
 '<circle cx=18 cy=7 r=2.5/>'
 '<circle cx=12 cy=18 r=2.5/>'
 '<path d=M8.5 7h7M16.5 9l-3.5 6.5M10.5 15.5L7.5 9 fill=none stroke=currentColor stroke-width=1.8 stroke-linecap=round/>'
 '<path d=M11 6.5l2.5.5-1.5 2 fill=currentColor/>'
 '</g>'
 ),

 # LangChain: Parrot outline & chain links
 'langchain': (
 '<g stroke=currentColor stroke-width=1.8 fill=none stroke-linecap=round stroke-linejoin=round>'
 '<path d=M9 15l-3 3a3 3 0 0 1-4.2-4.2l3-3a3 3 0 0 1 4.2 0/>'
 '<path d=M15 9l3-3a3 3 0 0 1 4.2 4.2l-3 3a3 3 0 0 1-4.2 0/>'
 '<line x1=10 y1=14 x2=14 y2=10/>'
 '</g>'
 ),

 # LlamaIndex: Geometric llama head silhouette
 'llamaindex': (
 '<g fill=currentColor>'
 '<path d=M7 21h10v-3h-3v-6l4-5V3h-4v2l-3 4V3H7v7l2 3v5H7v3z/>'
 '<circle cx=9.5 cy=5.5 r=1 fill=#0e131b/>'
 '</g>'
 ),

 # AutoGen: Multi-agent conversational feedback loop
 'autogen': (
 '<g fill=none stroke=currentColor stroke-width=1.8 stroke-linecap=round stroke-linejoin=round>'
 '<circle cx=7 cy=8 r=3.5/>'
 '<circle cx=17 cy=8 r=3.5/>'
 '<circle cx=12 cy=17 r=3.5/>'
 '<path d=M9 10l2 4M15 10l-2 4M10 8h4/>'
 '</g>'
 ),

 # CrewAI: Team crew icon
 'crewai': (
 '<g fill=currentColor>'
 '<circle cx=12 cy=6 r=3/>'
 '<circle cx=5 cy=9 r=2.2/>'
 '<circle cx=19 cy=9 r=2.2/>'
 '<path d=M7 20v-2a5 5 0 0 1 10 0v2H7z/>'
 '<path d=M2 20v-1a4 4 0 0 1 4-4h.5M22 20v-1a4 4 0 0 0-4-4h-.5/>'
 '</g>'
 ),

 # Semantic Kernel: Microsoft spark with kernel cog
 'semantic_kernel': (
 '<g fill=currentColor>'
 '<path d=M12 2l1.5 5.5L19 9l-5.5 1.5L12 16l-1.5-5.5L5 9l5.5-1.5L12 2z/>'
 '<circle cx=18 cy=18 r=3 fill=none stroke=currentColor stroke-width=1.5/>'
 '<circle cx=6 cy=18 r=2 fill=none stroke=currentColor stroke-width=1.5/>'
 '</g>'
 ),

 # OpenAI / Swarm: 6-fold spiral rosette
 'openai': (
 '<g fill=currentColor>'
 '<path d=M20.5 10.2a5.4 5.4 0 0 0-.4-4.2 5.5 5.5 0 0 0-4.7-2.7 5.4 5.4 0 0 0-3.3 1.1A5.4 5.4 0 0 0 7.8 3a5.5 5.5 0 0 0-5.3 4 5.4 5.4 0 0 0 .8 5.4 5.4 5.4 0 0 0-.4 4.2 5.5 5.5 0 0 0 4.7 2.7 5.4 5.4 0 0 0 3.3-1.1A5.4 5.4 0 0 0 15.2 21a5.5 5.5 0 0 0 5.3-4 5.4 5.4 0 0 0-.8-5.4l.8-1.4zm-7.6 9.4c-1.3 0-2.5-.5-3.4-1.4l.8-.5 3.3-1.9a.8.8 0 0 0 .4-.7v-4.5l1.4.8v3.9a3.7 3.7 0 0 1-2.5 4.3zm-7.6-3.2a3.7 3.7 0 0 1-.4-4.9l.8.5 3.3 1.9c.2.1.5.1.7 0l3.9-2.3v1.6l-3.4 2a3.7 3.7 0 0 1-4.9 1.2zm-1.1-7.7a3.7 3.7 0 0 1 2.1-3.6v6.2l3.9-2.3v-1.6l-3.4-2a3.7 3.7 0 0 1-2.6 3.3zm12.3-1.3l-3.9 2.3v-1.6l3.4-2a3.7 3.7 0 0 1 4.5 1.5 3.7 3.7 0 0 1-.4 4.9l-.8-.5-3.3-1.9a.8.8 0 0 0-.7 0l.2-.7zm2.8 5.6a3.7 3.7 0 0 1-2.1 3.6v-6.2l-3.9 2.3v1.6l3.4 2a3.7 3.7 0 0 1 2.6-3.3zm-6.9-1.9l-1.9-1.1 1.9-1.1 1.9 1.1-1.9 1.1z/>'
 '</g>'
 ),

 # Redis: Isometric memory grid layers
 'redis': (
 '<g fill=currentColor>'
 '<path d=M12 3L2 8l10 5 10-5-10-5z opacity=0.9/>'
 '<path d=M2 12l10 5 10-5-1.5-.7L12 15.5 3.5 11.3 2 12z opacity=0.75/>'
 '<path d=M2 16l10 5 10-5-1.5-.7L12 19.5 3.5 15.3 2 16z opacity=0.6/>'
 '</g>'
 ),

 # PostgreSQL / pgvector: Elephant head silhouette
 'postgres': (
 '<g fill=currentColor>'
 '<path d=M12 2C8 2 5 5 5 9c0 3 2 6 4 8v3h3v-2c2 1 5 1 7-1 2-2 3-5 3-8 0-4-4-7-7-7zm3 10c-.6 0-1-.4-1-1s.4-1 1-1 1 .4 1 1-.4 1-1 1zm-6 0c-.6 0-1-.4-1-1s.4-1 1-1 1 .4 1 1-.4 1-1 1z/>'
 '</g>'
 ),

 # Docker: Whale carrying containers
 'docker': (
 '<g fill=currentColor>'
 '<rect x=4 y=9 width=3 height=3 rx=0.3/>'
 '<rect x=8 y=9 width=3 height=3 rx=0.3/>'
 '<rect x=12 y=9 width=3 height=3 rx=0.3/>'
 '<rect x=8 y=5 width=3 height=3 rx=0.3/>'
 '<rect x=12 y=5 width=3 height=3 rx=0.3/>'
 '<rect x=16 y=9 width=3 height=3 rx=0.3/>'
 '<path d=M21.5 12.5c-.5-.3-1.5-.3-2.2.2-1-1-2.5-.9-3.3-.8C14.5 12 11 12 8 13.5c-3 1.5-5 4-5 5.5 0 2 3.5 3 9 3s9-2.5 9.5-6.5c0-.5.5-1.5 0-3z/>'
 '</g>'
 ),

 # E2B: Sandbox lightning box
 'e2b': (
 '<g fill=none stroke=currentColor stroke-width=1.8 stroke-linecap=round stroke-linejoin=round>'
 '<rect x=3 y=4 width=18 height=16 rx=3/>'
 '<path d=M13 7l-4 6h5l-2 5 fill=currentColor stroke=none/>'
 '</g>'
 ),

 # OpenTelemetry: Telemetry telescope / sensor ring
 'opentelemetry': (
 '<g stroke=currentColor stroke-width=1.8 fill=none stroke-linecap=round stroke-linejoin=round>'
 '<circle cx=12 cy=12 r=8/>'
 '<circle cx=12 cy=12 r=3 fill=currentColor/>'
 '<path d=M12 4v3M12 17v3M4 12h3M17 12h3/>'
 '</g>'
 ),

 # LangSmith: Tracing hammer & compass
 'langsmith': (
 '<g stroke=currentColor stroke-width=1.8 fill=none stroke-linecap=round stroke-linejoin=round>'
 '<circle cx=12 cy=12 r=8/>'
 '<path d=M8 8l8 8M8 16l8-8/>'
 '<circle cx=12 cy=12 r=2 fill=currentColor/>'
 '</g>'
 ),

 # Arize Phoenix: Flame / Diamond trace observer
 'phoenix': (
 '<g fill=currentColor>'
 '<path d=M12 2L4 12l8 10 8-10L12 2zm0 4.5l5 6.5-5 5-5-5 5-6.5z/>'
 '</g>'
 ),

 # AWS: Cloud arrow
 'aws': (
 '<g stroke=currentColor stroke-width=1.8 fill=none stroke-linecap=round stroke-linejoin=round>'
 '<path d=M4 15c4 4 12 4 16 0/>'
 '<path d=M17 17l3-2-1-3/>'
 '<path d=M6 7l2 6 2-6M12 7v6M16 7l2 6 2-6/>'
 '</g>'
 ),

 # Azure: 4-square grid
 'azure': (
 '<g fill=currentColor>'
 '<rect x=3 y=3 width=8 height=8 rx=1/>'
 '<rect x=13 y=3 width=8 height=8 rx=1/>'
 '<rect x=3 y=13 width=8 height=8 rx=1/>'
 '<rect x=13 y=13 width=8 height=8 rx=1/>'
 '</g>'
 ),

 # Google Cloud: Cloud node
 'gcp': (
 '<g stroke=currentColor stroke-width=1.8 fill=none stroke-linecap=round stroke-linejoin=round>'
 '<path d=M7 18h10a4 4 0 0 0 .4-8 5.5 5.5 0 0 0-10.5-1.6A4.2 4.2 0 0 0 7 18z/>'
 '<circle cx=12 cy=12 r=2 fill=currentColor/>'
 '</g>'
 ),

 # Ollama: Local LLM runtime llama
 'ollama': (
 '<g fill=currentColor>'
 '<path d=M9 3v4h2v3l-3 4v7h8v-7l-3-4V7h2V3H9z/>'
 '<circle cx=10 cy=5 r=0.8 fill=#0e131b/>'
 '</g>'
 )
}

def render_logo(name, x, y, size=24, color=#60a5fa):
 inner = LOGOS.get(name, )
 if not inner:
 return 
 scale = size / 24.0
 return f'<g transform=translate({x}, {y}) scale({scale}) color={color}>{inner}</g>'

def render_logo_badge(name, x, y, label, width=130, height=32, color=#60a5fa, bg=#141c28, border=#253245, text_color=#cbd5e1):
 logo_svg = render_logo(name, 8, int((height - 18) / 2), size=18, color=color)
 return f'''<g transform=translate({x}, {y})>
 <rect x=0 y=0 width={width} height={height} rx=5 fill={bg} stroke={border} stroke-width=1.2/>
 {logo_svg}
 <text x=32 y={int(height / 2 + 4)} class=text-mono font-size=11 fill={text_color}>{label}</text>
 </g>'''
"

common_svg_content = "# Common SVG utilities and defs for Module 02
from .icons import render_icon

def svg_frame(content, viewBox=0 0 1344 470):
 return f'''<svg class=blueprint-svg viewBox={viewBox} xmlns=http://www.w3.org/2000/svg>
 <defs>
 <!-- Arrowhead markers -->
 <marker id=arr-blue viewBox=0 0 10 10 refX=8 refY=5 markerWidth=6 markerHeight=6 orient=auto-start-reverse>
 <path d=M 0 1.5 L 8 5 L 0 8.5 z fill=#60a5fa/>
 </marker>
 <marker id=arr-green viewBox=0 0 10 10 refX=8 refY=5 markerWidth=6 markerHeight=6 orient=auto-start-reverse>
 <path d=M 0 1.5 L 8 5 L 0 8.5 z fill=#6ee7b7/>
 </marker>
 <marker id=arr-purple viewBox=0 0 10 10 refX=8 refY=5 markerWidth=6 markerHeight=6 orient=auto-start-reverse>
 <path d=M 0 1.5 L 8 5 L 0 8.5 z fill=#b4a4e5/>
 </marker>
 <marker id=arr-amber viewBox=0 0 10 10 refX=8 refY=5 markerWidth=6 markerHeight=6 orient=auto-start-reverse>
 <path d=M 0 1.5 L 8 5 L 0 8.5 z fill=#e0c58e/>
 </marker>
 <marker id=arr-coral viewBox=0 0 10 10 refX=8 refY=5 markerWidth=6 markerHeight=6 orient=auto-start-reverse>
 <path d=M 0 1.5 L 8 5 L 0 8.5 z fill=#d98585/>
 </marker>
 <marker id=arr-dim viewBox=0 0 10 10 refX=8 refY=5 markerWidth=6 markerHeight=6 orient=auto-start-reverse>
 <path d=M 0 1.5 L 8 5 L 0 8.5 z fill=#64748b/>
 </marker>

 <!-- Linear Gradients -->
 <linearGradient id=grad-active-blue x1=0 y1=0 x2=0 y2=1>
 <stop offset=0% stop-color=#1e2c42/>
 <stop offset=100% stop-color=#141c28/>
 </linearGradient>
 <linearGradient id=grad-active-purple x1=0 y1=0 x2=0 y2=1>
 <stop offset=0% stop-color=#261e38/>
 <stop offset=100% stop-color=#141c28/>
 </linearGradient>
 <linearGradient id=grad-active-amber x1=0 y1=0 x2=0 y2=1>
 <stop offset=0% stop-color=#2d2516/>
 <stop offset=100% stop-color=#141c28/>
 </linearGradient>
 <linearGradient id=grad-active-green x1=0 y1=0 x2=0 y2=1>
 <stop offset=0% stop-color=#162e24/>
 <stop offset=100% stop-color=#141c28/>
 </linearGradient>
 <linearGradient id=grad-active-coral x1=0 y1=0 x2=0 y2=1>
 <stop offset=0% stop-color=#2e181c/>
 <stop offset=100% stop-color=#141c28/>
 </linearGradient>
 </defs>

 {content}
</svg>'''

def render_zone_badge(label, x, y, width=140, height=26, color=#60a5fa, bg=#101722):
 return f'''<g transform=translate({x}, {y})>
 <rect x=0 y=0 width={width} height={height} rx=4 fill={bg} stroke={color} stroke-width=1.2/>
 <circle cx=10 cy={height/2} r=3 fill={color}/>
 <text x=20 y={height/2 + 4} class=text-mono font-size=10 font-weight=700 fill={color}>{label}</text>
 </g>'''

def render_step_pill(num, text, x, y, width=150, height=28, color=#60a5fa):
 return f'''<g transform=translate({x}, {y})>
 <rect x=0 y=0 width={width} height={height} rx=4 fill=#141c28 stroke=#253245 stroke-width=1.2/>
 <rect x=2 y=2 width=24 height={height-4} rx=3 fill=#1b2434/>
 <text x=14 y={height/2 + 4} text-anchor=middle class=text-mono font-size=10.5 font-weight=700 fill={color}>{num}</text>
 <text x=34 y={height/2 + 4} class=text-p font-size=11 font-weight=600 fill=#e2e8f0>{text}</text>
 </g>'''
"

with open(icons_path, w, encoding=utf-8) as f:
 f.write(icons_content)
with open(logos_path, w, encoding=utf-8) as f:
 f.write(logos_content)
with open(common_svg_path, w, encoding=utf-8) as f:
 f.write(common_svg_content)

print(Icons, logos, and common_svg successfully generated!)
