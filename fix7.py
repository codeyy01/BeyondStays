with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('const newSrc = scrolled ? "./assets/nav-logo-green.png" : "./assets/nav-logo-white.png";', 'const newSrc = "./assets/nav-logo-green.png";')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
