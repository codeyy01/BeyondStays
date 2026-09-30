import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('''    to {
        transform: scale(1)

    }
}
}.hero-overlay {''', '''    to {
        transform: scale(1);
    }
}
.hero-overlay {''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
