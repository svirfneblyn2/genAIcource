Advanced GenAI — Module 01
Full Instructor Script FINAL · Cloud AI Capabilities Overview


## Instructor operating principle
Keep one question visible throughout the lesson: “Given this workload, which platform capabilities should we use, and what remains our application responsibility?” Do not present service lists unless each service answers that question.

## Timing plan

| Block | Time | Purpose |
| :--- | :--- | :--- |
| Opening + goals | 10 min | Clarify why the lecture exists and what students will produce. |
| Architecture and case | 25 min | Build the neutral mental model and the support-assistant case. |
| Cloud platform comparison | 35 min | Compare AWS, Azure, Google through models, RAG, agents, eval, observability, governance. |
| Cost and decision framework | 20 min | Teach cost categories and the five-question platform selection method. |
| Demo + workshop | 25 min | Translate one design three ways, then have students apply the method. |
| Close | 5 min | Lock the final takeaway and homework expectations. |



## Slide script

### Slide 1: Cloud AI Capabilities Overview
Say: “Today we are not comparing cloud vendors as brands. We are comparing how cloud AI platforms help us build one real application: a grounded support assistant with evidence, permissions, evaluation, monitoring, and cost visibility.”
Explain that the goal is a decision students can defend, not a list of logos they can repeat.
Teaching note: Open the lecture by stating the problem plainly: this lesson is about making cloud AI architecture choices, not memorizing vendor catalogs.

### Slide 2: Clear lesson goals
Walk through the three goals: identify building blocks, map one workload to three clouds, and defend a platform choice. Point to the decision board: data boundary, model fit, security, operations, and cost shape.
Teaching note: Students should identify cloud AI SaaS building blocks, map one workload to AWS/Azure/Google, and defend a platform choice.

### Slide 3: Why cloud AI platforms matter
Contrast a prototype with a production system. Say that prompt → model → text is useful, but not enough for an enterprise workload. Production systems require the boring parts that prevent expensive incidents: identity, data access, retrieval quality, action approvals, evaluation, monitoring, and cost control.
Teaching note: A model endpoint is enough for a prototype. Production also needs identity, data access, retrieval, tool boundaries, evaluation, observability, and cost control.

### Slide 4: What good vendor training usually does
Explain the training pattern used in strong cloud learning material: first concept, then capability map, then guided build, then decision. Say that this is the structure of the lecture.
Teaching note: Use the proven flow: concept, capability map, guided build, decision. Avoid a loose catalog tour.

### Slide 5: Cloud AI SaaS landscape
Introduce the six categories. Tell students these boxes are the comparison frame. Each vendor slide will answer: how does this platform provide models, knowledge, agents, evaluation, observability, and governance?
Teaching note: Introduce the comparison frame: models, knowledge, agents, evaluation, observability, governance.

### Slide 6: Running case: internal support assistant
Read the support question aloud. Then walk through the expected assistant behavior. Emphasize that the same simple case already contains the hard questions: citation, permissions, action approval, traceability, evaluation, and cost.
Teaching note: Use one realistic support assistant scenario to keep every platform comparison grounded.

### Slide 7: End-to-end architecture: two lanes
Separate the offline lane from the online lane. Offline: documents are prepared, permission labels are attached, and the index is built. Online: a user request goes through the app, retrieval, the model, answer generation, and maybe an approved action.
Teaching note: Separate document preparation from online request handling.

### Slide 8: Cloud, local, or hybrid?
Explain that cloud is not ideology. Managed cloud is attractive when speed, governance, identity, monitoring, evaluation, and procurement path matter. Local or self-hosted becomes attractive when data isolation or predictable high-volume economics dominate. Hybrid exists because enterprises usually want both control and acceleration.
Teaching note: Explain why cloud is one design option, and when local or hybrid may be more appropriate.

### Slide 9: Model catalog comparison
Use the model catalog slide carefully. Microsoft promotes a very broad catalog signal; Google promotes Gemini plus third-party and open models/tools; AWS Bedrock is a curated multi-provider platform. Say that catalog size is a starting question, not the answer.
Teaching note: Model counts are not directly comparable, but they show platform strategy and selection risk.

### Slide 10: Platform capability heatmap
Use the heatmap as a heuristic. Do not read it like a benchmark. It tells students what to investigate during selection: model breadth, RAG, agent runtime, evaluation, identity, data integration, ecosystem fit, and cost predictability.
Teaching note: Use qualitative comparison for this workload; do not present it as a benchmark.

### Slide 11: AWS service map for the case
Map the support assistant to AWS. Bedrock supplies model access; Knowledge Bases can support grounded retrieval; agents and AgentCore can help runtime and orchestration; IAM, KMS, VPC, CloudWatch, X-Ray, guardrails, and evaluation complete the operational story.
Teaching note: Map the neutral assistant to Bedrock-centered AWS services.

