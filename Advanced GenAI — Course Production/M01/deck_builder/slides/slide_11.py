# Slide 11: AWS Service Map for the Support Assistant
from ..common_svg import svg_frame
from ..icons import render_icon
from ..logos import render_logo, render_logo_badge

SLIDE_DATA = {
    "index": 11,
    "kicker": "AWS BEDROCK ARCHITECTURE",
    "title": "AWS Implementation: Bedrock-Centered Stack",
    "lead": "How AWS services implement the two-lane support assistant topology.",
    "section": "Cloud Implementation: AWS",
    "takeaway": "AWS provides a seamless serverless AI stack when coupled with existing AWS IAM and VPC infrastructure.",
    "svg": svg_frame(f"""<g transform="translate(40, 15)">
        <!-- Layer 1: App & User Interface Lane -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="1040" height="84" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono" font-size="10.5">1. APP LAYER</text>

          <!-- Frontend UI -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="64" rx="5" class="node-box"/>
            {render_icon("browser", 10, 12, size=20, color="#60a5fa")}
            <text x="36" y="24" class="text-h2">Next.js / Connect</text>
            <text x="36" y="44" class="text-dim">Enterprise Web UI &bull; Telephony</text>
            <text x="36" y="58" class="text-mono" font-size="9" fill="#93c5fd">User Session Initiator</text>
          </g>

          <path d="M 365 42 L 405 42" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

          <!-- API Gateway -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="64" rx="5" class="node-box"/>
            {render_icon("api", 10, 12, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2">Amazon API Gateway</text>
            <text x="36" y="44" class="text-dim">Rate Limiting &bull; REST Endpoints</text>
            <text x="36" y="58" class="text-mono-green" font-size="9">mTLS &amp; Private VPC Link</text>
          </g>

          <path d="M 675 42 L 715 42" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Cognito / IAM Auth -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="64" rx="5" class="node-box"/>
            {render_icon("lock", 10, 12, size=20, color="#e0c58e")}
            <text x="36" y="24" class="text-h2">Amazon Cognito / IAM</text>
            <text x="36" y="44" class="text-dim">Corporate IdP Federation &bull; JWT Auth</text>
            <text x="36" y="58" class="text-mono-amber" font-size="9">Claims Principal Validation</text>
          </g>
        </g>

        <!-- Downward Connector: API Gateway to AI Runtime Agent -->
        <path d="M 540 74 L 540 88 L 255 88 L 255 106" stroke="#60a5fa" stroke-width="1.8" stroke-dasharray="3 3" fill="none" marker-end="url(#arr-blue)"/>

        <!-- Layer 2: AI Runtime & Agent Core -->
        <g transform="translate(0, 96)">
          <rect x="0" y="0" width="1040" height="120" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono" font-size="10.5">2. AI RUNTIME</text>

          <!-- Bedrock Agent Core -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="98" rx="5" class="node-box-active"/>
            {render_icon("agent", 10, 10, size=20, color="#60a5fa")}
            <text x="36" y="24" class="text-h2" fill="#60a5fa">Bedrock Agent</text>
            <text x="12" y="46" class="text-dim">Bedrock AgentCore Runtime</text>
            <text x="12" y="66" class="text-mono" font-size="10">Orchestration &amp; Memory</text>
            <rect x="8" y="74" width="184" height="18" rx="3" fill="#172233"/>
            <text x="100" y="86" text-anchor="middle" class="text-mono" font-size="8.5" fill="#93c5fd">Invokes KB via PrivateLink</text>
          </g>

          <!-- Horizontal Arrow Agent to Model -->
          <path d="M 365 59 L 405 59" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Claude 3.5 Sonnet with Anthropic Logo -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="98" rx="5" class="node-box"/>
            {render_logo("anthropic", 10, 10, size=20, color="#d98585")}
            <text x="36" y="24" class="text-h2">Claude 3.5 Sonnet</text>
            <text x="12" y="46" class="text-dim">Bedrock Guardrails (PII filter)</text>
            <text x="12" y="66" class="text-mono-purple" font-size="10">Prompt Cache: 80% cost saved</text>
            <rect x="8" y="74" width="234" height="18" rx="3" fill="#221727"/>
            <text x="125" y="86" text-anchor="middle" class="text-mono-purple" font-size="8.5">Zero Data Retention (AWS SLA)</text>
          </g>

          <!-- Horizontal Arrow Model to Action Group -->
          <path d="M 675 59 L 715 59" stroke="#b4a4e5" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)"/>

          <!-- AWS Lambda Action Group with ServiceNow Logo -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="98" rx="5" class="node-box"/>
            {render_logo("servicenow", 10, 10, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2" fill="#6ee7b7">Lambda Action Group</text>
            <text x="12" y="46" class="text-dim">Confirmation Gate &rarr; ServiceNow API</text>
            <text x="12" y="66" class="text-mono-coral" font-size="10">Human-in-the-Loop Enforced</text>
            <rect x="8" y="74" width="279" height="18" rx="3" fill="#14261f"/>
            <text x="147" y="86" text-anchor="middle" class="text-mono-green" font-size="8.5">Deterministic API dispatch with audit</text>
          </g>
        </g>

        <!-- Downward Connector: Bedrock Agent to Knowledge Bases -->
        <path d="M 300 204 L 300 220 L 540 220 L 540 238" stroke="#6ee7b7" stroke-width="1.8" stroke-dasharray="3 3" fill="none" marker-end="url(#arr-green)"/>

        <!-- Layer 3: Enterprise Knowledge & Retrieval Lane -->
        <g transform="translate(0, 228)">
          <rect x="0" y="0" width="1040" height="88" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-green" font-size="10.5">3. KNOWLEDGE</text>

          <!-- S3 -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="68" rx="5" class="node-box"/>
            {render_icon("bucket", 10, 12, size=20, color="#60a5fa")}
            <text x="36" y="24" class="text-h2">Amazon S3</text>
            <text x="36" y="44" class="text-dim">Policy PDFs &amp; S3 ACL tags</text>
            <text x="36" y="60" class="text-mono" font-size="9" fill="#93c5fd">Offline Document Store</text>
          </g>

          <path d="M 365 44 L 405 44" stroke="#60a5fa" stroke-width="1.8" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Knowledge Bases -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="68" rx="5" class="node-box"/>
            {render_icon("tool", 10, 12, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2">Knowledge Bases for Bedrock</text>
            <text x="36" y="44" class="text-dim">Titan Embeddings V2 &bull; Auto-chunk</text>
            <text x="36" y="60" class="text-mono-green" font-size="9">Managed Vector Ingestion</text>
          </g>

          <path d="M 675 44 L 715 44" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- OpenSearch Serverless -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="68" rx="5" class="node-box-active"/>
            {render_icon("database", 10, 12, size=20, color="#60a5fa")}
            <text x="36" y="24" class="text-h2" fill="#60a5fa">OpenSearch Serverless</text>
            <text x="36" y="44" class="text-dim">Vector Collection &bull; Metadata Filter</text>
            <text x="36" y="60" class="text-mono" font-size="9" fill="#93c5fd">Hybrid Dense + Lexical Index</text>
          </g>
        </g>

        <!-- Layer 4: Shared Governance -->
        <g transform="translate(0, 328)">
          <rect x="0" y="0" width="1040" height="78" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono" font-size="10.5">4. GOVERNANCE</text>

          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="270" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("monitoring", 10, 10, size=18, color="#60a5fa")}
            <text x="36" y="22" class="text-h2" font-size="12">Amazon CloudWatch</text>
            <text x="12" y="42" class="text-dim" font-size="10">OTel Traces &bull; Token Usage Metrics</text>
          </g>

          <g transform="translate(440, 10)">
            <rect x="0" y="0" width="280" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("evaluation", 10, 10, size=18, color="#b4a4e5")}
            <text x="36" y="22" class="text-h2" font-size="12">Bedrock Model Evaluation</text>
            <text x="12" y="42" class="text-dim" font-size="10">Faithfulness &bull; Groundedness Scoring</text>
          </g>

          <g transform="translate(735, 10)">
            <rect x="0" y="0" width="285" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("shield", 10, 10, size=18, color="#e0c58e")}
            <text x="36" y="22" class="text-h2" font-size="12">AWS KMS &amp; IAM Policy</text>
            <text x="12" y="42" class="text-dim" font-size="10">Customer-Managed Keys &bull; Least Privilege</text>
          </g>
        </g>
      </g>"""),
    "notes": {
        "goal": "Map each conceptual block from the benchmark architecture to concrete AWS services. Show how S3, Bedrock KB, OpenSearch Serverless, Bedrock Agents, Claude 3.5, and CloudWatch form a cohesive stack.",
        "talkTrack": "Walk through the four swimlanes top to bottom. In the App layer, users connect via web or telephony through API Gateway and Cognito. In the AI Runtime, Bedrock Agent orchestrates the flow: retrieving chunks from KB, calling Claude 3.5 Sonnet for synthesis, and triggering Lambda action groups with explicit confirmation gates before touching ServiceNow. In the Content lane, raw PDFs in S3 are chunked and embedded by Bedrock Knowledge Bases into OpenSearch Serverless. Across the bottom, CloudWatch and IAM provide shared telemetry and access control.",
        "timing": "50:00 - 55:00 (5 min)"
    }
}
