import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

correct_right_html = '''<div class="about-desk-right reveal-right">
        <div class="desk-green-main">
            <div class="desk-frame-main" style="background: transparent;">
                <img id="aboutMainImg" src="./assets/aboutPictures/cozy_staysInKerala.jpeg" alt="Cozy Stays in Kerala" style="width:100%; height:100%; object-fit:cover; border-radius:16px; transition: opacity 0.4s ease;" />
            </div>
            <div class="desk-green-bottom">
                <h3 id="aboutMainTitle" style="color: white; font-family: var(--font-display); font-size: 1.5rem; margin: 0; transition: opacity 0.4s ease;">Cozy Stays in Kerala</h3>
                <p id="aboutMainDesc" style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem; line-height: 1.5; transition: opacity 0.4s ease;">Experience the authentic charm and tranquil backwaters of Kerala in our handpicked traditional retreats.</p>
            </div>
        </div>
        <div class="desk-sidebar">
            <div class="desk-logo-box">
                <img src="./assets/nav-logo-white.png" alt="Beyondstays" />
            </div>
            <div class="desk-side-box about-sidebar-item" data-img="./assets/aboutPictures/Family_Stays.png" data-title="Joyful Family Stays" data-desc="Create unforgettable memories with your loved ones in our spacious, safe, and welcoming family properties." style="background: transparent; overflow: hidden; cursor: pointer;">
                <img src="./assets/aboutPictures/Family_Stays.png" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" class="hover-zoom" />
            </div>
            <div class="desk-side-box about-sidebar-item" data-img="./assets/aboutPictures/kashmir_couples.jpeg" data-title="Romantic Kashmir Escapes" data-desc="Discover the paradise on earth with intimate, breathtaking stays designed perfectly for couples." style="background: transparent; overflow: hidden; cursor: pointer;">
                <img src="./assets/aboutPictures/kashmir_couples.jpeg" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" class="hover-zoom" />
            </div>
            <div class="desk-side-box about-sidebar-item" data-img="./assets/aboutPictures/North_trekking.jpeg" data-title="Thrilling Northern Treks" data-desc="Fuel your adventurous spirit with our guided trekking experiences and cozy basecamps across the majestic North." style="background: transparent; overflow: hidden; cursor: pointer;">
                <img src="./assets/aboutPictures/North_trekking.jpeg" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" class="hover-zoom" />
            </div>
            <div class="desk-side-box about-sidebar-item" data-img="./assets/aboutPictures/Wayanad_poolStay.jpeg" data-title="Luxury Pool Stays in Wayanad" data-desc="Unwind in the lap of nature with exclusive private pool villas nestled in the lush green hills of Wayanad." style="background: transparent; overflow: hidden; cursor: pointer;">
                <img src="./assets/aboutPictures/Wayanad_poolStay.jpeg" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" class="hover-zoom" />
            </div>
        </div>
    </div>'''

html = re.sub(r'<div class="about-desk-right reveal-right">[\s\S]*?</div>\s*</div>\s*</div>\s*<div class="about-mobile hide-on-desktop">', correct_right_html + '\n</div>\n    <div class="about-mobile hide-on-desktop">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
