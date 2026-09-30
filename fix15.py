with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# First, remove the new slides and the leftover old slides manually to be safe
# Find <section id="hero" class="hero">
start_idx = text.find('<section id="hero" class="hero">')
end_idx = text.find('<div class="hero-giant-title">')

if start_idx != -1 and end_idx != -1:
    new_slides = '''<section id="hero" class="hero">
                <div class="hero-slides" id="heroSlides">
                    <div class="hero-slide active" style="background-image:url('./assets/beyondPictures/wide1.jpeg');" data-desktop="./assets/beyondPictures/wide1.jpeg" data-mobile="./assets/beyondPictures/verti1.jpeg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/beyondPictures/wide2.jpg');" data-desktop="./assets/beyondPictures/wide2.jpg" data-mobile="./assets/beyondPictures/verti2.jpeg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/beyondPictures/wide3.webp');" data-desktop="./assets/beyondPictures/wide3.webp" data-mobile="./assets/beyondPictures/verti3.jpeg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/beyondPictures/wide4.jpg');" data-desktop="./assets/beyondPictures/wide4.jpg" data-mobile="./assets/beyondPictures/verti4.avif"></div>
                </div>

                '''
    text = text[:start_idx] + new_slides + text[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
