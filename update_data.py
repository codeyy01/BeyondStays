import json

# We will load the old data.json, replace packages for Kashmir, Manali, Goa, Kasol, and write it back.
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Package 1: Kashmir Bachelors
kashmir_bachelors = {
    "id": "kashmir-bachelors",
    "name": "Kashmir Bachelors Package",
    "price": "₹3,700",
    "duration": "6 Days / 5 Nights",
    "description": "Complete Kashmir experience covering Srinagar, Gulmarg, Pahalgam, and Sonamarg with sightseeing, transport, and stay.",
    "highlights": ["5 Nights Stay", "4 Days Transportation", "Srinagar Sightseeing", "Gulmarg Visit", "Pahalgam Visit", "Sonamarg Visit", "Parking & Toll Included"],
    "inclusions": ["Stay", "Transportation", "All taxes & parking"],
    "exclusions": ["Food", "Adventure activities", "Travel tickets", "Personal expenses", "Pickup & Drop", "Flight/Train Charges", "Any Extra Cabs", "Any cost arising due to natural calamities, weather problems, road blockage, political strikes etc."],
    "images": ["https://images.pexels.com/photos/540518/pexels-photo-540518.jpeg"]
}

# Package 2: Kashmir Budget
kashmir_budget = {
    "id": "kashmir-budget",
    "name": "Kashmir Budget Package",
    "price": "₹2,900",
    "duration": "5 Days / 4 Nights",
    "description": "Short and budget-friendly Kashmir trip covering major highlights with essential sightseeing and stay.",
    "highlights": ["4 Nights Stay", "3 Days Transportation", "Srinagar Sightseeing", "Gulmarg Visit", "Pahalgam Visit", "Parking & Toll Included", "Adventure Activities"],
    "inclusions": ["Stay", "Transportation", "All taxes & parking"],
    "exclusions": ["Food", "Adventure activities", "Travel tickets", "Personal expenses", "Pickup & Drop", "Flight/Train Charges", "Any Extra Cabs", "Any cost arising due to natural calamities, weather problems, road blockage, political strikes etc."],
    "images": ["https://images.pexels.com/photos/540518/pexels-photo-540518.jpeg"]
}

# Package 3: Manali Explorer
manali_explorer = {
    "id": "manali-explorer",
    "name": "Delhi to Manali Explorer",
    "price": "₹4,299",
    "duration": "5 Days / 4 Nights",
    "description": "Travel from Delhi to Manali in a comfortable Volvo bus and explore the best of Manali including temples, valleys, and Kullu sightseeing. Perfect mix of adventure and relaxation.\\n\\n**Heavy Snowfall Condition:** During heavy snowfall, sightseeing may be suspended. If you still wish to go sightseeing, you will need to hire an additional 4×4 vehicle at your own cost, as it is not included in the package, and explore independently. Alternatively, you may choose to stay at the hotel. In this case, the hotel balance amount must be paid, the taxi sightseeing charges will be reduced, and the final revised amount will be informed to you. Checkout Time: Guests are required to arrange a 4×4 vehicle on their own for checkout.",
    "highlights": ["Delhi-Manali Volvo (AC)", "2 Breakfast + 2 Dinner", "Hotel Stay (2N)", "Local Sightseeing", "Solang Valley Trip", "Kullu Visit", "Private Taxi"],
    "inclusions": ["Delhi ➝ Manali ➝ Delhi Volvo AC Semi Sleeper", "2 Breakfast + 2 Dinner", "3 Days / 2 Nights Manali Hotel Stay", "1 Day Local Sightseeing", "1 Day Solang Valley", "1 Day Kullu"],
    "exclusions": ["Atal Tunnel & Sissu (Extra Charge)", "Alto – ₹2000", "Tavera – ₹3000", "Tempo Traveller – ₹4500", "Lunch", "Local vehicle (4×4 for snow time)", "Adventure activities", "No activities included in the package", "Heat Pillar - Room Heater - Extra Charge ₹500", "Any cost arising due to natural calamities, weather problems, road blockage, political strikes etc."],
    "images": ["https://images.pexels.com/photos/1683492/pexels-photo-1683492.jpeg"]
}

