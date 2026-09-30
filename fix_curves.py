import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the cutout corner
css = css.replace(
'''.about-green-logo-box::before {
    content: '';
    position: absolute;
    bottom: -30px;
    left: 0;
    width: 30px;
    height: 30px;
    border-top-left-radius: 30px;
    box-shadow: -10px -10px 0 10px var(--green);
    background: transparent;
}''',
'''.about-green-logo-box::before {
    content: '';
    position: absolute;
    bottom: -30px;
    left: 30px; /* Shifted to perfectly align with the right edge of about-green-main */
    width: 30px;
    height: 30px;
    border-top-left-radius: 30px;
    box-shadow: -10px -10px 0 10px var(--green);
    background: transparent;
}'''
)

# Fix the logo box bottom right radius
css = css.replace(
'''.about-green-logo-box {
    position: absolute;
    top: 0;
    right: 0;
    width: 170px; /* 140px + 30px overlap to merge smoothly */
    height: 130px;
    background: var(--green);
    border-top-right-radius: 40px;
    border-bottom-left-radius: 30px;
}''',
'''.about-green-logo-box {
    position: absolute;
    top: 0;
    right: 0;
    width: 170px;
    height: 130px;
    background: var(--green);
    border-top-right-radius: 40px;
    border-bottom-left-radius: 30px;
    border-bottom-right-radius: 30px; /* Perfect S-curve rounding */
}'''
)

# Make thumbnails slightly shorter so 5 fit nicely
css = css.replace(
'''.about-thumbnails .thumb {
    width: 100%;
    height: 80px;''',
'''.about-thumbnails .thumb {
    width: 100%;
    height: 65px;'''
)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update HTML cache buster and add 5th dot/thumb
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=6', html)

# Add 5th dot
dots_html = """<div class="about-slider-dots" id="aboutSliderDots">
                                <span class="active"></span>
                                <span></span>
                                <span></span>
                                <span></span>
                                <span></span>
                            </div>"""
html = re.sub(r'<div class="about-slider-dots" id="aboutSliderDots">.*?</div>', dots_html, html, flags=re.DOTALL)

# Add 5th thumb
thumbs_html = """<div class="about-thumbnails" id="aboutThumbnails">
                            <img src="./assets/aboutPictures/Wayanad_poolStay.jpeg" class="thumb active" data-index="0">
                            <img src="./assets/aboutPictures/Family_Stays.png" class="thumb" data-index="1">
                            <img src="./assets/aboutPictures/North_trekking.jpeg" class="thumb" data-index="2">
                            <img src="./assets/aboutPictures/kashmir_couples.jpeg" class="thumb" data-index="3">
                            <img src="./assets/aboutPictures/cozy_staysInKerala.jpeg" class="thumb" data-index="4">
                        </div>"""
html = re.sub(r'<div class="about-thumbnails" id="aboutThumbnails">.*?</div>', thumbs_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update JS array
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_slides = """const slides = [
        {
            title: "Luxury Pool Stays in Wayanad",
            desc: "Unwind in the lap of nature with exclusive private pool villas nestled in the lush green hills of Wayanad.",
            img: "./assets/aboutPictures/Wayanad_poolStay.jpeg"
        },
        {
            title: "Joyful Family Stays",
            desc: "Create unforgettable memories with your loved ones in our spacious, safe, and welcoming family properties.",
            img: "./assets/aboutPictures/Family_Stays.png"
        },
        {
            title: "Thrilling Northern Treks",
            desc: "Fuel your adventurous spirit with our guided trekking experiences and cozy basecamps across the majestic North.",
            img: "./assets/aboutPictures/North_trekking.jpeg"
        },
        {
            title: "Romantic Kashmir Escapes",
            desc: "Discover the paradise on earth with intimate, breathtaking stays designed perfectly for couples.",
            img: "./assets/aboutPictures/kashmir_couples.jpeg"
        },
        {
            title: "Authentic Backwaters",
            desc: "Experience the authentic charm and tranquil backwaters of Kerala in our handpicked traditional retreats.",
            img: "./assets/aboutPictures/cozy_staysInKerala.jpeg"
        }
    ];"""

js = re.sub(r'const slides = \[.*?\];', new_slides, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Applied S-curve fix and added 5th slider image!")
