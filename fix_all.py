import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_injection = '''
    /* Fix giant title size for mobile */
    .hero-giant-title {
        font-size: clamp(4rem, 18vw, 6rem) !important;
    }
}'''

# Replace all occurrences of bad_injection with a simple closing bracket }
css = css.replace(bad_injection, '''}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
