# Slide 04: The Core Orchestrator Abstraction
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 4,
    "kicker": "ORCHESTRATOR ANATOMY",
    "title": "The Four Primitives of Graph-Based Orchestration",
    "lead": "Abstracting agent execution into State, Nodes, Conditional Edges, and Checkpointers.",
    "section": "Core Abstractions",
    "takeaway": "Decoupling node computation from edge routing transforms agents from black boxes into verifiable state automata.",
    "notes": {
        "goal": "Deconstruct modern agent runtimes (such as LangGraph) into four core computer science primitives.",
        "talkTrack": "To engineer reliable agents, we must discard fuzzy anthropomorphic terms like 'agent memory' or 'agent thoughts' and use systems engineering primitives. A graph orchestrator consists of four elements: State is the typed schema holding variables. Nodes are functions that execute business logic or call models. Conditional Edges are deterministic routing functions that inspect state and choose the next node. And Checkpointers write state snapshots to persistent storage at every super-step.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Container Box -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("state_machine", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Formal State Automaton Anatomy (The 4 Primitives)</text>

        <!-- Top Row: State Schema Banner -->
        <g transform="translate(25, 58)">
          <rect x="0" y="0" width="1210" height="65" rx="6" fill="#141c28" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="16" y="22" class="text-mono" font-size="11">PRIMITIVE 1: CENTRALIZED STATE SCHEMA (Typed Channels)</text>
          <text x="16" y="44" class="text-p">class AgentState(TypedDict): messages: Annotated[list[BaseMessage], add_messages], context: dict, retry_count: int</text>
          <rect x="1050" y="16" width="140" height="32" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
          <text x="1120" y="37" text-anchor="middle" class="text-mono" font-size="11">Immutable Delta</text>
        </g>

        <!-- Middle Row: Nodes and Edges Flow -->
        <g transform="translate(25, 140)">
          <!-- Node A: Planner -->
          <rect x="0" y="10" width="220" height="95" rx="6" class="node-box-active"/>
          <rect x="0" y="10" width="220" height="26" rx="6" fill="#1e2c42"/>
          <text x="110" y="28" text-anchor="middle" class="text-mono" font-size="11">PRIMITIVE 2: NODE A</text>
          <text x="16" y="56" class="text-h2">Model Reasoning</text>
          <text x="16" y="74" class="text-dim">fn(state) -&gt; {{'messages': [AIMsg]}}</text>
          <text x="16" y="92" class="text-mono-green" font-size="10.5">Executes pure LLM call</text>

          <!-- Edge 1 -->
          <path d="M 220 57 L 290 57" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>
          <rect x="228" y="38" width="55" height="18" rx="3" fill="#111824"/>
          <text x="255" y="51" text-anchor="middle" class="text-dim" font-size="9.5">delta</text>

          <!-- Node B: Tool -->
          <rect x="300" y="10" width="220" height="95" rx="6" class="node-box-active-green"/>
          <rect x="0" y="10" width="220" height="26" rx="6" fill="#152420" transform="translate(300, 0)"/>
          <text x="410" y="28" text-anchor="middle" class="text-mono-green" font-size="11">PRIMITIVE 2: NODE B</text>
          <text x="316" y="56" class="text-h2">Tool Sandbox</text>
          <text x="316" y="74" class="text-dim">fn(state) -&gt; {{'messages': [ToolMsg]}}</text>
          <text x="316" y="92" class="text-mono-green" font-size="10.5">Executes sandbox action</text>

          <!-- Conditional Edge Primitive 3 -->
          <path d="M 520 57 L 600 57" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>

          <g transform="translate(610, 0)">
            <polygon points="90,10 180,57 90,105 0,57" fill="#1e2433" stroke="#e0c58e" stroke-width="1.8"/>
            <text x="90" y="48" text-anchor="middle" class="text-mono-amber" font-size="10">PRIMITIVE 3</text>
            <text x="90" y="65" text-anchor="middle" class="text-h2" fill="#ffffff" font-size="11">Conditional Edge</text>
            <text x="90" y="80" text-anchor="middle" class="text-dim" font-size="9.5">route(state) -&gt; str</text>
          </g>

          <!-- Edge Branch: Continue / Cycle -->
          <path d="M 700 10 Q 700 -20 110 -20 L 110 5" stroke="#e0c58e" stroke-width="2" stroke-dasharray="4 3" fill="none" marker-end="url(#arr-amber)"/>
          <rect x="360" y="-32" width="160" height="22" rx="4" fill="#1b2434" stroke="#e0c58e" stroke-width="1"/>
          <text x="440" y="-17" text-anchor="middle" class="text-mono-amber" font-size="10">route == 'retry' (cycle back)</text>

          <!-- Edge Branch: Finalize -->
          <path d="M 790 57 L 870 57" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>
          
          <rect x="880" y="10" width="330" height="95" rx="6" class="node-box-active-purple"/>
          <rect x="880" y="10" width="330" height="26" rx="6" fill="#241b33"/>
          <text x="1045" y="28" text-anchor="middle" class="text-mono-purple" font-size="11">PRIMITIVE 2: NODE C (END)</text>
          <text x="896" y="56" class="text-h2">Synthesizer &amp; Final Delivery</text>
          <text x="896" y="74" class="text-dim">Transforms state array into structured JSON client response</text>
          <text x="896" y="92" class="text-mono-green" font-size="10.5">Terminal state reached</text>
        </g>

        <!-- Bottom Row: Primitive 4 Checkpointer Bus -->
        <g transform="translate(25, 270)">
          <rect x="0" y="0" width="1210" height="105" rx="6" fill="#111824" stroke="#e0c58e" stroke-width="1.2"/>
          {render_zone_badge("PRIMITIVE 4: PERSISTENT CHECKPOINTER BUS", 15, 12, 280, 24, "#e0c58e")}
          
          <g transform="translate(15, 48)">
            <text x="0" y="16" class="text-mono" font-size="11" fill="#cbd5e1">SUPER-STEP SNAPSHOTTING:</text>
            <text x="0" y="36" class="text-p">After every Node execution, the orchestrator intercepts the updated state delta.</text>
            <text x="0" y="54" class="text-dim">It serializes the full state checkpoint into Postgres/Redis before yielding to the next node.</text>
          </g>

          <g transform="translate(680, 48)">
            <text x="0" y="16" class="text-mono-green" font-size="11">ENTERPRISE CAPABILITIES UNLOCKED:</text>
            <text x="0" y="36" class="text-p">&bull; Time-travel debugging (rewind state to step N)</text>
            <text x="0" y="54" class="text-p">&bull; Multi-turn thread resumption &amp; Human-in-the-loop approvals</text>
          </g>
        </g>
      </g>
    """)
}
