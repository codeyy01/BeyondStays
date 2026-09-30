import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_cta = '#navbar.cutout-mode .nav-cta {'
new_cta = '#navbar.cutout-mode .nav-links a.nav-cta {'
css = css.replace(old_cta, new_cta)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
