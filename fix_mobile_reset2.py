import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

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

    /* Remove ONLY the glass card on mobile, keep the text and button */
    .hero-right-glass-card {
        display: none !important;
    }
    
    /* Adjust UI layer for mobile to center the button */
    .hero-ui-layer {
        justify-content: center !important;
        left: 20px !important;
        right: 20px !important;
        bottom: 120px !important; /* Move button up slightly */
    }
    .hero-left-content {
        text-align: center;
    }
    .hero-left-content p {
        display: none; /* Hide the tiny paragraph, just keep the button */
    }

    /* Remove the white desktop bezel from the hero on mobile */
    .hero-slides {
        inset: 0 !important;
        border-radius: 0 !important;
    }
    
    /* Make sure absolutely nothing is rounding the image */
    .hero-wrapper, #hero, .hero-frame {
        padding: 0 !important;
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

css = re.sub(r'/\* COMPREHENSIVE MOBILE RESET \*/.*', new_mobile_reset, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
