import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('function initHero() {')
end_idx = text.find('}', start_idx + 100) + 1

new_text = '''function initHero() {
    const slides = document.querySelectorAll('.hero-slide');
    const prev = document.getElementById('heroPrev');
    const next = document.getElementById('heroNext');
    if (!slides.length) return;
    function updateHeroImages() {
        const isMobile = window.innerWidth <= 768;
        slides.forEach(slide => {
            const url = isMobile ? slide.dataset.mobile : slide.dataset.desktop;
            if (url) slide.style.backgroundImage = "url('" + url + "')";
        });
    }
    updateHeroImages();
    window.addEventListener('resize', updateHeroImages);
    function goSlide(idx) {
        slides[heroIdx].classList.remove('active');
        heroIdx = (idx + slides.length) % slides.length;
        slides[heroIdx].classList.add('active');
        clearInterval(heroTimer);
        heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500);
    }
    if (prev && next) {
        prev.addEventListener('click', () => goSlide(heroIdx - 1));
        next.addEventListener('click', () => goSlide(heroIdx + 1));
    }
    heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500);
}'''

if start_idx != -1:
    text = text[:start_idx] + new_text + text[end_idx:]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(text)
