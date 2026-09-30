import re

html_code = """    <section id="about" class="section section-light">
        <div class="container about-container">
            
            <!-- Left Column -->
            <div class="about-left">
                <div class="about-eyebrow">&bull; ABOUT BEYONDSTAYS</div>
                <h2 class="about-title">NOT JUST TRAVEL.<br>A FEELING.</h2>
                <img src="./assets/aboutPictures/about_Permenant.jpeg" alt="About Beyondstays" class="about-permanent-img">
                <p class="about-desc">Beyondstays transforms everyday journeys into curated experiences - thoughtfully shaped, and made to bring warmth to every travel.</p>
                <a href="#destinations" class="about-btn">
                    <span class="btn-text">DISCOVER BEYONDSTAYS</span>
                    <span class="btn-icon">&#x2197;</span>
                </a>
            </div>

            <!-- Right Column (Slider) -->
            <div class="about-right">
                <!-- Complex Green Background Shape -->
                <div class="about-green-bg">
                    <div class="about-green-main"></div>
                    <div class="about-green-logo-box"></div>
                </div>

                <!-- Content -->
                <div class="about-right-content">
                    
                    <div class="about-slider-main">
                        <img src="./assets/aboutPictures/Wayanad_poolStay.jpeg" alt="Luxury Pool Stays" class="about-main-img" id="aboutMainImg">
                        <div class="about-slider-bottom">
                            <div class="about-slider-text">
                                <h3 id="aboutMainTitle">Luxury Pool Stays in Wayanad</h3>
                                <p id="aboutMainDesc">Unwind in the lap of nature with exclusive private pool villas nestled in the lush green hills of Wayanad.</p>
                            </div>
                            <div class="about-slider-dots" id="aboutSliderDots">
                                <span class="active"></span>
                                <span></span>
                                <span></span>
                                <span></span>
                            </div>
                        </div>
                    </div>

                    <div class="about-sidebar">
                        <div class="about-logo-box">
                            <img src="./assets/nav-logo-white.png" alt="Beyondstays">
                        </div>
                        <div class="about-thumbnails" id="aboutThumbnails">
                            <img src="./assets/aboutPictures/Family_Stays.png" class="thumb" data-index="0">
                            <img src="./assets/aboutPictures/North_trekking.jpeg" class="thumb" data-index="1">
                            <img src="./assets/aboutPictures/kashmir_couples.jpeg" class="thumb" data-index="2">
                            <img src="./assets/aboutPictures/cozy_staysInKerala.jpeg" class="thumb" data-index="3">
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>"""