# Package 4 & 5: Goa
goa_resort = {
    "id": "goa-resort",
    "name": "Goa Budget Resort Stay",
    "price": "₹4,500",
    "duration": "3 Days / 2 Nights",
    "description": "Stay in a comfortable resort near Calangute with bike rentals, sightseeing tours, and easy access to Goa’s top beaches. Perfect for friends and budget travelers.",
    "highlights": ["A/C Rooms", "Swimming Pool", "Pickup & Drop (Thivim)", "2 Days Bike Rental", "North Goa Tour", "South Goa Tour", "3 Breakfast + 2 Dinner", "Online Tour Coordinator"],
    "inclusions": ["Stay in A/C Room", "Bike Rental", "Meals as per plan"],
    "exclusions": ["Travel to Goa", "Personal expenses", "Entry fees"],
    "images": ["https://images.pexels.com/photos/1036856/pexels-photo-1036856.jpeg"]
}

goa_bike = {
    "id": "goa-bike",
    "name": "Goa Budget Bike Package",
    "price": "₹3,499",
    "duration": "2 Days / 1 Nights",
    "description": "Enjoy Goa on a budget with bike rentals, comfortable A/C stays, and guided support. Perfect for exploring beaches, nightlife, and local culture at your own pace.",
    "highlights": ["A/C Rooms", "2 Days Bike Rental", "Pickup & Drop (Thivim railway station)", "Breakfast & Dinner", "Online Tour Coordinator", "Local Exploration"],
    "inclusions": ["Stay in A/C Room", "Bike Rental", "Breakfast & Dinner"],
    "exclusions": ["Travel to Goa", "Personal expenses", "Fuel for bike"],
    "images": ["https://images.pexels.com/photos/1036856/pexels-photo-1036856.jpeg"]
}

# Package 6: Kasol
kasol_pack = {
    "id": "kasol-pack",
    "name": "Kasol Backpacking Package",
    "price": "₹5,500",
    "duration": "5 Days / 4 Nights",
    "description": "Explore the serene Parvati Valley with village treks, waterfalls, and scenic mountain landscapes. A perfect getaway for backpackers and nature lovers.",
    "highlights": ["Delhi to Delhi Volvo", "Breakfast Included", "Stay Included", "Grahan Village Trek", "Tosh Village Visit", "Manikaran Visit", "Local Transport"],
    "inclusions": ["Volvo Tickets", "Stay", "Breakfast"],
    "exclusions": ["Lunch & Dinner", "Personal expenses", "Trek guide if not specified"],
    "images": ["https://images.pexels.com/photos/2812061/pexels-photo-2812061.jpeg"]
}

# Package 7: Sar Pass
kasol_sar = {
    "id": "kasol-sar",
    "name": "Sar Pass Trek",
    "price": "₹4,999",
    "duration": "5 Days / 4 Nights",
    "description": "Experience pure Himalayan thrill From dense pine forests to snow-covered slopes and an unforgettable summit at 13,800 ft.",
    "highlights": ["Stay (Tents / Guesthouse)", "Meals", "Certified Trek Leader", "Basic Camping Equipment", "Local Transfers"],
    "inclusions": ["Tents/Guesthouse", "Meals on trek", "Trek Leader", "Camping Equipments"],
    "exclusions": ["Travel to base camp", "Backpack offloading", "Personal gear"],
    "images": ["https://images.pexels.com/photos/2812061/pexels-photo-2812061.jpeg"]
}

# Update the data list
for p in data:
    if p['place'] == 'Kashmir':
        p['packages'] = [kashmir_bachelors, kashmir_budget]
    elif p['place'] == 'Manali':
        p['packages'] = [manali_explorer]
    elif p['place'] == 'Goa':
        p['packages'] = [goa_resort, goa_bike]
    elif p['place'] == 'Kasol':
        p['packages'] = [kasol_pack, kasol_sar]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
