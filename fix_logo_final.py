import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix logo-tab top
css = re.sub(r'\.logo-tab \{\s*top: 16px;', '.logo-tab {\n    top: 0;', css)

# Fix logo-tab before top
css = re.sub(
    r'\.logo-tab::before \{\s*left: -30px;\s*top: 0;',
    '.logo-tab::before {\n    left: -30px;\n    top: 16px;',
    css
)

# Fix logo-tab after top
css = re.sub(
    r'\.logo-tab::after \{\s*right: -30px;\s*top: 0;',
    '.logo-tab::after {\n    right: -30px;\n    top: 16px;',
    css
)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Logo tab and curves positioned.")
