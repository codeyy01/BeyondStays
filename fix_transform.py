import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the trailing hardware acceleration rule
old_hw = '''#navbar.cutout-mode .nav-logo-container, .hero-nav {
    transform: translateZ(0);
    will-change: transform;
}'''

new_hw = '''#navbar.cutout-mode .nav-logo-container {
    transform: translateX(-50%) translateZ(0) !important;
    will-change: transform;
}
.hero-nav {
    transform: translateY(-50%) translateZ(0);
    will-change: transform;
}
/* Ensure the default scrolled state also retains its centering when transitioning */
.nav-logo-container {
    transform: translateX(-50%) translateZ(0);
}'''

css = css.replace(old_hw, new_hw)

# Double check that we don't have stray transforms ruining things
css = css.replace('transform: translateX(-50%);', 'transform: translateX(-50%) translateZ(0);')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
