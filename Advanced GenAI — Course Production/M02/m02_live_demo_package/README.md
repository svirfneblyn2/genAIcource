# Module 02 Live Demo Package: Autonomous Accounts Payable Agent

A self-contained, turnkey demonstration kit for instructors lecturing on Agent Frameworks, State Machines, and Human-in-the-Loop Orchestration.

Compatible with **Windows**, **macOS**, and **Linux**.
Runs on standard library Python 3.9+ with **zero mandatory pip dependencies**.

---

## 1. Quickstart (How to Run in 10 Seconds)

### On Windows
Simply double-click the launcher batch script in File Explorer:
```bat
run_windows.bat
```
Or run from PowerShell:
```powershell
.\run_windows.ps1
```

### On macOS / Linux
Open Terminal, navigate to the folder, and run:
```bash
chmod +x run_mac.sh
./run_mac.sh
```

---

## 2. What Happens When You Launch

1. A lightweight local web studio launches automatically at:
   `http://localhost:8080`
2. Your default web browser (Chrome, Safari, Edge) opens automatically.
3. You see the **Compiled State Machine Topology Canvas**:
   - `Node 1 (OCR Extract)` -> `Node 2 (ERP Lookup)` -> `Node 3 (Reconcile)` -> `Node 4 (Post Ledger)`
   - The red dashed **HITL Interrupt Barrier** before `post_to_ledger`.

---

## 3. The 3 Pre-Configured Scenarios

Click any scenario button on the left panel during class:

### Scenario 1: Auto-Approve ($0 Variance)
- **Input**: Invoice INV-1001 for $12,500.00 matching PO-8821.
- **Behavior**: Nodes 1, 2, 3 execute, detect zero discrepancy, and automatically route to `node_auto_post_ledger`. Runs to completion in under 1 second without pausing.

### Scenario 2: HITL Breakpoint & State Mutation (The Lecture Showcase)
- **Input**: Invoice INV-8912 for $14,500.00 vs PO-4011 for $14,050.00 ($450 discrepancy).
- **Behavior**:
  1. Nodes 1, 2, 3 execute and compute `variance = $450.00`.
  2. Execution safely halts with status `AWAITING_HUMAN_APPROVAL`.
  3. The `post_to_ledger` node illuminates amber with the `INTERRUPT` badge.
  4. The right panel displays the **Human-in-the-Loop Intervention Box**.
  5. As the instructor, click **"Approve & Resume Graph"** (or adjust the approved amount to $14,050.00).
  6. The graph unlocks, mutates state, and completes the ledger entry.

### Scenario 3: Fault Tolerance & Circuit Breaker (Anti-Loop Protection)
- **Input**: Simulated ERP network blackout (HTTP 504 / DB Connection Timeout).
- **Behavior**:
  1. The ERP lookup tool fails with connection timeout.
  2. The graph catches the error, increments `retry_count` (Attempts 1, 2, 3).
  3. On attempt 3, the **Circuit Breaker** triggers.
  4. Execution escapes the infinite loop and routes safely to the Dead-Letter Queue (DLQ).

---

## 4. Alternative: Terminal High-Contrast CLI Mode

If you prefer presenting directly inside your terminal or VS Code console without opening a browser:
```bash
python -m m02_live_demo_package.demo_cli
```
This interactive console features ANSI color codes and step-by-step pauses designed for large lecture room projectors.

---

## 5. Architectural Guarantees & Zero Dependencies

- **Offline Independence**: Works without internet access in lecture halls.
- **Zero API Spend**: Includes deterministic mock tools and local state automata ($0.00 spend).
- **ACID Persistence**: Writes real state checkpoints to `checkpoints.db` (SQLite).
- **LangGraph Compatible**: If `pip install langgraph` is run, it uses official LangGraph; otherwise, it uses the built-in standalone engine seamlessly.
