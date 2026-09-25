"""
StateGraph definition for Module 02 Live Demo: Accounts Payable Reconciliation Agent.
Works seamlessly with official LangGraph or standalone zero-dependency fallback.
Supports both package execution and direct script execution.
"""
import sys
import os
from typing import Dict, Any

try:
    from langgraph.graph import StateGraph, END
    from langgraph.checkpoint.sqlite import SqliteSaver
    USING_OFFICIAL_LANGGRAPH = True
except ImportError:
    USING_OFFICIAL_LANGGRAPH = False

if not USING_OFFICIAL_LANGGRAPH:
    try:
        from .mock_engine import StandaloneStateGraph as StateGraph, StandaloneSqliteSaver as SqliteSaver
    except (ImportError, ValueError):
        from mock_engine import StandaloneStateGraph as StateGraph, StandaloneSqliteSaver as SqliteSaver
    END = "END"

try:
    from .state import InvoiceState
    from .tools import query_erp_po, post_to_general_ledger, ToolExecutionError
except (ImportError, ValueError):
    from state import InvoiceState
    from tools import query_erp_po, post_to_general_ledger, ToolExecutionError

# Node 1: Ingest & Extract
def node_ocr_extract(state: InvoiceState) -> Dict[str, Any]:
    invoice_id = state.get("invoice_id", "UNKNOWN")
    amt = state.get("billed_amount", 0.0)
    return {
        "logs": [f"[SUPERSTEP 1: OCR] Extracted invoice {invoice_id} with billed total ${amt:,.2f}"],
        "reconciled": False
    }

# Node 2: Sandboxed ERP Lookup with Fault Detection
def node_erp_lookup(state: InvoiceState) -> Dict[str, Any]:
    po_num = state.get("po_number", "")
    retry_count = state.get("retry_count", 0)
    simulate_fault = state.get("simulate_tool_fault", False)

    # In fault simulation mode, fail on first 2 attempts, trigger circuit breaker on 3rd
    if simulate_fault and retry_count < 3:
        new_retries = retry_count + 1
        return {
            "retry_count": new_retries,
            "circuit_broken": (new_retries >= 3),
            "logs": [f"[SUPERSTEP 2: ERP LOOKUP] Error: DB_CONNECTION_TIMEOUT (Attempt {new_retries}/3)"]
        }

    try:
        po_record = query_erp_po(po_num)
        return {
            "po_authorized_amount": po_record["authorized_amount"],
            "logs": [f"[SUPERSTEP 2: ERP LOOKUP] Found {po_num}: authorized ${po_record['authorized_amount']:,.2f}"]
        }
    except ToolExecutionError as e:
        new_retries = retry_count + 1
        return {
            "retry_count": new_retries,
            "circuit_broken": (new_retries >= 3),
            "logs": [f"[SUPERSTEP 2: ERP LOOKUP] Exception caught: {str(e)} (Attempt {new_retries}/3)"]
        }

# Node 3: Reconcile Variance
def node_reconcile(state: InvoiceState) -> Dict[str, Any]:
    billed = state.get("billed_amount", 0.0)
    auth = state.get("po_authorized_amount", 0.0)
    variance = round(billed - auth, 2)
    
    if variance == 0.0:
        status = "AUTO_APPROVED"
        log_msg = "[SUPERSTEP 3: RECONCILE] Variance $0.00 -> Eligible for automatic general ledger posting"
    else:
        status = "AWAITING_HUMAN_APPROVAL"
        log_msg = f"[SUPERSTEP 3: RECONCILE] Variance +${variance:,.2f} detected! Halting at HITL breakpoint"

    return {
        "variance": variance,
        "approval_status": status,
        "logs": [log_msg]
    }

# Conditional Router
def router_variance_check(state: InvoiceState) -> str:
    if state.get("circuit_broken", False):
        return "route_circuit_breaker"
    if state.get("retry_count", 0) > 0 and state.get("po_authorized_amount", 0.0) == 0.0:
        return "route_retry"
    if state.get("variance", 0.0) == 0.0:
        return "route_auto_ledger"
    return "route_human_ledger"

