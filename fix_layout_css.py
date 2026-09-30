import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add scroll indicator CSS globally
scroll_css = '''
/* --- SCROLL INDICATOR --- */
.scroll-indicator {
    position: absolute;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 100;
}
.scroll-line {
    width: 2px;
    height: 48px;
    background: rgba(255, 255, 255, 0.2);
    position: relative;
    overflow: hidden;
    border-radius: 2px;
}
.scroll-line::before {
    content: '';
    position: absolute;
    top: -100%;
    left: 0;
    width: 100%;
    height: 100%;
    background: #ffffff;
    animation: scrollDrop 1.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
@keyframes scrollDrop {
    0% { top: -100%; }
    100% { top: 100%; }
}
'''
if '/* --- SCROLL INDICATOR --- */' not in css:
    css += scroll_css

# Update the mobile reset for .hero-ui-layer
old_ui_mobile = '''    /* Adjust UI layer for mobile to center the button */
    .hero-ui-layer {
        justify-content: center !important;
        left: 20px !important;
        right: 20px !important;
        bottom: 120px !important; /* Move button up slightly */
    }'''

new_ui_mobile = '''    /* Position Explore Now button to bottom left */
    .hero-ui-layer {
        justify-content: flex-start !important;
        align-items: flex-end !important;
        left: 24px !important;
        right: 24px !important;
        bottom: 30px !important; 
    }'''

css = css.replace(old_ui_mobile, new_ui_mobile)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
