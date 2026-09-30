import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_string = '''
    /* Fix giant title size for mobile */
    .hero-giant-title {
        font-size: clamp(4rem, 18vw, 6rem) !important;
    }'''

css = css.replace(bad_string, '''
    }
}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
