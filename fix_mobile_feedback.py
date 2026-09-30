with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- MOBILE FIXES BASED ON USER FEEDBACK --- */
@media (max-width: 768px) {
    /* 1. Remove green border */
    .hero-wrapper { 
        padding: 0 !important; 
        background: transparent !important; 
    }
    
    /* 2. Remove box card from bottom, keep only button */
    .hero-left-content {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        padding: 0 !important;
    }
    .hero-left-content p { display: none !important; }
    
    /* 3. Hamburger styling */
    .navbar-scrolled .hamburger span {
        background: var(--dark-green) !important;
        height: 2px !important;
        width: 24px !important;
        border-radius: 2px !important;
    }
    .navbar-scrolled .hamburger {
        gap: 6px !important;
        justify-content: center !important;
    }
    
    /* 4. Dropdown Menu Integration */
    .navbar-scrolled {
        transition: border-radius 0.3s ease !important;
    }
    .navbar-scrolled.menu-open {
        border-bottom-left-radius: 0 !important;
        border-bottom-right-radius: 0 !important;
        border-bottom: none !important;
        background: rgba(255, 255, 255, 0.8) !important; /* Slightly more opaque when open */
    }
    .mobile-menu {
        top: 80px !important; /* Exact distance to sit flush under navbar (24px top + 56px height) */
        left: 20px !important; /* Matches navbar calc(100% - 40px) */
        width: calc(100% - 40px) !important;
        border-top-left-radius: 0 !important;
        border-top-right-radius: 0 !important;
        border-top: none !important;
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1) !important;
        padding: 20px 0 40px !important;
    }
    .mobile-menu ul {
        display: flex !important;
        flex-direction: column !important;
        gap: 24px !important;
        align-items: center !important;
    }
    .mm-link {
        color: var(--dark-green) !important;
        font-size: 1.1rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        font-weight: 700 !important;
        opacity: 0.8 !important;
    }
}
''')
print("CSS appended.")
