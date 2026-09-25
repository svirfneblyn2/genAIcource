@echo off
title Module 02 Live Demo Launcher
color 0b

cd /d "%~dp0"

echo ================================================================================
echo   STARTING MODULE 02 AGENT ORCHESTRATION LIVE STUDIO
echo ================================================================================

where python >nul 2>nul
if %errorlevel% neq 0 (
    where py >nul 2>nul
    if %errorlevel% neq 0 (
        echo [ERROR] Python not found in PATH. Please install Python 3.9+ from python.org
        pause
        exit /b 1
    ) else (
        py main.py
        exit /b 0
    )
)

python main.py

if %errorlevel% neq 0 (
    echo.
    echo Application exited with an error. Press any key to close.
    pause
)
