# Slide 01: Course Title & Architectural Roadmap
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 1,
    "kicker": "ADVANCED GENAI | MODULE 02: AGENT FRAMEWORKS & ORCHESTRATION",
    "title": "State Machines, Multi-Agent Topologies, and Production Reliability",
    "lead": "Engineering resilient, cyclic, and observable agent runtimes with state persistence and human oversight.",
    "section": "Course Roadmap",
    "takeaway": "Production agents are deterministic state machines governing stochastic model outputs, not free-form prompt loops.",
    "notes": {
        "goal": "Establish the foundational thesis of Module 02: moving beyond fragile chains to deterministic, observable state machine graphs.",
        "talkTrack": "Welcome to Module 02. In Module 01 we evaluated cloud platforms. Today we confront the engineering reality of agent orchestration. A prompt loop is not an architecture. When model calls fail, tools timeout, or context windows overflow, you need a deterministic state machine. We will dismantle the illusion of magic agents and build production systems with explicit state channels, checkpointing, and human gates.",
        "timing": "3 minutes"
    },
    "svg": svg_frame(f"""
      <!-- Pipeline stages -->
      <g transform="translate(40, 35)">
        <!-- Stage 1 -->
        <rect x="0" y="0" width="230" height="230" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="230" height="38" rx="8" fill="#1e2c42"/>
        <text x="115" y="24" text-anchor="middle" class="text-h1" fill="#60a5fa">1. State &amp; Reducers</text>
        {render_icon("state_machine", 20, 52, size=24, color="#60a5fa")}
        <text x="54" y="69" class="text-h2">Deterministic Core</text>
        <text x="20" y="102" class="text-p">&bull; TypedDict &amp; Pydantic state</text>
        <text x="20" y="125" class="text-p">&bull; Append-only message reducers</text>
        <text x="20" y="148" class="text-p">&bull; Memory, Postgres, Redis savers</text>
        <rect x="18" y="172" width="194" height="36" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="115" y="194" text-anchor="middle" class="text-mono" font-size="11">Time-Travel Checkpointing</text>
      </g>

      <path d="M 280 150 L 315 150" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

      <!-- Stage 2 -->
      <g transform="translate(325, 35)">
        <rect x="0" y="0" width="230" height="230" rx="8" class="node-box"/>
        <rect x="0" y="0" width="230" height="38" rx="8" fill="#1b2434"/>
        <text x="115" y="24" text-anchor="middle" class="text-h1" fill="#6ee7b7">2. Tool Sandboxing</text>
        {render_icon("tool", 20, 52, size=24, color="#6ee7b7")}
        <text x="54" y="69" class="text-h2">Execution Isolation</text>
        <text x="20" y="102" class="text-p">&bull; Function calling schemas</text>
        <text x="20" y="125" class="text-p">&bull; E2B microVMs &amp; Docker sandboxes</text>
        <text x="20" y="148" class="text-p">&bull; 4-tier error reflection &amp; retries</text>
        <rect x="18" y="172" width="194" height="36" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="115" y="194" text-anchor="middle" class="text-mono-green" font-size="11">Host Process Defense</text>
      </g>

      <path d="M 565 150 L 600 150" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

      <!-- Stage 3 -->
      <g transform="translate(610, 35)">
        <rect x="0" y="0" width="230" height="230" rx="8" class="node-box"/>
        <rect x="0" y="0" width="230" height="38" rx="8" fill="#1b2434"/>
        <text x="115" y="24" text-anchor="middle" class="text-h1" fill="#b4a4e5">3. Multi-Agent Topologies</text>
        {render_icon("supervisor", 20, 52, size=24, color="#b4a4e5")}
        <text x="54" y="69" class="text-h2">Context Boundaries</text>
        <text x="20" y="102" class="text-p">&bull; Routers, Supervisors, Swarms</text>
        <text x="20" y="125" class="text-p">&bull; Ephemeral child threads</text>
        <text x="20" y="148" class="text-p">&bull; Token blowup prevention</text>
        <rect x="18" y="172" width="194" height="36" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="115" y="194" text-anchor="middle" class="text-mono-purple" font-size="11">Decoupled Sub-Graphs</text>
      </g>

      <path d="M 850 150 L 885 150" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>

      <!-- Stage 4 -->
      <g transform="translate(895, 35)">
        <rect x="0" y="0" width="230" height="230" rx="8" class="node-box-active" stroke="#e0c58e"/>
        <rect x="0" y="0" width="230" height="38" rx="8" fill="#2d2516"/>
        <text x="115" y="24" text-anchor="middle" class="text-h1" fill="#e0c58e">4. HITL &amp; Production SLAs</text>
        {render_icon("approval", 20, 52, size=24, color="#e0c58e")}
        <text x="54" y="69" class="text-h2">Production Governance</text>
        <text x="20" y="102" class="text-p">&bull; Interrupt before side-effects</text>
        <text x="20" y="125" class="text-p">&bull; State mutation on resume</text>
        <text x="20" y="148" class="text-p">&bull; OTel distributed tracing</text>
        <rect x="18" y="172" width="194" height="36" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="115" y="194" text-anchor="middle" class="text-mono-amber" font-size="11">Zero-Leak Guardrails</text>
      </g>

      <!-- Bottom Platform Ecosystem Strip -->
      <g transform="translate(40, 290)">
        <rect x="0" y="0" width="1085" height="135" rx="8" class="swimlane-bg"/>
        {render_zone_badge("ORCHESTRATION ECOSYSTEM", 15, 12, 195, 24, "#60a5fa")}
        
        <g transform="translate(15, 45)">
          {render_logo_badge("langgraph", 0, 0, "LangGraph", 155, 34, color="#60a5fa")}
          {render_logo_badge("llamaindex", 170, 0, "LlamaIndex Workflows", 195, 34, color="#e0c58e")}
          {render_logo_badge("autogen", 380, 0, "AutoGen (MSFT)", 165, 34, color="#6ee7b7")}
          {render_logo_badge("crewai", 560, 0, "CrewAI", 135, 34, color="#d98585")}
          {render_logo_badge("semantic_kernel", 710, 0, "Semantic Kernel", 175, 34, color="#b4a4e5")}
          {render_logo_badge("openai", 900, 0, "OpenAI Swarm", 155, 34, color="#cbd5e1")}
        </g>
        
        <g transform="translate(15, 90)">
          <text x="5" y="24" class="text-mono" font-size="11" fill="#64748b">SUPPORTING INFRASTRUCTURE:</text>
          {render_logo_badge("postgres", 220, 5, "PostgreSQL (pgvector)", 195, 28, color="#60a5fa")}
          {render_logo_badge("redis", 430, 5, "Redis Checkpointer", 165, 28, color="#d98585")}
          {render_logo_badge("docker", 610, 5, "Docker / E2B Sandbox", 185, 28, color="#6ee7b7")}
          {render_logo_badge("opentelemetry", 810, 5, "OpenTelemetry / LangSmith", 215, 28, color="#e0c58e")}
        </g>
      </g>
    """)
}
