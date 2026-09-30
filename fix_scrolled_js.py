import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the scroll toggle logic
new_js = '''
window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;
    
    // Toggle hidden on initial pieces
    document.querySelectorAll('.nav-piece').forEach(piece => {
        piece.classList.toggle('hidden', scrolled);
    });
    
    // Toggle visible on new sticky navbar
    const stickyNav = document.getElementById('navbar-scrolled');
    if (stickyNav) {
        stickyNav.classList.toggle('visible', scrolled);
    }
'''

js = re.sub(r'window\.addEventListener\(''scroll'', \(\) => \{.*?piece\.classList\.toggle\(''scrolled'', scrolled\);\s*\}\);', new_js, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS updated.")
