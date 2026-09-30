import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_loader_css = '''#loader {
    position: fixed;
    inset: 0;
    z-index: 9999;
    background-color: var(--green);
    background-image: url('./assets/loader-desktop.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 0.8s ease, visibility 0.8s ease;
}

@media (max-width: 768px) {
    #loader {
        background-image: url('./assets/loader-mobile.png');
    }
}

#loader::before {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(18, 53, 0, 0.75); /* Dark green overlay */
    z-index: 0;
}'''

new_loader_css = '''#loader {
    position: fixed;
    inset: 0;
    z-index: 9999;
    background: #123500;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: opacity 0.8s ease, visibility 0.8s ease;
}

.loader-logo {
    width: 250px;
    margin-bottom: 40px;
    opacity: 0;
    animation: fadeInLogo 1s ease forwards 0.2s;
}

@keyframes fadeInLogo {
    to { opacity: 1; }
}

#loader::before {
    display: none;
}'''

css = css.replace(old_loader_css, new_loader_css)

if 'fadeInLogo' not in css:
    css = re.sub(r'#loader\s*\{[^}]*\}', new_loader_css, css)
    
css += '''
#navbar.cutout-mode .nav-logo-container, .hero-nav {
    transform: translateZ(0);
    will-change: transform;
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
