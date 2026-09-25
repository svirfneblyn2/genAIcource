# Slide 17: SaaS Capability Matrix: 3-Way Direct Comparison
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 17,
    "kicker": "CAPABILITY MATRIX",
    "title": "Side-by-Side Enterprise Component Alignment",
    "lead": "Translating architectural functions across AWS, Azure, and Google Cloud.",
    "section": "Multi-Cloud Alignment",
    "takeaway": "The concepts are universal: architecture decisions outlive specific cloud vendor branding.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Table Header -->
        <rect x="0" y="0" width="1040" height="42" rx="6" fill="#1b2434" stroke="#253245"/>
        <text x="24" y="26" class="text-mono" font-size="12" fill="#cbd5e1">ARCHITECTURAL FUNCTION</text>
        <text x="270" y="26" class="text-mono" font-size="12" fill="#60a5fa">AMAZON BEDROCK</text>
        <text x="530" y="26" class="text-mono" font-size="12" fill="#b4a4e5">AZURE AI FOUNDRY</text>
        <text x="790" y="26" class="text-mono" font-size="12" fill="#e0c58e">GOOGLE CLOUD (GEMINI / VERTEX)</text>

        <!-- Rows -->
        <!-- Row 1: Model Catalog -->
        <g transform="translate(0, 48)">
          <rect x="0" y="0" width="1040" height="42" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="26" class="text-h2">Model Catalog &amp; API</text>
          <text x="270" y="26" class="text-p">Bedrock Multi-provider &bull; Converse</text>
          <text x="530" y="26" class="text-p">Foundry 10k+ &bull; Azure OpenAI</text>
          <text x="790" y="26" class="text-p">Model Garden &bull; Gemini 1.5/2.0 API</text>
        </g>

        <!-- Row 2: Managed RAG -->
        <g transform="translate(0, 96)">
          <rect x="0" y="0" width="1040" height="42" rx="4" fill="#121824" stroke="#1e293b"/>
          <text x="24" y="26" class="text-h2">Managed Knowledge &amp; RAG</text>
          <text x="270" y="26" class="text-p">Knowledge Bases for Bedrock</text>
          <text x="530" y="26" class="text-p">Azure AI Search (Semantic Rerank)</text>
          <text x="790" y="26" class="text-p">Vertex AI Search &amp; Enterprise Grounding</text>
        </g>

        <!-- Row 3: Agent Orchestration -->
        <g transform="translate(0, 144)">
          <rect x="0" y="0" width="1040" height="42" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="26" class="text-h2">Agent &amp; Tool Orchestration</text>
          <text x="270" y="26" class="text-p">Bedrock Agents &bull; Bedrock AgentCore</text>
          <text x="530" y="26" class="text-p">Azure AI Foundry Agent Service</text>
          <text x="790" y="26" class="text-p">Gemini Agent Platform &bull; ADK</text>
        </g>

        <!-- Row 4: Content Safety -->
        <g transform="translate(0, 192)">
          <rect x="0" y="0" width="1040" height="42" rx="4" fill="#121824" stroke="#1e293b"/>
          <text x="24" y="26" class="text-h2">Content Safety &amp; Guardrails</text>
          <text x="270" y="26" class="text-p">Bedrock Guardrails (PII &amp; Prompt)</text>
          <text x="530" y="26" class="text-p">Azure AI Content Safety</text>
          <text x="790" y="26" class="text-p">Model Armor &bull; Vertex Safety Filters</text>
        </g>

        <!-- Row 5: Observability -->
        <g transform="translate(0, 240)">
          <rect x="0" y="0" width="1040" height="42" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="26" class="text-h2">Tracing &amp; Observability</text>
          <text x="270" y="26" class="text-p">Amazon CloudWatch &bull; AWS X-Ray</text>
          <text x="530" y="26" class="text-p">Azure Application Insights &bull; OTel</text>
          <text x="790" y="26" class="text-p">Google Cloud Observability (Trace)</text>
        </g>

        <!-- Row 6: Evaluation -->
        <g transform="translate(0, 288)">
          <rect x="0" y="0" width="1040" height="42" rx="4" fill="#121824" stroke="#1e293b"/>
          <text x="24" y="26" class="text-h2">Model Evaluation</text>
          <text x="270" y="26" class="text-p">Bedrock Model Evaluation</text>
          <text x="530" y="26" class="text-p">Foundry Evaluation Hub</text>
          <text x="790" y="26" class="text-p">Vertex AI Model Evaluation</text>
        </g>

        <!-- Row 7: Enterprise Identity -->
        <g transform="translate(0, 336)">
          <rect x="0" y="0" width="1040" height="42" rx="4" fill="#141c28" stroke="#1e293b"/>
          <text x="24" y="26" class="text-h2">Enterprise Identity &amp; Auth</text>
          <text x="270" y="26" class="text-p">AWS IAM &bull; Amazon Cognito</text>
          <text x="530" y="26" class="text-p">Microsoft Entra ID (Native M365)</text>
          <text x="790" y="26" class="text-p">Cloud Identity &bull; IAM Workload Auth</text>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Show the direct side-by-side SaaS capability alignment across AWS, Azure, and Google Cloud.",
        "talkTrack": "Show the SaaS capability map. Tell students that similar categories exist across vendors, but implementation details differ. This is why architecture concepts must be stable while service labels can change. Product names will inevitably be rebranded every 18 months, but the core system boundaries (model access, vector search, agent memory, safety filters, and distributed tracing) will remain identical.",
        "timing": "80:00 - 85:00 (5 min)"
    }
}
