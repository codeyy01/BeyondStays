import re

html_mobile_cards = """
            <!-- Mobile About Cards (Visible only on max-width: 768px) -->
            <div class="about-mobile-cards">
                <div class="mobile-pill-card left-img">
                    <img src="./assets/aboutPictures/Wayanad_poolStay.jpeg" class="mobile-pill-img">
                    <div class="mobile-pill-text">
                        <h4>Luxury Pool Stays</h4>
                        <p>Unwind with exclusive private pool villas in Wayanad.</p>
                    </div>
                </div>
                
                <div class="mobile-pill-card right-img">
                    <div class="mobile-pill-text">
                        <h4>Joyful Family Stays</h4>
                        <p>Create unforgettable memories with your loved ones.</p>
                    </div>
                    <img src="./assets/aboutPictures/Family_Stays.png" class="mobile-pill-img">
                </div>

                <div class="mobile-pill-card left-img">
                    <img src="./assets/aboutPictures/North_trekking.jpeg" class="mobile-pill-img">
                    <div class="mobile-pill-text">
                        <h4>Northern Treks</h4>
                        <p>Fuel your spirit with guided trekking experiences.</p>
                    </div>
                </div>

                <div class="mobile-pill-card right-img">
                    <div class="mobile-pill-text">
                        <h4>Kashmir Escapes</h4>
                        <p>Discover paradise with intimate, breathtaking stays.</p>
                    </div>
                    <img src="./assets/aboutPictures/kashmir_couples.jpeg" class="mobile-pill-img">
                </div>

                <div class="mobile-pill-card left-img">
                    <img src="./assets/aboutPictures/cozy_staysInKerala.jpeg" class="mobile-pill-img">
                    <div class="mobile-pill-text">
                        <h4>Authentic Backwaters</h4>
                        <p>Experience the tranquil charm of Kerala's backwaters.</p>
                    </div>
                </div>
            </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert right after the closing </div> of .about-right
html = html.replace('</div>\n        </div>\n    </section>', '</div>\n' + html_mobile_cards + '\n        </div>\n    </section>')

# Update cache buster
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=7', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

css_code = """
/* =========================================
   ABOUT SECTION (MOBILE DESIGN)
   ========================================= */
.about-mobile-cards {
    display: none;
}

@media (max-width: 768px) {
    .about-right {
        display: none !important;
    }
    .about-container {
        gap: 32px;
    }
    .about-mobile-cards {
        display: flex;
        flex-direction: column;
        gap: 24px;
        width: 100%;
        margin-top: 16px;
    }
    .mobile-pill-card {
        position: relative;
        width: 100%;
        height: 180px;
        border-radius: 90px;
        background: linear-gradient(to right, #cfd3cd, #5b6c4b);
        display: flex;
        align-items: center;
    }
    .mobile-pill-img {
        position: absolute;
        top: 0;
        width: 55%;
        height: 100%;
        object-fit: cover;
        border-radius: 90px;
        box-shadow: 0 0 20px rgba(0,0,0,0.35);
        z-index: 2;
    }
    .mobile-pill-card.left-img .mobile-pill-img {
        left: 0;
    }
    .mobile-pill-card.right-img .mobile-pill-img {
        right: 0;
    }
    
    .mobile-pill-text {
        position: relative;
        width: 45%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 20px;
        z-index: 1;
        box-sizing: border-box;
    }
    .mobile-pill-card.left-img .mobile-pill-text {
        margin-left: 55%;
        text-align: right;
        color: #fff; /* Dark green background */
    }
    .mobile-pill-card.right-img .mobile-pill-text {
        margin-right: 55%;
        text-align: left;
        color: #1a1a1a; /* Light silver background */
    }
    .mobile-pill-text h4 {
        font-family: var(--font-display);
        font-size: 1.05rem;
        margin-bottom: 6px;
        line-height: 1.2;
    }
    .mobile-pill-text p {
        font-size: 0.75rem;
        line-height: 1.4;
        opacity: 0.9;
        font-family: var(--font-body);
        margin: 0;
    }
}
"""

with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_code + '\n')

print("Applied mobile about section!")
