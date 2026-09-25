# Slide 22: Where "Cheaper" Really Comes From
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 22,
    "kicker": "COST OPTIMIZATION",
    "title": "Cost Optimization: Engineering Architectural Efficiency",
    "lead": "Low cost is a design outcome, not a vendor discount: four engineering levers.",
    "section": "Cost Optimization",
    "takeaway": "Do not negotiate vendor prices: optimize your token density, caching hit rates, and model routing.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Quadrant 1: Context Compaction -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="505" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="505" height="42" rx="8" fill="#1b2434"/>
          {render_icon("document", 14, 9, size=24, color="#60a5fa")}
          <text x="46" y="27" class="text-h1" fill="#60a5fa">1. Context Compaction</text>
          <text x="460" y="27" text-anchor="end" class="text-mono-green" font-size="12">30-50% Savings</text>
          
          <g transform="translate(20, 58)">
            <text x="0" y="0" class="text-h2">Trim Boilerplate Before Prompt Assembly</text>
            <text x="0" y="22" class="text-p">&bull; Strip repetitive HTML headers, legal disclaimers, and conversational fluff.</text>
            <text x="0" y="42" class="text-p">&bull; Clean markdown extraction preserves tabular structure in half the tokens.</text>
            <rect x="0" y="60" width="465" height="30" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="80" class="text-mono" font-size="11">Architecture: Client-side AST pruning pipeline</text>
          </g>
        </g>

        <!-- Quadrant 2: Semantic Caching -->
        <g transform="translate(535, 0)">
          <rect x="0" y="0" width="505" height="185" rx="8" class="node-box-active" stroke="#6ee7b7"/>
          <rect x="0" y="0" width="505" height="42" rx="8" fill="#162924"/>
          {render_icon("database", 14, 9, size=24, color="#6ee7b7")}
          <text x="46" y="27" class="text-h1" fill="#6ee7b7">2. Semantic &amp; Prompt Caching</text>
          <text x="460" y="27" text-anchor="end" class="text-mono-green" font-size="12">50-80% Savings</text>
          
          <g transform="translate(20, 58)">
            <text x="0" y="0" class="text-h2">Bypass Model Inference on Repetitive Queries</text>
            <text x="0" y="22" class="text-p">&bull; Exact match + cosine vector cache on Redis for common policy FAQs (0 tokens).</text>
            <text x="0" y="42" class="text-p">&bull; Provider prompt caching (Bedrock Claude / Azure OpenAI / Gemini) on system prompts.</text>
            <rect x="0" y="60" width="465" height="30" rx="4" fill="#152420" stroke="#6ee7b7" stroke-width="1.2"/>
            <text x="12" y="80" class="text-mono-green" font-size="11">Architecture: Prefix caching with static system guidelines</text>
          </g>
        </g>

        <!-- Quadrant 3: Model Tiering & Routing -->
        <g transform="translate(0, 205)">
          <rect x="0" y="0" width="505" height="185" rx="8" class="node-box-active" stroke="#b4a4e5"/>
          <rect x="0" y="0" width="505" height="42" rx="8" fill="#221c32"/>
          {render_icon("brain_model", 14, 9, size=24, color="#b4a4e5")}
          <text x="46" y="27" class="text-h1" fill="#b4a4e5">3. Model Tiering &amp; SLM Routing</text>
          <text x="460" y="27" text-anchor="end" class="text-mono-green" font-size="12">70% Savings</text>
          
          <g transform="translate(20, 58)">
            <text x="0" y="0" class="text-h2">Route by Workload Difficulty</text>
            <text x="0" y="22" class="text-p">&bull; Send 80% simple lookup questions to SLMs (Haiku / 4o-mini / Flash).</text>
            <text x="0" y="42" class="text-p">&bull; Escalate multi-step exceptions to Frontier models (Sonnet / GPT-4o / Pro).</text>
            <rect x="0" y="60" width="465" height="30" rx="4" fill="#1b1c30" stroke="#b4a4e5" stroke-width="1.2"/>
            <text x="12" y="80" class="text-mono-purple" font-size="11">Architecture: Lightweight intent classification gateway</text>
          </g>
        </g>

        <!-- Quadrant 4: Batch & Flex Processing -->
        <g transform="translate(535, 205)">
          <rect x="0" y="0" width="505" height="185" rx="8" class="node-box"/>
          <rect x="0" y="0" width="505" height="42" rx="8" fill="#1b2434"/>
          {render_icon("cost", 14, 9, size=24, color="#e0c58e")}
          <text x="46" y="27" class="text-h1" fill="#e0c58e">4. Batch &amp; Flex Pricing</text>
          <text x="460" y="27" text-anchor="end" class="text-mono-green" font-size="12">50% Off-Peak Discount</text>
          
          <g transform="translate(20, 58)">
            <text x="0" y="0" class="text-h2">Decouple Non-Interactive Inference</text>
            <text x="0" y="22" class="text-p">&bull; Run offline document chunk summarization and embedding rebuilds overnight.</text>
            <text x="0" y="42" class="text-p">&bull; Execute regression evaluation test batches via 24h batch APIs at 50% discount.</text>
            <rect x="0" y="60" width="465" height="30" rx="4" fill="#141c28" stroke="#253245"/>
            <text x="12" y="80" class="text-mono-amber" font-size="11">Architecture: Asynchronous SQS / Service Bus queues</text>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Explain the four concrete engineering levers that produce radical cost reduction: compaction, caching, tiering/routing, and batch queues.",
        "talkTrack": "Answer the cheapness question. Cheaper usually comes from design: reduce tokens, improve retrieval, use batch or flexible tiers when latency allows, cache safely, and consider local or hybrid only when the organization can operate it responsibly. Do not spend time negotiating model discounts with cloud account reps: by engineering prompt caching, SLM routing to Haiku or Flash, and context compaction, you cut 70% of the bill on day one.",
        "timing": "105:00 - 110:00 (5 min)"
    }
}
