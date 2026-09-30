with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<link rel="style_ultimate.css?v=1" />', '<link rel="stylesheet" href="style_ultimate.css?v=2" />')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
