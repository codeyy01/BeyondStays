import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix Margin Collapse on hero-wrapper
css = css.replace('.hero-wrapper {\n    background: #123500;\n    position: relative;\n}', '.hero-wrapper {\n    background: #123500;\n    position: relative;\n    padding: 16px;\n}')
css = css.replace('.hero-frame {\n    margin: 16px;', '.hero-frame {\n    margin: 0;')

# 2. Change Nav Logo Container background to #123500
css = css.replace('background: #ffffff;\n    padding: 24px 60px 16px 60px;', 'background: #123500;\n    padding: 24px 60px 16px 60px;')

# 3. Change Arrow Tabs background and color
css = css.replace('background: #ffffff;\n    z-index: 10;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    cursor: pointer;\n    font-size: 1.8rem;\n    color: #123500;', 'background: #123500;\n    z-index: 10;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    cursor: pointer;\n    font-size: 1.8rem;\n    color: #ffffff;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update Logo in index.html to white because the background is now dark green!
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<img src=\"./assets/nav-logo-green.png\" id=\"navLogo\" alt=\"Beyondstays Logo\" />', '<img src=\"./assets/nav-logo-white.png\" id=\"navLogo\" alt=\"Beyondstays Logo\" />')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
