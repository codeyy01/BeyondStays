import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('slides[heroIdx].classList.remove(\'active\');', 'console.log("goSlide called! old idx:", heroIdx, "new idx:", (idx + slides.length) % slides.length); slides[heroIdx].classList.remove(\'active\');')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