css_code = """
/* =========================================
   ABOUT SECTION (MOCKUP DESIGN)
   ========================================= */

.about-container {
    display: grid;
    grid-template-columns: 0.9fr 1.3fr;
    gap: 80px;
    align-items: center;
    max-width: 1300px;
}

/* Left Side */
.about-left {
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.about-eyebrow {
    font-size: 0.85rem;
    font-weight: 700;
    color: #888;
    letter-spacing: 2px;
}
.about-title {
    font-size: 4.2rem;
    line-height: 1.1;
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    color: #111;
}
.about-permanent-img {
    width: 100%;
    border-radius: 16px;
    height: 220px;
    object-fit: cover;
}
.about-desc {
    font-size: 1.15rem;
    line-height: 1.6;
    color: #666;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
}
.about-btn {
    display: inline-flex;
    align-items: center;
    gap: 20px;
    border: 1px solid #ddd;
    border-radius: 50px;
    padding: 8px 8px 8px 24px;
    align-self: flex-start;
    background: #fff;
    color: #111;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}
.about-btn:hover {
    border-color: var(--green);
}
.about-btn .btn-icon {
    background: #3c4927; /* Dark olive green */
    color: #fff;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    transition: background 0.3s ease;
}
.about-btn:hover .btn-icon {
    background: var(--green);
}

/* Right Side (Slider) */
.about-right {
    position: relative;
    padding: 32px;
    min-height: 600px;
}

/* The Green Background Shape */
.about-green-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
}
.about-green-main {
    position: absolute;
    top: 0;
    left: 0;
    width: calc(100% - 130px); /* Leave exactly 130px for thumbnails */
    height: 100%;
    background: var(--green);
    border-radius: 40px;
}
.about-green-logo-box {
    position: absolute;
    top: 0;
    right: 0;
    width: 160px; /* Slightly wider to overlap smoothly */
    height: 140px;
    background: var(--green);
    border-top-right-radius: 40px;
    border-bottom-left-radius: 30px;
}
/* The inverted corner cutout below the logo box */
.about-green-logo-box::before {
    content: '';
    position: absolute;
    bottom: -30px;
    left: 0;
    width: 30px;
    height: 30px;
    border-top-left-radius: 30px;
    box-shadow: -10px -10px 0 10px var(--green);
    background: transparent;
}

/* Content over the green shape */
.about-right-content {
    position: relative;
    z-index: 2;
    display: flex;
    gap: 32px;
    height: 100%;
}

.about-slider-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.about-main-img {
    width: 100%;
    height: 420px;
    object-fit: cover;
    border-radius: 24px;
    transition: opacity 0.4s ease;
}
.about-slider-bottom {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding: 24px 0 0 0;
}
.about-slider-text {
    max-width: 80%;
    color: #fff;
}
.about-slider-text h3 {
    font-family: var(--font-display);
    font-size: 1.6rem;
    margin-bottom: 8px;
}
.about-slider-text p {
    font-size: 0.85rem;
    line-height: 1.6;
    opacity: 0.9;
}
.about-slider-dots {
    display: flex;
    gap: 8px;
    align-items: center;
    padding-bottom: 8px;
}
.about-slider-dots span {
    display: block;
    width: 8px;
    height: 8px;
    background: rgba(255,255,255,0.4);
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s;
}
.about-slider-dots span.active {
    width: 24px;
    border-radius: 10px;
    background: #fff;
}

.about-sidebar {
    width: 110px;
    display: flex;
    flex-direction: column;
}
.about-logo-box {
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 30px;
}
.about-logo-box img {
    width: 100px;
}
.about-thumbnails {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.about-thumbnails .thumb {
    width: 100%;
    height: 80px;
    object-fit: cover;
    border-radius: 20px;
    cursor: pointer;
    transition: transform 0.3s;
    border: 2px solid transparent;
}
.about-thumbnails .thumb:hover {
    transform: scale(1.05);
}
.about-thumbnails .thumb.active {
    border-color: var(--green);
}

@media (max-width: 1024px) {
    .about-container { grid-template-columns: 1fr; }
    .about-right { padding: 16px; }
    .about-green-main { width: 100%; border-radius: 24px; }
    .about-green-logo-box { display: none; }
    .about-right-content { flex-direction: column; }
    .about-sidebar { width: 100%; flex-direction: row; justify-content: space-between; align-items: center; }
    .about-logo-box { display: none; }
    .about-thumbnails { flex-direction: row; width: 100%; overflow-x: auto; }
    .about-thumbnails .thumb { width: 80px; height: 80px; }
}
"""

js_code = """
// About Section Slider Logic
document.addEventListener('DOMContentLoaded', () => {
    const mainImg = document.getElementById('aboutMainImg');
    const mainTitle = document.getElementById('aboutMainTitle');
    const mainDesc = document.getElementById('aboutMainDesc');
    const thumbs = document.querySelectorAll('#aboutThumbnails .thumb');
    const dots = document.querySelectorAll('#aboutSliderDots span');

    const slides = [
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
    ];

    let currentIndex = 0;

    function updateSlider(index) {
        currentIndex = index;
        
        // Fade out
        mainImg.style.opacity = '0';
        mainTitle.style.opacity = '0';
        mainDesc.style.opacity = '0';
        
        setTimeout(() => {
            mainImg.src = slides[index].img;
            mainTitle.textContent = slides[index].title;
            mainDesc.textContent = slides[index].desc;
            
            // Fade in
            mainImg.style.opacity = '1';
            mainTitle.style.opacity = '1';
            mainDesc.style.opacity = '1';
        }, 300);

        // Update dots and thumbs
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
        thumbs.forEach((thumb, i) => {
            thumb.classList.toggle('active', i === index);
        });
    }

    thumbs.forEach((thumb, i) => {
        thumb.addEventListener('click', () => updateSlider(i));
    });
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => updateSlider(i));
    });

    // Auto rotate every 5 seconds
    setInterval(() => {
        let next = (currentIndex + 1) % slides.length;
        updateSlider(next);
    }, 5000);
});
"""

import sys
# 1. HTML Replacement
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

about_start = html.find('<section id="about"')
dest_start = html.find('<section id="destinations"')
if about_start != -1 and dest_start != -1:
    html = html[:about_start] + html_code + '\n    ' + html[dest_start:]
    
    # Update cache buster
    html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=4', html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
else:
    print("Could not find boundaries in index.html")
    sys.exit(1)

# 2. CSS Appending
with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_code + '\n')

# 3. JS Appending
with open('script.js', 'a', encoding='utf-8') as f:
    f.write('\n' + js_code + '\n')

print("About section built successfully!")
