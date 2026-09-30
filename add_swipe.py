import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add touch swipe logic to the hero slider
swipe_js = '''
    // Touch swipe logic for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    const heroSlides = document.getElementById('heroSlides');
    if (heroSlides) {
        heroSlides.addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
        }, {passive: true});
        
        heroSlides.addEventListener('touchend', e => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }, {passive: true});
    }

    function handleSwipe() {
        if (touchEndX < touchStartX - 50) {
            goSlide(heroIdx + 1); // Swipe left -> next
        }
        if (touchEndX > touchStartX + 50) {
            goSlide(heroIdx - 1); // Swipe right -> prev
        }
    }
'''

# Find the end of initHero() function
# It ends with: heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500); }
old_end = '''heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500);
}'''
new_end = '''heroTimer = setInterval(() => goSlide(heroIdx + 1), 5500);
''' + swipe_js + '''
}'''

js = js.replace(old_end, new_end)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
