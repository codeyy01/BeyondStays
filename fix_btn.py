import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_btn = '''.hero-btn-pill {
    background: #ffffff;
    color: #123500;
    padding: 14px 28px;
    border-radius: 40px;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
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

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
