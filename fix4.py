import re

# UPDATE HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_nav = '''                    <ul class="nav-links nav-left">
                        <li><a href="#hero">Home</a></li>
                        <li><a href="#destinations">Programs</a></li>
                        <li><a href="#faq">Coaching</a></li>
                    </ul>
                    
                    <div class="nav-logo-container">
                        <a href="#" class="nav-logo">
                            <img src="./assets/nav-logo-white.png" id="navLogo" alt="Beyondstays Logo" />
                        </a>
                    </div>
                    
                    <ul class="nav-links nav-right">
                        <li><a href="#about">Academy</a></li>
                        <li><a href="#testimonials">Reviews</a></li>
                        <li><a href="#contact" class="nav-cta">Book a Session</a></li>
                    </ul>'''

new_nav = '''                    <ul class="nav-links nav-left">
                        <li><a href="#hero">Home</a></li>
                        <li><a href="#about">About</a></li>
                        <li><a href="#destinations">Packages</a></li>
                    </ul>
                    
                    <div class="nav-logo-container">
                        <a href="#" class="nav-logo">
                            <img src="./assets/nav-logo-white.png" id="navLogo" alt="Beyondstays Logo" />
                        </a>
                    </div>
                    
                    <ul class="nav-links nav-right">
                        <li><a href="#testimonials">Reviews</a></li>
                        <li><a href="#faq">FAQ</a></li>
                        <li><a href="#contact" class="nav-cta">Book Now</a></li>
                    </ul>'''
html = html.replace(old_nav, new_nav)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# UPDATE CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_css = '''#navbar.cutout-mode .nav-links {
    display: flex;
    gap: 32px;
    margin-top: 30px;
}'''

new_css = '''#navbar.cutout-mode .nav-links {
    display: flex;
    gap: 32px;
    margin-top: 30px;
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 50px !important;
    padding: 0 32px !important;
    align-items: center !important;
    height: 56px;
}'''
css = css.replace(old_css, new_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

