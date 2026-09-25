"""
Entry point for Module 02 Live Demo Package.
Runs on Windows, macOS, and Linux with standard library Python 3.9+.
Supports both package execution and direct script execution.
"""
import sys
import os

try:
    from .demo_cli import main as run_cli
    from .demo_web import start_server as run_web
except (ImportError, ValueError):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from demo_cli import main as run_cli
    from demo_web import start_server as run_web

def main():
    print("\n================================================================================")
    print("  MODULE 02: AGENT FRAMEWORKS & ORCHESTRATION - INSTRUCTOR LIVE KIT")
    print("================================================================================")
    print("Choose launch mode:")
    print("  1. Launch Web Visual Studio (Recommended: opens browser at localhost:8080)")
    print("  2. Launch High-Contrast Terminal CLI (For quick projector terminal runs)")
    print("  3. Exit")
    
    try:
        choice = input("\nEnter choice [1-3, default 1]: ").strip() or "1"
    except (EOFError, KeyboardInterrupt):
        choice = "1"

    if choice == "2":
        run_cli()
    elif choice == "3":
        sys.exit(0)
    else:
        run_web()

if __name__ == "__main__":
    main()
