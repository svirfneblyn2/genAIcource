# Slide 19: Agent Runtime Choices: Deterministic vs Autonomous
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 19,
    "kicker": "ORCHESTRATION SPECTRUM",
    "title": "Agent Runtime Choices: When Do You Actually Need an Agent?",
    "lead": "The spectrum of orchestration complexity: avoid over-engineering.",
    "section": "Agent Orchestration",
    "takeaway": "For 80% of support assistants, a deterministic DAG is superior: reserve agentic loops for genuine multi-step workflows.",
    "svg": svg_frame(f"""<g transform="translate(40, 25)">
        <!-- Tier 1: Deterministic DAG -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="245" height="395" rx="8" class="node-box-active-green"/>
          <rect x="0" y="0" width="245" height="44" rx="8" fill="#162924"/>
          <text x="16" y="27" class="text-mono-green" font-size="12">TIER 1</text>
          <text x="75" y="27" class="text-h1" font-size="13">Deterministic DAG</text>
          
          <g transform="translate(10, 54)">
            <!-- Visual Topology Diagram Box -->
            <rect x="0" y="0" width="225" height="135" rx="5" fill="#111824" stroke="#253245" stroke-width="1.2"/>
            <text x="10" y="16" class="text-mono-green" font-size="9">TOPOLOGY: LINEAR PIPELINE</text>
            
            <!-- Nodes -->
            <g transform="translate(8, 22)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#141c28" stroke="#253245"/>
              <text x="10" y="14" class="text-mono" font-size="8.5" fill="#93c5fd">1. Query &rarr; Dense Embedding</text>
            </g>
            <path d="M 112 42 L 112 48" stroke="#6ee7b7" stroke-width="1.5" fill="none" marker-end="url(#arr-green)"/>
            
            <g transform="translate(8, 50)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#141c28" stroke="#253245"/>
              <text x="10" y="14" class="text-mono" font-size="8.5" fill="#a7f3d0">2. Vector Search (Top-3)</text>
            </g>
            <path d="M 112 70 L 112 76" stroke="#6ee7b7" stroke-width="1.5" fill="none" marker-end="url(#arr-green)"/>

            <g transform="translate(8, 78)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#172e25" stroke="#6ee7b7" stroke-width="1.2"/>
              <text x="10" y="14" class="text-mono-green" font-size="8.5">3. Grounded Citation Output</text>
            </g>

            <rect x="8" y="106" width="209" height="20" rx="3" fill="#13271f"/>
            <text x="112" y="120" text-anchor="middle" class="text-mono-green" font-size="8">Zero loops &bull; 100% deterministic</text>

            <!-- Production Profile -->
            <g transform="translate(0, 144)">
              <rect x="0" y="0" width="225" height="184" rx="6" fill="#152420" stroke="#6ee7b7" stroke-width="1.2"/>
              <text x="12" y="22" class="text-mono-green" font-size="10.5">PRODUCTION PROFILE</text>
              <text x="12" y="44" class="text-p">&bull; Reliability: 99.5%</text>
              <text x="12" y="66" class="text-p">&bull; Latency: Sub-1.2s TTFT</text>
              <text x="12" y="88" class="text-p">&bull; Cost: 1x baseline</text>
              <text x="12" y="110" class="text-p">&bull; Debug: Direct trace line</text>
              <rect x="8" y="126" width="209" height="46" rx="4" fill="#1b382d" stroke="#6ee7b7" stroke-width="1"/>
              <text x="112" y="144" text-anchor="middle" class="text-mono-green" font-size="10">RECOMMENDED DEFAULT</text>
              <text x="112" y="160" text-anchor="middle" class="text-dim" font-size="8.5">80% of enterprise support</text>
            </g>
          </g>
        </g>

        <!-- Tier 2: Prompt Agent -->
        <g transform="translate(265, 0)">
          <rect x="0" y="0" width="245" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="245" height="44" rx="8" fill="#1b2434"/>
          <text x="16" y="27" class="text-mono" font-size="12">TIER 2</text>
          <text x="75" y="27" class="text-h1" font-size="13">Prompt Agent</text>
          
          <g transform="translate(10, 54)">
            <!-- Visual Topology Diagram Box -->
            <rect x="0" y="0" width="225" height="135" rx="5" fill="#111824" stroke="#253245" stroke-width="1.2"/>
            <text x="10" y="16" class="text-mono" font-size="9">TOPOLOGY: FUNCTION ROUTER</text>
            
            <!-- Nodes -->
            <g transform="translate(8, 22)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#141c28" stroke="#253245"/>
              <text x="10" y="14" class="text-mono" font-size="8.5" fill="#93c5fd">1. LLM Tool-Call Selection</text>
            </g>
            <path d="M 112 42 L 112 48" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>
            
            <g transform="translate(8, 50)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#172233" stroke="#3b82f6" stroke-width="1"/>
              <text x="10" y="14" class="text-mono" font-size="8.5" fill="#93c5fd">2. Host Executes Tool API</text>
            </g>
            <path d="M 112 70 L 112 76" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

            <g transform="translate(8, 78)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#141c28" stroke="#253245"/>
              <text x="10" y="14" class="text-mono" font-size="8.5" fill="#cbd5e1">3. Formatted LLM Response</text>
            </g>

            <rect x="8" y="106" width="209" height="20" rx="3" fill="#172233"/>
            <text x="112" y="120" text-anchor="middle" class="text-mono" font-size="8">Single-turn branch &bull; Fixed tools</text>

            <!-- Production Profile -->
            <g transform="translate(0, 144)">
              <rect x="0" y="0" width="225" height="184" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="12" y="22" class="text-mono" font-size="10.5">PRODUCTION PROFILE</text>
              <text x="12" y="44" class="text-p">&bull; Reliability: 95%</text>
              <text x="12" y="66" class="text-p">&bull; Latency: 2.0s to 3.5s</text>
              <text x="12" y="88" class="text-p">&bull; Cost: 2x baseline</text>
              <text x="12" y="110" class="text-p">&bull; Debug: Standard API logs</text>
              <rect x="8" y="126" width="209" height="46" rx="4" fill="#172233" stroke="#253245"/>
              <text x="112" y="144" text-anchor="middle" class="text-mono" font-size="10">BEST ARCHITECTURAL FIT</text>
              <text x="112" y="160" text-anchor="middle" class="text-dim" font-size="8.5">Single tool lookup (e.g. Weather)</text>
            </g>
          </g>
        </g>

        <!-- Tier 3: Hosted Code Agent -->
        <g transform="translate(530, 0)">
          <rect x="0" y="0" width="245" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="245" height="44" rx="8" fill="#1b2434"/>
          <text x="16" y="27" class="text-mono-purple" font-size="12">TIER 3</text>
          <text x="75" y="27" class="text-h1" font-size="13">Hosted Agent</text>
          
          <g transform="translate(10, 54)">
            <!-- Visual Topology Diagram Box -->
            <rect x="0" y="0" width="225" height="135" rx="5" fill="#111824" stroke="#253245" stroke-width="1.2"/>
            <text x="10" y="16" class="text-mono-purple" font-size="9">TOPOLOGY: BOUNDED STATE MACHINE</text>
            
            <!-- Nodes -->
            <g transform="translate(8, 22)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#221b33" stroke="#b4a4e5" stroke-width="1"/>
              <text x="10" y="14" class="text-mono-purple" font-size="8">Supervisor (Plan &amp; Decide)</text>
            </g>
            
            <!-- Bidirectional loop arrows -->
            <path d="M 50 44 L 50 56" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>
            <path d="M 174 56 L 174 44" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>
            <text x="112" y="52" text-anchor="middle" class="text-mono-purple" font-size="7.5">&le; 3 iterations</text>

            <g transform="translate(8, 58)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#141c28" stroke="#253245"/>
              <text x="10" y="14" class="text-mono" font-size="8" fill="#cbd5e1">Worker Tool Execution</text>
            </g>
            <path d="M 112 78 L 112 84" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>

            <g transform="translate(8, 86)">
              <rect x="0" y="0" width="209" height="20" rx="3" fill="#141c28" stroke="#253245"/>
              <text x="10" y="14" class="text-mono" font-size="8" fill="#cbd5e1">Session Memory &amp; Gate</text>
            </g>

            <rect x="8" y="110" width="209" height="18" rx="3" fill="#221b33"/>
            <text x="112" y="122" text-anchor="middle" class="text-mono-purple" font-size="8">Bounded state loop &bull; Max turns</text>

            <!-- Production Profile -->
            <g transform="translate(0, 144)">
              <rect x="0" y="0" width="225" height="184" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="12" y="22" class="text-mono-purple" font-size="10.5">PRODUCTION PROFILE</text>
              <text x="12" y="44" class="text-p">&bull; Reliability: 88%</text>
              <text x="12" y="66" class="text-p">&bull; Latency: 4.0s to 8.0s</text>
              <text x="12" y="88" class="text-p">&bull; Cost: 4x to 6x baseline</text>
              <text x="12" y="110" class="text-p">&bull; Debug: Requires OTel spans</text>
              <rect x="8" y="126" width="209" height="46" rx="4" fill="#221b33" stroke="#253245"/>
              <text x="112" y="144" text-anchor="middle" class="text-mono-purple" font-size="10">BEST ARCHITECTURAL FIT</text>
              <text x="112" y="160" text-anchor="middle" class="text-dim" font-size="8.5">Multi-system enterprise flows</text>
            </g>
          </g>
        </g>

        <!-- Tier 4: Autonomous Loop -->
        <g transform="translate(795, 0)">
          <rect x="0" y="0" width="245" height="395" rx="8" class="node-box-active-coral"/>
          <rect x="0" y="0" width="245" height="44" rx="8" fill="#29181c"/>
          <text x="16" y="27" class="text-mono-coral" font-size="12">TIER 4</text>
          <text x="75" y="27" class="text-h1" font-size="13">Autonomous Loop</text>
          
          <g transform="translate(10, 54)">
            <!-- Visual Topology Diagram Box -->
            <rect x="0" y="0" width="225" height="135" rx="5" fill="#111824" stroke="#253245" stroke-width="1.2"/>
            <text x="10" y="16" class="text-mono-coral" font-size="9">TOPOLOGY: UNBOUNDED CYCLE</text>
            
            <!-- Cyclic diagram -->
            <g transform="translate(26, 26)">
              <rect x="0" y="0" width="76" height="22" rx="3" fill="#23171a" stroke="#d98585"/>
              <text x="38" y="15" text-anchor="middle" class="text-mono-coral" font-size="8">PLAN</text>

              <path d="M 78 11 L 94 11" stroke="#d98585" stroke-width="1.5" fill="none" marker-end="url(#arr-coral)"/>

              <rect x="96" y="0" width="76" height="22" rx="3" fill="#23171a" stroke="#d98585"/>
              <text x="134" y="15" text-anchor="middle" class="text-mono-coral" font-size="8">ACT</text>

              <path d="M 134 24 L 134 40" stroke="#d98585" stroke-width="1.5" fill="none" marker-end="url(#arr-coral)"/>

              <rect x="96" y="42" width="76" height="22" rx="3" fill="#23171a" stroke="#d98585"/>
              <text x="134" y="57" text-anchor="middle" class="text-mono-coral" font-size="8">OBSERVE</text>

              <path d="M 94 53 L 78 53" stroke="#d98585" stroke-width="1.5" fill="none" marker-end="url(#arr-coral)"/>

              <rect x="0" y="42" width="76" height="22" rx="3" fill="#23171a" stroke="#d98585"/>
              <text x="38" y="57" text-anchor="middle" class="text-mono-coral" font-size="8">REFLECT</text>

              <path d="M 38 40 L 38 24" stroke="#d98585" stroke-width="1.5" fill="none" marker-end="url(#arr-coral)"/>
            </g>

            <rect x="8" y="104" width="209" height="24" rx="3" fill="#29181c" stroke="#d98585" stroke-width="1"/>
            <text x="112" y="119" text-anchor="middle" class="text-mono-coral" font-size="8">Warning: Runaway loop risk</text>

            <!-- Production Profile -->
            <g transform="translate(0, 144)">
              <rect x="0" y="0" width="225" height="184" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="12" y="22" class="text-mono-coral" font-size="10.5">PRODUCTION PROFILE</text>
              <text x="12" y="44" class="text-p">&bull; Reliability: &lt; 65% (Compounding)</text>
              <text x="12" y="66" class="text-p">&bull; Latency: 10s to 60s+</text>
              <text x="12" y="88" class="text-p">&bull; Cost: 10x to 20x+ baseline</text>
              <text x="12" y="110" class="text-p">&bull; Debug: Non-deterministic</text>
              <rect x="8" y="126" width="209" height="46" rx="4" fill="#24191d" stroke="#d98585" stroke-width="1"/>
              <text x="112" y="144" text-anchor="middle" class="text-mono-coral" font-size="10">PRODUCTION WARNING</text>
              <text x="112" y="160" text-anchor="middle" class="text-dim" font-size="8.5">Avoid for end-user support</text>
            </g>
          </g>
        </g>
      </g>"""),
    "notes": {
        "goal": "Introduce a 4-tier spectrum of agentic complexity and argue that a simple, deterministic pipeline is usually superior for customer support.",
        "talkTrack": "De-mystify agents. Start by showing the spectrum from simple prompt-based tool calling to full autonomous loops. Emphasize that for 80% of support cases, a deterministic DAG is faster, cheaper, and far easier to debug. Reserve agentic loops for true multi-step workflows like cross-system ticket escalation. Point out the reliability drop: Tier 1 achieves 99.5% reliability, while an unbounded Tier 4 loop compounds error across turns, dropping below 65% real-world success.",
        "timing": "90:00 - 95:00 (5 min)"
    }
}
