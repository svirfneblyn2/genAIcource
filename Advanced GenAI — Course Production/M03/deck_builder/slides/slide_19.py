# -*- coding: utf-8 -*-
slide_data = {
    "index": 19,
    "badge": "FINANCIAL ENGINEERING",
    "title": "Production TCO: The 5 Cost Pillars of Enterprise RAG",
    "subtitle": "Raw token cost is only one bar: dissecting the complete monthly infrastructure bill.",
    "takeaway_tag": "TCO BREAKDOWN",
    "takeaway": "At moderate traffic, vector database minimums and telemetry storage often exceed LLM token costs.",
    "notes": """
      <h4>Cost Pillars</h4>
      <p>Detail the 5 cost drivers: Vector DB capacity, Embedding generation, Reranker compute, LLM tokens, and Observability log retention.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 25)">
        <rect width="780" height="300" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="780" height="34" rx="8" fill="#1b2434"/>
        <text x="390" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#e0c58e">ENTERPRISE RAG MONTHLY INFRASTRUCTURE BILL</text>

        <g transform="translate(30, 50)">
          <!-- Pillar 1 -->
          <g transform="translate(0, 0)">
            <rect width="135" height="150" rx="4" fill="#1b2434" stroke="#60a5fa" stroke-width="1.2"/>
            <text x="67" y="22" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#60a5fa">Pillar 1</text>
            <text x="67" y="42" text-anchor="middle" class="text-h1" font-size="11">Vector Index</text>
            <text x="67" y="60" text-anchor="middle" class="text-dim" font-size="9">OpenSearch / Pinecone</text>
            <rect x="15" y="80" width="105" height="50" rx="3" fill="#0e131b"/>
            <text x="67" y="100" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#e0c58e">$250 - $700</text>
            <text x="67" y="118" text-anchor="middle" class="text-dim" font-size="8.5">Min compute floor</text>
          </g>

          <!-- Pillar 2 -->
          <g transform="translate(150, 0)">
            <rect width="135" height="150" rx="4" fill="#1b2434" stroke="#b4a4e5" stroke-width="1.2"/>
            <text x="67" y="22" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#b4a4e5">Pillar 2</text>
            <text x="67" y="42" text-anchor="middle" class="text-h1" font-size="11">Embeddings</text>
            <text x="67" y="60" text-anchor="middle" class="text-dim" font-size="9">Doc Ingestion Updates</text>
            <rect x="15" y="80" width="105" height="50" rx="3" fill="#0e131b"/>
            <text x="67" y="100" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#e0c58e">$20 - $80</text>
            <text x="67" y="118" text-anchor="middle" class="text-dim" font-size="8.5">Per 10M tokens</text>
          </g>

          <!-- Pillar 3 -->
          <g transform="translate(300, 0)">
            <rect width="135" height="150" rx="4" fill="#1b2434" stroke="#e0c58e" stroke-width="1.2"/>
            <text x="67" y="22" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#e0c58e">Pillar 3</text>
            <text x="67" y="42" text-anchor="middle" class="text-h1" font-size="11">Reranker</text>
            <text x="67" y="60" text-anchor="middle" class="text-dim" font-size="9">Cross-Encoder Service</text>
            <rect x="15" y="80" width="105" height="50" rx="3" fill="#0e131b"/>
            <text x="67" y="100" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#e0c58e">$80 - $220</text>
            <text x="67" y="118" text-anchor="middle" class="text-dim" font-size="8.5">Hosted GPU container</text>
          </g>

          <!-- Pillar 4 -->
          <g transform="translate(450, 0)">
            <rect width="135" height="150" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
            <text x="67" y="22" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#6ee7b7">Pillar 4</text>
            <text x="67" y="42" text-anchor="middle" class="text-h1" font-size="11">LLM Inference</text>
            <text x="67" y="60" text-anchor="middle" class="text-dim" font-size="9">Context + Output</text>
            <rect x="15" y="80" width="105" height="50" rx="3" fill="#0e131b"/>
            <text x="67" y="100" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#e0c58e">$150 - $450</text>
            <text x="67" y="118" text-anchor="middle" class="text-dim" font-size="8.5">Prompt cache discount</text>
          </g>

          <!-- Pillar 5 -->
          <g transform="translate(600, 0)">
            <rect width="120" height="150" rx="4" fill="#1b2434" stroke="#d98585" stroke-width="1.2"/>
            <text x="60" y="22" text-anchor="middle" class="text-mono-bold" font-size="10" fill="#d98585">Pillar 5</text>
            <text x="60" y="42" text-anchor="middle" class="text-h1" font-size="11">Telemetry</text>
            <text x="60" y="60" text-anchor="middle" class="text-dim" font-size="9">OTel Traces &amp; Logs</text>
            <rect x="10" y="80" width="100" height="50" rx="3" fill="#0e131b"/>
            <text x="60" y="100" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#e0c58e">$60 - $180</text>
            <text x="60" y="118" text-anchor="middle" class="text-dim" font-size="8.5">Trace storage 30d</text>
          </g>
        </g>

        <!-- Summary Footer Banner -->
        <g transform="translate(30, 220)">
          <rect width="720" height="55" rx="4" fill="#0e131b" stroke="#e0c58e" stroke-width="1"/>
          <text x="20" y="24" class="text-mono-bold" font-size="11" fill="#e0c58e">ARCHITECTURAL TAKEAWAY:</text>
          <text x="20" y="42" class="text-p" font-size="10">Model tokens represent only 25-35% of the total monthly production bill at standard corporate volumes.</text>
        </g>
      </g>
    </svg>"""
}
