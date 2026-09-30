import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_logic = '''
/* -----------------------------------------------------------
   ABOUT DESKTOP HOVER INTERACTION
----------------------------------------------------------- */
const aboutSidebarItems = document.querySelectorAll('.about-sidebar-item');
const aboutMainImg = document.getElementById('aboutMainImg');
const aboutMainTitle = document.getElementById('aboutMainTitle');
const aboutMainDesc = document.getElementById('aboutMainDesc');

if (aboutSidebarItems.length > 0 && aboutMainImg && aboutMainTitle && aboutMainDesc) {
    let hoverTimeout;
    const defaultImg = aboutMainImg.src;
    const defaultTitle = aboutMainTitle.innerText;
    const defaultDesc = aboutMainDesc.innerText;

    aboutSidebarItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            clearTimeout(hoverTimeout);
            aboutMainImg.style.opacity = '0.3';
            aboutMainTitle.style.opacity = '0';
            aboutMainDesc.style.opacity = '0';
            setTimeout(() => {
                aboutMainImg.src = item.getAttribute('data-img');
                aboutMainTitle.innerText = item.getAttribute('data-title');
                aboutMainDesc.innerText = item.getAttribute('data-desc');
                aboutMainImg.style.opacity = '1';
                aboutMainTitle.style.opacity = '1';
                aboutMainDesc.style.opacity = '1';
            }, 200);
        });
        
        item.addEventListener('mouseleave', () => {
            hoverTimeout = setTimeout(() => {
                aboutMainImg.style.opacity = '0.3';
                aboutMainTitle.style.opacity = '0';
                aboutMainDesc.style.opacity = '0';
                setTimeout(() => {
                    aboutMainImg.src = defaultImg;
                    aboutMainTitle.innerText = defaultTitle;
                    aboutMainDesc.innerText = defaultDesc;
                    aboutMainImg.style.opacity = '1';
                    aboutMainTitle.style.opacity = '1';
                    aboutMainDesc.style.opacity = '1';
                }, 200);
            }, 400);
        });
    });
}
'''

if "ABOUT DESKTOP HOVER INTERACTION" not in js:
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js + '\n' + new_logic)
