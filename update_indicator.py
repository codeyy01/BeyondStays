import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_logic = r"const updateIndicator = \(\) => \{.*?indicator\.style\.transform = `scaleX.*?\}\;"

new_logic = '''const updateIndicator = () => {
            if (maxScroll <= 0) {
                indicator.style.transform = 'translateX(0)';
                return;
            }
            const scrollPercentage = (slider.scrollLeft / maxScroll);
            indicator.style.transform = `translateX(${scrollPercentage * 300}%)`;
        };'''

js = re.sub(old_logic, new_logic, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'\.pkg-indicator-bar\s*{[^}]*}', '''.pkg-indicator-bar {
    position: absolute;
    top: 0; left: 0; height: 100%;
    width: 25%;
    background: var(--green);
    border-radius: 6px;
    will-change: transform;
    transform: translateX(0);
    transition: transform 0.1s ease-out;
}''', css)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=10004', html)
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=21', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
