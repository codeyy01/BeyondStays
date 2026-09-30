# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The LinkedIn icon has aria-label="LinkedIn"
html = re.sub(r'<a href="#" aria-label="LinkedIn">.*?</a>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed LinkedIn icon.")
