# Slide 16: Context Window Protection
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 16,
    "kicker": "TOKEN OPTIMIZATION",
    "title": "Context Window Protection: Pruning and Condensation",
    "lead": "Preventing quadratic token inflation and prompt degradation across multi-turn agent execution.",
    "section": "Production Reliability",
    "takeaway": "Never pass raw conversation histories to sub-agents; summarize intermediate tool outputs into structured deltas.",
    "notes": {
        "goal": "Explain specific systems techniques to prune, filter, and summarize state to keep token consumption flat over long runs.",
        "talkTrack": "In multi-step agents, token bloat is the number one cause of production failure. When an agent runs for 15 turns, intermediate tool outputs (like 500 lines of JSON from an ERP) flood the context. The model loses track of its original goal. We use three techniques: Message Trimming keeps the system prompt plus the last K turns; Tool Scrubbing strips HTML and returns only requested keys; and State Condensation runs a background pass to turn 10 conversation turns into a 3-sentence summary.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("cost", 15, 10, size=24, color="#6ee7b7")}
        <text x="48" y="28" class="text-h1" fill="#6ee7b7">Context Window Protection: Trimming, Scrubbing &amp; Condensation</text>

        <!-- 3 Architecture Columns -->
        <g transform="translate(20, 60)">
          <!-- Technique 1: Message Trimming -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#1e2c42"/>
            <text x="14" y="20" class="text-mono" font-size="11">TECHNIQUE 1: MESSAGE TRIMMING</text>
            
            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="55" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="20" class="text-mono" font-size="9" fill="#e2e8f0">trim_messages(</text>
              <text x="18" y="34" class="text-mono" font-size="9" fill="#60a5fa">  max_tokens=4000, strategy="last",</text>
              <text x="18" y="48" class="text-mono" font-size="9" fill="#60a5fa">  include_system=True, allow_partial=False)</text>

              <text x="0" y="75" class="text-mono-green" font-size="10.5">HOW IT PROTECTS CONTEXT:</text>
              <text x="0" y="95" class="text-p">&bull; Retains the foundational SystemMessage.</text>
              <text x="0" y="115" class="text-p">&bull; Discards oldest intermediate turns once threshold trips.</text>
              <text x="0" y="135" class="text-dim">&bull; Prevents ContextWindowExceededException errors.</text>
            </g>
          </g>

          <!-- Technique 2: Tool Output Scrubbing -->
          <g transform="translate(415, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box-active-green"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#152420"/>
            <text x="14" y="20" class="text-mono-green" font-size="11">TECHNIQUE 2: TOOL PAYLOAD SCRUBBING</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="55" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-coral" font-size="9">RAW API: 120kb HTML / 45-field JSON</text>
              <text x="12" y="38" class="text-mono-green" font-size="9">&rarr; FILTERED: {{"status": 200, "balance": 450.00}}</text>

              <text x="0" y="75" class="text-mono-green" font-size="10.5">HOW IT PROTECTS CONTEXT:</text>
              <text x="0" y="95" class="text-p">&bull; Strips CSS, HTML boilerplate, and metadata keys.</text>
              <text x="0" y="115" class="text-p">&bull; Retains strictly the typed fields requested by the schema.</text>
              <text x="0" y="135" class="text-dim">&bull; 85% to 95% token savings on tool observation steps.</text>
            </g>
          </g>

          <!-- Technique 3: State Condensation -->
          <g transform="translate(830, 0)">
            <rect x="0" y="0" width="390" height="235" rx="6" class="node-box-active-amber"/>
            <rect x="0" y="0" width="390" height="30" rx="6" fill="#2d2516"/>
            <text x="14" y="20" class="text-mono-amber" font-size="11">TECHNIQUE 3: SUMMARY CONDENSATION</text>

            <g transform="translate(14, 45)">
              <rect x="0" y="0" width="360" height="55" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-amber" font-size="9">Background Summarizer Node:</text>
              <text x="12" y="38" class="text-p">Compresses turns 1..10 into 1 summary message</text>

              <text x="0" y="75" class="text-mono-amber" font-size="10.5">HOW IT PROTECTS CONTEXT:</text>
              <text x="0" y="95" class="text-p">&bull; Preserves critical business facts without token weight.</text>
              <text x="0" y="115" class="text-p">&bull; Appends summary: HumanMessage(content="[Prior Summary]")</text>
              <text x="0" y="135" class="text-dim">&bull; Keeps token curve flat across 100+ turns.</text>
            </g>
          </g>
        </g>

        <!-- Bottom Metric Comparison -->
        <g transform="translate(20, 310)">
          <rect x="0" y="0" width="1220" height="65" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-green" font-size="11">ENTERPRISE PRODUCTION METRIC (15-TURN WORKFLOW):</text>
          <text x="16" y="46" class="text-p">Unmanaged thread token usage: 48,500 tokens ($0.48/run) &bull; Managed thread token usage: 3,400 tokens ($0.034/run) &bull; 14.2x Cost Reduction.</text>
        </g>
      </g>
    """)
}
