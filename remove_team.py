import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to match the specific team section
pattern = r'<section class="section">\s*<div class="container">\s*<!-- HEADER -->\s*<div class="team-header reveal-up">\s*<div class="section-eyebrow">The Brain Behind It</div>.*?</section>'

# Replace it using regex with DOTALL to match across newlines
html_cleaned = re.sub(pattern, '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_cleaned)
