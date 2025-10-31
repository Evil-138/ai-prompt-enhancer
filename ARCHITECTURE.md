# 🎨 Visual Guide & Architecture

## 📊 Application Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  AI PROMPT ENHANCER                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  WEB INTERFACE (Streamlit - app.py)                  │  │
│  │  ├─ Input Section                                    │  │
│  │  ├─ Style Selection (Professional/Creative/etc)    │  │
│  │  ├─ Context Boost Toggle                           │  │
│  │  ├─ Results Display                                │  │
│  │  ├─ Download & Copy Features                       │  │
│  │  └─ Examples & Help Tabs                           │  │
│  └──────────────────────────────────────────────────────┘  │
│                           ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  CORE ENGINE (prompt_enhancer.py)                   │  │
│  ├─────────────────────────────────────────────────────┤  │
│  │ PromptEnhancer Class                                │  │
│  │ ├─ extract_keywords()     → Keywords               │  │
│  │ ├─ get_synonyms()         → Alternatives           │  │
│  │ ├─ expand_vague_sentences()→ Elaboration           │  │
│  │ ├─ apply_style()          → Style Transform        │  │
│  │ ├─ add_context_boost()    → Context Details        │  │
│  │ └─ enhance_prompt()       → Main Function          │  │
│  └──────────────────────────────────────────────────────┘  │
│                           ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  NLP PROCESSING LAYER                               │  │
│  ├─────────────────────────────────────────────────────┤  │
│  │ spaCy          NLTK          WordNet                │  │
│  │ ├─ NER         ├─ Tokenize   ├─ Synonyms          │  │
│  │ ├─ POS Tag     ├─ POS Tag    ├─ Lemmatization     │  │
│  │ ├─ Noun Chunks ├─ Stopwords  └─ Semantic Links    │  │
│  │ └─ Parsing     └─ Stemming                         │  │
│  └──────────────────────────────────────────────────────┘  │
│                           ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  DEPENDENCIES                                        │  │
│  │  (Loaded from requirements.txt)                     │  │
│  │  ├─ transformers ├─ torch   ├─ spacy               │  │
│  │  ├─ nltk         ├─ numpy   └─ streamlit           │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow Diagram

```
USER INPUT
    ↓
┌───────────────────────────────────┐
│  1. ANALYZE                       │
│  ├─ Extract Keywords              │
│  ├─ Identify Entities             │
│  └─ Parse Sentence Structure      │
└───────────┬───────────────────────┘
            ↓
┌───────────────────────────────────┐
│  2. EXPAND                        │
│  ├─ Elaborate Short Sentences     │
│  ├─ Add Context                   │
│  └─ Suggest Alternatives          │
└───────────┬───────────────────────┘
            ↓
┌───────────────────────────────────┐
│  3. TRANSFORM                     │
│  ├─ Apply Style Template          │
│  ├─ Adjust Tone                   │
│  └─ Restructure Text              │
└───────────┬───────────────────────┘
            ↓
┌───────────────────────────────────┐
│  4. ENHANCE (Optional)            │
│  ├─ Add Context Boost             │
│  ├─ Include Examples              │
│  └─ Add Specifications            │
└───────────┬───────────────────────┘
            ↓
OUTPUT RESULTS
├─ Enhanced Prompt
├─ Keywords
├─ Synonyms
└─ Metadata
```

## 🎨 UI Layout

```
╔════════════════════════════════════════════════════════════════╗
║  ✨ AI PROMPT ENHANCER                                         ║
║  Enhance your prompts intelligently to get better AI responses ║
╚════════════════════════════════════════════════════════════════╝

┌─ SIDEBAR ──────────────────────────────────────────────────────┐
│ ⚙️ Settings & Options                                          │
│                                                                 │
│ 🎯 Enhancement Style                                           │
│ ⊙ Professional - Clear, structured, business-focused         │
│ ○ Creative - Innovative, engaging, imaginative                │
│ ○ Detailed - Comprehensive, thorough, well-specified         │
│ ○ Simplified - Easy to understand, straightforward            │
│                                                                 │
│ 📚 Add Context Boost [☐]                                       │
│                                                                 │
│ 📖 How It Works                                               │
│ ├─ Enter your prompt                                          │
│ ├─ Select an enhancement style                                │
│ ├─ Toggle context boost                                       │
│ └─ Get enhanced prompt with keywords                          │
└─────────────────────────────────────────────────────────────────┘

MAIN AREA:

[🚀 Enhancer | 📚 Examples | ℹ️ About] ← Tabs

┌─ ENHANCER TAB ─────────────────────────────────────────────────┐
│                                                                 │
│ 📝 Enter Your Prompt                                           │
│ ┌──────────────────────────────────────────────────────────┐  │
│ │ Enter your prompt here...                                │  │
│ │                                                          │  │
│ │                                                          │  │
│ └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│ 📊 Word Count: 12  |  📄 Characters: 85  |  📌 Sentences: 2  │
│                                                                 │
│ ┌─────────────── [✨ Enhance My Prompt] ────────────────────┐ │
│                                                                 │
│ ─── RESULTS ─────────────────────────────────────────────────  │
│                                                                 │
│ Original Prompt:             Enhanced Prompt:                 │
│ ┌──────────────────────┐     ┌──────────────────────────┐     │
│ │ Make a website that  │     │ Create a modern,         │     │
│ │ looks cool for data  │     │ visually appealing       │     │
│ │ science students.    │     │ website with a dark      │     │
│ └──────────────────────┘     │ neon theme that...       │     │
│                               └──────────────────────────┘     │
│                                                                 │
│ 📊 Metrics:                                                    │
│ • Original Length: 10 words    • Enhanced Length: 24 words    │
│ • Added: +14 words              • Style: CREATIVE              │
│                                                                 │
│ 🔑 Extracted Keywords:                                        │
│ [website] [data science] [students] [modern] [design]         │
│                                                                 │
│ 🔄 Suggested Synonyms:                                        │
│ ▼ website → 3 alternatives     ▼ design → 5 alternatives     │
│                                                                 │
│ ─────────────────────────────────────────────────────────────  │
│ [📋 Copy] [🔄 New] [📥 Download] ← Action Buttons             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 🔌 Function Signatures

```python
# Main public API
enhance_prompt(
    prompt: str,              # User's prompt to enhance
    style: str = 'professional',  # Style: 'professional', 'creative', 'detailed', 'simplified'
    context_boost: bool = False   # Add context specifications
) -> dict:
    """
    Returns:
    {
        'enhanced_prompt': str,           # The enhanced text
        'keywords': List[str],             # Extracted keywords
        'synonyms': Dict[str, List[str]],  # {word: [alternatives]}
        'style': str,                      # Applied style
        'context_boost_applied': bool,     # Was boost used?
        'original_length': int,            # Original word count
        'enhanced_length': int             # Enhanced word count
    }
    """
