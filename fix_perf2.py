import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_title = '''.hero-giant-title {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-family: 'Anton', 'Oswald', 'Fraunces', sans-serif;
    font-size: clamp(6rem, 15vw, 15rem);
    font-weight: 900;
    color: rgba(255, 255, 255, 0.95);
    line-height: 0.9;
    letter-spacing: -0.02em;
    z-index: 2;
    pointer-events: none;
    text-transform: uppercase;
}'''

new_title = '''.hero-giant-title {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-family: 'Anton', 'Oswald', 'Fraunces', sans-serif;
    font-size: clamp(6rem, 15vw, 15rem);
    font-weight: 900;
    color: rgba(255, 255, 255, 0.95);
    line-height: 0.9;
    letter-spacing: -0.02em;
    z-index: 2;
    pointer-events: none;
    text-transform: uppercase;
    transform: translateZ(0);
    will-change: transform;
}'''
css = css.replace(old_title, new_title)

# add hardware acceleration to the ui layer to isolate blur rendering
old_ui = '''.hero-ui-layer {
    position: absolute;
    bottom: 60px;
    left: 60px;
    right: 60px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    z-index: 3;
}'''
new_ui = '''.hero-ui-layer {
    position: absolute;
    bottom: 60px;
    left: 60px;
    right: 60px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    z-index: 3;
    transform: translateZ(0);
    will-change: transform;
}'''
css = css.replace(old_ui, new_ui)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
