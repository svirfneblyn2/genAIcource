# Slide 15: Google Cloud Service Map
from ..common_svg import svg_frame
from ..icons import render_icon
from ..logos import render_logo, render_logo_badge

SLIDE_DATA = {
    "index": 15,
    "kicker": "GOOGLE CLOUD ARCHITECTURE",
    "title": "Google Cloud Implementation: Gemini Enterprise Stack",
    "lead": "Orchestrating the assistant with Gemini Enterprise Agent Platform and Vertex AI.",
    "section": "Cloud Implementation: Google Cloud",
    "takeaway": "Google Cloud excels in long-context document grounding, multimodal understanding, and data-warehouse co-location.",
    "svg": svg_frame(f"""<g transform="translate(40, 15)">
        <!-- Layer 1: App & User Interface Lane -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="1040" height="84" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-amber" font-size="10.5">1. APP LAYER</text>

          <!-- Google Chat / Web UI -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="64" rx="5" class="node-box"/>
            {render_icon("chat", 10, 12, size=20, color="#e0c58e")}
            <text x="36" y="24" class="text-h2">Google Chat / Web UI</text>
            <text x="36" y="44" class="text-dim">Workspace Bot &bull; Angular/React</text>
            <text x="36" y="58" class="text-mono-amber" font-size="9">User Session Initiator</text>
          </g>

          <path d="M 365 42 L 405 42" stroke="#e0c58e" stroke-width="1.8" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Cloud Run -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="64" rx="5" class="node-box"/>
            {render_icon("api", 10, 12, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2">Cloud Run</text>
            <text x="36" y="44" class="text-dim">Serverless Containers &bull; VPC Connector</text>
            <text x="36" y="58" class="text-mono-green" font-size="9">Direct Serverless Endpoint</text>
          </g>

          <path d="M 675 42 L 715 42" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Cloud Identity / IAM -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="64" rx="5" class="node-box"/>
            {render_icon("lock", 10, 12, size=20, color="#60a5fa")}
            <text x="36" y="24" class="text-h2">Cloud Identity / IAM</text>
            <text x="36" y="44" class="text-dim">Context-Aware Access &bull; OAuth 2.0</text>
            <text x="36" y="58" class="text-mono" font-size="9" fill="#93c5fd">Google Workspace Identity Scope</text>
          </g>
        </g>

        <!-- Downward Connector: Cloud Run to Gemini Agent Platform -->
        <path d="M 540 74 L 540 88 L 255 88 L 255 106" stroke="#e0c58e" stroke-width="1.8" stroke-dasharray="3 3" fill="none" marker-end="url(#arr-amber)"/>

        <!-- Layer 2: AI Runtime & Logic -->
        <g transform="translate(0, 96)">
          <rect x="0" y="0" width="1040" height="120" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-amber" font-size="10.5">2. AI RUNTIME</text>

          <!-- Gemini Enterprise Agent Platform -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="98" rx="5" class="node-box-active-amber"/>
            {render_icon("agent", 10, 10, size=20, color="#e0c58e")}
            <text x="36" y="24" class="text-h2" fill="#e0c58e">Gemini Agent Platform</text>
            <text x="12" y="46" class="text-dim">Agent Development Kit (ADK)</text>
            <text x="12" y="66" class="text-mono-amber" font-size="10">Multi-turn session engine</text>
            <rect x="8" y="74" width="184" height="18" rx="3" fill="#1b2434"/>
            <text x="100" y="86" text-anchor="middle" class="text-mono-amber" font-size="8">Queries Vertex Search via IAM</text>
          </g>

          <path d="M 365 59 L 405 59" stroke="#e0c58e" stroke-width="1.8" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Gemini 1.5 Flash/Pro with Gemini Logo -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="98" rx="5" class="node-box"/>
            {render_logo("gemini", 10, 10, size=20, color="#e0c58e")}
            <text x="36" y="24" class="text-h2">Gemini 1.5 Flash / Pro</text>
            <text x="12" y="46" class="text-dim">Model Armor (Safety &amp; Defense)</text>
            <text x="12" y="66" class="text-mono-green" font-size="10">1M Context &bull; Native Multimodal</text>
            <rect x="8" y="74" width="234" height="18" rx="3" fill="#2d2516"/>
            <text x="125" y="86" text-anchor="middle" class="text-mono-amber" font-size="8.5">Context Caching: 75% cost savings</text>
          </g>

          <path d="M 675 59 L 715 59" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Cloud Function / Workflows with ServiceNow Logo -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="98" rx="5" class="node-box"/>
            {render_logo("servicenow", 10, 10, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2" fill="#6ee7b7">Cloud Run Functions</text>
            <text x="12" y="46" class="text-dim">Workflows Connector &rarr; ServiceNow</text>
            <text x="12" y="66" class="text-mono-coral" font-size="10">Escalation &amp; Approval Logic</text>
            <rect x="8" y="74" width="279" height="18" rx="3" fill="#14261f"/>
            <text x="147" y="86" text-anchor="middle" class="text-mono-green" font-size="8.5">Deterministic API dispatch with audit</text>
          </g>
        </g>

        <!-- Downward Connector: Gemini Agent to Vertex Search -->
        <path d="M 300 204 L 300 220 L 540 220 L 540 238" stroke="#e0c58e" stroke-width="1.8" stroke-dasharray="3 3" fill="none" marker-end="url(#arr-amber)"/>

        <!-- Layer 3: Content Ingestion Lane -->
        <g transform="translate(0, 228)">
          <rect x="0" y="0" width="1040" height="88" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-amber" font-size="10.5">3. KNOWLEDGE</text>

          <!-- GCS / Drive -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="68" rx="5" class="node-box"/>
            {render_icon("bucket", 10, 12, size=20, color="#e0c58e")}
            <text x="36" y="24" class="text-h2">GCS / Drive</text>
            <text x="36" y="44" class="text-dim">Enterprise Storage &bull; Workspace</text>
            <text x="36" y="60" class="text-mono-amber" font-size="9">Continuous Document Sync</text>
          </g>

          <path d="M 365 44 L 405 44" stroke="#e0c58e" stroke-width="1.8" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Vertex AI Search -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="68" rx="5" class="node-box"/>
            {render_icon("search", 10, 12, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2">Vertex AI Search</text>
            <text x="36" y="44" class="text-dim">Enterprise Grounding &bull; Multi-turn</text>
            <text x="36" y="60" class="text-mono-green" font-size="9">Semantic Chunking &amp; Citations</text>
          </g>

          <path d="M 675 44 L 715 44" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Vertex Vector Search -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="68" rx="5" class="node-box-active-amber"/>
            {render_icon("database", 10, 12, size=20, color="#e0c58e")}
            <text x="36" y="24" class="text-h2" fill="#e0c58e">Vertex Vector / AlloyDB</text>
            <text x="36" y="44" class="text-dim">ScaNN index &bull; Document ACL metadata</text>
            <text x="36" y="60" class="text-mono-amber" font-size="9">High-Scale Vector Grounding</text>
          </g>
        </g>

        <!-- Layer 4: Shared Governance -->
        <g transform="translate(0, 328)">
          <rect x="0" y="0" width="1040" height="78" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-amber" font-size="10.5">4. GOVERNANCE</text>

          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="270" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("monitoring", 10, 10, size=18, color="#60a5fa")}
            <text x="36" y="22" class="text-h2" font-size="12">Cloud Logging &amp; Trace</text>
            <text x="12" y="42" class="text-dim" font-size="10">Vertex AI Telemetry &bull; Latency Spans</text>
          </g>

          <g transform="translate(440, 10)">
            <rect x="0" y="0" width="280" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("evaluation", 10, 10, size=18, color="#b4a4e5")}
            <text x="36" y="22" class="text-h2" font-size="12">Vertex GenAI Evaluation</text>
            <text x="12" y="42" class="text-dim" font-size="10">AutoSxS &bull; Groundedness &bull; Toxicity</text>
          </g>

          <g transform="translate(735, 10)">
            <rect x="0" y="0" width="285" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("shield", 10, 10, size=18, color="#e0c58e")}
            <text x="36" y="22" class="text-h2" font-size="12">Cloud KMS &amp; VPC-SC</text>
            <text x="12" y="42" class="text-dim" font-size="10">Customer Encryption &bull; Perimeters</text>
          </g>
        </g>
      </g>"""),
    "notes": {
        "goal": "Map the benchmark architecture to Google Cloud and Vertex AI. Detail the Gemini Enterprise Agent Platform, Vertex AI Search, and long-context capabilities.",
        "talkTrack": "Demonstrate the Google Cloud counterpart. In the App layer, users connect via Google Chat or Web UI through Cloud Run and Cloud Identity. In the AI Runtime, Gemini Enterprise Agent Platform coordinates inference with Gemini 1.5 Flash or Pro, using context caching for 75% cost reductions, and dispatches ServiceNow actions through Cloud Run Functions. In the Knowledge lane, Vertex AI Search acts as the turnkey grounding layer over Cloud Storage and Workspace documents. Governance is anchored by Cloud Logging and Vertex GenAI Evaluation.",
        "timing": "70:00 - 75:00 (5 min)"
    }
}
