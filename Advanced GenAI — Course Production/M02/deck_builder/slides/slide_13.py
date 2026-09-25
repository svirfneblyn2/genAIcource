# Slide 13: Pattern 2: Supervisor & Sub-Agents
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 13,
    "kicker": "TOPOLOGY PATTERNS",
    "title": "Pattern 2: Supervisor & Sub-Agents Architecture",
    "lead": "A centralized supervisor maintains master state, delegating specialized subtasks to child worker agents.",
    "section": "Multi-Agent Topologies",
    "takeaway": "Supervisors prevent context poisoning by running child agents in ephemeral, isolated scratchpad threads.",
    "notes": {
        "goal": "Examine how the Supervisor pattern decouples complex multi-step reasoning while keeping the primary context window lean.",
        "talkTrack": "When a task requires multiple distinct skills (researching documentation, writing code, and running tests), a single agent will pollute its prompt with hundreds of lines of intermediate compiler outputs and API responses. In the Supervisor pattern, the lead agent acts as an engineering manager. It creates ephemeral child threads for workers. The workers execute in isolation and report back only their summarized conclusion.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active-purple"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#241b33"/>
        {render_icon("supervisor", 15, 10, size=24, color="#b4a4e5")}
        <text x="48" y="28" class="text-h1" fill="#b4a4e5">Supervisor &amp; Child Workers: Ephemeral Scratchpads &amp; Context Isolation</text>

        <!-- Master Supervisor Zone -->
        <g transform="translate(25, 60)">
          <!-- Supervisor Core -->
          <g transform="translate(0, 40)">
            <rect x="0" y="0" width="310" height="190" rx="6" class="node-box-active-purple"/>
            <rect x="0" y="0" width="310" height="32" rx="6" fill="#2d1e44"/>
            <text x="155" y="22" text-anchor="middle" class="text-mono-purple" font-size="11">SUPERVISOR (MASTER ORCHESTRATOR)</text>

            <g transform="translate(16, 44)">
              <text x="0" y="16" class="text-h2">Responsibilities:</text>
              <text x="0" y="36" class="text-p">&bull; Owns the global task decomposition plan</text>
              <text x="0" y="56" class="text-p">&bull; Delegates subtasks via conditional edges</text>
              <text x="0" y="76" class="text-p">&bull; Aggregates worker returns into final deliverable</text>

              <rect x="0" y="94" width="278" height="40" rx="4" fill="#141c28" stroke="#3b82f6"/>
              <text x="14" y="112" class="text-mono" font-size="9.5" fill="#60a5fa">Current Plan Step: 2 of 3</text>
              <text x="14" y="126" class="text-dim" font-size="8.5">Delegate: Coder Agent (Clean Context)</text>
            </g>
          </g>

          <!-- Delegation & Return Connectors -->
          <!-- To Researcher -->
          <path d="M 310 75 L 430 35" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>
          <path d="M 430 48 L 310 88" stroke="#6ee7b7" stroke-width="1.8" stroke-dasharray="3 3" fill="none"/>

          <!-- To Coder -->
          <path d="M 310 135 L 430 135" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>
          <path d="M 430 148 L 310 148" stroke="#6ee7b7" stroke-width="1.8" stroke-dasharray="3 3" fill="none"/>

          <!-- To Reviewer -->
          <path d="M 310 195 L 430 235" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>
          <path d="M 430 248 L 310 208" stroke="#6ee7b7" stroke-width="1.8" stroke-dasharray="3 3" fill="none"/>

          <!-- 3 Child Worker Agents -->
          <!-- Worker 1: Researcher -->
          <g transform="translate(440, 0)">
            <rect x="0" y="0" width="460" height="75" rx="6" class="node-box"/>
            <text x="16" y="22" class="text-mono" font-size="10.5" fill="#60a5fa">EPHEMERAL CHILD THREAD 1: RESEARCHER AGENT</text>
            <text x="16" y="44" class="text-p">Executes 4 internal tool calls (Vector RAG, Web Search, PDF parser)</text>
            <text x="16" y="62" class="text-mono-green" font-size="10">Returns to Supervisor: 1 paragraph synthesis (180 tokens)</text>
          </g>

          <!-- Worker 2: Coder -->
          <g transform="translate(440, 100)">
            <rect x="0" y="0" width="460" height="75" rx="6" class="node-box-active-green"/>
            <text x="16" y="22" class="text-mono-green" font-size="10.5">EPHEMERAL CHILD THREAD 2: CODER AGENT</text>
            <text x="16" y="44" class="text-p">Generates code in isolated E2B sandbox, runs pytest 3 times</text>
            <text x="16" y="62" class="text-mono-green" font-size="10">Returns to Supervisor: Final verified Python file (420 tokens)</text>
          </g>

          <!-- Worker 3: Reviewer -->
          <g transform="translate(440, 200)">
            <rect x="0" y="0" width="460" height="75" rx="6" class="node-box"/>
            <text x="16" y="22" class="text-mono-amber" font-size="10.5">EPHEMERAL CHILD THREAD 3: SECURITY REVIEWER</text>
            <text x="16" y="44" class="text-p">Audits code for SQL injection, hardcoded secrets, and buffer limits</text>
            <text x="16" y="62" class="text-mono-green" font-size="10">Returns to Supervisor: Audit approval token: PASS (45 tokens)</text>
          </g>

          <!-- Right Side: Token Isolation Audit -->
          <g transform="translate(930, 20)">
            <rect x="0" y="0" width="280" height="235" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="14" y="24" class="text-mono-green" font-size="11">CONTEXT PROTECTION AUDIT</text>
            
            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-mono-coral" font-size="10">WITHOUT SUPERVISOR:</text>
              <text x="0" y="32" class="text-p">45,000 tokens accumulated</text>
              <text x="0" y="48" class="text-dim">(raw bash, pytest, vector chunks)</text>
              
              <text x="0" y="80" class="text-mono-green" font-size="10">WITH SUPERVISOR:</text>
              <text x="0" y="96" class="text-p">Master state: 2,400 tokens</text>
              <text x="0" y="112" class="text-dim">Child threads destroyed upon exit</text>
              
              <rect x="0" y="130" width="250" height="42" rx="4" fill="#152420" stroke="#6ee7b7"/>
              <text x="125" y="156" text-anchor="middle" class="text-mono-green" font-size="11">94.6% Token Reduction</text>
            </g>
          </g>
        </g>

        <!-- Bottom Takeaway -->
        <g transform="translate(25, 330)">
          <rect x="0" y="0" width="1210" height="50" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="22" class="text-mono-purple" font-size="11">ARCHITECTURAL RULE:</text>
          <text x="16" y="38" class="text-p">Child agents must never communicate directly. All state transitions, approvals, and error recoveries flow through the central Supervisor.</text>
        </g>
      </g>
    """)
}
