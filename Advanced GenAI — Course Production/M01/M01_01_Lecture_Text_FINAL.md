Advanced GenAI — Module 01
Lecture Text FINAL · Cloud AI Capabilities Overview


## Purpose of the lesson
This lesson gives students a practical method for choosing managed cloud AI services for a production GenAI workload. The lecture deliberately avoids a catalog tour. The central skill is to start with a workload, identify the required platform capabilities, compare AWS, Microsoft Azure, and Google Cloud against those capabilities, and produce a defensible architecture decision.
Students understand why cloud AI platforms matter: they package models, retrieval, agents, evaluation, observability, governance, and cost controls.
Students can map the same support-assistant architecture to three cloud platforms without changing the business contract.
Students can explain when managed cloud, local/self-hosted, or hybrid deployment is the better starting point.

## Running case
The lecture uses one recurring case: an internal support assistant that answers questions from approved policy documents. The user asks: “How long can I borrow a laptop, and where do I collect it?” A correct system must answer with evidence, cite the source, respect the user’s document permissions, and create a support ticket only after explicit user confirmation.
This case is small enough to understand in class, but it forces the important enterprise questions: where does evidence come from, who may see it, where is the approval boundary, how is quality tested, how can failures be traced, and what cost categories appear in the bill.

## Conceptual model
A prototype can look like prompt → model → text. A production system needs more. It needs document preparation, identity, data access control, retrieval or enterprise search, model inference, tool/action boundaries, evaluation datasets, traces, monitoring, and cost control. A cloud AI platform helps by providing managed versions of many of these layers, but it does not decide the business policy. The application still owns the user journey, approval rules, quality threshold, and fallback behavior.

## Cloud, local, or hybrid

| Option | Use when | Trade-off |
| :--- | :--- | :--- |
| Managed cloud AI SaaS | The team needs speed, enterprise controls, integrated identity, monitoring, evaluation, and procurement path. | Less low-level control; exact cost depends on usage pattern, model choice, region, and platform services. |
| Local / self-hosted | The workload requires maximum control, strict data isolation, predictable model choice, or high steady volume with an operations team. | More infrastructure work: GPU capacity, serving, scaling, security hardening, monitoring, and incident response. |
| Hybrid | The organization wants managed control plane or cloud services while keeping sensitive data or some model execution inside a stricter boundary. | More architecture complexity and more integration/testing work. |



## Platform comparison
The lecture compares the platforms through six recurring capability groups: models, knowledge/RAG, agents, evaluation, observability, and governance. Model catalog size is useful but not decisive. Microsoft Foundry promotes the broadest catalog signal; Google emphasizes Gemini, third-party and open models together with data platform integration; AWS Bedrock emphasizes a curated provider catalog and tight AWS operations integration. The right answer depends on workload and organizational context.

| Dimension | AWS | Microsoft Azure / Foundry | Google Cloud |
| :--- | :--- | :--- | :--- |
| Model access | Amazon Bedrock model/provider catalog | Foundry model catalog and deployments | Gemini, third-party, and open models via Model Garden |
| Grounded answers | Knowledge Bases for Bedrock | AI Search and knowledge/tooling options | Search and grounding patterns in the Agent Platform / Google Cloud stack |
| Agents | Bedrock Agents / AgentCore where useful | Foundry Agent Service, prompt agents, hosted agents | Gemini Enterprise Agent Platform and ADK |
| Evaluation | Bedrock model and RAG evaluations | Foundry evaluations, traces, and monitoring dashboards | Model Evaluation service and cloud observability tools |
| Governance | IAM, VPC, KMS, Guardrails, CloudWatch/X-Ray | Entra ID, RBAC, Azure Policy, network isolation, Application Insights | IAM, VPC controls, project governance, Cloud Monitoring |
| Strong default when | The company is AWS-first and needs Bedrock close to existing AWS workloads. | The company is Microsoft/Azure-first and uses Entra, M365, Azure data, and Azure governance. | The workload is close to Google data, analytics, search, or BigQuery-centered workflows. |



