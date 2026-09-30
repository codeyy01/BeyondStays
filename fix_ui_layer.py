import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_ui = '''    /* Position Explore Now button to bottom left */
    .hero-ui-layer {
        justify-content: flex-start !important;
        align-items: flex-end !important;
        left: 24px !important;
        right: 24px !important;
        bottom: 30px !important; 
    }'''

new_ui = '''    /* Position Explore Now button to bottom left */
    .hero-ui-layer {
        flex-direction: row !important;
        justify-content: flex-start !important;
        align-items: flex-end !important;
        left: 24px !important;
        right: 24px !important;
        bottom: 24px !important; 
    }'''

css = css.replace(old_ui, new_ui)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
