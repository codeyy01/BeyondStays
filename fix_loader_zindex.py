import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace z-index: 9999 with z-index: 99999 inside #loader
# But be careful to only do it for #loader
css = re.sub(r'(#loader\s*\{[^}]*?z-index:\s*)9999(;|)', r'\g<1>99999\2', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
