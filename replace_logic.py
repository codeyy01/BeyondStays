import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the old hover block
js = re.sub(r'/\* -+\s*ABOUT DESKTOP HOVER INTERACTION\s*-+\s*\*/[\s\S]*?(?=\Z|/\* -+)', '', js)

new_logic = '''
/* -----------------------------------------------------------
   ABOUT DESKTOP AUTO SLIDER
----------------------------------------------------------- */
const aboutMainImg = document.getElementById('aboutMainImg');
const aboutMainTitle = document.getElementById('aboutMainTitle');
const aboutMainDesc = document.getElementById('aboutMainDesc');

if (aboutMainImg && aboutMainTitle && aboutMainDesc) {
    const aboutSlides = [
        {
            img: "./assets/aboutPictures/cozy_staysInKerala.jpeg",
            title: "Cozy Stays in Kerala",
            desc: "Experience the authentic charm and tranquil backwaters of Kerala in our handpicked traditional retreats."
        },
        {
            img: "./assets/aboutPictures/Family_Stays.png",
            title: "Joyful Family Stays",
            desc: "Create unforgettable memories with your loved ones in our spacious, safe, and welcoming family properties."
        },
        {
            img: "./assets/aboutPictures/kashmir_couples.jpeg",
            title: "Romantic Kashmir Escapes",
            desc: "Discover the paradise on earth with intimate, breathtaking stays designed perfectly for couples."
        },
        {
            img: "./assets/aboutPictures/North_trekking.jpeg",
            title: "Thrilling Northern Treks",
            desc: "Fuel your adventurous spirit with our guided trekking experiences and cozy basecamps across the majestic North."
        },
        {
            img: "./assets/aboutPictures/Wayanad_poolStay.jpeg",
            title: "Luxury Pool Stays in Wayanad",
            desc: "Unwind in the lap of nature with exclusive private pool villas nestled in the lush green hills of Wayanad."
        }
    ];

    let currentSlide = 0;

    setInterval(() => {
        aboutMainImg.style.opacity = '0.3';
        aboutMainTitle.style.opacity = '0';
        aboutMainDesc.style.opacity = '0';
        
        setTimeout(() => {
            currentSlide = (currentSlide + 1) % aboutSlides.length;
            aboutMainImg.src = aboutSlides[currentSlide].img;
            aboutMainTitle.innerText = aboutSlides[currentSlide].title;
            aboutMainDesc.innerText = aboutSlides[currentSlide].desc;
            
            aboutMainImg.style.opacity = '1';
            aboutMainTitle.style.opacity = '1';
            aboutMainDesc.style.opacity = '1';
        }, 400);
    }, 4000);
}
'''

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js + '\n' + new_logic)
