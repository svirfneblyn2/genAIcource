# Slide 12: Pattern 1: Router & Dispatcher
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 12,
    "kicker": "TOPOLOGY PATTERNS",
    "title": "Pattern 1: Router & Dispatcher Architecture",
    "lead": "Using a lightweight classifier node to dispatch incoming requests to dedicated, single-purpose sub-graphs.",
    "section": "Multi-Agent Topologies",
    "takeaway": "Routers maximize prompt caching and minimize token overhead by keeping specialized sub-graphs completely decoupled.",
    "notes": {
        "goal": "Deep-dive into Pattern 1 (Router/Dispatcher), illustrating intent classification, isolated tool sets, and latency economics.",
        "talkTrack": "The most common architectural mistake in enterprise agents is the 'God Agent' anti-pattern: cramming 40 tools and a 2,000-word prompt into a single model. The model gets confused, tool selection accuracy plummets, and cost explodes. The Router pattern fixes this. A lightweight, fast classifier evaluates the user intent and routes the query to an isolated sub-graph that only possesses the 2 or 3 tools needed for that domain.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("router", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Router Architecture: Intent Classification to Isolated Sub-Graphs</text>

        <!-- Ingress -> Router Node -->
        <g transform="translate(25, 65)">
          <!-- User Ingress -->
          <rect x="0" y="80" width="180" height="85" rx="6" fill="#141c28" stroke="#253245"/>
          <text x="16" y="105" class="text-mono" font-size="10.5">INGRESS QUERY:</text>
          <text x="16" y="125" class="text-p">"Can I get a refund</text>
          <text x="16" y="143" class="text-p">for invoice INV-401?"</text>

          <path d="M 180 122 L 240 122" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Classifier / Router Node -->
          <g transform="translate(250, 45)">
            <rect x="0" y="0" width="260" height="155" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="260" height="30" rx="6" fill="#1e2c42"/>
            <text x="130" y="20" text-anchor="middle" class="text-mono" font-size="11">ROUTER NODE (CLASSIFIER)</text>
            
            <g transform="translate(14, 42)">
              <text x="0" y="14" class="text-dim" font-size="10">Model: Gemini Flash / Claude Haiku</text>
              <text x="0" y="32" class="text-p">Latency SLA: &lt; 350ms</text>
              
              <rect x="0" y="44" width="230" height="55" rx="4" fill="#0b1018" stroke="#3b82f6"/>
              <text x="10" y="62" class="text-mono" font-size="9" fill="#e0c58e">RouteDecision(</text>
              <text x="16" y="76" class="text-mono" font-size="9" fill="#6ee7b7">  target='billing_subgraph',</text>
              <text x="16" y="90" class="text-mono" font-size="9" fill="#cbd5e1">  confidence=0.98)</text>
            </g>
          </g>

          <!-- Routing Conditional Arrows -->
          <path d="M 510 90 L 590 40" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>
          <path d="M 510 122 L 590 122" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>
          <path d="M 510 155 L 590 205" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>

          <!-- 3 Dedicated Sub-Graphs -->
          <!-- Sub-Graph 1: Selected (Billing) -->
          <g transform="translate(600, 0)">
            <rect x="0" y="0" width="370" height="95" rx="6" class="node-box-active-green"/>
            <rect x="0" y="0" width="370" height="26" rx="6" fill="#152420"/>
            <text x="14" y="18" class="text-mono-green" font-size="11">ACTIVE: BILLING SUB-GRAPH</text>
            <text x="14" y="44" class="text-h2">Tools: Stripe API, SAP Invoice Lookup</text>
            <text x="14" y="62" class="text-dim">Context: 1.2k tokens (isolated accounting prompt)</text>
            <text x="14" y="80" class="text-mono-green" font-size="10">Target Activated (Confidence 0.98)</text>
          </g>

          <!-- Sub-Graph 2: Support -->
          <g transform="translate(600, 105)">
            <rect x="0" y="0" width="370" height="75" rx="6" class="node-box"/>
            <text x="14" y="24" class="text-mono" font-size="10.5" fill="#64748b">SUPPORT SUB-GRAPH (BYPASSED)</text>
            <text x="14" y="44" class="text-p" fill="#64748b">Tools: Confluence RAG, Ticket Creator</text>
            <text x="14" y="62" class="text-dim">0 tokens consumed</text>
          </g>

          <!-- Sub-Graph 3: Sales -->
          <g transform="translate(600, 190)">
            <rect x="0" y="0" width="370" height="75" rx="6" class="node-box"/>
            <text x="14" y="24" class="text-mono" font-size="10.5" fill="#64748b">SALES SUB-GRAPH (BYPASSED)</text>
            <text x="14" y="44" class="text-p" fill="#64748b">Tools: Salesforce CRM, Lead Qualifier</text>
            <text x="14" y="62" class="text-dim">0 tokens consumed</text>
          </g>

          <!-- Output Synthesizer -->
          <path d="M 970 47 L 1030 110" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

          <g transform="translate(1040, 75)">
            <rect x="0" y="0" width="165" height="95" rx="6" fill="#141c28" stroke="#3b82f6"/>
            <text x="12" y="24" class="text-mono-green" font-size="10.5">OUTPUT TO USER</text>
            <text x="12" y="48" class="text-p">Refund validated</text>
            <text x="12" y="68" class="text-p">Status: Approved</text>
            <text x="12" y="86" class="text-dim">Total: 720ms SLA</text>
          </g>
        </g>

        <!-- Bottom Benchmark Box -->
        <g transform="translate(25, 320)">
          <rect x="0" y="0" width="1210" height="60" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-green" font-size="11">BENCHMARK ADVANTAGE VS ALL-IN-ONE AGENT:</text>
          <text x="16" y="44" class="text-p">78% reduction in token consumption per session &bull; 99.2% tool call precision (models select from 2 tools instead of 40) &bull; Sub-second p50 latency.</text>
        </g>
      </g>
    """)
}
