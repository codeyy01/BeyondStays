import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix hamburger color variable from --dark-green to --green
css = css.replace('background: var(--dark-green) !important;', 'background: var(--green) !important;')

# 2. Strict bottom left for button container
new_css = '''
@media (max-width: 768px) {
    /* Strict bottom-left positioning */
    .hero-ui-layer {
        position: absolute !important;
        inset: 0 !important;
        padding: 0 !important;
    }
    .hero-left-content {
        position: absolute !important;
        bottom: 30px !important;
        left: 20px !important;
    }
    /* Ensure the button itself has the exact glass effect */
    .hero-left-content .hero-btn-pill {
        background: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        color: #fff !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
        font-weight: 700 !important;
        padding: 12px 30px !important;
        border-radius: 40px !important;
    }
}
'''
css += '\n' + new_css

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied.")
