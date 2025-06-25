# Jarvis Voice AI Agent - PowerShell Launcher
# Run this script to start Jarvis

Write-Host "🤖 Starting Jarvis Voice AI Agent..." -ForegroundColor Green
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.7 or higher." -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if .env file exists
if (Test-Path ".env") {
    Write-Host "✅ Environment file found" -ForegroundColor Green
} else {
    Write-Host "⚠️  No .env file found. Please create one with your OpenAI API key." -ForegroundColor Yellow
    Write-Host "Copy env_example.txt to .env and add your API key." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🚀 Launching Jarvis..." -ForegroundColor Cyan
Write-Host ""

# Run Jarvis
try {
    python jarvis_agent.py
} catch {
    Write-Host "❌ Error running Jarvis: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting tips:" -ForegroundColor Yellow
    Write-Host "1. Run 'python setup.py' to install dependencies" -ForegroundColor Yellow
    Write-Host "2. Run 'python test_setup.py' to check your setup" -ForegroundColor Yellow
    Write-Host "3. Make sure your OpenAI API key is configured" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Press Enter to exit" 