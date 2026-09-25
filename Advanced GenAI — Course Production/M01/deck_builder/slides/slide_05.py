# Slide 05: The Cloud AI SaaS Capability Landscape
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 5,
    "kicker": "PLATFORM ANATOMY",
    "title": "The 6 Pillars of Managed Enterprise AI",
    "lead": "The standardized capability framework used to evaluate every cloud provider.",
    "section": "Capability Framework",
    "takeaway": "Every vendor provides these 6 pillars: the difference lies in integration depth and operational friction.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Pillar 1: Models -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="335" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="335" height="42" rx="8" fill="#1b2434"/>
          {render_icon("brain_model", 14, 9, size=24, color="#60a5fa")}
          <text x="46" y="27" class="text-h1" fill="#60a5fa">1. Foundation Models</text>
          <text x="16" y="65" class="text-p">Multi-provider catalog &amp; open-weight weights</text>
          <text x="16" y="88" class="text-p">Serverless pay-per-token vs Provisioned Units</text>
          <text x="16" y="111" class="text-p">Adapter fine-tuning (LoRA) &amp; distillation</text>
          <rect x="14" y="132" width="305" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="156" class="text-mono" font-size="11">AWS Bedrock &bull; Foundry &bull; Model Garden</text>
        </g>

        <!-- Pillar 2: Knowledge / RAG -->
        <g transform="translate(365, 0)">
          <rect x="0" y="0" width="335" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="335" height="42" rx="8" fill="#1b2434"/>
          {render_icon("search", 14, 9, size=24, color="#6ee7b7")}
          <text x="46" y="27" class="text-h1" fill="#6ee7b7">2. Knowledge &amp; RAG</text>
          <text x="16" y="65" class="text-p">Managed connectors (S3, SharePoint, Drive)</text>
          <text x="16" y="88" class="text-p">Automated chunking &amp; embedding pipelines</text>
          <text x="16" y="111" class="text-p">Hybrid lexical + dense search &amp; reranking</text>
          <rect x="14" y="132" width="305" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="156" class="text-mono-green" font-size="11">Bedrock KB &bull; AI Search &bull; Vertex Search</text>
        </g>

        <!-- Pillar 3: Agents & Tools -->
        <g transform="translate(730, 0)">
          <rect x="0" y="0" width="335" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="335" height="42" rx="8" fill="#1b2434"/>
          {render_icon("agent", 14, 9, size=24, color="#b4a4e5")}
          <text x="46" y="27" class="text-h1" fill="#b4a4e5">3. Agents &amp; Orchestration</text>
          <text x="16" y="65" class="text-p">Stateful session memory &amp; conversational state</text>
          <text x="16" y="88" class="text-p">Sandbox code interpretation &amp; API invocation</text>
          <text x="16" y="111" class="text-p">Human in the loop approval confirmation gates</text>
          <rect x="14" y="132" width="305" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="156" class="text-mono-purple" font-size="11">AgentCore &bull; Foundry Agent &bull; Gemini ADK</text>
        </g>

        <!-- Pillar 4: Evaluation -->
        <g transform="translate(0, 205)">
          <rect x="0" y="0" width="335" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="335" height="42" rx="8" fill="#1b2434"/>
          {render_icon("evaluation", 14, 9, size=24, color="#e0c58e")}
          <text x="46" y="27" class="text-h1" fill="#e0c58e">4. Evaluation &amp; Benchmarks</text>
          <text x="16" y="65" class="text-p">Pre-release golden Q&amp;A test sets</text>
          <text x="16" y="88" class="text-p">Automated Model-as-a-Judge scoring</text>
          <text x="16" y="111" class="text-p">Groundedness, relevance &amp; toxicity metrics</text>
          <rect x="14" y="132" width="305" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="156" class="text-mono-amber" font-size="11">Bedrock Evals &bull; Foundry Evals &bull; Vertex Eval</text>
        </g>

        <!-- Pillar 5: Observability -->
        <g transform="translate(365, 205)">
          <rect x="0" y="0" width="335" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="335" height="42" rx="8" fill="#1b2434"/>
          {render_icon("monitoring", 14, 9, size=24, color="#60a5fa")}
          <text x="46" y="27" class="text-h1" fill="#60a5fa">5. Tracing &amp; Telemetry</text>
          <text x="16" y="65" class="text-p">Distributed spans via OpenTelemetry standard</text>
          <text x="16" y="88" class="text-p">Per-request token accounting &amp; latency tracking</text>
          <text x="16" y="111" class="text-p">Failure clustering &amp; error categorization</text>
          <rect x="14" y="132" width="305" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="156" class="text-mono" font-size="11">CloudWatch/X-Ray &bull; App Insights &bull; Trace</text>
        </g>

        <!-- Pillar 6: Governance -->
        <g transform="translate(730, 205)">
          <rect x="0" y="0" width="335" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="335" height="42" rx="8" fill="#1b2434"/>
          {render_icon("shield", 14, 9, size=24, color="#d98585")}
          <text x="46" y="27" class="text-h1" fill="#d98585">6. Enterprise Governance</text>
          <text x="16" y="65" class="text-p">IAM roles, SSO &amp; document-level ACL filtering</text>
          <text x="16" y="88" class="text-p">Customer Managed Encryption Keys (CMEK)</text>
          <text x="16" y="111" class="text-p">Content safety, PII redaction &amp; jailbreak filters</text>
          <rect x="14" y="132" width="305" height="38" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="24" y="156" class="text-mono-coral" font-size="11">Guardrails &bull; Content Safety &bull; Model Armor</text>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Introduce the six standardized SaaS capability categories: models, knowledge, agents, evaluation, observability, and governance.",
        "talkTrack": "Introduce the six categories. Tell students these boxes are the comparison frame. Each vendor slide will answer: how does this platform provide models, knowledge, agents, evaluation, observability, and governance? When you look across AWS, Azure, and Google Cloud, every vendor offers these 6 pillars. The differentiator is never the presence of a box: it is how cleanly those boxes integrate with your existing corporate identity and data platforms.",
        "timing": "20:00 - 25:00 (5 min)"
    }
}
