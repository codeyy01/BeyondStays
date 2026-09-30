import re

new_css = '''
/* --- RECOVERED BASE STYLES --- */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.8rem 1.5rem;
    border-radius: 40px;
    font-weight: 600;
    font-size: 0.9rem;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
    outline: none;
}

.btn-primary {
    background: var(--primary);
    color: var(--white);
}
.btn-primary:hover {
    background: var(--primary-dark);
}

.nav-cta {
    margin-left: 1rem;
}

/* Nav Toggle */
.nav-toggle {
    display: none;
    flex-direction: column;
    justify-content: space-between;
    width: 24px;
    height: 18px;
    background: transparent;
    border: none;
    cursor: pointer;
    z-index: 1000;
}
.nav-toggle span {
    width: 100%;
    height: 2px;
    background: var(--text-dark);
    transition: all 0.3s;
}
@media (max-width: 768px) {
    .nav-toggle {
        display: flex;
    }
    .nav-links {
        position: fixed;
        top: 0;
        right: -100%;
        width: 80%;
        height: 100vh;
        background: var(--bg-color);
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: right 0.4s ease;
        z-index: 999;
        box-shadow: -5px 0 15px rgba(0,0,0,0.1);
    }
    .nav-links.active {
        right: 0;
    }
    .nav-cta {
        display: none; /* Hide on mobile if needed, or adjust */
    }
}

/* Reviews / Testimonials */
.reviews-section {
    padding: 80px 0;
    background: var(--white);
    overflow: hidden;
}
.testimonials-slider {
    display: flex;
    gap: 20px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    padding-bottom: 20px;
    scrollbar-width: none;
}
.testimonials-slider::-webkit-scrollbar {
    display: none;
}
.review-card {
    min-width: 300px;
    background: var(--bg-color);
    padding: 24px;
    border-radius: 16px;
    scroll-snap-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}
.review-stars {
    color: #f59e0b;
    font-size: 1.2rem;
    margin-bottom: 12px;
}
.review-text {
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--text-light);
    margin-bottom: 16px;
}
.review-author h4 {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-dark);
    margin: 0;
}
.review-author p {
    font-size: 0.8rem;
    color: var(--text-light);
    margin: 2px 0 0 0;
}

/* WhatsApp FAB */
.wa-fab {
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 56px;
    height: 56px;
    background: #25D366;
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    box-shadow: 0 4px 12px rgba(37,211,102,0.4);
    z-index: 990;
    cursor: pointer;
    transition: transform 0.3s;
}
.wa-fab:hover {
    transform: scale(1.1);
}
.wa-fab svg {
    width: 32px;
    height: 32px;
    fill: currentColor;
}
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will inject this right before /* --- NEW HERO REDESIGN --- */ 
# which is where the deletion happened.
css = css.replace('/* --- NEW HERO REDESIGN --- */', new_css + '\n/* --- NEW HERO REDESIGN --- */')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
