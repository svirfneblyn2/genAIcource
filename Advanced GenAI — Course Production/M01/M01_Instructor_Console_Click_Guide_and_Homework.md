# Module 01: Instructor Console Click-Guide & Zero-Cost Homework Specification

Course: Advanced Generative AI for Engineers
Module 01: Cloud AI Capabilities Overview (AWS Bedrock, Azure AI Foundry, Google Cloud)

---

## Part 1: Instructor Console Click-by-Click Guide (15-Minute Tour)

### Pedagogical Goal
Demonstrate to students that AWS Bedrock, Azure AI Foundry, and Google Cloud Vertex AI share the exact same architectural layers (Offline Ingestion, Vector Knowledge Store, Frontier Model, Agent Runtime, Guardrails, and Governance). You do NOT need to deploy models, spin up billable clusters, or run live code. You simply navigate the consoles to anchor the conceptual architecture in real portal screens.

### Preparation Before Lecture (Open 4 Browser Tabs)
1. Tab 1: Presentation deck (`presentation_M01_Cloud_AI_Overview.html`), opened to Slide 24.
2. Tab 2: AWS Console (`https://console.aws.amazon.com/bedrock/home?region=us-east-1`).
3. Tab 3: Azure AI Foundry Portal (`https://ai.azure.com/` or Azure Portal `portal.azure.com`).
4. Tab 4: Google Cloud Console (`https://console.cloud.google.com/vertex-ai`).

*Tip: Log into all 3 cloud accounts 15 minutes before the lecture so MFA and session timeouts do not interrupt you on screen.*

---

### Step 1: AWS Bedrock Walkthrough (4-5 minutes)

#### Where to click:
1. **Left Navigation -> Foundation Models -> Base Models**
   - Direct URL: `https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/models`
   - What to show: Filter by Provider (`Anthropic`, `Amazon`, `Meta`, `Mistral`, `Cohere`).
   - What to say:
     > "Notice how AWS treats foundation models: they are not arbitrary VMs. They are managed serverless endpoints under a unified Converse API contract. We can invoke Claude 3.5 Sonnet, Amazon Nova, or Llama 3.3 using the exact same request structure."

2. **Left Navigation -> Builder tools -> Knowledge bases**
   - Direct URL: `https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/knowledge-bases`
   - What to click: Click the orange button **"Create knowledge base"** (Step 1 of the wizard).
   - What to show:
     - Data source: Point to Amazon S3 (the Offline Ingestion Lane).
     - Chunking options: Point out Default chunking (300 tokens) vs Fixed vs Semantic chunking.
     - Vector store: Point out the options: Amazon OpenSearch Serverless (automated default), Amazon Aurora pgvector, Pinecone, or Redis Enterprise.
   - What to say:
     > "This wizard is our Slide 11 in action. Layer 3 (Knowledge Store) connects S3 files directly into a serverless vector database like OpenSearch Serverless or Aurora pgvector. AWS handles embedding generation and chunking under the hood."
   - Action: Click **"Cancel"** (do not actually create the knowledge base).

3. **Left Navigation -> Builder tools -> Agents**
   - Direct URL: `https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/agents`
   - What to show: Show the Agent configuration overview (Model selection, Instructions, Action Groups, Knowledge Bases).
   - What to say:
     > "Here is Layer 2 (AI Runtime). An Agent is a managed state machine. It pairs Claude 3.5 Sonnet with instructions, attaches our Knowledge Base for policy retrieval, and attaches Lambda functions as Action Groups to perform actions like creating a support ticket."

4. **Left Navigation -> Safeties -> Guardrails**
   - Direct URL: `https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/guardrails`
   - What to show: Point out Content filters, Denied topics, PII filters (masking Social Security numbers / emails), and Grounding check filters.
   - What to say:
     > "This is enterprise governance. Guardrails sit between the user and the model. They mask PII before it hits Claude and reject responses that hallucinate without citation evidence."

---

### Step 2: Microsoft Azure AI Foundry Walkthrough (4-5 minutes)

#### Where to click:
1. **Azure AI Foundry Portal (`https://ai.azure.com/`) -> Open or Create a Project**
   - Left Navigation: **Model catalog**
   - What to show: 10,000+ models. Point out OpenAI (GPT-4o, o1, o3-mini), Meta Llama, Mistral, and Hugging Face collection.
   - What to say:
     > "Compare this with AWS. Microsoft operates as a massive enterprise model marketplace. Through Azure, you get strategic first-party access to OpenAI models with zero data retention under your corporate HIPAA/BAA agreement."

