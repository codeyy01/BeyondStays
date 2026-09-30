import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('about_desktop.html', 'r', encoding='utf-8') as f:
    desktop_html = f.read()

# Replace <div class="about-layout"> with the new desktop version + the mobile version
replacement = desktop_html + '\n' + '<div class="about-mobile hide-on-desktop">\n<div class="about-layout">'

html = html.replace('<div class="about-layout">', replacement)

# We need to add a closing </div> for the about-mobile block
# Find the end of the about section.
# The end of about-layout is </div></div></section>
html = html.replace('</div>\n        </div>\n    </section>\n\n    <section class="section">', '</div>\n        </div>\n        </div>\n    </section>\n\n    <section class="section">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
