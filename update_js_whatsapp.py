import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Change slider interval from 3000 to 6000
js = js.replace('}, 3000);', '}, 6000);')

# 2. Add the bookPackageWa function
new_func = '''
function bookPackageWa(placeName, packageName) {
    const msg = `Hello Beyondstays, I would like to book a trip!

👤 Name: 
📍 Destination: ${placeName} (${packageName})
📅 Check-in Date: 
📅 Check-out Date: 
👥 Adults: 
🧒 Kids: 
🏕️ Group Type: 
🏨 No. of Rooms: 

Please share available packages and pricing.`;
    openWaPage(msg);
}
'''
if 'function bookPackageWa' not in js:
    js = js.replace('function openWaPage', new_func + '\nfunction openWaPage')

# 3. Update the HTML generated in renderModernPackages
# Add onclick to the image wrap and arrow button
old_img_html = r'<div class="pkg-img-wrap">'
new_img_html = r'<div class="pkg-img-wrap" style="cursor:pointer;" onclick="bookPackageWa(\'${pkg.placeName}\', \'${pkg.name}\')">'
js = js.replace(old_img_html, new_img_html)

old_arrow_btn = r'<div class="pkg-arrow-btn" onclick="openModal(\'${pkg.id}\', \'${pkg.placeName}\')">&#8599;</div>'
new_arrow_btn = r'<div class="pkg-arrow-btn" onclick="bookPackageWa(\'${pkg.placeName}\', \'${pkg.name}\', event)">&#8599;</div>'
js = js.replace(old_arrow_btn, new_arrow_btn)

# Wait, if they click the arrow, it's inside the pkg-img-wrap which also has onclick. 
# We should stop propagation or just rely on bubbling doing the same thing.
# To prevent double triggering, we can add event.stopPropagation():
new_arrow_btn2 = r'<div class="pkg-arrow-btn" onclick="event.stopPropagation(); bookPackageWa(\'${pkg.placeName}\', \'${pkg.name}\')">&#8599;</div>'
js = js.replace(new_arrow_btn, new_arrow_btn2)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
