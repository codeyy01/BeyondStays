import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace FAQ header
html = re.sub(
    r'<div class="section-eyebrow">FAQ</div>\s*<h2 class="section-title">Got Questions\?<br /><em>We.*?Answers</em></h2>',
    r'<div class="section-eyebrow text-center">SUPPORT & GUIDANCE</div>\n                <h2 class="section-title text-center">Frequently<br>Asked Questions</h2>',
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("FAQ header modified.")
