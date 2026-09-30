import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the old auto slider block
js = re.sub(r'/\* -+\s*ABOUT DESKTOP AUTO SLIDER\s*-+\s*\*/[\s\S]*?(?=\Z|/\* -+)', '', js)

new_logic = '''
/* -----------------------------------------------------------
   ABOUT DESKTOP AUTO SLIDER
----------------------------------------------------------- */
const aboutMainImg = document.getElementById('aboutMainImg');
const aboutMainTitle = document.getElementById('aboutMainTitle');
const aboutMainDesc = document.getElementById('aboutMainDesc');
const aboutSidebarItems = document.querySelectorAll('.about-sidebar-item img'); // Get the images directly
const aboutSliderDots = document.querySelectorAll('#aboutSliderDots span');

if (aboutMainImg && aboutMainTitle && aboutMainDesc && aboutSidebarItems.length === 4) {
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
        // Fade out main elements
        aboutMainImg.style.opacity = '0.3';
        aboutMainTitle.style.opacity = '0';
        aboutMainDesc.style.opacity = '0';
        
        // Also fade out sidebar images for a smooth swap
        aboutSidebarItems.forEach(img => img.style.opacity = '0.3');
        
        setTimeout(() => {
            currentSlide = (currentSlide + 1) % aboutSlides.length;
            
            // Update main image and text
            aboutMainImg.src = aboutSlides[currentSlide].img;
            aboutMainTitle.innerText = aboutSlides[currentSlide].title;
            aboutMainDesc.innerText = aboutSlides[currentSlide].desc;
            
            // Update sidebar images with the other 4
            for(let i = 0; i < 4; i++) {
                let sidebarIndex = (currentSlide + i + 1) % aboutSlides.length;
                aboutSidebarItems[i].src = aboutSlides[sidebarIndex].img;
            }
            
            // Update dots
            if (aboutSliderDots.length > 0) {
                aboutSliderDots.forEach(dot => dot.classList.remove('active'));
                if (aboutSliderDots[currentSlide]) {
                    aboutSliderDots[currentSlide].classList.add('active');
                }
            }
            
            // Fade in all
            aboutMainImg.style.opacity = '1';
            aboutMainTitle.style.opacity = '1';
            aboutMainDesc.style.opacity = '1';
            aboutSidebarItems.forEach(img => img.style.opacity = '1');
        }, 400); // Wait for fade out
    }, 4000); // Change every 4 seconds
}
'''

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js + '\n' + new_logic)
