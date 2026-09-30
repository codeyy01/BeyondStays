import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_scroll = '''window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;

    if (navbar) {
        navbar.classList.toggle('scrolled', scrolled);
    }'''

new_scroll = '''window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;

    if (navbar) {
        navbar.classList.toggle('scrolled', scrolled);
        if (scrolled) {
            navbar.classList.remove('cutout-mode');
        } else {
            navbar.classList.add('cutout-mode');
        }
    }'''

text = text.replace(old_scroll, new_scroll)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
