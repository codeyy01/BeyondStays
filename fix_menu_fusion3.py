import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_menu = '''    top: 68px; /* sits right beneath the navbar */
    left: 50%;
    transform: translateX(-50%) translateY(-20px);
    width: 90%;
    padding: 24px 0 40px 0;'''

good_menu = '''    top: 90px; /* tucked just behind the bottom edge of navbar */
    left: 50%;
    transform: translateX(-50%) translateY(-20px);
    width: 90%;
    padding: 30px 0 40px 0;'''

css = css.replace(bad_menu, good_menu)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
