"""
AI Prompt Enhancer - Streamlit Web Application
A user-friendly interface for enhancing and improving text prompts.
"""

import streamlit as st
import time
from prompt_enhancer import enhance_prompt

# Page configuration
st.set_page_config(
    page_title="AI Prompt Enhancer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.1rem;
            font-weight: 600;
        }
        .header-title {
            color: #6366f1;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .subheader-text {
            color: #64748b;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }
        .result-box {
            background: linear-gradient(135deg, #f0f4ff 0%, #f9fafb 100%);
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #6366f1;
            margin: 1rem 0;
        }
        .info-box {
            background: #e0f2fe;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #0284c7;
            margin: 1rem 0;
            color: #075985;
        }
        .success-box {
            background: #dcfce7;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #16a34a;
            margin: 1rem 0;
            color: #166534;
        }
        .metric-card {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown('<div class="header-title">✨ AI Prompt Enhancer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheader-text">Enhance your prompts intelligently to get better AI responses</div>',
    unsafe_allow_html=True
)

# Sidebar - Settings
st.sidebar.markdown("### ⚙️ Settings & Options")
st.sidebar.divider()

# Style selection
style_description = {
    'professional': 'Clear, structured, and business-focused',
    'creative': 'Innovative, engaging, and imaginative',
    'detailed': 'Comprehensive, thorough, and well-specified',
    'simplified': 'Easy to understand, straightforward, and minimal'
}

selected_style = st.sidebar.radio(
    "🎯 **Enhancement Style**",
    options=['professional', 'creative', 'detailed', 'simplified'],
    format_func=lambda x: f"{x.capitalize()} - {style_description[x]}",
    help="Choose the tone and approach for enhancing your prompt"
)

# Context Boost toggle
st.sidebar.divider()
context_boost = st.sidebar.checkbox(
    "📚 **Add Context Boost**",
    value=False,
    help="Adds examples, specifications, and target audience details"
)

# Info box in sidebar
with st.sidebar:
    st.divider()
    st.markdown("### 📖 How It Works")
    st.info(
        """
        1. **Enter** your prompt in the text area
        2. **Select** an enhancement style
        3. **Toggle** context boost for more details
        4. **Get** your enhanced prompt with keywords and synonyms
        
        The app analyzes your prompt and improves:
        - Clarity and structure
        - Detail and specificity
        - Tone and style
        - Professional impact
        """
    )

# Main content area
st.divider()

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["🚀 Enhancer", "📚 Examples", "ℹ️ About"])

with tab1:
    # Input section
    st.markdown("### 📝 Enter Your Prompt")
    
    # Example prompts
    example_prompts = [
        "Make a website that looks cool for data science students.",
        "Build an app to track fitness goals",
        "Write better code for my project",
        "Create a learning resource for beginners"
    ]
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("💡 Load Example", use_container_width=True):
            st.session_state.example_loaded = True
    
    if 'example_loaded' in st.session_state and st.session_state.example_loaded:
        default_text = example_prompts[0]
        st.session_state.example_loaded = False
    else:
        default_text = ""
    
    # Input text area
    user_prompt = st.text_area(
        label="Input Prompt",
        placeholder="Enter your prompt here... (e.g., 'Build a responsive website for a tech startup')",
        height=120,
        value=default_text,
        label_visibility="collapsed"
    )
    
    # Input statistics
    if user_prompt:
        col1, col2, col3 = st.columns(3)
        with col1:
            word_count = len(user_prompt.split())
            st.metric("📊 Word Count", word_count)
        with col2:
            char_count = len(user_prompt)
            st.metric("📄 Character Count", char_count)
        with col3:
            sent_count = len([s for s in user_prompt.split('.') if s.strip()])
            st.metric("📌 Sentences", sent_count)
    
    st.divider()
    
    # Enhancement button
    if st.button("✨ Enhance My Prompt", type="primary", use_container_width=True):
        if not user_prompt or not user_prompt.strip():
            st.error("❌ Please enter a prompt to enhance")
        else:
            with st.spinner("🔄 Enhancing your prompt..."):
                try:
                    # Enhance the prompt
                    result = enhance_prompt(
                        prompt=user_prompt,
                        style=selected_style,
                        context_boost=context_boost
                    )
                    
                    # Store result in session state
                    st.session_state.enhancement_result = result
                    st.session_state.show_result = True
                    
                except Exception as e:
                    st.error(f"❌ Error during enhancement: {str(e)}")
    
    # Display results
    if 'show_result' in st.session_state and st.session_state.show_result:
        result = st.session_state.enhancement_result
        
        st.divider()
        st.markdown("### 🎯 Enhancement Results")
        
        # Original vs Enhanced comparison
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Original Prompt:**")
            st.info(user_prompt)
        
        with col2:
            st.markdown("**Enhanced Prompt:**")
            st.success(result['enhanced_prompt'])
        
        st.divider()
        
        # Metadata section
        st.markdown("### 📊 Analysis & Metadata")
        
        # Metrics
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        
        with metric_col1:
            st.metric("📈 Original Length", f"{result['original_length']} words")
        with metric_col2:
            st.metric("📊 Enhanced Length", f"{result['enhanced_length']} words")
        with metric_col3:
            improvement = result['enhanced_length'] - result['original_length']
            st.metric("✨ Added", f"{improvement} words")
        with metric_col4:
            st.metric("🎯 Style Applied", result['style'].capitalize())
        
        st.divider()
        
        # Keywords and Synonyms
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔑 Extracted Keywords")
            if result['keywords']:
                # Display keywords with styling
                keywords_html = " ".join([
                    f'<span style="background-color: #e0e7ff; color: #3730a3; padding: 0.25rem 0.5rem; border-radius: 4px; margin-right: 0.5rem;">{kw}</span>'
                    for kw in result['keywords']
                ])
                st.markdown(keywords_html, unsafe_allow_html=True)
            else:
                st.info("No keywords extracted")
        
        with col2:
            st.markdown("#### 🔄 Suggested Synonyms")
            if result['synonyms']:
                for word, syns in result['synonyms'].items():
                    with st.expander(f"**{word}** → {len(syns)} alternatives"):
                        st.write(", ".join(syns))
            else:
                st.info("No synonyms available")
        
        st.divider()
        
        # Copy to clipboard button
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Copy Enhanced Prompt", use_container_width=True):
                st.success("✅ Copied to clipboard! (You can paste it now)")
        
        with col2:
            if st.button("🔄 New Enhancement", use_container_width=True):
                st.session_state.show_result = False
                st.rerun()
        
        with col3:
            if st.button("📥 Download Results", use_container_width=True):
                download_text = f"""
PROMPT ENHANCEMENT REPORT
=========================

Original Prompt:
{user_prompt}

Enhanced Prompt:
{result['enhanced_prompt']}

Metadata:
--------
Style: {result['style'].upper()}
Context Boost: {'Yes' if result['context_boost_applied'] else 'No'}
Original Length: {result['original_length']} words
Enhanced Length: {result['enhanced_length']} words

Keywords:
{', '.join(result['keywords'])}

Synonyms:
"""
                for word, syns in result['synonyms'].items():
                    download_text += f"\n{word}: {', '.join(syns)}"
                
                st.download_button(
                    label="📄 Download Report",
                    data=download_text,
                    file_name="prompt_enhancement_report.txt",
                    mime="text/plain",
                    use_container_width=True
                )

with tab2:
    st.markdown("### 📚 Examples & Use Cases")
    
    examples = [
        {
            'title': 'Website Design',
            'original': 'Make a website that looks cool for data science students.',
            'enhanced': 'Create a modern, visually appealing website with a dark neon theme that highlights data science projects and includes interactive charts and animations suitable for student portfolios.',
            'style': 'Creative'
        },
        {
            'title': 'API Documentation',
            'original': 'Build an API for user management.',
            'enhanced': 'Develop a comprehensive REST API for user management that implements role-based access control, authentication, data validation, and comprehensive error handling, with detailed documentation and example usage patterns.',
            'style': 'Professional'
        },
        {
            'title': 'Learning App',
            'original': 'Make an app for learning Python.',
            'enhanced': 'Create an intuitive, interactive learning application for Python programming that includes interactive code editors, visual feedback mechanisms, progressive difficulty levels, real-time error detection, and community-driven learning modules designed for beginners.',
            'style': 'Detailed'
        },
        {
            'title': 'Mobile App',
            'original': 'Build a todo app with many features.',
            'enhanced': 'Build a straightforward task management application with easy-to-use features for tracking daily activities, simple organization, and quick task completion without unnecessary complexity.',
            'style': 'Simplified'
        }
    ]
    
    for i, example in enumerate(examples, 1):
        with st.expander(f"**Example {i}: {example['title']}** ({example['style']})"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Original:**")
                st.info(example['original'])
            
            with col2:
                st.markdown("**Enhanced:**")
                st.success(example['enhanced'])

with tab3:
    st.markdown("### ℹ️ About This Application")
    
    st.markdown("""
    ## 🎯 Purpose
    
    The **AI Prompt Enhancer** helps you craft better prompts for AI models by:
    - Improving clarity and structure
    - Adding relevant details and specifications
    - Adjusting tone to match your needs
    - Suggesting related terms and synonyms
    
    ## 🔧 How It Works
    
    The app uses advanced NLP techniques:
    
    1. **Keyword Extraction** - Identifies key concepts using spaCy NER and NLTK
    2. **Synonym Generation** - Suggests alternatives using WordNet
    3. **Sentence Expansion** - Elaborates vague or simple sentences
    4. **Style Application** - Transforms text to match selected tone
    5. **Context Boost** - Adds examples, specifications, and audience details
    
    ## 💡 Enhancement Styles
    
    - **Professional**: Clear, structured, business-focused language
    - **Creative**: Innovative, engaging, and imaginative tone
    - **Detailed**: Comprehensive, thorough specifications
    - **Simplified**: Straightforward, easy-to-understand format
    
    ## 🛠️ Technologies Used
    
    - **Streamlit** - Web interface
    - **spaCy** - Named entity recognition and NLP
    - **NLTK** - Natural language processing
    - **Transformers** - Advanced NLP models
    - **Python** - Core programming language
    
    ## ⚡ Features
    
    ✅ Free and open-source  
    ✅ Works offline (no API keys needed)  
    ✅ Multiple enhancement styles  
    ✅ Real-time keyword extraction  
    ✅ Synonym suggestions  
    ✅ Context boost option  
    ✅ Download results as text  
    ✅ Copy to clipboard functionality  
    
    ## 📝 Tips for Best Results
    
    1. **Be Specific** - More details in your original prompt lead to better enhancements
    2. **Choose the Right Style** - Match the style to your use case
    3. **Use Context Boost** - Enable it when you need more comprehensive prompts
    4. **Review Keywords** - Check if the extracted keywords match your intent
    5. **Experiment** - Try different styles for the same prompt
    
    ## 🤝 Use Cases
    
    - Creating better prompts for ChatGPT, Claude, or other AI models
    - Improving technical documentation
    - Crafting job descriptions
    - Writing creative briefs
    - Refining research questions
    - Enhancing project requirements
    - Improving content briefs
    
    ---
    
    **Version**: 1.0  
    **Last Updated**: October 2025  
    **Made with ❤️ for better AI interactions**
    """)

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center; color: #64748b; font-size: 0.9rem;'>"
    "✨ AI Prompt Enhancer | Free & Open Source | Made with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
