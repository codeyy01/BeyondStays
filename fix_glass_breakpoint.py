import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change the liquid glass / rounded corners media query to 1024px
css = re.sub(
    r'@media \(max-width: 768px\) \{\s*/\* Remove rounded corners on hero images \*/',
    r'@media (max-width: 1024px) {\n    /* Remove rounded corners on hero images */',
    css
)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Liquid glass breakpoint updated.")
