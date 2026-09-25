# Slide 14: Pattern 3: Swarm & Peer Handoffs
from ..common_svg import svg_frame, render_zone_badge
from ..icons import render_icon

SLIDE_DATA = {
    "index": 14,
    "kicker": "TOPOLOGY PATTERNS",
    "title": "Pattern 3: Swarm & Peer-to-Peer Handoff Architecture",
    "lead": "Decentralized agents directly transfer execution control and context to peers via handoff functions.",
    "section": "Multi-Agent Topologies",
    "takeaway": "Swarm patterns minimize orchestration latency for collaborative workflows without a bottleneck supervisor.",
    "notes": {
        "goal": "Explain the mechanics of peer-to-peer agent handoffs, popularized by OpenAI Swarm, and their enterprise trade-offs.",
        "talkTrack": "In contrast to the rigid hierarchy of a supervisor, the Swarm pattern is decentralized. Agents talk to each other as peers. When a customer support triage agent realizes the user wants to book a flight, it does not report back to a supervisor. It invokes a handoff function: transfer_to_flight_agent(). The runtime immediately transitions control, tools, and message history to the flight agent. It is exceptionally low latency, but requires strict loop guards.",
        "timing": "4 minutes"
    },
    "svg": svg_frame(f"""
      <g transform="translate(40, 25)">
        <!-- Master Container -->
        <rect x="0" y="0" width="1260" height="400" rx="8" class="node-box"/>
        <rect x="0" y="0" width="1260" height="44" rx="8" fill="#1b2434"/>
        {render_icon("swarm", 15, 10, size=24, color="#6ee7b7")}
        <text x="48" y="28" class="text-h1" fill="#6ee7b7">Peer Swarm: Direct Execution Handoff Mechanics</text>

        <!-- 3 Peer Agents in Sequence -->
        <g transform="translate(25, 65)">
          <!-- Agent 1: Triage -->
          <g transform="translate(0, 30)">
            <rect x="0" y="0" width="340" height="195" rx="6" class="node-box-active"/>
            <rect x="0" y="0" width="340" height="32" rx="6" fill="#1e2c42"/>
            <text x="170" y="22" text-anchor="middle" class="text-mono" font-size="11">AGENT 1: TRIAGE &amp; INTENT</text>

            <g transform="translate(16, 46)">
              <text x="0" y="16" class="text-h2">Active Context: User Greeting</text>
              <text x="0" y="36" class="text-p">"I need to reschedule flight FL-891"</text>
              
              <!-- Handoff Tool Call -->
              <rect x="0" y="55" width="308" height="52" rx="4" fill="#0b1018" stroke="#6ee7b7"/>
              <text x="12" y="74" class="text-mono-green" font-size="9.5">TOOL: transfer_to_flight_agent(</text>
              <text x="20" y="92" class="text-mono" font-size="9" fill="#cbd5e1">flight_id="FL-891", user_id="U41")</text>

              <text x="0" y="128" class="text-dim" font-size="9.5">Hands over active execution token</text>
            </g>
          </g>

          <!-- Handoff 1-to-2 Arrow -->
          <path d="M 340 125 L 430 125" stroke="#6ee7b7" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>
          <rect x="350" y="102" width="70" height="20" rx="3" fill="#152420" stroke="#6ee7b7" stroke-width="1"/>
          <text x="385" y="116" text-anchor="middle" class="text-mono-green" font-size="8.5">HANDOFF</text>

          <!-- Agent 2: Flight Operations -->
          <g transform="translate(440, 30)">
            <rect x="0" y="0" width="340" height="195" rx="6" class="node-box-active-green"/>
            <rect x="0" y="0" width="340" height="32" rx="6" fill="#152420"/>
            <text x="170" y="22" text-anchor="middle" class="text-mono-green" font-size="11">AGENT 2: FLIGHT BOOKING</text>

            <g transform="translate(16, 46)">
              <text x="0" y="16" class="text-h2">Inherited Scope: Reschedule API</text>
              <text x="0" y="36" class="text-p">Validates seat inventory for flight FL-891</text>
              
              <!-- Handoff Tool Call -->
              <rect x="0" y="55" width="308" height="52" rx="4" fill="#0b1018" stroke="#e0c58e"/>
              <text x="12" y="74" class="text-mono-amber" font-size="9.5">TOOL: transfer_to_payment_agent(</text>
              <text x="20" y="92" class="text-mono" font-size="9" fill="#cbd5e1">fee_amount=75.00, currency="USD")</text>

              <text x="0" y="128" class="text-dim" font-size="9.5">Re-routes control directly to checkout</text>
            </g>
          </g>

          <!-- Handoff 2-to-3 Arrow -->
          <path d="M 780 125 L 870 125" stroke="#e0c58e" stroke-width="2.5" fill="none" marker-end="url(#arr-amber)"/>
          <rect x="790" y="102" width="70" height="20" rx="3" fill="#2d2516" stroke="#e0c58e" stroke-width="1"/>
          <text x="825" y="116" text-anchor="middle" class="text-mono-amber" font-size="8.5">HANDOFF</text>

          <!-- Agent 3: Payment -->
          <g transform="translate(880, 30)">
            <rect x="0" y="0" width="330" height="195" rx="6" class="node-box-active-amber"/>
            <rect x="0" y="0" width="330" height="32" rx="6" fill="#2d2516"/>
            <text x="165" y="22" text-anchor="middle" class="text-mono-amber" font-size="11">AGENT 3: PAYMENT GATEWAY</text>

            <g transform="translate(16, 46)">
              <text x="0" y="16" class="text-h2">Inherited Scope: Stripe Charge</text>
              <text x="0" y="36" class="text-p">Processes $75.00 change fee</text>
              
              <rect x="0" y="55" width="298" height="52" rx="4" fill="#141c28" stroke="#6ee7b7"/>
              <text x="12" y="74" class="text-mono-green" font-size="9.5">STATUS: Charge Complete ($75)</text>
              <text x="12" y="92" class="text-p">Emits confirmation code to user</text>

              <text x="0" y="128" class="text-mono-green" font-size="9.5">TERMINAL NODE REACHED</text>
            </g>
          </g>
        </g>

        <!-- Bottom Warning & Tradeoff -->
        <g transform="translate(25, 290)">
          <rect x="0" y="0" width="1210" height="85" rx="6" fill="#111722" stroke="#253245"/>
          {render_zone_badge("SWARM ENGINEERING TRADE-OFFS", 15, 12, 230, 24, "#e0c58e")}

          <g transform="translate(15, 45)">
            <text x="0" y="16" class="text-mono-green" font-size="10.5">LATENCY ADVANTAGE:</text>
            <text x="0" y="32" class="text-p">Zero intermediate supervisor hops. Execution transitions immediately in 1 step.</text>
          </g>

          <g transform="translate(560, 45)">
            <text x="0" y="16" class="text-mono-coral" font-size="10.5">ENTERPRISE RISK (PING-PONG LOOPS):</text>
            <text x="0" y="32" class="text-p">Agent A can hand off to Agent B, which hands back to Agent A. Runtime MUST enforce max_handoffs = 5.</text>
          </g>
        </g>
      </g>
    """)
}
