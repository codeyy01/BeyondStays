import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_slides = '''                <div class="hero-slides" id="heroSlides">
                    <div class="hero-slide active" style="background-image:url('./assets/hero1.jpg');"></div>
                    <div class="hero-slide" style="background-image:url('./assets/hero2.jpg');"></div>
                    <div class="hero-slide" style="background-image:url('./assets/hero3.jpg');"></div>
                    <div class="hero-slide" style="background-image:url('./assets/hero4.jpg');"></div>
                    <div class="hero-slide" style="background-image:url('./assets/hero5.jpg');"></div>
                </div>'''

new_slides = '''                <div class="hero-slides" id="heroSlides">
                    <div class="hero-slide active" style="background-image:url('./assets/hero1-desk.jpg');" data-desktop="./assets/hero1-desk.jpg" data-mobile="./assets/hero1-desk.jpg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/hero2-desk.jpg');" data-desktop="./assets/hero2-desk.jpg" data-mobile="./assets/hero2-desk.jpg"></div>
                    <div class="hero-slide" style="background-image:url('./assets/hero3-desk.jpg');" data-desktop="./assets/hero3-desk.jpg" data-mobile="./assets/hero3-desk.jpg"></div>
                </div>'''

html = html.replace(old_slides, new_slides)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
