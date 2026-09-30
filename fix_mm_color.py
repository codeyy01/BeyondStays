with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('color: var(--dark-green)', 'color: var(--green)')

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)
