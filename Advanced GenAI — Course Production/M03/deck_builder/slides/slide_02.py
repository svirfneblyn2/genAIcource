# -*- coding: utf-8 -*-
slide_data = {
    "index": 2,
    "badge": "SYSTEMS MENTAL MODEL",
    "title": "Parametric Weights vs Dynamic Retrieval Memory",
    "subtitle": "Why enterprise applications must decouple knowledge storage from language reasoning.",
    "takeaway_tag": "MEMORY DUALITY",
    "takeaway": "Parametric weights store language logic: external indexes store factual truth.",
    "notes": """
      <h4>Key Mental Model</h4>
      <p>Contrast internal synaptic weights with external vector memory. Weights are frozen, expensive to modify, and probabilistic. RAG is instant, inspectable, and access-controlled.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left Box: Parametric Weights -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="36" rx="8" fill="#1b2434"/>
        <text x="20" y="24" class="text-h1" font-size="13" fill="#d98585">Internal Parametric Memory (LLM Weights)</text>
        
        <g transform="translate(20, 52)">
          <rect width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="20" class="text-mono" font-size="10.5" fill="#e2e8f0">Update Latency: Hours to Days</text>
          <text x="14" y="34" class="text-dim" font-size="9">Requires retraining, fine-tuning, or alignment checkpoint</text>

          <rect y="50" width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="70" class="text-mono" font-size="10.5" fill="#e2e8f0">Access Control: Impossible (Global Leak)</text>
          <text x="14" y="84" class="text-dim" font-size="9">Weights cannot enforce per-user tenant or role boundaries</text>

          <rect y="100" width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="120" class="text-mono" font-size="10.5" fill="#e2e8f0">Factual Verifiability: Opaque Black Box</text>
          <text x="14" y="134" class="text-dim" font-size="9">Cannot audit exact origin file or paragraph for claims</text>

          <rect y="150" width="320" height="66" rx="4" fill="#1b2434" stroke="#d98585" stroke-width="1.2"/>
          <text x="14" y="172" class="text-mono-bold" font-size="11" fill="#d98585">Failure Mode: Fluent Hallucination</text>
          <text x="14" y="190" class="text-p" font-size="9.5">Generates statistically plausible text that is factually false</text>
          <text x="14" y="204" class="text-dim" font-size="8.5">Silent failure: user cannot distinguish fact from fiction</text>
        </g>
      </g>

      <!-- Center VS Divider -->
      <circle cx="430" cy="175" r="20" fill="#1b2434" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="430" y="180" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#60a5fa">VS</text>

      <!-- Right Box: Non-Parametric Memory -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#253245" stroke-width="1.2"/>
        <rect width="360" height="36" rx="8" fill="#1b2434"/>
        <text x="20" y="24" class="text-h1" font-size="13" fill="#6ee7b7">External Non-Parametric Memory (Vector Store)</text>

        <g transform="translate(20, 52)">
          <rect width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="20" class="text-mono" font-size="10.5" fill="#e2e8f0">Update Latency: Milliseconds</text>
          <text x="14" y="34" class="text-dim" font-size="9">Instant document insert, update, or tombstone deletion</text>

          <rect y="50" width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="70" class="text-mono" font-size="10.5" fill="#e2e8f0">Access Control: Strict Role Pre-Filtering</text>
          <text x="14" y="84" class="text-dim" font-size="9">Metadata tags enforce tenant and user permissions</text>

          <rect y="100" width="320" height="42" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="14" y="120" class="text-mono" font-size="10.5" fill="#e2e8f0">Factual Verifiability: Cryptographic Audit</text>
          <text x="14" y="134" class="text-dim" font-size="9">Every statement links to doc_id, section, and version tag</text>

          <rect y="150" width="320" height="66" rx="4" fill="#1b2434" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="14" y="172" class="text-mono-bold" font-size="11" fill="#6ee7b7">Safe Failure: Explicit Refusal</text>
          <text x="14" y="190" class="text-p" font-size="9.5">States 'Insufficient evidence in approved policy'</text>
          <text x="14" y="204" class="text-dim" font-size="8.5">Deterministic failure boundary prevents compliance incidents</text>
        </g>
      </g>
    </svg>"""
}
