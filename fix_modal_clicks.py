import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix image wrap
js = re.sub(
    r'onclick="bookPackageWa\(\'\$\{pkg\.placeName\}\', \'\$\{pkg\.name\}\'\)"',
    r'onclick="openModal(${i})"',
    js
)

# Fix arrow btn
js = re.sub(
    r'onclick="event\.stopPropagation\(\); bookPackageWa\(\'\$\{pkg\.placeName\}\', \'\$\{pkg\.name\}\'\)"',
    r'onclick="event.stopPropagation(); openModal(${i})"',
    js
)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