2. **Left Navigation -> Data + indexes -> Indexes**
   - What to click: Click **"+ New index"**.
   - What to show: The integration with **Azure AI Search** and Azure Blob Storage / Microsoft 365 SharePoint connectors.
   - What to say:
     > "Here is Azure Layer 3. Azure AI Search provides the industry standard hybrid search: BM25 lexical keyword search plus vector embeddings, followed by a semantic cross-encoder reranker. It also inherits corporate ACL security tags from Microsoft Entra ID."
   - Action: Close the wizard.

3. **Left Navigation -> Build -> Agents**
   - What to show: Azure AI Foundry Agent Service. Show the Playground with Model selection (GPT-4o), System prompt, and Tools (`File Search`, `Code Interpreter`, `Custom Functions`).
   - What to say:
     > "Notice how similar this is to Bedrock Agents. We choose our model, attach Azure AI Search as the File Search tool, and connect Logic Apps or Azure Functions to trigger actions inside ServiceNow or Microsoft Teams."

4. **Left Navigation -> Safety + security -> Content Safety**
   - What to show: Prompt Shields (direct and indirect prompt injection detection), Protected material text filter, and PII detection.
   - What to say:
     > "This is the Azure defense layer. Prompt Shields stop malicious users from overriding system instructions via documents or user chats."

---

### Step 3: Google Cloud Vertex AI Walkthrough (4-5 minutes)

#### Where to click:
1. **Google Cloud Console -> Vertex AI (`https://console.cloud.google.com/vertex-ai`)**
   - Left Navigation: **Model Garden**
   - What to show: Search for `Gemini 2.0 Flash`, `Gemini 1.5 Pro`, `Claude 3.5 Sonnet`, `Gemma 2`.
   - What to say:
     > "Google Cloud combines first-party frontier Gemini models with open models like Gemma and third-party models like Claude. Gemini 1.5 Pro gives you a native 2-million token context window, allowing you to bypass RAG entirely for documents under 1,000 pages."

2. **Left Navigation -> Agent Builder -> Search and Conversation -> Data Stores**
   - Direct URL: `https://console.cloud.google.com/gen-app-builder/data-stores`
   - What to click: Click **"Create Data Store"**.
   - What to show: Options: Cloud Storage, BigQuery, Google Drive, Website URLs, Jira, Confluence.
   - What to say:
     > "This is Google Layer 3 (Vertex AI Search). Because of Google's search DNA, their turnkey ingestion handles table extraction and multi-page layouts automatically. You can ground models directly on BigQuery data lakes without building custom ETL pipelines."
   - Action: Click Cancel.

3. **Left Navigation -> Agent Builder -> Apps / Agents**
   - What to show: Vertex AI Agent Builder interface.
   - What to say:
     > "Here is the Gemini Enterprise Agent Platform. You create multi-turn conversational agents with built-in Session State management and multi-tool routing."

4. **Left Navigation -> Vertex AI -> Vertex AI Studio -> Freeform / Chat Prompt**
   - What to show: In the right sidebar, point out the toggle **"Grounding" -> "Vertex AI Search"**.
   - What to say:
     > "With one click, any Gemini prompt is grounded against our enterprise knowledge base. Google automatically computes a Grounding Score, showing exact confidence and citations."

---

### Step 4: Live Cost Comparison Wrap-up (2-3 minutes)

Open one pricing calculator or point back to Slide 21/22:
- **AWS Bedrock**: Pay-as-you-go tokens, but OpenSearch Serverless has a minimum cost of ~4 OCUs ($0.70/hour = ~$500/month) even at zero traffic.
- **Azure AI Foundry**: Pay-as-you-go tokens or PTU (Provisioned Throughput). Azure AI Search Basic tier starts at ~$75/month.
- **Google Cloud Vertex AI**: Gemini 1.5 Flash is extremely cost-effective ($0.075 / 1M tokens), and Vertex Search charges per search request ($0.005 / query) with zero fixed cluster minimums.

Takeaway statement:
> "Portals look different, but the architecture is identical. Your choice comes down to organizational data gravity, identity controls, and fixed infrastructure pricing floors."

---

## Part 2: Student Homework Specification (100% Free / Zero-Cost)

### Assignment Title
**Enterprise Architecture Decision Package: Medical Claims Processing Assistant**

### Deadline & Format
- **Format**: 1 Architecture Design Document (PDF or Markdown) + 1 Optional Sandbox Verification.
- **Cost**: **$0.00 (Zero financial cost guaranteed)**. Students do NOT need to provide credit cards or pay for cloud infrastructure.

---

### Business Scenario (From Slide 25)
You are the Lead AI Architect for *OmniHealth Insurance*. The company processes 50,000 medical reimbursement claims per month. Currently, human adjusters manually review scanned receipts and hospital invoices to check policy eligibility, extract diagnostic codes (ICD-10, CPT), and detect billing anomalies.

