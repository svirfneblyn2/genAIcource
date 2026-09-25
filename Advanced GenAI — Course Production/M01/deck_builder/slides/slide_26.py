# Slide 26: Worked Solution: Benchmark Defense
from ..common_svg import svg_frame
from ..icons import render_icon
from ..logos import render_logo, render_logo_badge

SLIDE_DATA = {
    "index": 26,
    "kicker": "SOLUTION BENCHMARK",
    "title": "Reference Solution: Claims Assistant on Azure AI Foundry",
    "lead": "What an executive-ready architecture decision package looks like.",
    "section": "Solution Benchmark",
    "takeaway": "Technical elegance never outweighs existing enterprise identity, compliance, and procurement inertia.",
    "svg": svg_frame(f"""<g transform="translate(40, 20)">
        <!-- Left Side: Visual Architecture Blueprint -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="530" height="395" rx="8" class="node-box-active" stroke="#b4a4e5"/>
          <rect x="0" y="0" width="530" height="38" rx="8" fill="#221c32"/>
          {render_logo("azure", 14, 9, size=20, color="#b4a4e5")}
          <text x="42" y="25" class="text-h1" fill="#b4a4e5">Azure Reference Architecture (Healthcare BAA)</text>

          <g transform="translate(18, 48)">
            <!-- Layer 1: Ingestion & OCR -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="494" height="62" rx="5" fill="#141c28" stroke="#253245"/>
              <text x="12" y="16" class="text-mono-purple" font-size="9.5">INGESTION &amp; OCR LANE</text>
              
              <!-- Blob Node -->
              <rect x="12" y="24" width="115" height="30" rx="4" fill="#1b2434"/>
              {render_icon("bucket", 16, 29, size=16, color="#b4a4e5")}
              <text x="36" y="44" class="text-mono" font-size="9" fill="#e2e8f0">Azure Blob</text>

              <path d="M 127 39 L 147 39" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>

              <!-- Document Intelligence Node -->
              <rect x="150" y="24" width="332" height="30" rx="4" fill="#1b2434"/>
              {render_icon("tool", 156, 29, size=16, color="#6ee7b7")}
              <text x="178" y="44" class="text-mono" font-size="9" fill="#e2e8f0">Document Intelligence (Healthcare Model)</text>
            </g>

            <path d="M 247 64 L 247 74" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>

            <!-- Layer 2: Knowledge & ACL -->
            <g transform="translate(0, 76)">
              <rect x="0" y="0" width="494" height="52" rx="5" fill="#141c28" stroke="#253245"/>
              <text x="12" y="16" class="text-mono-purple" font-size="9.5">GROUNDED POLICY RETRIEVAL</text>
              
              <rect x="12" y="22" width="470" height="24" rx="4" fill="#1b2434"/>
              {render_icon("search", 16, 26, size=16, color="#b4a4e5")}
              <text x="38" y="38" class="text-mono" font-size="9" fill="#cbd5e1">Azure AI Search (Semantic Rerank &bull; Entra ID ACL Trimming)</text>
            </g>

            <path d="M 247 130 L 247 140" stroke="#b4a4e5" stroke-width="1.5" fill="none" marker-end="url(#arr-purple)"/>

            <!-- Layer 3: Tiered Router & Human Gate -->
            <g transform="translate(0, 142)">
              <rect x="0" y="0" width="494" height="135" rx="5" fill="#141c28" stroke="#253245"/>
              <text x="12" y="16" class="text-mono-purple" font-size="9.5">TIERED INFERENCE &amp; CONFIDENCE ROUTER</text>

              <!-- Foundry Agent Box -->
              <rect x="12" y="24" width="130" height="100" rx="4" fill="#1c1829" stroke="#b4a4e5"/>
              {render_icon("agent", 16, 30, size=16, color="#b4a4e5")}
              <text x="36" y="44" class="text-mono-purple" font-size="9.5">Foundry Agent</text>
              <text x="14" y="66" class="text-dim" font-size="8.5">Evaluates policy</text>
              <text x="14" y="80" class="text-dim" font-size="8.5">match confidence</text>
              <text x="14" y="98" class="text-mono" font-size="8" fill="#93c5fd">&gt; 90% Auto-pass</text>

              <!-- Routes -->
              <!-- Route 1: GPT-4o-mini -->
              <g transform="translate(152, 24)">
                <rect x="0" y="0" width="330" height="30" rx="4" fill="#1b2434" stroke="#253245"/>
                {render_logo("openai", 8, 6, size=18, color="#60a5fa")}
                <text x="30" y="16" class="text-mono" font-size="9" fill="#93c5fd">GPT-4o-mini: Fast code extraction</text>
                <text x="30" y="25" class="text-dim" font-size="8">$0.15/1M &bull; CPT/ICD-10 table parsing</text>
              </g>

              <!-- Route 2: GPT-4o -->
              <g transform="translate(152, 58)">
                <rect x="0" y="0" width="330" height="30" rx="4" fill="#1b2434" stroke="#253245"/>
                {render_logo("openai", 8, 6, size=18, color="#b4a4e5")}
                <text x="30" y="16" class="text-mono-purple" font-size="9">GPT-4o: Deep anomaly reasoning</text>
                <text x="30" y="25" class="text-dim" font-size="8">Diagnostic mismatches &bull; Audit cross-check</text>
              </g>

              <!-- Route 3: Human Gate -->
              <g transform="translate(152, 92)">
                <rect x="0" y="0" width="330" height="32" rx="4" fill="#152420" stroke="#6ee7b7" stroke-width="1.2"/>
                {render_logo("teams", 8, 7, size=18, color="#6ee7b7")}
                <text x="30" y="16" class="text-mono-green" font-size="9">Power Automate &rarr; Teams Card</text>
                <text x="30" y="26" class="text-dim" font-size="8">Nurse review queue if confidence &lt; 90%</text>
              </g>
            </g>

            <!-- Governance Footer -->
            <g transform="translate(0, 286)">
              <rect x="0" y="0" width="494" height="48" rx="4" fill="#172233" stroke="#253245"/>
              <text x="12" y="18" class="text-mono" font-size="9.5">SHARED GOVERNANCE &amp; SECURITY PLANE</text>
              <text x="12" y="36" class="text-dim" font-size="8.5">&bull; App Insights OTel spans &bull; Key Vault CMEK &bull; Content Safety PII filter</text>
            </g>
          </g>
        </g>

        <!-- Right Side: Executive Defense Package -->
        <g transform="translate(555, 0)">
          <rect x="0" y="0" width="485" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="485" height="38" rx="8" fill="#1b2434"/>
          <text x="22" y="25" class="text-h1" fill="#e0c58e">Executive Decision Defense</text>

          <g transform="translate(18, 48)">
            <!-- Chosen Rationale -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="449" height="142" rx="6" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
              <text x="14" y="22" class="text-mono-green" font-size="11">WHY AZURE WAS SELECTED (JUSTIFICATION)</text>
              <text x="14" y="44" class="text-p">&bull; Organization already maintains BAA (HIPAA) on Azure.</text>
              <text x="14" y="66" class="text-p">&bull; Claims reviewers work exclusively in Microsoft Teams &amp; M365.</text>
              <text x="14" y="88" class="text-p">&bull; AI Search semantic reranking delivers 94% recall on policy rules.</text>
              <text x="14" y="110" class="text-p">&bull; Zero new procurement friction or vendor security audits required.</text>
              <text x="14" y="130" class="text-mono-green" font-size="10">Procurement Velocity: 0 Weeks delay (already active)</text>
            </g>

            <!-- Rejected Rationale -->
            <g transform="translate(0, 154)">
              <rect x="0" y="0" width="449" height="175" rx="6" fill="#24191d" stroke="#d98585" stroke-width="1.5"/>
              <text x="14" y="22" class="text-mono-coral" font-size="11">EXPLICITLY REJECTED ALTERNATIVE: AWS BEDROCK</text>
              <text x="14" y="44" class="text-p">&bull; Technical Capability: Bedrock with Claude 3.5 Sonnet is highly</text>
              <text x="14" y="62" class="text-p">  capable of medical extraction and complex reasoning.</text>
              <text x="14" y="84" class="text-p">&bull; Rejection Reason 1: Introducing AWS requires new corporate SecOps</text>
              <text x="14" y="102" class="text-p">  security review and legal BAA procurement (adds 4-6 months delay).</text>
              <text x="14" y="124" class="text-p">&bull; Rejection Reason 2: Lack of native Teams Adaptive Card approval</text>
              <text x="14" y="142" class="text-p">  integration creates unnecessary custom frontend maintenance.</text>
              <text x="14" y="162" class="text-mono-coral" font-size="10">Disqualification: Organizational inertia &gt; technical parity</text>
            </g>
          </g>
        </g>
      </g>"""),
    "notes": {
        "goal": "Show the worked solution as the benchmark quality bar. Demonstrate how an executive-ready package justifies the chosen platform and explicitly disqualifies alternatives.",
        "talkTrack": "Show the worked solution as the quality bar, not as the only correct answer. A good answer has a clear architecture, a cloud rationale, application-owned boundaries, evaluation, and one rejected alternative. Notice how AWS Bedrock was rejected not because its models are bad (Claude 3.5 is exceptional!), but because introducing AWS into a pure Microsoft healthcare organization adds six months of procurement and security delays. Technical elegance never outweighs operational reality.",
        "timing": "135:00 - 145:00 (10 min)"
    }
}
