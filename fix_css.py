import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove body { background: #123500; }
css = css.replace('body { background: #123500; }', '')

# 2. Update #navbar.cutout-mode
old_nav_mode = '#navbar.cutout-mode {\n    position: absolute;\n    top: 0;\n    left: 0;\n    width: 100%;\n    max-width: 100%;\n    background: transparent;\n    border: none;\n    backdrop-filter: none;\n    -webkit-backdrop-filter: none;\n    box-shadow: none;\n    z-index: 1000;\n}'
new_nav_mode = '''#navbar.cutout-mode {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    transform: none !important;
    width: 100% !important;
    max-width: none !important;
    background: transparent !important;
    border: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    box-shadow: none !important;
    z-index: 1000 !important;
}'''
css = css.replace(old_nav_mode, new_nav_mode)

# 3. Fix nav links color specificity
old_nav_links = '#navbar.cutout-mode .nav-links a {\n    color: #ffffff;\n    font-weight: 500;\n}'
new_nav_links = '''#navbar.cutout-mode .nav-links a {
    color: #ffffff !important;
    font-weight: 500;
}'''
css = css.replace(old_nav_links, new_nav_links)

# 4. Fix CTA color specificity
old_cta = '#navbar.cutout-mode .nav-cta {\n    background: #ffffff;\n    color: var(--green);\n    border-radius: 40px;\n    padding: 10px 24px;\n}'
new_cta = '''#navbar.cutout-mode .nav-cta {
    background: #ffffff !important;
    color: #123500 !important;
    border-radius: 40px;
    padding: 10px 24px;
}'''
css = css.replace(old_cta, new_cta)

# 5. Fix arrow styles
old_hero_nav = '''.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 48px;
    height: 80px;
    background: #ffffff;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-weight: bold;
    font-size: 1.5rem;
    color: #123500;
}'''
new_hero_nav = '''.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 56px;
    height: 96px;
    background: #ffffff;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.8rem;
    color: #123500;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}'''
css = css.replace(old_hero_nav, new_hero_nav)

# 6. Make .hero-frame slightly taller if needed, but height is fine.
# 7. In cutout mode, hide the old pseudo element underlines if any
css += '\n#navbar.cutout-mode .nav-links a::after { display: none !important; }\n'

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Now fix index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert font Anton
font_tag = '<link href=\"https://fonts.googleapis.com/css2?family=Anton&display=swap\" rel=\"stylesheet\" />'
if 'family=Anton' not in html:
    html = html.replace('<!-- Fonts -->', '<!-- Fonts -->\n    ' + font_tag)

# Update arrows to beautiful unicode characters
html = html.replace('<div class=\"hero-nav prev\" id=\"heroPrev\">&lt;</div>', '<div class=\"hero-nav prev\" id=\"heroPrev\">&#10094;</div>')
html = html.replace('<div class=\"hero-nav next\" id=\"heroNext\">&gt;</div>', '<div class=\"hero-nav next\" id=\"heroNext\">&#10095;</div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
