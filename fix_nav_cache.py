import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the nav-inner flex layout
css = css.replace(
    '''#navbar.cutout-mode .nav-inner {\n    position: relative;\n    width: 100%;\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n}''',
    '''#navbar.cutout-mode .nav-inner {\n    position: relative;\n    width: 100%;\n    display: flex;\n    justify-content: center;\n    gap: 200px;\n    align-items: center;\n}'''
)
# Just in case whitespace was different
css = re.sub(r'#navbar\.cutout-mode \.nav-inner\s*\{[^\}]*\}', '''#navbar.cutout-mode .nav-inner {
    position: relative;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 280px;
    align-items: center;
}''', css)

with open('style_absolute_final.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[0-9]+', 'style_absolute_final.css?v=9999', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
