import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_js = '''
const navPieces = document.querySelectorAll('.nav-piece');
const navLogo = document.querySelector('#navLogo');
let lastLogo = '';

window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;
    
    navPieces.forEach(piece => {
        piece.classList.toggle('scrolled', scrolled);
    });
'''

# Use raw string and exact match
js = re.sub(r'const navbar = \$\(\'navbar\'\);.*?(?=    if \(\$\(\'btt\'\)\))', new_js + '\n', js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
