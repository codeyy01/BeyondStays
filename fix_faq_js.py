import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove 'reveal-up' from faq-item creation
js = js.replace("const item = el('div', 'faq-item reveal-up');", "const item = el('div', 'faq-item');")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Removed reveal-up from faq-item.")
