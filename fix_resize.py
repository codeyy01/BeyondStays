import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_resize = '''      function updateHeroImages() {
          const isMobile = window.innerWidth <= 768;
          slides.forEach(slide => {
              const url = isMobile ? slide.dataset.mobile : slide.dataset.desktop;
              if (url) {
                  const bgStr = "url(\\"" + url + "\\")";
                  // Only update if it actually changed to prevent paint thrashing
                  if (slide.style.backgroundImage !== bgStr) {
                      slide.style.backgroundImage = bgStr;
                  }
              }
          });
      }
      updateHeroImages();
      window.addEventListener('resize', updateHeroImages);'''

new_resize = '''      let lastIsMobile = null;
      function updateHeroImages() {
          const isMobile = window.innerWidth <= 768;
          if (lastIsMobile === isMobile) return; // Prevent updating on mobile scroll resizing
          lastIsMobile = isMobile;
          
          slides.forEach(slide => {
              const url = isMobile ? slide.dataset.mobile : slide.dataset.desktop;
              if (url) {
                  slide.style.backgroundImage = "url('" + url + "')";
              }
          });
      }
      updateHeroImages();
      window.addEventListener('resize', updateHeroImages);'''

js = js.replace(old_resize, new_resize)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
