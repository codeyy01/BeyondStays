import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_menu = '''.mobile-menu {
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

new_menu = '''.mobile-menu {
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

css = css.replace(old_menu, new_menu)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
