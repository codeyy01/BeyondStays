import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old #destinations and .dest-layout CSS
pattern_to_remove = r'/\* \?\?\? DESTINATIONS & PACKAGES.*?(?=/\* \?\?\?|\Z)'
css = re.sub(pattern_to_remove, '', css, flags=re.DOTALL)

new_css = '''/*  MODERN PACKAGES SLIDER  */
.packages-slider-container {
    margin-top: 40px;
    width: 100%;
    overflow: hidden;
    padding: 20px 0;
}

.packages-slider {
    display: flex;
    gap: 24px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    padding: 0 20px 40px 20px;
    -ms-overflow-style: none;
    scrollbar-width: none;
}
.packages-slider::-webkit-scrollbar {
    display: none;
}

.pkg-card {
    flex: 0 0 calc(33.333% - 16px);
    min-width: 320px;
    background: #fff;
    border-radius: 32px;
    padding: 16px;
    box-shadow: 0 24px 48px rgba(0,0,0,0.06);
    scroll-snap-align: center;
    display: flex;
    flex-direction: column;
    gap: 16px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.pkg-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 32px 64px rgba(0,0,0,0.1);
}

@media (max-width: 1024px) {
    .pkg-card {
        flex: 0 0 calc(50% - 12px);
    }
}
@media (max-width: 600px) {
    .pkg-card {
        flex: 0 0 90%;
    }
}

/* Image Top Section */
.pkg-img-wrap {
    width: 100%;
    aspect-ratio: 4 / 3;
    border-radius: 24px;
    position: relative;
    overflow: hidden;
}

.pkg-img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.pkg-img-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 60%);
    pointer-events: none;
}

.pkg-badges {
    position: absolute;
    top: 16px;
    right: 16px;
    display: flex;
    gap: 8px;
    z-index: 2;
}

.pkg-badge {
    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(4px);
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    color: #333;
}

.pkg-heart {
    width: 32px;
    height: 32px;
    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(4px);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #333;
    cursor: pointer;
    font-size: 1.1rem;
}

.pkg-title-area {
    position: absolute;
    bottom: 24px;
    left: 20px;
    right: 20px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    z-index: 2;
}

.pkg-title {
    color: #fff;
    max-width: 60%;
}
.pkg-title h3 {
    margin: 0 0 4px 0;
    font-size: 1.25rem;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.pkg-location {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.8);
    display: flex;
    align-items: center;
    gap: 4px;
}
.pkg-location svg {
    width: 12px;
    height: 12px;
    fill: currentColor;
}

.pkg-route-btn {
    background: #fff;
    color: #333;
    border: none;
    padding: 8px 16px;
    border-radius: 24px;
    font-size: 0.8rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: background 0.3s ease;
}
.pkg-route-btn:hover {
    background: #f0f0f0;
}

/* Bottom Stats Section */
.pkg-stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    padding: 8px 8px;
}

.pkg-stat {
    display: flex;
    flex-direction: column;
    gap: 4px;
}
.pkg-stat strong {
    font-size: 0.95rem;
    color: #111;
}
.pkg-stat span {
    font-size: 0.75rem;
    color: #777;
}

.pkg-level-bar {
    width: 100%;
    height: 4px;
    background: #eee;
    border-radius: 2px;
    margin-bottom: 4px;
    overflow: hidden;
}
.pkg-level-fill {
    height: 100%;
    background: #4A90E2;
    border-radius: 2px;
}
.pkg-level-fill.moderate { background: #4A90E2; }
.pkg-level-fill.easy { background: #50E3C2; }
.pkg-level-fill.hard { background: #F5A623; }

.pkg-rating {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 0.95rem;
    font-weight: 700;
    color: #111;
}
.pkg-rating svg {
    width: 12px;
    height: 12px;
    fill: #FFB800;
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + new_css)
