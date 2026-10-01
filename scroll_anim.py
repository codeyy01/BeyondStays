import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_scroll = r'<!-- NEW SCROLL INDICATOR -->\s*<div class="scroll-indicator">\s*<div class="scroll-line"></div>\s*</div>'

new_scroll = '''<!-- SUPER ANIMATED SCROLL INDICATOR -->
                <div class="scroll-indicator-super" onclick="document.getElementById('about').scrollIntoView({behavior:'smooth'});">
                    <div class="chevron"></div>
                    <div class="chevron"></div>
                    <div class="chevron"></div>
                </div>'''

html = re.sub(old_scroll, new_scroll, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css_super = '''
/* --- SUPER ANIMATED SCROLL INDICATOR --- */
.scroll-indicator-super {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 60px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 1000;
}
.scroll-indicator-super .chevron {
    width: 20px;
    height: 20px;
    border-right: 3px solid #fff;
    border-bottom: 3px solid #fff;
    transform: rotate(45deg);
    animation: bounceChevron 2s infinite;
    margin-top: -10px;
}
.scroll-indicator-super .chevron:nth-child(1) { animation-delay: 0s; }
.scroll-indicator-super .chevron:nth-child(2) { animation-delay: 0.15s; }
.scroll-indicator-super .chevron:nth-child(3) { animation-delay: 0.3s; }

@keyframes bounceChevron {
    0% { opacity: 0; transform: rotate(45deg) translate(-10px, -10px); }
    50% { opacity: 1; }
    100% { opacity: 0; transform: rotate(45deg) translate(10px, 10px); }
}
'''

with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write(css_super)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=24', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
