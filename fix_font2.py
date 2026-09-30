with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css += '''
@media (max-width: 768px) {
    .hero-giant-title {
        font-size: clamp(3.5rem, 18vw, 6rem) !important;
        line-height: 1 !important;
    }
}
'''
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