### Slide 12: AWS: when it is a strong choice
Translate AWS into selection logic. AWS is a strong choice when the organization is already AWS-heavy, when data and applications live there, and when the team wants GenAI close to existing IAM, networking, logging, and platform operations.
Teaching note: AWS is strongest when the organization already runs data, IAM, monitoring, and apps on AWS.

### Slide 13: Microsoft Azure / Foundry service map
Map the same design to Microsoft Azure / Foundry. Foundry gives model catalog and deployment, agent service, evaluations, tracing, and enterprise management. AI Search and Azure platform services support the grounded-answer path. Entra ID, RBAC, policy, private networking, and Application Insights matter for enterprise operation.
Teaching note: Map the assistant to Foundry, AI Search, agents, evaluation, and Azure controls.

### Slide 14: Azure: when it is a strong choice
Explain Azure selection logic. If the company already uses Microsoft identity, M365, Azure governance, and Azure data/services, Azure often becomes the lowest-friction path to a governed GenAI pilot and production rollout.
Teaching note: Azure is strongest for Microsoft-stack organizations with Entra, Azure governance, and approved Azure operations.

### Slide 15: Google Cloud service map
Map the same design to Google Cloud. Highlight Gemini, Model Garden, Agent Platform, grounding/search, evaluation, Cloud Observability, and data platform integration. Keep older naming out of the main story unless students ask about migration context.
Teaching note: Map the assistant to Gemini Enterprise Agent Platform, Model Garden, grounding/search, and Cloud Observability.

### Slide 16: Google Cloud: when it is a strong choice
Explain Google Cloud selection logic. It is especially strong when the assistant is tied to analytics, BigQuery, search/grounding, data engineering, or Google Cloud-native workflows.
Teaching note: Google is strongest when the workload is close to analytics, data engineering, BigQuery, and Google Cloud operations.

### Slide 17: SaaS capability map
Show the SaaS capability map. Tell students that similar categories exist across vendors, but implementation details differ. This is why architecture concepts must be stable while service labels can change.
Teaching note: Show what each platform gives across models, knowledge, agents, evaluation, and observability.

### Slide 18: RAG and enterprise knowledge
Compare managed RAG and custom RAG. Managed RAG is faster and easier to operate. Custom RAG gives more control over chunking, ranking, permissions, and optimization. The right choice depends on control requirements and team maturity.
Teaching note: Compare managed RAG with a custom RAG pipeline.

### Slide 19: Agent runtime choices
Explain that an agent is not always needed. A fixed workflow is often easier to test and operate. Use an agent runtime when the model needs to choose tools, maintain state, handle multi-step tasks, or integrate with managed observability and sessions.
Teaching note: Show when fixed workflow is enough and when agent runtime becomes useful.

### Slide 20: Evaluation and observability loop
Walk around the evaluation loop. A production AI system needs test datasets before release, evaluation runs, release gates, runtime traces, failure analysis, and fixes. If you cannot trace a bad answer, you cannot operate the system.
Teaching note: Connect datasets, evaluations, release gates, traces, and failure analysis.

### Slide 21: Cost model
Explain the cost model. Model tokens are only one bar. Retrieval, embeddings, agent runtime, sessions, evaluation, storage, logs, traces, and monitoring also matter. Exact prices must be checked live; the slide teaches what to estimate.
Teaching note: Cost includes model usage, retrieval, agent runtime, storage, evaluation, and monitoring.

### Slide 22: Where cheaper comes from
Answer the cheapness question. Cheaper usually comes from design: reduce tokens, improve retrieval, use batch or flexible tiers when latency allows, cache safely, and consider local or hybrid only when the organization can operate it responsibly.
Teaching note: Cheaper is a design outcome: token reduction, retrieval quality, tiers, caching, and sometimes local/hybrid operation.

### Slide 23: Decision framework
Present the five-question decision framework. Ask students to use it in the workshop: workload, data boundary, model class, observability, and operator. Require one rejected alternative so the decision is not cosmetic.
Teaching note: Use five questions: workload, data boundary, model class, observability, operator.

### Slide 24: Demo sequence
Explain the demo sequence before starting. The demo is requirements → neutral architecture → AWS mapping → Azure mapping → Google mapping → decision and cost check. Do not open three unrelated demos.
Teaching note: Demo one design translated to three clouds, not three unrelated apps.

### Slide 25: Workshop
Set up the workshop. Students design a claims-processing assistant with PDF/image input, extracted fields, anomaly explanation, and human review. They have 12 minutes to build and 3 minutes to defend.
Teaching note: Students design and defend a claims-processing assistant.

### Slide 26: Worked solution
Show the worked solution as the quality bar, not as the only correct answer. A good answer has a clear architecture, a cloud rationale, application-owned boundaries, evaluation, and one rejected alternative.
Teaching note: Show a good-enough architecture decision package.

### Slide 27: Final takeaway
Close with the final statement: managed platforms can remove infrastructure work, but they cannot remove architecture decisions. Read the five closing questions and connect them to the homework.
Teaching note: Managed platforms remove infrastructure work; they do not remove architecture decisions.