# Slide 11: Multi-Agent Network Topologies
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 11,
    "kicker": "MULTI-AGENT SYSTEMS",
    "title": "Taxonomy of Multi-Agent Coordination Topologies",
    "lead": "Selecting the optimal network structure based on task modularity, context boundaries, and latency budgets.",
    "section": "Multi-Agent Topologies",
    "takeaway": "Topology is an engineering trade-off between centralized predictability and decentralized flexibility.",
    "notes": {
        "goal": "Introduce the four primary multi-agent network topologies that govern enterprise agent orchestration.",
        "talkTrack": "When a single agent context becomes too cluttered with tools and prompts, engineers divide the work among multiple agents. But how should those agents communicate? There is no single universal topology. We classify multi-agent networks into four fundamental design patterns: the Router, the Supervisor, the Peer Swarm, and Hierarchical Teams. Choosing the wrong pattern leads to either chaotic token loops or rigid bottlenecks.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- 4 Quadrants -->
        <!-- Quadrant 1: Router -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="610" height="190" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="610" height="34" rx="8" fill="#1e2c42"/>
          {render_icon("router", 12, 6, size=20, color="#60a5fa")}
          <text x="40" y="22" class="text-h2" fill="#60a5fa">PATTERN 1: DETERMINISTIC ROUTER / DISPATCHER</text>

          <g transform="translate(15, 45)">
            <!-- Mini Blueprint -->
            <rect x="0" y="10" width="85" height="40" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="42" y="34" text-anchor="middle" class="text-mono" font-size="9">Ingress</text>

            <path d="M 85 30 L 120 30" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

            <rect x="125" y="5" width="95" height="50" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
            <text x="172" y="27" text-anchor="middle" class="text-mono" font-size="9.5">Router Node</text>
            <text x="172" y="42" text-anchor="middle" class="text-dim" font-size="8.5">Classifier</text>

            <!-- 3 Output Arrows -->
            <path d="M 220 20 L 255 10" stroke="#60a5fa" stroke-width="1.2" fill="none" marker-end="url(#arr-blue)"/>
            <path d="M 220 30 L 255 30" stroke="#60a5fa" stroke-width="1.2" fill="none" marker-end="url(#arr-blue)"/>
            <path d="M 220 40 L 255 50" stroke="#60a5fa" stroke-width="1.2" fill="none" marker-end="url(#arr-blue)"/>

            <!-- 3 Target Sub-Graphs -->
            <rect x="260" y="0" width="75" height="20" rx="3" fill="#141c28" stroke="#253245"/>
            <text x="297" y="14" text-anchor="middle" class="text-mono" font-size="8">Graph A</text>

            <rect x="260" y="22" width="75" height="20" rx="3" fill="#141c28" stroke="#253245"/>
            <text x="297" y="36" text-anchor="middle" class="text-mono" font-size="8">Graph B</text>

            <rect x="260" y="44" width="75" height="20" rx="3" fill="#141c28" stroke="#253245"/>
            <text x="297" y="58" text-anchor="middle" class="text-mono" font-size="8">Graph C</text>

            <!-- Specs -->
            <g transform="translate(355, 0)">
              <text x="0" y="16" class="text-mono-green" font-size="10">COORDINATION MODEL:</text>
              <text x="0" y="34" class="text-p">&bull; 1-to-N single-turn dispatch</text>
              <text x="0" y="52" class="text-p">&bull; Sub-graphs execute in complete isolation</text>
              <text x="0" y="70" class="text-dim">&bull; Minimal token overhead; fast routing</text>
            </g>
          </g>
        </g>

        <!-- Quadrant 2: Supervisor -->
        <g transform="translate(630, 0)">
          <rect x="0" y="0" width="630" height="190" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="630" height="34" rx="8" fill="#1e2c42"/>
          {render_icon("supervisor", 12, 6, size=20, color="#b4a4e5")}
          <text x="40" y="22" class="text-h2" fill="#b4a4e5">PATTERN 2: SUPERVISOR &amp; WORKER AGENTS</text>

          <g transform="translate(15, 45)">
            <!-- Mini Blueprint -->
            <rect x="0" y="10" width="115" height="50" rx="4" fill="#241b33" stroke="#b4a4e5"/>
            <text x="57" y="30" text-anchor="middle" class="text-mono-purple" font-size="9.5">Supervisor</text>
            <text x="57" y="45" text-anchor="middle" class="text-dim" font-size="8.5">Owns Plan &amp; State</text>

            <path d="M 115 25 L 155 15" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>
            <path d="M 155 18 L 115 30" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="2 2" fill="none"/>

            <path d="M 115 45 L 155 55" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>
            <path d="M 155 58 L 115 48" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="2 2" fill="none"/>

            <rect x="160" y="0" width="100" height="30" rx="3" fill="#141c28" stroke="#253245"/>
            <text x="210" y="19" text-anchor="middle" class="text-mono" font-size="8.5">Worker: Coder</text>

            <rect x="160" y="40" width="100" height="30" rx="3" fill="#141c28" stroke="#253245"/>
            <text x="210" y="59" text-anchor="middle" class="text-mono" font-size="8.5">Worker: QA</text>

            <!-- Specs -->
            <g transform="translate(285, 0)">
              <text x="0" y="16" class="text-mono-purple" font-size="10">COORDINATION MODEL:</text>
              <text x="0" y="34" class="text-p">&bull; Central supervisor delegates subtasks</text>
              <text x="0" y="52" class="text-p">&bull; Workers run in ephemeral scratchpads</text>
              <text x="0" y="70" class="text-dim">&bull; Supervisor synthesizes final result</text>
            </g>
          </g>
        </g>

        <!-- Quadrant 3: Swarm / Peer-to-Peer -->
        <g transform="translate(0, 210)">
          <rect x="0" y="0" width="610" height="190" rx="8" class="node-box"/>
          <rect x="0" y="0" width="610" height="34" rx="8" fill="#1b2434"/>
          {render_icon("swarm", 12, 6, size=20, color="#6ee7b7")}
          <text x="40" y="22" class="text-h2" fill="#6ee7b7">PATTERN 3: SWARM &amp; PEER-TO-PEER HANDOFFS</text>

          <g transform="translate(15, 45)">
            <!-- Mini Blueprint -->
            <rect x="0" y="15" width="85" height="40" rx="4" fill="#141c28" stroke="#6ee7b7"/>
            <text x="42" y="38" text-anchor="middle" class="text-mono-green" font-size="9">Agent A</text>

            <path d="M 85 30 L 125 15" stroke="#6ee7b7" stroke-width="1.5" fill="none" marker-end="url(#arr-green)"/>
            <path d="M 125 20 L 85 35" stroke="#6ee7b7" stroke-width="1.2" stroke-dasharray="2 2" fill="none"/>

            <rect x="130" y="0" width="85" height="40" rx="4" fill="#141c28" stroke="#6ee7b7"/>
            <text x="172" y="24" text-anchor="middle" class="text-mono-green" font-size="9">Agent B</text>

            <path d="M 215 20 L 255 35" stroke="#6ee7b7" stroke-width="1.5" fill="none" marker-end="url(#arr-green)"/>

            <rect x="260" y="15" width="85" height="40" rx="4" fill="#141c28" stroke="#6ee7b7"/>
            <text x="302" y="38" text-anchor="middle" class="text-mono-green" font-size="9">Agent C</text>

            <!-- Specs -->
            <g transform="translate(365, 0)">
              <text x="0" y="16" class="text-mono-green" font-size="10">COORDINATION MODEL:</text>
              <text x="0" y="34" class="text-p">&bull; Decentralized direct handoff tools</text>
              <text x="0" y="52" class="text-p">&bull; Control transferred via transfer_to_agent()</text>
              <text x="0" y="70" class="text-dim">&bull; 0 central supervisor latency bottleneck</text>
            </g>
          </g>
        </g>

        <!-- Quadrant 4: Hierarchical Teams -->
        <g transform="translate(630, 210)">
          <rect x="0" y="0" width="630" height="190" rx="8" class="node-box"/>
          <rect x="0" y="0" width="630" height="34" rx="8" fill="#1b2434"/>
          {render_icon("hierarchy", 12, 6, size=20, color="#e0c58e")}
          <text x="40" y="22" class="text-h2" fill="#e0c58e">PATTERN 4: HIERARCHICAL MULTI-TIER TEAMS</text>

          <g transform="translate(15, 45)">
            <!-- Mini Blueprint -->
            <rect x="80" y="0" width="100" height="24" rx="3" fill="#2d2516" stroke="#e0c58e"/>
            <text x="130" y="16" text-anchor="middle" class="text-mono-amber" font-size="8.5">Executive Lead</text>

            <path d="M 110 24 L 60 38" stroke="#e0c58e" stroke-width="1.2" fill="none"/>
            <path d="M 150 24 L 200 38" stroke="#e0c58e" stroke-width="1.2" fill="none"/>

            <rect x="15" y="38" width="90" height="22" rx="3" fill="#141c28" stroke="#253245"/>
            <text x="60" y="52" text-anchor="middle" class="text-mono" font-size="8">Lead: Backend</text>

            <rect x="155" y="38" width="90" height="22" rx="3" fill="#141c28" stroke="#253245"/>
            <text x="200" y="52" text-anchor="middle" class="text-mono" font-size="8">Lead: Frontend</text>

            <!-- Specs -->
            <g transform="translate(285, 0)">
              <text x="0" y="16" class="text-mono-amber" font-size="10">COORDINATION MODEL:</text>
              <text x="0" y="34" class="text-p">&bull; Multi-tier supervisory management</text>
              <text x="0" y="52" class="text-p">&bull; Mirrors enterprise organizational structure</text>
              <text x="0" y="70" class="text-dim">&bull; Scales to large software engineering systems</text>
            </g>
          </g>
        </g>
      </g>
    """)
}