# Node 4A: Auto-Post to General Ledger (When variance == 0.0)
def node_auto_post_ledger(state: InvoiceState) -> Dict[str, Any]:
    inv_id = state.get("invoice_id", "")
    amt = state.get("billed_amount", 0.0)
    vendor = state.get("vendor_id", "")
    authorizer = "SYSTEM_AUTO_AUTHORIZATION"
    
    res = post_to_general_ledger(inv_id, amt, vendor, authorizer)
    return {
        "reconciled": True,
        "approval_status": "POSTED_TO_LEDGER",
        "audit_notes": f"Journal entry {res['journal_entry_id']} created for ${amt:,.2f}. Authorized by: {authorizer}",
        "logs": [f"[SUPERSTEP 4: LEDGER] Auto-posted! {res['journal_entry_id']} created for ${amt:,.2f}"]
    }

# Node 4B: Human-Approved Ledger Post (Gated by interrupt_before)
def node_human_post_ledger(state: InvoiceState) -> Dict[str, Any]:
    inv_id = state.get("invoice_id", "")
    amt = state.get("billed_amount", 0.0)
    vendor = state.get("vendor_id", "")
    authorizer = state.get("approved_by") or "PENDING_REVIEW"
    
    res = post_to_general_ledger(inv_id, amt, vendor, authorizer)
    return {
        "reconciled": True,
        "approval_status": "POSTED_TO_LEDGER",
        "audit_notes": f"Journal entry {res['journal_entry_id']} created for ${amt:,.2f}. Authorized by: {authorizer}",
        "logs": [f"[SUPERSTEP 4: LEDGER] Human-authorized! {res['journal_entry_id']} created. Approved by: {authorizer}"]
    }

# Node 5: Dead-Letter Queue / Circuit Breaker Node
def node_dead_letter(state: InvoiceState) -> Dict[str, Any]:
    return {
        "approval_status": "CIRCUIT_BREAKER_TRIGGERED",
        "audit_notes": "Execution aborted: Max retries (3) reached on tool call. Escaped infinite loop.",
        "logs": ["[CIRCUIT BREAKER] Infinite loop prevented. Thread quarantined to Dead-Letter Queue (DLQ)."]
    }

def build_reconciliation_graph(db_path: str = "checkpoints.db"):
    """
    Constructs and compiles the production state machine.
    Configured with interrupt_before=['node_human_post_ledger'] to enforce HITL gating.
    """
    checkpointer = SqliteSaver(db_path)
    workflow = StateGraph(InvoiceState)

    # Register Nodes
    workflow.add_node("node_ocr_extract", node_ocr_extract)
    workflow.add_node("node_erp_lookup", node_erp_lookup)
    workflow.add_node("node_reconcile", node_reconcile)
    workflow.add_node("node_auto_post_ledger", node_auto_post_ledger)
    workflow.add_node("node_human_post_ledger", node_human_post_ledger)
    workflow.add_node("node_dead_letter", node_dead_letter)

    # Define Linear Edges
    workflow.set_entry_point("node_ocr_extract")
    workflow.add_edge("node_ocr_extract", "node_erp_lookup")
    workflow.add_edge("node_erp_lookup", "node_reconcile")

    # Define Conditional Branch
    workflow.add_conditional_edges(
        "node_reconcile",
        router_variance_check,
        {
            "route_auto_ledger": "node_auto_post_ledger",
            "route_human_ledger": "node_human_post_ledger",
            "route_retry": "node_erp_lookup",
            "route_circuit_breaker": "node_dead_letter"
        }
    )

    workflow.add_edge("node_auto_post_ledger", END)
    workflow.add_edge("node_human_post_ledger", END)
    workflow.add_edge("node_dead_letter", END)

    # Compile with human-in-the-loop breakpoint on discrepancy path only
    app = workflow.compile(
        checkpointer=checkpointer,
        interrupt_before=["node_human_post_ledger"]
    )
    return app
