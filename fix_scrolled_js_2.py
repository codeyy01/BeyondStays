import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_js = '''
window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;
    
    document.querySelectorAll('.nav-piece').forEach(piece => {
        piece.classList.toggle('hidden', scrolled);
    });
    
    const stickyNav = document.getElementById('navbar-scrolled');
    if (stickyNav) {
        stickyNav.classList.toggle('visible', scrolled);
    }
'''

js = re.sub(r'window\.addEventListener\(''scroll'', \(\) => \{.*?\}\);', new_js, js, flags=re.DOTALL, count=1)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
