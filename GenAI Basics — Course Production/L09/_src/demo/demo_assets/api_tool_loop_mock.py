import json

def mock_claude_tool_loop():
    user_request = "Build a support triage dashboard from support_tickets.csv"
    print("USER:", user_request)
    tool_use = {
        "type": "tool_use",
        "name": "read_csv_summary",
        "input": {"path": "support_tickets.csv", "group_by": ["severity", "owner"]}
    }
    print("CLAUDE REQUESTS TOOL:")
    print(json.dumps(tool_use, indent=2))
    tool_result = {
        "p1_stale": ["T-1001", "T-1006"],
        "missing_owner": ["T-1005", "T-1010"],
        "owner_load": {"Marta": 3, "Jon": 3, "Ravi": 2, "Anya": 2, "missing": 2}
    }
    print("APPLICATION SENDS TOOL RESULT:")
    print(json.dumps(tool_result, indent=2))
    print("CLAUDE FINAL RESPONSE:")
    print("Create dashboard with stale P1 section above the fold and owner-missing warning.")

if __name__ == "__main__":
    mock_claude_tool_loop()
