import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

click_outside_js = '''
// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (mobileMenu.classList.contains('open')) {
        const clickedInsideNav = navbar && navbar.contains(e.target);
        const clickedInsideMenu = mobileMenu.contains(e.target);
        
        if (!clickedInsideNav && !clickedInsideMenu) {
            mobileMenu.classList.remove('open');
            if (navbar) navbar.classList.remove('menu-open');
        }
    }
});
'''

if 'clickedInsideNav' not in js:
    js += click_outside_js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
