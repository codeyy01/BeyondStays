import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_logo_cont = '''.nav-logo-container {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    top: 0;
    height: 100%;
}'''

new_logo_cont = '''.nav-logo-container {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    top: 0;
    height: 100%;
    transition: all 0.4s ease;
}'''

css = css.replace(old_logo_cont, new_logo_cont)
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
