import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_cutout = '''#navbar.cutout-mode .nav-logo-container {
    position: absolute;
    top: 0px;
    left: 50%;
    transform: translateX(-50%);
    background: #ffffff;
    padding: 16px 60px 16px 60px;
    border-radius: 0 0 32px 32px;
    display: flex;
    align-items: center;
    justify-content: center;
}'''

new_cutout = '''#navbar.cutout-mode .nav-logo-container {
    position: absolute;
    top: 0px;
    left: 50%;
    transform: translateX(-50%);
    background: #ffffff;
    padding: 16px 60px 16px 60px;
    border-radius: 0 0 32px 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: auto !important;
}'''
css = css.replace(old_cutout, new_cutout)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
