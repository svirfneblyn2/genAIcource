"""
Automated validation test suite for Module 02 Live Demo Package.
Verifies all 3 scenarios pass without errors.
"""
import os
import unittest
from .graph import build_reconciliation_graph

class TestLiveDemoScenarios(unittest.TestCase):
    def test_scenario_1_auto_approve(self):
        """Verify matching invoice auto-approves and posts to ledger without pausing."""
        db_path = "test_sc1.db"
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
            except Exception:
                pass

        app = build_reconciliation_graph(db_path)
        payload = {
            "invoice_id": "INV-1001",
            "vendor_id": "VEND-ACME-CORP",
            "billed_amount": 12500.00,
            "po_number": "PO-8821",
            "line_items": [],
            "po_authorized_amount": 0.0,
            "variance": 0.0,
            "reconciled": False,
            "approval_status": "NEW",
            "approved_by": None,
            "audit_notes": "",
            "retry_count": 0,
            "circuit_broken": False,
            "logs": [],
            "messages": []
        }
        res = app.invoke(payload, config={"configurable": {"thread_id": "t_test_sc1"}})
        self.assertEqual(res["approval_status"], "POSTED_TO_LEDGER")
        self.assertEqual(res["variance"], 0.0)
        self.assertTrue(res["reconciled"])

    def test_scenario_2_hitl_breakpoint_and_resumption(self):
        """Verify invoice with discrepancy hits breakpoint, pauses, and resumes on mutation."""
        db_path = "test_sc2.db"
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
            except Exception:
                pass

        app = build_reconciliation_graph(db_path)
        payload = {
            "invoice_id": "INV-8912",
            "vendor_id": "VEND-ACME-CORP",
            "billed_amount": 14500.00,
            "po_number": "PO-4011",
            "line_items": [],
            "po_authorized_amount": 0.0,
            "variance": 0.0,
            "reconciled": False,
            "approval_status": "NEW",
            "approved_by": None,
            "audit_notes": "",
            "retry_count": 0,
            "circuit_broken": False,
            "logs": [],
            "messages": []
        }
        config = {"configurable": {"thread_id": "t_test_sc2"}}

        # Phase 1: Must hit breakpoint before node_human_post_ledger
        halted_state = app.invoke(payload, config=config)
        self.assertEqual(halted_state["approval_status"], "AWAITING_HUMAN_APPROVAL")
        self.assertEqual(halted_state["variance"], 450.0)
        self.assertFalse(halted_state["reconciled"])

        # Phase 2: Simulate human state mutation
        app.update_state(config, {
            "billed_amount": 14050.00,
            "approved_by": "cfo_alice@enterprise.com",
            "approval_status": "APPROVED_BY_CFO"
        })

        # Phase 3: Resume graph
        resumed_state = app.invoke(None, config=config)
        self.assertEqual(resumed_state["approval_status"], "POSTED_TO_LEDGER")
        self.assertEqual(resumed_state["approved_by"], "cfo_alice@enterprise.com")
        self.assertTrue(resumed_state["reconciled"])

    def test_scenario_3_circuit_breaker(self):
        """Verify tool failures increment retry cap and route to dead-letter queue."""
        db_path = "test_sc3.db"
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
            except Exception:
                pass

        app = build_reconciliation_graph(db_path)
        payload = {
            "invoice_id": "INV-FAIL-500",
            "vendor_id": "VEND-ACME-CORP",
            "billed_amount": 9900.00,
            "po_number": "PO-FAIL",
            "simulate_tool_fault": True,
            "line_items": [],
            "po_authorized_amount": 0.0,
            "variance": 0.0,
            "reconciled": False,
            "approval_status": "NEW",
            "approved_by": None,
            "audit_notes": "",
            "retry_count": 0,
            "circuit_broken": False,
            "logs": [],
            "messages": []
        }
        res = app.invoke(payload, config={"configurable": {"thread_id": "t_test_sc3"}})
        self.assertEqual(res["approval_status"], "CIRCUIT_BREAKER_TRIGGERED")
        self.assertTrue(res["circuit_broken"])
        self.assertFalse(res["reconciled"])

if __name__ == "__main__":
    unittest.main()
