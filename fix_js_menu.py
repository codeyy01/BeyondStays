import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the hamburger toggle logic to toggle menu-open on navbar-scrolled
new_js = '''
// Hamburger
const hamburgers = document.querySelectorAll('.hamburger');
const mobileMenu = document.getElementById('mobileMenu');
const stickyNavOverlay = document.getElementById('navbar-scrolled');
hamburgers.forEach(btn => {
    btn.addEventListener('click', () => {
        if(mobileMenu) mobileMenu.classList.toggle('open');
        btn.classList.toggle('active');
        if(stickyNavOverlay) stickyNavOverlay.classList.toggle('menu-open');
    });
});
'''

js = re.sub(r'// Hamburger.*?\}\);.*?\}\);', new_js, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("JS updated for mobile menu.")
