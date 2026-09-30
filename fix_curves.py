import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix logo-tab top
css = re.sub(r'\.logo-tab \{\s*top: -16px;', '.logo-tab {\n    top: 16px;', css)

# Fix hero-nav.prev left
css = re.sub(r'\.hero-nav\.prev \{\s*left: 16px;', '.hero-nav.prev {\n    left: 0;', css)

# Fix hero-nav.next right
css = re.sub(r'\.hero-nav\.next \{\s*right: 16px;', '.hero-nav.next {\n    right: 0;', css)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS fixed.")
