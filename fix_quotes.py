with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(r"\'${pkg.placeName}\'", "'${pkg.placeName}'")
js = js.replace(r"\'${pkg.name}\'", "'${pkg.name}'")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
