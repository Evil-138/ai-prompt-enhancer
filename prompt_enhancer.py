"""
Prompt Enhancement Module - Lightweight Pure-Python Version
No sklearn dependencies, works with basic Python + optional spaCy/NLTK
"""

import re
import warnings

warnings.filterwarnings("ignore")

# Optional imports - graceful fallback if not available
NLTK_AVAILABLE = False
SPACY_AVAILABLE = False
nlp = None

try:
    import nltk
    from nltk.corpus import wordnet, stopwords
    from nltk.tokenize import sent_tokenize, word_tokenize
    NLTK_AVAILABLE = True
    
    # Download resources silently
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
        
except (ImportError, Exception):
    NLTK_AVAILABLE = False

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    SPACY_AVAILABLE = True
except (ImportError, Exception):
    SPACY_AVAILABLE = False
    nlp = None


class PromptEnhancer:
    """Main class for prompt enhancement - Pure Python with optional NLP."""
    
    def __init__(self):
        """Initialize the enhancer."""
        # Load stopwords with fallback
        try:
            if NLTK_AVAILABLE:
                self.stop_words = set(stopwords.words('english'))
            else:
                self.stop_words = self._get_fallback_stopwords()
        except:
            self.stop_words = self._get_fallback_stopwords()
        
        self.style_templates = {
            'professional': {
                'prefixes': ['Create', 'Develop', 'Implement', 'Design', 'Establish'],
                'additions': [' with clear specifications', ' ensuring quality and efficiency', ' following best practices'],
                'tone_words': ['professional', 'structured', 'efficient', 'scalable', 'robust']
            },
            'creative': {
                'prefixes': ['Imagine', 'Create', 'Design', 'Craft', 'Conceptualize'],
                'additions': [' with innovative features', ' that stands out visually', ' with unique interactive elements'],
                'tone_words': ['innovative', 'visually appealing', 'creative', 'engaging', 'dynamic', 'modern']
            },
            'detailed': {
                'prefixes': ['Create a comprehensive', 'Develop a detailed', 'Build an in-depth'],
                'additions': [' including all components and specifications', ' with complete documentation', ' covering all aspects'],
                'tone_words': ['comprehensive', 'detailed', 'thorough', 'complete', 'well-documented']
            },
            'simplified': {
                'prefixes': ['Make a simple', 'Create an easy', 'Build a basic'],
                'additions': [' that is easy to use', ' without complexity', ' keeping it straightforward'],
                'tone_words': ['simple', 'clean', 'easy to use', 'straightforward', 'minimal']
            }
        }
    
    @staticmethod
    def _get_fallback_stopwords():
        """Return a basic set of English stopwords."""
        return {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
            'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
            'could', 'should', 'may', 'might', 'can', 'must', 'shall', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what',
            'which', 'who', 'when', 'where', 'why', 'how'
        }
    
    def _basic_tokenize(self, text):
        """Basic tokenization without NLTK."""
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words
    
    def _basic_sentence_split(self, text):
        """Basic sentence splitting without NLTK."""
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def extract_keywords(self, text):
        """Extract important keywords from text using available tools."""
        keywords = []
        
        if SPACY_AVAILABLE and nlp is not None:
            try:
                doc = nlp(text)
                # Extract named entities
                for ent in doc.ents:
                    if len(ent.text) > 2:
                        keywords.append(ent.text.lower())
                
                # Extract nouns
                for token in doc:
                    if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
                        keywords.append(token.text.lower())
                
                # Extract noun chunks
                for noun_chunk in doc.noun_chunks:
                    if len(noun_chunk.text.split()) > 1 and len(noun_chunk.text) > 2:
                        keywords.append(noun_chunk.text.lower())
                        
                if keywords:
                    return self._deduplicate_keywords(keywords)
            except:
                pass
        
        # Fallback to basic extraction
        return self._extract_keywords_basic(text)
    
    def _extract_keywords_basic(self, text):
        """Basic keyword extraction using regex."""
        words = self._basic_tokenize(text)
        keywords = []
        for word in words:
            if len(word) > 3 and word not in self.stop_words:
                keywords.append(word)
        
        return self._deduplicate_keywords(keywords)
    
    def _deduplicate_keywords(self, keywords):
        """Remove duplicates while preserving order."""
        seen = set()
        unique_keywords = []
        for keyword in keywords:
            if keyword not in seen and len(keyword) > 2:
                seen.add(keyword)
                unique_keywords.append(keyword)
        
        return unique_keywords[:10]  # Return top 10
    
    def get_synonyms(self, word):
        """Get synonyms for a word using WordNet if available."""
        if not NLTK_AVAILABLE:
            return []
        
        try:
            from nltk.corpus import wordnet
            synonyms = set()
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    syn_name = lemma.name().replace("_", " ")
                    if syn_name.lower() != word.lower() and len(syn_name) > 2:
                        synonyms.add(syn_name)
            return list(synonyms)[:5]
        except:
            return []
    
    def expand_vague_sentences(self, text):
        """Expand vague or simple sentences with more detail."""
        # Try NLTK sentence splitting first
        if NLTK_AVAILABLE:
            try:
                sentences = sent_tokenize(text)
            except:
                sentences = self._basic_sentence_split(text)
        else:
            sentences = self._basic_sentence_split(text)
        
        enhanced_sentences = []
        
        for sent in sentences:
            words = self._basic_tokenize(sent)
            
            # If sentence is very short, add elaboration
            if len(words) < 8:
                elaboration = self._get_elaboration(sent)
                enhanced_sentences.append(f"{sent.strip()} {elaboration}.")
            else:
                enhanced_sentences.append(sent.strip())
        
        return ' '.join(enhanced_sentences)
    
    def _get_elaboration(self, sentence):
        """Add elaboration to sentences based on context."""
        elaborations = {
            'make': 'by implementing best practices',
            'build': 'with proper architecture and design',
            'create': 'ensuring functionality and user experience',
            'design': 'with attention to detail and user needs',
            'develop': 'following structured methodology',
            'improve': 'through systematic enhancement',
            'add': 'with appropriate integration',
            'use': 'for maximum effectiveness',
            'write': 'with clear structure and organization',
            'get': 'through effective implementation'
        }
        
        sentence_lower = sentence.lower()
        for key, value in elaborations.items():
            if key in sentence_lower:
                return value
        
        return "with comprehensive specifications"
    
    def apply_style(self, text, style):
        """Apply style transformations to text."""
        if style not in self.style_templates:
            style = 'professional'
        
        template = self.style_templates[style]
        
        # Split sentences
        if NLTK_AVAILABLE:
            try:
                sentences = sent_tokenize(text)
            except:
                sentences = self._basic_sentence_split(text)
        else:
            sentences = self._basic_sentence_split(text)
        
        if not sentences:
            return text
        
        enhanced_text = text
        first_sent = sentences[0]
        new_prefix = template['prefixes'][0]
        
        # Remove common weak starters
        weak_starters = ['Make', 'Build', 'Create', 'Design', 'Develop', 'Add', 'Use', 'Try', 'Write', 'Get']
        first_sent_lower = first_sent.lower()
        
        for starter in weak_starters:
            if first_sent_lower.startswith(starter.lower()):
                first_sent = first_sent[len(starter):].lstrip()
                break
        
        enhanced_text = f"{new_prefix} {first_sent}"
        
        # Add remaining sentences
        if len(sentences) > 1:
            enhanced_text += ' ' + ' '.join(sentences[1:])
        
        # Add style-specific addition
        addition = template['additions'][0]
        if not enhanced_text.endswith(('.', '!', '?')):
            enhanced_text += addition + '.'
        
        return enhanced_text
    
    def add_context_boost(self, text, include_context=False):
        """Add context boost with examples and target audience."""
        if not include_context:
            return text
        
        boosts = {
            'audience': "Target audience: professionals, developers, and stakeholders.",
            'requirements': "Include clear requirements, specifications, and deliverables.",
            'examples': "Add relevant examples and use cases to illustrate the concept.",
            'format': "Structure the output in a clear, organized manner.",
            'standards': "Ensure alignment with industry standards and best practices."
        }
        
        enhancements = '\n'.join([f"• {v}" for v in boosts.values()])
        return f"{text}\n\nContext Boost Applied:\n{enhancements}"
    
    def enhance_prompt(self, prompt, style='professional', context_boost=False):
        """
        Main function to enhance a prompt.
        
        Args:
            prompt (str): The original prompt text
            style (str): Enhancement style - 'professional', 'creative', 'detailed', or 'simplified'
            context_boost (bool): Whether to add context boost
        
        Returns:
            dict: Dictionary containing enhanced prompt and metadata
        """
        if not prompt or not prompt.strip():
            return {
                'enhanced_prompt': 'Please provide a prompt to enhance.',
                'keywords': [],
                'synonyms': {},
                'style': style,
                'context_boost_applied': False,
                'original_length': 0,
                'enhanced_length': 0
            }
        
        # Clean and normalize input
        prompt = prompt.strip()
        
        # Step 1: Extract keywords
        keywords = self.extract_keywords(prompt)
        
        # Step 2: Get synonyms
        synonyms = {}
        for keyword in keywords[:5]:
            syns = self.get_synonyms(keyword)
            if syns:
                synonyms[keyword] = syns
        
        # Step 3: Expand vague sentences
        expanded = self.expand_vague_sentences(prompt)
        
        # Step 4: Apply style
        enhanced = self.apply_style(expanded, style)
        
        # Step 5: Add context boost if requested
        if context_boost:
            enhanced = self.add_context_boost(enhanced, include_context=True)
        
        # Step 6: Refine for style
        enhanced = self._refine_for_style(enhanced, style)
        
        return {
            'enhanced_prompt': enhanced,
            'keywords': keywords,
            'synonyms': synonyms,
            'style': style,
            'context_boost_applied': context_boost,
            'original_length': len(prompt.split()),
            'enhanced_length': len(enhanced.split())
        }
    
    def _refine_for_style(self, text, style):
        """Apply final refinements based on style."""
        template = self.style_templates.get(style, self.style_templates['professional'])
        
        # Add style-specific tone
        if style == 'professional' and 'ensure' not in text.lower():
            text = text.replace('.', ', ensuring quality and efficiency.')
        elif style == 'creative' and 'innovative' not in text.lower():
            sentences = self._basic_sentence_split(text)
            if sentences:
                last_sent = sentences[-1]
                replacement = f"{last_sent.rstrip('.')}, creating an engaging and memorable experience."
                text = text.replace(last_sent, replacement)
        elif style == 'detailed' and 'comprehensive' not in text.lower():
            if not text.endswith('.'):
                text = text + '.'
            text = text + ' Ensure comprehensive coverage of all aspects and components.'
        elif style == 'simplified':
            # Remove unnecessary adjectives
            text = re.sub(r'\b(very|extremely|highly|significantly)\s+', '', text, flags=re.IGNORECASE)
        
        return text


# Global instance
enhancer = PromptEnhancer()


def enhance_prompt(prompt, style='professional', context_boost=False):
    """
    Public API for prompt enhancement.
    
    Args:
        prompt (str): The prompt to enhance
        style (str): 'professional', 'creative', 'detailed', or 'simplified'
        context_boost (bool): Add context boost if True
    
    Returns:
        dict: Enhanced prompt with metadata
    """
    return enhancer.enhance_prompt(prompt, style, context_boost)


if __name__ == '__main__':
    # Test the enhancer
    test_prompt = "Make a website that looks cool for data science students."
    result = enhance_prompt(test_prompt, style='creative', context_boost=True)
    
    print("Original Prompt:")
    print(test_prompt)
    print("\n" + "="*60 + "\n")
    print("Enhanced Prompt:")
    print(result['enhanced_prompt'])
    print("\n" + "="*60 + "\n")
    print(f"Keywords: {', '.join(result['keywords'])}")
    print(f"\nSynonyms:")
    for word, syns in result['synonyms'].items():
        print(f"  {word}: {', '.join(syns)}")
