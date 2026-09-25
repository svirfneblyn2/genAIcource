# Slide 21: The Full Cost Model: What Goes into the Bill
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 21,
    "kicker": "COST & TCO",
    "title": "The Anatomy of an Enterprise GenAI Bill",
    "lead": "Raw token price is only one component: dissecting the 7 production cost categories.",
    "section": "Cost & TCO Modeling",
    "takeaway": "Vector index minimums and high-frequency tracing often exceed raw model inference costs at moderate traffic.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Waterfall Stacked Cost Bar Chart -->
        <g transform="translate(0, 10)">
          <rect x="0" y="0" width="1040" height="215" rx="8" class="swimlane-bg"/>
          <text x="24" y="24" class="text-mono-amber" font-size="12">MONTHLY PRODUCTION COST STACK (MODERATE TRAFFIC: 50,000 QUERIES/MO)</text>

          <!-- Bars container -->
          <g transform="translate(24, 62)">
            <!-- Bar 1: Raw LLM Tokens -->
            <g transform="translate(0, 0)">
              <rect x="0" y="35" width="125" height="100" rx="5" fill="#1e2c42" stroke="#60a5fa" stroke-width="1.2"/>
              <text x="62" y="22" text-anchor="middle" class="text-mono" font-size="11">$240 / mo</text>
              <text x="62" y="68" text-anchor="middle" class="text-h2" fill="#60a5fa">1. Tokens</text>
              <text x="62" y="88" text-anchor="middle" class="text-dim">Input &amp; Output</text>
              <text x="62" y="108" text-anchor="middle" class="text-dim">Claude / GPT-4o</text>
            </g>

            <!-- Bar 2: Prompt Caching Discount -->
            <g transform="translate(145, 0)">
              <rect x="0" y="75" width="125" height="60" rx="5" fill="#14241e" stroke="#6ee7b7" stroke-width="1.2"/>
              <text x="62" y="62" text-anchor="middle" class="text-mono-green" font-size="11">-$120 / mo</text>
              <text x="62" y="98" text-anchor="middle" class="text-h2" fill="#6ee7b7">2. Caching</text>
              <text x="62" y="118" text-anchor="middle" class="text-dim">50-80% rebate</text>
            </g>

            <!-- Bar 3: Embeddings -->
            <g transform="translate(290, 0)">
              <rect x="0" y="110" width="125" height="25" rx="5" fill="#221e16" stroke="#e0c58e" stroke-width="1.2"/>
              <text x="62" y="98" text-anchor="middle" class="text-mono-amber" font-size="11">$25 / mo</text>
              <text x="62" y="127" text-anchor="middle" class="text-dim">3. Embeddings</text>
            </g>

            <!-- Bar 4: Vector Index Store -->
            <g transform="translate(435, 0)">
              <rect x="0" y="0" width="135" height="135" rx="5" fill="#2d1c22" stroke="#d98585" stroke-width="1.8"/>
              <text x="67" y="-12" text-anchor="middle" class="text-mono-coral" font-size="11" font-weight="700">COST DRIVER</text>
              <text x="67" y="20" text-anchor="middle" class="text-mono-coral" font-size="12">$700 / mo</text>
              <text x="67" y="62" text-anchor="middle" class="text-h2" fill="#d98585">4. Vector DB</text>
              <text x="67" y="84" text-anchor="middle" class="text-dim">OpenSearch OCU</text>
              <text x="67" y="104" text-anchor="middle" class="text-dim">or Azure S1 Units</text>
            </g>

            <!-- Bar 5: Agent State -->
            <g transform="translate(590, 0)">
              <rect x="0" y="85" width="125" height="50" rx="5" fill="#221c32" stroke="#b4a4e5" stroke-width="1.2"/>
              <text x="62" y="72" text-anchor="middle" class="text-mono-purple" font-size="11">$60 / mo</text>
              <text x="62" y="108" text-anchor="middle" class="text-h2" fill="#b4a4e5">5. Agent State</text>
              <text x="62" y="126" text-anchor="middle" class="text-dim">Session store</text>
            </g>

            <!-- Bar 6: Eval Batches -->
            <g transform="translate(735, 0)">
              <rect x="0" y="80" width="125" height="55" rx="5" fill="#1b2434" stroke="#253245" stroke-width="1.2"/>
              <text x="62" y="67" text-anchor="middle" class="text-mono" font-size="11">$80 / mo</text>
              <text x="62" y="106" text-anchor="middle" class="text-h2">6. Evals</text>
              <text x="62" y="125" text-anchor="middle" class="text-dim">Judge LLM runs</text>
            </g>

            <!-- Bar 7: Tracing & Logs -->
            <g transform="translate(880, 0)">
              <rect x="0" y="55" width="115" height="80" rx="5" fill="#1b2434" stroke="#60a5fa" stroke-width="1.2"/>
              <text x="57" y="42" text-anchor="middle" class="text-mono" font-size="11">$140 / mo</text>
              <text x="57" y="90" text-anchor="middle" class="text-h2">7. Traces</text>
              <text x="57" y="110" text-anchor="middle" class="text-dim">OTel log storage</text>
            </g>
          </g>
        </g>

        <!-- Bottom: The 3 Surprising Cost Realities -->
        <g transform="translate(0, 240)">
          <rect x="0" y="0" width="1040" height="155" rx="8" class="node-box"/>
          <rect x="0" y="0" width="1040" height="34" rx="8" fill="#1b2434"/>
          <text x="24" y="23" class="text-h2" fill="#e0c58e">PRODUCTION COST REALITIES &amp; LESSONS</text>

          <g transform="translate(20, 46)">
            <!-- Reality 1 -->
            <rect x="0" y="0" width="315" height="96" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="14" y="22" class="text-mono-coral">1. Vector Minimums Dominate</text>
            <text x="14" y="44" class="text-p">OpenSearch Serverless (4 OCUs) or</text>
            <text x="14" y="60" class="text-p">Azure AI Search (S1) cost $250-$700/mo.</text>
            <text x="14" y="82" class="text-mono-green" font-size="11">Mitigate: Aurora pgvector for small apps</text>

            <!-- Reality 2 -->
            <g transform="translate(340, 0)">
              <rect x="0" y="0" width="320" height="96" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-mono-green">2. Prompt Caching Saves 50-80%</text>
              <text x="14" y="44" class="text-p">Static system instructions &amp; policy chunks</text>
              <text x="14" y="60" class="text-p">qualify for high-speed cache read rates.</text>
              <text x="14" y="82" class="text-mono-green" font-size="11">Mitigate: Order prompt static-first</text>
            </g>

            <!-- Reality 3 -->
            <g transform="translate(685, 0)">
              <rect x="0" y="0" width="315" height="96" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-mono-amber">3. Tracing High-Frequency Overhead</text>
              <text x="14" y="44" class="text-p">Logging full prompt payloads to CloudWatch</text>
              <text x="14" y="60" class="text-p">rapidly accumulates gigabytes of ingestion.</text>
              <text x="14" y="82" class="text-mono-green" font-size="11">Mitigate: 10% sampling on successful runs</text>
            </g>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Explain the full production bill. Show students that model tokens are only one component, while vector store floors and observability retention can exceed inference costs.",
        "talkTrack": "Explain the cost model. Model tokens are only one bar. Look at this monthly waterfall: Foundation Model tokens might only be $240, with caching saving $120. But OpenSearch Serverless minimum OCUs add $700, and distributed tracing adds $140. At moderate traffic, your database and logging can cost three times more than your model! Never evaluate an AI platform by raw $/1M token prices alone: calculate the full production footprint.",
        "timing": "100:00 - 105:00 (5 min)"
    }
}
