import re

# 1. Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacements
replacements = {
    "Unwind with exclusive private pool villas in Wayanad.": "Exclusive private pool villas.",
    "Create unforgettable memories with your loved ones.": "Memories with loved ones.",
    "Fuel your spirit with guided trekking experiences.": "Guided trekking experiences.",
    "Discover paradise with intimate, breathtaking stays.": "Intimate, breathtaking stays.",
    "Experience the tranquil charm of Kerala's backwaters.": "Tranquil Kerala backwaters."
}

for old, new in replacements.items():
    html = html.replace(old, new)

html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=8', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update CSS
with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('height: 180px;\n        border-radius: 90px;', 'height: 130px;\n        border-radius: 70px;')
css = css.replace('border-radius: 90px;\n        box-shadow', 'border-radius: 70px;\n        box-shadow')
css = css.replace('padding: 0 20px;', 'padding: 0 16px;')

# Add bulletproof text clamping to prevent overflow
if '-webkit-line-clamp' not in css:
    css = css.replace(
        '''.mobile-pill-text p {
        font-size: 0.75rem;''',
        '''.mobile-pill-text p {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
        font-size: 0.75rem;'''
    )
    
    css = css.replace(
        '''.mobile-pill-text h4 {
        font-family: var(--font-display);''',
        '''.mobile-pill-text h4 {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
        font-family: var(--font-display);'''
    )

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Shortened descriptions and reduced pill heights!")
