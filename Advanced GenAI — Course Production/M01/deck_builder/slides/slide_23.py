# Slide 23: Architecture Decision Framework: 5 Core Questions
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 23,
    "kicker": "DECISION METHODOLOGY",
    "title": "The 5-Question Platform Selection Framework",
    "lead": "The structured method for producing an executive-ready architectural recommendation.",
    "section": "Decision Framework",
    "takeaway": "A defensible decision explicitly names the rejected alternative and explains why it was disqualified.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Funnel Step 1 -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="1040" height="65" rx="6" class="node-box"/>
          <circle cx="30" cy="32" r="16" fill="#1e2c42" stroke="#60a5fa" stroke-width="1.5"/>
          <text x="30" y="37" text-anchor="middle" class="text-mono" font-size="12">Q1</text>
          <text x="65" y="26" class="text-h2" fill="#60a5fa">Workload Pattern &amp; Interaction Shape</text>
          <text x="65" y="48" class="text-p">Is this a deterministic policy FAQ, complex multimodal document parser, or autonomous multi-step agent?</text>
          <rect x="850" y="16" width="170" height="32" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="935" y="36" text-anchor="middle" class="text-mono" font-size="11">Drives: Runtime Choice</text>
        </g>

        <!-- Funnel Step 2 -->
        <g transform="translate(0, 75)">
          <rect x="0" y="0" width="1040" height="65" rx="6" class="node-box"/>
          <circle cx="30" cy="32" r="16" fill="#162924" stroke="#6ee7b7" stroke-width="1.5"/>
          <text x="30" y="37" text-anchor="middle" class="text-mono-green" font-size="12">Q2</text>
          <text x="65" y="26" class="text-h2" fill="#6ee7b7">Data Gravity, Residency &amp; Document ACLs</text>
          <text x="65" y="48" class="text-p">Where do source documents currently reside (S3, SharePoint, BigQuery)? What are cross-border compliance boundaries?</text>
          <rect x="850" y="16" width="170" height="32" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="935" y="36" text-anchor="middle" class="text-mono-green" font-size="11">Drives: Cloud Gravity</text>
        </g>

        <!-- Funnel Step 3 -->
        <g transform="translate(0, 150)">
          <rect x="0" y="0" width="1040" height="65" rx="6" class="node-box"/>
          <circle cx="30" cy="32" r="16" fill="#221c32" stroke="#b4a4e5" stroke-width="1.5"/>
          <text x="30" y="37" text-anchor="middle" class="text-mono-purple" font-size="12">Q3</text>
          <text x="65" y="26" class="text-h2" fill="#b4a4e5">Model Capability Tier &amp; Context Window</text>
          <text x="65" y="48" class="text-p">Does the application require 1M+ context (Gemini), enterprise Claude (Bedrock), or OpenAI reasoning models (Foundry)?</text>
          <rect x="850" y="16" width="170" height="32" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="935" y="36" text-anchor="middle" class="text-mono-purple" font-size="11">Drives: Model Selection</text>
        </g>

        <!-- Funnel Step 4 -->
        <g transform="translate(0, 225)">
          <rect x="0" y="0" width="1040" height="65" rx="6" class="node-box"/>
          <circle cx="30" cy="32" r="16" fill="#2d2516" stroke="#e0c58e" stroke-width="1.5"/>
          <text x="30" y="37" text-anchor="middle" class="text-mono-amber" font-size="12">Q4</text>
          <text x="65" y="26" class="text-h2" fill="#e0c58e">Enterprise Identity &amp; Observability Baseline</text>
          <text x="65" y="48" class="text-p">Which identity provider (Entra ID vs AWS IAM) and tracing standard (OpenTelemetry) are approved by corporate SecOps?</text>
          <rect x="850" y="16" width="170" height="32" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="935" y="36" text-anchor="middle" class="text-mono-amber" font-size="11">Drives: Governance Fit</text>
        </g>

        <!-- Funnel Step 5 -->
        <g transform="translate(0, 300)">
          <rect x="0" y="0" width="1040" height="65" rx="6" class="node-box-active" stroke="#d98585"/>
          <circle cx="30" cy="32" r="16" fill="#2d1c22" stroke="#d98585" stroke-width="1.5"/>
          <text x="30" y="37" text-anchor="middle" class="text-mono-coral" font-size="12">Q5</text>
          <text x="65" y="26" class="text-h2" fill="#d98585">Operational Team Profile &amp; Operator Burden</text>
          <text x="65" y="48" class="text-p">Can the team maintain custom Kubernetes clusters and vLLM GPU servers, or does the workload require serverless SaaS?</text>
          <rect x="850" y="16" width="170" height="32" rx="4" fill="#24191d" stroke="#d98585" stroke-width="1.2"/>
          <text x="935" y="36" text-anchor="middle" class="text-mono-coral" font-size="11">Drives: SaaS vs Self-Host</text>
        </g>

        <!-- Mandatory Rule Footer Banner -->
        <g transform="translate(0, 375)">
          <rect x="0" y="0" width="1040" height="32" rx="4" fill="#1a2538" stroke="#3b82f6"/>
          <text x="520" y="21" text-anchor="middle" class="text-mono" font-size="11">MANDATORY DEFENSE RULE: MUST EXPLICITLY NAME AND DISQUALIFY ONE REJECTED ALTERNATIVE</text>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Present the five-question decision framework. Train students to produce an executive-ready architectural recommendation with an explicit rejected alternative.",
        "talkTrack": "Present the five-question decision framework. Ask students to use it in the workshop: workload, data boundary, model class, observability, and operator. Require one rejected alternative so the decision is not cosmetic. An architecture recommendation that says 'Cloud X is great' gets rejected by leadership; an architecture recommendation that says 'We chose Cloud X because of identity and data gravity, and explicitly rejected Cloud Y because of vector cost floors and procurement friction' wins immediate approval.",
        "timing": "110:00 - 115:00 (5 min)"
    }
}
