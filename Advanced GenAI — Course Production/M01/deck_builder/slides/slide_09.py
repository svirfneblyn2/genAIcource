# Slide 09: Model Catalog Analysis: Reading Beyond Headline Numbers
from ..common_svg import svg_frame
from ..icons import render_icon
from ..logos import render_logo, render_logo_badge

SLIDE_DATA = {
    "index": 9,
    "kicker": "MODEL ECOSYSTEM",
    "title": "Model Catalog Philosophy: Curated vs Marketplace vs First-Party",
    "lead": "Raw model counts are marketing signals: evaluate operational fit and regional availability.",
    "section": "Model Strategy",
    "takeaway": "Catalog size reflects ecosystem strategy: production stability requires SLAs, regional latency, and data privacy guarantees.",
    "svg": svg_frame(f"""<g transform="translate(40, 25)">
        <!-- Card 1: Azure AI Foundry -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="330" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="330" height="46" rx="8" fill="#1b2434"/>
          {render_logo("azure", 14, 11, size=24, color="#b4a4e5")}
          <text x="46" y="29" class="text-h1" fill="#b4a4e5">Microsoft Azure AI Foundry</text>
          
          <g transform="translate(15, 58)">
            <!-- Headline Signal -->
            <rect x="0" y="0" width="300" height="36" rx="4" fill="#221b33" stroke="#b4a4e5" stroke-width="1.2"/>
            <text x="12" y="15" class="text-mono-purple" font-size="9">CATALOG PHILOSOPHY</text>
            <text x="12" y="28" class="text-h2" font-size="12" fill="#f8fafc">Marketplace Hub &bull; 10,000+ Models</text>

            <!-- Visual Vendor Badges -->
            <g transform="translate(0, 44)">
              <!-- OpenAI Flagship -->
              <rect x="0" y="0" width="300" height="32" rx="4" fill="#141c28" stroke="#3b82f6" stroke-width="1.2"/>
              {render_logo("openai", 10, 6, size=20, color="#60a5fa")}
              <text x="36" y="16" class="text-mono" font-size="10.5" fill="#93c5fd">OpenAI: GPT-4o &bull; o1 &bull; o3-mini</text>
              <text x="36" y="26" class="text-dim" font-size="8.5">Flagship Strategic Exclusive Partner</text>
            </g>

            <g transform="translate(0, 82)">
              <!-- Hugging Face -->
              <rect x="0" y="0" width="300" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("huggingface", 10, 6, size=18, color="#e0c58e")}
              <text x="36" y="19" class="text-p" fill="#e2e8f0">Hugging Face: Direct Open Catalog</text>
            </g>

            <g transform="translate(0, 118)">
              <!-- Mistral & Meta -->
              <rect x="0" y="0" width="145" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("mistral", 8, 7, size=16, color="#f97316")}
              <text x="28" y="19" class="text-mono" font-size="8.5" fill="#cbd5e1">Mistral Large</text>

              <rect x="155" y="0" width="145" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("meta", 163, 7, size=16, color="#60a5fa")}
              <text x="183" y="19" class="text-mono" font-size="8.5" fill="#cbd5e1">Llama 3.3 70B</text>
            </g>

            <!-- Architectural Evaluation -->
            <g transform="translate(0, 156)">
              <rect x="0" y="0" width="300" height="172" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-purple" font-size="10">ENGINEERING EVALUATION</text>
              <text x="12" y="40" class="text-p">&bull; API: Native OpenAI wire-format SDK</text>
              <text x="12" y="60" class="text-p">&bull; SLAs: Tier-1 on OpenAI; OSS varies</text>
              <text x="12" y="80" class="text-p">&bull; Privacy: Zero Data Retention via BAA</text>
              <text x="12" y="100" class="text-p">&bull; Quota: PTU reservations for TPS SLA</text>
              <rect x="10" y="122" width="280" height="36" rx="4" fill="#221b33" stroke="#b4a4e5" stroke-width="1"/>
              <text x="150" y="137" text-anchor="middle" class="text-mono-purple" font-size="9.5">OPTIMAL STACK FIT</text>
              <text x="150" y="150" text-anchor="middle" class="text-dim" font-size="8.5">OpenAI models &amp; OSS marketplace</text>
            </g>
          </g>
        </g>

        <!-- Card 2: AWS Bedrock -->
        <g transform="translate(355, 0)">
          <rect x="0" y="0" width="330" height="395" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="330" height="46" rx="8" fill="#1b2434"/>
          {render_logo("aws", 14, 11, size=24, color="#60a5fa")}
          <text x="46" y="29" class="text-h1" fill="#60a5fa">Amazon Bedrock</text>
          
          <g transform="translate(15, 58)">
            <!-- Headline Signal -->
            <rect x="0" y="0" width="300" height="36" rx="4" fill="#172233" stroke="#3b82f6" stroke-width="1.2"/>
            <text x="12" y="15" class="text-mono" font-size="9">CATALOG PHILOSOPHY</text>
            <text x="12" y="28" class="text-h2" font-size="12" fill="#f8fafc">Curated Multi-Provider Serverless</text>

            <!-- Visual Vendor Badges -->
            <g transform="translate(0, 44)">
              <!-- Anthropic Flagship -->
              <rect x="0" y="0" width="300" height="32" rx="4" fill="#141c28" stroke="#60a5fa" stroke-width="1.2"/>
              {render_logo("anthropic", 10, 6, size=20, color="#d98585")}
              <text x="36" y="16" class="text-mono" font-size="10.5" fill="#93c5fd">Anthropic: Claude 3.5 Sonnet / Haiku</text>
              <text x="36" y="26" class="text-dim" font-size="8.5">Flagship Reasoning &amp; Coding Engine</text>
            </g>

            <g transform="translate(0, 82)">
              <!-- Amazon Nova & Titan -->
              <rect x="0" y="0" width="300" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_icon("brain_model", 10, 6, size=18, color="#6ee7b7")}
              <text x="36" y="19" class="text-p" fill="#e2e8f0">Amazon Nova Pro &bull; Titan Embeddings V2</text>
            </g>

            <g transform="translate(0, 118)">
              <!-- Meta & Cohere -->
              <rect x="0" y="0" width="145" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("meta", 8, 7, size=16, color="#60a5fa")}
              <text x="28" y="19" class="text-mono" font-size="8.5" fill="#cbd5e1">Llama 3.3 70B</text>

              <rect x="155" y="0" width="145" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("cohere", 163, 7, size=16, color="#6ee7b7")}
              <text x="183" y="19" class="text-mono" font-size="8.5" fill="#cbd5e1">Cohere Embed</text>
            </g>

            <!-- Architectural Evaluation -->
            <g transform="translate(0, 156)">
              <rect x="0" y="0" width="300" height="172" rx="6" fill="#172233" stroke="#3b82f6" stroke-width="1.2"/>
              <text x="12" y="20" class="text-mono" font-size="10">ENGINEERING EVALUATION</text>
              <text x="12" y="40" class="text-p">&bull; API: 100% Unified Converse API contract</text>
              <text x="12" y="60" class="text-p">&bull; SLAs: Uniform AWS enterprise SLA</text>
              <text x="12" y="80" class="text-p">&bull; Privacy: Zero Data Retention by default</text>
              <text x="12" y="100" class="text-p">&bull; Quota: Serverless On-Demand + Provisioned</text>
              <rect x="10" y="122" width="280" height="36" rx="4" fill="#1e2c42" stroke="#60a5fa" stroke-width="1"/>
              <text x="150" y="137" text-anchor="middle" class="text-mono" font-size="9.5">OPTIMAL STACK FIT</text>
              <text x="150" y="150" text-anchor="middle" class="text-dim" font-size="8.5">Claude 3.5 &amp; unified Converse contract</text>
            </g>
          </g>
        </g>

        <!-- Card 3: Google Cloud Model Garden -->
        <g transform="translate(710, 0)">
          <rect x="0" y="0" width="330" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="330" height="46" rx="8" fill="#1b2434"/>
          {render_logo("gcp", 14, 11, size=24, color="#e0c58e")}
          <text x="46" y="29" class="text-h1" fill="#e0c58e">Google Cloud Model Garden</text>
          
          <g transform="translate(15, 58)">
            <!-- Headline Signal -->
            <rect x="0" y="0" width="300" height="36" rx="4" fill="#2d2516" stroke="#e0c58e" stroke-width="1.2"/>
            <text x="12" y="15" class="text-mono-amber" font-size="9">CATALOG PHILOSOPHY</text>
            <text x="12" y="28" class="text-h2" font-size="12" fill="#f8fafc">First-Party Multimodal &amp; Open Models</text>

            <!-- Visual Vendor Badges -->
            <g transform="translate(0, 44)">
              <!-- Gemini Flagship -->
              <rect x="0" y="0" width="300" height="32" rx="4" fill="#141c28" stroke="#e0c58e" stroke-width="1.2"/>
              {render_logo("gemini", 10, 6, size=20, color="#e0c58e")}
              <text x="36" y="16" class="text-mono-amber" font-size="10.5">Gemini: 2.0 Flash &bull; 1.5 Pro</text>
              <text x="36" y="26" class="text-dim" font-size="8.5">1M to 2M Token Native Multimodal Context</text>
            </g>

            <g transform="translate(0, 82)">
              <!-- Claude on Vertex & Gemma -->
              <rect x="0" y="0" width="300" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("anthropic", 10, 6, size=18, color="#d98585")}
              <text x="36" y="19" class="text-p" fill="#e2e8f0">Claude 3.5 Sonnet + Gemma 2 (9B/27B)</text>
            </g>

            <g transform="translate(0, 118)">
              <!-- Meta & Mistral -->
              <rect x="0" y="0" width="145" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("meta", 8, 7, size=16, color="#60a5fa")}
              <text x="28" y="19" class="text-mono" font-size="8.5" fill="#cbd5e1">Llama 3.3 70B</text>

              <rect x="155" y="0" width="145" height="30" rx="4" fill="#141c28" stroke="#253245"/>
              {render_logo("mistral", 163, 7, size=16, color="#f97316")}
              <text x="183" y="19" class="text-mono" font-size="8.5" fill="#cbd5e1">Mistral Large</text>
            </g>

            <!-- Architectural Evaluation -->
            <g transform="translate(0, 156)">
              <rect x="0" y="0" width="300" height="172" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="12" y="20" class="text-mono-amber" font-size="10">ENGINEERING EVALUATION</text>
              <text x="12" y="40" class="text-p">&bull; Context: Unmatched 1M-2M context tokens</text>
              <text x="12" y="60" class="text-p">&bull; Multimodal: Audio, video, and PDF native</text>
              <text x="12" y="80" class="text-p">&bull; TPU v5e: High-throughput Flash economics</text>
              <text x="12" y="100" class="text-p">&bull; Caching: 75% savings via context caching</text>
              <rect x="10" y="122" width="280" height="36" rx="4" fill="#2d2516" stroke="#e0c58e" stroke-width="1"/>
              <text x="150" y="137" text-anchor="middle" class="text-mono-amber" font-size="9.5">OPTIMAL STACK FIT</text>
              <text x="150" y="150" text-anchor="middle" class="text-dim" font-size="8.5">Native audio/video &amp; 1M+ context</text>
            </g>
          </g>
        </g>
      </g>"""),
    "notes": {
        "goal": "Explain how to evaluate model catalogs critically. Detail that raw numbers are marketing signals: operational SLAs, regional latency, and zero data retention agreements matter.",
        "talkTrack": "Explain that model count is a marketing vanity metric. Azure boasts 10,000+ models, but in production, enterprises rarely deploy more than 2 or 3 curated models. What matters is the operational SLA, whether Zero Data Retention applies by default, and whether the API contract is unified. AWS Bedrock stands out for its unified Converse API contract: switching from Claude to Nova or Llama requires zero code changes to tool definitions. Google Vertex leads in native multimodal context and context caching economics.",
        "timing": "40:00 - 45:00 (5 min)"
    }
}
