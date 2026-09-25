# Slide 08: Tool Calling Contracts
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 8,
    "kicker": "TOOL EXECUTION",
    "title": "Tool Calling Contracts: JSON Schemas & Type Coercion",
    "lead": "Enforcing strict type boundaries between stochastic model tokens and deterministic business code.",
    "section": "Tools & Sandboxing",
    "takeaway": "The model never runs code directly; it emits structured arguments validated against Pydantic schemas.",
    "notes": {
        "goal": "Demystify function calling mechanics and explain the contract lifecycle between Python code, JSON schema, and model output.",
        "talkTrack": "A common student misconception is that LLMs 'execute tools'. Models do not execute anything. Models generate text tokens. Tool calling is a protocol: runtime tools are serialized to JSON Schema and passed in the API request. When the model determines a tool is needed, it stops generating prose and emits a structured JSON payload matching the schema. The orchestrator intercepts this JSON, validates it with Pydantic, executes the Python code, and feeds the result back as a ToolMessage.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("tool", 15, 10, size=24, color="#6ee7b7")}
        <text x="48" y="28" class="text-h1" fill="#6ee7b7">The End-to-End Function Calling Contract Lifecycle</text>

        <!-- 5 Sequential Stages -->
        <g transform="translate(20, 60)">
          <!-- Stage 1: Tool Declaration -->
          <g transform="translate(0, 0)">
            <rect x="0" y="0" width="225" height="230" rx="6" class="node-box-active"/>
            <text x="14" y="22" class="text-mono" font-size="10.5">1. TOOL DECLARATION</text>
            <rect x="12" y="32" width="200" height="90" rx="4" fill="#0b1018" stroke="#253245"/>
            <text x="18" y="48" class="text-mono" font-size="9.5" fill="#60a5fa">@tool</text>
            <text x="18" y="64" class="text-mono" font-size="9.5" fill="#e0c58e">def get_orders(</text>
            <text x="24" y="80" class="text-mono" font-size="9" fill="#cbd5e1">cust_id: str,</text>
            <text x="24" y="96" class="text-mono" font-size="9" fill="#cbd5e1">limit: int = 10</text>
            <text x="18" y="112" class="text-mono" font-size="9.5" fill="#e0c58e">) -&gt; list[dict]:</text>
            
            <text x="14" y="145" class="text-p">&bull; Typed Python signature</text>
            <text x="14" y="165" class="text-p">&bull; Docstrings define intent</text>
            <text x="14" y="185" class="text-p">&bull; Type hints guide schema</text>
            <text x="14" y="210" class="text-mono-green" font-size="10">Source of Truth</text>
          </g>

          <path d="M 225 115 L 250 115" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Stage 2: JSON Schema -->
          <g transform="translate(255, 0)">
            <rect x="0" y="0" width="225" height="230" rx="6" class="node-box"/>
            <text x="14" y="22" class="text-mono" font-size="10.5">2. JSON SCHEMA EXPORT</text>
            <rect x="12" y="32" width="200" height="110" rx="4" fill="#0b1018" stroke="#253245"/>
            <text x="18" y="48" class="text-mono" font-size="8.5" fill="#cbd5e1">{{"name": "get_orders",</text>
            <text x="18" y="64" class="text-mono" font-size="8.5" fill="#cbd5e1"> "parameters": {{</text>
            <text x="24" y="80" class="text-mono" font-size="8.5" fill="#6ee7b7">  "cust_id": {{"type": "str"}},</text>
            <text x="24" y="96" class="text-mono" font-size="8.5" fill="#6ee7b7">  "limit": {{"type": "int"}}</text>
            <text x="18" y="112" class="text-mono" font-size="8.5" fill="#cbd5e1"> }}, "required": ["cust_id"]}}</text>
            
            <text x="14" y="165" class="text-p">&bull; Sent to model API request</text>
            <text x="14" y="185" class="text-p">&bull; Constrains grammar tokens</text>
            <text x="14" y="210" class="text-mono-blue" font-size="10">API Wire Schema</text>
          </g>

          <path d="M 480 115 L 505 115" stroke="#60a5fa" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

          <!-- Stage 3: Model Output -->
          <g transform="translate(510, 0)">
            <rect x="0" y="0" width="225" height="230" rx="6" class="node-box-active-purple"/>
            <text x="14" y="22" class="text-mono-purple" font-size="10.5">3. MODEL GENERATION</text>
            <rect x="12" y="32" width="200" height="90" rx="4" fill="#0b1018" stroke="#253245"/>
            <text x="18" y="48" class="text-mono" font-size="8.5" fill="#b4a4e5">tool_calls: [{{</text>
            <text x="24" y="64" class="text-mono" font-size="8.5" fill="#b4a4e5">"id": "call_991",</text>
            <text x="24" y="80" class="text-mono" font-size="8.5" fill="#b4a4e5">"name": "get_orders",</text>
            <text x="24" y="96" class="text-mono" font-size="8.5" fill="#b4a4e5">"args": '{{"cust_id": "C4"}}'</text>
            <text x="18" y="112" class="text-mono" font-size="8.5" fill="#b4a4e5">}}]</text>

            <text x="14" y="145" class="text-p">&bull; Raw stringified JSON</text>
            <text x="14" y="165" class="text-p">&bull; Stop sequence triggered</text>
            <text x="14" y="185" class="text-p">&bull; Stochastic generation</text>
            <text x="14" y="210" class="text-mono-purple" font-size="10">Unvalidated JSON</text>
          </g>

          <path d="M 735 115 L 760 115" stroke="#b4a4e5" stroke-width="2" fill="none" marker-end="url(#arr-purple)"/>

          <!-- Stage 4: Runtime Validation -->
          <g transform="translate(765, 0)">
            <rect x="0" y="0" width="225" height="230" rx="6" class="node-box-active-amber"/>
            <text x="14" y="22" class="text-mono-amber" font-size="10.5">4. RUNTIME VALIDATION</text>
            <rect x="12" y="32" width="200" height="90" rx="4" fill="#141c28" stroke="#e0c58e"/>
            <text x="18" y="52" class="text-mono-amber" font-size="9">Pydantic Parser</text>
            <text x="18" y="70" class="text-p">&bull; Coerce types</text>
            <text x="18" y="88" class="text-p">&bull; Validate constraints</text>
            <text x="18" y="106" class="text-p">&bull; Check required fields</text>

            <text x="14" y="145" class="text-p">&bull; Intercepts malformed JSON</text>
            <text x="14" y="165" class="text-p">&bull; Emits validation errors</text>
            <text x="14" y="185" class="text-p">&bull; Prevents code injection</text>
            <text x="14" y="210" class="text-mono-amber" font-size="10">Security Boundary</text>
          </g>

          <path d="M 990 115 L 1015 115" stroke="#e0c58e" stroke-width="2" fill="none" marker-end="url(#arr-amber)"/>

          <!-- Stage 5: Execution & State Injection -->
          <g transform="translate(1020, 0)">
            <rect x="0" y="0" width="200" height="230" rx="6" class="node-box-active-green"/>
            <text x="14" y="22" class="text-mono-green" font-size="10.5">5. EXECUTION &amp; STATE</text>
            <rect x="12" y="32" width="176" height="90" rx="4" fill="#152420" stroke="#6ee7b7"/>
            <text x="18" y="52" class="text-mono-green" font-size="9">Tool Node Execution</text>
            <text x="18" y="72" class="text-p">&bull; Run Python func</text>
            <text x="18" y="90" class="text-p">&bull; Sandbox timeout</text>
            <text x="18" y="108" class="text-dim">&lt; 2000ms SLA</text>

            <text x="14" y="145" class="text-p">&bull; Appends ToolMessage</text>
            <text x="14" y="165" class="text-p">&bull; Matches call_id</text>
            <text x="14" y="185" class="text-p">&bull; Updates State channel</text>
            <text x="14" y="210" class="text-mono-green" font-size="10">State Appended</text>
          </g>
        </g>

        <!-- Bottom Warning Bar -->
        <g transform="translate(20, 310)">
          <rect x="0" y="0" width="1220" height="65" rx="6" fill="#111722" stroke="#253245"/>
          <text x="16" y="24" class="text-mono-coral" font-size="11">ENGINEERING CONTRACT INVARIANT:</text>
          <text x="16" y="46" class="text-p">If validation fails at Stage 4, the runtime must not crash. It formats a ToolMessage(content="ValidationError: ...")</text>
          <text x="730" y="46" class="text-dim">and feeds it back to the Model Node to trigger parameter self-correction.</text>
        </g>
      </g>
    """)
}
