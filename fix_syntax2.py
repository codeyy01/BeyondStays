import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace any backslash at the very end of a line
js = re.sub(r'\\\n', r'\\n', js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
