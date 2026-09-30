import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_func = '''    function updateHeroImages() {
        const isMobile = window.innerWidth <= 768;
        slides.forEach(slide => {
            const url = isMobile ? slide.dataset.mobile : slide.dataset.desktop;
            if (url) slide.style.backgroundImage = "url('" + url + "')";
        });
    }'''

new_func = '''    function updateHeroImages() {
        const isMobile = window.innerWidth <= 768;
        slides.forEach(slide => {
            const url = isMobile ? slide.dataset.mobile : slide.dataset.desktop;
            if (url) {
                const bgStr = "url(\\"" + url + "\\")";
                // Only update if it actually changed to prevent paint thrashing
                if (slide.style.backgroundImage !== bgStr) {
                    slide.style.backgroundImage = bgStr;
                }
            }
        });
    }'''

text = text.replace(old_func, new_func)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
