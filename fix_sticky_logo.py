import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Append absolute centering for the sticky logo
new_css = '''
.navbar-scrolled .nav-logo {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    margin: 0;
}
'''
css += '\n' + new_css

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Logo centered.")
