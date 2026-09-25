"""
Zero-dependency web server for Module 02 Live Demo Studio.
Runs locally on standard library Python 3.9+ without pip install.
Compatible with Windows, macOS, and Linux.
Supports both package execution and direct script execution.
"""
import os
import sys
import json
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

try:
    from .graph import build_reconciliation_graph
except (ImportError, ValueError):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from graph import build_reconciliation_graph

HTML_PATH = os.path.join(os.path.dirname(__file__), "web", "index.html")
APP_INSTANCE = None

def get_graph():
    global APP_INSTANCE
    if APP_INSTANCE is None:
        APP_INSTANCE = build_reconciliation_graph("demo_web.db")
    return APP_INSTANCE

class DemoRequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, data: dict, status_code: int = 200):
        body = json.dumps(data, default=str).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path in ["/", "/index.html"]:
            try:
                with open(HTML_PATH, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_error(500, f"Error reading web template: {e}")
            return

        if path == "/api/run":
            query = parse_qs(parsed.query)
            scenario = query.get("scenario", ["sc2"])[0]
            app = get_graph()

            if scenario == "sc1":
                thread_id = "thread_web_sc1"
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
            elif scenario == "sc3":
                thread_id = "thread_web_sc3"
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
            else:  # sc2: HITL Breakpoint demo
                thread_id = "thread_web_sc2"
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

            config = {"configurable": {"thread_id": thread_id}}
            result_state = app.invoke(payload, config=config)
            result_state["thread_id"] = thread_id
            self._send_json(result_state)
            return

        self.send_error(404, "Endpoint not found")

    def do_POST(self):
        if self.path == "/api/resume":
            length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(length)
            body = json.loads(raw_body.decode("utf-8"))

            thread_id = body.get("thread_id", "thread_web_sc2")
            billed_amount = float(body.get("billed_amount", 14050.00))
            approved_by = body.get("approved_by", "cfo_alice@enterprise.com")

            app = get_graph()
            config = {"configurable": {"thread_id": thread_id}}
            
            # Apply state mutation
            mutation = {
                "billed_amount": billed_amount,
                "approved_by": approved_by,
                "approval_status": "APPROVED_BY_CFO"
            }
            app.update_state(config, mutation)

            # Resume execution
            resumed_state = app.invoke(None, config=config)
            resumed_state["thread_id"] = thread_id
            self._send_json(resumed_state)
            return

        self.send_error(404, "Endpoint not found")

def start_server(port: int = 8080):
    server_address = ("", port)
    try:
        httpd = HTTPServer(server_address, DemoRequestHandler)
    except OSError:
        port = 8081
        server_address = ("", port)
        httpd = HTTPServer(server_address, DemoRequestHandler)

    url = f"http://localhost:{port}"
    print(f"\n================================================================================")
    print(f"  MODULE 02 LIVE DEMO STUDIO RUNNING AT: {url}")
    print(f"  Opening browser automatically... (Press Ctrl+C to stop)")
    print(f"================================================================================\n")
    
    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping web studio. Goodbye!")
        httpd.server_close()

if __name__ == "__main__":
    start_server()
