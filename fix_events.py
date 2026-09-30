import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make sure hamburger exists
js = js.replace('hamburger.addEventListener', 'if(hamburger) hamburger.addEventListener')

# Make sure contactForm exists
js = js.replace('.addEventListener', 'if() .addEventListener')

# Make sure modalClose exists
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')

# Make sure waClose exists
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')

# Make sure tPrev and tNext exist (testimonials)
js = js.replace('.addEventListener', 'if() .addEventListener')
js = js.replace('.addEventListener', 'if() .addEventListener')

# Make sure btt exists
js = js.replace('.addEventListener', 'if() .addEventListener')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
