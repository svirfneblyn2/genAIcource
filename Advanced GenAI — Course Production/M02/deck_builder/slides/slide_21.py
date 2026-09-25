# Slide 21: Framework Deep-Dive
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 21,
    "kicker": "DECISION LOGIC",
    "title": "Architectural Selection Tree: Framework Choice",
    "lead": "Guiding enterprise architecture teams to the defensible framework based on workflow constraints.",
    "section": "Framework Landscape",
    "takeaway": "Choose based on operational boundaries: event-driven data apps fit LlamaIndex; cyclic multi-step workflows fit LangGraph.",
    "notes": {
        "goal": "Provide a deterministic decision tree for architecture review boards selecting an agent orchestration runtime.",
        "talkTrack": "When presenting to an Architecture Review Board, you must defend your framework selection with hard technical criteria. Do not say 'we like LangGraph because it is popular'. You say: 'We selected LangGraph because our accounts payable workload requires cyclic retry loops, sub-step time travel debugging, and an ACID-compliant Postgres checkpointer. We rejected CrewAI because it lacks fine-grained checkpointer threads, and we rejected Semantic Kernel because our platform engineering team standardizes on Python.'",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("branch", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Enterprise Architecture Selection Tree</text>

        <!-- Decision Tree Layout -->
        <g transform="translate(30, 65)">
          <!-- Question 1 -->
          <g transform="translate(0, 70)">
            <polygon points="120,0 240,40 120,80 0,40" fill="#172233" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="120" y="36" text-anchor="middle" class="text-mono" font-size="10.5">CYCLIC LOOPS &amp;</text>
            <text x="120" y="52" text-anchor="middle" class="text-mono-green" font-size="10">PERSISTENCE NEEDED?</text>
          </g>

          <!-- YES Branch -> Question 2 -->
          <path d="M 240 110 L 330 60" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>
          <text x="270" y="75" class="text-mono-green" font-size="10.5">YES</text>

          <g transform="translate(340, 20)">
            <polygon points="120,0 240,40 120,80 0,40" fill="#172233" stroke="#e0c58e" stroke-width="1.8"/>
            <text x="120" y="36" text-anchor="middle" class="text-mono" font-size="10.5">PRIMARY ENTERPRISE</text>
            <text x="120" y="52" text-anchor="middle" class="text-mono-amber" font-size="10">TECH STACK?</text>
          </g>

          <!-- Branch 2A: Python / TS -> LangGraph -->
          <path d="M 580 45 L 670 25" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>
          <text x="600" y="25" class="text-mono" font-size="9.5">Python / TS</text>

          <g transform="translate(680, 0)">
            <rect x="0" y="0" width="530" height="65" rx="6" class="node-box-active"/>
            <text x="16" y="24" class="text-h2" fill="#60a5fa">SELECT: LANGGRAPH (RECOMMENDED)</text>
            <text x="16" y="44" class="text-p">Full cyclic state graphs &bull; Postgres/Redis checkpointer &bull; Time-travel debugging &bull; LangSmith</text>
          </g>

          <!-- Branch 2B: C# / .NET -> Semantic Kernel -->
          <path d="M 580 75 L 670 95" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>
          <text x="600" y="100" class="text-mono" font-size="9.5">C# / Azure</text>

          <g transform="translate(680, 75)">
            <rect x="0" y="0" width="530" height="65" rx="6" class="node-box-active-purple"/>
            <text x="16" y="24" class="text-h2" fill="#b4a4e5">SELECT: SEMANTIC KERNEL</text>
            <text x="16" y="44" class="text-p">Deep Microsoft .NET alignment &bull; Azure OpenAI native &bull; Strong typing &bull; Copilot integration</text>
          </g>

          <!-- NO Branch -> Question 3 -->
          <path d="M 240 110 L 330 170" stroke="#d98585" stroke-width="2" fill="none" marker-end="url(#arr-coral)"/>
          <text x="270" y="155" class="text-mono-coral" font-size="10.5">NO</text>

          <g transform="translate(340, 140)">
            <polygon points="120,0 240,40 120,80 0,40" fill="#172233" stroke="#e0c58e" stroke-width="1.8"/>
            <text x="120" y="36" text-anchor="middle" class="text-mono" font-size="10">UNSTRUCTURED RAG</text>
            <text x="120" y="52" text-anchor="middle" class="text-mono-amber" font-size="10">&amp; DOCUMENT ETL?</text>
          </g>

          <!-- Branch 3A: YES -> LlamaIndex -->
          <path d="M 580 165 L 670 165" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>
          <text x="610" y="155" class="text-mono-amber" font-size="10">YES</text>

          <g transform="translate(680, 145)">
            <rect x="0" y="0" width="530" height="65" rx="6" class="node-box-active-amber"/>
            <text x="16" y="24" class="text-h2" fill="#e0c58e">SELECT: LLAMAININDEX WORKFLOWS</text>
            <text x="16" y="44" class="text-p">Event-driven steps &bull; Deep embedding &amp; hybrid search &bull; LlamaParse document extraction</text>
          </g>

          <!-- Branch 3B: NO -> Rapid PoC / Research -->
          <path d="M 580 195 L 670 235" stroke="#d98585" stroke-width="2" fill="none" marker-end="url(#arr-coral)"/>
          <text x="610" y="225" class="text-mono-coral" font-size="10">NO</text>

          <g transform="translate(680, 220)">
            <rect x="0" y="0" width="530" height="75" rx="6" class="node-box"/>
            <text x="16" y="24" class="text-h2" fill="#d98585">SELECT: CREWAI / AUTOGEN (PROTOTYPING ONLY)</text>
            <text x="16" y="44" class="text-p">Role-playing personas (CrewAI) or multi-agent chat research (AutoGen).</text>
            <text x="16" y="62" class="text-mono-coral" font-size="9.5">Caveat: Avoid in mission-critical transactional banking workloads due to weak checkpointers.</text>
          </g>
        </g>
      </g>
    """)
}
