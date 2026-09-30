import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_override = '''
/* MOBILE NAVBAR FIX */
@media (max-width: 768px) {
    .nav-logo-container {
        position: static !important;
        transform: none !important;
        left: auto !important;
        height: auto !important;
        justify-content: flex-start !important;
    }
}
'''

if '/* MOBILE NAVBAR FIX */' not in css:
    css += mobile_override

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
