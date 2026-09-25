# -*- coding: utf-8 -*-
slide_data = {
    "index": 21,
    "badge": "INCIDENT TRIAGE",
    "title": "RAG Failure Taxonomy: Root-Cause Analysis (Part 2)",
    "subtitle": "Pinpointing defects across reranking, context assembly, and synthesis stages.",
    "takeaway_tag": "FAILURE TRIAGE 2",
    "takeaway": "Address context crowding and lost-in-the-middle positioning before blaming LLM generation.",
    "notes": """
      <h4>Failure Modes 5-7</h4>
      <p>Break down the final 3 stages: Reranking Fall (valid chunk ranked outside top-5), Context Truncation (lost in middle), and Synthesis Hallucination (model relies on weights over evidence).</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(50, 30)">
        <!-- Stage 5 -->
        <g transform="translate(0, 0)">
          <rect width="235" height="280" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
          <rect width="235" height="32" rx="6" fill="#1b2434"/>
          <text x="117" y="20" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#d98585">5. RERANKING FALL</text>

          <g transform="translate(15, 45)">
            <text x="0" y="16" class="text-mono" font-size="10" fill="#f8fafc">Root Cause:</text>
            <text x="0" y="34" class="text-p" font-size="9.5">Valid chunk pushed out of</text>
            <text x="0" y="48" class="text-p" font-size="9.5">top-5 by peripheral noise</text>
            <text x="0" y="62" class="text-p" font-size="9.5">or low cross-encoder score.</text>

            <rect y="78" width="205" height="52" rx="4" fill="#0e131b"/>
            <text x="10" y="98" class="text-dim" font-size="9">Chunk was in top-50, but</text>
            <text x="10" y="114" class="text-dim" font-size="9">dropped before LLM prompt.</text>

            <text x="0" y="152" class="text-mono-bold" font-size="10" fill="#6ee7b7">Fix:</text>
            <text x="0" y="170" class="text-p" font-size="9">Domain fine-tuned reranker</text>
            <text x="0" y="184" class="text-p" font-size="9">&amp; expand top-k to 8-10 chunks.</text>
          </g>
        </g>

        <!-- Stage 6 -->
        <g transform="translate(265, 0)">
          <rect width="235" height="280" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
          <rect width="235" height="32" rx="6" fill="#1b2434"/>
          <text x="117" y="20" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#d98585">6. CONTEXT OVERLOOK</text>

          <g transform="translate(15, 45)">
            <text x="0" y="16" class="text-mono" font-size="10" fill="#f8fafc">Root Cause:</text>
            <text x="0" y="34" class="text-p" font-size="9.5">Evidence buried in center</text>
            <text x="0" y="48" class="text-p" font-size="9.5">of 16k context window</text>
            <text x="0" y="62" class="text-p" font-size="9.5">(Lost in the Middle decay).</text>

            <rect y="78" width="205" height="52" rx="4" fill="#0e131b"/>
            <text x="10" y="98" class="text-dim" font-size="9">Chunk was inside prompt,</text>
            <text x="10" y="114" class="text-dim" font-size="9">but attention missed it.</text>

            <text x="0" y="152" class="text-mono-bold" font-size="10" fill="#6ee7b7">Fix:</text>
            <text x="0" y="170" class="text-p" font-size="9">Pin top evidence to start;</text>
            <text x="0" y="184" class="text-p" font-size="9">trim context budget aggressively.</text>
          </g>
        </g>

        <!-- Stage 7 -->
        <g transform="translate(530, 0)">
          <rect width="235" height="280" rx="6" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
          <rect width="235" height="32" rx="6" fill="#1b2434"/>
          <text x="117" y="20" text-anchor="middle" class="text-mono-bold" font-size="10.5" fill="#d98585">7. SYNTHESIS HALLUCINATION</text>

          <g transform="translate(15, 45)">
            <text x="0" y="16" class="text-mono" font-size="10" fill="#f8fafc">Root Cause:</text>
            <text x="0" y="34" class="text-p" font-size="9.5">Model overrides evidence</text>
            <text x="0" y="48" class="text-p" font-size="9.5">with pre-trained weights,</text>
            <text x="0" y="62" class="text-p" font-size="9.5">or extrapolates unsupported.</text>

            <rect y="78" width="205" height="52" rx="4" fill="#0e131b"/>
            <text x="10" y="98" class="text-dim" font-size="9">Evidence was present, but</text>
            <text x="10" y="114" class="text-dim" font-size="9">generated claims are false.</text>

            <text x="0" y="152" class="text-mono-bold" font-size="10" fill="#6ee7b7">Fix:</text>
            <text x="0" y="170" class="text-p" font-size="9">Lower temperature to 0.0 &amp;</text>
            <text x="0" y="184" class="text-p" font-size="9">strict citation guardrails.</text>
          </g>
        </g>
      </g>
    </svg>"""
}
