"""
Step 1: Document Ingestion, Parsing, and Structure-Aware Chunking.

Demonstrates the architectural difference between:
1. Naive fixed-size character chunking (cuts sentences, loses context)
2. Structure-aware chunking (preserves headers, hierarchy, and metadata tags)
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import re

@dataclass
class DocumentChunk:
    chunk_id: str
    doc_id: str
    title: str
    section: str
    content: str
    allowed_roles: List[str]
    version: str
    metadata: Dict[str, Any]

SAMPLE_DOCUMENTS = [
    {
        "doc_id": "POL-IT-101",
        "title": "Corporate Hardware and Laptop Loan Policy",
        "version": "2.4",
        "raw_text": """
# Corporate Hardware and Laptop Loan Policy

## Section 1: Eligibility and Scope
All full-time employees, contractors, and temporary interns are eligible for standard hardware issuance. Standard issue includes one laptop workstation and associated peripherals.

## Section 2: Temporary Hardware Loans
Employees requiring a temporary replacement laptop due to travel, hardware failure, or project testing may request an emergency loan.
- Loan Duration: Up to 14 calendar days without manager extension.
- Collection Point: IT Service Desk, Room B12, Building 4.
- Extension Approval: Extensions beyond 14 days require written approval from a Director or Department Head.
- Overdue Policy: Equipment unreturned after 21 days is flagged as lost and remote wiped via MDM.

## Section 3: Hardware Disposal and Buyback
Employees in good standing for more than 3 years may purchase decommissioned laptops at 15% fair market salvage value upon IT asset depreciation sign-off.
        """.strip()
    },
    {
        "doc_id": "POL-HR-204",
        "title": "Remote Work and Home Office Expense Policy",
        "version": "1.8",
        "raw_text": """
# Remote Work and Home Office Expense Policy

## Section 1: Home Office Stipend
Full-time remote employees receive a one-time setup allowance of $500 for ergonomic office furniture and external monitors.
- Invoicing: Expense reports must be submitted within 30 days of purchase with itemized receipts.
- Prohibited Expenses: Luxury desks, gaming chairs, and home broadband subscription fees are strictly non-reimbursable.

## Section 2: Executive Hardware Tier (Confidential)
C-level executives and Senior VPs are eligible for Tier-4 priority hardware including encrypted cellular failover routers and dedicated redundant workstations.
- Access: Strictly restricted to executive level.
- Approval: Automated through Executive Support Desk.
        """.strip()
    },
    {
        "doc_id": "SEC-OPS-305",
        "title": "Incident Escalation and Lost Device Protocol",
        "version": "3.1",
        "raw_text": """
# Incident Escalation and Lost Device Protocol

## Section 1: Immediate Containment
If a corporate laptop or smartphone is lost, stolen, or compromised:
- Timeframe: The employee must notify the Security Operations Center (SOC) within 60 minutes.
- Hotline: Emergency SOC line: +1-800-555-0199 or Slack channel #soc-emergency.
- Immediate Actions: The SOC automatically revokes all active OAuth session tokens and issues a remote cryptographic wipe command.
        """.strip()
    }
]

def naive_fixed_chunking(text: str, chunk_size: int = 150, overlap: int = 30) -> List[str]:
    """Naive chunking by character count: cuts words and destroys semantic context."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks

def structure_aware_chunking(docs: List[Dict[str, Any]]) -> List[DocumentChunk]:
    """
    Structure-aware chunking:
    - Splits on markdown headers (## Section)
    - Preserves document hierarchy and title
    - Extracts and attaches security ACLs and version metadata
    """
    chunks = []
    chunk_counter = 1

    for doc in docs:
        doc_id = doc["doc_id"]
        title = doc["title"]
        version = doc["version"]
        raw = doc["raw_text"]

        sections = re.split(r'\n(?=##\s+)', raw)
        for sec in sections:
            sec = sec.strip()
            if not sec:
                continue

            lines = sec.split('\n')
            first_line = lines[0].strip()
            if first_line.startswith('## '):
                section_name = first_line.replace('## ', '').strip()
                body = '\n'.join(lines[1:]).strip()
            elif first_line.startswith('# '):
                section_name = "Overview"
                body = '\n'.join(lines[1:]).strip()
            else:
                section_name = "General"
                body = sec

            allowed_roles = ["all"]
            if "Confidential" in section_name or "Executive" in section_name:
                allowed_roles = ["executive", "hr_admin"]
            elif "Expense" in title or "HR" in doc_id:
                allowed_roles = ["employee", "manager", "hr_admin", "executive"]

            enriched_content = f"Document: {title} ({doc_id})\nSection: {section_name}\n\n{body}"

            chunk = DocumentChunk(
                chunk_id=f"chk_{chunk_counter:03d}",
                doc_id=doc_id,
                title=title,
                section=section_name,
                content=enriched_content,
                allowed_roles=allowed_roles,
                version=version,
                metadata={
                    "char_length": len(enriched_content),
                    "word_count": len(enriched_content.split()),
                    "has_dates": bool(re.search(r'\d+\s+(days|calendar days)', enriched_content)),
                    "has_money": bool(re.search(r'\$\d+', enriched_content))
                }
            )
            chunks.append(chunk)
            chunk_counter += 1

    return chunks

if __name__ == "__main__":
    print("=" * 70)
    print("DEMO STEP 1: DOCUMENT INGESTION & STRUCTURE-AWARE CHUNKING")
    print("=" * 70)

    print("\n[A] Naive Fixed-Size Chunking Example (First 2 chunks of POL-IT-101):")
    sample_text = SAMPLE_DOCUMENTS[0]["raw_text"]
    naive_chunks = naive_fixed_chunking(sample_text, chunk_size=160, overlap=30)
    for i, c in enumerate(naive_chunks[:2], 1):
        print(f"--- Naive Chunk #{i} ({len(c)} chars) ---")
        print(repr(c))

    print("\n[B] Structure-Aware Chunking (Parsed with semantic headers & ACL metadata):")
    structured_chunks = structure_aware_chunking(SAMPLE_DOCUMENTS)
    print(f"Generated {len(structured_chunks)} clean, structure-preserved chunks.\n")

    for chk in structured_chunks:
        print(f"ID: [{chk.chunk_id}] | Doc: {chk.doc_id} § {chk.section}")
        print(f"    Roles Allowed: {chk.allowed_roles} | Length: {chk.metadata['word_count']} words")
        print(f"    Sample Preview: {chk.content.splitlines()[-1][:75]}...")
        print("-" * 70)
