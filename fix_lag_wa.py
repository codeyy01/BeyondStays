import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update the heart to an angled arrow and make it a WhatsApp link
old_heart = """<div class="pkg-heart">
                        <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                    </div>"""
new_wa_link = """<a href="https://wa.me/919999999999?text=${encodeURIComponent('Hi Beyondstays! I am interested in the ' + pkg.name + ' package at ' + pkg.placeName + '. Can you share more details?')}" target="_blank" class="pkg-arrow-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
                    </a>"""
js = js.replace(old_heart, new_wa_link)

# 2. Fix the scroll thrashing in updateIndicator
old_scroll_logic_pattern = r'const updateIndicator = \(\) => \{.*?setTimeout\(updateIndicator, 200\);\s*\}'

new_scroll_logic = """
        let maxScroll = slider.scrollWidth - slider.clientWidth;
        let minWidth = (slider.clientWidth / slider.scrollWidth) * 100;

        const updateIndicator = () => {
            if (maxScroll <= 0) {
                indicator.style.width = '100%';
                return;
            }
            const scrollPercentage = (slider.scrollLeft / maxScroll);
            const availableWidth = 100 - minWidth;
            indicator.style.width = (minWidth + (scrollPercentage * availableWidth)) + '%';
        };

        window.addEventListener('resize', () => {
            maxScroll = slider.scrollWidth - slider.clientWidth;
            minWidth = (slider.clientWidth / slider.scrollWidth) * 100;
            updateIndicator();
        });

        let isTicking = false;
        slider.addEventListener('scroll', () => {
            if (!isTicking) {
                window.requestAnimationFrame(() => {
                    updateIndicator();
                    isTicking = false;
                });
                isTicking = true;
            }
        }, { passive: true });
        
        setTimeout(() => {
            maxScroll = slider.scrollWidth - slider.clientWidth;
            minWidth = (slider.clientWidth / slider.scrollWidth) * 100;
            updateIndicator();
        }, 500);
    }"""

js = re.sub(old_scroll_logic_pattern, new_scroll_logic, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated script.js successfully!")
