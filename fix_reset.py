import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The missing reset block from the original code
reset_block = """
/* ── Reset ── */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
html {
    scroll-behavior: smooth;
}
body {
    font-family: var(--font-body);
    color: var(--text);
    background: var(--cream);
    overflow-x: hidden;
}
img {
    display: block;
    max-width: 100%;
    object-fit: cover;
}
a {
    text-decoration: none;
    color: inherit;
}
"""

# Let's remove my broken `body` declaration from perfect_css
css = re.sub(r'body\s*\{[^}]*\}', '', css, count=1)

# Now inject the reset block right after :root { ... }
root_end = css.find('}') + 1
css = css[:root_end] + '\n\n' + reset_block + css[root_end:]

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update HTML cache buster to force reload
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=3', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Restored typography, reset block, and fixed body background!")
