# 🚀 Quick Reference Guide

A quick cheat sheet for using the AI Prompt Enhancer.

## ⚡ Quick Start (30 seconds)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download spaCy model
python -m spacy download en_core_web_sm

# 3. Run the app
streamlit run app.py

# 4. Open browser
# Visit: http://localhost:8501
```

## 🎯 Using the Web App

### Basic Workflow
1. **Paste your prompt** in the input box
2. **Choose a style** from the sidebar (Professional/Creative/Detailed/Simplified)
3. **Toggle Context Boost** if you want more details
4. **Click "Enhance My Prompt"**
5. **Copy or download** the enhanced version

### Output Sections

| Section | What It Shows |
|---------|---------------|
| **Original vs Enhanced** | Side-by-side comparison |
| **Metadata** | Word counts and style used |
| **Keywords** | Important concepts extracted |
| **Synonyms** | Alternative word choices |

## 💻 Using as Python Module

### Basic Enhancement

```python
from prompt_enhancer import enhance_prompt

result = enhance_prompt(
    prompt="Make a website for students",
    style="creative",
    context_boost=True
)

print(result['enhanced_prompt'])
print(result['keywords'])
print(result['synonyms'])
```

### Batch Processing

```python
from prompt_enhancer import enhance_prompt

prompts = [
    "Build a mobile app",
    "Create a website",
    "Design a dashboard"
]

for prompt in prompts:
    result = enhance_prompt(prompt, style='professional')
    print(f"Enhanced: {result['enhanced_prompt']}\n")
```

### Result Dictionary

```python
{
    'enhanced_prompt': str,      # The enhanced text
    'keywords': list,             # Extracted keywords
    'synonyms': dict,             # {word: [alternatives]}
    'style': str,                 # Applied style
    'context_boost_applied': bool,# Was boost used?
    'original_length': int,       # Word count original
    'enhanced_length': int        # Word count enhanced
}
```

## 🎨 Enhancement Styles

### Professional
- **Use for**: Business, technical, official documents
- **Tone**: Clear, structured, formal
- **Example**: "Develop a comprehensive REST API with proper documentation"

### Creative
- **Use for**: Art, design, social media, entertainment
- **Tone**: Engaging, imaginative, innovative
- **Example**: "Craft an innovative mobile app with stunning visuals"

### Detailed
- **Use for**: Requirements, specifications, research
- **Tone**: Thorough, comprehensive, complete
- **Example**: "Create a detailed specification with all features documented"

### Simplified
- **Use for**: Basic explanations, user-friendly content, beginners
- **Tone**: Simple, clear, easy-to-understand
- **Example**: "Build a simple app that's easy to use"

## 🔑 Common Use Cases

### 1. ChatGPT/Claude Prompts
```
Original: "Write code for web scraping"
Enhanced: "Write clean, well-documented Python code for web scraping with proper error handling, rate limiting, and respect for robots.txt"
```

### 2. Job Descriptions
```
Original: "Need a developer for a project"
Enhanced: "Seeking an experienced full-stack developer with expertise in modern web frameworks, cloud deployment, and collaborative development practices"
```

### 3. Research Questions
```
Original: "How does AI work?"
Enhanced: "How do modern deep learning architectures, particularly transformer models, process sequential data and generate contextually relevant responses?"
```

### 4. Project Requirements
```
Original: "Build a dashboard"
Enhanced: "Develop a comprehensive analytics dashboard with real-time data visualization, user authentication, responsive design, and export capabilities"
```

## 🛠️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Stop the app |
| `Ctrl+Enter` | Submit (if in input box) |
| `Ctrl+L` | Clear all in many terminals |
| `F5` (browser) | Refresh the app |

## 📊 File Reference

| File | Purpose |
|------|---------|
| `app.py` | Web interface (Streamlit) |
| `prompt_enhancer.py` | Core enhancement logic |
| `requirements.txt` | Python dependencies |
| `run.bat` | Windows quick start |
| `quickstart.py` | Cross-platform startup |
| `README.md` | Full documentation |
| `INSTALLATION.md` | Setup guide |

## 🐛 Quick Fixes

**App won't start?**
```bash
# Clear cache and restart
rm -r __pycache__ .streamlit
streamlit run app.py
```

**Models not downloaded?**
```bash
# Download spaCy model
python -m spacy download en_core_web_sm

# Download NLTK data
python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"
```

**Port already in use?**
```bash
# Use different port
streamlit run app.py --server.port 8502
```

**Out of memory?**
```bash
# Restart and close other apps first
# Then run the app again
```

## 📈 Performance Tips

1. **First Run**: Takes longer (models download) - be patient
2. **Subsequent Runs**: Much faster after first run
3. **Longer Prompts**: May take 2-5 seconds
4. **Multiple Enhancements**: Sequential processing

## 🎓 Learning Resources

- **Inside the App**: Check "📚 Examples" tab for use cases
- **README.md**: Full feature documentation
- **INSTALLATION.md**: Detailed setup instructions
- **Python API**: See advanced usage in README.md

## 🚨 Important Notes

- **No Internet Needed** after setup (except initial model download)
- **No API Keys** required - fully local
- **Data Privacy** - everything runs on your machine
- **Open Source** - free to use and modify

## 📞 Troubleshooting Flowchart

```
App won't start?
├─ Check Python version: python --version
├─ Install requirements: pip install -r requirements.txt
├─ Check port: streamlit run app.py --server.port 8502
└─ Restart computer

Enhancement is slow?
├─ First run? Yes = Wait (5-15 min)
├─ Low RAM? Close other apps
└─ Internet slow? Download models again

Error on enhancement?
├─ Try shorter prompt
├─ Check keywords section
└─ Restart the app
```

## 💡 Pro Tips

1. **Iterate**: Use enhanced prompt as input for another enhancement
2. **Compare Styles**: Try same prompt in all 4 styles
3. **Mix & Match**: Copy parts from different enhanced versions
4. **Context Boost**: Use when you need comprehensive specifications
5. **Keywords**: Use extracted keywords for SEO/tagging
6. **Batch Process**: Enhance multiple prompts in sequence

---

**Need more help?** See README.md or INSTALLATION.md

**Ready to enhance?** Run `streamlit run app.py` 🚀
