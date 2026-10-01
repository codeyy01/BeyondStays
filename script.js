/* ===== Beyondstays — script.js ===== */
'use strict';

/* ── State ── */
let travelData = [];
let activePlace = null;
let activeRegion = 'All';
let carouselImages = [];
let currentCarouselIdx = 0;
let heroIdx = 0;
let heroTimer = null;
let testiIdx = 0;
let faqData = [];

/* ── Helpers ── */
const $ = id => document.getElementById(id);
const el = (tag, cls) => { const e = document.createElement(tag); if (cls) e.className = cls; return e; };

/* ══════════════════════════════════════
   LOADER
══════════════════════════════════════ */
window.addEventListener('load', () => {
    setTimeout(() => {
        loader.classList.add('done');
        document.body.classList.remove('loading');
        document.body.style.overflow = '';
        // Restart auto-slide
        if (window.packageAutoSlide) clearInterval(window.packageAutoSlide);
        const slider = document.getElementById('packagesSlider');
        if (slider) {
            window.packageAutoSlide = setInterval(() => {
                const card = slider.querySelector('.pkg-card');
                if (!card) return;
                const cardWidth = card.offsetWidth + 24;
                const maxScroll = slider.scrollWidth - slider.clientWidth;
                if (slider.scrollLeft >= maxScroll - 10) {
                    slider.scrollTo({ left: 0, behavior: 'smooth' });
                } else {
                    slider.scrollBy({ left: cardWidth, behavior: 'smooth' });
                }
            }, 6000);
        }
        document.documentElement.style.overflow = '';
    }, 2400);
});
document.body.style.overflow = 'hidden';
document.documentElement.style.overflow = 'hidden';

if (!window.requestIdleCallback) {
  window.requestIdleCallback = function (cb) {
    return setTimeout(() => {
      cb({
        didTimeout: false,
        timeRemaining: function () {
          return 0;
        },
      });
    }, 1);
  };
}

if (!window.cancelIdleCallback) {
  window.cancelIdleCallback = function (id) {
    clearTimeout(id);
  };
}

function fetchFAQ() {
    faqData = [
      {
        "question": "How do I book a trip?",
        "answer": "You can explore packages and click 'Book Now' to connect with us on WhatsApp. Our team will assist you with the complete booking process."
      },
      {
        "question": "Can I customize my travel package?",
        "answer": "Yes, all our packages can be customized based on your preferences, budget, and travel dates."
      },
      {
        "question": "What payment methods do you accept?",
        "answer": "We accept UPI, bank transfer, and other secure payment methods. Details will be shared during booking."
      },
      {
        "question": "Do you provide group discounts?",
        "answer": "Yes, we offer special discounts for group bookings. Contact us for details."
      }
    ];
    renderFAQ();
}

/* ══════════════════════════════════════
   NAVBAR
══════════════════════════════════════ */

const navPieces = document.querySelectorAll('.nav-piece');
const navLogo = document.querySelector('#navLogo');
let lastLogo = '';

window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;
    
    document.querySelectorAll('.nav-piece').forEach(piece => {
        piece.classList.toggle('hidden', scrolled);
    });
    
    const stickyNav = document.getElementById('navbar-scrolled');
    if (stickyNav) {
        stickyNav.classList.toggle('visible', scrolled);
    }

    if ($('btt')) {
        $('btt').classList.toggle('hidden', window.scrollY < 400);
    }

    if (!navLogo) return;

    // Verified: Logo remains green in both states based on the new design.
    const newSrc = "./assets/nav-logo-green.png";

    if (lastLogo !== newSrc) {
        navLogo.src = newSrc;
        lastLogo = newSrc;
    }
});



// Hamburger
const hamburgers = document.querySelectorAll('.hamburger');
const mobileMenu = document.getElementById('mobileMenu');
const stickyNavOverlay = document.getElementById('navbar-scrolled');
hamburgers.forEach(btn => {
    btn.addEventListener('click', () => {
        if(mobileMenu) mobileMenu.classList.toggle('open');
        btn.classList.toggle('active');
        if(stickyNavOverlay) stickyNavOverlay.classList.toggle('menu-open');
    });
});


