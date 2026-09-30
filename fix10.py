import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_cutout = '''#navbar.cutout-mode {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    transform: none !important;
    width: 100% !important;
    max-width: none !important;
    background: transparent !important;
    border: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    box-shadow: none !important;
    z-index: 1000 !important;
}'''

new_cutout = '''#navbar.cutout-mode {
    position: absolute !important;
    top: 0 !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 100% !important;
    max-width: none !important;
    background: transparent !important;
    border: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    box-shadow: none !important;
    z-index: 1000 !important;
}'''
css = css.replace(old_cutout, new_cutout)

# Also let's make sure the background transition of .nav-links is smooth
old_nav_links = '''#navbar.cutout-mode .nav-links {
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

new_nav_links = '''#navbar.cutout-mode .nav-links {
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
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}'''
css = css.replace(old_nav_links, new_nav_links)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
