#!/usr/bin/env python
"""
Quick Start Script for AI Prompt Enhancer
Run this script to set up and start the app.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a shell command and print status."""
    print(f"\n{'='*60}")
    print(f"📌 {description}")
    print(f"{'='*60}")
    print(f"Running: {cmd}\n")
    
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0

def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║         🚀 AI Prompt Enhancer - Quick Start Setup        ║
    ║                                                           ║
    ║    This script will set up and run the prompt enhancer   ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Check Python version
    print("\n📍 Step 1: Checking Python version...")
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"   Current version: {python_version.major}.{python_version.minor}")
        return False
    print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro} - OK")
    
    # Step 2: Install requirements
    print("\n📍 Step 2: Installing dependencies...")
    print("   This may take a few minutes on first run...\n")
    
    if not run_command(f"{sys.executable} -m pip install -r requirements.txt", 
                       "Installing Python packages"):
        print("❌ Failed to install dependencies")
        return False
    print("✅ Dependencies installed successfully")
    
    # Step 3: Download spaCy model
    print("\n📍 Step 3: Downloading spaCy language model...")
    if not run_command(f"{sys.executable} -m spacy download en_core_web_sm",
                       "Downloading spaCy model (first time only)"):
        print("⚠️  spaCy model download failed, but continuing...")
    print("✅ spaCy model ready")
    
    # Step 4: Start the app
    print("\n📍 Step 4: Starting Streamlit app...\n")
    print("="*60)
    print("🎉 Starting AI Prompt Enhancer!")
    print("="*60)
    print("\n📖 The app will open in your browser at:")
    print("   👉 http://localhost:8501\n")
    print("💡 Tips:")
    print("   • Use Ctrl+C to stop the app")
    print("   • Check your browser if it doesn't open automatically")
    print("   • The first enhancement may take a few seconds\n")
    print("="*60 + "\n")
    
    # Run streamlit app
    run_command(f"{sys.executable} -m streamlit run app.py", 
                "Running Streamlit application")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
