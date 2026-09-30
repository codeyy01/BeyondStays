with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

opens = html.count('<div')
closes = html.count('</div')
print(f'Open divs: {opens}, Close divs: {closes}')
