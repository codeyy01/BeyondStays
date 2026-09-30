import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will find the block from .pkg-card { to the end of the file or to the next major section,
# but it's safer to just append to the very end of style_ultimate.css with !important or stronger selectors,
# OR find and replace the specific blocks.
# Let's just find everything after `/* Image Top Section */` and `.pkg-card {` and remove it, then append the new CSS.
# Actually, I'll just look for `.pkg-card {` and find the end of the media queries.

# Let's just append the new CSS at the very end of the file. CSS cascades, so later rules overwrite earlier ones!
# But to be safe, I'll use stronger selectors or just rely on the cascade.
# Let's clean it up properly.
# The old pkg-card CSS starts around line 680 or so. Let's just replace all instances of `.pkg-card` rules with empty string if possible, or just overwrite.

# It's better to just do a smart regex replacement to clean up the old package styles.
old_css_regex = r'\.pkg-card \{.*?(?=\/\*|@media|$)'
# This is risky. Let's just append at the end and rely on the cascade, but I'll redefine everything.

new_css = """
/* =========================================
   PACKAGES SECTION (NEW DESIGN)
   ========================================= */
.packages-slider-container {
    width: 100%;
    overflow: visible; /* to allow box-shadow to show */
    padding: 40px 0 80px 0;
    position: relative;
    margin: 0 auto;
}
.packages-slider {
    display: flex;
    gap: 32px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    padding: 0 40px 40px 40px; /* padding for shadow and edges */
    scrollbar-width: none;
    -ms-overflow-style: none;
}
.packages-slider::-webkit-scrollbar {
    display: none;
}

.pkg-card {
    flex: 0 0 calc(33.333% - 22px) !important;
    min-width: 340px !important;
    height: 480px !important;
    border-radius: 32px !important;
    background: #000 !important;
    position: relative !important;
    overflow: hidden !important;
    border: 6px solid #fff !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.12) !important;
    scroll-snap-align: center !important;
    cursor: pointer !important;
    transform: translateY(0) !important;
    transition: transform 0.4s ease, box-shadow 0.4s ease !important;
    display: block !important; /* override old flex */
    padding: 0 !important; /* override old padding */
}
.pkg-card:hover {
    transform: translateY(-10px) !important;
    box-shadow: 0 30px 60px rgba(0,0,0,0.18) !important;
}

.pkg-bg-img {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    z-index: 1;
    transition: transform 0.7s ease;
}
.pkg-card:hover .pkg-bg-img {
    transform: scale(1.05);
}

.pkg-gradient {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(to top, rgba(15, 20, 15, 0.95) 0%, rgba(15, 20, 15, 0.8) 35%, transparent 100%);
    z-index: 2;
    pointer-events: none;
}

.pkg-content {
    position: absolute;
    bottom: 0; left: 0;
    width: 100%;
    padding: 32px 24px 24px 24px;
    z-index: 3;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
}

.pkg-title {
    font-family: var(--font-display) !important;
    font-weight: 600;
    font-size: 2.2rem !important;
    line-height: 1.1;
    margin-bottom: 4px !important;
    color: #fff !important;
}
.pkg-subtitle {
    font-family: var(--font-body);
    font-size: 1.05rem;
    color: rgba(255, 255, 255, 0.6);
    margin-bottom: 16px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-weight: 400;
}

.pkg-desc {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.7);
    line-height: 1.5;
    margin-bottom: 2px !important;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
.pkg-read-more {
    font-weight: 600;
    color: #fff;
    cursor: pointer;
    font-size: 0.85rem;
    margin-bottom: 20px;
    display: inline-block;
}

.pkg-tags {
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.9);
    font-weight: 500;
}
.pkg-tag {
    display: flex;
    align-items: center;
    gap: 6px;
}
.pkg-tag svg {
    width: 16px;
    height: 16px;
    opacity: 0.7;
}

.pkg-action-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
}
.pkg-btn {
    flex: 1;
    background: #fff;
    color: #111;
    text-align: center;
    padding: 14px 0;
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.95rem;
    text-decoration: none;
    transition: background 0.3s;
    font-family: var(--font-body);
}
.pkg-btn:hover {
    background: var(--cream);
}
.pkg-heart {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background 0.3s;
    flex-shrink: 0;
}
.pkg-heart:hover {
    background: rgba(255, 255, 255, 0.3);
}
.pkg-heart svg {
    width: 20px;
    height: 20px;
    fill: #fff;
}

@media (max-width: 1024px) {
    .pkg-card {
        flex: 0 0 calc(50% - 16px) !important;
    }
}
@media (max-width: 768px) {
    .pkg-card {
        flex: 0 0 85% !important;
        min-width: 280px !important;
    }
    .packages-slider {
        padding: 0 20px 40px 20px;
    }
}
"""

with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('\n' + new_css + '\n')

print("CSS Updated successfully!")
