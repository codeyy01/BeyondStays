import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = """
    <!-- BEAUTIFUL TYPOGRAPHY BREAK -->
    <section class="quote-break-section reveal-up">
        <div class="container" style="text-align: center; max-width: 800px; margin: 0 auto;">
            <h2 class="quote-break-text">CHOOSE THE PATH<br><span class="italic-serif">less traveled</span></h2>
            <p class="quote-break-sub">Immerse yourself in handpicked destinations designed to elevate your senses and reconnect you with the extraordinary.</p>
        </div>
    </section>

    <section id="destinations" """

html = html.replace('<section id="destinations"', new_html)
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=12', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css = """
/* =========================================
   TYPOGRAPHY BREAK SECTION
   ========================================= */
.quote-break-section {
    padding: 0 0 60px 0; /* Fills the empty space between About and Packages */
    margin-top: -20px;
    text-align: center;
}
.quote-break-text {
    font-family: 'Anton', sans-serif;
    font-size: 5.5rem;
    line-height: 0.95;
    color: var(--green);
    margin-bottom: 24px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.quote-break-text .italic-serif {
    font-family: var(--font-display); /* Fraunces */
    font-style: italic;
    font-weight: 400;
    font-size: 4.5rem;
    color: var(--gold);
    letter-spacing: 0;
    text-transform: lowercase;
    display: block;
    margin-top: -10px;
}
.quote-break-sub {
    font-family: var(--font-body);
    font-size: 1.15rem;
    color: var(--text-muted);
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}

@media (max-width: 1024px) {
    .quote-break-text { font-size: 4.5rem; }
    .quote-break-text .italic-serif { font-size: 3.8rem; }
}
@media (max-width: 768px) {
    .quote-break-section { padding-top: 40px; padding-bottom: 20px; }
    .quote-break-text { font-size: 3rem; }
    .quote-break-text .italic-serif { font-size: 2.8rem; }
    .quote-break-sub { font-size: 1rem; padding: 0 20px; }
}
"""

with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css + '\n')

print("Typography break added successfully!")
