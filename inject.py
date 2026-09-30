import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open('block_to_inject.js', 'r', encoding='utf-8') as f:
    block = f.read()

# Remove the commented out Testimonials header at the bottom of the block
block = re.sub(r'// /\*.*TESTIMONIALS.*', '', block, flags=re.DOTALL)

js = js.replace('function initTestimonials() {', block + '\nfunction initTestimonials() {')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
