import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the onclick
pattern = r'onclick="openModal\([^)]+\)"'
replacement = r'onclick="event.stopPropagation(); bookPackageWa(\'${pkg.placeName}\', \'${pkg.name}\')"'
js = re.sub(pattern, replacement, js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
