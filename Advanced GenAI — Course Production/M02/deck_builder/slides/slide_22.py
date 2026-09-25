# Slide 22: Production Observability
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon
from ..logos import render_logo_badge

SLIDE_DATA = {
    "index": 22,
    "kicker": "OBSERVABILITY & TRACING",
    "title": "Distributed Tracing: OpenTelemetry, LangSmith, and Phoenix",
    "lead": "Instrumenting multi-step agent runs with span hierarchies, latency waterfalls, and token accounting.",
    "section": "Production Observability",
    "takeaway": "Agent observability requires graph-aware tracing: inspect every intermediate node input, model call, and tool execution.",
    "notes": {
        "goal": "Explain how distributed tracing works across cyclic agent runtimes, standardizing on OpenTelemetry semantic conventions.",
        "talkTrack": "Observing an agent is fundamentally different from observing a microservice. An HTTP request enters, but inside the agent, 12 sequential model inferences and 8 tool calls may fire. When an error occurs, you cannot just look at the final HTTP 500. You need a distributed waterfall trace. Every node, model invocation, and tool call must produce an OpenTelemetry span containing token counts, latency, and sanitized payloads.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box-active"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1e2c42"/>
        {render_icon("trace", 15, 10, size=24, color="#60a5fa")}
        <text x="48" y="28" class="text-h1" fill="#60a5fa">Graph-Aware Distributed Trace Waterfall &amp; Telemetry Bus</text>

        <!-- Left: Trace Waterfall Visualization -->
        <g transform="translate(20, 60)">
          <rect x="0" y="0" width="760" height="320" rx="6" fill="#0b1018" stroke="#253245"/>
          <text x="16" y="24" class="text-mono" font-size="10.5" fill="#64748b">TRACE_ID: 4bf92f3577b34da6a3ce929d0e0e4736 (Total: 4,820ms &bull; 12.4k tokens &bull; $0.038)</text>

          <!-- Root Span -->
          <g transform="translate(16, 40)">
            <rect x="0" y="0" width="728" height="36" rx="4" fill="#172233" stroke="#3b82f6"/>
            <text x="12" y="22" class="text-mono" font-size="10" fill="#60a5fa">Root Span: Graph.invoke(ReconcileInvoiceWorkflow)</text>
            <text x="630" y="22" class="text-mono" font-size="10" fill="#cbd5e1">4,820ms</text>
          </g>

          <!-- Child Span 1: Model Planner -->
          <g transform="translate(40, 85)">
            <rect x="0" y="0" width="280" height="34" rx="4" fill="#1e2c42" stroke="#60a5fa"/>
            <text x="10" y="22" class="text-mono" font-size="9.5" fill="#e2e8f0">1. Node: supervisor_plan (LLM)</text>
            <text x="215" y="22" class="text-mono" font-size="9.5" fill="#6ee7b7">850ms</text>
          </g>

          <!-- Child Span 2: Tool OCR -->
          <g transform="translate(180, 128)">
            <rect x="0" y="0" width="240" height="34" rx="4" fill="#152420" stroke="#6ee7b7"/>
            <text x="10" y="22" class="text-mono-green" font-size="9.5">2. Tool: doc_ai_ocr (HTTP)</text>
            <text x="175" y="22" class="text-mono" font-size="9.5" fill="#6ee7b7">1,200ms</text>
          </g>

          <!-- Child Span 3: Tool ERP -->
          <g transform="translate(320, 171)">
            <rect x="0" y="0" width="180" height="34" rx="4" fill="#152420" stroke="#6ee7b7"/>
            <text x="10" y="22" class="text-mono-green" font-size="9.5">3. Tool: erp_match (SQL)</text>
            <text x="125" y="22" class="text-mono" font-size="9.5" fill="#6ee7b7">650ms</text>
          </g>

          <!-- Child Span 4: Final Synthesizer -->
          <g transform="translate(420, 214)">
            <rect x="0" y="0" width="310" height="34" rx="4" fill="#241b33" stroke="#b4a4e5"/>
            <text x="10" y="22" class="text-mono-purple" font-size="9.5">4. Node: synthesizer (LLM Output)</text>
            <text x="245" y="22" class="text-mono" font-size="9.5" fill="#6ee7b7">2,120ms</text>
          </g>

          <!-- Bottom Metric Axis -->
          <g transform="translate(16, 265)">
            <line x1="0" y1="10" x2="728" y2="10" stroke="#253245" stroke-width="1.5"/>
            <text x="0" y="28" class="text-mono" font-size="9" fill="#64748b">0ms</text>
            <text x="180" y="28" class="text-mono" font-size="9" fill="#64748b">1,200ms</text>
            <text x="360" y="28" class="text-mono" font-size="9" fill="#64748b">2,400ms</text>
            <text x="540" y="28" class="text-mono" font-size="9" fill="#64748b">3,600ms</text>
            <text x="700" y="28" class="text-mono" font-size="9" fill="#64748b">4,820ms</text>
          </g>
        </g>

        <!-- Right: OTel Attributes & Platform Badges -->
        <g transform="translate(800, 60)">
          <!-- Span Attributes Box -->
          <rect x="0" y="0" width="440" height="190" rx="6" fill="#141c28" stroke="#3b82f6"/>
          <text x="16" y="24" class="text-mono-green" font-size="11">OTEL GENAI SEMANTIC CONVENTIONS</text>
          
          <g transform="translate(16, 42)">
            <text x="0" y="14" class="text-mono" font-size="9.5" fill="#cbd5e1">gen_ai.system: "langgraph"</text>
            <text x="0" y="32" class="text-mono" font-size="9.5" fill="#cbd5e1">gen_ai.request.model: "claude-3-5-sonnet"</text>
            <text x="0" y="50" class="text-mono" font-size="9.5" fill="#6ee7b7">gen_ai.usage.input_tokens: 10850</text>
            <text x="0" y="68" class="text-mono" font-size="9.5" fill="#6ee7b7">gen_ai.usage.output_tokens: 1550</text>
            <text x="0" y="86" class="text-mono" font-size="9.5" fill="#e0c58e">gen_ai.response.finish_reasons: ["tool_calls"]</text>
            <text x="0" y="104" class="text-mono" font-size="9.5" fill="#60a5fa">thread.id: "usr_reconcile_8921"</text>
            <text x="0" y="122" class="text-mono" font-size="9.5" fill="#60a5fa">checkpoint.id: "1ef892a0b1"</text>
          </g>

          <!-- Ecosystem Compatibility Badges -->
          <g transform="translate(0, 205)">
            <rect x="0" y="0" width="440" height="115" rx="6" fill="#111722" stroke="#253245"/>
            <text x="16" y="24" class="text-mono" font-size="10.5" fill="#64748b">SUPPORTED OBSERVABILITY BACKENDS:</text>
            <g transform="translate(14, 38)">
              {render_logo_badge("langsmith", 0, 0, "LangSmith", 125, 30, color="#60a5fa")}
              {render_logo_badge("opentelemetry", 135, 0, "OpenTelemetry", 145, 30, color="#e0c58e")}
              {render_logo_badge("phoenix", 290, 0, "Arize Phoenix", 120, 30, color="#d98585")}
            </g>
            <text x="16" y="98" class="text-dim" font-size="9.5">Export spans over gRPC/OTLP to Datadog, Honeycomb, or Dynatrace.</text>
          </g>
        </g>
      </g>
    """)
}
