with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('slider.appendChild(card);\n    });')
if idx != -1:
    # 34 is the length of 'slider.appendChild(card);\n    });'
    injection_point = idx + 34
    
    addition = """
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
            const minWidth = (slider.clientWidth / slider.scrollWidth) * 100;
            const scrollPercentage = (slider.scrollLeft / maxScroll);
            const availableWidth = 100 - minWidth;
            indicator.style.width = (minWidth + (scrollPercentage * availableWidth)) + '%';
        };
        slider.addEventListener('scroll', updateIndicator);
        window.addEventListener('resize', updateIndicator);
        setTimeout(updateIndicator, 200);
    }
"""
    js = js[:injection_point] + addition + js[injection_point:]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("JS injected!")
else:
    print("Could not find injection point.")
