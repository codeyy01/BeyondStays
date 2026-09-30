import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix catch syntax
js = js.replace('catch {', 'catch (e) {')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed catch syntax.")
