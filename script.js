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

async function fetchFAQ() {
    try {
        const res = await fetch('faq.json');
        if (!res.ok) throw new Error();
        faqData = await res.json();
    } catch {
        faqData = [
            {
                question: "Sample Question?",
                answer: "Sample answer if JSON fails."
            }
        ];
    }

    renderFAQ();
}

/* ══════════════════════════════════════
   NAVBAR
══════════════════════════════════════ */
const navbar = $('navbar');
const navLogo = document.querySelector('#navbar .nav-logo img');
let lastLogo = '';

window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;

    if (navbar) {
        navbar.classList.toggle('scrolled', scrolled);
        if (scrolled) {
            navbar.classList.remove('cutout-mode');
        } else {
            navbar.classList.add('cutout-mode');
        }
    }
    
    if ($('btt')) {
        $('btt').classList.toggle('hidden', window.scrollY < 400);
    }

    if (!navLogo) return;

    const newSrc = "./assets/nav-logo-green.png";

    if (lastLogo !== newSrc) {
        navLogo.src = newSrc;
        lastLogo = newSrc;
    }
});

// Hamburger
const hamburger = $('hamburger');
const mobileMenu = $('mobileMenu');
if(hamburger) hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    if (navbar) navbar.classList.toggle('menu-open');
});
document.querySelectorAll('.mm-link').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        if (navbar) navbar.classList.remove('menu-open');
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
    try {
        const res = await fetch('data.json?v=' + new Date().getTime());
        if (!res.ok) throw new Error();
        travelData = await res.json();
    } catch {
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
            <!-- Top Image Section -->
            <div class="pkg-img-wrap" style="cursor:pointer;" onclick="openModal(${index})">
                <img src="${pkg.coverImage}?auto=compress&cs=tinysrgb&w=600" alt="${pkg.name}" loading="lazy" />
                <div class="pkg-img-overlay"></div>
                
                <div class="pkg-badges">
                    ${pkg.region === 'International' ? '<span class="pkg-badge">Popular</span>' : ''}
                    <div class="pkg-arrow-btn" onclick="event.stopPropagation(); openModal(${index})">&#8599;</div>
                </div>
                
                <div class="pkg-title-area">
                    <div class="pkg-title">
                        <h3>${pkg.name}</h3>
                        <div class="pkg-location">
                            <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                            ${pkg.placeName}
                        </div>
                        <div class="pkg-desc-text">${pkg.description}</div>
                    </div>
                </div>
            </div>
            
            <!-- Bottom Stats Section -->
            <div class="pkg-stats-grid">
                <div class="pkg-stat">
                    <span>Price</span>
                    <strong>${pkg.price}</strong>
                </div>
                <div class="pkg-stat">
                    <span>Duration</span>
                    <strong>${pkg.duration.split(' ')[0]} ${pkg.duration.split(' ')[1]}</strong>
                </div>
                <div class="pkg-stat">
                    <span>Type</span>
                    <strong>${pkg.region}</strong>
                </div>
                
                <div class="pkg-stat" style="grid-column: span 2;">
                    <span>${levels[levelIdx]}</span>
                    <div class="pkg-level-bar">
                        <div class="pkg-level-fill ${levelClasses[levelIdx]}" style="width: ${70 + (index*10)%30}%"></div>
                    </div>
                </div>
                <div class="pkg-stat">
                    <span>Rating</span>
                    <div class="pkg-rating">
                        ${rating} 
                        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                    </div>
                </div>
            </div>
        `;
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
        const visibleCards = 2;
        const maxIndex = total - visibleCards;

        testiIdx = Math.max(0, Math.min(idx, maxIndex));

        const cardW = cards[0].getBoundingClientRect().width + 24;

        track.style.transform = `translateX(-${testiIdx * cardW}px)`;

        dotsWrap.querySelectorAll('.testi-dot')
            .forEach((d, i) => d.classList.toggle('active', i === testiIdx));
    }

    $('tPrev').addEventListener('click', () => goTesti(testiIdx > 0 ? testiIdx - 1 : total - 1));
    $('tNext').addEventListener('click', () => goTesti(testiIdx < total - 1 ? testiIdx + 1 : 0));

    buildDots();
    setInterval(() => goTesti(testiIdx < total - 1 ? testiIdx + 1 : 0), 5000);
    window.addEventListener('resize', () => { testiIdx = 0; goTesti(0); });
}

function renderFAQ() {
    const list = $('faqList');
    if (!list) return;

    list.innerHTML = '';

    faqData.forEach((faq, i) => {
        const item = el('div', 'faq-item reveal-up');
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












// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (mobileMenu.classList.contains('open')) {
        const clickedInsideNav = navbar && navbar.contains(e.target);
        const clickedInsideMenu = mobileMenu.contains(e.target);
        
        if (!clickedInsideNav && !clickedInsideMenu) {
            mobileMenu.classList.remove('open');
            if (navbar) navbar.classList.remove('menu-open');
        }
    }
});






/* -----------------------------------------------------------
   ABOUT DESKTOP AUTO SLIDER
----------------------------------------------------------- */
const aboutMainImg = document.getElementById('aboutMainImg');
const aboutMainTitle = document.getElementById('aboutMainTitle');
const aboutMainDesc = document.getElementById('aboutMainDesc');
const aboutSidebarItems = document.querySelectorAll('.about-sidebar-item img'); // Get the images directly
const aboutSliderDots = document.querySelectorAll('#aboutSliderDots span');

if (aboutMainImg && aboutMainTitle && aboutMainDesc && aboutSidebarItems.length === 4) {
    const aboutSlides = [
        {
            img: "./assets/aboutPictures/cozy_staysInKerala.jpeg",
            title: "Cozy Stays in Kerala",
            desc: "Experience the authentic charm and tranquil backwaters of Kerala in our handpicked traditional retreats."
        },
        {
            img: "./assets/aboutPictures/Family_Stays.png",
            title: "Joyful Family Stays",
            desc: "Create unforgettable memories with your loved ones in our spacious, safe, and welcoming family properties."
        },
        {
            img: "./assets/aboutPictures/kashmir_couples.jpeg",
            title: "Romantic Kashmir Escapes",
            desc: "Discover the paradise on earth with intimate, breathtaking stays designed perfectly for couples."
        },
        {
            img: "./assets/aboutPictures/North_trekking.jpeg",
            title: "Thrilling Northern Treks",
            desc: "Fuel your adventurous spirit with our guided trekking experiences and cozy basecamps across the majestic North."
        },
        {
            img: "./assets/aboutPictures/Wayanad_poolStay.jpeg",
            title: "Luxury Pool Stays in Wayanad",
            desc: "Unwind in the lap of nature with exclusive private pool villas nestled in the lush green hills of Wayanad."
        }
    ];

    let currentSlide = 0;

    setInterval(() => {
        // Fade out main elements
        aboutMainImg.style.opacity = '0.3';
        aboutMainTitle.style.opacity = '0';
        aboutMainDesc.style.opacity = '0';
        
        // Also fade out sidebar images for a smooth swap
        aboutSidebarItems.forEach(img => img.style.opacity = '0.3');
        
        setTimeout(() => {
            currentSlide = (currentSlide + 1) % aboutSlides.length;
            
            // Update main image and text
            aboutMainImg.src = aboutSlides[currentSlide].img;
            aboutMainTitle.innerText = aboutSlides[currentSlide].title;
            aboutMainDesc.innerText = aboutSlides[currentSlide].desc;
            
            // Update sidebar images with the other 4
            for(let i = 0; i < 4; i++) {
                let sidebarIndex = (currentSlide + i + 1) % aboutSlides.length;
                aboutSidebarItems[i].src = aboutSlides[sidebarIndex].img;
            }
            
            // Update dots
            if (aboutSliderDots.length > 0) {
                aboutSliderDots.forEach(dot => dot.classList.remove('active'));
                if (aboutSliderDots[currentSlide]) {
                    aboutSliderDots[currentSlide].classList.add('active');
                }
            }
            
            // Fade in all
            aboutMainImg.style.opacity = '1';
            aboutMainTitle.style.opacity = '1';
            aboutMainDesc.style.opacity = '1';
            aboutSidebarItems.forEach(img => img.style.opacity = '1');
        }, 400); // Wait for fade out
    }, 4000); // Change every 4 seconds
}
