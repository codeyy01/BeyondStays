import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_navbar = '''            <!-- 3 DISTINCT NAVBAR PIECES -->
            <nav id="nav-left" class="nav-piece left-pill">
                <ul class="nav-links">
                    <li><a href="#hero">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#destinations">Packages</a></li>
                </ul>
            </nav>

            <div id="nav-logo" class="nav-piece logo-tab">
                <a href="#" class="nav-logo">
                    <img src="./assets/nav-logo-green.png" id="navLogo" alt="Beyondstays Logo" />
                </a>
            </div>

            <nav id="nav-right" class="nav-piece right-pill">
                <ul class="nav-links">
                    <li><a href="#testimonials">Reviews</a></li>
                    <li><a href="#faq">FAQ</a></li>
                    <li><a href="#contact" class="nav-cta">Book Now</a></li>
                </ul>
                <button class="hamburger" id="hamburger" aria-label="Menu">
                    <span></span><span></span>
                </button>
            </nav>'''

html = re.sub(r'<nav id="navbar"[^>]*>.*?</nav>', new_navbar, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated.")
