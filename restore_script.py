import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the window event listener
js = re.sub(r'window(?:if\(\)\s*)+\.addEventListener', 'window.addEventListener', js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
