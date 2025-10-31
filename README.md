# ✨ AI Prompt Enhancer

A free, open-source Python application that intelligently enhances and improves text prompts using advanced NLP techniques. Perfect for crafting better prompts for AI models like ChatGPT, Claude, and other language models.

## 🎯 Features

- ✅ **Completely Free** - No API keys, no paid services required
- ✅ **Works Offline** - All processing happens locally on your machine
- ✅ **Multiple Styles** - Professional, Creative, Detailed, and Simplified
- ✅ **Smart Enhancement** - Not just grammar, but structure and clarity improvement
- ✅ **Keyword Extraction** - Automatically identifies key concepts
- ✅ **Synonym Suggestions** - Provides alternative word choices
- ✅ **Context Boost** - Adds examples, specifications, and audience details
- ✅ **Beautiful UI** - Streamlit-based web interface
- ✅ **Download Results** - Export enhancements as text files
- ✅ **No Setup Required** - Simple one-command installation

## 🚀 Quick Start

### Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download spaCy model** (one-time setup):
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 💡 How to Use

1. **Enter Your Prompt** - Type or paste your prompt in the input box
2. **Select a Style**:
   - 📘 **Professional** - For business and technical contexts
   - 🎨 **Creative** - For artistic and imaginative projects
   - 📊 **Detailed** - For comprehensive specifications
   - 📝 **Simplified** - For straightforward, easy-to-read text
3. **Optional: Enable Context Boost** - Adds examples and specifications
4. **Click "Enhance My Prompt"** - Watch the magic happen
5. **Review Results** - See your enhanced prompt, keywords, and synonyms
6. **Copy or Download** - Use the enhanced prompt or download the report

## 🧠 How It Works

The enhancement process uses multiple NLP techniques:

### 1. **Keyword Extraction**
- Uses spaCy Named Entity Recognition (NER)
- Identifies nouns and important concepts
- Extracts multi-word phrases and domain terms

### 2. **Synonym Suggestion**
- Leverages WordNet for semantic alternatives
- Suggests up to 5 alternatives per keyword
- Helps diversify vocabulary

### 3. **Sentence Expansion**
- Detects short or vague sentences
- Adds context and elaboration
- Maintains original meaning while improving clarity

### 4. **Style Application**
- Transforms text tone based on selected style
- Applies style-specific vocabulary
- Restructures sentences for better impact

### 5. **Context Boost**
- Adds target audience information
- Includes best practices and standards
- Provides examples and use cases

## 📚 Example Use Cases

### Example 1: Website Design
**Original:**
```
Make a website that looks cool for data science students.
```

**Enhanced (Creative + Context Boost):**
```
Create a modern, visually appealing website with a dark neon theme that highlights data science projects and includes interactive charts and animations suitable for student portfolios.
```

---

### Example 2: API Documentation
**Original:**
```
Build an API for user management.
```

**Enhanced (Professional):**
```
Develop a comprehensive REST API for user management that implements role-based access control, authentication, data validation, and comprehensive error handling, with detailed documentation and example usage patterns, ensuring quality and efficiency.
```

---

### Example 3: Learning App
**Original:**
```
Make an app for learning Python.
```

**Enhanced (Detailed):**
```
Create an intuitive, interactive learning application for Python programming that includes interactive code editors, visual feedback mechanisms, progressive difficulty levels, real-time error detection, and community-driven learning modules designed for beginners. Ensure comprehensive coverage of all aspects and components.
```

---

### Example 4: Mobile App
**Original:**
```
Build a todo app with many features.
```

**Enhanced (Simplified):**
```
Build a straightforward task management application with easy-to-use features for tracking daily activities, simple organization, and quick task completion.
```

## 🛠️ Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web interface and UI framework |
| **spaCy** | Named entity recognition and NLP |
| **NLTK** | Natural language processing toolkit |
| **Transformers** | Advanced NLP models (Hugging Face) |
| **WordNet** | Synonym and semantic relationships |
| **Torch** | Deep learning backend |
| **Python 3.8+** | Core programming language |

## 📦 Project Structure

```
ai-prompt-optimiser/
├── app.py                    # Main Streamlit application
├── prompt_enhancer.py        # Core enhancement logic
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── LICENSE                   # License information
```

## 🔧 Configuration & Customization

### Modify Style Templates
Edit the `style_templates` in `prompt_enhancer.py`:

