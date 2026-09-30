import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Using regex to replace the entire <div class="hero-slides" id="heroSlides"> ... </div> block
old_slides_pattern = r'<div class="hero-slides" id="heroSlides">.*?</div>'

new_slides = '''<div class="hero-slides" id="heroSlides">
                    <div class="hero-slide active" style="background-image:url('./assets/beyondPictures/wide1.jpeg');" data-desktop="./assets/beyondPictures/wide1.jpeg" data-mobile="./assets/beyondPictures/verti1.jpeg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/beyondPictures/wide2.jpg');" data-desktop="./assets/beyondPictures/wide2.jpg" data-mobile="./assets/beyondPictures/verti2.jpeg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/beyondPictures/wide3.webp');" data-desktop="./assets/beyondPictures/wide3.webp" data-mobile="./assets/beyondPictures/verti3.jpeg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/beyondPictures/wide4.jpg');" data-desktop="./assets/beyondPictures/wide4.jpg" data-mobile="./assets/beyondPictures/verti4.avif"></div>
                </div>'''

html = re.sub(old_slides_pattern, new_slides, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
