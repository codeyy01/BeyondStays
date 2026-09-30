import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_scroll = '''document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) {
            e.preventDefault();
            const y = target.getBoundingClientRect().top + window.scrollY - 72;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    });
});'''

new_scroll = '''document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const href = a.getAttribute('href');
        if (href === '#') {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
            return;
        }
        
        try {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const y = target.getBoundingClientRect().top + window.scrollY - 72;
                window.scrollTo({ top: y, behavior: 'smooth' });
            }
        } catch (err) {
            // Ignore invalid selectors like #! or just #
        }
    });
});'''

text = text.replace(old_scroll, new_scroll)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
