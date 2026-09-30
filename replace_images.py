import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Left side image: replace desk-frame-small content
left_frame_regex = r'<div class="desk-frame-small">[\s\S]*?</div>'
left_frame_new = '''<div class="desk-frame-small" style="background: transparent;">
            <img src="./assets/aboutPictures/about_Permenant.jpeg" alt="About Beyondstays" style="width:100%; height:100%; object-fit:cover; border-radius:12px;" />
        </div>'''
html = re.sub(left_frame_regex, left_frame_new, html, count=1)

# 2. Main green card: replace desk-frame-main content
main_frame_regex = r'<div class="desk-frame-main">[\s\S]*?</div>\s*</div>\s*<div class="desk-logo-wrap">'
main_frame_new = '''<div class="desk-frame-main" style="background: transparent;">
                    <img id="aboutMainImg" src="./assets/aboutPictures/cozy_staysInKerala.jpeg" alt="Cozy Stays in Kerala" style="width:100%; height:100%; object-fit:cover; transition: opacity 0.4s ease;" />
                </div>
                <div class="desk-logo-wrap">'''
html = re.sub(main_frame_regex, main_frame_new, html, count=1)

# 3. Main green card text: replace desk-green-bottom content
bottom_text_regex = r'<div class="desk-green-bottom">[\s\S]*?</div>'
bottom_text_new = '''<div class="desk-green-bottom">
                <h3 id="aboutMainTitle" style="color: white; font-family: var(--font-display); font-size: 1.5rem; margin: 0; transition: opacity 0.4s ease;">Cozy Stays in Kerala</h3>
                <p id="aboutMainDesc" style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem; line-height: 1.5; transition: opacity 0.4s ease;">Experience the authentic charm and tranquil backwaters of Kerala in our handpicked traditional retreats.</p>
            </div>'''
html = re.sub(bottom_text_regex, bottom_text_new, html, count=1)

# 4. Sidebar boxes: replace the 4 desk-side-box elements
sidebar_regex = r'<div class="desk-side-box"></div>\s*<div class="desk-side-box"></div>\s*<div class="desk-side-box"></div>\s*<div class="desk-side-box"></div>'

sidebar_new = '''<div class="desk-side-box about-sidebar-item" data-img="./assets/aboutPictures/Family_Stays.png" data-title="Joyful Family Stays" data-desc="Create unforgettable memories with your loved ones in our spacious, safe, and welcoming family properties." style="background: transparent; overflow: hidden; cursor: pointer;">
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
            </div>'''
html = re.sub(sidebar_regex, sidebar_new, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
