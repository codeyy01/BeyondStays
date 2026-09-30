import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the about-mobile section
pattern = r'<div class="about-mobile hide-on-desktop">.*?(?=</section>)'

new_html = '''<div class="about-mobile hide-on-desktop">
        <div class="container" style="padding-top: 40px; padding-bottom: 40px;">
            <div class="mob-about-eyebrow">&bull; ABOUT BEYONDSTAYS</div>
            <h2 class="mob-about-title">NOT JUST TRAVEL.<br>A FEELING.</h2>
            
            <div class="mob-about-hero">
                <img src="./assets/aboutPictures/about_Permenant.jpeg" alt="About Beyondstays" />
            </div>
            
            <p class="mob-about-desc">
                Beyondstays transforms everyday journeys into curated experiences - thoughtfully shaped, and made to bring warmth to every travel.
            </p>
            
            <a href="#destinations" class="mob-about-btn">
                <span>DISCOVER BEYONDSTAYS</span>
                <div class="mob-btn-icon">&#8599;</div>
            </a>

            <div class="mob-about-pills">
                <!-- Pill 1 (Image Left) -->
                <div class="mob-pill pill-left">
                    <img src="./assets/aboutPictures/Family_Stays.png" class="mob-pill-img" alt="Family Stays" />
                    <div class="mob-pill-content">
                        <h4>Family Stays</h4>
                        <p>Joyful memories</p>
                    </div>
                </div>
                <!-- Pill 2 (Image Right) -->
                <div class="mob-pill pill-right">
                    <img src="./assets/aboutPictures/North_trekking.jpeg" class="mob-pill-img" alt="Trekking" />
                    <div class="mob-pill-content">
                        <h4>North Treks</h4>
                        <p>Thrilling trails</p>
                    </div>
                </div>
                <!-- Pill 3 (Image Left) -->
                <div class="mob-pill pill-left">
                    <img src="./assets/aboutPictures/kashmir_couples.jpeg" class="mob-pill-img" alt="Couples" />
                    <div class="mob-pill-content">
                        <h4>Couples</h4>
                        <p>Intimate escapes</p>
                    </div>
                </div>
                <!-- Pill 4 (Image Right) -->
                <div class="mob-pill pill-right">
                    <img src="./assets/aboutPictures/cozy_staysInKerala.jpeg" class="mob-pill-img" alt="Kerala" />
                    <div class="mob-pill-content">
                        <h4>Kerala</h4>
                        <p>Cozy backwaters</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
'''

html_cleaned = re.sub(pattern, new_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_cleaned)
