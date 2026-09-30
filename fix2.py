import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

garbage = '''});

    function goSlide(idx) {
        slides[heroIdx].classList.remove('active');
        dotsWrap.children[heroIdx].classList.remove('active');
        heroIdx = (idx + slides.length) % slides.length;
        slides[heroIdx].classList.add('active');
        dotsWrap.children[heroIdx].classList.add('active');
    }

    heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500);
}'''

text = text.replace(garbage, '}')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
