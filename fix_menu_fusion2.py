import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_menu = '''.mobile-menu {
    position: fixed;
    top: 110px;
    left: 50%;
    transform: translateX(-50%) translateY(-20px);
    width: 90%;
    padding: 40px 0;
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 32px;
    z-index: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}
.mobile-menu.open {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
    pointer-events: auto;
}
.mobile-menu ul {
    display: flex;
    flex-direction: column;
    gap: 24px;
    text-align: center;
}
.mobile-menu a {
    font-family: var(--font-display);
    font-size: 1.8rem;
    color: var(--green);
    font-weight: 600;
    transition: color 0.3s;
}'''

new_menu = '''.mobile-menu {
    position: fixed;
    top: 68px; /* sits right beneath the navbar */
    left: 50%;
    transform: translateX(-50%) translateY(-20px);
    width: 90%;
    padding: 24px 0 40px 0;
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-top: none; /* seamlessly merges with navbar */
    border-radius: 0 0 32px 32px;
    z-index: 700; /* behind navbar */
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}
.mobile-menu.open {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
    pointer-events: auto;
}
.mobile-menu ul {
    display: flex;
    flex-direction: column;
    gap: 28px;
    text-align: center;
}
.mobile-menu a {
    font-family: var(--font-body);
    font-size: 1.25rem;
    color: var(--green);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    transition: color 0.3s;
}'''

css = css.replace(old_menu, new_menu)

fusion_css = '''
/* Fuse the navbar with the dropdown on mobile */
@media (max-width: 768px) {
    #navbar.menu-open {
        border-radius: 32px 32px 0 0 !important;
        border-bottom-color: transparent !important;
        background: rgba(255, 255, 255, 0.12) !important;
    }
}
'''
if '/* Fuse the navbar with the dropdown on mobile */' not in css:
    css += fusion_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
