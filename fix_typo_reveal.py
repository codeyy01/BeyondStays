import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('class="quote-break-section reveal-up"', 'class="quote-break-section"')
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=13', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed reveal-up on typo block!")
