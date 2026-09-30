import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the single hamburger logic with querySelectorAll
new_js = '''
// Hamburger
const hamburgers = document.querySelectorAll('.hamburger');
const mobileMenu = mobileMenu;
hamburgers.forEach(btn => {
    btn.addEventListener('click', () => {
        mobileMenu.classList.toggle('open');
        btn.classList.toggle('active');
    });
});
'''

js = re.sub(r'// Hamburger.*?\}\);', new_js, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("JS modified.")
