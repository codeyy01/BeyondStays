import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_slide = '''.hero-slide {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 0.8s ease-in-out;
}'''

new_slide = '''.hero-slide {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 0.8s ease-in-out;
    will-change: opacity;
    transform: translateZ(0);
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    perspective: 1000px;
}'''
css = css.replace(old_slide, new_slide)

if new_slide not in css:
    css = re.sub(r'\.hero-slide\s*\{[^}]*\}', new_slide, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
