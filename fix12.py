import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_scrolled_cta = '#navbar.scrolled .nav-cta { background: var(--green); color: var(--white); }'
new_scrolled_cta = '#navbar.scrolled .nav-links a.nav-cta { background: var(--green); color: var(--white); }'
css = css.replace(old_scrolled_cta, new_scrolled_cta)

old_scrolled_cta_hover = '#navbar.scrolled .nav-cta:hover { background: var(--green-light); }'
new_scrolled_cta_hover = '#navbar.scrolled .nav-links a.nav-cta:hover { background: var(--green-light); }'
css = css.replace(old_scrolled_cta_hover, new_scrolled_cta_hover)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
