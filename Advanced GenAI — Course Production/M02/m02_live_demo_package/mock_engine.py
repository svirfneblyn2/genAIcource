"""
Deterministic standalone StateGraph engine for Module 02 Live Demo.
Provides zero-dependency LangGraph API compatibility for offline lectures.
"""
import copy
import sqlite3
import json
from typing import Dict, Any, List, Callable, Optional

class StandaloneSqliteSaver:
    """
    Local SQLite checkpointer providing state persistence across steps.
    """
    def __init__(self, db_path: str = "checkpoints.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS checkpoints (
                    thread_id TEXT,
                    step_index INTEGER,
                    node_name TEXT,
                    state_json TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (thread_id, step_index)
                )
            """)
            conn.commit()
        finally:
            conn.close()

    def save(self, thread_id: str, step_index: int, node_name: str, state: Dict[str, Any]):
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(
                "INSERT OR REPLACE INTO checkpoints (thread_id, step_index, node_name, state_json) VALUES (?, ?, ?, ?)",
                (thread_id, step_index, node_name, json.dumps(state, default=str))
            )
            conn.commit()
        finally:
            conn.close()

    def load_latest(self, thread_id: str) -> Optional[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.execute(
                "SELECT state_json FROM checkpoints WHERE thread_id = ? ORDER BY step_index DESC LIMIT 1",
                (thread_id,)
            )
            row = cur.fetchone()
            if row:
                return json.loads(row[0])
            return None
        finally:
            conn.close()

    def get_max_step(self, thread_id: str) -> int:
        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.execute(
                "SELECT COALESCE(MAX(step_index), 0) FROM checkpoints WHERE thread_id = ?",
                (thread_id,)
            )
            row = cur.fetchone()
            return row[0] if row else 0
        finally:
            conn.close()

class StandaloneStateGraph:
    """
    Standalone graph compiler matching the LangGraph StateGraph interface.
    """
    def __init__(self, state_schema):
        self.state_schema = state_schema
        self.nodes: Dict[str, Callable] = {}
        self.edges: Dict[str, str] = {}
        self.conditional_edges: Dict[str, tuple] = {}
        self.entry_point: Optional[str] = None

    def add_node(self, name: str, func: Callable):
        self.nodes[name] = func

    def set_entry_point(self, name: str):
        self.entry_point = name

    def add_edge(self, start_key: str, end_key: str):
        self.edges[start_key] = end_key

    def add_conditional_edges(self, source: str, path: Callable, path_map: Dict[str, str]):
        self.conditional_edges[source] = (path, path_map)

    def compile(self, checkpointer=None, interrupt_before: Optional[List[str]] = None):
        return CompiledStandaloneGraph(
            nodes=self.nodes,
            edges=self.edges,
            conditional_edges=self.conditional_edges,
            entry_point=self.entry_point,
            checkpointer=checkpointer,
            interrupt_before=interrupt_before or []
        )

class CompiledStandaloneGraph:
    """
    Compiled graph runtime with superstep execution, breakpoints, and resume.
    """
    def __init__(self, nodes, edges, conditional_edges, entry_point, checkpointer, interrupt_before):
        self.nodes = nodes
        self.edges = edges
        self.conditional_edges = conditional_edges
        self.entry_point = entry_point
        self.checkpointer = checkpointer or StandaloneSqliteSaver()
        self.interrupt_before = set(interrupt_before)
        self.interrupted_threads: Dict[str, str] = {}  # thread_id -> next_node

    def invoke(self, state_input: Optional[Dict[str, Any]], config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        config = config or {}
        thread_id = config.get("configurable", {}).get("thread_id", "default_thread")
        
        resumed_node = None
        if state_input is None:
            state = self.checkpointer.load_latest(thread_id)
            if not state:
                raise ValueError(f"No checkpoint found for thread_id '{thread_id}' to resume.")
            current_node = self.interrupted_threads.pop(thread_id, None)
            if not current_node:
                raise ValueError(f"Thread '{thread_id}' is not currently interrupted.")
            resumed_node = current_node
            step_index = self.checkpointer.get_max_step(thread_id) + 1
        else:
            state = copy.deepcopy(state_input)
            current_node = self.entry_point
            step_index = 0

        while current_node and current_node != "END":
            # Check for interrupt breakpoint (skip if this is the node being actively resumed)
            if current_node in self.interrupt_before and current_node != resumed_node and thread_id not in self.interrupted_threads:
                self.interrupted_threads[thread_id] = current_node
                self.checkpointer.save(thread_id, step_index, current_node, state)
                state["__interrupt__"] = current_node
                state["status"] = "INTERRUPTED"
                return state

            resumed_node = None  # Clear bypass after the first step

            # Execute node
            node_fn = self.nodes[current_node]
            updates = node_fn(state)
            
            # Apply state updates
            if updates:
                for k, v in updates.items():
                    if k == "logs" and "logs" in state:
                        state["logs"].extend(v if isinstance(v, list) else [v])
                    elif k == "messages" and "messages" in state:
                        state["messages"].extend(v if isinstance(v, list) else [v])
                    else:
                        state[k] = v

            step_index += 1
            self.checkpointer.save(thread_id, step_index, current_node, state)

            # Determine next node
            if current_node in self.conditional_edges:
                router_fn, path_map = self.conditional_edges[current_node]
                decision = router_fn(state)
                current_node = path_map.get(decision, "END")
            else:
                current_node = self.edges.get(current_node, "END")

        state.pop("__interrupt__", None)
        return state

    def update_state(self, config: Dict[str, Any], values: Dict[str, Any]):
        thread_id = config.get("configurable", {}).get("thread_id", "default_thread")
        state = self.checkpointer.load_latest(thread_id)
        if not state:
            raise ValueError(f"No checkpoint found for thread_id '{thread_id}' to update.")
        for k, v in values.items():
            state[k] = v
        next_step = self.checkpointer.get_max_step(thread_id) + 1
        self.checkpointer.save(thread_id, next_step, "human_mutation", state)
        return {"status": "STATE_UPDATED", "thread_id": thread_id}
