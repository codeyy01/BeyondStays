import json
import codecs
import re

with codecs.open('data.js', 'r', 'utf-8') as f:
    text = f.read()

json_str = text.split('=', 1)[1].strip()
if json_str.endswith(';'):
    json_str = json_str[:-1]

data = json.loads(json_str)

# Map names to their image files
img_map = {
    "Kashmir Bachelors Package": "./assets/packagePictures/Kashmir_Bachelors_package.jpeg",
    "Kashmir Budget Package": "./assets/packagePictures/Kashmir_budget_package.jpeg",
    "Delhi to Manali Explorer": "./assets/packagePictures/Manali_package.jpeg",
    "Goa Budget Resort Stay": "./assets/packagePictures/Goa_budget_package.jpeg",
    "Goa Budget Bike Trip": "./assets/packagePictures/Goa_budget_bike_package.jpeg",
    "Kasol Backpacking Trip": "./assets/packagePictures/kasol.jpeg",
    "Sar Pass Trek": "./assets/packagePictures/Sarpass_trekking.jpeg",
    "Wayanad": "./assets/packagePictures/Wayanad.jpeg",
    "Munnar": "./assets/packagePictures/Munnar.jpeg",
    "Kodaikanal": "./assets/packagePictures/Kodaikanal.jpeg",
    "Ooty": "./assets/packagePictures/Ooty.jpeg",
    "kolukkumalai": "./assets/packagePictures/kolukkumalai_sunrise.jpeg"
}

for dest in data:
    for pkg in dest["packages"]:
        name = pkg["name"]
        if name in img_map:
            pkg["images"] = [img_map[name]]
            pkg["coverImage"] = img_map[name]
        elif name.lower() == "vagamon":
            # Just use Munnar or Ooty as a placeholder since Vagamon is missing
            pkg["images"] = ["./assets/packagePictures/Munnar.jpeg"]
            pkg["coverImage"] = "./assets/packagePictures/Munnar.jpeg"

js_content = "window.localTravelData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";"

with codecs.open("data.js", "w", "utf-8") as f:
    f.write(js_content)

# Bump cache version in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'data\.js\?v=[0-9]+', 'data.js?v=100', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
