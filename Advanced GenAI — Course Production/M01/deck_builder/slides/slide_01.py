# Slide 01: Course Title & Architectural Roadmap
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 1,
    "kicker": "ADVANCED GENAI | MODULE 01 - CLOUD AI CAPABILITIES",
    "title": "Cloud AI Capabilities Overview: Enterprise Architecture",
    "lead": "Navigating AWS Bedrock, Azure AI Foundry, and Google Cloud for production GenAI.",
    "section": "Architecture Overview",
    "takeaway": "Enterprise GenAI is an architecture decision, not a vendor brand choice.",
    "svg": svg_frame(f"""
      <!-- Pipeline stages -->
      <g transform="translate(40, 45)">
        <!-- Stage 1 -->
        <rect x="0" y="0" width="220" height="220" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="220" height="38" rx="8" fill="#1e2c42"/>
        <text x="110" y="24" text-anchor="middle" class="text-h1" fill="#60a5fa">1. Workload Scope</text>
        {render_icon("document", 20, 55, size=22, color="#60a5fa")}
        <text x="52" y="72" class="text-h2">Business Contract</text>
        <text x="20" y="105" class="text-p">Grounded Support FAQ</text>
        <text x="20" y="128" class="text-p">Identity &amp; ACL Rules</text>
        <text x="20" y="151" class="text-p">Ticket Approval Gate</text>
        <rect x="18" y="172" width="184" height="28" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="110" y="191" text-anchor="middle" class="text-mono">Zero Platform Assumptions</text>
      </g>

      <path d="M 270 155 L 305 155" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

      <g transform="translate(315, 45)">
        <!-- Stage 2 -->
        <rect x="0" y="0" width="220" height="220" rx="8" class="node-box"/>
        <rect x="0" y="0" width="220" height="38" rx="8" fill="#1b2434"/>
        <text x="110" y="24" text-anchor="middle" class="text-h1" fill="#e2e8f0">2. Dual-Lane Topology</text>
        {render_icon("pipeline", 20, 55, size=22, color="#6ee7b7")}
        <text x="52" y="72" class="text-h2">Architectural Isolation</text>
        <text x="20" y="105" class="text-p">Offline Ingestion Lane</text>
        <text x="20" y="128" class="text-p">Online Request Lane</text>
        <text x="20" y="151" class="text-p">Security Policy Checks</text>
        <rect x="18" y="172" width="184" height="28" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="110" y="191" text-anchor="middle" class="text-mono-green">Ingest / Query Decoupling</text>
      </g>

      <path d="M 545 155 L 580 155" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

      <g transform="translate(590, 45)">
        <!-- Stage 3 -->
        <rect x="0" y="0" width="220" height="220" rx="8" class="node-box"/>
        <rect x="0" y="0" width="220" height="38" rx="8" fill="#1b2434"/>
        <text x="110" y="24" text-anchor="middle" class="text-h1" fill="#b4a4e5">3. 3-Cloud Mapping</text>
        {render_icon("cloud", 20, 55, size=22, color="#b4a4e5")}
        <text x="52" y="72" class="text-h2">Service Translation</text>
        <text x="20" y="105" class="text-p">AWS Bedrock Stack</text>
        <text x="20" y="128" class="text-p">Azure Foundry Stack</text>
        <text x="20" y="151" class="text-p">Google Cloud Stack</text>
        <rect x="18" y="172" width="184" height="28" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="110" y="191" text-anchor="middle" class="text-mono-purple">Neutral Capability Contract</text>
      </g>

      <path d="M 820 155 L 855 155" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>

      <g transform="translate(865, 45)">
        <!-- Stage 4 -->
        <rect x="0" y="0" width="220" height="220" rx="8" class="node-box-active" stroke="#e0c58e"/>
        <rect x="0" y="0" width="220" height="38" rx="8" fill="#2d2516"/>
        <text x="110" y="24" text-anchor="middle" class="text-h1" fill="#e0c58e">4. Defensible Choice</text>
        {render_icon("approval", 20, 55, size=22, color="#e0c58e")}
        <text x="52" y="72" class="text-h2">Evaluation Board</text>
        <text x="20" y="105" class="text-p">5-Question Framework</text>
        <text x="20" y="128" class="text-p">Full Bill TCO Modeling</text>
        <text x="20" y="151" class="text-p">Rejected Alternative</text>
        <rect x="18" y="172" width="184" height="28" rx="4" fill="#141c28" stroke="#253245"/>
        <text x="110" y="191" text-anchor="middle" class="text-mono-amber">Executive Justification</text>
      </g>

      <!-- Bottom Governance and Platform Matrix Bar -->
      <g transform="translate(40, 290)">
        <rect x="0" y="0" width="1045" height="135" rx="8" class="swimlane-bg"/>
        <rect x="15" y="14" width="280" height="106" rx="6" fill="#172233" stroke="#253245"/>
        <text x="30" y="38" class="text-h2" fill="#60a5fa">Amazon Bedrock</text>
        <text x="30" y="62" class="text-p">Curated models (Claude, Nova)</text>
        <text x="30" y="83" class="text-p">Knowledge Bases &amp; Guardrails</text>
        <text x="30" y="104" class="text-dim">AWS IAM &amp; VPC Native</text>

        <rect x="310" y="14" width="280" height="106" rx="6" fill="#172233" stroke="#253245"/>
        <text x="325" y="38" class="text-h2" fill="#b4a4e5">Azure AI Foundry</text>
        <text x="325" y="62" class="text-p">10,000+ model catalog &amp; OpenAI</text>
        <text x="325" y="83" class="text-p">AI Search Semantic Rerank</text>
        <text x="325" y="104" class="text-dim">Entra ID &amp; M365 Ecosystem</text>

        <rect x="605" y="14" width="280" height="106" rx="6" fill="#172233" stroke="#253245"/>
        <text x="620" y="38" class="text-h2" fill="#e0c58e">Google Cloud</text>
        <text x="620" y="62" class="text-p">Gemini native 1M-2M context</text>
        <text x="620" y="83" class="text-p">Vertex AI Search &amp; Grounding</text>
        <text x="620" y="104" class="text-dim">BigQuery &amp; Lakehouse Native</text>

        <rect x="900" y="14" width="130" height="106" rx="6" fill="#151d2a" stroke="#364761"/>
        <text x="965" y="42" text-anchor="middle" class="text-mono-coral">CORE RULE</text>
        <text x="965" y="68" text-anchor="middle" class="text-p">Same contract.</text>
        <text x="965" y="90" text-anchor="middle" class="text-p">Three stacks.</text>
        <text x="965" y="108" text-anchor="middle" class="text-dim">Zero vendor lock.</text>
      </g>
    """),
    "notes": {
        "goal": "Open the lecture by establishing the core engineering principle: we compare how cloud platforms support one real application with identity, grounding, evaluation, and cost visibility.",
        "talkTrack": "Today we are not comparing cloud vendors as brands. We are comparing how cloud AI platforms help us build one real application: a grounded support assistant with evidence, permissions, evaluation, monitoring, and cost visibility. The goal of this module is to give you a defensible decision framework that you can take to an engineering review board, complete with concrete trade-offs and at least one rejected alternative.",
        "timing": "00:00 - 05:00 (5 min)"
    }
}
