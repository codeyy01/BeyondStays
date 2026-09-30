import re

new_css = '''
/* --- RECOVERED TESTIMONIALS CSS --- */
.testi-slider-wrap {
    position: relative;
    overflow: hidden;
    padding: 20px 0;
}
.testi-track {
    display: flex;
    gap: 20px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scrollbar-width: none;
    -ms-overflow-style: none;
}
.testi-track::-webkit-scrollbar {
    display: none;
}
.testi-card {
    min-width: 320px;
    background: #fff;
    padding: 32px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    scroll-snap-align: center;
    display: flex;
    flex-direction: column;
}
.testi-stars {
    color: #f59e0b;
    font-size: 1.2rem;
    margin-bottom: 16px;
}
.testi-card p {
    font-size: 1rem;
    line-height: 1.6;
    color: #555;
    margin-bottom: 24px;
    flex-grow: 1;
}
.testi-author {
    display: flex;
    align-items: center;
    gap: 16px;
}
.testi-author img {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    object-fit: cover;
}
.testi-author div {
    display: flex;
    flex-direction: column;
}
.testi-author strong {
    color: #111;
    font-size: 0.95rem;
}
.testi-author span {
    color: #777;
    font-size: 0.8rem;
}
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the wrong reviews css I injected
css = re.sub(r'/\* Reviews / Testimonials \*/.*?/\* WhatsApp FAB \*/', new_css + '\n/* WhatsApp FAB */', css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
