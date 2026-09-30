with open('style.css', 'a', encoding='utf-8') as f:
    with open('about_desktop.css', 'r', encoding='utf-8') as css:
        f.write('\n' + css.read())
