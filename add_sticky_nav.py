import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scrolled_nav = '''
            <!-- UNIFIED STICKY NAVBAR (SCROLLED STATE) -->
            <nav id="navbar-scrolled" class="navbar-scrolled">
                <div class="nav-inner">
                    <ul class="nav-links">
                        <li><a href="#hero">Home</a></li>
                        <li><a href="#about">About</a></li>
                        <li><a href="#destinations">Packages</a></li>
                    </ul>
                    <a href="#" class="nav-logo">
                        <img src="./assets/nav-logo-green.png" alt="Beyondstays Logo" style="height: 32px; width: auto;" />
                    </a>
                    <ul class="nav-links">
                        <li><a href="#testimonials">Reviews</a></li>
                        <li><a href="#faq">FAQ</a></li>
                        <li><a href="#contact" class="nav-cta">Book Now</a></li>
                    </ul>
                </div>
            </nav>
'''

# Find the end of nav-right
if 'id="navbar-scrolled"' not in html:
    html = re.sub(r'(<nav id="nav-right"[^>]*>.*?</nav>)', r'\1\n' + scrolled_nav, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added sticky navbar to HTML.")
