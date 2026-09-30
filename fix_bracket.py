import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_css = '''        -webkit-backdrop-filter: blur(16px) !important;

    /* Fix giant title size for mobile */'''

good_css = '''        -webkit-backdrop-filter: blur(16px) !important;
    }

    /* Fix giant title size for mobile */'''

css = css.replace(bad_css, good_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
