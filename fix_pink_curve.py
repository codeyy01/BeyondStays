import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the entire logo-tab block to ensure perfect geometry
new_css = '''
/* Logo Tab Cutout */
.logo-tab {
    top: 0;
    height: 76px;
    padding: 0 40px;
    background: #fff;
    border-bottom-left-radius: 40px 30px;
    border-bottom-right-radius: 40px 30px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.logo-tab::before, .logo-tab::after {
    content: '';
    position: absolute;
    top: 16px;
    width: 60px;
    height: 30px;
    box-shadow: none;
}
.logo-tab::before {
    left: -60px;
    background: radial-gradient(60px 30px at bottom left, transparent 98%, #fff 99.5%);
}
.logo-tab::after {
    right: -60px;
    background: radial-gradient(60px 30px at bottom right, transparent 98%, #fff 99.5%);
}
'''

# Use regex to find and replace everything from .logo-tab { to the end of .logo-tab::after { ... }
# Since there are multiple blocks, let's just do a manual string replace of the known blocks, or a smart regex.

# Remove old .logo-tab block
css = re.sub(r'\.logo-tab \{[^}]*\}', '', css)
# Remove old .logo-tab::before, .logo-tab::after block (the shared one)
css = re.sub(r'\.logo-tab::before, \.logo-tab::after \{[^}]*\}', '', css)
# Remove old .logo-tab::before block
css = re.sub(r'\.logo-tab::before \{[^}]*\}', '', css)
# Remove old .logo-tab::after block
css = re.sub(r'\.logo-tab::after \{[^}]*\}', '', css)

# Now insert the new_css where the old one roughly was, or just append it before "/* -- SCROLLED STATE (Unified Pill) -- */"
css = css.replace('/* -- SCROLLED STATE (Unified Pill) -- */', new_css + '\n/* -- SCROLLED STATE (Unified Pill) -- */')

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Sweeping S-curves applied.")
