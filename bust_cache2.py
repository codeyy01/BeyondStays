import re
import time

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())

# Replace style.css with cache busted version
html = re.sub(r'href="style\.css(\?v=\d+)?"', f'href="style.css?v={ts}"', html)
html = re.sub(r'src="script\.js(\?v=\d+)?"', f'src="script.js?v={ts}"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
