import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will append these highly specific, overriding styles to the absolute end of the file.
new_css = '''
/* ====================================================
   ULTIMATE RECOVERY STYLES
   ==================================================== */

/* 1. Navbar Book Now Button */
.nav-cta {
    background-color: var(--primary);
    color: var(--white) !important;
    padding: 12px 28px;
    border-radius: 40px;
    font-weight: 700;
    transition: all 0.3s;
}
.nav-cta:hover {
    background-color: var(--primary-dark);
    transform: translateY(-2px);
}

/* 2. Hamburger Mobile Menu Icon */
.hamburger {
    display: none;
    flex-direction: column;
    justify-content: space-between;
    width: 30px;
    height: 18px;
    background: transparent;
    border: none;
    cursor: pointer;
    z-index: 1050;
    margin-left: auto; /* Push to right */
}
.hamburger span {
    width: 100%;
    height: 2px;
    background: var(--text-dark);
    transition: all 0.3s;
    border-radius: 2px;
}
@media (max-width: 1024px) {
    .hamburger { display: flex; }
    .nav-links { display: none !important; }
}

/* 3. Review / Testimonial Track (For JS transform scrolling) */
.testi-slider-wrap {
    overflow: hidden; /* Hide overflow so transform works */
    width: 100%;
    padding: 20px 0;
}
.testi-track {
    display: flex !important;
    gap: 24px !important;
    width: max-content !important; /* Allow track to expand based on card widths */
    transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1) !important;
}
.testi-card {
    width: calc(50vw - 36px) !important;
    min-width: 320px !important;
    max-width: 400px !important;
    background: #fff;
    padding: 32px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}
@media (max-width: 768px) {
    .testi-card {
        width: calc(100vw - 48px) !important;
        max-width: 100vw !important;
    }
}

/* 4. Contact Form Mobile Fixes */
@media (max-width: 1024px) {
    .contact-layout {
        grid-template-columns: 1fr !important;
        gap: 40px !important;
    }
    .contact-form {
        grid-template-columns: 1fr !important;
        padding: 24px !important;
    }
    .form-row {
        grid-template-columns: 1fr !important;
    }
    .contact-form .full-width, 
    .contact-form button {
        grid-column: span 1 !important;
    }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + new_css)
