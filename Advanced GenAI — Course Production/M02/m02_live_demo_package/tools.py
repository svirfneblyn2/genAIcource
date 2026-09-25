"""
Deterministic tool layer for Module 02 Live Demo.
Provides local mock ERP database, ledger posting, and fault injection.
"""
from typing import Dict, Any

# Pre-seeded ERP database records (SAP / NetSuite mock)
ERP_DATABASE = {
    "PO-4011": {
        "po_number": "PO-4011",
        "vendor_id": "VEND-ACME-CORP",
        "authorized_amount": 14050.00,
        "status": "APPROVED",
        "currency": "USD"
    },
    "PO-8821": {
        "po_number": "PO-8821",
        "vendor_id": "VEND-ACME-CORP",
        "authorized_amount": 12500.00,
        "status": "APPROVED",
        "currency": "USD"
    },
    "PO-9900": {
        "po_number": "PO-9900",
        "vendor_id": "VEND-GLOBAL-TECH",
        "authorized_amount": 8400.00,
        "status": "APPROVED",
        "currency": "USD"
    }
}

class ToolExecutionError(Exception):
    """Raised when an external tool or database fails."""
    pass

def query_erp_po(po_number: str, simulate_timeout: bool = False) -> Dict[str, Any]:
    """
    Simulates a sandboxed SQL query to SAP ERP.
    If simulate_timeout is True, raises a simulated HTTP 504 / DB Connection Timeout.
    """
    if simulate_timeout:
        raise ToolExecutionError("DB_CONNECTION_TIMEOUT: ERP cluster did not respond within 5000ms (504 Gateway Timeout)")
    
    record = ERP_DATABASE.get(po_number)
    if not record:
        raise ToolExecutionError(f"RECORD_NOT_FOUND: PO '{po_number}' does not exist in ERP database")
    
    return record

def post_to_general_ledger(invoice_id: str, amount: float, vendor_id: str, authorizer: str) -> Dict[str, Any]:
    """
    Simulates writing a journal entry to the corporate general ledger.
    """
    journal_id = f"JE-{invoice_id.replace('INV-', '')}-POSTED"
    return {
        "status": "SUCCESS",
        "journal_entry_id": journal_id,
        "amount_posted": amount,
        "vendor_id": vendor_id,
        "authorized_by": authorizer,
        "ledger_account": "2100-ACCOUNTS-PAYABLE"
    }
