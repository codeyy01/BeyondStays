import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('const runInit = () => {', 'const runInit = () => { console.log("runInit called!");')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
