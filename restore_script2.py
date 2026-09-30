import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix all instances of if() corruption
js = re.sub(r'(if\(\)\s*)+', '', js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
