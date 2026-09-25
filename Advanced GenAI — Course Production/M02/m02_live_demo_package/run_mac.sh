#!/usr/bin/env bash
# macOS and Linux Launcher for Module 02 Live Demo

echo "================================================================================"
echo "  STARTING MODULE 02 AGENT ORCHESTRATION LIVE STUDIO (macOS / Linux)"
echo "================================================================================"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${SCRIPT_DIR}"

if command -v python3 &>/dev/null; then
    PYTHON_BIN="python3"
elif command -v python &>/dev/null; then
    PYTHON_BIN="python"
else
    echo "[ERROR] Python 3 was not found. Please install Python 3.9+ via brew install python or python.org"
    exit 1
fi

"${PYTHON_BIN}" main.py
