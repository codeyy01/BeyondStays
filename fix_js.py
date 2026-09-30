import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace navbar scroll logic
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

js = re.sub(r'const navbar = \$\(''navbar''\);.*?window\.addEventListener\(''scroll'', \(\) => \{.*?if \(navbar\) \{.*?\}\n', new_js, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS updated.")
