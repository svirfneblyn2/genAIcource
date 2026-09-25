# -*- coding: utf-8 -*-
slide_data = {
    "index": 16,
    "badge": "ATTRIBUTION & INTEGRITY",
    "title": "Grounding & Verifiable Citations: System Guardrails",
    "subtitle": "Enforcing inline source attribution and deterministic refusal on out-of-domain queries.",
    "takeaway_tag": "CITATION DEFENSE",
    "takeaway": "An answer without citations is an unverified assertion: mandatory refusal stops hallucinations.",
    "notes": """
      <h4>Citation Protocol</h4>
      <p>Demonstrate the structure: every factual assertion ends in [Source: doc_id § section]. If evidence is missing, model is strictly commanded to refuse rather than extrapolate.</p>
    """,
    "svg": """<svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Citation Enforcement -->
      <g transform="translate(40, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#6ee7b7" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#6ee7b7">INLINE CITATION SPECIFICATION</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="75" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10" fill="#6ee7b7">Synthesized Assistant Output:</text>
          <text x="12" y="42" class="text-p" font-size="9.5">"You may borrow a loaner laptop for up to 14 days"</text>
          <text x="12" y="58" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">[Source: POL-IT-101 § Section 2]</text>

          <rect y="85" width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10" fill="#6ee7b7">Multi-Source Fact Attribution:</text>
          <text x="12" y="40" class="text-p" font-size="9.5">"Extensions require Department Head approval"</text>
          <text x="12" y="54" class="text-mono-bold" font-size="9.5" fill="#6ee7b7">[Source: POL-IT-101 § Section 2.3]</text>

          <rect y="155" width="320" height="65" rx="4" fill="#1b2434" stroke="#6ee7b7"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10" fill="#6ee7b7">Automated Audit Verification:</text>
          <text x="12" y="40" class="text-p" font-size="9">+ Regex parser checks citation presence</text>
          <text x="12" y="54" class="text-p" font-size="9">+ Verifies doc_id exists in retrieved candidate set</text>
        </g>
      </g>

      <!-- Right: Refusal Guardrail -->
      <g transform="translate(460, 30)">
        <rect width="360" height="290" rx="8" fill="#141c28" stroke="#d98585" stroke-width="1.2"/>
        <rect width="360" height="34" rx="8" fill="#1b2434"/>
        <text x="180" y="22" text-anchor="middle" class="text-mono-bold" font-size="11" fill="#d98585">DETERMINISTIC REFUSAL GUARDRAIL</text>

        <g transform="translate(20, 50)">
          <rect width="320" height="60" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="10" fill="#d98585">Out-of-Scope Employee Query:</text>
          <text x="12" y="40" class="text-h1" font-size="10">"Can I bring my pet iguana to the office?"</text>

          <rect y="70" width="320" height="65" rx="4" fill="#0e131b" stroke="#253245"/>
          <text x="12" y="20" class="text-mono" font-size="10" fill="#e0c58e">Retrieval Score Threshold Check:</text>
          <text x="12" y="38" class="text-dim" font-size="9.5">Max Cosine Score = 0.18 (Below 0.45 cutoff)</text>
          <text x="12" y="52" class="text-mono" font-size="9.5" fill="#d98585">Condition: ZERO VALID EVIDENCE</text>

          <rect y="145" width="320" height="75" rx="4" fill="#1b2434" stroke="#d98585"/>
          <text x="12" y="22" class="text-mono-bold" font-size="10" fill="#d98585">Enforced Refusal Template:</text>
          <text x="12" y="42" class="text-p" font-size="9.5">"I cannot find evidence in the approved company policy</text>
          <text x="12" y="56" class="text-p" font-size="9.5">to answer this question. Please contact HR Desk."</text>
          <text x="12" y="68" class="text-mono" font-size="8.5" fill="#6ee7b7">[HALLUCINATION SAFELY PREVENTED]</text>
        </g>
      </g>
    </svg>"""
}
