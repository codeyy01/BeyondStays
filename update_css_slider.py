import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* Packages Slider Indicators - Glass Pills */
.pkg-slider-indicators {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    margin-top: -10px; /* Pull it slightly closer to the cards */
    padding-bottom: 30px;
}

.pkg-indicator {
    width: 24px;
    height: 8px;
    border-radius: 12px;
    background: rgba(100, 100, 100, 0.15); /* Light transparent base */
    box-shadow: inset 0 1px 3px rgba(255, 255, 255, 0.5), 0 2px 4px rgba(0, 0, 0, 0.05);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
}

.pkg-indicator.active {
    width: 48px;
    background: rgba(43, 110, 70, 0.6); /* Brand green glass */
    border-color: rgba(43, 110, 70, 0.8);
    box-shadow: inset 0 1px 3px rgba(255, 255, 255, 0.4), 0 4px 8px rgba(43, 110, 70, 0.2);
}
'''

css = css + '\n' + new_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
