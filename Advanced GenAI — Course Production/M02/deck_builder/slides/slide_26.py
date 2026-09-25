# Slide 26: Instructor Live Walkthrough
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 26,
    "kicker": "INSTRUCTOR LIVE DEMO",
    "title": "Live Demo Tour: LangGraph Studio & State Inspection",
    "lead": "A safe, 10-15 minute visual walkthrough of graph compilation, breakpoint hits, and state mutation.",
    "section": "Instructor Demo",
    "takeaway": "Demonstrate agent internals visually: compile the graph, step through nodes, trigger an interrupt, and resume.",
    "notes": {
        "goal": "Provide instructors with a structured, zero-stress 15-minute click-by-click live walkthrough script.",
        "talkTrack": "Now we move to our live demo. Instructors, you do not need to deploy cloud clusters. Open LangGraph Studio or the local trace UI. We will walk through five concrete steps: first, show the compiled graph topology. Second, inject an invoice test payload. Third, watch the graph illuminate and pause at our interrupt_before breakpoint. Fourth, edit the state in real-time to simulate a CFO approval. Finally, inspect the OpenTelemetry trace waterfall.",
        "timing": "15 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("browser", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Instructor Console Walkthrough: 5-Stage Demo Map</text>

        <!-- 5 Demo Stages -->
        <g transform="translate(20, 60)">
          <!-- Stage 1 -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="225" height="235" rx="6" class="node-box-active"/>
            <text x="14" y="22" class="text-mono" font-size="11">STAGE 1: COMPILE</text>
            
            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-h2">Graph Compilation</text>
              <text x="0" y="36" class="text-p">&bull; Open LangGraph Studio</text>
              <text x="0" y="56" class="text-p">&bull; Point to workflow graph</text>
              <text x="0" y="76" class="text-p">&bull; Show visual canvas</text>
              
              <rect x="0" y="95" width="195" height="40" rx="4" fill="#141c28" stroke="#3b82f6"/>
              <text x="10" y="114" class="text-mono" font-size="9.5">app = builder.compile(</text>
              <text x="16" y="128" class="text-mono-green" font-size="9">  checkpointer=saver)</text>

              <text x="0" y="155" class="text-dim" font-size="9.5">Duration: 2-3 minutes</text>
            </g>
          </g>

          <!-- Stage 2 -->
          <g transform="translate(250, 0)">
            <rect x="0" y="0" width="225" height="235" rx="6" class="node-box"/>
            <text x="14" y="22" class="text-mono" font-size="11">STAGE 2: INJECT</text>

            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-h2">Inject Test Payload</text>
              <text x="0" y="36" class="text-p">&bull; Paste invoice JSON</text>
              <text x="0" y="56" class="text-p">&bull; Click 'Start Run'</text>
              <text x="0" y="76" class="text-p">&bull; Watch nodes illuminate</text>
              
              <rect x="0" y="95" width="195" height="40" rx="4" fill="#141c28" stroke="#253245"/>
              <text x="10" y="114" class="text-mono" font-size="9.5">State: Step 1 (OCR)</text>
              <text x="10" y="128" class="text-mono-green" font-size="9">&rarr; Step 2 (ERP Match)</text>

              <text x="0" y="155" class="text-dim" font-size="9.5">Duration: 2-3 minutes</text>
            </g>
          </g>

          <!-- Stage 3 -->
          <g transform="translate(500, 0)">
            <rect x="0" y="0" width="225" height="235" rx="6" class="node-box-active-amber"/>
            <text x="14" y="22" class="text-mono-amber" font-size="11">STAGE 3: BREAKPOINT</text>

            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-h2">Inspect Paused State</text>
              <text x="0" y="36" class="text-p">&bull; Graph halts at barrier</text>
              <text x="0" y="56" class="text-p">&bull; Open State Inspector</text>
              <text x="0" y="76" class="text-p">&bull; Show variance: $450.00</text>
              
              <rect x="0" y="95" width="195" height="40" rx="4" fill="#2d2516" stroke="#e0c58e"/>
              <text x="10" y="114" class="text-mono-amber" font-size="9.5">STATUS: INTERRUPTED</text>
              <text x="10" y="128" class="text-dim" font-size="9">Awaiting human review</text>

              <text x="0" y="155" class="text-dim" font-size="9.5">Duration: 3 minutes</text>
            </g>
          </g>

          <!-- Stage 4 -->
          <g transform="translate(750, 0)">
            <rect x="0" y="0" width="225" height="235" rx="6" class="node-box-active-green"/>
            <text x="14" y="22" class="text-mono-green" font-size="11">STAGE 4: MUTATE</text>

            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-h2">Live State Mutation</text>
              <text x="0" y="36" class="text-p">&bull; Edit state variable in UI</text>
              <text x="0" y="56" class="text-p">&bull; Set approved_by="cfo"</text>
              <text x="0" y="76" class="text-p">&bull; Click 'Resume Graph'</text>
              
              <rect x="0" y="95" width="195" height="40" rx="4" fill="#152420" stroke="#6ee7b7"/>
              <text x="10" y="114" class="text-mono-green" font-size="9.5">State Updated: 200 OK</text>
              <text x="10" y="128" class="text-mono-green" font-size="9">Graph resumes to END</text>

              <text x="0" y="155" class="text-dim" font-size="9.5">Duration: 3 minutes</text>
            </g>
          </g>

          <!-- Stage 5 -->
          <g transform="translate(1000, 0)">
            <rect x="0" y="0" width="220" height="235" rx="6" class="node-box-active-purple"/>
            <text x="14" y="22" class="text-mono-purple" font-size="11">STAGE 5: TRACE</text>

            <g transform="translate(14, 45)">
              <text x="0" y="16" class="text-h2">Audit Tracing Spans</text>
              <text x="0" y="36" class="text-p">&bull; Open LangSmith trace</text>
              <text x="0" y="56" class="text-p">&bull; Inspect span latency</text>
              <text x="0" y="76" class="text-p">&bull; Review token spend</text>
              
              <rect x="0" y="95" width="190" height="40" rx="4" fill="#241b33" stroke="#b4a4e5"/>
              <text x="10" y="114" class="text-mono-purple" font-size="9.5">Total Tokens: 3,420</text>
              <text x="10" y="128" class="text-mono-purple" font-size="9">Run Cost: $0.012</text>

              <text x="0" y="155" class="text-dim" font-size="9.5">Duration: 3 minutes</text>
            </g>
          </g>
        </g>

        <!-- Bottom Demo Tips -->
        <g transform="translate(20, 310)">
          <rect x="0" y="0" width="1220" height="65" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-green" font-size="11">INSTRUCTOR PREPARATION CHECKLIST:</text>
          <text x="16" y="46" class="text-p">Run locally with MemorySaver for zero cloud dependency &bull; Pre-load sample invoice JSON payload in clipboard &bull; Keep LangGraph Studio window open in Chrome tab 2.</text>
        </g>
      </g>
    """)
}
