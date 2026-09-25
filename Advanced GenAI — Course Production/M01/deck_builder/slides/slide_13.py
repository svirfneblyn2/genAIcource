# Slide 13: Microsoft Azure / Foundry Service Map
from ..common_svg import svg_frame
from ..icons import render_icon
from ..logos import render_logo, render_logo_badge

SLIDE_DATA = {
    "index": 13,
    "kicker": "AZURE AI FOUNDRY ARCHITECTURE",
    "title": "Azure Implementation: Foundry & AI Search Stack",
    "lead": "Deploying the support assistant on the Microsoft enterprise ecosystem.",
    "section": "Cloud Implementation: Azure",
    "takeaway": "Azure AI Foundry delivers the tightest integration with Microsoft 365, SharePoint, and corporate Entra ID.",
    "svg": svg_frame(f"""<g transform="translate(40, 15)">
        <!-- Layer 1: App & User Interface Lane -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="1040" height="84" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-purple" font-size="10.5">1. APP LAYER</text>

          <!-- Teams Bot -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="64" rx="5" class="node-box"/>
            {render_logo("teams", 10, 12, size=20, color="#b4a4e5")}
            <text x="36" y="24" class="text-h2">Teams Bot / Power App</text>
            <text x="36" y="44" class="text-dim">Native M365 Desktop &amp; Mobile UI</text>
            <text x="36" y="58" class="text-mono-purple" font-size="9">User Session Initiator</text>
          </g>

          <path d="M 365 42 L 405 42" stroke="#b4a4e5" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)"/>

          <!-- Azure App Service -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="64" rx="5" class="node-box"/>
            {render_icon("api", 10, 12, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2">Azure App Service</text>
            <text x="36" y="44" class="text-dim">Container Apps &bull; Private VNet</text>
            <text x="36" y="58" class="text-mono-green" font-size="9">Managed VNet Private Link</text>
          </g>

          <path d="M 675 42 L 715 42" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Microsoft Entra ID -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="64" rx="5" class="node-box"/>
            {render_icon("lock", 10, 12, size=20, color="#60a5fa")}
            <text x="36" y="24" class="text-h2">Microsoft Entra ID</text>
            <text x="36" y="44" class="text-dim">Corporate Claims Principal &bull; SSO</text>
            <text x="36" y="58" class="text-mono" font-size="9" fill="#93c5fd">Enterprise Token &amp; ACL Scope</text>
          </g>
        </g>

        <!-- Downward Connector: App Service to Foundry Agent -->
        <path d="M 540 74 L 540 88 L 255 88 L 255 106" stroke="#b4a4e5" stroke-width="1.8" stroke-dasharray="3 3" fill="none" marker-end="url(#arr-purple)"/>

        <!-- Layer 2: AI Runtime & Logic -->
        <g transform="translate(0, 96)">
          <rect x="0" y="0" width="1040" height="120" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-purple" font-size="10.5">2. AI RUNTIME</text>

          <!-- Foundry Agent -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="98" rx="5" class="node-box-active-purple"/>
            {render_icon("agent", 10, 10, size=20, color="#b4a4e5")}
            <text x="36" y="24" class="text-h2" fill="#b4a4e5">Foundry Agent</text>
            <text x="12" y="46" class="text-dim">Agent Service SDK</text>
            <text x="12" y="66" class="text-mono-purple" font-size="10">Thread State &amp; Sessions</text>
            <rect x="8" y="74" width="184" height="18" rx="3" fill="#1b2434"/>
            <text x="100" y="86" text-anchor="middle" class="text-mono-purple" font-size="8">Queries AI Search via Identity</text>
          </g>

          <path d="M 365 59 L 405 59" stroke="#b4a4e5" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)"/>

          <!-- GPT-4o with OpenAI Logo -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="98" rx="5" class="node-box"/>
            {render_logo("openai", 10, 10, size=20, color="#60a5fa")}
            <text x="36" y="24" class="text-h2">GPT-4o / 4o-mini</text>
            <text x="12" y="46" class="text-dim">Azure AI Content Safety (Filters)</text>
            <text x="12" y="66" class="text-mono-green" font-size="10">Prompt Caching: 50% discount</text>
            <rect x="8" y="74" width="234" height="18" rx="3" fill="#172233"/>
            <text x="125" y="86" text-anchor="middle" class="text-mono" font-size="8.5">Provisioned Throughput (PTU)</text>
          </g>

          <path d="M 675 59 L 715 59" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Azure Function / Logic Apps with ServiceNow Logo -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="98" rx="5" class="node-box"/>
            {render_logo("servicenow", 10, 10, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2" fill="#6ee7b7">Functions / Logic Apps</text>
            <text x="12" y="46" class="text-dim">ServiceNow Connector &bull; Teams Approval</text>
            <text x="12" y="66" class="text-mono-coral" font-size="10">Adaptive Card Approval Gate</text>
            <rect x="8" y="74" width="279" height="18" rx="3" fill="#14261f"/>
            <text x="147" y="86" text-anchor="middle" class="text-mono-green" font-size="8.5">Direct M365 actionable cards in Teams</text>
          </g>
        </g>

        <!-- Downward Connector: Foundry Agent to AI Search -->
        <path d="M 300 204 L 300 220 L 872 220 L 872 238" stroke="#b4a4e5" stroke-width="1.8" stroke-dasharray="3 3" fill="none" marker-end="url(#arr-purple)"/>

        <!-- Layer 3: Content Ingestion Lane -->
        <g transform="translate(0, 228)">
          <rect x="0" y="0" width="1040" height="88" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-purple" font-size="10.5">3. KNOWLEDGE</text>

          <!-- Blob / SharePoint -->
          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="200" height="68" rx="5" class="node-box"/>
            {render_icon("bucket", 10, 12, size=20, color="#b4a4e5")}
            <text x="36" y="24" class="text-h2">Blob / SharePoint</text>
            <text x="36" y="44" class="text-dim">M365 Connectors &bull; Policy Docs</text>
            <text x="36" y="60" class="text-mono-purple" font-size="9">Enterprise Storage Sync</text>
          </g>

          <path d="M 365 44 L 405 44" stroke="#b4a4e5" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)"/>

          <!-- Document Intelligence -->
          <g transform="translate(415, 10)">
            <rect x="0" y="0" width="250" height="68" rx="5" class="node-box"/>
            {render_icon("tool", 10, 12, size=20, color="#6ee7b7")}
            <text x="36" y="24" class="text-h2">Document Intelligence</text>
            <text x="36" y="44" class="text-dim">Layout OCR &bull; text-embedding-3</text>
            <text x="36" y="60" class="text-mono-green" font-size="9">Table Structure &amp; Layout Parse</text>
          </g>

          <path d="M 675 44 L 715 44" stroke="#6ee7b7" stroke-width="1.8" fill="none" marker-end="url(#arr-green)"/>

          <!-- Azure AI Search -->
          <g transform="translate(725, 10)">
            <rect x="0" y="0" width="295" height="68" rx="5" class="node-box-active-purple"/>
            {render_icon("search", 10, 12, size=20, color="#b4a4e5")}
            <text x="36" y="24" class="text-h2" fill="#b4a4e5">Azure AI Search</text>
            <text x="36" y="44" class="text-dim">Semantic Reranker &bull; Entra ID ACL tags</text>
            <text x="36" y="60" class="text-mono-purple" font-size="9">Cross-Encoder Hybrid Index</text>
          </g>
        </g>

        <!-- Layer 4: Shared Governance -->
        <g transform="translate(0, 328)">
          <rect x="0" y="0" width="1040" height="78" rx="6" class="swimlane-bg"/>
          <rect x="10" y="10" width="130" height="22" rx="4" fill="#1b2434"/>
          <text x="18" y="25" class="text-mono-purple" font-size="10.5">4. GOVERNANCE</text>

          <g transform="translate(155, 10)">
            <rect x="0" y="0" width="270" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("monitoring", 10, 10, size=18, color="#60a5fa")}
            <text x="36" y="22" class="text-h2" font-size="12">Azure Monitor / Insights</text>
            <text x="12" y="42" class="text-dim" font-size="10">Application Insights &bull; OTel Spans</text>
          </g>

          <g transform="translate(440, 10)">
            <rect x="0" y="0" width="280" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("evaluation", 10, 10, size=18, color="#b4a4e5")}
            <text x="36" y="22" class="text-h2" font-size="12">Foundry Model Evaluations</text>
            <text x="12" y="42" class="text-dim" font-size="10">Groundedness &bull; Relevance &bull; Safety</text>
          </g>

          <g transform="translate(735, 10)">
            <rect x="0" y="0" width="285" height="58" rx="5" fill="#141c28" stroke="#253245"/>
            {render_icon("shield", 10, 10, size=18, color="#e0c58e")}
            <text x="36" y="22" class="text-h2" font-size="12">Azure Key Vault &amp; Entra RBAC</text>
            <text x="12" y="42" class="text-dim" font-size="10">Customer-Managed Keys &bull; Principals</text>
          </g>
        </g>
      </g>"""),
    "notes": {
        "goal": "Map each conceptual block to Azure AI Foundry, Azure AI Search, GPT-4o, and Microsoft 365 integration points.",
        "talkTrack": "Show how Azure implements the identical four-lane architecture with Microsoft ecosystem tooling. In the App layer, users connect via Teams Bot or Power App through App Service and Entra ID. In the AI Runtime, Foundry Agent orchestrates the flow with GPT-4o, triggering Azure Functions or Logic Apps for ServiceNow actions with adaptive card approval in Teams. In the Knowledge lane, Document Intelligence parses PDFs with OCR and table awareness into Azure AI Search. Governance is anchored by Application Insights and Azure Key Vault.",
        "timing": "60:00 - 65:00 (5 min)"
    }
}
