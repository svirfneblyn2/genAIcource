# Slide 25: End-to-End Enterprise Case Study
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 25,
    "kicker": "ENTERPRISE ARCHITECTURE",
    "title": "Production Case Study: Autonomous Financial Reconciliation",
    "lead": "A resilient multi-agent graph with OCR extraction, ERP integration, anomaly checks, and HITL authorization.",
    "section": "Production Case Study",
    "takeaway": "Enterprise agents succeed when deterministic business rules, cyclic graphs, and HITL gateways unite.",
    "notes": {
        "goal": "Synthesize all concepts from Module 02 into a complete production architecture for autonomous accounts payable.",
        "talkTrack": "Here is the unified architecture of a production reconciliation agent processing 50,000 invoices a month. An invoice PDF triggers the graph. Node 1 extracts text. Node 2 queries the ERP database in an isolated sandbox. Node 3 runs the reconciliation logic. If there is a $0 variance, it posts directly to the ledger. But if variance exceeds $0, or if confidence drops below 95%, the graph hits an interrupt barrier and waits for human approval in Postgres.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("pipeline", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Enterprise Multi-Agent Blueprint: Autonomous Accounts Payable</text>

        <g transform="translate(20, 60)">
          <!-- Swimlane 1: Ingestion & Extraction -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="220" height="230" rx="6" class="node-box"/>
            <rect x="0" y="0" width="220" height="28" rx="6" fill="#1b2434"/>
            <text x="14" y="18" class="text-mono" font-size="10.5">1. INGEST &amp; OCR</text>
            
            <g transform="translate(12, 40)">
              <text x="0" y="14" class="text-p">&bull; PDF arrives via S3 bucket</text>
              <text x="0" y="32" class="text-p">&bull; Document AI / Textract</text>
              <text x="0" y="50" class="text-dim">Extracts: Lines, Tax, Total</text>

              <rect x="0" y="70" width="196" height="50" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="8" y="88" class="text-mono-green" font-size="9">InvoiceState(</text>
              <text x="14" y="104" class="text-mono" font-size="8.5">total=14500.0, vendor="Acme")</text>

              <text x="0" y="145" class="text-mono-green" font-size="9.5">State Initialized</text>
            </g>
          </g>

          <path d="M 220 115 L 245 115" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Swimlane 2: ERP Lookup Tool -->
          <g transform="translate(250, 0)">
            <rect x="0" y="0" width="230" height="230" rx="6" class="node-box-active-green"/>
            <rect x="0" y="0" width="230" height="28" rx="6" fill="#152420"/>
            <text x="14" y="18" class="text-mono-green" font-size="10.5">2. ERP LOOKUP (SANDBOX)</text>

            <g transform="translate(12, 40)">
              <text x="0" y="14" class="text-p">&bull; Queries SAP / NetSuite</text>
              <text x="0" y="32" class="text-p">&bull; Read-only SQL connection</text>
              <text x="0" y="50" class="text-dim">Matches PO-8821 lines</text>

              <rect x="0" y="70" width="206" height="50" rx="4" fill="#0b1018" stroke="#253245"/>
              <text x="8" y="88" class="text-mono-green" font-size="9">PO_Record(</text>
              <text x="14" y="104" class="text-mono" font-size="8.5">authorized_amt=14500.0)</text>

              <text x="0" y="145" class="text-mono-green" font-size="9.5">Tool Return Appended</text>
            </g>
          </g>

          <path d="M 480 115 L 505 115" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Swimlane 3: Reconciliation Reasoner -->
          <g transform="translate(510, 0)">
            <rect x="0" y="0" width="250" height="230" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="250" height="28" rx="6" fill="#1e2c42"/>
            <text x="14" y="18" class="text-mono" font-size="10.5">3. RECONCILIATION NODE</text>

            <g transform="translate(12, 40)">
              <text x="0" y="14" class="text-p">&bull; Computes variance</text>
              <text x="0" y="32" class="text-p">&bull; Checks tax rules &amp; fraud</text>
              <text x="0" y="50" class="text-dim">Model evaluates policy</text>

              <!-- Diamond Decision -->
              <polygon points="110,65 170,95 110,125 50,95" fill="#1e293b" stroke="#e0c58e" stroke-width="1.5"/>
              <text x="110" y="99" text-anchor="middle" class="text-mono-amber" font-size="9">VARIANCE?</text>
            </g>
          </g>

          <!-- Branch A: Match (Direct to Ledger) -->
          <path d="M 680 95 L 750 45" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>
          <text x="690" y="60" class="text-mono-green" font-size="9">$0 Variance</text>

          <g transform="translate(760, 10)">
            <rect x="0" y="0" width="460" height="90" rx="6" class="node-box-active-green"/>
            <text x="14" y="24" class="text-mono-green" font-size="11">AUTO-APPROVE: POST TO GENERAL LEDGER</text>
            <text x="14" y="46" class="text-p">Variance == $0.00 &amp; Confidence &gt;= 95%. Automated journal entry created.</text>
            <text x="14" y="66" class="text-dim">Total runtime: 1,850ms &bull; Zero human touches required.</text>
          </g>

          <!-- Branch B: Mismatch / HITL -->
          <path d="M 680 120 L 750 170" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>
          <text x="690" y="160" class="text-mono-amber" font-size="9">Variance &gt; $0</text>

          <g transform="translate(760, 125)">
            <rect x="0" y="0" width="460" height="105" rx="6" class="node-box-active-amber"/>
            <text x="14" y="24" class="text-mono-amber" font-size="11">HITL GATEWAY: INTERRUPT &amp; REVIEW</text>
            <text x="14" y="46" class="text-p">Variance &gt; $0.00. Graph pauses (interrupt_before=['post_ledger']).</text>
            <text x="14" y="66" class="text-p">Webhook dispatched to Slack. AP Manager reviews discrepancy in UI.</text>
            <text x="14" y="86" class="text-mono-green" font-size="9.5">State frozen in Postgres checkpointer awaiting human signoff.</text>
          </g>
        </g>

        <!-- Bottom Infrastructure & Persistence Bar -->
        <g transform="translate(20, 310)">
          <rect x="0" y="0" width="1220" height="65" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="22" class="text-mono" font-size="10.5" fill="#64748b">SUPPORTING ARCHITECTURE:</text>
          <g transform="translate(16, 30)">
            {render_logo_badge("postgres", 0, 0, "PostgresSaver (JSONB)", 180, 26, color="#60a5fa")}
            {render_logo_badge("docker", 195, 0, "E2B Sandbox (SQL Isolation)", 220, 26, color="#6ee7b7")}
            {render_logo_badge("opentelemetry", 430, 0, "OpenTelemetry Spans", 180, 26, color="#e0c58e")}
            {render_logo_badge("langsmith", 625, 0, "LangSmith Studio", 160, 26, color="#b4a4e5")}
          </g>
        </g>
      </g>
    """)
}
