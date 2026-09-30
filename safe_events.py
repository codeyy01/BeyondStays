import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace .addEventListener with a safe pattern where possible, or just wrap the specific ones at the bottom.
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
