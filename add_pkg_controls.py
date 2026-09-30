import re

# 1. Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html_block = '''            <!-- Modern Slider -->
            <div class="packages-slider-container">
                <button class="pkg-arrow pkg-prev" id="pkgPrev"><svg viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg></button>
                <button class="pkg-arrow pkg-next" id="pkgNext"><svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg></button>
                
                <div class="packages-slider" id="packagesSlider">
                    <!-- Packages will be injected here via JS -->
                </div>
                
                <!-- Slide Indicator -->
                <div class="pkg-indicator-wrap">
                    <div class="pkg-indicator">
                        <div class="pkg-indicator-bar" id="pkgIndicatorBar"></div>
                    </div>
                </div>
            </div>'''

# Replace the old container
old_html_regex = r'<!-- Modern Slider -->\s*<div class="packages-slider-container">\s*<div class="packages-slider" id="packagesSlider">\s*<!-- Packages will be injected here via JS -->\s*</div>\s*</div>'
html = re.sub(old_html_regex, new_html_block, html)

html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=11', html)
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=9995', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update CSS
css_additions = '''
/* =========================================
   PACKAGES ARROWS AND INDICATORS
   ========================================= */
.pkg-arrow {
    position: absolute;
    top: calc(50% - 20px);
    transform: translateY(-50%);
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: #fff;
    border: none;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    cursor: pointer;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s;
}
.pkg-arrow:hover {
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}
.pkg-arrow svg {
    width: 28px;
    height: 28px;
    fill: #111;
}
.pkg-prev { left: 24px; }
.pkg-next { right: 24px; }

/* Hide arrows on mobile */
@media (max-width: 768px) {
    .pkg-arrow { display: none; }
}

.pkg-indicator-wrap {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 20px;
}
.pkg-indicator {
    width: 240px;
    height: 6px;
    background: rgba(0,0,0,0.08);
    border-radius: 6px;
    position: relative;
    overflow: hidden;
}
.pkg-indicator-bar {
    position: absolute;
    top: 0; left: 0; height: 100%;
    width: 15%; /* Default */
    background: #5b6c4b; /* Dark Green */
    border-radius: 6px;
    transition: width 0.15s ease-out;
}
'''

with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_additions + '\n')


# 3. Update JS
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_addition = '''
    // Setup Arrows and Slide Indicator
    const prevBtn = document.getElementById('pkgPrev');
    const nextBtn = document.getElementById('pkgNext');
    const indicator = document.getElementById('pkgIndicatorBar');

    if (prevBtn && nextBtn && slider) {
        prevBtn.addEventListener('click', () => {
            const card = slider.querySelector('.pkg-card');
            if(card) {
                const cardWidth = card.offsetWidth + 32;
                slider.scrollBy({ left: -cardWidth, behavior: 'smooth' });
            }
        });
        nextBtn.addEventListener('click', () => {
            const card = slider.querySelector('.pkg-card');
            if(card) {
                const cardWidth = card.offsetWidth + 32;
                slider.scrollBy({ left: cardWidth, behavior: 'smooth' });
            }
        });
    }

    if (slider && indicator) {
        const updateIndicator = () => {
            const maxScroll = slider.scrollWidth - slider.clientWidth;
            if (maxScroll <= 0) {
                indicator.style.width = '100%';
                return;
            }
            // Ensure width is at least something visible
            const minWidth = (slider.clientWidth / slider.scrollWidth) * 100;
            const scrollPercentage = (slider.scrollLeft / maxScroll);
            const availableWidth = 100 - minWidth;
            indicator.style.width = (minWidth + (scrollPercentage * availableWidth)) + '%';
        };
        slider.addEventListener('scroll', updateIndicator);
        window.addEventListener('resize', updateIndicator);
        setTimeout(updateIndicator, 200);
    }
'''

# Find the end of renderModernPackages and inject this before the closing brace
render_func_regex = r'(function renderModernPackages\(\) \{.*?\n        slider\.appendChild\(card\);\n    \}\);)(?=\n\})'
js = re.sub(render_func_regex, r'\1\n' + js_addition, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Added arrows and slide indicator successfully!")
