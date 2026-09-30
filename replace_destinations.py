import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<!-- DESTINATIONS -->\s*<section id="destinations".*?</section>'
match = re.search(pattern, html, flags=re.DOTALL)
if match:
    print("Found!")
    
    new_html = '''<!-- DESTINATIONS -->
    <section id="destinations" class="section">
        <div class="container">
            <div class="dest-header reveal-up">
                <div class="section-eyebrow">Our Packages</div>
                <h2 class="section-title">Find Your<br /><em>Perfect Escape</em></h2>
                <p class="section-sub">Swipe to explore our carefully curated travel packages.</p>
            </div>
            
            <!-- Modern Slider -->
            <div class="packages-slider-container reveal-up">
                <div class="packages-slider" id="packagesSlider">
                    <!-- Packages will be injected here via JS -->
                </div>
            </div>
        </div>
    </section>'''
    
    html = html.replace(match.group(0), new_html)
    
    with open('index.html', 'w', encoding='utf-8') as fw:
        fw.write(html)
    print("Replaced!")
else:
    print("Not found!")
