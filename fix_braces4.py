import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('''scale(1)
    }
    50% {
        opacity: 0.5;
        transform: scale(1.4)

    }
}
}.hero-title {''', '''scale(1);
    }
    50% {
        opacity: 0.5;
        transform: scale(1.4);
    }
}
.hero-title {''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
