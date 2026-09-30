import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* --- NEW MOBILE ABOUT SECTION --- */
.mob-about-eyebrow {
    font-size: 0.75rem;
    font-weight: 700;
    color: #889380;
    letter-spacing: 1px;
    margin-bottom: 12px;
    text-transform: uppercase;
}

.mob-about-title {
    font-family: var(--font-heading);
    font-size: 2.2rem;
    font-weight: 900;
    color: #111;
    line-height: 1.1;
    margin-bottom: 24px;
    text-transform: uppercase;
    letter-spacing: -0.5px;
}

.mob-about-hero {
    width: 100%;
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 24px;
}

.mob-about-hero img {
    width: 100%;
    display: block;
    object-fit: cover;
    aspect-ratio: 16 / 9;
}

.mob-about-desc {
    font-size: 0.95rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 24px;
}

.mob-about-btn {
    display: inline-flex;
    align-items: center;
    background: #fff;
    color: #111;
    padding: 8px 8px 8px 24px;
    border-radius: 32px;
    text-decoration: none;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    border: 1px solid #eee;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 40px;
}

.mob-btn-icon {
    width: 32px;
    height: 32px;
    background: #3B5241; /* Dark Green */
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 16px;
    font-size: 1.1rem;
}

/* Stacking Pills */
.mob-about-pills {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.mob-pill {
    position: relative;
    width: 100%;
    height: 120px;
    border-radius: 60px;
    display: flex;
    align-items: center;
    overflow: visible; /* so shadow can bleed if needed */
}

/* Background Colors alternating */
.mob-pill:nth-child(odd) {
    background: #738466; /* Solid sage green */
}
.mob-pill:nth-child(even) {
    background: linear-gradient(to right, #e0e4e1, #a3b0a0); /* Silver to green */
}

.mob-pill-img {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 65%;
    height: 100%;
    border-radius: 60px;
    object-fit: cover;
    z-index: 2;
}

.mob-pill-content {
    position: absolute;
    width: 35%;
    z-index: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.mob-pill-content h4 {
    margin: 0 0 4px 0;
    font-size: 0.85rem;
    font-weight: 700;
    color: #fff;
}
.mob-pill-content p {
    margin: 0;
    font-size: 0.7rem;
    color: rgba(255,255,255,0.8);
}

/* Image on Left */
.mob-pill.pill-left .mob-pill-img {
    left: 0;
    box-shadow: 6px 0 16px rgba(0,0,0,0.25);
}
.mob-pill.pill-left .mob-pill-content {
    right: 20px;
    align-items: flex-end;
    text-align: right;
}

/* Image on Right */
.mob-pill.pill-right .mob-pill-img {
    right: 0;
    box-shadow: -6px 0 16px rgba(0,0,0,0.25);
}
.mob-pill.pill-right .mob-pill-content {
    left: 24px;
    align-items: flex-start;
    text-align: left;
}
.mob-pill:nth-child(even) .mob-pill-content h4 {
    color: #333;
}
.mob-pill:nth-child(even) .mob-pill-content p {
    color: #555;
}

'''

css = css + '\n' + new_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