```python
self.style_templates = {
    'professional': {
        'prefixes': ['Create', 'Develop', 'Implement', ...],
        'additions': [' with clear specifications', ...],
        'tone_words': ['professional', 'structured', ...]
    },
    # ... more styles
}
```

### Adjust Enhancement Levels
Modify the `PromptEnhancer` class methods for different enhancement intensities:
- `extract_keywords()` - Change `[:10]` to limit keyword count
- `_refine_for_style()` - Add custom refinements

## 📝 Tips for Best Results

1. **Be Specific** - More details in your original prompt lead to better enhancements
2. **Choose the Right Style** - Match the style to your use case (professional for work, creative for art, etc.)
3. **Use Context Boost Wisely** - Enable it when you need comprehensive prompts with extra details
4. **Review Keywords** - Check if extracted keywords match your intent
5. **Experiment** - Try different styles for the same prompt to find the best version
6. **Iterate** - Use the enhanced prompt as input for another round of enhancement

## 💻 System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: ~2GB for models and dependencies
- **Internet**: Required only for first installation

## 🐛 Troubleshooting

### Issue: "Module not found" error
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: spaCy model not found
**Solution**: Download the model manually:
```bash
python -m spacy download en_core_web_sm
```

### Issue: Slow performance on first run
**Solution**: This is normal - models are being downloaded and initialized. Subsequent runs will be faster.

### Issue: Out of memory error
**Solution**: 
- Close other applications
- Restart the app
- Consider upgrading your system RAM

## 🚀 Advanced Usage

### Use as Python Module
```python
from prompt_enhancer import enhance_prompt

# Enhance a prompt
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
prompts = [
    "Make a website",
    "Build an app",
    "Create a tool"
]

for prompt in prompts:
    result = enhance_prompt(prompt, style='professional')
    print(f"Original: {prompt}")
    print(f"Enhanced: {result['enhanced_prompt']}\n")
```

## 🤝 Contributing

Contributions are welcome! Here are some ways to improve the project:

1. **Add new enhancement styles** - Propose new style templates
2. **Improve keyword extraction** - Enhance the NLP logic
3. **Expand synonym database** - Add more semantic relationships
4. **Optimize performance** - Make it faster or more efficient
5. **Report bugs** - Help identify and fix issues
6. **Suggest features** - Request new functionality

## 📄 License

This project is open-source and free to use. See LICENSE file for details.

## 🌟 Use Cases

- ✨ Creating better prompts for ChatGPT, Claude, or other AI models
- 📖 Improving technical documentation
- 💼 Crafting professional job descriptions
- 🎨 Writing creative briefs and artistic prompts
- 🔬 Refining research questions and hypotheses
- 📋 Enhancing project requirements and specifications
- ✍️ Improving content briefs and marketing copy
- 🎓 Tutoring and educational content creation
- 💬 Preparing questions for interviews
- 🎯 Marketing and copywriting

## 🔮 Future Roadmap

- [ ] Support for multiple languages
- [ ] Advanced style customization UI
- [ ] Batch processing mode
- [ ] API for integration with other tools
- [ ] Real-time collaboration features
- [ ] History and favorites management
- [ ] Export to multiple formats (PDF, Word, etc.)
- [ ] Fine-tuned models for specific domains
- [ ] A/B testing for enhanced vs original prompts
- [ ] Community-contributed prompts library

## ❓ FAQ

**Q: Do I need internet to use this app?**
A: No! Everything runs locally after the initial installation.

**Q: Can I modify the enhancement styles?**
A: Yes! Edit the `style_templates` in `prompt_enhancer.py`.

**Q: How long does enhancement take?**
A: Usually 1-5 seconds depending on prompt length.

**Q: Can I use this for commercial purposes?**
A: Yes! The app is free and open-source.

**Q: Will it work on my machine?**
A: If it has Python 3.8+ and 4GB+ RAM, yes!

**Q: Can I contribute improvements?**
A: Absolutely! We welcome contributions.

## 📞 Support

For issues, questions, or suggestions:
1. Check the troubleshooting section above
2. Review the example use cases
3. Ensure all dependencies are properly installed

## 🙏 Acknowledgments

- **spaCy** - For powerful NLP capabilities
- **NLTK** - For comprehensive linguistic tools
- **Hugging Face** - For Transformers library
- **Streamlit** - For beautiful and easy web interfaces
- **WordNet** - For synonym and semantic relationships

---

**Made with ❤️ for better AI interactions**

**Version**: 1.0  
**Last Updated**: October 2025

Happy prompting! 🚀
