import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make initial pills slightly larger
css = re.sub(
    r'\.left-pill, \.right-pill \{[\s\S]*?\}',
    '''.left-pill, .right-pill {
    top: 40px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 40px;
    padding: 0 40px;
    height: 56px;
    display: flex;
    align-items: center;
    gap: 40px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}''', css
)

# Remove the old buggy scrolled state css for nav-pieces
css = re.sub(r'/\* -- SCROLLED STATE \(Unified Pill\) -- \*/[\s\S]*?\.logo-tab\.scrolled::before, \.logo-tab\.scrolled::after \{\s*opacity: 0;\s*\}', '', css)

# Hide initial pieces when scrolled
new_css = '''
/* -- SCROLLED STATE VISIBILITY -- */
.nav-piece { transition: opacity 0.4s ease, transform 0.4s ease; }
.nav-piece.hidden { opacity: 0; pointer-events: none; transform: translateY(-20px); }

/* -- UNIFIED STICKY NAVBAR -- */
.navbar-scrolled {
    position: fixed;
    top: -100px; /* Hidden initially */
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 1100px;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 50px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    opacity: 0;
    visibility: hidden;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.navbar-scrolled.visible {
    top: 24px;
    opacity: 1;
    visibility: visible;
}
.navbar-scrolled .nav-inner {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 40px;
}
.navbar-scrolled .nav-links {
    display: flex;
    gap: 32px;
    align-items: center;
}
'''
css += '\n' + new_css

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated.")
