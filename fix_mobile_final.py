import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's completely replace the old mobile reset with an even more aggressive one
new_mobile_reset = '''
/* COMPREHENSIVE MOBILE RESET */
@media (max-width: 768px) {
    /* Hide the desktop cutout fillet curves on mobile */
    #navbar.cutout-mode .nav-logo-container::before,
    #navbar.cutout-mode .nav-logo-container::after,
    .hero-nav::before,
    .hero-nav::after {
        display: none !important;
    }

    /* Remove arrows on mobile */
    .hero-nav {
        display: none !important;
    }

    /* Remove the texts and buttons on mobile */
    .hero-ui-layer,
    .hero-giant-title {
        display: none !important;
    }

    /* Remove the white desktop bezel from the hero on mobile */
    .hero-slides {
        inset: 0 !important;
        border-radius: 0 !important;
    }
    
    /* Make sure the hero frame doesn't constrain or round the image on mobile */
    .hero-wrapper {
        padding: 0 !important;
    }
    .hero-frame {
        border-radius: 0 !important;
        overflow: visible !important;
    }

    /* Fix the logo position on mobile */
    .nav-logo-container {
        position: static !important;
        transform: none !important;
        left: auto !important;
        height: auto !important;
        justify-content: flex-start !important;
        padding: 0 !important;
        background: transparent !important;
    }
    
    /* Ensure the mobile navbar looks like a floating pill from the start */
    #navbar.cutout-mode {
        position: fixed !important;
        top: 24px !important;
        left: 50% !important;
        transform: translateX(-50%) translateZ(0) !important;
        width: 90% !important;
        background: rgba(255, 255, 255, 0.12) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 50px !important;
        padding: 10px 20px !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
    }
}
'''

if '/* COMPREHENSIVE MOBILE RESET */' in css:
    css = re.sub(r'/\* COMPREHENSIVE MOBILE RESET \*/.*', new_mobile_reset, css, flags=re.DOTALL)
else:
    css += new_mobile_reset

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
