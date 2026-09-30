import re

with open('data.js', 'r', encoding='utf-8') as f:
    djs = f.read()
djs = djs.replace('const localTravelData', 'window.localTravelData')
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(djs)

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()
js = js.replace('typeof localTravelData !== "undefined"', 'typeof window.localTravelData !== "undefined"')
js = js.replace('travelData = localTravelData', 'travelData = window.localTravelData')
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('class="packages-slider-container reveal-up"', 'class="packages-slider-container"')
html = re.sub(r'data\.js\?v=[0-9]+', 'data.js?v=4', html)
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=9994', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fixed reveal-up and local data!')