## Cost model
Students should not compare clouds by a single model price. They should estimate the whole usage shape: input tokens, output tokens, retrieval depth, embeddings or search usage, agent runtime and sessions, document storage, evaluation runs, trace/log retention, and batch versus real-time needs. Exact prices should be checked immediately before delivery with the current vendor pricing pages or calculators.

## Demo and practice
The instructor demonstrates one neutral support-assistant architecture and translates it to AWS, Azure, and Google Cloud. Students then design a claims-processing assistant that accepts a PDF or image receipt, extracts fields, validates amounts, explains anomalies, and routes uncertain cases to human review. Their output is an architecture diagram, a platform choice, managed versus application-owned components, a security boundary, an evaluation plan, an observability plan, and one rejected alternative.

## Slide-by-slide map
1. Cloud AI Capabilities Overview. Open the lecture by stating the problem plainly: this lesson is about making cloud AI architecture choices, not memorizing vendor catalogs.
2. Clear lesson goals. Students should identify cloud AI SaaS building blocks, map one workload to AWS/Azure/Google, and defend a platform choice.
3. Why cloud AI platforms matter. A model endpoint is enough for a prototype. Production also needs identity, data access, retrieval, tool boundaries, evaluation, observability, and cost control.
4. What good vendor training usually does. Use the proven flow: concept, capability map, guided build, decision. Avoid a loose catalog tour.
5. Cloud AI SaaS landscape. Introduce the comparison frame: models, knowledge, agents, evaluation, observability, governance.
6. Running case: internal support assistant. Use one realistic support assistant scenario to keep every platform comparison grounded.
7. End-to-end architecture: two lanes. Separate document preparation from online request handling.
8. Cloud, local, or hybrid?. Explain why cloud is one design option, and when local or hybrid may be more appropriate.
9. Model catalog comparison. Model counts are not directly comparable, but they show platform strategy and selection risk.
10. Platform capability heatmap. Use qualitative comparison for this workload; do not present it as a benchmark.
11. AWS service map for the case. Map the neutral assistant to Bedrock-centered AWS services.
12. AWS: when it is a strong choice. AWS is strongest when the organization already runs data, IAM, monitoring, and apps on AWS.
13. Microsoft Azure / Foundry service map. Map the assistant to Foundry, AI Search, agents, evaluation, and Azure controls.
14. Azure: when it is a strong choice. Azure is strongest for Microsoft-stack organizations with Entra, Azure governance, and approved Azure operations.
15. Google Cloud service map. Map the assistant to Gemini Enterprise Agent Platform, Model Garden, grounding/search, and Cloud Observability.
16. Google Cloud: when it is a strong choice. Google is strongest when the workload is close to analytics, data engineering, BigQuery, and Google Cloud operations.
17. SaaS capability map. Show what each platform gives across models, knowledge, agents, evaluation, and observability.
18. RAG and enterprise knowledge. Compare managed RAG with a custom RAG pipeline.
19. Agent runtime choices. Show when fixed workflow is enough and when agent runtime becomes useful.
20. Evaluation and observability loop. Connect datasets, evaluations, release gates, traces, and failure analysis.
21. Cost model. Cost includes model usage, retrieval, agent runtime, storage, evaluation, and monitoring.
22. Where cheaper comes from. Cheaper is a design outcome: token reduction, retrieval quality, tiers, caching, and sometimes local/hybrid operation.
23. Decision framework. Use five questions: workload, data boundary, model class, observability, operator.
24. Demo sequence. Demo one design translated to three clouds, not three unrelated apps.
25. Workshop. Students design and defend a claims-processing assistant.
26. Worked solution. Show a good-enough architecture decision package.
27. Final takeaway. Managed platforms remove infrastructure work; they do not remove architecture decisions.