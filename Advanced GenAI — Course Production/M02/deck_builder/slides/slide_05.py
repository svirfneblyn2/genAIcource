# Slide 05: State Schema Architecture: TypedDict vs. Pydantic
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 5,
    "kicker": "STATE MANAGEMENT",
    "title": "State Schemas, Reducers, and Channel Isolation",
    "lead": "Defining explicit state schemas with append-only message reducers to eliminate race conditions and state corruption.",
    "section": "State & Persistence",
    "takeaway": "Use TypedDict with append reducers for high-throughput message streaming; use Pydantic for strict domain validation.",
    "notes": {
        "goal": "Explain how orchestrators manage state via channels, reducers, and schemas, contrasting TypedDict with Pydantic.",
        "talkTrack": "In Python, state can easily become a tangled global dictionary. Graph runtimes enforce structure using channels. Each channel has an update reducer. By default, returning a dictionary key overwrites the existing value. But for conversational histories, overwriting destroys context. We use Annotated with the add_messages reducer. This appends new messages while updating existing messages by unique ID.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Left: TypedDict with Reducers -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="600" height="395" rx="8" class="node-box-active"/>
          <rect x="0" y="0" width="600" height="44" rx="8" fill="#1e2c42"/>
          {render_icon("state_machine", 14, 10, size=24, color="#60a5fa")}
          <text x="46" y="28" class="text-h1" fill="#60a5fa">TypedDict Schema with Custom Reducers</text>

          <g transform="translate(20, 58)">
            <!-- Code Block Visual -->
            <rect x="0" y="0" width="560" height="175" rx="6" fill="#0b1018" stroke="#253245"/>
            <text x="16" y="24" class="text-mono" font-size="11.5" fill="#e2e8f0">from typing import TypedDict, Annotated</text>
            <text x="16" y="44" class="text-mono" font-size="11.5" fill="#e2e8f0">from langgraph.graph.message import add_messages</text>
            <text x="16" y="64" class="text-mono" font-size="11.5" fill="#60a5fa">import operator</text>
            <text x="16" y="94" class="text-mono" font-size="11.5" fill="#e0c58e">class AgentState(TypedDict):</text>
            <text x="36" y="114" class="text-mono" font-size="11.5" fill="#6ee7b7">messages: Annotated[list[BaseMessage], add_messages]</text>
            <text x="36" y="134" class="text-mono" font-size="11.5" fill="#cbd5e1">context: dict[str, Any]       # Default: overwrites on update</text>
            <text x="36" y="154" class="text-mono" font-size="11.5" fill="#b4a4e5">audit_log: Annotated[list[str], operator.add] # Appends list</text>

            <!-- Reducer Deep Dive -->
            <g transform="translate(0, 190)">
              <rect x="0" y="0" width="560" height="130" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="16" y="24" class="text-mono-green" font-size="11">REDUCER BEHAVIOR: add_messages</text>
              <text x="16" y="46" class="text-p">&bull; Appends new HumanMessage, AIMessage, or ToolMessage to state array.</text>
              <text x="16" y="66" class="text-p">&bull; ID Deduplication: If an incoming message matches an existing message.id,</text>
              <text x="16" y="84" class="text-p">  it updates the message in-place rather than duplicating it (crucial for streaming).</text>
              <text x="16" y="106" class="text-dim">&bull; Zero runtime overhead: Native Python typing without Pydantic parsing costs.</text>
            </g>
          </g>
        </g>

        <!-- Right: Pydantic Domain Validation -->
        <g transform="translate(630, 0)">
          <rect x="0" y="0" width="630" height="395" rx="8" class="node-box"/>
          <rect x="0" y="0" width="630" height="44" rx="8" fill="#1b2434"/>
          {render_icon("shield", 14, 10, size=24, color="#e0c58e")}
          <text x="46" y="28" class="text-h1" fill="#e0c58e">Pydantic Domain Validation &amp; Invariants</text>

          <g transform="translate(20, 58)">
            <!-- Code Block Visual -->
            <rect x="0" y="0" width="590" height="175" rx="6" fill="#0b1018" stroke="#253245"/>
            <text x="16" y="24" class="text-mono" font-size="11.5" fill="#e2e8f0">from pydantic import BaseModel, Field, field_validator</text>
            <text x="16" y="54" class="text-mono" font-size="11.5" fill="#e0c58e">class ReconciliationState(BaseModel):</text>
            <text x="36" y="74" class="text-mono" font-size="11.5" fill="#6ee7b7">invoice_id: str = Field(..., pattern=r'^INV-[0-9]{{6}}$')</text>
            <text x="36" y="94" class="text-mono" font-size="11.5" fill="#6ee7b7">billed_amount: float = Field(..., gt=0.0)</text>
            <text x="36" y="114" class="text-mono" font-size="11.5" fill="#6ee7b7">approved_by: str | None = None</text>
            <text x="36" y="144" class="text-mono" font-size="11.5" fill="#b4a4e5">@field_validator('billed_amount')</text>
            <text x="36" y="164" class="text-mono" font-size="11.5" fill="#e2e8f0">def check_currency(cls, v): return round(v, 2)</text>

            <!-- Pydantic Deep Dive -->
            <g transform="translate(0, 190)">
              <rect x="0" y="0" width="590" height="130" rx="6" fill="#141c28" stroke="#253245"/>
              <text x="16" y="24" class="text-mono-amber" font-size="11">WHEN TO CHOOSE PYDANTIC OVER TYPEDDICT</text>
              <text x="16" y="46" class="text-p">&bull; Domain Invariants: Enforces strict business rules before nodes execute.</text>
              <text x="16" y="66" class="text-p">&bull; Serialization: Built-in .model_dump_json() for clean DB storage.</text>
              <text x="16" y="84" class="text-p">&bull; Type Coercion: Automatically casts string numbers ('150.00') to float.</text>
              <text x="16" y="106" class="text-dim">&bull; Trade-off: Small CPU overhead (~5-10ms per step) during high-rate validation.</text>
            </g>
          </g>
        </g>
      </g>
    """)
}
