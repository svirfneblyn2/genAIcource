# Slide 20: Framework Trade-Off Matrix
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 20,
    "kicker": "FRAMEWORK EVALUATION",
    "title": "Framework Comparison Matrix: Technical Dimensions",
    "lead": "Rigorous comparative analysis across state persistence, graph cyclicity, typing, and production readiness.",
    "section": "Framework Landscape",
    "takeaway": "For complex cyclic logic and time-travel debugging, LangGraph leads; for enterprise Microsoft environments, Semantic Kernel leads.",
    "notes": {
        "goal": "Equip students with an architectural decision matrix evaluating frameworks across five technical dimensions.",
        "talkTrack": "When choosing an agent framework, do not rely on GitHub stars. Evaluate these five technical dimensions: Graph Topology, State Persistence, Type Safety, Human-in-the-Loop, and Production Maturity. If your system requires cyclic error recovery, LangGraph is the market leader. If you are deeply embedded in an Azure and C# environment, Semantic Kernel is optimal. If your primary task is RAG document processing, LlamaIndex Workflows shines.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("pipeline", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Enterprise Architectural Comparison Matrix</text>

        <!-- Matrix Table -->
        <g transform="translate(20, 58)">
          <!-- Header Row -->
          <rect x="0" y="0" width="1220" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="15" y="24" class="text-mono" font-size="11" fill="#64748b">FRAMEWORK</text>
          <text x="210" y="24" class="text-mono" font-size="11" fill="#64748b">TOPOLOGY</text>
          <text x="440" y="24" class="text-mono" font-size="11" fill="#64748b">STATE PERSISTENCE</text>
          <text x="680" y="24" class="text-mono" font-size="11" fill="#64748b">TYPE SAFETY</text>
          <text x="890" y="24" class="text-mono" font-size="11" fill="#64748b">HITL MECHANICS</text>
          <text x="1080" y="24" class="text-mono" font-size="11" fill="#64748b">PROD MATURITY</text>

          <!-- Row 1: LangGraph -->
          <g transform="translate(0, 44)">
            <rect x="0" y="0" width="1220" height="52" rx="4" fill="#1e2c42" stroke="#3b82f6" stroke-width="1.2"/>
            <text x="15" y="32" class="text-h2" fill="#60a5fa">LangGraph</text>
            <text x="210" y="32" class="text-mono-green" font-size="11">Cyclic State Graph</text>
            <text x="440" y="32" class="text-p">Postgres / Redis / Memory</text>
            <text x="680" y="32" class="text-mono" font-size="11">TypedDict + Pydantic</text>
            <text x="890" y="32" class="text-mono-green" font-size="11">interrupt_before / mutate</text>
            <rect x="1080" y="14" width="125" height="24" rx="3" fill="#152420" stroke="#6ee7b7"/>
            <text x="1142" y="30" text-anchor="middle" class="text-mono-green" font-size="10">High (Tier 1)</text>
          </g>

          <!-- Row 2: LlamaIndex Workflows -->
          <g transform="translate(0, 102)">
            <rect x="0" y="0" width="1220" height="52" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="15" y="32" class="text-h2" fill="#e0c58e">LlamaIndex Workflows</text>
            <text x="210" y="32" class="text-p">Async Event Pub/Sub</text>
            <text x="440" y="32" class="text-p">LlamaCloud / Key-Value</text>
            <text x="680" y="32" class="text-mono-amber" font-size="11">Pydantic Event Classes</text>
            <text x="890" y="32" class="text-p">Event Listener Pauses</text>
            <rect x="1080" y="14" width="125" height="24" rx="3" fill="#172233" stroke="#60a5fa"/>
            <text x="1142" y="30" text-anchor="middle" class="text-mono" font-size="10">High (Data/RAG)</text>
          </g>

          <!-- Row 3: AutoGen -->
          <g transform="translate(0, 160)">
            <rect x="0" y="0" width="1220" height="52" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="15" y="32" class="text-h2" fill="#6ee7b7">AutoGen (MSFT)</text>
            <text x="210" y="32" class="text-p">Conversational Chat Loop</text>
            <text x="440" y="32" class="text-p">Disk Cache / Custom JSON</text>
            <text x="680" y="32" class="text-dim">Dict / Dynamic Messages</text>
            <text x="890" y="32" class="text-p">HumanInputMode.ALWAYS</text>
            <rect x="1080" y="14" width="125" height="24" rx="3" fill="#2d2516" stroke="#e0c58e"/>
            <text x="1142" y="30" text-anchor="middle" class="text-mono-amber" font-size="10">Moderate (Research)</text>
          </g>

          <!-- Row 4: CrewAI -->
          <g transform="translate(0, 218)">
            <rect x="0" y="0" width="1220" height="52" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="15" y="32" class="text-h2" fill="#d98585">CrewAI</text>
            <text x="210" y="32" class="text-p">Sequential / Hierarchical</text>
            <text x="440" y="32" class="text-p">SQLite / Memory Store</text>
            <text x="680" y="32" class="text-mono" font-size="11">Pydantic Task Outputs</text>
            <text x="890" y="32" class="text-p">CLI Human Input Flag</text>
            <rect x="1080" y="14" width="125" height="24" rx="3" fill="#24191d" stroke="#d98585"/>
            <text x="1142" y="30" text-anchor="middle" class="text-mono-coral" font-size="10">Early (PoC Fast)</text>
          </g>

          <!-- Row 5: Semantic Kernel -->
          <g transform="translate(0, 276)">
            <rect x="0" y="0" width="1220" height="52" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="15" y="32" class="text-h2" fill="#b4a4e5">Semantic Kernel</text>
            <text x="210" y="32" class="text-p">Plan-Execute Pipeline</text>
            <text x="440" y="32" class="text-p">Azure Cosmos / Redis</text>
            <text x="680" y="32" class="text-mono-purple" font-size="11">Strict C# / Pydantic</text>
            <text x="890" y="32" class="text-p">Filter Middleware Hooks</text>
            <rect x="1080" y="14" width="125" height="24" rx="3" fill="#152420" stroke="#6ee7b7"/>
            <text x="1142" y="30" text-anchor="middle" class="text-mono-green" font-size="10">High (MSFT .NET)</text>
          </g>
        </g>
      </g>
    """)
}