Your task is to design an automated, multimodal **Claims Processing Assistant** with the following pipeline:
1. **Input**: Scanned medical receipt or invoice (PDF or JPEG image).
2. **Field Extraction & OCR**: Extract patient name, service date, provider, billed amounts, and medical procedure codes.
3. **Policy Grounding (RAG)**: Validate whether the billed procedure is covered under the patient's insurance plan document.
4. **Anomaly Reasoning**: Flag billing discrepancies (e.g. duplicate billing, unbundled procedure codes, charges exceeding fee schedule).
5. **Human-in-the-Loop Review**: If extraction confidence is < 90% or an anomaly is detected, route the claim to a human nurse review queue.

---

### Zero-Cost Implementation Options for Students

Students choose ONE of the two options below:

#### Option A: Architecture Design Package (Recommended, $0, No Credit Card Required)
Students produce an enterprise-grade architecture specification document without touching cloud billing:
- **Architecture Diagram**: Drawn using free tools: Mermaid.js, Draw.io, Excalidraw, or Google Slides.
- **Platform Choice**: Clear selection between AWS Bedrock, Azure AI Foundry, or Google Cloud Vertex AI.
- **The 5-Question Framework**: Formally answered for OmniHealth Insurance.
- **Security Boundary**: How HIPAA BAA, CMEK encryption, and PII masking are handled.
- **Mandatory Rejected Alternative**: Clear explanation of why at least one competing cloud was disqualified.

#### Option B: Hands-On Prototype via Free Sandboxes ($0 Cost)
Students who want to write code and test live multimodal models can use 100% free developer sandboxes:
1. **Google AI Studio (`https://aistudio.google.com/`)**:
   - Free tier includes **15 requests per minute completely free** for Gemini 2.0 Flash and Gemini 1.5 Pro.
   - **Zero credit card required**.
   - Students can upload a sample invoice image, prompt Gemini to extract JSON fields and detect anomalies, and verify accuracy.
2. **Azure for Students (`https://azure.microsoft.com/free/students/`)**:
   - $100 free Azure credits for anyone with an active university/college email (`.edu`).
   - **Zero credit card required**.
3. **AWS Educate / AWS Free Tier**:
   - Free access to learning labs and free tier allowances.

---

### Required Student Deliverables (Checklist)

Every submission must contain the following 5 sections:

1. **System Architecture Diagram**:
   - Must show the 4 distinct layers: App/Input Layer, AI Ingestion & Inference Layer, Retrieval/Knowledge Layer, and Human Approval Queue.
   - Demarcate which components are Managed Cloud Services vs Application-Owned code.

2. **Platform Selection & Justification (The 5 Questions)**:
   - Question 1 (Workload): Multimodal receipt OCR + table parsing + policy search.
   - Question 2 (Data Boundary): Where health records reside and HIPAA compliance boundaries.
   - Question 3 (Model Strategy): Chosen foundation model (e.g. GPT-4o, Claude 3.5 Sonnet, or Gemini 1.5 Flash).
   - Question 4 (Observability): Tracing spans, latency monitoring, and hallucination scoring.
   - Question 5 (Operating Team): Required team skills to operate the chosen stack.

3. **Managed vs Application-Owned Component Table**:
   - Example: Managed Cloud OCR vs Custom Table Extractor; Managed Vector Store vs Custom pgvector.

4. **Evaluation & Quality Gate Plan**:
   - Define a Golden Test Dataset (e.g. 50 labeled historical claims with ground-truth anomalies).
   - Define Pass/Fail threshold (e.g. >= 95% code extraction accuracy; >= 90% confidence for auto-approval).

5. **Mandatory Disqualified Alternative (Critical Requirement)**:
   - Students must explicitly name one cloud platform they **rejected** (e.g. AWS Bedrock or Google Cloud) and provide concrete technical or operational reasons (e.g. procurement delay for new BAA, lack of native Teams integration, or high fixed cluster costs).

---

### Grading Rubric (Total: 100 Points)

| Criteria | Max Points | Description |
| :--- | :---: | :--- |
| **1. Architecture Flow & Layering** | 25 pts | Complete end-to-end flow from scanned PDF to human review queue. Clear separation of offline and online paths. |
| **2. Security & Compliance Controls** | 20 pts | Explicit handling of HIPAA BAA, PII masking, customer-managed KMS encryption, and role-based access. |
| **3. Evaluation & Guardrails Plan** | 20 pts | Realistic Golden Dataset definition, hallucination check, and automated confidence scoring (< 90% routing). |
| **4. Cost & Operating Model Defense** | 15 pts | Realistic justification of platform fit, awareness of fixed vs variable pricing (PTU vs PayG vs OCUs). |
| **5. Disqualified Alternative Defense** | 20 pts | Concrete, defensible technical rejection of an alternative cloud provider (zero points if missing). |
