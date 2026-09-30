import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update hero-slides for the white bezel
old_slides = '''.hero-slides {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    border-radius: 40px;
    overflow: hidden;
}'''
new_slides = '''.hero-slides {
    position: absolute;
    inset: 20px;
    width: auto;
    height: auto;
    border-radius: 28px;
    overflow: hidden;
    background: #e0e0e0; /* fallback */
}'''
css = css.replace(old_slides, new_slides)
if new_slides not in css:
    # try looser replace
    css = re.sub(r'\.hero-slides\s*\{[^}]*\}', new_slides, css)

# 2. Update nav-logo-container for white tab and fillets
old_logo = '''#navbar.cutout-mode .nav-logo-container {
    position: absolute;
    top: -16px;
    left: 50%;
    transform: translateX(-50%);
    background: #123500;
    padding: 24px 60px 16px 60px;
    border-radius: 0 0 32px 32px;
    display: flex;
    align-items: center;
    justify-content: center;
}'''
new_logo = '''#navbar.cutout-mode .nav-logo-container {
    position: absolute;
    top: 0px;
    left: 50%;
    transform: translateX(-50%);
    background: #ffffff;
    padding: 16px 60px 16px 60px;
    border-radius: 0 0 32px 32px;
    display: flex;
    align-items: center;
    justify-content: center;
}
#navbar.cutout-mode .nav-logo-container::before,
#navbar.cutout-mode .nav-logo-container::after {
    content: '';
    position: absolute;
    top: 20px;
    width: 24px;
    height: 24px;
}
#navbar.cutout-mode .nav-logo-container::before {
    left: -24px;
    background: radial-gradient(circle at bottom left, transparent 24px, #ffffff 24px);
}
#navbar.cutout-mode .nav-logo-container::after {
    right: -24px;
    background: radial-gradient(circle at bottom right, transparent 24px, #ffffff 24px);
}'''
css = css.replace(old_logo, new_logo)

# 3. Update arrow tabs
old_arrows = '''.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 56px;
    height: 96px;
    background: #123500;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.8rem;
    color: #ffffff;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}
.hero-nav.prev {
    left: -1px;
    border-radius: 0 24px 24px 0;
}
.hero-nav.next {
    right: -1px;
    border-radius: 24px 0 0 24px;
}'''
new_arrows = '''.hero-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 64px;
    height: 100px;
    background: #ffffff;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.5rem;
    color: #123500;
}
.hero-nav::before, .hero-nav::after {
    content: '';
    position: absolute;
    width: 24px;
    height: 24px;
}
.hero-nav.prev {
    left: 0;
    border-radius: 0 24px 24px 0;
}
.hero-nav.prev::before {
    left: 20px;
    top: -24px;
    background: radial-gradient(circle at top right, transparent 24px, #ffffff 24px);
}
.hero-nav.prev::after {
    left: 20px;
    bottom: -24px;
    background: radial-gradient(circle at bottom right, transparent 24px, #ffffff 24px);
}
.hero-nav.next {
    right: 0;
    border-radius: 24px 0 0 24px;
}
.hero-nav.next::before {
    right: 20px;
    top: -24px;
    background: radial-gradient(circle at top left, transparent 24px, #ffffff 24px);
}
.hero-nav.next::after {
    right: 20px;
    bottom: -24px;
    background: radial-gradient(circle at bottom left, transparent 24px, #ffffff 24px);
}'''
css = css.replace(old_arrows, new_arrows)

# Ensure the logo in the html is green since background is white again!
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('<img src="./assets/nav-logo-white.png" id="navLogo" alt="Beyondstays Logo" />', '<img src="./assets/nav-logo-green.png" id="navLogo" alt="Beyondstays Logo" />')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

