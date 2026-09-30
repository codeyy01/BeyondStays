import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define basic packages for 8-13
p8 = {
    "id": "wayanad-resorts",
    "name": "Wayanad Resorts",
    "price": "Enquire Now",
    "duration": "Custom",
    "description": "Experience the lush green landscapes, waterfalls, and wildlife of Wayanad from our premium and budget resort options.",
    "highlights": ["Nature Walks", "Resort Stay", "Sightseeing"],
    "inclusions": ["Stay", "Breakfast"],
    "exclusions": ["Travel", "Personal Expenses"],
    "images": ["https://images.pexels.com/photos/10106822/pexels-photo-10106822.jpeg"]
}

p9 = {
    "id": "munnar-resorts",
    "name": "Munnar Resorts",
    "price": "Enquire Now",
    "duration": "Custom",
    "description": "Stay amidst the sprawling tea gardens of Munnar with breathtaking valley views and cool mountain breeze.",
    "highlights": ["Tea Gardens", "Resort Stay", "Viewpoints"],
    "inclusions": ["Stay", "Breakfast"],
    "exclusions": ["Travel", "Personal Expenses"],
    "images": ["https://images.pexels.com/photos/13691355/pexels-photo-13691355.jpeg"]
}

p10 = {
    "id": "kodaikanal-resorts",
    "name": "Kodaikanal Resorts",
    "price": "Enquire Now",
    "duration": "Custom",
    "description": "Relax in the Princess of Hill Stations. Enjoy the lakes, pine forests, and misty weather from our cozy resorts.",
    "highlights": ["Lake Visit", "Resort Stay", "Pine Forests"],
    "inclusions": ["Stay", "Breakfast"],
    "exclusions": ["Travel", "Personal Expenses"],
    "images": ["https://images.pexels.com/photos/17638363/pexels-photo-17638363.jpeg"]
}

p11 = {
    "id": "ooty-resorts",
    "name": "Ooty Resorts",
    "price": "Enquire Now",
    "duration": "Custom",
    "description": "Discover the charm of Ooty. Vintage toy trains, botanical gardens, and heritage stays await you.",
    "highlights": ["Heritage Stay", "Sightseeing", "Cool Climate"],
    "inclusions": ["Stay", "Breakfast"],
    "exclusions": ["Travel", "Personal Expenses"],
    "images": ["https://images.pexels.com/photos/11140989/pexels-photo-11140989.jpeg"]
}

p12 = {
    "id": "vagamon-resorts",
    "name": "Vagamon Resorts",
    "price": "Enquire Now",
    "duration": "Custom",
    "description": "Get away from the crowds and unwind in the rolling meadows and pine forests of Vagamon.",
    "highlights": ["Pine Forests", "Meadows", "Resort Stay"],
    "inclusions": ["Stay", "Breakfast"],
    "exclusions": ["Travel", "Personal Expenses"],
    "images": ["https://images.pexels.com/photos/7533345/pexels-photo-7533345.jpeg"]
}

p13 = {
    "id": "kolikkimalai-pack",
    "name": "Kolikkimalai Package",
    "price": "Enquire Now",
    "duration": "Custom",
    "description": "Experience the world's highest tea estate. Off-road jeep safari, breathtaking sunrise views, and camping options.",
    "highlights": ["Jeep Safari", "Sunrise View", "Highest Tea Estate"],
    "inclusions": ["Jeep Safari", "Stay", "Breakfast"],
    "exclusions": ["Travel to Base", "Personal Expenses"],
    "images": ["https://images.pexels.com/photos/16380678/pexels-photo-16380678.jpeg"]
}

# Add them to data
for place in data:
    if place['place'] == 'Wayanad':
        place['packages'] = [p8]
    elif place['place'] == 'Munnar':
        place['packages'] = [p9]
    elif place['place'] == 'Kodaikanal':
        place['packages'] = [p10]
    elif place['place'] == 'Ooty':
        place['packages'] = [p11]
    elif place['place'] == 'Vagamon':
        place['packages'] = [p12]
    elif place['place'] == 'Kolukkumalai':
        place['packages'] = [p13]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
