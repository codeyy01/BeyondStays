import re

new_hero_css = """
/* =========================================
   PIXEL-PERFECT HERO & NAVBAR (Rebuild)
   ========================================= */

/* ── Layout & Typography ── */
body {
    background: var(--cream);
    overflow-x: hidden;
}
.hero-wrapper {
    position: relative;
    width: 100%;
    height: 100vh;
    padding: 24px;
    box-sizing: border-box;
    background: var(--cream);
}
.hero-frame {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 32px;
    overflow: hidden;
    background: #000;
}
.hero-slides {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
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
    background: linear-gradient(to bottom, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.4) 100%);
}
.hero-slide.active {
    opacity: 1;
    z-index: 1;
}

/* Giant Discover India Text */
.hero-giant-title {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
    color: #fff;
    font-family: 'Anton', sans-serif;
    font-size: 16vw;
    line-height: 0.9;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 2px;
    pointer-events: none;
    opacity: 0.9;
}

/* ── Cutout Mode Navbar (Initial State) ── */
#navbar.cutout-mode {
    position: absolute;
    top: 24px; /* Distance from top of hero-frame */
    left: 0;
    width: 100%;
    z-index: 100;
    padding: 0 40px;
    pointer-events: none;
}
#navbar.cutout-mode .nav-inner {
    position: relative;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
#navbar.cutout-mode .nav-left,
#navbar.cutout-mode .nav-right {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 40px;
    padding: 0 24px;
    height: 44px;
    display: flex;
    align-items: center;
    pointer-events: auto;
    gap: 24px;
}
.nav-links {
    list-style: none;
    margin: 0;
}

/* Logo Cutout (Top Center) */
#navbar.cutout-mode .nav-logo-container {
    position: absolute;
    top: -24px; /* Move exactly up to the hero-frame top edge */
    left: 50%;
    transform: translateX(-50%);
    background: var(--cream);
    padding: 12px 32px 16px;
    border-bottom-left-radius: 24px;
    border-bottom-right-radius: 24px;
    pointer-events: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}
#navbar.cutout-mode .nav-logo-container::before,
#navbar.cutout-mode .nav-logo-container::after {
    content: '';
    position: absolute;
    top: 0;
    width: 24px;
    height: 24px;
    background: transparent;
}
#navbar.cutout-mode .nav-logo-container::before {
    left: -24px;
    border-top-right-radius: 24px;
    box-shadow: 12px -12px 0 12px var(--cream);
}
#navbar.cutout-mode .nav-logo-container::after {
    right: -24px;
    border-top-left-radius: 24px;
    box-shadow: -12px -12px 0 12px var(--cream);
}
.nav-logo img {
    height: 32px;
    width: auto;
    display: block;
}

/* ── Scrolled Navbar (Unified State) ── */
#navbar.scrolled {
    position: fixed;
    top: 16px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 1000px;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 50px;
    padding: 8px 32px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
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
    gap: 24px;
    background: transparent;
    border: none;
    padding: 0;
    height: auto;
}
#navbar.scrolled .nav-logo-container {
    position: relative;
    background: transparent;
    padding: 0;
    top: 0;
    transform: none;
}
#navbar.scrolled .nav-logo-container::before,
#navbar.scrolled .nav-logo-container::after {
    display: none;
}

/* Nav Links Base */
.nav-links a {
    font-size: 0.85rem;
    font-weight: 500;
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
}
#navbar.scrolled .nav-links a {
    color: var(--text);
}
.nav-cta {
    background: #fff;
    color: var(--green) !important;
    padding: 8px 20px;
    border-radius: 30px;
    font-weight: 600;
}
#navbar.scrolled .nav-cta {
    background: var(--green);
    color: #fff !important;
}

/* ── Hero Navigation Arrows (Left/Right Cutouts) ── */
.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: var(--cream);
    color: var(--text);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    font-size: 1rem;
}
.hero-nav.prev {
    left: 0;
    padding: 12px 12px 12px 4px;
    width: 36px;
    height: 70px;
    border-top-right-radius: 24px;
    border-bottom-right-radius: 24px;
}
.hero-nav.prev::before, .hero-nav.prev::after {
    content: '';
    position: absolute;
    left: 0;
    width: 20px;
    height: 20px;
    background: transparent;
}
.hero-nav.prev::before {
    top: -20px;
    border-bottom-left-radius: 20px;
    box-shadow: -10px 10px 0 10px var(--cream);
}
.hero-nav.prev::after {
    bottom: -20px;
    border-top-left-radius: 20px;
    box-shadow: -10px -10px 0 10px var(--cream);
}

.hero-nav.next {
    right: 0;
    padding: 12px 4px 12px 12px;
    width: 36px;
    height: 70px;
    border-top-left-radius: 24px;
    border-bottom-left-radius: 24px;
}
.hero-nav.next::before, .hero-nav.next::after {
    content: '';
    position: absolute;
    right: 0;
    width: 20px;
    height: 20px;
    background: transparent;
}
.hero-nav.next::before {
    top: -20px;
    border-bottom-right-radius: 20px;
    box-shadow: 10px 10px 0 10px var(--cream);
}
.hero-nav.next::after {
    bottom: -20px;
    border-top-right-radius: 20px;
    box-shadow: 10px -10px 0 10px var(--cream);
}

/* ── Hero UI Layer (Bottom Cards) ── */
.hero-ui-layer {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 40px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    z-index: 10;
    pointer-events: none;
}
.hero-left-content {
    max-width: 300px;
    color: #fff;
    pointer-events: auto;
}
.hero-left-content p {
    font-size: 0.9rem;
    line-height: 1.5;
    margin-bottom: 20px;
    font-weight: 400;
    opacity: 0.9;
}
.hero-btn-pill {
    background: transparent;
    color: #fff;
    padding: 10px 28px;
    border-radius: 30px;
    border: 1px solid #fff;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    display: inline-block;
    text-decoration: none;
}
.hero-btn-pill:hover {
    background: #fff;
    color: #000;
}

.hero-right-glass-card {
    max-width: 220px;
    background: rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 16px 20px;
    border-radius: 16px;
    color: #fff;
    pointer-events: auto;
}
.hero-right-glass-card p {
    font-size: 0.8rem;
    line-height: 1.5;
    margin: 0;
    opacity: 0.9;
}

/* ── Mobile Responsive Overrides ── */
@media (max-width: 1024px) {
    #navbar.cutout-mode { padding: 0 20px; }
    #navbar.cutout-mode .nav-left, #navbar.cutout-mode .nav-right { display: none; }
    .hero-ui-layer { flex-direction: column; padding: 20px; align-items: flex-start; gap: 20px; bottom: 40px; }
    .hero-right-glass-card { display: none; }
    .hero-giant-title { font-size: 22vw; }
    .hero-wrapper { padding: 12px; }
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
# Strip out the previous injected hero section CSS
css = re.sub(r'/\* =========================================\s*PIXEL-PERFECT HERO & NAVBAR \(Rebuild\)\s*========================================= \*/.*?/\* ── About Section Base ── \*/', '/* ── About Section Base ── */', css, flags=re.DOTALL)

# Also strip any older generic hero css that might have crept in
css = re.sub(r'/\* ── Hero Section ── \*/.*?/\* ── Marquee ── \*/', '/* ── Marquee ── */', css, flags=re.DOTALL)
css = re.sub(r'/\* ── Layout & Typography ── \*/.*?/\* ── About Section Base ── \*/', '/* ── About Section Base ── */', css, flags=re.DOTALL)

# Inject at the very top (after root)
reset_idx = css.find('/* ── Reset ── */')
if reset_idx != -1:
    css = css[:reset_idx] + new_hero_css + '\n' + css[reset_idx:]
else:
    css = new_hero_css + '\n' + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Bust cache
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'style\.css\?v=[0-9]+', 'style.css?v=5000', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
