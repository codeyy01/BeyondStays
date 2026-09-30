import re

css_code = """
/* =========================================
   ABOUT SECTION (MOCKUP DESIGN)
   ========================================= */

.about-container {
    display: grid;
    grid-template-columns: 1fr 1.25fr;
    gap: 60px;
    align-items: center;
    max-width: 1300px;
    margin: 0 auto;
}

/* Left Side */
.about-left {
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.about-eyebrow {
    font-size: 0.85rem;
    font-weight: 700;
    color: #888;
    letter-spacing: 2px;
}
.about-title {
    font-size: 3.8rem;
    line-height: 1.1;
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    color: #111;
}
.about-permanent-img {
    width: 100%;
    border-radius: 20px;
    height: 240px;
    object-fit: cover;
}
.about-desc {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #555;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
}
.about-btn {
    display: inline-flex;
    align-items: center;
    gap: 20px;
    border: 1px solid #ddd;
    border-radius: 50px;
    padding: 8px 8px 8px 24px;
    align-self: flex-start;
    background: #fff;
    color: #111;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}
.about-btn:hover {
    border-color: var(--green);
}
.about-btn .btn-icon {
    background: #3c4927; /* Dark olive green */
    color: #fff;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    transition: background 0.3s ease;
}
.about-btn:hover .btn-icon {
    background: var(--green);
}

/* Right Side (Slider) */
.about-right {
    position: relative;
    padding: 0; /* Removing padding so the green shapes align perfectly */
    min-height: 560px;
    display: flex;
}

/* The Green Background Shape */
.about-green-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
}
.about-green-main {
    position: absolute;
    top: 0;
    left: 0;
    width: calc(100% - 140px); /* Leave exactly 140px on the right for thumbnails */
    height: 100%;
    background: var(--green);
    border-radius: 40px;
}
.about-green-logo-box {
    position: absolute;
    top: 0;
    right: 0;
    width: 170px; /* 140px + 30px overlap to merge smoothly */
    height: 130px;
    background: var(--green);
    border-top-right-radius: 40px;
    border-bottom-left-radius: 30px;
}
/* The inverted corner cutout below the logo box */
.about-green-logo-box::before {
    content: '';
    position: absolute;
    bottom: -30px;
    left: 0;
    width: 30px;
    height: 30px;
    border-top-left-radius: 30px;
    box-shadow: -10px -10px 0 10px var(--green);
    background: transparent;
}

/* Content over the green shape */
.about-right-content {
    position: relative;
    z-index: 2;
    display: flex;
    width: 100%;
    height: 100%;
}

.about-slider-main {
    width: calc(100% - 140px); /* Exactly matches the main green background */
    padding: 32px; /* Inner padding inside the green box */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.about-main-img {
    width: 100%;
    height: 420px;
    object-fit: cover;
    border-radius: 24px;
    transition: opacity 0.4s ease;
}
.about-slider-bottom {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding: 24px 0 0 0;
}
.about-slider-text {
    max-width: 80%;
    color: #fff;
}
.about-slider-text h3 {
    font-family: var(--font-display);
    font-size: 1.5rem;
    margin-bottom: 8px;
}
.about-slider-text p {
    font-size: 0.85rem;
    line-height: 1.5;
    opacity: 0.9;
}
.about-slider-dots {
    display: flex;
    gap: 8px;
    align-items: center;
    padding-bottom: 8px;
}
.about-slider-dots span {
    display: block;
    width: 8px;
    height: 8px;
    background: rgba(255,255,255,0.4);
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s;
}
.about-slider-dots span.active {
    width: 24px;
    border-radius: 10px;
    background: #fff;
}

.about-sidebar {
    width: 140px; /* Fills the exact gap */
    display: flex;
    flex-direction: column;
}
.about-logo-box {
    height: 130px; /* Matches the green logo box exactly */
    display: flex;
    align-items: center;
    justify-content: center;
}
.about-logo-box img {
    width: 100px;
}
.about-thumbnails {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 16px 16px 0 16px; /* Space the thumbnails nicely inside their column */
}
.about-thumbnails .thumb {
    width: 100%;
    height: 80px;
    object-fit: cover;
    border-radius: 20px;
    cursor: pointer;
    transition: transform 0.3s;
    border: 2px solid transparent;
}
.about-thumbnails .thumb:hover {
    transform: scale(1.05);
}
.about-thumbnails .thumb.active {
    border-color: var(--green);
}

@media (max-width: 1024px) {
    .about-container { grid-template-columns: 1fr; }
    .about-right { padding: 16px; }
    .about-green-main { width: 100%; border-radius: 24px; }
    .about-green-logo-box { display: none; }
    .about-right-content { flex-direction: column; }
    .about-slider-main { width: 100%; padding: 16px; }
    .about-sidebar { width: 100%; flex-direction: row; justify-content: space-between; align-items: center; padding: 0; }
    .about-logo-box { display: none; }
    .about-thumbnails { flex-direction: row; width: 100%; overflow-x: auto; padding: 16px 0 0 0; }
    .about-thumbnails .thumb { width: 80px; height: 80px; }
}
"""

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the About section CSS
import re
match = re.search(r'/\* =========================================\s*ABOUT SECTION.*', css, flags=re.DOTALL)
if match:
    css = css[:match.start()] + css_code
    with open('style_ultimate.css', 'w', encoding='utf-8') as f:
        f.write(css)
    
    # Bump cache
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=5', html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced About CSS and bumped cache!")
else:
    print("Could not find About CSS block.")
