import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* -- 3 DISTINCT NAVBAR PIECES (INITIAL) -- */
.nav-piece {
    position: absolute;
    z-index: 100;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Glass Pills */
.left-pill, .right-pill {
    top: 40px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 40px;
    padding: 0 32px;
    height: 50px;
    display: flex;
    align-items: center;
    gap: 32px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}
.left-pill { left: 40px; }
.right-pill { right: 40px; }

/* Logo Tab Cutout */
.logo-tab {
    top: -16px; /* Touch the white frame */
    left: 50%;
    transform: translateX(-50%);
    background: #fff;
    padding: 12px 40px 16px;
    border-bottom-left-radius: 30px;
    border-bottom-right-radius: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.logo-tab::before, .logo-tab::after {
    content: '';
    position: absolute;
    top: 0;
    width: 30px;
    height: 30px;
    background: transparent;
    transition: opacity 0.4s;
}
.logo-tab::before {
    left: -30px;
    border-top-right-radius: 30px;
    box-shadow: 15px -15px 0 15px #fff;
}
.logo-tab::after {
    right: -30px;
    border-top-left-radius: 30px;
    box-shadow: -15px -15px 0 15px #fff;
}

/* -- SCROLLED STATE (Unified Pill) -- */
.nav-piece.scrolled {
    position: fixed;
    top: 24px;
}
.left-pill.scrolled {
    left: calc(50% - 250px);
    transform: translateX(-100%);
    border-radius: 50px 0 0 50px;
    border-right: none;
    padding-right: 20px;
}
.right-pill.scrolled {
    right: calc(50% - 250px);
    transform: translateX(100%);
    border-radius: 0 50px 50px 0;
    border-left: none;
    padding-left: 20px;
}
.logo-tab.scrolled {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 0;
    padding: 0 20px;
    height: 50px;
    top: 24px;
}
.logo-tab.scrolled::before, .logo-tab.scrolled::after {
    opacity: 0;
}
'''

# Find the start of the old navbar CSS
start_idx = css.find('/* -- Navbar (Cutout Mode - Initial) -- */')
end_idx = css.find('/* Nav Links Base */')

if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + new_css + '\n' + css[end_idx:]
    print("Replaced CSS section.")
else:
    print("Could not find markers, appending instead.")
    css += '\n' + new_css

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

