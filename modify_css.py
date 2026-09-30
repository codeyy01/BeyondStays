with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- NEW MOBILE HERO REDESIGN --- */
@media (max-width: 768px) {
    /* Remove white border */
    .hero-frame { padding: 0 !important; border-radius: 0 !important; }
    
    /* Hide desktop-specific arrows and complex initial navbar pieces */
    .hero-nav, .nav-piece { display: none !important; }
    
    /* Force the sticky unified navbar to be visible immediately on mobile */
    .navbar-scrolled {
        opacity: 1 !important;
        visibility: visible !important;
        top: 24px !important;
        width: calc(100% - 40px) !important;
        max-width: 100% !important;
    }
    
    /* Hide desktop links in the mobile sticky navbar, show hamburger */
    .navbar-scrolled .nav-links { display: none !important; }
    .hamburger { display: flex !important; margin-left: auto; }
    .navbar-scrolled .nav-inner { padding: 12px 20px !important; justify-content: space-between; }
    .navbar-scrolled .nav-logo { position: static !important; transform: none !important; margin-right: auto; }
    
    /* Stack Typography */
    .hero-giant-title {
        font-size: 20vw !important;
        line-height: 0.9 !important;
        text-align: center !important;
    }
    .mobile-break { display: block !important; }
    
    /* Center bottom Explore pill */
    .hero-ui-layer {
        justify-content: center !important;
        align-items: flex-end !important;
        padding-bottom: 40px !important;
    }
    /* Hide desktop descriptive text, keep only the button in a glass pill */
    .hero-left-text p { display: none !important; }
    .hero-left-text { width: auto !important; padding: 16px 24px !important; border-radius: 40px !important; }
    .hero-right-glass-card { display: none !important; }
    
    /* Mobile Menu Override for exact design */
    .mobile-menu {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    .mm-link {
        color: var(--green) !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
    }
}
.mobile-break { display: none; }
''')
print("CSS updated.")
