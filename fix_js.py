import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('if (slider && pkgModal) {', 'const modalSlider = document.getElementById("packagesSlider");\n    if (modalSlider && pkgModal) {')
js = js.replace("slider.addEventListener('click',", "modalSlider.addEventListener('click',")
js = js.replace("Array.from(slider.children)", "Array.from(modalSlider.children)")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=9998', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
