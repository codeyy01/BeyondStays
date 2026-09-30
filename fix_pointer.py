import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_title = '''.hero-giant-title {
    position: absolute;
    inset: 0;
    display: flex;'''

good_title = '''.hero-giant-title {
    position: absolute;
    inset: 0;
    pointer-events: none;
    display: flex;'''

css = css.replace(bad_title, good_title)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
