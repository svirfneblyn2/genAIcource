# Slide 16: Google Cloud: Selection Rationale & Watch-Outs
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 16,
    "kicker": "DECISION LOGIC: GOOGLE CLOUD",
    "title": "When Google Cloud is the Strongest Choice",
    "lead": "Analytics synergy, context length supremacy, and platform evolution.",
    "section": "Decision Logic: Google Cloud",
    "takeaway": "Choose Google Cloud when the assistant intersects directly with BigQuery analytics, complex multimodal inputs, or long-context grounding.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Left Card: Architectural Alignment & Strengths -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="505" height="395" rx="8" class="node-box-active" stroke="#e0c58e"/>
          <rect x="0" y="0" width="505" height="46" rx="8" fill="#2d2516"/>
          {render_icon("approval", 16, 11, size=24, color="#e0c58e")}
          <text x="48" y="30" class="text-h1" fill="#e0c58e">Why Choose Google Cloud?</text>
          
          <g transform="translate(20, 60)">
            <!-- Point 1 -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">1. BigQuery Lakehouse Co-location</text>
              <text x="14" y="42" class="text-p">If enterprise operational tables, customer service logs, and</text>
              <text x="14" y="60" class="text-dim">analytics live in BigQuery, Vertex AI provides zero-ETL grounding.</text>
            </g>

            <!-- Point 2 -->
            <g transform="translate(0, 80)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">2. 1M-2M Native Context &amp; Caching</text>
              <text x="14" y="42" class="text-p">Gemini native context windows allow entire equipment manuals</text>
              <text x="14" y="60" class="text-dim">or codebases to be cached in memory with up to 75% cost reduction.</text>
            </g>

            <!-- Point 3 -->
            <g transform="translate(0, 160)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#6ee7b7">3. Superior Flash Tier Unit Economics</text>
              <text x="14" y="42" class="text-p">Gemini 1.5 Flash delivers sub-second TTFT at pricing</text>
              <text x="14" y="60" class="text-dim">dramatically below comparable enterprise reasoning models.</text>
            </g>

            <!-- Bottom summary box -->
            <g transform="translate(0, 240)">
              <rect x="0" y="0" width="465" height="78" rx="6" fill="#221e16" stroke="#e0c58e" stroke-width="1.2"/>
              <text x="14" y="24" class="text-mono-amber" font-size="11">ORGANIZATIONAL ALIGNMENT</text>
              <text x="14" y="46" class="text-p">Strongest for data-engineering and analytics-heavy firms that</text>
              <text x="14" y="64" class="text-dim">already run their primary data warehouse on Google Cloud Platform.</text>
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
              <text x="14" y="22" class="text-h2" fill="#d98585">1. Rapid Product Rebranding Pace</text>
              <text x="14" y="42" class="text-p">Transitions from Duet AI to Gemini Enterprise to Vertex Search</text>
              <text x="14" y="60" class="text-dim">create documentation churn and API parameter deprecations.</text>
            </g>

            <!-- Watch-out 2 -->
            <g transform="translate(0, 80)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">2. Regional Parity &amp; Model Rollout</text>
              <text x="14" y="42" class="text-p">New Gemini checkpoints deploy first to us-central1; European</text>
              <text x="14" y="60" class="text-dim">and Asian regions often lag by several weeks or months.</text>
            </g>

            <!-- Watch-out 3 -->
            <g transform="translate(0, 160)">
              <rect x="0" y="0" width="465" height="72" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="14" y="22" class="text-h2" fill="#d98585">3. Active Directory / Entra ID Friction</text>
              <text x="14" y="42" class="text-p">Federating legacy Windows Active Directory into Cloud Identity</text>
              <text x="14" y="60" class="text-dim">requires building and maintaining SAML/SCIM identity bridges.</text>
            </g>

            <!-- Bottom mitigation box -->
            <g transform="translate(0, 240)">
              <rect x="0" y="0" width="465" height="78" rx="6" fill="#24191d" stroke="#d98585" stroke-width="1.2"/>
              <text x="14" y="24" class="text-mono-coral" font-size="11">ARCHITECTURAL MITIGATION</text>
              <text x="14" y="46" class="text-p">Deploy Workload Identity Federation for clean token exchange</text>
              <text x="14" y="64" class="text-dim">and explicitly lock model endpoint versions in Terraform.</text>
            </g>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Explain Google Cloud selection logic. Emphasize BigQuery analytics synergy, context length advantages, and warn about regional rollout differences.",
        "talkTrack": "Explain Google Cloud selection logic. It is especially strong when the assistant is tied to analytics, BigQuery, search/grounding, data engineering, or Google Cloud-native workflows. The ability to pass 1M tokens into Gemini 1.5 Flash at low cost is a game-changer for document-heavy enterprises. However, warn students that product rebranding moves fast, and they must verify regional model availability before committing to European or APAC data boundaries.",
        "timing": "75:00 - 80:00 (5 min)"
    }
}
