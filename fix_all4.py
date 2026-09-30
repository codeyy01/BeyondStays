import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('''        -webkit-backdrop-filter: blur(16px) !important;
    }

    }
}
@media (max-width: 768px) {''', '''        -webkit-backdrop-filter: blur(16px) !important;
    }
}
@media (max-width: 768px) {''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
