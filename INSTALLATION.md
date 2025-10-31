# 📋 Installation & Setup Guide

Complete step-by-step guide to set up and run the AI Prompt Enhancer.

## 🖥️ System Requirements

Before you start, ensure your system meets these requirements:

- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended for smooth operation)
- **Disk Space**: ~2GB for models and libraries
- **Internet**: Required only for first installation to download models

## 📥 Installation Steps

### Step 1: Download Python (if not installed)

If you don't have Python installed:

1. Go to [python.org](https://www.python.org/downloads/)
2. Download **Python 3.10 or 3.11** (latest stable)
3. **Important**: During installation, check "Add Python to PATH"
4. Complete the installation

### Step 2: Download the Project

1. Download the `ai-prompt-optimiser` folder to your computer
2. Or clone via git: `git clone <repo-url>`
3. Navigate to the folder in your terminal

### Step 3: Create a Virtual Environment (Optional but Recommended)

A virtual environment keeps dependencies isolated. Run in the project folder:

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4: Install Dependencies

Run this command to install all required packages:

```bash
pip install -r requirements.txt
```

**First run**: This will take 5-15 minutes as it downloads libraries (~500MB).

### Step 5: Download spaCy Language Model

This is required for text analysis:

```bash
python -m spacy download en_core_web_sm
```

## 🚀 Running the Application

### Method 1: Using the Startup Script (Easiest)

**Windows:**
- Double-click `run.bat` file

**macOS/Linux:**
```bash
python quickstart.py
```

### Method 2: Manual Command Line

```bash
streamlit run app.py
```

### Method 3: Using Python Directly

```bash
python -m streamlit run app.py
```

## 🌐 Access the App

Once started, you'll see:
```
You can now view your Streamlit app in your browser.

  URL: http://localhost:8501
```

- Open your browser to `http://localhost:8501`
- The app will load automatically
- Start enhancing your prompts!

## 🔧 Troubleshooting

### ❌ "Python is not recognized"

**Problem**: The system can't find Python

**Solutions**:
1. Add Python to PATH:
   - Windows: Reinstall Python and check "Add Python to PATH"
   - macOS: Use `python3` instead of `python`
   - Linux: Install Python via package manager

2. Or use full path:
   ```bash
   C:\Python311\python.exe -m streamlit run app.py
   ```

### ❌ "ModuleNotFoundError: No module named 'streamlit'"

**Problem**: Dependencies not installed

**Solutions**:
1. Activate virtual environment if using one
2. Run installation again:
   ```bash
   pip install -r requirements.txt
   ```
3. Check you're in the correct folder

### ❌ "spaCy model not found"

**Problem**: Language model not downloaded

**Solutions**:
1. Download manually:
   ```bash
   python -m spacy download en_core_web_sm
   ```
2. If still fails, try:
   ```bash
   python -m spacy download en_core_web_sm --user-local
   ```

### ❌ "Port 8501 already in use"

**Problem**: Another app is using the port

**Solutions**:
1. Close other Streamlit apps
2. Wait 30 seconds and try again
3. Use a different port:
   ```bash
   streamlit run app.py --server.port 8502
   ```

### ❌ "Out of Memory" Error

**Problem**: System running out of RAM

**Solutions**:
1. Close other applications
2. Restart the computer
3. Use a machine with more RAM

### ❌ Very Slow Performance

**Problem**: First run takes a long time

**This is normal** - first run downloads and initializes models.

**Solutions**:
1. Wait for completion (5-15 minutes)
2. Subsequent runs will be much faster
3. Ensure good internet connection

### ❌ Model Download Fails

**Problem**: Internet connection issues

**Solutions**:
1. Check your internet connection
2. Try again later
3. Use a VPN if you're behind a proxy
4. Download models manually on a machine with good connection

## 📊 Verifying Installation

To verify everything works, run:

```bash
python -c "import streamlit; import transformers; import spacy; import nltk; print('✅ All modules installed successfully!')"
```

Expected output:
```
✅ All modules installed successfully!
```

## 🆘 Getting Help

If you encounter issues:

1. **Check System Requirements**: Ensure Python 3.8+
2. **Reinstall Dependencies**: `pip install --upgrade -r requirements.txt`
3. **Clear Cache**: Delete `.streamlit` and `__pycache__` folders
4. **Restart**: Close terminal, restart computer, try again
5. **Check Logs**: Look at error messages carefully

## 📱 Running on Different Systems

### Windows Specifics

- Use `python` or `python3` interchangeably
- Batch file (`run.bat`) works with Command Prompt and PowerShell
- Virtual environment path: `.\.venv\Scripts\activate.bat` (cmd) or `.\.venv\Scripts\Activate.ps1` (PowerShell)

### macOS Specifics

- Use `python3` (not `python`)
- Install Xcode Command Line Tools if needed: `xcode-select --install`
- Virtual environment: `source .venv/bin/activate`

### Linux Specifics

- Most distributions have Python installed
- Use package manager: `apt install python3-pip` (Ubuntu/Debian)
- Virtual environment: `source .venv/bin/activate`

## 💾 Storage Requirements

Approximate disk space needed:

| Component | Size |
|-----------|------|
| Python Packages | ~800 MB |
| spaCy Model | ~40 MB |
| PyTorch | ~500 MB |
| Transformers | ~400 MB |
| **Total** | **~2 GB** |

## 🔐 Security Notes

- The app runs locally - no data is sent to external servers
- No API keys or authentication required
- All processing happens on your machine
- Safe to use with sensitive information

## 🚀 Next Steps

After installation:

1. **Read the README.md** - Learn about features
2. **Try Examples** - Use "Load Example" button in app
3. **Experiment** - Try different styles
4. **Explore Advanced Usage** - See README.md for Python API
5. **Customize** - Modify styles in `prompt_enhancer.py`

## ✅ You're Ready!

Once installation is complete and the app starts successfully, you're all set to enhance your prompts!

---

**Questions?** Check the FAQ in README.md or revisit this troubleshooting guide.

Happy prompt enhancing! 🎉
