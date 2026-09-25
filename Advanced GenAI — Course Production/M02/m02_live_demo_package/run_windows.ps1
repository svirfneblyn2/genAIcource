# Windows PowerShell Launcher for Module 02 Live Demo
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  STARTING MODULE 02 AGENT ORCHESTRATION LIVE STUDIO (POWERSHELL)" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "[ERROR] Python was not found in your PATH. Please install Python 3.9+." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

$parentDir = Split-Path -Parent $PSScriptRoot
Set-Location $parentDir

python -m m02_live_demo_package
