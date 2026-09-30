import re

new_css = '''
/* --- RECOVERED RESPONSIVE & MISSING STYLES --- */

/* Fix Testimonials */
.testi-slider-wrap {
    position: relative;
    overflow: hidden;
    padding: 20px 0;
    width: 100%;
}
.testi-track {
    display: flex;
    gap: 24px;
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    width: 100%;
}
.testi-card {
    min-width: calc(50% - 12px);
    background: #fff;
    padding: 32px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
}
.testi-stars {
    color: #f59e0b;
    font-size: 1.2rem;
    margin-bottom: 16px;
}
.testi-card p {
    font-size: 1rem;
    line-height: 1.6;
    color: #555;
    margin-bottom: 24px;
    flex-grow: 1;
}
.testi-author {
    display: flex;
    align-items: center;
    gap: 16px;
}
.testi-author img {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    object-fit: cover;
}
.testi-author div {
    display: flex;
    flex-direction: column;
}
.testi-author strong {
    color: #111;
    font-size: 0.95rem;
}
.testi-author span {
    color: #777;
    font-size: 0.8rem;
}

/* Nav & Mobile Menu */
.nav-toggle {
    display: none;
    flex-direction: column;
    justify-content: space-between;
    width: 28px;
    height: 20px;
    background: transparent;
    border: none;
    cursor: pointer;
    z-index: 1100;
}
.nav-toggle span {
    width: 100%;
    height: 2px;
    background: var(--text-dark);
    transition: all 0.3s;
    border-radius: 2px;
}

.mobile-menu {
    position: fixed;
    top: 0;
    right: -100%;
    width: 80%;
    max-width: 400px;
    height: 100vh;
    background: var(--white);
    z-index: 1050;
    display: flex;
    flex-direction: column;
    padding: 80px 40px;
    transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: -10px 0 30px rgba(0,0,0,0.1);
}
.mobile-menu.active {
    right: 0;
}
.mobile-menu ul {
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.mobile-menu ul li a {
    font-size: 1.5rem;
    font-family: var(--font-heading);
    color: var(--text-dark);
    text-decoration: none;
}

/* Global Responsive Fixes */
@media (max-width: 1024px) {
    .nav-links { display: none; }
    .nav-cta { display: none; }
    .nav-toggle { display: flex; }
    
    .testi-card {
        min-width: 100%;
    }
}

@media (max-width: 768px) {
    .contact-layout {
        grid-template-columns: 1fr;
        gap: 40px;
    }
    .form-grid {
        grid-template-columns: 1fr !important;
    }
    .contact-form .full-width {
        grid-column: span 1 !important;
    }
    .contact-form button {
        grid-column: span 1 !important;
    }
    
    .hero-content h1 {
        font-size: 3rem;
    }
    .section-title {
        font-size: 2.5rem;
    }
    .footer-top {
        grid-template-columns: 1fr;
        gap: 40px;
    }
    .wa-fab {
        bottom: 16px;
        right: 16px;
        width: 50px;
        height: 50px;
    }
}
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the broken testimonials and nav-toggle from the previous recovery attempt
css = re.sub(r'/\* --- RECOVERED BASE STYLES ---\*/.*?/\* --- NEW HERO REDESIGN --- \*/', '/* --- NEW HERO REDESIGN --- */', css, flags=re.DOTALL)
# Wait, I didn't match the exact comment string in the regex. I will just append the new_css to the end, and let it override whatever is broken.

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + new_css)
