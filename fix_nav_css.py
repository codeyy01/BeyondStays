import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_nav = '''.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 64px;
    height: 100px;
    background: #ffffff;
    z-index: 10;'''

good_nav = '''.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 64px;
    height: 100px;
    background: #ffffff;
    z-index: 9999;
    pointer-events: auto;
    cursor: pointer;'''

css = css.replace(bad_nav, good_nav)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
