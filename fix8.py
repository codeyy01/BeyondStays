import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .nav-inner to have justify-content: space-between and position: relative
old_nav_inner = '''.nav-inner {
    max-width: 1280px;
    margin: auto;
    padding: 0 40px;
    height: var(--nav-h);
    display: flex;
    align-items: center;
    gap: 48px;
}'''
new_nav_inner = '''.nav-inner {
    max-width: 1280px;
    margin: auto;
    padding: 0 40px;
    height: var(--nav-h);
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
}'''
css = css.replace(old_nav_inner, new_nav_inner)

# 2. Add absolute centering for the logo in the default state
# We can just append a rule for .nav-logo-container (since it doesn't exist in the default CSS yet)
css += '''
.nav-logo-container {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    top: 0;
    height: 100%;
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
