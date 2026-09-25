# Slide 02: Clear Lesson Goals
from ..common_svg import svg_frame
from ..icons import render_icon

SLIDE_DATA = {
    "index": 2,
    "kicker": "CURRICULUM OBJECTIVES",
    "title": "Three Student Deliverables",
    "lead": "What every engineering student must be able to design and defend by the end of this module.",
    "section": "Curriculum Objectives",
    "takeaway": "A defensible decision requires trade-offs, explicit boundaries, and a rejected alternative.",
    "svg": svg_frame(f"""
      <g transform="translate(40, 35)">
        <!-- Column 1 -->
        <rect x="0" y="0" width="330" height="385" rx="8" class="node-box"/>
        <rect x="0" y="0" width="330" height="48" rx="8" fill="#1b2434"/>
        {render_icon("brain_model", 18, 12, size=24, color="#60a5fa")}
        <text x="52" y="30" class="text-h1" fill="#60a5fa">Deliverable 1: Building Blocks</text>
        
        <rect x="20" y="65" width="290" height="60" rx="6" fill="#141c28" stroke="#253245"/>
        <text x="32" y="88" class="text-h2">Identify Managed AI SaaS</text>
        <text x="32" y="110" class="text-p">Models, RAG, Agents, Evals, Traces, Governance</text>

        <text x="20" y="152" class="text-h2" fill="#cbd5e1">Mastery Verification Criteria:</text>
        
        <g transform="translate(20, 168)">
          <circle cx="8" cy="12" r="4" fill="#60a5fa"/>
          <text x="24" y="16" class="text-p">Deconstruct vendor catalogs into 6 capabilities</text>
          
          <circle cx="8" cy="42" r="4" fill="#60a5fa"/>
          <text x="24" y="46" class="text-p">Distinguish managed RAG from custom search</text>
          
          <circle cx="8" cy="72" r="4" fill="#60a5fa"/>
          <text x="24" y="76" class="text-p">Spot managed agent limits vs custom loops</text>

          <circle cx="8" cy="102" r="4" fill="#60a5fa"/>
          <text x="24" y="106" class="text-p">Identify the full 7-item production cost shape</text>
        </g>

        <rect x="20" y="325" width="290" height="40" rx="4" fill="#151f2e" stroke="#3b82f6" stroke-width="1.2"/>
        <text x="165" y="350" text-anchor="middle" class="text-mono">Outcome: Capability Fluency</text>
      </g>

      <g transform="translate(395, 35)">
        <!-- Column 2 -->
        <rect x="0" y="0" width="330" height="385" rx="8" class="node-box"/>
        <rect x="0" y="0" width="330" height="48" rx="8" fill="#1b2434"/>
        {render_icon("pipeline", 18, 12, size=24, color="#6ee7b7")}
        <text x="52" y="30" class="text-h1" fill="#6ee7b7">Deliverable 2: Cross-Cloud Map</text>
        
        <rect x="20" y="65" width="290" height="60" rx="6" fill="#141c28" stroke="#253245"/>
        <text x="32" y="88" class="text-h2">1 Workload, 3 Realizations</text>
        <text x="32" y="110" class="text-p">AWS Bedrock, Azure Foundry, Google Cloud</text>

        <text x="20" y="152" class="text-h2" fill="#cbd5e1">Mastery Verification Criteria:</text>
        
        <g transform="translate(20, 168)">
          <circle cx="8" cy="12" r="4" fill="#6ee7b7"/>
          <text x="24" y="16" class="text-p">Keep the identical business contract intact</text>
          
          <circle cx="8" cy="42" r="4" fill="#6ee7b7"/>
          <text x="24" y="46" class="text-p">Map offline data ingestion across 3 clouds</text>
          
          <circle cx="8" cy="72" r="4" fill="#6ee7b7"/>
          <text x="24" y="76" class="text-p">Map online query and human approval gates</text>

          <circle cx="8" cy="102" r="4" fill="#6ee7b7"/>
          <text x="24" y="106" class="text-p">Enforce enterprise IAM &amp; document ACLs</text>
        </g>

        <rect x="20" y="325" width="290" height="40" rx="4" fill="#152424" stroke="#6ee7b7" stroke-width="1.2"/>
        <text x="165" y="350" text-anchor="middle" class="text-mono-green">Outcome: Multi-Cloud Portability</text>
      </g>

      <g transform="translate(750, 35)">
        <!-- Column 3 -->
        <rect x="0" y="0" width="330" height="385" rx="8" class="node-box-active" stroke="#e0c58e"/>
        <rect x="0" y="0" width="330" height="48" rx="8" fill="#2d2516"/>
        {render_icon("shield", 18, 12, size=24, color="#e0c58e")}
        <text x="52" y="30" class="text-h1" fill="#e0c58e">Deliverable 3: Defend Choice</text>
        
        <rect x="20" y="65" width="290" height="60" rx="6" fill="#141c28" stroke="#253245"/>
        <text x="32" y="88" class="text-h2">Architectural Defense</text>
        <text x="32" y="110" class="text-p">5-Question Framework &amp; Trade-off Audit</text>

        <text x="20" y="152" class="text-h2" fill="#cbd5e1">Mastery Verification Criteria:</text>
        
        <g transform="translate(20, 168)">
          <circle cx="8" cy="12" r="4" fill="#e0c58e"/>
          <text x="24" y="16" class="text-p">Evaluate data boundary and compliance rules</text>
          
          <circle cx="8" cy="42" r="4" fill="#e0c58e"/>
          <text x="24" y="46" class="text-p">Calculate cost drivers beyond raw token price</text>
          
          <circle cx="8" cy="72" r="4" fill="#e0c58e"/>
          <text x="24" y="76" class="text-p">State exactly which platform was rejected</text>

          <circle cx="8" cy="102" r="4" fill="#e0c58e"/>
          <text x="24" y="106" class="text-p">Defend against team operational constraints</text>
        </g>

        <rect x="20" y="325" width="290" height="40" rx="4" fill="#242018" stroke="#e0c58e" stroke-width="1.2"/>
        <text x="165" y="350" text-anchor="middle" class="text-mono-amber">Outcome: Executive Justification</text>
      </g>
    """),
    "notes": {
        "goal": "Walk through the three concrete student deliverables: identify building blocks, map one workload to three clouds, and defend a platform choice.",
        "talkTrack": "Walk through the three goals: identify building blocks, map one workload to three clouds, and defend a platform choice. Point to the decision board: data boundary, model fit, security, operations, and cost shape. By the end of this session, you should be able to look at any vendor catalog, strip away the marketing, and map the workload to the services that actually matter.",
        "timing": "05:00 - 10:00 (5 min)"
    }
}
