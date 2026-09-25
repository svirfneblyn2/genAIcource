# Slide 10: Tool Error Recovery Policies
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 10,
    "kicker": "FAULT TOLERANCE",
    "title": "Tool Error Handling: Retries, Reflection, and Circuit Breakers",
    "lead": "Designing graceful degradation paths when third-party APIs fail or model parameters hallucinate.",
    "section": "Tools & Sandboxing",
    "takeaway": "Distinguish between transient network faults (exponential backoff) and semantic schema errors (model reflection).",
    "notes": {
        "goal": "Equip engineers with a 4-tier taxonomy for handling tool failures without crashing the agent.",
        "talkTrack": "A production agent will encounter tool failures continuously. But treating all errors the same is an anti-pattern. If you get an HTTP 429 or 503, retrying with exponential backoff makes sense. But if you get an HTTP 401 Unauthorized, retrying is useless. And if Pydantic rejects an argument because the model passed an invalid date format, retrying the tool code will fail again. You must route schema errors back to the model so it can self-correct.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("circuit_breaker", 15, 10, size=24, color="#e0c58e")}
        <text x="48" y="28" class="text-h1" fill="#e0c58e">The 4-Tier Tool Fault Tolerance Decision Funnel</text>

        <!-- 4 Tiers Layout -->
        <g transform="translate(20, 60)">
          <!-- Tier 1: Transient Errors -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="295" height="235" rx="6" class="node-box-active"/>
            <text x="14" y="22" class="text-mono" font-size="11">TIER 1: TRANSIENT FAULTS</text>
            <rect x="12" y="32" width="270" height="42" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="20" y="52" class="text-mono-coral" font-size="10.5">HTTP 429 / 502 / 503 / 504 Timeout</text>
            <text x="20" y="66" class="text-dim" font-size="9.5">Network blips, upstream rate limits</text>

            <g transform="translate(12, 85)">
              <text x="0" y="16" class="text-mono-green" font-size="10.5">RECOVERY MECHANISM:</text>
              <text x="0" y="36" class="text-p">&bull; Exponential backoff + Full Jitter</text>
              <text x="0" y="54" class="text-mono" font-size="9.5">t = min(max_t, b * 2^n + rand())</text>
              <text x="0" y="74" class="text-p">&bull; Max 3 retry attempts</text>
              <text x="0" y="94" class="text-p">&bull; Circuit breaker trips if &gt; 5 faults/min</text>
            </g>

            <rect x="12" y="195" width="270" height="30" rx="4" fill="#1b2434" stroke="#60a5fa"/>
            <text x="147" y="215" text-anchor="middle" class="text-mono" font-size="10">Action: Retry Tool Node in-place</text>
          </g>

          <path d="M 295 115 L 315 115" stroke="#253245" stroke-width="2" fill="none"/>

          <!-- Tier 2: Schema / Validation Errors -->
          <g transform="translate(320, 0)">
            <rect x="0" y="0" width="295" height="235" rx="6" class="node-box-active-amber"/>
            <text x="14" y="22" class="text-mono-amber" font-size="11">TIER 2: SCHEMA VALIDATION FAULT</text>
            <rect x="12" y="32" width="270" height="42" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="20" y="52" class="text-mono-amber" font-size="10.5">Pydantic ValidationError</text>
            <text x="20" y="66" class="text-dim" font-size="9.5">Missing argument, invalid type/regex</text>

            <g transform="translate(12, 85)">
              <text x="0" y="16" class="text-mono-amber" font-size="10.5">RECOVERY MECHANISM:</text>
              <text x="0" y="36" class="text-p">&bull; NEVER retry tool code blindly</text>
              <text x="0" y="54" class="text-p">&bull; Intercept error message &amp; fields</text>
              <text x="0" y="74" class="text-p">&bull; Append ToolMessage(error=...) to state</text>
              <text x="0" y="94" class="text-p">&bull; Model Node reflects &amp; adjusts JSON</text>
            </g>

            <rect x="12" y="195" width="270" height="30" rx="4" fill="#2d2516" stroke="#e0c58e"/>
            <text x="147" y="215" text-anchor="middle" class="text-mono-amber" font-size="10">Action: Cycle to Model Node</text>
          </g>

          <path d="M 615 115 L 635 115" stroke="#253245" stroke-width="2" fill="none"/>

          <!-- Tier 3: Non-Retryable Faults -->
          <g transform="translate(640, 0)">
            <rect x="0" y="0" width="295" height="235" rx="6" class="node-box-active-coral"/>
            <text x="14" y="22" class="text-mono-coral" font-size="11">TIER 3: PERMANENT / AUTH FAULT</text>
            <rect x="12" y="32" width="270" height="42" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="20" y="52" class="text-mono-coral" font-size="10.5">HTTP 401 / 403 / 404 Entity Missing</text>
            <text x="20" y="66" class="text-dim" font-size="9.5">Invalid credentials or forbidden scope</text>

            <g transform="translate(12, 85)">
              <text x="0" y="16" class="text-mono-coral" font-size="10.5">RECOVERY MECHANISM:</text>
              <text x="0" y="36" class="text-p">&bull; Zero retries (retries waste tokens/cost)</text>
              <text x="0" y="54" class="text-p">&bull; Deterministic fast-fail path</text>
              <text x="0" y="74" class="text-p">&bull; Log security audit event to SIEM</text>
              <text x="0" y="94" class="text-p">&bull; Route directly to Fallback Node</text>
            </g>

            <rect x="12" y="195" width="270" height="30" rx="4" fill="#24191d" stroke="#d98585"/>
            <text x="147" y="215" text-anchor="middle" class="text-mono-coral" font-size="10">Action: Fast-Fail to Fallback</text>
          </g>

          <path d="M 935 115 L 955 115" stroke="#253245" stroke-width="2" fill="none"/>

          <!-- Tier 4: Fallback & DLQ -->
          <g transform="translate(960, 0)">
            <rect x="0" y="0" width="260" height="235" rx="6" class="node-box-active-purple"/>
            <text x="14" y="22" class="text-mono-purple" font-size="11">TIER 4: DEGRADED FALLBACK</text>
            <rect x="12" y="32" width="235" height="42" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="20" y="52" class="text-mono-purple" font-size="10.5">Retries / Budget Exhausted</text>
            <text x="20" y="66" class="text-dim" font-size="9.5">Tool completely unreachable</text>

            <g transform="translate(12, 85)">
              <text x="0" y="16" class="text-mono-purple" font-size="10.5">FINAL SAFETY GATE:</text>
              <text x="0" y="36" class="text-p">&bull; Emit Dead-Letter Queue event</text>
              <text x="0" y="54" class="text-p">&bull; Deliver partial result to user</text>
              <text x="0" y="74" class="text-p">&bull; Explanatory error caveat</text>
              <text x="0" y="94" class="text-p">&bull; Trigger human support ticket</text>
            </g>

            <rect x="12" y="195" width="235" height="30" rx="4" fill="#1e1829" stroke="#b4a4e5"/>
            <text x="130" y="215" text-anchor="middle" class="text-mono-purple" font-size="10">Action: Graceful Delivery</text>
          </g>
        </g>

        <!-- Bottom Summary Bar -->
        <g transform="translate(20, 315)">
          <rect x="0" y="0" width="1220" height="60" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-green" font-size="11">SLA POLICY FOR ENTERPRISE APIS:</text>
          <text x="16" y="44" class="text-p">Wrap all external calls in an explicit timeout handler (2000ms max). Never let an unhandled tool exception bubble up to terminate the graph.</text>
        </g>
      </g>
    """)
}
