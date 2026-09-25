# Slide 23: Runaway Loop Detection & Guardrails
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 23,
    "kicker": "PRODUCTION RELIABILITY",
    "title": "Loop Detection, Recursion Limits, and Cost Governors",
    "lead": "Implementing circuit breakers to terminate runaway agent oscillations and enforce hard cost ceilings.",
    "section": "Production Observability",
    "takeaway": "Never deploy an agent without hard recursion limits and per-run token budget circuit breakers.",
    "notes": {
        "goal": "Explain how to protect production budgets and compute from catastrophic runaway agent loops and infinite tool calls.",
        "talkTrack": "In distributed systems, runaway processes cause out-of-memory errors. In GenAI, runaway agents drain corporate credit cards. If an agent gets stuck in a loop calling a paid search API 100 times, a single user prompt could cost $50 and lock a thread. We enforce three defense layers: compile-time recursion_limit, state hash cycle detection to catch repetitive oscillations, and budget circuit breakers that terminate execution once a dollar or token ceiling is breached.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active-coral"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#24191d"/>
        {render_icon("alert", 15, 10, size=24, color="#d98585")}
        <text x="48" y="28" class="text-h1" fill="#d98585">Defense-in-Depth: Runaway Loop Prevention &amp; Cost Circuit Breakers</text>

        <!-- 3 Defense Layers -->
        <g transform="translate(20, 60)">
          <!-- Layer 1: Recursion Limits -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#1b2434"/>
            <text x="14" y="20" class="text-mono" font-size="11">LAYER 1: RECURSION DEPTH CAP</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="50" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="20" class="text-mono" font-size="9.5" fill="#e2e8f0">app.invoke(inputs,</text>
              <text x="20" y="36" class="text-mono-green" font-size="9.5">  config={{"recursion_limit": 25}})</text>

              <text x="0" y="75" class="text-mono-green" font-size="10.5">HOW IT GOVERNS RUNS:</text>
              <text x="0" y="95" class="text-p">&bull; Hard limit on total super-step node transitions.</text>
              <text x="0" y="115" class="text-p">&bull; Throws GraphRecursionError on step 26.</text>
              <text x="0" y="135" class="text-dim">&bull; Prevents unbounded graph traversals.</text>
            </g>
          </g>

          <!-- Layer 2: State Hash Cycle Detector -->
          <g transform="translate(415, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#1b2434"/>
            <text x="14" y="20" class="text-mono-amber" font-size="11">LAYER 2: STATE HASH CYCLE DETECTOR</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="50" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-amber" font-size="9.5">h = md5(last_3_tool_signatures)</text>
              <text x="12" y="36" class="text-mono-coral" font-size="9.5">if seen_hashes[h] &gt; 2: trip_circuit()</text>

              <text x="0" y="75" class="text-mono-amber" font-size="10.5">HOW IT DETECTS OSCILLATION:</text>
              <text x="0" y="95" class="text-p">&bull; Detects identical tool calls repeated consecutively.</text>
              <text x="0" y="115" class="text-p">&bull; Catches A &rarr; B &rarr; A &rarr; B ping-pong oscillations.</text>
              <text x="0" y="135" class="text-dim">&bull; Interrupts before token budget is burned.</text>
            </g>
          </g>

          <!-- Layer 3: Dollar & Token Budget Breaker -->
          <g transform="translate(830, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box-active-coral"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#24191d"/>
            <text x="14" y="20" class="text-mono-coral" font-size="11">LAYER 3: FINANCIAL BUDGET BREAKER</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="50" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-coral" font-size="9.5">if total_cost_usd &gt; 0.50 or</text>
              <text x="12" y="36" class="text-mono-coral" font-size="9.5">   total_tokens &gt; 40000: abort_run()</text>

              <text x="0" y="75" class="text-mono-coral" font-size="10.5">HOW IT ENFORCES BUDGETS:</text>
              <text x="0" y="95" class="text-p">&bull; Real-time token counter updated on every LLM span.</text>
              <text x="0" y="115" class="text-p">&bull; Enforces strict corporate cost ceilings ($0.50 max/run).</text>
              <text x="0" y="135" class="text-dim">&bull; Routes to graceful degraded fallback on trip.</text>
            </g>
          </g>
        </g>

        <!-- Bottom Fail-Safe Action -->
        <g transform="translate(20, 310)">
          <rect x="0" y="0" width="1220" height="65" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-green" font-size="11">ACTION ON GOVERNOR TRIP:</text>
          <text x="16" y="46" class="text-p">Graph pauses immediately &bull; State status updated to TIMEOUT_CIRCUIT_BROKEN &bull; PagerDuty alert emitted &bull; Safe fallback response delivered to end-user.</text>
        </g>
      </g>
    """)
}
