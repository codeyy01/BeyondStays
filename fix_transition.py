import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_slide = '''.hero-slide {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    opacity: 0;
    backface-visibility: hidden;
    perspective: 1000px;
}
.hero-slide.active { opacity: 1; }'''

good_slide = '''.hero-slide {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 1.2s ease-in-out;
    backface-visibility: hidden;
    perspective: 1000px;
}
.hero-slide.active { opacity: 1; }'''

css = css.replace(bad_slide, good_slide)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
