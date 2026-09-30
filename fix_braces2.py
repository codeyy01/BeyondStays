import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix fillBar
css = css.replace('''@keyframes fillBar {
    to {
        width: 100%;

    }
}
}''', '''@keyframes fillBar {
    to {
        width: 100%;
    }
}''')

# Fix fadeSlideUp
css = css.replace('''@keyframes fadeSlideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);

    }
}
}''', '''@keyframes fadeSlideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
