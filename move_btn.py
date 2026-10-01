import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the existing button desktop-only
html = html.replace('class="hero-btn-pill"', 'class="hero-btn-pill desktop-explore-btn"')

# Add the new button to the giant title
new_title = '''<div class="hero-giant-title">DISCOVER<br>INDIA
                    <div style="text-align: center; margin-top: 2vh;">
                        <a href="#destinations" class="hero-btn-pill mobile-explore-btn">Explore Now</a>
                    </div>
                </div>'''
html = re.sub(r'<div class="hero-giant-title">DISCOVER<br>INDIA</div>', new_title, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now add CSS
with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

css += '''
/* --- MOBILE EXPLORE BUTTON FIX --- */
.mobile-explore-btn { display: none !important; }

@media (max-width: 768px) {
    .desktop-explore-btn { display: none !important; }
    .mobile-explore-btn { 
        display: inline-block !important; 
        font-size: 1.1rem !important;
        letter-spacing: 1px !important;
        padding: 12px 28px !important;
        font-family: var(--font-body) !important;
    }
}
'''

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Cache bump
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=25', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
