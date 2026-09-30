import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix ReferenceError (i to index)
js = js.replace('openModal(${i})', 'openModal(${index})')

# Bind window.allPackagesData
# Insert right after `let allPackages = [];`
# Actually, it's safer to just do window.allPackagesData = allPackages right before the forEach loop.
js = js.replace('allPackages.forEach((pkg, index) => {', 'window.allPackagesData = allPackages;\n    allPackages.forEach((pkg, index) => {')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
