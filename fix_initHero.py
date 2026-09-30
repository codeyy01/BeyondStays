import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the entire initHero function
new_initHero = '''function initHero() {
    const slides = document.querySelectorAll('#heroSlides .hero-slide');
    const prev = document.getElementById('heroPrev');
    const next = document.getElementById('heroNext');
    if (!slides || slides.length === 0) return;
    
    let lastIsMobile = null;
    function updateHeroImages() {
        const isMobile = window.innerWidth <= 768;
        if (lastIsMobile === isMobile) return;
        lastIsMobile = isMobile;
        
        slides.forEach(slide => {
            const url = isMobile ? slide.getAttribute('data-mobile') : slide.getAttribute('data-desktop');
            if (url) {
                slide.style.backgroundImage = 'url("' + url + '")';
            }
        });
    }
    updateHeroImages();
    window.addEventListener('resize', updateHeroImages);
    
    function goSlide(idx) {
        slides[heroIdx].classList.remove('active');
        heroIdx = (idx + slides.length) % slides.length;
        slides[heroIdx].classList.add('active');
        
        if (heroTimer) clearInterval(heroTimer);
        heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500);
    }
    
    if (prev && next) {
        prev.addEventListener('click', (e) => { e.preventDefault(); goSlide(heroIdx - 1); });
        next.addEventListener('click', (e) => { e.preventDefault(); goSlide(heroIdx + 1); });
    }
    
    if (heroTimer) clearInterval(heroTimer);
    heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500);

    // Touch swipe logic for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    const heroSlidesWrap = document.getElementById('heroSlides');
    if (heroSlidesWrap) {
        heroSlidesWrap.addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
        }, {passive: true});
        
        heroSlidesWrap.addEventListener('touchend', e => {
            touchEndX = e.changedTouches[0].screenX;
            if (touchEndX < touchStartX - 50) goSlide(heroIdx + 1);
            if (touchEndX > touchStartX + 50) goSlide(heroIdx - 1);
        }, {passive: true});
    }
}'''

js = re.sub(r'function initHero\(\)\s*\{[\s\S]*?(?=\nfunction initTestimonials)', new_initHero + '\n\n', js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
