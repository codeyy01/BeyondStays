import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove all reveal-up, reveal-left, reveal-right classes from html
html = html.replace(' reveal-up', '')
html = html.replace('reveal-up ', '')
html = html.replace('class="reveal-up"', '')

html = html.replace(' reveal-left', '')
html = html.replace('reveal-left ', '')
html = html.replace('class="reveal-left"', '')

html = html.replace(' reveal-right', '')
html = html.replace('reveal-right ', '')
html = html.replace('class="reveal-right"', '')

html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=14', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed all reveal classes to prevent invisible elements!")
