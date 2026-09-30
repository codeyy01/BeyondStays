import re

perfect_css = """
/* =========================================
   PIXEL-PERFECT HERO & NAVBAR (FINAL DESIGN)
   ========================================= */

body {
    background: var(--green); /* Dark green background */
    overflow-x: hidden;
    margin: 0;
}

/* ── Hero Wrapper & Frame ── */
.hero-wrapper {
    position: relative;
    width: 100%;
    height: 100vh;
    padding: 24px;
    box-sizing: border-box;
    background: var(--green);
}
.hero-frame {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 40px;
    background: #fff;
    padding: 16px; /* Creates the white border effect */
    box-sizing: border-box;
}
.hero-slides {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 28px; /* Inner radius */
    overflow: hidden;
    background: #000;
}
.hero-slide {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 1.2s cubic-bezier(0.4, 0, 0.2, 1);
    background-size: cover;
    background-position: center;
}
.hero-slide::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.5) 100%);
}
.hero-slide.active {
    opacity: 1;
    z-index: 1;
}

/* ── Giant Text ── */
.hero-giant-title {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
    color: #fff;
    font-family: 'Anton', sans-serif;
    font-size: 18vw;
    line-height: 0.85;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 2px;
    pointer-events: none;
    opacity: 0.95;
    text-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

/* ── Navbar (Cutout Mode - Initial) ── */
#navbar.cutout-mode {
    position: absolute;
    top: 16px; /* Aligns perfectly with the white padding */
    left: 16px;
    width: calc(100% - 32px); /* Fits inside the white padding */
    z-index: 100;
    pointer-events: none;
    padding: 0 40px; /* Spacing from edges */
}
#navbar.cutout-mode .nav-inner {
    position: relative;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 24px;
}
#navbar.cutout-mode .nav-left,
#navbar.cutout-mode .nav-right {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 40px;
    padding: 0 32px;
    height: 50px;
    display: flex;
    align-items: center;
    pointer-events: auto;
    gap: 32px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

/* Center Logo Cutout */
#navbar.cutout-mode .nav-logo-container {
    position: absolute;
    top: -24px; /* Move up to touch the white frame */
    left: 50%;
    transform: translateX(-50%);
    background: #fff;
    padding: 12px 40px 16px;
    border-bottom-left-radius: 30px;
    border-bottom-right-radius: 30px;
    pointer-events: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
}
#navbar.cutout-mode .nav-logo-container::before,
#navbar.cutout-mode .nav-logo-container::after {
    content: '';
    position: absolute;
    top: 0;
    width: 30px;
    height: 30px;
    background: transparent;
}
#navbar.cutout-mode .nav-logo-container::before {
    left: -30px;
    border-top-right-radius: 30px;
    box-shadow: 15px -15px 0 15px #fff;
}
#navbar.cutout-mode .nav-logo-container::after {
    right: -30px;
    border-top-left-radius: 30px;
    box-shadow: -15px -15px 0 15px #fff;
}
.nav-logo img {
    height: 32px;
    width: auto;
    display: block;
}

/* ── Navbar (Scrolled Mode - Unified Pill) ── */
#navbar.scrolled {
    position: fixed;
    top: 24px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 1000px;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 50px;
    padding: 12px 40px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
}
#navbar.scrolled .nav-inner {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
#navbar.scrolled .nav-left,
#navbar.scrolled .nav-right {
    display: flex;
    gap: 32px;
    background: transparent;
    border: none;
    padding: 0;
    height: auto;
    box-shadow: none;
}
#navbar.scrolled .nav-logo-container {
    position: relative;
    background: transparent;
    padding: 0;
    top: 0;
    transform: none;
    display: flex;
    align-items: center;
}
#navbar.scrolled .nav-logo-container::before,
#navbar.scrolled .nav-logo-container::after {
    display: none;
}

/* Nav Links Base */
.nav-links {
    list-style: none;
    margin: 0;
    padding: 0;
}
.nav-links a {
    font-size: 0.95rem;
    font-weight: 600;
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
}
.nav-cta {
    background: var(--green) !important;
    color: #fff !important;
    padding: 10px 24px;
    border-radius: 30px;
    font-weight: 600;
}
#navbar.scrolled .nav-links a {
    color: #fff; /* Keep white because it's a glass pill over the site */
}

/* ── Hero Arrows (Left/Right Cutouts) ── */
.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: #fff;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    width: 48px;
    height: 96px;
    font-size: 1.2rem;
}
.hero-nav::before, .hero-nav::after {
    content: '';
    position: absolute;
    width: 30px;
    height: 30px;
    background: transparent;
}
/* The actual arrow circle inside the white cutout */
.hero-nav-inner {
    width: 32px;
    height: 32px;
    background: var(--green);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.hero-nav.prev {
    left: 16px;
    border-top-right-radius: 35px;
    border-bottom-right-radius: 35px;
    padding-right: 8px;
}
.hero-nav.prev::before {
    left: 0;
    top: -30px;
    border-bottom-left-radius: 30px;
    box-shadow: -15px 15px 0 15px #fff;
}
.hero-nav.prev::after {
    left: 0;
    bottom: -30px;
    border-top-left-radius: 30px;
    box-shadow: -15px -15px 0 15px #fff;
}

.hero-nav.next {
    right: 16px;
    border-top-left-radius: 35px;
    border-bottom-left-radius: 35px;
    padding-left: 8px;
}
.hero-nav.next::before {
    right: 0;
    top: -30px;
    border-bottom-right-radius: 30px;
    box-shadow: 15px 15px 0 15px #fff;
}
.hero-nav.next::after {
    right: 0;
    bottom: -30px;
    border-top-right-radius: 30px;
    box-shadow: 15px -15px 0 15px #fff;
}

/* ── Hero UI Layer (Bottom Cards) ── */
.hero-ui-layer {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 32px 50px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    z-index: 10;
    pointer-events: none;
    box-sizing: border-box;
}
.hero-left-content {
    max-width: 320px;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 30px;
    padding: 24px 32px;
    color: #fff;
    pointer-events: auto;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
}
.hero-left-content p {
    font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 20px;
    font-weight: 500;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
.hero-btn-pill {
    background: var(--green);
    color: #fff;
    padding: 10px 24px;
    border-radius: 30px;
    border: none;
    font-weight: 600;
    font-size: 0.85rem;
    cursor: pointer;
    display: inline-block;
    transition: background 0.3s ease;
}
.hero-btn-pill:hover {
    background: var(--green-dark);
}

.hero-right-glass-card {
    max-width: 260px;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 24px 32px;
    border-radius: 30px;
    color: #fff;
    pointer-events: auto;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
}
.hero-right-glass-card p {
    font-size: 0.9rem;
    line-height: 1.5;
    margin: 0;
    font-weight: 500;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

/* ── Mobile Responsive Overrides ── */
@media (max-width: 1024px) {
    #navbar.cutout-mode { padding: 0 20px; }
    #navbar.cutout-mode .nav-left, #navbar.cutout-mode .nav-right { display: none; }
    .hero-ui-layer { flex-direction: column; padding: 20px; align-items: flex-start; gap: 20px; bottom: 40px; }
    .hero-right-glass-card { display: none; }
    .hero-giant-title { font-size: 22vw; }
    .hero-wrapper { padding: 12px; }
    .hero-frame { padding: 8px; border-radius: 24px; }
    .hero-slides { border-radius: 16px; }
    #navbar.cutout-mode .nav-logo-container { padding: 8px 24px 12px; }
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Strip any hero block that was injected previously (just to be safe)
import re
css = re.sub(r'/\* =========================================\s*PIXEL-PERFECT HERO & NAVBAR.*?/\* ── Loader ── \*/', '/* ── Loader ── */', css, flags=re.DOTALL)
# Also strip the base reset and body from the old file so we don't conflict
css = re.sub(r'/\* ── Reset ── \*/.*?/\* ── Loader ── \*/', '/* ── Loader ── */', css, flags=re.DOTALL)

# Extract :root
root_match = re.search(r'(:root\s*\{.*?\})', css, flags=re.DOTALL)
root_vars = root_match.group(1) if root_match else ''

# Extract everything from Loader onwards
loader_idx = css.find('/* ── Loader ── */')
rest_of_css = css[loader_idx:] if loader_idx != -1 else ''

# Assemble
final_css = '/* ===== Beyondstays style.css ===== */\n' + root_vars + '\n\n' + perfect_css + '\n\n' + rest_of_css

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(final_css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update HTML to use the new CSS file
html = re.sub(r'style.*?\.css\?v=[0-9]+', 'style_ultimate.css?v=1', html)

# Also update the HTML arrows to contain the inner circle
html = html.replace('<div class="hero-nav prev" id="heroPrev">&#10094;</div>', '<div class="hero-nav prev" id="heroPrev"><div class="hero-nav-inner">&#10094;</div></div>')
html = html.replace('<div class="hero-nav next" id="heroNext">&#10095;</div>', '<div class="hero-nav next" id="heroNext"><div class="hero-nav-inner">&#10095;</div></div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Ultimate hero design applied!')
