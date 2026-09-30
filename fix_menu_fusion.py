import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make the hamburger also toggle a class on the navbar
old_burger = '''hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
});'''

new_burger = '''hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    if (navbar) navbar.classList.toggle('menu-open');
});'''

js = js.replace(old_burger, new_burger)

# Also remove 'menu-open' when clicking a link
old_link = '''document.querySelectorAll('.mm-link').forEach(link => {
    link.addEventListener('click', () => mobileMenu.classList.remove('open'));
});'''

new_link = '''document.querySelectorAll('.mm-link').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        if (navbar) navbar.classList.remove('menu-open');
    });
});'''

js = js.replace(old_link, new_link)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
