import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('bottom: 12px !important;\n        right: 12px !important;', 'bottom: 4px !important;\n        right: 4px !important;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
