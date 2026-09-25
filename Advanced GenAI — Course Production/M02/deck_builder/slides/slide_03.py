# Slide 03: The ReAct Paradigm and its Limitations
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 3,
    "kicker": "EXECUTION PARADIGMS",
    "title": "The ReAct Loop: Fragility at Enterprise Scale",
    "lead": "While ReAct enables dynamic tool usage, unconstrained prompt-based loops introduce severe operational vulnerabilities.",
    "section": "Foundations & Graph Theory",
    "takeaway": "Unconstrained ReAct loops risk quadratic token growth, non-deterministic termination, and latency blowup.",
    "notes": {
        "goal": "Critically analyze the ReAct (Reason + Act) prompting pattern, explaining why production systems must wrap ReAct in strict state machines.",
        "talkTrack": "ReAct, published by Yao et al. in 2022, was a breakthrough in prompting: interleaving reasoning thoughts with action calls. But when deployed raw in production without an orchestrator, ReAct becomes a liability. Every thought and tool observation is appended to the prompt history. Token count compounds quadratically, p99 latency explodes past 45 seconds, and models often enter infinite oscillation loops. We need explicit state guards.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Left: ReAct Token Accumulation Wheel -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="560" height="400" rx="8" class="node-box"/>
          <rect x="0" y="0" width="560" height="44" rx="8" fill="#1b2434"/>
          {render_icon("cycle", 14, 10, size=24, color="#e0c58e")}
          <text x="46" y="28" class="text-h1" fill="#e0c58e">ReAct Cycle: Compounding Token Consumption</text>
          
          <g transform="translate(30, 65)">
            <!-- Circular Loop Nodes -->
            <!-- Step 1: Thought -->
            <rect x="180" y="0" width="140" height="50" rx="6" class="node-box-active"/>
            <text x="250" y="25" text-anchor="middle" class="text-mono" fill="#60a5fa">1. Thought</text>
            <text x="250" y="40" text-anchor="middle" class="text-dim">Reason about state</text>

            <path d="M 320 25 Q 420 25 420 100" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

            <!-- Step 2: Action -->
            <rect x="350" y="100" width="140" height="50" rx="6" class="node-box-active-green"/>
            <text x="420" y="125" text-anchor="middle" class="text-mono-green">2. Action</text>
            <text x="420" y="140" text-anchor="middle" class="text-dim">Emit tool payload</text>

            <path d="M 420 150 Q 420 220 320 220" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

            <!-- Step 3: Observation -->
            <rect x="180" y="195" width="140" height="50" rx="6" class="node-box-active-amber"/>
            <text x="250" y="220" text-anchor="middle" class="text-mono-amber">3. Observation</text>
            <text x="250" y="235" text-anchor="middle" class="text-dim">Raw tool response</text>

            <path d="M 180 220 Q 80 220 80 145 Q 80 25 180 25" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>

            <!-- Token Growth Step Bar -->
            <g transform="translate(10, 260)">
              <rect x="0" y="0" width="480" height="65" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="20" class="text-mono" font-size="10.5" fill="#cbd5e1">QUADRATIC TOKEN ACCUMULATION PER ROUNDTRIP:</text>
              <text x="14" y="44" class="text-mono-coral" font-size="11">Turn 1: 1.2k tokens &rarr; Turn 2: 3.8k tokens &rarr; Turn 3: 8.5k tokens &rarr; Turn 4: 16.2k tokens</text>
            </g>
          </g>
        </g>

        <!-- Right: 4 Production Failure Modes -->
        <g transform="translate(590, 0)">
          <rect x="0" y="0" width="670" height="400" rx="8" class="node-box"/>
          <rect x="0" y="0" width="670" height="44" rx="8" fill="#24191d"/>
          {render_icon("alert", 14, 10, size=24, color="#d98585")}
          <text x="46" y="28" class="text-h1" fill="#d98585">The Four Production Failure Modes of Raw ReAct</text>
          
          <g transform="translate(20, 60)">
            <!-- Failure 1 -->
            <rect x="0" y="0" width="630" height="68" rx="6" fill="#171922" stroke="#253245"/>
            <rect x="0" y="0" width="6" height="68" rx="2" fill="#d98585"/>
            <text x="18" y="22" class="text-mono-coral" font-size="11">1. CONTEXT WINDOW POISONING &amp; NEEDLE DRIFT</text>
            <text x="18" y="42" class="text-p">Every raw tool return (e.g. 50-row SQL dumps) stays in memory. Attention on initial system prompt</text>
            <text x="18" y="58" class="text-dim">degrades as sequence length grows, inducing semantic drift and loss of original user constraints.</text>

            <!-- Failure 2 -->
            <rect x="0" y="78" width="630" height="68" rx="6" fill="#171922" stroke="#253245"/>
            <rect x="0" y="0" width="6" height="68" rx="2" fill="#e0c58e"/>
            <text x="18" y="100" class="text-mono-amber" font-size="11">2. INFINITE OSCILLATION &amp; TOOL RETRY LOOPS</text>
            <text x="18" y="120" class="text-p">When a tool returns an error, the model repeatedly alternates between two identical failing tools</text>
            <text x="18" y="136" class="text-dim">without adjusting parameters. Raw ReAct lacks stateful cycle counters to break infinite loops.</text>

            <!-- Failure 3 -->
            <rect x="0" y="156" width="630" height="68" rx="6" fill="#171922" stroke="#253245"/>
            <rect x="0" y="0" width="6" height="68" rx="2" fill="#60a5fa"/>
            <text x="18" y="178" class="text-mono" font-size="11">3. LATENCY SLA BLOWUP (p99 &gt; 45 SECONDS)</text>
            <text x="18" y="198" class="text-p">Unbounded sequential LLM inferences compound total user response time linearly per step.</text>
            <text x="18" y="214" class="text-dim">6 tool iterations at 4s per LLM generation plus 1.5s tool latency creates a catastrophic 33-second SLA.</text>

            <!-- Failure 4 -->
            <rect x="0" y="234" width="630" height="85" rx="6" fill="#171922" stroke="#253245"/>
            <rect x="0" y="0" width="6" height="85" rx="2" fill="#6ee7b7"/>
            <text x="18" y="256" class="text-mono-green" font-size="11">4. THE FIX: GRAPH WRAPPERS WITH HARD GOVERNORS</text>
            <text x="18" y="276" class="text-p">&bull; Wrap ReAct within a State Graph with explicit recursion_limit = 10.</text>
            <text x="18" y="294" class="text-p">&bull; Prune tool observations before re-injecting into the message history.</text>
            <text x="18" y="310" class="text-dim">&bull; Route to deterministic fallback handler when loop limits trigger.</text>
          </g>
        </g>
      </g>
    """)
}
