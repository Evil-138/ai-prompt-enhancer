@echo off
REM AI Prompt Enhancer - Windows Quick Start Script
REM This script sets up and runs the application on Windows

title AI Prompt Enhancer - Setup & Launch

echo.
echo =====================================================
echo  AI Prompt Enhancer - Windows Quick Start
echo =====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

REM Show Python version
echo Python version:
python --version
echo.

REM Install requirements
echo Installing dependencies...
echo (This may take a few minutes on first run)
echo.

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Installing spaCy model...
python -m spacy download en_core_web_sm

echo.
echo =====================================================
echo  Starting AI Prompt Enhancer...
echo =====================================================
echo.
echo The app will open at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the app
echo.

python -m streamlit run app.py

pause