```

## 🎯 Style Template Structure

```python
style_templates = {
    'professional': {
        'prefixes': ['Create', 'Develop', 'Implement', ...],
        'additions': [' with clear specifications', ...],
        'tone_words': ['professional', 'structured', ...]
    },
    'creative': {
        'prefixes': ['Imagine', 'Create', 'Design', ...],
        'additions': [' with innovative features', ...],
        'tone_words': ['innovative', 'visually appealing', ...]
    },
    # ... etc for detailed and simplified
}
```

## 📈 Enhancement Process Flowchart

```
START
  ↓
[Input Prompt]
  ↓
┌─────────────────────────┐
│ Validate Input          │ → If empty, show error
└──────────┬──────────────┘
           ↓
┌─────────────────────────┐
│ Extract Keywords        │ ← spaCy NER, NLTK
├─ Named Entities        │
├─ Important Nouns       │
└──────────┬──────────────┘
           ↓
┌─────────────────────────┐
│ Get Synonyms            │ ← WordNet lookup
├─ For top 5 keywords   │
└──────────┬──────────────┘
           ↓
┌─────────────────────────┐
│ Expand Sentences        │ ← Add detail & context
├─ Detect short sentences│
├─ Add elaboration      │
└──────────┬──────────────┘
           ↓
┌─────────────────────────┐
│ Apply Style             │
├─ Change prefixes      │
├─ Add tone words       │
└──────────┬──────────────┘
           ↓
        Is Context Boost
        Enabled?
        ├─ YES → [Add specifications & examples]
        └─ NO  → [Skip enhancement]
           ↓
┌─────────────────────────┐
│ Generate Output         │
├─ Enhanced prompt       │
├─ Keywords list         │
├─ Synonyms dict         │
└──────────┬──────────────┘
           ↓
[Return Results Dictionary]
  ↓
END
```

## 🎛️ File Dependencies

```
app.py
├─ streamlit          (for UI)
├─ prompt_enhancer.py (core logic)
│  ├─ nltk
│  ├─ spacy
│  ├─ transformers
│  └─ re, warnings
└─ time (Python stdlib)

prompt_enhancer.py
├─ nltk              (NLP toolkit)
├─ spacy             (NER, parsing)
├─ transformers      (models)
├─ re               (regex)
└─ warnings         (suppress messages)
```

## 💾 Memory Usage

```
Approximate startup memory:
├─ Python base           ~50 MB
├─ spaCy model          ~40 MB
├─ NLTK data            ~100 MB
├─ PyTorch             ~300 MB
├─ Transformers        ~200 MB
└─ Streamlit app       ~100 MB
───────────────────────────────
Total                  ~800 MB

After optimization: ~500 MB
```

## ⏱️ Performance Metrics

```
First Run (includes downloads):
├─ Model download       5-10 minutes
├─ Dependency load      2-3 minutes
└─ App startup         ~30 seconds
    Total: 7-13 minutes

Subsequent Runs:
├─ App startup         ~2-3 seconds
├─ Enhancement        ~1-3 seconds
└─ UI rendering       ~0.5 seconds
    Total: 3-6 seconds

Enhancement Times:
├─ Short prompt (< 50 words)    ~0.5 seconds
├─ Medium prompt (50-200 words) ~1-2 seconds
└─ Long prompt (> 200 words)    ~2-3 seconds
```

---

**Visual architecture helps developers understand the system structure and data flow!**
