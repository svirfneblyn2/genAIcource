"""
Interactive CLI Demonstrator for Module 02: Accounts Payable Agent.
Designed for live projection during lectures on Windows, macOS, and Linux.
Supports both package execution and direct script execution.
"""
import sys
import os
import time

try:
    from .graph import build_reconciliation_graph
except (ImportError, ValueError):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from graph import build_reconciliation_graph

# ANSI Color Codes for high-contrast presentation terminal
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header(text: str):
    print(f"\n{BOLD}{CYAN}================================================================================{RESET}")
    print(f"{BOLD}{CYAN}  {text}{RESET}")
    print(f"{BOLD}{CYAN}================================================================================{RESET}")

def run_scenario_1():
    print_header("SCENARIO 1: AUTO-APPROVE PATH (ZERO VARIANCE)")
    print("Injecting Invoice INV-1001 matching PO-8821 ($12,500.00).")
    
    app = build_reconciliation_graph("demo_sc1.db")
    payload = {
        "invoice_id": "INV-1001",
        "vendor_id": "VEND-ACME-CORP",
        "billed_amount": 12500.00,
        "po_number": "PO-8821",
        "line_items": [{"sku": "PARTS", "qty": 10, "unit_price": 1250.00}],
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

    config = {"configurable": {"thread_id": "thread_auto_001"}}
    state = app.invoke(payload, config=config)

    for log in state.get("logs", []):
        print(f"  {GREEN}{log}{RESET}")
        time.sleep(0.3)

    print(f"\n{BOLD}Result:{RESET} {GREEN}{state.get('approval_status')}{RESET}")
    print(f"{BOLD}Notes:{RESET} {state.get('audit_notes')}")

def run_scenario_2():
    print_header("SCENARIO 2: LIVE LECTURE DEMO (HITL BREAKPOINT & STATE MUTATION)")
    print("Injecting Invoice INV-8912 ($14,500.00) vs PO-4011 ($14,050.00). Discrepancy = $450.00.")

    app = build_reconciliation_graph("demo_sc2.db")
    payload = {
        "invoice_id": "INV-8912",
        "vendor_id": "VEND-ACME-CORP",
        "billed_amount": 14500.00,
        "po_number": "PO-4011",
        "line_items": [{"sku": "HEAVY-MOTOR", "qty": 1, "unit_price": 14500.00}],
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

    config = {"configurable": {"thread_id": "thread_hitl_8912"}}

    # Phase 1: Run to Breakpoint
    print(f"\n{BOLD}[PHASE 1: RUNNING GRAPH TO BREAKPOINT]{RESET}")
    state = app.invoke(payload, config=config)

    for log in state.get("logs", []):
        print(f"  {CYAN}{log}{RESET}")
        time.sleep(0.3)

    print(f"\n{BOLD}{YELLOW}>>> BREAKPOINT TRIGGERED (interrupt_before=['node_human_post_ledger']) <<<{RESET}")
    print(f"  Thread ID:       {config['configurable']['thread_id']}")
    print(f"  Billed Amount:   ${state.get('billed_amount'):,.2f}")
    print(f"  PO Authorized:   ${state.get('po_authorized_amount'):,.2f}")
    print(f"  Variance:        {RED}+${state.get('variance'):,.2f}{RESET}")
    print(f"  Status:          {YELLOW}{state.get('approval_status')}{RESET}")
    print(f"  Checkpointer:    State persisted to SQLite. Process memory can be wiped safely.")

    # Phase 2: Live Human Interaction
    print(f"\n{BOLD}[PHASE 2: HUMAN-IN-THE-LOOP STATE MUTATION]{RESET}")
    print("Press ENTER to simulate CFO review and state correction...")
    try:
        input()
    except EOFError:
        pass

    print(f"{MAGENTA}Action: CFO reviewed contract dispute. Deducting $450 unauthorized fee.{RESET}")
    mutation = {
        "billed_amount": 14050.00,
        "approved_by": "cfo_alice@enterprise.com",
        "approval_status": "APPROVED_BY_CFO"
    }
    app.update_state(config, mutation)
    print(f"{GREEN}[SUCCESS] Checkpoint updated in database: billed_amount=$14,050.00, approved_by='cfo_alice'{RESET}")

    # Phase 3: Resume Graph
    print(f"\n{BOLD}[PHASE 3: RESUMING GRAPH EXECUTION]{RESET}")
    resumed_state = app.invoke(None, config=config)

    for log in resumed_state.get("logs", [])[-1:]:
        print(f"  {GREEN}{log}{RESET}")

    print(f"\n{BOLD}Final Ledger Audit:{RESET}")
    print(f"  Status:  {GREEN}{resumed_state.get('approval_status')}{RESET}")
    print(f"  Details: {resumed_state.get('audit_notes')}")

def run_scenario_3():
    print_header("SCENARIO 3: FAULT TOLERANCE & CIRCUIT BREAKER")
    print("Simulating ERP network blackout (HTTP 504 Timeout) to verify infinite-loop prevention.")

    app = build_reconciliation_graph("demo_sc3.db")
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

    config = {"configurable": {"thread_id": "thread_circuit_breaker"}}
    state = app.invoke(payload, config=config)

    for log in state.get("logs", []):
        if "Attempt" in log:
            print(f"  {YELLOW}{log}{RESET}")
        else:
            print(f"  {RED}{log}{RESET}")
        time.sleep(0.3)

    print(f"\n{BOLD}Circuit Breaker Result:{RESET} {RED}{state.get('approval_status')}{RESET}")
    print(f"{BOLD}Dead-Letter Audit:{RESET}     {state.get('audit_notes')}")

def main():
    while True:
        print_header("MODULE 02: AGENT ORCHESTRATION LIVE DEMO CONSOLE")
        print("Select a pre-configured scenario to execute:")
        print("  1. Scenario 1: Auto-Approve Path ($0 Variance)")
        print("  2. Scenario 2: HITL Breakpoint & State Mutation (The Lecture Demo)")
        print("  3. Scenario 3: Tool Error & Circuit Breaker (Anti-Loop Guard)")
        print("  4. Run All Scenarios in Sequence")
        print("  5. Exit")
        
        try:
            choice = input(f"\n{BOLD}Enter selection [1-5]: {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(0)

        if choice == "1":
            run_scenario_1()
        elif choice == "2":
            run_scenario_2()
        elif choice == "3":
            run_scenario_3()
        elif choice == "4":
            run_scenario_1()
            run_scenario_2()
            run_scenario_3()
        elif choice == "5":
            print("Done. Happy lecturing!")
            break
        else:
            print(f"{RED}Invalid option. Please enter 1-5.{RESET}")

if __name__ == "__main__":
    main()
