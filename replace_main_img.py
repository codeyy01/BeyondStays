import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_frame_regex = r'<div class="desk-frame-main">[\s\S]*?<div class="desk-frame-dots">[\s\S]*?</div>\s*</div>'

main_frame_new = '''<div class="desk-frame-main" style="background: transparent;">
                <img id="aboutMainImg" src="./assets/aboutPictures/cozy_staysInKerala.jpeg" alt="Cozy Stays in Kerala" style="width:100%; height:100%; object-fit:cover; transition: opacity 0.4s ease;" />
            </div>'''
html = re.sub(main_frame_regex, main_frame_new, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
