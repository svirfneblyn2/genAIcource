# Slide 02: The Failure of Linear DAGs
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 2,
    "kicker": "FOUNDATIONS: GRAPH THEORY",
    "title": "Why Linear DAGs Fail in Production AI Workloads",
    "lead": "Directed Acyclic Graphs assume forward-only execution; real-world tool failures and model hallucinations demand cycles.",
    "section": "Foundations & Graph Theory",
    "takeaway": "DAGs treat errors as fatal pipeline crashes; cyclic state machines treat errors as routing decisions.",
    "notes": {
        "goal": "Explain the fundamental theoretical limitation of DAGs for agentic workflows and why cyclic graphs are non-negotiable.",
        "talkTrack": "Early LLM frameworks popularized linear chains: Step A feeds Step B feeds Step C. This works for simple extract-transform-load tasks. But real production agents interact with external APIs that fail, databases that return empty sets, and models that generate malformed JSON. In a DAG, an error aborts the pipeline. In a cyclic state machine, the error is an observation appended to state, enabling the model to self-correct.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Left: Rigid Linear DAG -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="520" height="400" rx="8" class="node-box"/>
          <rect x="0" y="0" width="520" height="44" rx="8" fill="#24191d"/>
          {render_icon("alert", 14, 10, size=24, color="#d98585")}
          <text x="46" y="28" class="text-h1" fill="#d98585">Linear DAG: The Fragile Forward Pipeline</text>
          
          <g transform="translate(20, 65)">
            <!-- Step 1 -->
            <rect x="0" y="0" width="130" height="60" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="65" y="26" text-anchor="middle" class="text-h2">1. Ingress</text>
            <text x="65" y="44" text-anchor="middle" class="text-dim">User Prompt</text>
            
            <path d="M 130 30 L 165 30" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>
            
            <!-- Step 2 -->
            <rect x="175" y="0" width="140" height="60" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="245" y="26" text-anchor="middle" class="text-h2">2. Model Prompt</text>
            <text x="245" y="44" text-anchor="middle" class="text-dim">Generates SQL</text>
            
            <path d="M 315 30 L 350 30" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>
            
            <!-- Step 3 (Failed) -->
            <rect x="360" y="0" width="130" height="60" rx="6" fill="#2d161a" stroke="#d98585" stroke-width="1.8"/>
            <text x="425" y="26" text-anchor="middle" class="text-h2" fill="#d98585">3. Tool Call</text>
            <text x="425" y="44" text-anchor="middle" class="text-mono-coral">HTTP 504 Timeout</text>
            
            <!-- Crash Box -->
            <path d="M 425 60 L 425 105" stroke="#d98585" stroke-width="1.8" stroke-dasharray="3 3" fill="none" marker-end="url(#arr-coral)"/>
            
            <rect x="150" y="115" width="340" height="75" rx="6" fill="#1c1417" stroke="#d98585" stroke-width="1.2"/>
            <text x="170" y="140" class="text-mono-coral" font-size="11">FATAL EXCEPTION: PIPELINE HALTED</text>
            <text x="170" y="160" class="text-p">&bull; Ephemeral state garbage collected</text>
            <text x="170" y="178" class="text-p">&bull; 0 self-healing or retry capability</text>

            <!-- DAG Metrics Summary -->
            <g transform="translate(0, 215)">
              <rect x="0" y="0" width="480" height="95" rx="6" fill="#121824" stroke="#253245"/>
              <text x="16" y="24" class="text-mono-coral" font-size="10.5">ARCHITECTURAL FLAWS OF DAG RUNTIMES</text>
              <text x="16" y="46" class="text-p">&bull; Cannot represent while-loops or iterative query refinement</text>
              <text x="16" y="66" class="text-p">&bull; Tool failures bubble up directly to client applications</text>
              <text x="16" y="86" class="text-p">&bull; Rigid graph structures cannot branch conditionally on runtime values</text>
            </g>
          </g>
        </g>

        <!-- Right: Cyclic State Machine Graph -->
        <g transform="translate(560, 0)">
          <rect x="0" y="0" width="690" height="400" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="690" height="44" rx="8" fill="#1e2c42"/>
          {render_icon("cycle", 14, 10, size=24, color="#60a5fa")}
          <text x="46" y="28" class="text-h1" fill="#60a5fa">Cyclic State Machine: Enterprise Self-Correction</text>
          
          <g transform="translate(25, 65)">
            <!-- Ingress -->
            <rect x="0" y="15" width="105" height="54" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="52" y="38" text-anchor="middle" class="text-h2">Ingress</text>
            <text x="52" y="54" text-anchor="middle" class="text-dim">User Task</text>

            <path d="M 105 42 L 140 42" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

            <!-- Node 1: Model Reasoning -->
            <rect x="150" y="10" width="140" height="64" rx="6" class="node-box-active"/>
            <text x="220" y="34" text-anchor="middle" class="text-h1" fill="#60a5fa">Model Node</text>
            <text x="220" y="52" text-anchor="middle" class="text-mono">emit tool_call</text>

            <path d="M 290 42 L 325 42" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

            <!-- Node 2: Tool Execution -->
            <rect x="335" y="10" width="140" height="64" rx="6" class="node-box-active-green"/>
            <text x="405" y="34" text-anchor="middle" class="text-h1" fill="#6ee7b7">Tool Node</text>
            <text x="405" y="52" text-anchor="middle" class="text-mono-green">exec SQL / API</text>

            <!-- Conditional Router Diamond -->
            <path d="M 475 42 L 510 42" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>
            
            <polygon points="545,15 585,42 545,69 505,42" fill="#1e293b" stroke="#e0c58e" stroke-width="1.5"/>
            <text x="545" y="46" text-anchor="middle" class="text-mono-amber" font-size="9.5">ROUTE</text>

            <!-- Success Path -> Terminal Answer -->
            <path d="M 585 42 L 625 42" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>
            <rect x="625" y="15" width="100" height="54" rx="6" fill="#152420" stroke="#6ee7b7"/>
            <text x="675" y="38" text-anchor="middle" class="text-h2" fill="#6ee7b7">Finalize</text>
            <text x="675" y="54" text-anchor="middle" class="text-dim">Answer Delivered</text>

            <!-- Cyclic Recovery Path -->
            <path d="M 545 69 L 545 120 L 220 120 L 220 74" stroke="#e0c58e" stroke-width="2" stroke-dasharray="4 3" fill="none" marker-end="url(#arr-amber)"/>
            
            <!-- Recovery Annotation Badge -->
            <rect x="250" y="105" width="260" height="30" rx="4" fill="#1b2434" stroke="#e0c58e" stroke-width="1.2"/>
            <text x="380" y="125" text-anchor="middle" class="text-mono-amber" font-size="10.5">ON ERROR: Append ToolMessage &amp; Loop</text>

            <!-- State Machine Specifications -->
            <g transform="translate(0, 160)">
              <rect x="0" y="0" width="635" height="150" rx="6" fill="#111824" stroke="#253245"/>
              {render_zone_badge("CYCLIC STATE ADVANTAGES", 15, 12, 190, 24, "#60a5fa")}
              
              <g transform="translate(15, 48)">
                <text x="0" y="18" class="text-mono-green" font-size="11">DETERMINISTIC RETRY GOVERNOR</text>
                <text x="0" y="38" class="text-p">State retains retry_counter: int. Graph enforces hard cap (max 3 cycles)</text>
                <text x="0" y="56" class="text-p">before routing to a deterministic fallback handler.</text>
              </g>

              <g transform="translate(330, 48)">
                <text x="0" y="18" class="text-mono-amber" font-size="11">MODEL SELF-REFLECTION</text>
                <text x="0" y="38" class="text-p">Error details (e.g. invalid column name) are fed directly into the model context,</text>
                <text x="0" y="56" class="text-p">allowing it to adjust arguments rather than failing the user request.</text>
              </g>
            </g>
          </g>
        </g>
      </g>
    """)
}
