# -*- coding: utf-8 -*-
slide_data = {
    "index": 24,
    "badge": "REFERENCE TOPOLOGY",
    "title": "Production Architecture Reference: Industrial RAG Pipeline",
    "subtitle": "The complete enterprise architecture incorporating semantic caching, guardrails, and telemetry.",
    "takeaway_tag": "INDUSTRIAL SPEC",
    "takeaway": "Enterprise RAG wraps the core pipeline in semantic caching, security gates, and continuous tracing.",
    "notes": """
      <h4>Production Reference Design</h4>
      <p>Walk through the complete production stack: Semantic Cache (bypasses LLM for 40% of FAQ queries), PII Masking, Multi-tenant Vector Store, Cross-Encoder Reranker, and OpenTelemetry collector.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#60a5fa"/>
        </marker>
        <marker id="arr-green" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
          <polygon points="0 0, 8 3, 0 6" fill="#6ee7b7"/>
        </marker>
      </defs>

      <g transform="translate(30, 25)">
        <rect width="800" height="300" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>

        <!-- Top Row: Client & Frontline Gate -->
        <g transform="translate(25, 20)">
          <!-- Client -->
          <rect width="130" height="75" rx="6" fill="#0e131b" stroke="#253245"/>
          <text x="65" y="24" text-anchor="middle" class="text-h1" font-size="11">Client UI / API</text>
          <text x="65" y="42" text-anchor="middle" class="text-dim" font-size="9">Web / Slack / Teams</text>
          <text x="65" y="58" text-anchor="middle" class="text-mono" font-size="8.5" fill="#60a5fa">JWT / Bearer Token</text>

          <path d="M 135 37 L 165 37" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <!-- Semantic Cache -->
          <rect x="170" width="140" height="75" rx="6" fill="#1b2434" stroke="#e0c58e" stroke-width="1.2"/>
          <text x="240" y="24" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#e0c58e">Semantic Cache</text>
          <text x="240" y="42" text-anchor="middle" class="text-dim" font-size="9">Exact / Vector Match</text>
          <text x="240" y="58" text-anchor="middle" class="text-mono" font-size="8.5" fill="#6ee7b7">35% FAQ Cache Hit</text>

          <path d="M 315 37 L 345 37" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <!-- Guardrail & PII -->
          <rect x="350" width="135" height="75" rx="6" fill="#0e131b" stroke="#253245"/>
          <text x="417" y="24" text-anchor="middle" class="text-h1" font-size="11">Input Guardrail</text>
          <text x="417" y="42" text-anchor="middle" class="text-dim" font-size="9">PII Masking &amp; Anonymize</text>
          <text x="417" y="58" text-anchor="middle" class="text-mono" font-size="8.5" fill="#d98585">Prompt Injection Gate</text>

          <path d="M 490 37 L 520 37" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <!-- Authorization Filter -->
          <rect x="525" width="130" height="75" rx="6" fill="#0e131b" stroke="#253245"/>
          <text x="590" y="24" text-anchor="middle" class="text-h1" font-size="11">Auth &amp; ACL Pruner</text>
          <text x="590" y="42" text-anchor="middle" class="text-dim" font-size="9">RBAC &amp; Tenant ID</text>
          <text x="590" y="58" text-anchor="middle" class="text-mono" font-size="8.5" fill="#6ee7b7">Pre-Filtering Engine</text>

          <path d="M 660 37 L 690 37" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

          <!-- Vector Store -->
          <rect x="695" width="80" height="75" rx="6" fill="#1b2434" stroke="#60a5fa" stroke-width="1.2"/>
          <text x="735" y="32" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#60a5fa">Vector</text>
          <text x="735" y="48" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#60a5fa">Index</text>
          <text x="735" y="64" text-anchor="middle" class="text-dim" font-size="8">HNSW</text>
        </g>

        <!-- Down Arrow from Vector Store to Bottom Row -->
        <path d="M 760 102 L 760 135" stroke="#6ee7b7" stroke-width="1.5" marker-end="url(#arr-green)"/>

        <!-- Bottom Row: Rerank, Assembly, Generation & Telemetry -->
        <g transform="translate(25, 145)">
          <!-- Telemetry OTel -->
          <rect width="130" height="125" rx="6" fill="#0e131b" stroke="#d98585" stroke-width="1"/>
          <text x="65" y="24" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#d98585">OTel Telemetry</text>
          <text x="65" y="44" text-anchor="middle" class="text-dim" font-size="8.5">Distributed Spans</text>
          <text x="65" y="60" text-anchor="middle" class="text-dim" font-size="8.5">Latency &amp; Token Count</text>
          <text x="65" y="76" text-anchor="middle" class="text-dim" font-size="8.5">Failure Root Cause</text>
          <rect x="10" y="88" width="110" height="26" rx="3" fill="#1b2434"/>
          <text x="65" y="105" text-anchor="middle" class="text-mono" font-size="8.5" fill="#e0c58e">Tracing Bus</text>

          <!-- Generation -->
          <rect x="170" width="160" height="125" rx="6" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="250" y="24" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Grounded LLM</text>
          <text x="250" y="44" text-anchor="middle" class="text-p" font-size="9">Temperature = 0.0</text>
          <text x="250" y="60" text-anchor="middle" class="text-p" font-size="9">Prompt Caching Enabled</text>
          <text x="250" y="76" text-anchor="middle" class="text-mono" font-size="8.5" fill="#6ee7b7">Inline Citation Format</text>
          <text x="250" y="92" text-anchor="middle" class="text-dim" font-size="8.5">Mandatory Refusal Rule</text>
          <text x="250" y="108" text-anchor="middle" class="text-mono" font-size="8.5" fill="#e0c58e">Sub-1s Latency Target</text>

          <path d="M 370 60 L 335 60" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

          <!-- Context Assembly -->
          <rect x="375" width="160" height="125" rx="6" fill="#0e131b" stroke="#253245"/>
          <text x="455" y="24" text-anchor="middle" class="text-h1" font-size="11">Context Assembler</text>
          <text x="455" y="44" text-anchor="middle" class="text-dim" font-size="8.5">Primacy: Top Rerank at Start</text>
          <text x="455" y="60" text-anchor="middle" class="text-dim" font-size="8.5">Recency: Task at End</text>
          <text x="455" y="76" text-anchor="middle" class="text-mono" font-size="8.5" fill="#b4a4e5">Evidence Token Budget</text>
          <text x="455" y="92" text-anchor="middle" class="text-dim" font-size="8.5">Deduplicate Overlaps</text>
          <text x="455" y="108" text-anchor="middle" class="text-mono" font-size="8.5" fill="#60a5fa">Top-5 Chunks Packed</text>

          <path d="M 575 60 L 540 60" stroke="#6ee7b7" stroke-width="1.2" marker-end="url(#arr-green)"/>

          <!-- Cross-Encoder Reranker -->
          <rect x="580" width="195" height="125" rx="6" fill="#1b2434" stroke="#b4a4e5" stroke-width="1.2"/>
          <text x="677" y="24" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#b4a4e5">Cross-Encoder Reranker</text>
          <text x="677" y="44" text-anchor="middle" class="text-p" font-size="9">Takes Top-50 Hybrid Candidates</text>
          <text x="677" y="60" text-anchor="middle" class="text-dim" font-size="8.5">Runs joint self-attention across pairs</text>
          <text x="677" y="76" text-anchor="middle" class="text-mono" font-size="8.5" fill="#6ee7b7">NDCG@5 Precision Boost</text>
          <text x="677" y="92" text-anchor="middle" class="text-dim" font-size="8.5">Latency: ~35ms compute budget</text>
          <text x="677" y="108" text-anchor="middle" class="text-mono" font-size="8.5" fill="#e0c58e">Prunes 90% of noise</text>
        </g>
      </g>
    </svg>"""
}
