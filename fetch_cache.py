import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = re.sub(r"fetch\('data\.json'\)", "fetch('data.json?v=' + new Date().getTime())", js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
