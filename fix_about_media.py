import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_css = '''#about .container {
    max-width: 1536px;
    padding: 0 60px;
}'''

new_css = '''@media (min-width: 1025px) {
    #about .container {
        max-width: 1600px;
        padding: 0 80px;
    }
}'''

css = css.replace(old_css, new_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
