import re

# 1. Remove Back To Top button from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<!-- BACK TO TOP -->\s*<button class="btt[^>]+>.*?</button>', '', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update style.css for the Explore button, liquid glass, and WhatsApp icon
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change hero button to liquid glass globally
old_btn = '''.hero-btn-pill {
    background: #ffffff;
    color: #123500;
    padding: 14px 28px;
    border-radius: 40px;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
}'''

new_btn = '''.hero-btn-pill {
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    color: #ffffff !important;
    padding: 14px 32px;
    border-radius: 40px;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
}'''

css = css.replace(old_btn, new_btn)

# Update mobile layout for .hero-ui-layer to center the button under INDIA
old_ui_mobile = '''    /* Position Explore Now button to bottom left */
    .hero-ui-layer {
        flex-direction: row !important;
        justify-content: flex-start !important;
        align-items: flex-end !important;
        left: 24px !important;
        right: 24px !important;
        bottom: 24px !important; 
    }'''

new_ui_mobile = '''    /* Position Explore Now button under INDIA */
    .hero-ui-layer {
        flex-direction: row !important;
        justify-content: center !important;
        align-items: center !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 15% !important; /* Move it up directly under INDIA */
    }'''

css = css.replace(old_ui_mobile, new_ui_mobile)

# Update whatsapp icon position on mobile
wa_mobile_css = '''
    /* Push WhatsApp icon much closer to the bottom */
    .wa-float {
        bottom: 12px !important;
        right: 12px !important;
    }
'''
css = re.sub(r'(?=\}\s*$)', wa_mobile_css, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