document.querySelectorAll('.mm-link').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        const sno = document.getElementById('navbar-scrolled'); if (sno) sno.classList.remove('menu-open');
    });
});

/* ══════════════════════════════════════
   SMOOTH SCROLL
══════════════════════════════════════ */
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const href = a.getAttribute('href');
        if (href === '#') {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
            return;
        }
        
        try {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const y = target.getBoundingClientRect().top + window.scrollY - 72;
                window.scrollTo({ top: y, behavior: 'smooth' });
            }
        } catch (err) {
            // Ignore invalid selectors like #! or just #
        }
    });
});

/* ══════════════════════════════════════
   HERO SLIDESHOW
══════════════════════════════════════ */
function initHero() {
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
    
    
    console.log("INIT HERO FINISHED. ATTACHING EVENTS!");
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
}



/* SCROLL REVEAL */
function initReveal() {
    const obs = new IntersectionObserver(entries => {
        entries.forEach(en => {
            if (en.isIntersecting) {
                en.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right').forEach(el => obs.observe(el));
}

async function fetchData() {
    if (typeof window.localTravelData !== "undefined") {
        travelData = window.localTravelData;
    } else {
        travelData = getFallbackData();
    }
    renderModernPackages();
}

function getFallbackData() {
    return [
        {
            place: 'Munnar', region: 'Resorts', tagline: 'Tea Gardens & Misty Hills',
            coverImage: 'https://images.pexels.com/photos/32262519/pexels-photo-32262519.jpeg',
            packages: []
        },
        {
            place: 'Goa', region: 'Domestic', tagline: 'Beaches, Bikes & Chill Vibes',
            coverImage: 'https://images.pexels.com/photos/35916755/pexels-photo-35916755.jpeg',
            packages: [{
                id: 'g1', name: 'Goa Budget Escape', price: '₹3,999', duration: '3 Days / 2 Nights',
                description: 'Sun, sand and everything in between.',
                features: ['A/C Rooms', 'Bike Rental', 'Breakfast'],
                images: ['https://images.pexels.com/photos/1604287/pexels-photo-1604287.jpeg']
            }]
        }
    ];
}

/* ══════════════════════════════════════
   REGION FILTERS
══════════════════════════════════════ */
function buildRegionFilters() {
    const regions = ['All', ...new Set(travelData.map(d => d.region))];
    const wrap = $('regionFilters');
    wrap.innerHTML = '';
    regions.forEach(r => {
        const btn = el('button', 'region-btn' + (r === 'All' ? ' active' : ''));
        btn.textContent = r;
        btn.addEventListener('click', () => {
            activeRegion = r;
            wrap.querySelectorAll('.region-btn').forEach(b => b.classList.toggle('active', b.textContent === r));
            renderModernPackages();
            clearPackages();
        });
        wrap.appendChild(btn);
    });
}

/* ══════════════════════════════════════
   RENDER PLACES
══════════════════════════════════════ */

function renderModernPackages() {
    const slider = document.getElementById('packagesSlider');
    if (!slider) return;
    slider.innerHTML = '';
    
    // Flatten all packages
    let allPackages = [];
    travelData.forEach(placeObj => {
        if(placeObj.packages) {
            placeObj.packages.forEach(pkg => {
                allPackages.push({
                    ...pkg,
                    placeName: placeObj.place,
                    coverImage: placeObj.coverImage,
                    region: placeObj.region
                });
            });
        }
    });
    
    // If no packages, show message
    if (allPackages.length === 0) {
        slider.innerHTML = '<p style="color:#777; margin: auto;">No packages available.</p>';
        return;
    }
    
    // Generate cards
    window.allPackagesData = allPackages;
    allPackages.forEach((pkg, index) => {
        // Randomize rating and level slightly for aesthetic variety based on index
        const rating = (4.7 + (index % 4) * 0.1).toFixed(1);
        const levels = ['Easy Level', 'Moderate Level', 'Premium Level'];
        const levelClasses = ['easy', 'moderate', 'hard'];
        const levelIdx = index % 3;
        
        const card = document.createElement('div');
        card.className = 'pkg-card';
        card.innerHTML = `
            <img class="pkg-bg-img" src="${pkg.images && pkg.images.length > 0 ? pkg.images[0] : (pkg.coverImage || 'https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg')}" alt="${pkg.name}" loading="lazy">
            <div class="pkg-gradient"></div>
            
            <div class="pkg-content">
                <h3 class="pkg-title">${pkg.placeName}</h3>
                <div class="pkg-subtitle">${pkg.name}</div>
                
                <p class="pkg-desc">${pkg.description || 'Explore the breathtaking beauty of ' + pkg.placeName + ' with our highly exclusive and beautifully curated package.'}</p>
                <div class="pkg-read-more">Read more</div>
                
                <div class="pkg-tags">
                    <div class="pkg-tag">
                        <svg viewBox="0 0 24 24" fill="#fff"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.41l9 9c.36.36.86.58 1.41.58s1.05-.22 1.41-.59l7-7c.36-.36.59-.86.59-1.41s-.23-1.06-.59-1.41zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/></svg>
                        from ${pkg.price}
                    </div>
                    <div class="pkg-tag">
                        <svg viewBox="0 0 24 24" fill="#fff"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
                        ${pkg.duration}
                    </div>
                </div>
                
                <div class="pkg-action-row">
                    <a href="#" class="pkg-btn">View Package</a>
                    <a href="https://wa.me/919999999999?text=${encodeURIComponent('Hi Beyondstays! I am interested in the ' + pkg.name + ' package at ' + pkg.placeName + '. Can you share more details?')}" target="_blank" class="pkg-arrow-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg>
                    </a>
                </div>
            </div>
        `;
        slider.appendChild(card);
    });

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
    }
    
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
    }, 6000);
}



function openModal(index) {
    const pkg = window.allPackagesData[index];
    if (!pkg) return;
    
    // Stop auto-slide
    if (window.packageAutoSlide) {
        clearInterval(window.packageAutoSlide);
    }
    
    // Populate Modal
    const modalTitle = document.getElementById('modalTitle');
    const modalBadges = document.getElementById('modalBadges');
    const modalMeta = document.getElementById('modalMeta');
    const modalDesc = document.getElementById('modalDesc');
    const modalHighlights = document.getElementById('modalHighlights');
    const modalInclusions = document.getElementById('modalInclusions');
    const modalExclusions = document.getElementById('modalExclusions');
    const modalBookBtn = document.getElementById('modalBookBtn');
    
    modalTitle.textContent = pkg.name;
    
    modalBadges.innerHTML = `
        <span class="modal-badge-place">${pkg.placeName}</span>
        ${pkg.region === 'International' ? '<span class="modal-badge-pop">Popular</span>' : ''}
    `;
    
    modalMeta.innerHTML = `
        <span class="modal-meta-item">⏱️ ${pkg.duration}</span>
        <span class="modal-meta-item">💰 ${pkg.price}</span>
    `;
    
    // Description (handle bolding and newlines)
    let desc = pkg.description || '';
    desc = desc.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    desc = desc.replace(/\\n/g, '<br/>');
    modalDesc.innerHTML = desc;
    
    // Highlights
    if (pkg.highlights && pkg.highlights.length > 0) {
        document.getElementById('modalHighlightsSec').style.display = 'block';
        modalHighlights.innerHTML = pkg.highlights.map(h => `<li>${h}</li>`).join('');
    } else {
        document.getElementById('modalHighlightsSec').style.display = 'none';
    }
    
    // Inclusions
    if (pkg.inclusions && pkg.inclusions.length > 0) {
        document.getElementById('modalInclusionsSec').style.display = 'block';
        modalInclusions.innerHTML = pkg.inclusions.map(i => `<li>${i}</li>`).join('');
    } else {
        document.getElementById('modalInclusionsSec').style.display = 'none';
    }
    
    // Exclusions
    if (pkg.exclusions && pkg.exclusions.length > 0) {
        document.getElementById('modalExclusionsSec').style.display = 'block';
        modalExclusions.innerHTML = pkg.exclusions.map(e => `<li>${e}</li>`).join('');
    } else {
        document.getElementById('modalExclusionsSec').style.display = 'none';
    }
    
    // Book Btn Action
    modalBookBtn.onclick = () => {
        bookPackageWa(pkg.placeName, pkg.name);
    };
    
    // Show Modal
    const overlay = document.getElementById('modalOverlay');
    overlay.classList.remove('hidden');
    requestAnimationFrame(() => {
        overlay.classList.add('visible');
        document.body.style.overflow = 'hidden'; // prevent background scrolling
    });
}


function closeModal() {
    const overlay = $('modalOverlay');
    if (!overlay) return;
    overlay.classList.remove('visible');
    setTimeout(() => {
        overlay.classList.add('hidden');
        document.body.style.overflow = '';
        // Restart auto-slide
        if (window.packageAutoSlide) clearInterval(window.packageAutoSlide);
        const slider = document.getElementById('packagesSlider');
        if (slider) {
            window.packageAutoSlide = setInterval(() => {
                const card = slider.querySelector('.pkg-card');
                if (!card) return;
                const cardWidth = card.offsetWidth + 24;
                const maxScroll = slider.scrollWidth - slider.clientWidth;
                if (slider.scrollLeft >= maxScroll - 10) {
                    slider.scrollTo({ left: 0, behavior: 'smooth' });
                } else {
                    slider.scrollBy({ left: cardWidth, behavior: 'smooth' });
                }
            }, 6000);
        }
    }, 300);
}

if ($('modalClose')) $('modalClose').addEventListener('click', closeModal);
if ($('modalOverlay')) $('modalOverlay').addEventListener('click', e => { if (e.target === $('modalOverlay')) closeModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

/* ══════════════════════════════════════
   WHATSAPP HELPER & FAB
══════════════════════════════════════ */

function bookPackageWa(placeName, packageName) {
    const msg = `Hello Beyondstays, I would like to book a trip!

👤 Name: 
📍 Destination: ${placeName} (${packageName})
📅 Check-in Date: 
📅 Check-out Date: 
👥 Adults: 
🧒 Kids: 
🏕️ Group Type: 
🏨 No. of Rooms: 

Please share available packages and pricing.`;
    openWaPage(msg);
}

function openWaPage(message) {
    const phone = "917306023388";
    const msg = encodeURIComponent(message || '');
    window.open(`https://wa.me/${phone}?text=${msg}`, "_blank");
}
window.openWaPage = openWaPage;

if ($('waClose')) $('waClose').addEventListener('click', () => $('waPopup') && $('waPopup').classList.add('hidden'));
if ($('waPopup')) $('waPopup').addEventListener('click', e => { if (e.target === $('waPopup')) $('waPopup').classList.add('hidden'); });
if ($('waFab')) $('waFab').addEventListener('click', () => openWaPage('Hello! I would like to enquire about travel packages.'));

function initTestimonials() {
    const track = $('testiTrack');
    const cards = track.querySelectorAll('.testi-card');
    const dotsWrap = $('testiDots');
    const total = cards.length;

    function buildDots() {
        dotsWrap.innerHTML = '';
        for (let i = 0; i < total; i++) {
            const d = el('div', 'testi-dot' + (i === testiIdx ? ' active' : ''));
            d.addEventListener('click', () => goTesti(i));
            dotsWrap.appendChild(d);
        }
    }

    function goTesti(idx) {
        const visibleCards = window.innerWidth < 768 ? 1 : 2;
        const maxIndex = Math.max(0, total - visibleCards);

        testiIdx = Math.max(0, Math.min(idx, maxIndex));

        const cardW = cards[0].getBoundingClientRect().width + 24;

        track.style.transform = `translateX(-${testiIdx * cardW}px)`;

        dotsWrap.querySelectorAll('.testi-dot')
            .forEach((d, i) => d.classList.toggle('active', i === testiIdx));
    }

    tPrev.addEventListener('click', () => {
        const maxIndex = total - (window.innerWidth < 768 ? 1 : 2);
        goTesti(testiIdx > 0 ? testiIdx - 1 : maxIndex);
    });
    tNext.addEventListener('click', () => {
        const maxIndex = total - (window.innerWidth < 768 ? 1 : 2);
        goTesti(testiIdx < maxIndex ? testiIdx + 1 : 0);
    });

    buildDots();
    setInterval(() => {
        const maxIndex = total - (window.innerWidth < 768 ? 1 : 2);
        goTesti(testiIdx < maxIndex ? testiIdx + 1 : 0);
    }, 5000);
    window.addEventListener('resize', () => { testiIdx = 0; goTesti(0); });
}

function renderFAQ() {
    const list = $('faqList');
    if (!list) return;

    list.innerHTML = '';

    faqData.forEach((faq, i) => {
        const item = el('div', 'faq-item');
        item.style.setProperty('--d', `${i * 0.1}s`);

        item.innerHTML = `
      <div class="faq-question">
        ${faq.question}
        <span class="faq-icon">+</span>
      </div>
      <div class="faq-answer">${faq.answer}</div>
    `;

        item.querySelector('.faq-question').addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            document.querySelectorAll('.faq-item').forEach(f => {
                f.classList.remove('active');
            });

            if (!isActive) {
                item.classList.add('active');
            }
        });

        list.appendChild(item);
    });

    initReveal();
}

/* ══════════════════════════════════════
   BOOKING / CONTACT FORM
══════════════════════════════════════ */
const contactForm = $('contactForm');
if (contactForm) {
    const checkinInput = $('bookCheckin');
    const checkoutInput = $('bookCheckout');
    if (checkinInput && checkoutInput) {
        const today = new Date().toISOString().split('T')[0];
        checkinInput.min = today;
        checkinInput.addEventListener('change', () => {
            checkoutInput.min = checkinInput.value;
            if (checkoutInput.value && checkoutInput.value < checkinInput.value) {
                checkoutInput.value = checkinInput.value;
            }
        });
    }

    contactForm.addEventListener('submit', e => {
        e.preventDefault();
        const form = e.target;
        const name = $('bookName') ? $('bookName').value.trim() : '';
        const dest = $('bookDest') ? $('bookDest').value.trim() : '';
        const checkin = $('bookCheckin') ? $('bookCheckin').value : '';
        const checkout = $('bookCheckout') ? $('bookCheckout').value : '';
        const adults = $('bookAdults') ? $('bookAdults').value : '1';
        const kids = $('bookKids') ? $('bookKids').value : '0';
        const groupType = $('bookGroupType') ? $('bookGroupType').value : '';
        const rooms = $('bookRooms') ? $('bookRooms').value : '1';

        const msg = `Hello Beyondstays, I would like to book a trip!\n\n` +
            `👤 Name: ${name || 'Guest'}\n` +
            `📍 Destination: ${dest || 'Not specified'}\n` +
            `📅 Check-in Date: ${checkin || 'Flexible'}\n` +
            `📅 Check-out Date: ${checkout || 'Flexible'}\n` +
            `👥 Adults: ${adults}\n` +
            `🧒 Kids: ${kids}\n` +
            `🏷️ Group Type: ${groupType || 'Not specified'}\n` +
            `🏨 No. of Rooms: ${rooms}\n\n` +
            `Please share available packages and pricing.`;

        const btn = form.querySelector('.btn-submit');
        const origContent = btn ? btn.innerHTML : 'Book Now <span>→</span>';
        if (btn) {
            btn.textContent = '⏳ Redirecting…';
            btn.style.opacity = '0.8';
        }

        setTimeout(() => openWaPage(msg), 500);
        setTimeout(() => {
            if (btn) {
                btn.innerHTML = origContent;
                btn.style.opacity = '1';
            }
            form.reset();
        }, 3500);
    });
}

/* ══════════════════════════════════════
   BACK TO TOP
══════════════════════════════════════ */
if($('btt')) if($('btt')) $('btt').addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

/* ══════════════════════════════════════
   INIT
══════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
    // Fallback for Safari which doesn't support requestIdleCallback
    const runInit = () => { console.log("runInit called!");
        initHero();
        initTestimonials();
        fetchData();
        fetchFAQ();
        initReveal();
    };
    if (window.requestIdleCallback) {
        requestIdleCallback(runInit);
    } else {
        setTimeout(runInit, 1);
    }
});

window.onerror = function (msg, url, line, col, error) {
  alert("Error: " + msg);
};



















// About Section Slider Logic
document.addEventListener('DOMContentLoaded', () => {
    const mainImg = document.getElementById('aboutMainImg');
    const mainTitle = document.getElementById('aboutMainTitle');
    const mainDesc = document.getElementById('aboutMainDesc');
    const thumbs = document.querySelectorAll('#aboutThumbnails .thumb');
    const dots = document.querySelectorAll('#aboutSliderDots span');

    const slides = [
        {
            title: "Luxury Pool Stays in Wayanad",
            desc: "Unwind in the lap of nature with exclusive private pool villas nestled in the lush green hills of Wayanad.",
            img: "./assets/aboutPictures/Wayanad_poolStay.jpeg"
        },
        {
            title: "Joyful Family Stays",
            desc: "Create unforgettable memories with your loved ones in our spacious, safe, and welcoming family properties.",
            img: "./assets/aboutPictures/Family_Stays.png"
        },
        {
            title: "Thrilling Northern Treks",
            desc: "Fuel your adventurous spirit with our guided trekking experiences and cozy basecamps across the majestic North.",
            img: "./assets/aboutPictures/North_trekking.jpeg"
        },
        {
            title: "Romantic Kashmir Escapes",
            desc: "Discover the paradise on earth with intimate, breathtaking stays designed perfectly for couples.",
            img: "./assets/aboutPictures/kashmir_couples.jpeg"
        },
        {
            title: "Authentic Backwaters",
            desc: "Experience the authentic charm and tranquil backwaters of Kerala in our handpicked traditional retreats.",
            img: "./assets/aboutPictures/cozy_staysInKerala.jpeg"
        }
    ];

    let currentIndex = 0;

    function updateSlider(index) {
        currentIndex = index;
        
        // Fade out
        mainImg.style.opacity = '0';
        mainTitle.style.opacity = '0';
        mainDesc.style.opacity = '0';
        
        setTimeout(() => {
            mainImg.src = slides[index].img;
            mainTitle.textContent = slides[index].title;
            mainDesc.textContent = slides[index].desc;
            
            // Fade in
            mainImg.style.opacity = '1';
            mainTitle.style.opacity = '1';
            mainDesc.style.opacity = '1';
        }, 300);

        // Update dots and thumbs
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
        thumbs.forEach((thumb, i) => {
            thumb.classList.toggle('active', i === index);
        });
    }

    thumbs.forEach((thumb, i) => {
        thumb.addEventListener('click', () => updateSlider(i));
    });
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => updateSlider(i));
    });

    // Auto rotate every 5 seconds
    setInterval(() => {
        let next = (currentIndex + 1) % slides.length;
        updateSlider(next);
    }, 5000);
});



    
// Package Modal Logic
document.addEventListener('DOMContentLoaded', () => {
    const pkgModal = document.getElementById('pkgModal');
    const pkgModalClose = document.getElementById('pkgModalClose');
    const pkgModalOverlay = document.getElementById('pkgModalOverlay');
    const pkgModalBody = document.getElementById('pkgModalBody');
    const pkgModalWaBtn = document.getElementById('pkgModalWaBtn');
    const modalSlider = document.getElementById('packagesSlider');

    if (modalSlider && pkgModal) {
        modalSlider.addEventListener('click', (e) => {
            const btn = e.target.closest('.pkg-btn');
            if (btn) {
                e.preventDefault();
                const card = btn.closest('.pkg-card');
                const idx = Array.from(modalSlider.children).indexOf(card);
                if (idx > -1 && window.allPackagesData && window.allPackagesData[idx]) {
                    openPkgModal(window.allPackagesData[idx]);
                }
            }
        });

        const closeModal = () => {
            pkgModal.classList.remove('active');
            document.body.style.overflow = '';
        };

        pkgModalClose.addEventListener('click', closeModal);
        pkgModalOverlay.addEventListener('click', closeModal);
    }
});

function openPkgModal(pkg) {
    const pkgModal = document.getElementById('pkgModal');
    const pkgModalBody = document.getElementById('pkgModalBody');
    const pkgModalWaBtn = document.getElementById('pkgModalWaBtn');
    
    let highlightsHtml = '';
    if (pkg.highlights && pkg.highlights.length > 0) {
        highlightsHtml = `
            <div class="pkg-m-section">
                <h4>Highlights</h4>
                <ul class="pkg-m-list">
                    ${pkg.highlights.map(h => `<li class="incl"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> ${h.replace(/^[✓✔] /, '')}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    let incExcHtml = '';
    if ((pkg.inclusions && pkg.inclusions.length > 0) || (pkg.exclusions && pkg.exclusions.length > 0)) {
        incExcHtml = `<div class="pkg-m-section"><h4>Inclusions & Exclusions</h4><ul class="pkg-m-list">`;
        if (pkg.inclusions) {
            pkg.inclusions.forEach(inc => {
                incExcHtml += `<li class="incl"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> ${inc.replace(/^[✓✔] /, '')}</li>`;
            });
        }
        if (pkg.exclusions) {
            pkg.exclusions.forEach(exc => {
                incExcHtml += `<li class="excl"><svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg> ${exc.replace(/^[✖✖] /, '')}</li>`;
            });
        }
        incExcHtml += `</ul></div>`;
    }

    let noteHtml = '';
    let mainDesc = pkg.description || '';
    if (mainDesc.includes('Condition:-')) {
        const parts = mainDesc.split('Condition:-');
        mainDesc = parts[0];
        noteHtml = `<div class="pkg-m-note"><strong>Important Note:</strong><br>${parts[1]}</div>`;
    } else if (mainDesc.includes('Heavy Snowfall')) {
        const parts = mainDesc.split('Heavy Snowfall');
        mainDesc = parts[0];
        noteHtml = `<div class="pkg-m-note"><strong>Heavy Snowfall Condition:</strong><br>${parts[1]}</div>`;
    }

    pkgModalBody.innerHTML = `
        <h2 class="pkg-m-title">${pkg.placeName || pkg.name}</h2>
        <div class="pkg-m-subtitle">${pkg.name}</div>
        
        <div class="pkg-m-meta">
            <span><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg> ${pkg.duration || 'Custom Duration'}</span>
            <span><svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.41l9 9c.36.36.86.58 1.41.58s1.05-.22 1.41-.59l7-7c.36-.36.59-.86.59-1.41s-.23-1.06-.59-1.41zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/></svg> from ${pkg.price || 'Ask Price'}</span>
        </div>

        <p class="pkg-m-desc">${mainDesc}</p>
        ${noteHtml}
        ${highlightsHtml}
        ${incExcHtml}
    `;

    const waMsg = `Hi Beyondstays! I am interested in the ${pkg.name} package. Can you share more details?`;
    pkgModalWaBtn.href = `https://wa.me/919999999999?text=${encodeURIComponent(waMsg)}`;

    pkgModal.classList.add('active');
    document.body.style.overflow = 'hidden';
}
