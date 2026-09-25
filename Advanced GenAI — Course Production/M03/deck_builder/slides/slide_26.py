# -*- coding: utf-8 -*-
slide_data = {
    "index": 26,
    "badge": "PRODUCTION READINESS",
    "title": "Architectural Checklist: The 7 Production Gates",
    "subtitle": "Essential verification gates before deploying any enterprise RAG workload.",
    "takeaway_tag": "PRODUCTION GATES",
    "takeaway": "A RAG system is only as reliable as its parsing boundaries, ACL filters, and evaluation suite.",
    "notes": """
      <h4>Final Synthesis & Checklist</h4>
      <p>Review the 7 gates: Structure-aware chunking, Hard ACL pre-filtering, Hybrid RRF retrieval, Cross-encoder reranking, Boundary prompt assembly, Mandatory refusal guardrails, and Automated CI/CD evaluation.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 25)">
        <rect width="780" height="300" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="780" height="34" rx="8" fill="#1b2434"/>
        <text x="390" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">THE 7 ENTERPRISE RAG PRODUCTION GATES</text>

        <g transform="translate(25, 48)">
          <!-- Gate 1 -->
          <g transform="translate(0, 0)">
            <rect width="355" height="48" rx="4" fill="#0e131b" stroke="#253245"/>
            <circle cx="20" cy="24" r="8" fill="#6ee7b7"/>
            <text x="20" y="28" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">1</text>
            <text x="36" y="20" class="text-mono-bold" font-size="10" fill="#f8fafc">Structure-Aware Parsing</text>
            <text x="36" y="34" class="text-dim" font-size="8.5">Headings preserved; table rows kept with headers</text>
          </g>

          <!-- Gate 2 -->
          <g transform="translate(375, 0)">
            <rect width="355" height="48" rx="4" fill="#0e131b" stroke="#253245"/>
            <circle cx="20" cy="24" r="8" fill="#6ee7b7"/>
            <text x="20" y="28" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">2</text>
            <text x="36" y="20" class="text-mono-bold" font-size="10" fill="#f8fafc">Hard Metadata Pre-Filtering</text>
            <text x="36" y="34" class="text-dim" font-size="8.5">Tenant and role ACL checked before vector search</text>
          </g>

          <!-- Gate 3 -->
          <g transform="translate(0, 58)">
            <rect width="355" height="48" rx="4" fill="#0e131b" stroke="#253245"/>
            <circle cx="20" cy="24" r="8" fill="#6ee7b7"/>
            <text x="20" y="28" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">3</text>
            <text x="36" y="20" class="text-mono-bold" font-size="10" fill="#f8fafc">Hybrid Search (Dense + BM25)</text>
            <text x="36" y="34" class="text-dim" font-size="8.5">Fused via Reciprocal Rank Fusion (k=60)</text>
          </g>

          <!-- Gate 4 -->
          <g transform="translate(375, 58)">
            <rect width="355" height="48" rx="4" fill="#0e131b" stroke="#253245"/>
            <circle cx="20" cy="24" r="8" fill="#6ee7b7"/>
            <text x="20" y="28" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">4</text>
            <text x="36" y="20" class="text-mono-bold" font-size="10" fill="#f8fafc">Cross-Encoder Precision Reranking</text>
            <text x="36" y="34" class="text-dim" font-size="8.5">Reranks top-50 down to top-5 highest confidence</text>
          </g>

          <!-- Gate 5 -->
          <g transform="translate(0, 116)">
            <rect width="355" height="48" rx="4" fill="#0e131b" stroke="#253245"/>
            <circle cx="20" cy="24" r="8" fill="#6ee7b7"/>
            <text x="20" y="28" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">5</text>
            <text x="36" y="20" class="text-mono-bold" font-size="10" fill="#f8fafc">Boundary Context Assembly</text>
            <text x="36" y="34" class="text-dim" font-size="8.5">Top evidence at start; schema &amp; task at end</text>
          </g>

          <!-- Gate 6 -->
          <g transform="translate(375, 116)">
            <rect width="355" height="48" rx="4" fill="#0e131b" stroke="#253245"/>
            <circle cx="20" cy="24" r="8" fill="#6ee7b7"/>
            <text x="20" y="28" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">6</text>
            <text x="36" y="20" class="text-mono-bold" font-size="10" fill="#f8fafc">Citations &amp; Mandatory Refusal</text>
            <text x="36" y="34" class="text-dim" font-size="8.5">Every fact cited; explicit refusal when evidence is missing</text>
          </g>

          <!-- Gate 7 -->
          <g transform="translate(0, 174)">
            <rect width="730" height="58" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
            <circle cx="20" cy="29" r="8" fill="#6ee7b7"/>
            <text x="20" y="33" text-anchor="middle" class="text-mono-bold" font-size="9" fill="#0e131b">7</text>
            <text x="36" y="24" class="text-mono-bold" font-size="10.5" fill="#6ee7b7">Continuous CI/CD Automated Evaluation Suite (Ragas / TruLens)</text>
            <text x="36" y="42" class="text-dim" font-size="9">Regression gates: Recall@5 &gt; 85%, Faithfulness &gt; 95%, Answer Relevance &gt; 88%</text>
          </g>
        </g>
      </g>
    </svg>"""
}
