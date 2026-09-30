import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace any occurrence of 3 closing braces that are right before a new CSS class or comment
css = re.sub(r'    \}\n\}\n\}(?=\s*(?:\/\*|\.|#|@))', r'    }\n}', css)
css = re.sub(r'    \}\n\}\n\n\}(?=\s*(?:\/\*|\.|#|@))', r'    }\n}', css)
css = re.sub(r'\}\n\}\n\}(?=\s*(?:\/\*|\.|#|@))', r'}\n}', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
