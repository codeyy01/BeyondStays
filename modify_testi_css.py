with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- LUXURY TESTIMONIALS REDESIGN --- */
#testimonials {
    background-color: var(--cream) !important;
}
.testi-card {
    position: relative !important;
    background: #fff !important;
    padding: 40px !important;
    border-radius: 24px !important;
    box-shadow: 0 10px 40px rgba(0,0,0,0.04) !important;
    border: 1px solid rgba(0,0,0,0.03) !important;
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.4s ease !important;
    overflow: hidden !important;
    display: flex !important;
    flex-direction: column !important;
}
.testi-card:hover {
    transform: translateY(-10px) !important;
    box-shadow: 0 24px 60px rgba(0,69,38,0.08) !important;
}

/* Massive background quote mark */
.testi-quote-icon {
    position: absolute !important;
    top: 30px !important;
    right: 30px !important;
    width: 80px !important;
    height: 80px !important;
    color: rgba(18, 53, 0, 0.04) !important;
    z-index: 0 !important;
    pointer-events: none !important;
}
.testi-quote-icon svg {
    width: 100% !important;
    height: 100% !important;
}

.testi-stars {
    position: relative !important;
    z-index: 1 !important;
    display: flex !important;
    gap: 4px !important;
    margin-bottom: 24px !important;
}
.testi-stars svg {
    width: 18px !important;
    height: 18px !important;
}

.testi-card p {
    position: relative !important;
    z-index: 1 !important;
    font-size: 1.2rem !important;
    line-height: 1.7 !important;
    color: var(--text) !important;
    font-family: var(--font-display) !important;
    font-style: italic !important;
    margin-bottom: 30px !important;
    flex-grow: 1 !important;
}

.testi-author {
    position: relative !important;
    z-index: 1 !important;
    display: flex !important;
    align-items: center !important;
    gap: 16px !important;
    border-top: 1px solid rgba(0,0,0,0.05) !important;
    padding-top: 24px !important;
}
.testi-author img {
    width: 56px !important;
    height: 56px !important;
    border-radius: 50% !important;
    object-fit: cover !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
}
.testi-author div {
    display: flex !important;
    flex-direction: column !important;
}
.testi-author strong {
    font-family: var(--font-body) !important;
    font-size: 1.05rem !important;
    color: var(--text) !important;
    font-weight: 700 !important;
    margin-bottom: 4px !important;
}
.testi-author span {
    font-size: 0.85rem !important;
    color: var(--green) !important; /* Make the package name pop in green */
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
''')
print("Testimonial CSS appended.")
