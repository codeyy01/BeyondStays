import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove the white logo filter override on mobile
bad_filter = '''    #navbar.cutout-mode .nav-logo img {
        filter: brightness(0) invert(1); /* make logo white on mobile over hero */
    }'''
css = css.replace(bad_filter, '')

# 2. Rewrite mobile menu to pop down with glass effect
old_menu = '''.mobile-menu {
    position: fixed;
    inset: 0;
    top: var(--nav-h);
    background: var(--green);
    z-index: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    transform: translateX(-100%);
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.mobile-menu.open {
    transform: translateX(0);
}
.mobile-menu ul {
    display: flex;
    flex-direction: column;
    gap: 32px;
    text-align: center;
}
.mobile-menu a {
    font-family: var(--font-display);
    font-size: 2rem;
    color: var(--white);
    font-weight: 400;
    transition: color 0.3s;
}'''

new_menu = '''.mobile-menu {
    position: fixed;
    inset: 0;
    top: 0;
    padding-top: 100px;
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    z-index: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    transform: translateY(-100%);
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.mobile-menu.open {
    transform: translateY(0);
}
.mobile-menu ul {
    display: flex;
    flex-direction: column;
    gap: 32px;
    text-align: center;
}
.mobile-menu a {
    font-family: var(--font-display);
    font-size: 2.2rem;
    color: var(--green);
    font-weight: 500;
    transition: color 0.3s;
}'''

css = css.replace(old_menu, new_menu)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
