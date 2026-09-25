# Slide 15: Pattern 4: Hierarchical Agent Teams
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 15,
    "kicker": "TOPOLOGY PATTERNS",
    "title": "Pattern 4: Hierarchical Multi-Agent Teams",
    "lead": "Scaling agent systems to enterprise software engineering through multi-tier supervisory hierarchies.",
    "section": "Multi-Agent Topologies",
    "takeaway": "Hierarchy mirrors organizational structures: executives manage leads; leads manage specialized contributors.",
    "notes": {
        "goal": "Explain how complex, multi-functional enterprise workloads (e.g. building an entire feature) require multi-tier hierarchical delegation.",
        "talkTrack": "For complex software projects, a single supervisor cannot manage 10 different worker agents. The supervisor context fills up and delegation becomes unreliable. Pattern 4 applies Conway's Law to agent systems: we construct a multi-tier hierarchy. An Executive Product Manager agent delegates specifications to a Backend Lead and a QA Lead. Those leads supervise their own localized teams of database, API, and unit-test specialists.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("hierarchy", 15, 10, size=24, color="#e0c58e")}
        <text x="48" y="28" class="text-h1" fill="#e0c58e">Hierarchical Multi-Tier Agent Architecture</text>

        <g transform="translate(25, 55)">
          <!-- Top Tier: Executive Orchestrator -->
          <g transform="translate(415, 0)">
            <rect x="0" y="0" width="370" height="65" rx="6" class="node-box-active-amber"/>
            <text x="185" y="22" text-anchor="middle" class="text-mono-amber" font-size="11">TIER 1: EXECUTIVE PRODUCT MANAGER AGENT</text>
            <text x="185" y="42" text-anchor="middle" class="text-h2">Owns Feature Epic &amp; High-Level Deliverable Contract</text>
            <text x="185" y="58" text-anchor="middle" class="text-dim" font-size="9.5">Decomposes user requirement into Backend Spec + QA Test Matrix</text>
          </g>

          <!-- Branching Lines from Tier 1 to Tier 2 -->
          <path d="M 500 65 L 290 105" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>
          <path d="M 700 65 L 910 105" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Tier 2: Team Leads -->
          <!-- Lead 1: Backend -->
          <g transform="translate(100, 110)">
            <rect x="0" y="0" width="380" height="75" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="380" height="26" rx="6" fill="#1e2c42"/>
            <text x="190" y="18" text-anchor="middle" class="text-mono" font-size="11">TIER 2: BACKEND ARCHITECTURE LEAD</text>
            <text x="16" y="44" class="text-h2">Supervises Code Implementation Team</text>
            <text x="16" y="62" class="text-dim">Coordinates schema migrations, ORM entities, and REST handlers</text>
          </g>

          <!-- Lead 2: QA & Reliability -->
          <g transform="translate(720, 110)">
            <rect x="0" y="0" width="380" height="75" rx="6" class="node-box-active-purple"/>
            <rect x="0" y="0" width="380" height="26" rx="6" fill="#241b33"/>
            <text x="190" y="18" text-anchor="middle" class="text-mono-purple" font-size="11">TIER 2: QA &amp; RELIABILITY LEAD</text>
            <text x="16" y="44" class="text-h2">Supervises Verification &amp; Security Team</text>
            <text x="16" y="62" class="text-dim">Coordinates integration testing, load generation, and pentests</text>
          </g>

          <!-- Branching Lines from Tier 2 to Tier 3 -->
          <path d="M 200 185 L 110 220" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>
          <path d="M 380 185 L 470 220" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

          <path d="M 820 185 L 730 220" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>
          <path d="M 1000 185 L 1090 220" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>

          <!-- Tier 3: Specialized Workers -->
          <!-- Worker 1: Database Specialist -->
          <g transform="translate(0, 225)">
            <rect x="0" y="0" width="260" height="75" rx="5" class="node-box"/>
            <text x="12" y="20" class="text-mono" font-size="10">WORKER 1: DB SPECIALIST</text>
            <text x="12" y="40" class="text-p">Generates Alembic / SQL DDL</text>
            <text x="12" y="58" class="text-mono-green" font-size="9.5">Runs in Postgres Sandbox</text>
          </g>

          <!-- Worker 2: API Engineer -->
          <g transform="translate(290, 225)">
            <rect x="0" y="0" width="260" height="75" rx="5" class="node-box"/>
            <text x="12" y="20" class="text-mono" font-size="10">WORKER 2: FASTAPI ENGINEER</text>
            <text x="12" y="40" class="text-p">Generates route endpoints</text>
            <text x="12" y="58" class="text-mono-green" font-size="9.5">Validated against Pydantic</text>
          </g>

          <!-- Worker 3: Unit Test Agent -->
          <g transform="translate(650, 225)">
            <rect x="0" y="0" width="260" height="75" rx="5" class="node-box"/>
            <text x="12" y="20" class="text-mono-purple" font-size="10">WORKER 3: UNIT TEST AGENT</text>
            <text x="12" y="40" class="text-p">Generates pytest test suite</text>
            <text x="12" y="58" class="text-mono-purple" font-size="9.5">Target: 90% branch coverage</text>
          </g>

          <!-- Worker 4: Pentest Agent -->
          <g transform="translate(940, 225)">
            <rect x="0" y="0" width="260" height="75" rx="5" class="node-box"/>
            <text x="12" y="20" class="text-mono-purple" font-size="10">WORKER 4: PENTEST AGENT</text>
            <text x="12" y="40" class="text-p">Executes Bandit / Semgrep</text>
            <text x="12" y="58" class="text-mono-purple" font-size="9.5">OWASP Top 10 check: PASS</text>
          </g>

          <!-- Bottom Operational Note -->
          <g transform="translate(0, 312)">
            <rect x="0" y="0" width="1200" height="26" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="600" y="17" text-anchor="middle" class="text-mono-green" font-size="10">ISOLATION INVARIANT: Tier 3 workers only report upward to their Tier 2 lead. Cross-team communication occurs strictly via Tier 2 leads.</text>
          </g>
        </g>
      </g>
    """)
}
