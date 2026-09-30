import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will just replace the exact text
broken_text = '''#loader::before {
    display: none;
}
}
#loader.done {'''

fixed_text = '''#loader::before {
    display: none;
}
#loader.done {'''

css = css.replace(broken_text, fixed_text)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
