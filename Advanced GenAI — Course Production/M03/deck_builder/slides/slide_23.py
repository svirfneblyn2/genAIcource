# -*- coding: utf-8 -*-
slide_data = {
    "index": 23,
    "badge": "EVALUATION METRICS",
    "title": "Generation Evaluation: The Ragas / TruLens Triad",
    "subtitle": "Automated Model-as-a-Judge assessment across context, grounding, and response quality.",
    "takeaway_tag": "RAGAS TRIAD",
    "takeaway": "Deconstruct answer quality into 3 distinct gates: context relevance, faithfulness, and answer relevance.",
    "notes": """
      <h4>The Ragas Triad</h4>
      <p>Explain the 3 core metrics: Context Relevance (signal vs noise in retrieved chunks), Faithfulness (every generated claim backed by context), and Answer Relevance (response directly addresses the prompt).</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#60a5fa"/>
        </marker>
      </defs>

      <!-- Center Triangle / Triad Diagram -->
      <g transform="translate(50, 30)">
        <!-- Node 1: Context Relevance -->
        <g transform="translate(0, 0)">
          <rect width="230" height="280" rx="8" fill="#141c28" stroke="#60a5fa" stroke-width="1.2"/>
          <rect width="230" height="34" rx="8" fill="#1b2434"/>
          <text x="115" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">1. CONTEXT RELEVANCE</text>

          <g transform="translate(15, 50)">
            <text x="0" y="16" class="text-mono" font-size="10" fill="#94a3b8">Equation:</text>
            <text x="0" y="34" class="text-mono-bold" font-size="10" fill="#f8fafc">|S_relevant| / |S_total_chunks|</text>

            <rect y="50" width="200" height="75" rx="4" fill="#0e131b"/>
            <text x="10" y="70" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">Evaluation Question:</text>
            <text x="10" y="90" class="text-p" font-size="9">"Did retrieval fetch clean</text>
            <text x="10" y="104" class="text-p" font-size="9">signal, or is the context</text>
            <text x="10" y="118" class="text-p" font-size="9">stuffed with noisy junk?"</text>

            <rect y="140" width="200" height="60" rx="4" fill="#1b2434"/>
            <text x="10" y="160" class="text-mono" font-size="9" fill="#e0c58e">Target Benchmark: &gt; 0.80</text>
            <text x="10" y="176" class="text-dim" font-size="8.5">Low score = excessive top-k</text>
          </g>
        </g>

        <!-- Node 2: Faithfulness / Groundedness -->
        <g transform="translate(265, 0)">
          <rect width="230" height="280" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
          <rect width="230" height="34" rx="8" fill="#1b2434"/>
          <text x="115" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">2. FAITHFULNESS</text>

          <g transform="translate(15, 50)">
            <text x="0" y="16" class="text-mono" font-size="10" fill="#94a3b8">Equation:</text>
            <text x="0" y="34" class="text-mono-bold" font-size="10" fill="#f8fafc">|V_claims| / |Total_claims|</text>

            <rect y="50" width="200" height="75" rx="4" fill="#0e131b"/>
            <text x="10" y="70" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">Evaluation Question:</text>
            <text x="10" y="90" class="text-p" font-size="9">"Can every factual statement</text>
            <text x="10" y="104" class="text-p" font-size="9">be verified mathematically</text>
            <text x="10" y="118" class="text-p" font-size="9">against the context?"</text>

            <rect y="140" width="200" height="60" rx="4" fill="#1b2434"/>
            <text x="10" y="160" class="text-mono" font-size="9" fill="#6ee7b7">Target Benchmark: &gt; 0.95</text>
            <text x="10" y="176" class="text-dim" font-size="8.5">Low score = Hallucination</text>
          </g>
        </g>

        <!-- Node 3: Answer Relevance -->
        <g transform="translate(530, 0)">
          <rect width="230" height="280" rx="8" fill="#141c28" stroke="#b4a4e5" stroke-width="1.2"/>
          <rect width="230" height="34" rx="8" fill="#1b2434"/>
          <text x="115" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#b4a4e5">3. ANSWER RELEVANCE</text>

          <g transform="translate(15, 50)">
            <text x="0" y="16" class="text-mono" font-size="10" fill="#94a3b8">Equation:</text>
            <text x="0" y="34" class="text-mono-bold" font-size="10" fill="#f8fafc">Cosine( Embed(Q), Embed(Q_pred) )</text>

            <rect y="50" width="200" height="75" rx="4" fill="#0e131b"/>
            <text x="10" y="70" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">Evaluation Question:</text>
            <text x="10" y="90" class="text-p" font-size="9">"Does the response directly</text>
            <text x="10" y="104" class="text-p" font-size="9">address the user prompt,</text>
            <text x="10" y="118" class="text-p" font-size="9">or does it ramble?"</text>

            <rect y="140" width="200" height="60" rx="4" fill="#1b2434"/>
            <text x="10" y="160" class="text-mono" font-size="9" fill="#b4a4e5">Target Benchmark: &gt; 0.88</text>
            <text x="10" y="176" class="text-dim" font-size="8.5">Low score = Incomplete response</text>
          </g>
        </g>
      </g>
    </svg>"""
}
