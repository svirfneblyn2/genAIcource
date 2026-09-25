# Slide 20: Evaluation & Observability: The Closed-Loop Lifecycle
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 20,
    "kicker": "PRODUCTION RELIABILITY",
    "title": "The Production Feedback Loop: Eval, Trace, & Mitigate",
    "lead": "If you cannot trace a bad answer, you cannot operate an enterprise AI system.",
    "section": "Evaluation & Observability",
    "takeaway": "Evaluation is not a one-time test: it is the continuous CI/CD control gate for non-deterministic software.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 20)">
        <!-- Top Half: Circular Lifecycle Nodes -->
        <!-- Step 1: Golden Dataset -->
        <g transform="translate(0, 15)">
          <rect x="0" y="0" width="220" height="155" rx="8" class="node-box"/>
          <rect x="0" y="0" width="220" height="36" rx="8" fill="#1b2434"/>
          {render_icon("documents", 12, 8, size=20, color="#60a5fa")}
          <text x="38" y="24" class="text-h2" fill="#60a5fa">1. Curated Golden Set</text>
          
          <text x="14" y="58" class="text-p">100-500 Verified Q&amp;A pairs</text>
          <text x="14" y="80" class="text-p">Edge cases &amp; negative queries</text>
          <text x="14" y="102" class="text-p">Grounded ground truth chunks</text>
          
          <rect x="12" y="118" width="196" height="26" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="110" y="135" text-anchor="middle" class="text-mono" font-size="11">Versioned in Git / S3</text>
        </g>

        <path d="M 230 92 L 265 92" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

        <!-- Step 2: Automated Eval Run -->
        <g transform="translate(275, 15)">
          <rect x="0" y="0" width="220" height="155" rx="8" class="node-box-active" stroke="#b4a4e5"/>
          <rect x="0" y="0" width="220" height="36" rx="8" fill="#221c32"/>
          {render_icon("evaluation", 12, 8, size=20, color="#b4a4e5")}
          <text x="38" y="24" class="text-h2" fill="#b4a4e5">2. Model-as-a-Judge</text>
          
          <text x="14" y="58" class="text-p">Faithfulness / Groundedness</text>
          <text x="14" y="80" class="text-p">Context Recall &amp; Precision</text>
          <text x="14" y="102" class="text-p">Answer Semantic Similarity</text>
          
          <rect x="12" y="118" width="196" height="26" rx="4" fill="#17182a" stroke="#b4a4e5" stroke-width="1.2"/>
          <text x="110" y="135" text-anchor="middle" class="text-mono-purple" font-size="11">Automated Scoring Batch</text>
        </g>

        <path d="M 505 92 L 540 92" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>

        <!-- Step 3: CI/CD Release Gate -->
        <g transform="translate(550, 15)">
          <rect x="0" y="0" width="220" height="155" rx="8" class="node-box" stroke="#6ee7b7"/>
          <rect x="0" y="0" width="220" height="36" rx="8" fill="#162924"/>
          {render_icon("approval", 12, 8, size=20, color="#6ee7b7")}
          <text x="38" y="24" class="text-h2" fill="#6ee7b7">3. Release Gate</text>
          
          <text x="14" y="58" class="text-p">Pass: Groundedness &gt; 92%</text>
          <text x="14" y="80" class="text-p">Pass: Hallucination &lt; 2%</text>
          <text x="14" y="102" class="text-p">Pass: Latency p95 &lt; 2.5s</text>
          
          <rect x="12" y="118" width="196" height="26" rx="4" fill="#14241e" stroke="#6ee7b7" stroke-width="1.2"/>
          <text x="110" y="135" text-anchor="middle" class="text-mono-green" font-size="11">CI/CD Pipeline Gate</text>
        </g>

        <path d="M 780 92 L 815 92" stroke="#6ee7b7" stroke-width="2" fill="none" marker-end="url(#arr-green)"/>

        <!-- Step 4: Production Telemetry -->
        <g transform="translate(825, 15)">
          <rect x="0" y="0" width="215" height="155" rx="8" class="node-box"/>
          <rect x="0" y="0" width="215" height="36" rx="8" fill="#1b2434"/>
          {render_icon("monitoring", 12, 8, size=20, color="#e0c58e")}
          <text x="38" y="24" class="text-h2" fill="#e0c58e">4. Live Traces</text>
          
          <text x="14" y="58" class="text-p">OTel distributed spans</text>
          <text x="14" y="80" class="text-p">User feedback (thumbs +/-)</text>
          <text x="14" y="102" class="text-p">Token &amp; latency tracking</text>
          
          <rect x="12" y="118" width="191" height="26" rx="4" fill="#141c28" stroke="#253245"/>
          <text x="107" y="135" text-anchor="middle" class="text-mono-amber" font-size="11">CloudWatch / AppInsights</text>
        </g>

        <!-- Feedback Loop Path Back -->
        <path d="M 932 175 L 932 205 L 110 205 L 110 175" stroke="#d98585" stroke-width="2" stroke-dasharray="5 3" fill="none" marker-end="url(#arr-coral)"/>
        <rect x="420" y="193" width="200" height="24" rx="4" fill="#1e1820" stroke="#d98585"/>
        <text x="520" y="209" text-anchor="middle" class="text-mono-coral" font-size="11">FAILURE RE-INGESTION LOOP</text>

        <!-- Bottom Half: Failure Diagnostics & Mitigation Grid -->
        <g transform="translate(0, 235)">
          <rect x="0" y="0" width="1040" height="160" rx="8" class="swimlane-bg"/>
          <text x="20" y="26" class="text-mono" font-size="12" fill="#cbd5e1">THREE CRITICAL EVALUATION PILLARS (RAG TRIAD)</text>

          <g transform="translate(20, 40)">
            <!-- Triad 1 -->
            <rect x="0" y="0" width="315" height="105" rx="6" fill="#141c28" stroke="#253245"/>
            <text x="16" y="24" class="text-h2" fill="#60a5fa">1. Groundedness (Faithfulness)</text>
            <text x="16" y="48" class="text-p">Is every generated claim directly supported by the retrieved chunk?</text>
            <text x="16" y="70" class="text-dim">Catches model hallucinations and false inferences.</text>
            <text x="16" y="92" class="text-mono" font-size="11">Automated prompt-judge metric</text>

            <!-- Triad 2 -->
            <g transform="translate(340, 0)">
              <rect x="0" y="0" width="320" height="105" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="16" y="24" class="text-h2" fill="#6ee7b7">2. Context Relevance (Recall)</text>
              <text x="16" y="48" class="text-p">Did the retrieval step return the exact policy paragraph required?</text>
              <text x="16" y="70" class="text-dim">Catches poor chunking, outdated indexes, or bad embeddings.</text>
              <text x="16" y="92" class="text-mono-green" font-size="11">Retrieval pipeline verification</text>
            </g>

            <!-- Triad 3 -->
            <g transform="translate(685, 0)">
              <rect x="0" y="0" width="315" height="105" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="16" y="24" class="text-h2" fill="#b4a4e5">3. Answer Relevance</text>
              <text x="16" y="48" class="text-p">Does the synthesized text directly address the user inquiry?</text>
              <text x="16" y="70" class="text-dim">Catches conversational drift and polite refusal boilerplate.</text>
              <text x="16" y="92" class="text-mono-purple" font-size="11">End-to-end user satisfaction</text>
            </g>
          </g>
        </g>
      </g>
    """),
    "notes": {
        "goal": "Connect test datasets, pre-release evals, CI/CD release gates, runtime traces, and failure analysis into one continuous engineering lifecycle.",
        "talkTrack": "Walk around the evaluation loop. A production AI system needs test datasets before release, evaluation runs, release gates, runtime traces, failure analysis, and fixes. If you cannot trace a bad answer, you cannot operate the system. The RAG Triad (Groundedness, Context Relevance, and Answer Relevance) gives you the mathematical metrics to prevent regressions before code hits staging.",
        "timing": "95:00 - 100:00 (5 min)"
    }
}
