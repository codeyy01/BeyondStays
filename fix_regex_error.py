import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the literal newline in the regex with \n
js = js.replace('desc = desc.replace(/\n/g, \'<br/>\');', 'desc = desc.replace(/\\\\n/g, \'<br/>\');')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
