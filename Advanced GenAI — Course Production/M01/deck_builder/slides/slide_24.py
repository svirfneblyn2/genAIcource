# Slide 24: Demo Translation Sequence
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 24,
    "kicker": "DEMO RUNBOOK",
    "title": "The Multi-Cloud Demonstration Flow",
    "lead": "Demonstrating one architectural contract across AWS, Azure, and Google Cloud consoles.",
    "section": "Demo Translation",
    "takeaway": "Portals look different; the underlying identity, retrieval, and inference mechanisms are identical.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Stage 1 -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="325" height="175" rx="8" class="node-box"/>
          <rect x="0" y="0" width="325" height="38" rx="8" fill="#1b2434"/>
          <text x="20" y="24" class="text-mono" font-size="12" fill="#60a5fa">STAGE 01</text>
          <text x="90" y="24" class="text-h2">Business Contract</text>
          
          <g transform="translate(16, 52)">
            <text x="0" y="0" class="text-p">&bull; Review Sarah's laptop loan query</text>
            <text x="0" y="22" class="text-p">&bull; Establish citation &amp; ticket approval rule</text>
            <text x="0" y="44" class="text-p">&bull; Define data boundary &amp; user role</text>
            <rect x="0" y="65" width="293" height="32" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="86" class="text-mono" font-size="11">Time Budget: 3 minutes</text>
          </g>
        </g>

        <path d="M 335 85 L 360 85" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

        <!-- Stage 2 -->
        <g transform="translate(370, 0)">
          <rect x="0" y="0" width="325" height="175" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="325" height="38" rx="8" fill="#1e2c42"/>
          <text x="20" y="24" class="text-mono" font-size="12" fill="#60a5fa">STAGE 02</text>
          <text x="90" y="24" class="text-h2" fill="#60a5fa">Neutral Topology</text>
          
          <g transform="translate(16, 52)">
            <text x="0" y="0" class="text-p">&bull; Display two-lane reference diagram</text>
            <text x="0" y="22" class="text-p">&bull; Point out offline vs online boundaries</text>
            <text x="0" y="44" class="text-p">&bull; Keep diagram pinned on second monitor</text>
            <rect x="0" y="65" width="293" height="32" rx="4" fill="#172233" stroke="#3b82f6"/>
            <text x="12" y="86" class="text-mono" font-size="11">Time Budget: 4 minutes</text>
          </g>
        </g>

        <path d="M 705 85 L 730 85" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

        <!-- Stage 3 -->
        <g transform="translate(740, 0)">
          <rect x="0" y="0" width="300" height="175" rx="8" class="node-box"/>
          <rect x="0" y="0" width="300" height="38" rx="8" fill="#1b2434"/>
          <text x="20" y="24" class="text-mono" font-size="12" fill="#60a5fa">STAGE 03</text>
          <text x="90" y="24" class="text-h2">AWS Bedrock</text>
          
          <g transform="translate(16, 52)">
            <text x="0" y="0" class="text-p">&bull; S3 &rarr; Knowledge Base sync</text>
            <text x="0" y="22" class="text-p">&bull; OpenSearch Serverless collection</text>
            <text x="0" y="44" class="text-p">&bull; Bedrock Agent &amp; Guardrails filter</text>
            <rect x="0" y="65" width="268" height="32" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="86" class="text-mono" font-size="11">Console Demo: 6 minutes</text>
          </g>
        </g>

        <!-- Stage 4 -->
        <g transform="translate(0, 205)">
          <rect x="0" y="0" width="325" height="175" rx="8" class="node-box"/>
          <rect x="0" y="0" width="325" height="38" rx="8" fill="#221c32"/>
          <text x="20" y="24" class="text-mono-purple" font-size="12">STAGE 04</text>
          <text x="90" y="24" class="text-h2" fill="#b4a4e5">Azure AI Foundry</text>
          
          <g transform="translate(16, 52)">
            <text x="0" y="0" class="text-p">&bull; AI Search index &amp; Entra ID ACL</text>
            <text x="0" y="22" class="text-p">&bull; Foundry Agent Service wiring</text>
            <text x="0" y="44" class="text-p">&bull; Semantic Reranker precision check</text>
            <rect x="0" y="65" width="293" height="32" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="86" class="text-mono-purple" font-size="11">Console Demo: 6 minutes</text>
          </g>
        </g>

        <path d="M 335 290 L 360 290" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>

        <!-- Stage 5 -->
        <g transform="translate(370, 205)">
          <rect x="0" y="0" width="325" height="175" rx="8" class="node-box"/>
          <rect x="0" y="0" width="325" height="38" rx="8" fill="#2d2516"/>
          <text x="20" y="24" class="text-mono-amber" font-size="12">STAGE 05</text>
          <text x="90" y="24" class="text-h2" fill="#e0c58e">Google Cloud</text>
          
          <g transform="translate(16, 52)">
            <text x="0" y="0" class="text-p">&bull; Vertex AI Search &amp; Enterprise Grounding</text>
            <text x="0" y="22" class="text-p">&bull; Gemini 1.5 Flash in Agent Platform</text>
            <text x="0" y="44" class="text-p">&bull; Model Armor prompt injection test</text>
            <rect x="0" y="65" width="293" height="32" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="86" class="text-mono-amber" font-size="11">Console Demo: 6 minutes</text>
          </g>
        </g>

        <path d="M 705 290 L 730 290" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>

        <!-- Stage 6 -->
        <g transform="translate(740, 205)">
          <rect x="0" y="0" width="300" height="175" rx="8" class="node-box-active" stroke="#6ee7b7"/>
          <rect x="0" y="0" width="300" height="38" rx="8" fill="#162924"/>
          <text x="20" y="24" class="text-mono-green" font-size="12">STAGE 06</text>
          <text x="90" y="24" class="text-h2" fill="#6ee7b7">Synthesis &amp; TCO</text>
          
          <g transform="translate(16, 52)">
            <text x="0" y="0" class="text-p">&bull; Open live pricing calculators</text>
            <text x="0" y="22" class="text-p">&bull; Contrast OCU vs PTU vs PayG</text>
            <text x="0" y="44" class="text-p">&bull; Announce defensible decision</text>
            <rect x="0" y="65" width="268" height="32" rx="4" fill="#152420" stroke="#6ee7b7"/>
            <text x="12" y="86" class="text-mono-green" font-size="11">Decision Check: 5 minutes</text>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Explain the multi-cloud live demonstration sequence. Warn instructors not to present 3 disconnected demos, but to anchor every console walk-through in the neutral architecture.",
        "talkTrack": "Explain the demo sequence before starting. The demo is requirements -> neutral architecture -> AWS mapping -> Azure mapping -> Google mapping -> decision and cost check. Do not open three unrelated demos. Keep the neutral architecture diagram on screen as the anchor. When students see how the same S3/Blob storage, vector index, model call, and approval gate map across all three portals, the cloud landscape suddenly becomes crystal clear.",
        "timing": "115:00 - 120:00 (5 min)"
    }
}
