import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_controls = '''
<div class="testi-controls">
    <button class="testi-btn" id="tPrev">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    </button>
    <div class="testi-dots" id="testiDots"></div>
    <button class="testi-btn" id="tNext">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    </button>
</div>
'''

html = re.sub(r'<div class="testi-controls">.*?</div>\s*</div>', new_controls + '\n              </div>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML modified for testimonial buttons.")
