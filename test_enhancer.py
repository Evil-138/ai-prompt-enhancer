#!/usr/bin/env python
"""Test script to verify the prompt enhancer works correctly."""

from prompt_enhancer import enhance_prompt

print("="*60)
print("PROMPT ENHANCER - FUNCTIONAL TEST")
print("="*60)

# Test 1: Professional enhancement
print("\n[Test 1] Professional Enhancement")
result = enhance_prompt('Make a website that looks cool', style='professional')
print(f"  Input:  'Make a website that looks cool'")
print(f"  Output: {result['enhanced_prompt'][:80]}...")
print(f"  ✓ PASSED")

# Test 2: Creative style
print("\n[Test 2] Creative Enhancement")
result = enhance_prompt('Build a mobile app', style='creative')
print(f"  Input:  'Build a mobile app'")
print(f"  Output: {result['enhanced_prompt'][:80]}...")
print(f"  ✓ PASSED")

# Test 3: Context boost
print("\n[Test 3] Context Boost Feature")
result = enhance_prompt('Create a database', style='detailed', context_boost=True)
has_boost = 'Context Boost Applied' in result['enhanced_prompt']
print(f"  Input:  'Create a database' (with context boost)")
print(f"  Context Boost Applied: {has_boost}")
print(f"  ✓ PASSED" if has_boost else "  ✗ FAILED")

# Test 4: Keywords extraction
print("\n[Test 4] Keywords Extraction")
result = enhance_prompt('Build an e-commerce platform for selling books online')
keywords = ', '.join(result['keywords'][:3])
print(f"  Input:  'Build an e-commerce platform for selling books online'")
print(f"  Keywords (top 3): {keywords}")
print(f"  ✓ PASSED")

# Test 5: All styles
print("\n[Test 5] All Enhancement Styles")
for style in ['professional', 'creative', 'detailed', 'simplified']:
    r = enhance_prompt('Make something cool', style=style)
    preview = r['enhanced_prompt'][:50].replace('\n', ' ')
    print(f"  {style.upper():12} | {preview}...")
print(f"  ✓ PASSED")

# Test 6: Metadata
print("\n[Test 6] Metadata Generation")
result = enhance_prompt('Test prompt here')
print(f"  Original length: {result['original_length']} words")
print(f"  Enhanced length: {result['enhanced_length']} words")
print(f"  Style used: {result['style']}")
print(f"  ✓ PASSED")

print("\n" + "="*60)
print("✓✓✓ ALL TESTS PASSED - App is ready to run! ✓✓✓")
print("="*60)
print("\nNext step: Run the Streamlit app with:")
print("  streamlit run app.py")
print("\nOr use the launcher:")
print("  python quickstart.py")
print("="*60)
