"""
State definitions for Module 02 Live Demo: Autonomous Accounts Payable Agent.
Defines the typed channel schema and message reducers.
"""
from typing import TypedDict, List, Dict, Any, Optional
import operator

def append_log(existing: List[str], new_val: Any) -> List[str]:
    """Append-only reducer for immutable audit trail."""
    if existing is None:
        existing = []
    if isinstance(new_val, list):
        return existing + new_val
    return existing + [str(new_val)]

class InvoiceState(TypedDict):
    """
    Central state schema for the accounts payable reconciliation graph.
    All nodes communicate strictly via these typed channels.
    """
    # Core Invoice Metadata
    invoice_id: str
    vendor_id: str
    billed_amount: float
    po_number: str
    line_items: List[Dict[str, Any]]
    
    # Reconciliation Audit Fields
    po_authorized_amount: float
    variance: float
    reconciled: bool
    
    # Governance & HITL Fields
    approval_status: str  # 'AUTO_APPROVED', 'AWAITING_HUMAN_APPROVAL', 'APPROVED_BY_CFO', 'REJECTED'
    approved_by: Optional[str]
    audit_notes: str
    
    # Fault Tolerance & Circuit Breaker Channels
    retry_count: int
    circuit_broken: bool
    
    # Append-only Audit Trail & Messages
    logs: List[str]
    messages: List[Dict[str, str]]
