import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

fallback = '''#loader {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    width: 100%;
    height: 100%;
    inset: 0;'''

css = css.replace('#loader {\n    position: fixed;\n    inset: 0;', fallback)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
