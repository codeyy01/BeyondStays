import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_css = '''@keyframes scrollDrop {
    0% { top: -100%; }
    100% { top: 100%; }

    /* Push WhatsApp icon much closer to the bottom */
    .wa-float {
        bottom: 12px !important;
        right: 12px !important;
    }
}'''

good_css = '''@keyframes scrollDrop {
    0% { top: -100%; }
    100% { top: 100%; }
}

@media (max-width: 768px) {
    /* Push WhatsApp icon much closer to the bottom */
    .wa-float {
        bottom: 12px !important;
        right: 12px !important;
    }
}'''

css = css.replace(bad_css, good_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
