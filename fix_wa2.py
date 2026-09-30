import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.wa-float', '.wa-fab')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
