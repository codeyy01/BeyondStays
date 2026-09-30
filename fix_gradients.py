import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace left arrow before
css = re.sub(
    r'\.hero-nav\.prev::before \{.*?(?=\})\}',
    '.hero-nav.prev::before {\n    left: 0;\n    top: -30px;\n    width: 30px;\n    height: 30px;\n    background: radial-gradient(circle at top right, transparent 30px, #fff 30px);\n    box-shadow: none;\n}',
    css, flags=re.DOTALL
)

# Replace left arrow after
css = re.sub(
    r'\.hero-nav\.prev::after \{.*?(?=\})\}',
    '.hero-nav.prev::after {\n    left: 0;\n    bottom: -30px;\n    width: 30px;\n    height: 30px;\n    background: radial-gradient(circle at bottom right, transparent 30px, #fff 30px);\n    box-shadow: none;\n}',
    css, flags=re.DOTALL
)

# Replace right arrow before
css = re.sub(
    r'\.hero-nav\.next::before \{.*?(?=\})\}',
    '.hero-nav.next::before {\n    right: 0;\n    top: -30px;\n    width: 30px;\n    height: 30px;\n    background: radial-gradient(circle at top left, transparent 30px, #fff 30px);\n    box-shadow: none;\n}',
    css, flags=re.DOTALL
)

# Replace right arrow after
css = re.sub(
    r'\.hero-nav\.next::after \{.*?(?=\})\}',
    '.hero-nav.next::after {\n    right: 0;\n    bottom: -30px;\n    width: 30px;\n    height: 30px;\n    background: radial-gradient(circle at bottom left, transparent 30px, #fff 30px);\n    box-shadow: none;\n}',
    css, flags=re.DOTALL
)

# Replace logo tab before
css = re.sub(
    r'\.logo-tab::before \{.*?(?=\})\}',
    '.logo-tab::before {\n    left: -30px;\n    top: 16px;\n    width: 30px;\n    height: 30px;\n    background: radial-gradient(circle at bottom left, transparent 30px, #fff 30px);\n    box-shadow: none;\n}',
    css, flags=re.DOTALL
)

# Replace logo tab after
css = re.sub(
    r'\.logo-tab::after \{.*?(?=\})\}',
    '.logo-tab::after {\n    right: -30px;\n    top: 16px;\n    width: 30px;\n    height: 30px;\n    background: radial-gradient(circle at bottom right, transparent 30px, #fff 30px);\n    box-shadow: none;\n}',
    css, flags=re.DOTALL
)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Gradients injected.")
