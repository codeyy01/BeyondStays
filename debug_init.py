import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add a massive console log right before goSlide is attached
debug_js = '''
    console.log("INIT HERO FINISHED. ATTACHING EVENTS!");
    if (prev && next) {
'''

js = js.replace('if (prev && next) {', debug_js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
