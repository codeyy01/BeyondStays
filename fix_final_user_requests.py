import re

# 1. Fix JS Error
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace if (navbar) navbar.classList.remove('menu-open'); with stickyNavOverlay
js = js.replace("if (navbar) navbar.classList.remove('menu-open');", "const sno = document.getElementById('navbar-scrolled'); if (sno) sno.classList.remove('menu-open');")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Fix CSS
with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change .hero-ui-layer justify-content to flex-start for bottom left
css = re.sub(r'justify-content: center !important;\s*align-items: flex-end !important;', 'justify-content: flex-start !important;\n        align-items: flex-end !important;', css)

# Append remaining CSS rules
new_css = '''
@media (max-width: 768px) {
    /* Remove rounded corners on hero images */
    .hero-slides, .hero-slides img {
        border-radius: 0 !important;
    }
    
    /* Liquid glass effect for Explore Now button */
    .hero-btn-pill {
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        color: #fff !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1) !important;
    }
}
'''
css += '\n' + new_css

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied.")
