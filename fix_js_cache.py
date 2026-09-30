import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'src="script\.js(\?v=[0-9]+)?"', 'src="script.js?v=9999"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Added cache buster to script.js!')
