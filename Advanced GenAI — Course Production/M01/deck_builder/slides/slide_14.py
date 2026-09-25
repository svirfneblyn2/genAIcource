# Slide 14: Azure: Selection Rationale & Watch-Outs
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 14,
    "kicker": "DECISION LOGIC: AZURE",
    "title": "When Azure AI Foundry is the Strongest Choice",
    "lead": "Corporate identity fit, M365 synergy, and architectural trade-offs.",
    "section": "Decision Logic: Azure",
    "takeaway": "Choose Azure when corporate identity is Entra ID and knowledge documents are distributed across Microsoft 365 repositories.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Left Card: Architectural Alignment & Strengths -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="505" height="395" rx="8" class="node-box-active" stroke="#b4a4e5"/>
          <rect x="0" y="0" width="505" height="46" rx="8" fill="#221c32"/>
          {render_icon("approval", 16, 11, size=24, color="#b4a4e5")}
          <text x="48" y="30" class="text-h1" fill="#b4a4e5">Why Choose Azure AI Foundry?</text>
          
          <g transform="translate(20, 60)">
            <!-- Point 1 -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">1. Native Microsoft Entra ID Trimming</text>
              <text x="14" y="42" class="text-p">Pass corporate JWT tokens directly into Azure AI Search: automatically</text>
              <text x="14" y="60" class="text-dim">enforces SharePoint document ACLs without custom sync scripts.</text>
            </g>

            <!-- Point 2 -->
            <g transform="translate(0, 80)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">2. Enterprise OpenAI Models &amp; SLAs</text>
              <text x="14" y="42" class="text-p">Priority access to GPT-4o, o1, and o3 with strict data guarantees:</text>
              <text x="14" y="60" class="text-dim">zero training on customer data and private virtual network endpoints.</text>
            </g>

            <!-- Point 3 -->
            <g transform="translate(0, 160)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">3. Single Pane of Glass in Foundry</text>
              <text x="14" y="42" class="text-p">Unified portal consolidating model catalog, prompt playground,</text>
              <text x="14" y="60" class="text-dim">agent workflows, automated evaluations, and App Insights tracing.</text>
            </g>

            <!-- Bottom summary box -->
            <g transform="translate(0, 240)">
              <rect x="0" y="0" width="465" height="78" rx="6" fill="#1b1c30" stroke="#b4a4e5" stroke-width="1.2"/>
              <text x="14" y="24" class="text-mono-purple" font-size="11">ORGANIZATIONAL ALIGNMENT</text>
              <text x="14" y="46" class="text-p">Strongest for M365 enterprises: lowest friction path to launch</text>
              <text x="14" y="64" class="text-dim">grounded assistants inside Teams and Power Platform environments.</text>
            </g>
          </g>
        </g>

        <!-- Right Card: Watch-outs & Architectural Constraints -->
        <g transform="translate(535, 0)">
          <rect x="0" y="0" width="505" height="395" rx="8" class="node-box" stroke="#d98585"/>
          <rect x="0" y="0" width="505" height="46" rx="8" fill="#2d1c22"/>
          {render_icon("alert", 16, 11, size=24, color="#d98585")}
          <text x="48" y="30" class="text-h1" fill="#d98585">Watch-Outs &amp; Operational Gotchas</text>
          
          <g transform="translate(20, 60)">
            <!-- Watch-out 1 -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">1. Brand &amp; Portal Renaming Churn</text>
              <text x="14" y="42" class="text-p">Fast product renaming (Azure OpenAI &rarr; AI Studio &rarr; AI Foundry)</text>
              <text x="14" y="60" class="text-dim">creates portal navigation churn and Python SDK version drift.</text>
            </g>

            <!-- Watch-out 2 -->
            <g transform="translate(0, 80)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">2. PTU Booking &amp; Regional Quotas</text>
              <text x="14" y="42" class="text-p">Provisioned Throughput Units (PTUs) carry high monthly financial</text>
              <text x="14" y="60" class="text-dim">commitments: pay-per-token tier subject to strict TPM quota limits.</text>
            </g>

            <!-- Watch-out 3 -->
            <g transform="translate(0, 160)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">3. Azure AI Search Service Tier Costs</text>
              <text x="14" y="42" class="text-p">Semantic search features require Standard (S1) tier or higher,</text>
              <text x="14" y="60" class="text-dim">creating a ~$250/mo baseline cost before query volume ramps up.</text>
            </g>

            <!-- Bottom mitigation box -->
            <g transform="translate(0, 240)">
              <rect x="0" y="0" width="465" height="78" rx="6" fill="#24191d" stroke="#d98585" stroke-width="1.2"/>
              <text x="14" y="24" class="text-mono-coral" font-size="11">ARCHITECTURAL MITIGATION</text>
              <text x="14" y="46" class="text-p">Pin exact SDK versions (azure-ai-projects) and utilize</text>
              <text x="14" y="64" class="text-dim">Global Standard deployments to maximize throughput elasticity.</text>
            </g>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Explain Azure selection logic. Detail how Entra ID integration and M365 make Azure the default choice for Windows/Active Directory enterprises.",
        "talkTrack": "Explain Azure selection logic. If the company already uses Microsoft identity, M365, Azure governance, and Azure data/services, Azure often becomes the lowest-friction path to a governed GenAI pilot and production rollout. Passing Entra ID security tokens directly into Azure AI Search for document-level trimming avoids rebuilding authentication from scratch. Warn students about PTU quotas and the ongoing naming transitions across Azure AI portals.",
        "timing": "65:00 - 70:00 (5 min)"
    }
}
