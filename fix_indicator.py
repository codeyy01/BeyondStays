import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace indicator.style.width = ... with indicator.style.transform = scaleX(...)
old_width_logic = r"indicator\.style\.width = \(minWidth \+ \(scrollPercentage \* availableWidth\)\) \+ '%';"
new_transform_logic = "indicator.style.transform = `scaleX(${(minWidth + (scrollPercentage * availableWidth)) / 100})`;"
js = re.sub(old_width_logic, new_transform_logic, js)

js = js.replace("indicator.style.width = '100%';", "indicator.style.transform = 'scaleX(1)';")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('width: 15%; /* Default */', 'width: 100%; transform-origin: left; transform: scaleX(0.15); will-change: transform;')
css = css.replace('transition: width 0.15s ease-out;', 'transition: transform 0.1s ease-out;')

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=10002', html)
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=19', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
