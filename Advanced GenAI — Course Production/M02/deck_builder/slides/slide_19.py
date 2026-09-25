# Slide 19: Framework Landscape Overview - 4 Architectural Archetypes
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 19,
    "kicker": "FRAMEWORK LANDSCAPE",
    "title": "Enterprise Agent Frameworks: Four Architectural Archetypes",
    "lead": "Visualizing the underlying architectural engines: state graphs, event buses, group chat loops, and enterprise kernels.",
    "section": "Framework Landscape",
    "takeaway": "Choose the engine matching your problem: LangGraph for stateful loops, LlamaIndex for event RAG, AutoGen for chat, Semantic Kernel for .NET.",
    "notes": {
        "goal": "Provide an architectural blueprint comparison of the four primary agent design patterns and orchestration engines.",
        "talkTrack": "Rather than comparing marketing checklists, let us inspect the actual execution topology of each engine. LangGraph is a deterministic state machine with database checkpointing and cyclic transitions. LlamaIndex Workflows is an asynchronous event bus where steps fire on typed events. CrewAI and AutoGen implement group chat managers with conversational personas. And Semantic Kernel coordinates native enterprise code with prompt plugins through an automatic planner.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("network", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Four Distinct Orchestration Engines: Architectural Blueprints</text>

        <!-- 4 Architecture Columns -->
        <g transform="translate(15, 55)">
          
          <!-- Column 1: LangGraph (Cyclic State Machine) -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="295" height="330" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="295" height="36" rx="6" fill="#1e2c42"/>
            {render_logo_badge("langgraph", 8, 4, "LangGraph", 140, 28, color="#60a5fa")}
            <text x="285" y="22" text-anchor="end" class="text-mono" font-size="9" fill="#60a5fa">CYCLIC AUTOMATA</text>

            <!-- Mini Architectural Diagram -->
            <g transform="translate(10, 46)">
              <!-- Postgres Checkpointer -->
              <rect x="175" y="0" width="95" height="36" rx="4" fill="#132035" stroke="#3b82f6" stroke-width="1.2"/>
              <text x="222" y="16" text-anchor="middle" class="text-mono" font-size="8.5" fill="#60a5fa">PostgresSaver</text>
              <text x="222" y="28" text-anchor="middle" class="text-dim" font-size="7.5">Thread Checkpoints</text>

              <!-- State Object -->
              <rect x="5" y="0" width="150" height="36" rx="4" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5"/>
              <text x="80" y="16" text-anchor="middle" class="text-mono" font-size="9" fill="#93c5fd">State[TypedDict]</text>
              <text x="80" y="28" text-anchor="middle" class="text-dim" font-size="7.5">reducers: operator.add</text>

              <!-- Sync Arrow between State and Checkpointer -->
              <path d="M 155 18 L 175 18" stroke="#60a5fa" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

              <!-- Planning Node -->
              <rect x="15" y="52" width="110" height="34" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="70" y="68" text-anchor="middle" class="text-h2" font-size="9.5">Plan Node</text>
              <text x="70" y="80" text-anchor="middle" class="text-dim" font-size="7.5">LLM Reasoner</text>

              <path d="M 125 69 L 155 69" stroke="#60a5fa" stroke-width="1.2" fill="none" marker-end="url(#arr-blue)"/>

              <!-- Execution Node -->
              <rect x="155" y="52" width="110" height="34" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="210" y="68" text-anchor="middle" class="text-h2" font-size="9.5">Tool Exec</text>
              <text x="210" y="80" text-anchor="middle" class="text-dim" font-size="7.5">Sandbox Call</text>

              <!-- Conditional Edge Diamond -->
              <polygon points="140,102 180,120 140,138 100,120" fill="#1e293b" stroke="#e0c58e" stroke-width="1.2"/>
              <text x="140" y="123" text-anchor="middle" class="text-mono-amber" font-size="7.5">VALID?</text>

              <!-- Connections -->
              <path d="M 210 86 L 210 120 L 180 120" stroke="#60a5fa" stroke-width="1.2" fill="none"/>
              <path d="M 100 120 L 70 120 L 70 86" stroke="#6ee7b7" stroke-width="1.2" fill="none" marker-end="url(#arr-green)"/>
              <text x="75" y="113" class="text-mono-green" font-size="7.5">Retry Loop</text>

              <!-- Rewind Arrow -->
              <path d="M 240 86 Q 265 145 140 145" stroke="#d98585" stroke-width="1.2" stroke-dasharray="2 2" fill="none" marker-end="url(#arr-coral)"/>
              <text x="205" y="142" class="text-mono-coral" font-size="7">Rewind / Fork</text>

              <!-- Done Arrow -->
              <path d="M 140 138 L 140 162" stroke="#6ee7b7" stroke-width="1.2" fill="none" marker-end="url(#arr-green)"/>
              <rect x="110" y="162" width="60" height="20" rx="3" fill="#152420" stroke="#6ee7b7"/>
              <text x="140" y="175" text-anchor="middle" class="text-mono-green" font-size="8">END</text>
            </g>

            <!-- Bottom Specs -->
            <g transform="translate(10, 240)">
              <rect x="0" y="0" width="275" height="42" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="10" y="16" class="text-mono" font-size="8.5" fill="#60a5fa">CORE PRIMITIVE: State Graph</text>
              <text x="10" y="32" class="text-dim" font-size="8">Checkpoints, Time-Travel, HITL Gates</text>

              <rect x="0" y="47" width="275" height="34" rx="4" fill="#0f172a" stroke="#1e293b"/>
              <text x="10" y="62" class="text-mono-green" font-size="8">BEST FIT: High-Stakes Cyclic Workflows</text>
              <text x="10" y="74" class="text-dim" font-size="7.5">Enterprise finance, healthcare, legal audit</text>
            </g>
          </g>

          <!-- Column 2: LlamaIndex Workflows (Event-Driven Pipeline) -->
          <g transform="translate(310, 0)">
            <rect x="0" y="0" width="295" height="330" rx="6" class="node-box"/>
            <rect x="0" y="0" width="295" height="36" rx="6" fill="#1b2434"/>
            {render_logo_badge("llamaindex", 8, 4, "LlamaIndex", 140, 28, color="#f59e0b")}
            <text x="285" y="22" text-anchor="end" class="text-mono-amber" font-size="9">EVENT PUB/SUB</text>

            <!-- Mini Architectural Diagram -->
            <g transform="translate(10, 46)">
              <!-- Start / QueryEvent -->
              <rect x="20" y="0" width="110" height="26" rx="4" fill="#2d2516" stroke="#f59e0b" stroke-width="1.2"/>
              <text x="75" y="16" text-anchor="middle" class="text-mono-amber" font-size="8">QueryEvent (Start)</text>

              <path d="M 75 26 L 75 42" stroke="#f59e0b" stroke-width="1.2" fill="none" marker-end="url(#arr-amber)"/>

              <!-- Step 1: RetrieveDocs -->
              <rect x="15" y="42" width="120" height="34" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="75" y="58" text-anchor="middle" class="text-h2" font-size="9.5">Step 1: Retrieve</text>
              <text x="75" y="70" text-anchor="middle" class="text-dim" font-size="7.5">Vector Store Query</text>

              <!-- Emits ContextEvent -->
              <path d="M 135 59 L 165 59" stroke="#f59e0b" stroke-width="1.2" fill="none" marker-end="url(#arr-amber)"/>
              <rect x="165" y="46" width="105" height="26" rx="4" fill="#2d2516" stroke="#f59e0b" stroke-width="1"/>
              <text x="217" y="62" text-anchor="middle" class="text-mono-amber" font-size="8">ContextEvent</text>

              <path d="M 217 72 L 217 96" stroke="#f59e0b" stroke-width="1.2" fill="none" marker-end="url(#arr-amber)"/>

              <!-- Step 2: RerankDocs -->
              <rect x="155" y="96" width="125" height="34" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="217" y="112" text-anchor="middle" class="text-h2" font-size="9.5">Step 2: Rerank</text>
              <text x="217" y="124" text-anchor="middle" class="text-dim" font-size="7.5">Cross-Encoder Filter</text>

              <!-- Emits StopEvent -->
              <path d="M 155 113 L 115 113 L 115 145" stroke="#6ee7b7" stroke-width="1.2" fill="none" marker-end="url(#arr-green)"/>
              <rect x="60" y="145" width="110" height="26" rx="4" fill="#152420" stroke="#6ee7b7" stroke-width="1.2"/>
              <text x="115" y="161" text-anchor="middle" class="text-mono-green" font-size="8">StopEvent (Synthesized)</text>

              <path d="M 170 158 L 205 158" stroke="#6ee7b7" stroke-width="1.2" fill="none" marker-end="url(#arr-green)"/>
              <rect x="205" y="148" width="65" height="20" rx="3" fill="#141c28" stroke="#253245"/>
              <text x="237" y="161" text-anchor="middle" class="text-p" font-size="7.5">Output</text>
            </g>

            <!-- Bottom Specs -->
            <g transform="translate(10, 240)">
              <rect x="0" y="0" width="275" height="42" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="10" y="16" class="text-mono-amber" font-size="8.5">CORE PRIMITIVE: Event Pub/Sub</text>
              <text x="10" y="32" class="text-dim" font-size="8">Asyncio Queue, Decoupled Steps</text>

              <rect x="0" y="47" width="275" height="34" rx="4" fill="#0f172a" stroke="#1e293b"/>
              <text x="10" y="62" class="text-mono-green" font-size="8">BEST FIT: Advanced RAG Pipelines</text>
              <text x="10" y="74" class="text-dim" font-size="7.5">Knowledge graphs, doc parsers, ETL</text>
            </g>
          </g>

          <!-- Column 3: AutoGen & CrewAI (Multi-Agent Group Chat) -->
          <g transform="translate(620, 0)">
            <rect x="0" y="0" width="295" height="330" rx="6" class="node-box"/>
            <rect x="0" y="0" width="295" height="36" rx="6" fill="#1b2434"/>
            {render_logo_badge("autogen", 8, 4, "AutoGen / CrewAI", 160, 28, color="#10b981")}
            <text x="285" y="22" text-anchor="end" class="text-mono-green" font-size="9">GROUP CHAT</text>

            <!-- Mini Architectural Diagram -->
            <g transform="translate(10, 46)">
              <!-- Group Chat Manager -->
              <rect x="50" y="0" width="175" height="32" rx="4" fill="#152420" stroke="#10b981" stroke-width="1.2"/>
              <text x="137" y="15" text-anchor="middle" class="text-mono-green" font-size="8.5">Group Chat Manager</text>
              <text x="137" y="26" text-anchor="middle" class="text-dim" font-size="7.5">Speaker Selection / Handoff</text>

              <!-- 3 Agents -->
              <g transform="translate(5, 50)">
                <!-- Researcher -->
                <rect x="0" y="0" width="80" height="42" rx="4" fill="#141c28" stroke="#253245"/>
                <text x="40" y="16" text-anchor="middle" class="text-mono-green" font-size="8">Researcher</text>
                <text x="40" y="28" text-anchor="middle" class="text-dim" font-size="7">Search Tool</text>

                <!-- Coder -->
                <rect x="95" y="0" width="75" height="42" rx="4" fill="#141c28" stroke="#253245"/>
                <text x="132" y="16" text-anchor="middle" class="text-mono-green" font-size="8">Coder</text>
                <text x="132" y="28" text-anchor="middle" class="text-dim" font-size="7">Docker Sandbox</text>

                <!-- Reviewer -->
                <rect x="185" y="0" width="80" height="42" rx="4" fill="#141c28" stroke="#253245"/>
                <text x="225" y="16" text-anchor="middle" class="text-mono-green" font-size="8">QA Critic</text>
                <text x="225" y="28" text-anchor="middle" class="text-dim" font-size="7">Syntax Linter</text>

                <!-- Communication Lines -->
                <path d="M 80 21 L 95 21" stroke="#10b981" stroke-width="1" fill="none"/>
                <path d="M 170 21 L 185 21" stroke="#10b981" stroke-width="1" fill="none"/>
              </g>

              <!-- Connection to Manager -->
              <path d="M 137 32 L 137 50" stroke="#10b981" stroke-width="1.2" fill="none" marker-end="url(#arr-green)"/>

              <!-- Shared Chat History Bus -->
              <rect x="15" y="112" width="245" height="34" rx="4" fill="#121824" stroke="#253245"/>
              <text x="137" y="127" text-anchor="middle" class="text-mono" font-size="8.5" fill="#94a3b8">Shared Conversation History</text>
              <text x="137" y="139" text-anchor="middle" class="text-dim" font-size="7.5">Broadcast Message Passing</text>

              <path d="M 45 92 L 45 112" stroke="#64748b" stroke-width="1" fill="none"/>
              <path d="M 137 92 L 137 112" stroke="#64748b" stroke-width="1" fill="none"/>
              <path d="M 225 92 L 225 112" stroke="#64748b" stroke-width="1" fill="none"/>

              <!-- Feedback Arrow -->
              <path d="M 260 129 Q 280 60 225 16" stroke="#10b981" stroke-width="1" stroke-dasharray="2 2" fill="none" marker-end="url(#arr-green)"/>
            </g>

            <!-- Bottom Specs -->
            <g transform="translate(10, 240)">
              <rect x="0" y="0" width="275" height="42" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="10" y="16" class="text-mono-green" font-size="8.5">CORE PRIMITIVE: Conversational Personas</text>
              <text x="10" y="32" class="text-dim" font-size="8">Backstories, Tasks, Peer Message Exchange</text>

              <rect x="0" y="47" width="275" height="34" rx="4" fill="#0f172a" stroke="#1e293b"/>
              <text x="10" y="62" class="text-mono-green" font-size="8">BEST FIT: Simulation &amp; Fast PoCs</text>
              <text x="10" y="74" class="text-dim" font-size="7.5">Role-play benchmarks, rapid ideation</text>
            </g>
          </g>

          <!-- Column 4: Semantic Kernel (Enterprise Core & Plugins) -->
          <g transform="translate(930, 0)">
            <rect x="0" y="0" width="295" height="330" rx="6" class="node-box"/>
            <rect x="0" y="0" width="295" height="36" rx="6" fill="#1b2434"/>
            {render_logo_badge("semantic_kernel", 8, 4, "Semantic Kernel", 160, 28, color="#c084fc")}
            <text x="285" y="22" text-anchor="end" class="text-mono-purple" font-size="9">ENTERPRISE SDK</text>

            <!-- Mini Architectural Diagram -->
            <g transform="translate(10, 46)">
              <!-- Enterprise App -->
              <rect x="40" y="0" width="195" height="24" rx="3" fill="#1e182e" stroke="#c084fc" stroke-width="1"/>
              <text x="137" y="15" text-anchor="middle" class="text-mono-purple" font-size="8">Enterprise App (.NET / Python)</text>

              <path d="M 137 24 L 137 38" stroke="#c084fc" stroke-width="1.2" fill="none" marker-end="url(#arr-purple)"/>

              <!-- Central Kernel Container -->
              <rect x="15" y="38" width="245" height="74" rx="4" fill="#161224" stroke="#7e22ce" stroke-width="1.2"/>
              <text x="25" y="52" class="text-mono-purple" font-size="8">SEMANTIC KERNEL CORE</text>

              <!-- Semantic & Native Plugins -->
              <rect x="25" y="58" width="105" height="24" rx="3" fill="#241a38" stroke="#a855f7"/>
              <text x="77" y="73" text-anchor="middle" class="text-p" font-size="7.5">Semantic (Prompt)</text>

              <rect x="140" y="58" width="110" height="24" rx="3" fill="#241a38" stroke="#a855f7"/>
              <text x="195" y="73" text-anchor="middle" class="text-p" font-size="7.5">Native (C# / Code)</text>

              <!-- Planner -->
              <rect x="55" y="86" width="165" height="20" rx="3" fill="#2e1065" stroke="#c084fc"/>
              <text x="137" y="99" text-anchor="middle" class="text-mono-purple" font-size="8">Automatic Planner</text>

              <!-- Connectors to Azure & Enterprise -->
              <path d="M 85 112 L 85 135" stroke="#c084fc" stroke-width="1.2" fill="none" marker-end="url(#arr-purple)"/>
              <path d="M 190 112 L 190 135" stroke="#c084fc" stroke-width="1.2" fill="none" marker-end="url(#arr-purple)"/>

              <rect x="25" y="135" width="110" height="26" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="80" y="151" text-anchor="middle" class="text-mono" font-size="7.5">Azure OpenAI</text>

              <rect x="145" y="135" width="110" height="26" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="200" y="151" text-anchor="middle" class="text-mono" font-size="7.5">SAP / Office 365</text>
            </g>

            <!-- Bottom Specs -->
            <g transform="translate(10, 240)">
              <rect x="0" y="0" width="275" height="42" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="10" y="16" class="text-mono-purple" font-size="8.5">CORE PRIMITIVE: Kernel + Plugins</text>
              <text x="10" y="32" class="text-dim" font-size="8">Type-Safe Connectors, Memory Stores</text>

              <rect x="0" y="47" width="275" height="34" rx="4" fill="#0f172a" stroke="#1e293b"/>
              <text x="10" y="62" class="text-mono-green" font-size="8">BEST FIT: Microsoft Enterprise Stacks</text>
              <text x="10" y="74" class="text-dim" font-size="7.5">C#/.NET enterprise solutions, Azure clouds</text>
            </g>
          </g>

        </g>
      </g>
    """)
}
