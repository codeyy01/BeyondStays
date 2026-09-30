import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add position absolute and centering back to logo-tab
css = re.sub(
    r'\.logo-tab \{\s*top: 0;',
    '.logo-tab {\n    position: absolute;\n    left: 50%;\n    transform: translateX(-50%);\n    top: 0;',
    css
)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed logo tab position.")
