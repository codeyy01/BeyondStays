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
    border-radius: 40px;
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
    font-family: var(--font-display);
    font-size: 14vw;
    font-weight: 800;
    line-height: 0.85;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: -2px;
    pointer-events: none;
    opacity: 0.95;
    text-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

/* ── Cutout Mode Navbar (Initial State) ── */
#navbar.cutout-mode {
    position: absolute;
    top: 30px;
    left: 0;
    width: 100%;
    z-index: 100;
    padding: 0 40px;
    pointer-events: none;
    display: flex;
    justify-content: center;
}
#navbar.cutout-mode .nav-inner {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 100%;
    padding: 0;
}
#navbar.cutout-mode .nav-left,
#navbar.cutout-mode .nav-right {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 40px;
    padding: 0 30px;
    height: 50px;
    display: flex;
    align-items: center;
    pointer-events: auto;
    gap: 32px;
}

/* Logo Cutout (Top Center) */
#navbar.cutout-mode .nav-logo-container {
    position: absolute;
    top: -30px; /* Pull up to touch the hero-frame top edge */
    left: 50%;
    transform: translateX(-50%);
    background: var(--cream);
    padding: 20px 40px 15px;
    border-bottom-left-radius: 30px;
    border-bottom-right-radius: 30px;
    pointer-events: auto;
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
    box-shadow: 15px -15px 0 15px var(--cream);
}
#navbar.cutout-mode .nav-logo-container::after {
    right: -30px;
    border-top-left-radius: 30px;
    box-shadow: -15px -15px 0 15px var(--cream);
}

/* ── Scrolled Navbar (Unified State) ── */
#navbar.scrolled {
    position: fixed;
    top: 15px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 1000px;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 50px;
    padding: 10px 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    display: flex;
    justify-content: center;
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
    font-size: 0.9rem;
    font-weight: 600;
    color: #fff;
    transition: color 0.3s;
}
#navbar.scrolled .nav-links a {
    color: var(--text);
}
.nav-cta {
    background: #fff;
    color: var(--green) !important;
    padding: 8px 24px;
    border-radius: 30px;
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
    font-size: 1.2rem;
}
.hero-nav.prev {
    left: 0;
    padding: 15px 15px 15px 5px;
    width: 45px;
    height: 90px;
    border-top-right-radius: 35px;
    border-bottom-right-radius: 35px;
}
.hero-nav.prev::before, .hero-nav.prev::after {
    content: '';
    position: absolute;
    left: 0;
    width: 30px;
    height: 30px;
    background: transparent;
}
.hero-nav.prev::before {
    top: -30px;
    border-bottom-left-radius: 30px;
    box-shadow: -15px 15px 0 15px var(--cream);
}
.hero-nav.prev::after {
    bottom: -30px;
    border-top-left-radius: 30px;
    box-shadow: -15px -15px 0 15px var(--cream);
}

.hero-nav.next {
    right: 0;
    padding: 15px 5px 15px 15px;
    width: 45px;
    height: 90px;
    border-top-left-radius: 35px;
    border-bottom-left-radius: 35px;
}
.hero-nav.next::before, .hero-nav.next::after {
    content: '';
    position: absolute;
    right: 0;
    width: 30px;
    height: 30px;
    background: transparent;
}
.hero-nav.next::before {
    top: -30px;
    border-bottom-right-radius: 30px;
    box-shadow: 15px 15px 0 15px var(--cream);
}
.hero-nav.next::after {
    bottom: -30px;
    border-top-right-radius: 30px;
    box-shadow: 15px -15px 0 15px var(--cream);
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
    max-width: 320px;
    color: #fff;
    pointer-events: auto;
}
.hero-left-content p {
    font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 24px;
    font-weight: 500;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
}
.hero-btn-pill {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    color: #fff;
    padding: 14px 32px;
    border-radius: 30px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-weight: 600;
    font-size: 0.95rem;
    transition: background 0.3s ease;
    display: inline-block;
}
.hero-btn-pill:hover {
    background: rgba(0, 0, 0, 0.6);
}

.hero-right-glass-card {
    max-width: 250px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 24px;
    border-radius: 20px;
    color: #fff;
    pointer-events: auto;
    text-shadow: 0 1px 5px rgba(0,0,0,0.2);
}
.hero-right-glass-card p {
    font-size: 0.85rem;
    line-height: 1.6;
    margin: 0;
}

/* ── Mobile Responsive Overrides ── */
@media (max-width: 1024px) {
    #navbar.cutout-mode { padding: 0 20px; }
    #navbar.cutout-mode .nav-left, #navbar.cutout-mode .nav-right { display: none; }
    .hero-ui-layer { flex-direction: column; padding: 20px; align-items: flex-start; gap: 20px; bottom: 40px; }
    .hero-right-glass-card { display: none; }
    .hero-giant-title { font-size: 18vw; }
    .hero-wrapper { padding: 10px; }
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will prepend this at the very top of style.css (after the :root variables)
# to completely override any conflicting generic styles from my previous script.
idx = css.find('/* ── Layout & Typography ── */')
if idx != -1:
    end_idx = css.find('/* ── About Section Base ── */')
    if end_idx != -1:
        # We found the block I added in restore_base_css.py! Let's replace just the hero/navbar part of it.
        # Actually, it's safer to just inject it after the variables.
        pass

# Let's cleanly inject it after the :root and general resets.
reset_idx = css.find('/* ── Loader ── */')
if reset_idx != -1:
    css = css[:reset_idx] + new_hero_css + '\n' + css[reset_idx:]
else:
    css = new_hero_css + '\n' + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Injected perfect hero CSS!")
