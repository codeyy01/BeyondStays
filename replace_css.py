import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Delete everything after /* --- NEW DESKTOP ABOUT LAYOUT --- */
idx = css.find('/* --- NEW DESKTOP ABOUT LAYOUT --- */')
if idx != -1:
    css = css[:idx]

new_css = '''/* --- NEW DESKTOP ABOUT LAYOUT --- */
.hide-on-mobile { display: block; }
.hide-on-desktop { display: none; }

@media (max-width: 1024px) {
    .hide-on-mobile { display: none !important; }
    .hide-on-desktop { display: block !important; }
}

.about-desktop {
    display: grid;
    grid-template-columns: 1fr 1.6fr;
    gap: 60px;
    align-items: center;
}

.about-desk-left {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.desk-eyebrow {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
}

.desk-title {
    font-family: var(--font-body); /* Changed to sans-serif */
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.1;
    color: var(--text);
    text-transform: uppercase;
}

.desk-frame-small {
    width: 100%;
    max-width: 340px; /* Narrower width */
    height: 180px;
    background: #e0e0e0;
    border-radius: 12px;
    margin: 16px 0;
}

.desk-body {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--text-muted);
    max-width: 90%;
}

.desk-btn {
    display: inline-flex;
    align-items: center;
    gap: 16px;
    padding: 8px 8px 8px 24px;
    border: 1px solid #ccc;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    width: fit-content;
    background: #fff;
    color: var(--text);
    transition: all 0.3s ease;
}

.desk-btn:hover {
    background: #f5f5f5;
}

.desk-btn-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: #475338;
    color: #fff;
    border-radius: 50%;
    font-size: 1.2rem;
}

.about-desk-right {
    display: flex;
    align-items: flex-start;
    gap: 0;
    height: 100%;
}

.desk-green-main {
    flex: 1;
    background: #143505;
    border-radius: 24px 0 24px 24px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 40px;
    height: 100%;
}

.desk-frame-main {
    flex: 1;
    background: #ccc;
    height: 380px;
    border-radius: 16px;
    position: relative;
    overflow: hidden;
}

.desk-frame-dots {
    position: absolute;
    bottom: 16px;
    right: 16px;
    display: flex;
    gap: 4px;
}

.desk-frame-dots span {
    display: block;
    width: 6px;
    height: 6px;
    background: #fff;
    border-radius: 50%;
    opacity: 0.5;
}

.desk-frame-dots span:first-child {
    width: 20px;
    border-radius: 10px;
    opacity: 1;
}

.desk-green-bottom {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding-bottom: 10px;
}

.desk-line {
    height: 10px;
    width: 50%;
    background: #fff;
    border-radius: 10px;
}

.desk-sidebar {
    width: 140px;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.desk-logo-box {
    background: #143505;
    border-radius: 0 24px 24px 0;
    padding: 24px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    /* Height must be exactly enough to match the top boundary naturally, flex will do this if not specified, but let's make it a fixed height */
    height: 140px;
}

.desk-logo-box img {
    width: 100%;
    height: auto;
}

.desk-side-box {
    width: calc(100% - 24px);
    aspect-ratio: 1;
    background: #d6d6d6;
    border-radius: 16px;
    margin-left: 24px;
}

'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css + new_css)
