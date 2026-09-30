import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("CURRENT DATA:")
for place in data:
    print(f"{place['place']}: {len(place['packages'])} packages")
    for pkg in place['packages']:
        print(f"  - {pkg['name']}")
