import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Pattern for the old JS logic we want to update
old_js = r'''
                    </div>
                    <button class="pkg-route-btn" onclick="openModal\('\${pkg.id}', '\${pkg.placeName}'\)">View Details ↗</button>
                </div>
'''

new_js = r'''
                    </div>
                </div>
'''

js = re.sub(old_js.strip(), new_js.strip(), js)

# Now we need to add the slide indicators and auto-slide logic to renderModernPackages
old_end = r'''
        slider.appendChild(card);
    });
}
'''

new_end = r'''
        slider.appendChild(card);
    });
    
    // Add slide indicators
    const container = slider.parentElement;
    let dotsContainer = document.getElementById('pkgSliderDots');
    if (!dotsContainer) {
        dotsContainer = document.createElement('div');
        dotsContainer.id = 'pkgSliderDots';
        dotsContainer.className = 'pkg-slider-indicators';
        container.appendChild(dotsContainer);
    }
    dotsContainer.innerHTML = '';
    
    allPackages.forEach((_, i) => {
        const dot = document.createElement('div');
        dot.className = `pkg-indicator ${i === 0 ? 'active' : ''}`;
        dot.onclick = () => {
            const cardWidth = slider.querySelector('.pkg-card').offsetWidth + 24;
            slider.scrollTo({ left: i * cardWidth, behavior: 'smooth' });
        };
        dotsContainer.appendChild(dot);
    });
    
    // Update active dot on scroll
    slider.addEventListener('scroll', () => {
        const cardWidth = slider.querySelector('.pkg-card').offsetWidth + 24;
        const activeIdx = Math.round(slider.scrollLeft / cardWidth);
        document.querySelectorAll('.pkg-indicator').forEach((dot, i) => {
            dot.classList.toggle('active', i === activeIdx);
        });
    });
    
    // Auto slide
    if (window.packageAutoSlide) clearInterval(window.packageAutoSlide);
    window.packageAutoSlide = setInterval(() => {
        const cardWidth = slider.querySelector('.pkg-card').offsetWidth + 24;
        const maxScroll = slider.scrollWidth - slider.clientWidth;
        
        if (slider.scrollLeft >= maxScroll - 10) {
            slider.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
            slider.scrollBy({ left: cardWidth, behavior: 'smooth' });
        }
    }, 3000);
}
'''

js = js.replace(old_end.strip(), new_end.strip())

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
