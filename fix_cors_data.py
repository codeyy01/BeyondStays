import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<script src="script.js', '<script src="data.js?v=1"></script>\n    <script src="script.js')
# Update cache buster for script.js just in case
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=9991', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated with data.js!')

# Now update script.js to use localTravelData instead of fetch
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the fetchData function
js = js.replace('''async function fetchData() {
    try {
        const res = await fetch('data.json?v=' + new Date().getTime());
        if (!res.ok) throw new Error();
        travelData = await res.json();
    } catch {
        travelData = getFallbackData();
    }
    renderModernPackages();
}''', '''async function fetchData() {
    if (typeof localTravelData !== "undefined") {
        travelData = localTravelData;
    } else {
        travelData = getFallbackData();
    }
    renderModernPackages();
}''')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('script.js updated to use local data!')
