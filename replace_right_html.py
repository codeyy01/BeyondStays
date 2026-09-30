import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_right_html = '''<div class="about-desk-right reveal-right">
        <div class="desk-green-main">
            <div class="desk-frame-main">
                <div class="desk-frame-dots">
                    <span></span><span></span><span></span><span></span>
                </div>
            </div>
            <div class="desk-green-bottom">
                <div class="desk-line"></div>
                <div class="desk-line" style="width: 60%;"></div>
                <div class="desk-line" style="width: 80%;"></div>
            </div>
        </div>
        <div class="desk-sidebar">
            <div class="desk-logo-box">
                <img src="./assets/nav-logo-white.png" alt="Beyondstays" />
            </div>
            <div class="desk-side-box"></div>
            <div class="desk-side-box"></div>
            <div class="desk-side-box"></div>
            <div class="desk-side-box"></div>
        </div>
    </div>'''

# Replace the old about-desk-right block
html = re.sub(r'<div class="about-desk-right reveal-right">[\s\S]*?<div class="about-mobile hide-on-desktop">', new_right_html + '\n</div>\n    <div class="about-mobile hide-on-desktop">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
