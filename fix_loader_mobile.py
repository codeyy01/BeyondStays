import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Completely remove the mobile loader block if it exists
css = re.sub(r'@media\s*\(\s*max-width\s*:\s*768px\s*\)\s*\{\s*#loader\s*\{[\s\S]*?(?=\}\s*#loader\.done)', '', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
