import json
import codecs

data = [
  {
    "place": "Kashmir",
    "region": "Domestic",
    "tagline": "Snow Peaks, Valleys & Scenic Serenity",
    "coverImage": "https://images.pexels.com/photos/5409673/pexels-photo-5409673.jpeg",
    "packages": [
      {
        "id": "kashmir-bachelors",
        "name": "Kashmir Bachelors Package",
        "price": "₹3,700",
        "duration": "6 Days / 5 Nights",
        "description": "Complete Kashmir experience covering Srinagar, Gulmarg, Pahalgam, and Sonamarg with sightseeing, transport, and stay.",
        "highlights": ["5 Nights Stay", "4 Days Transportation", "Srinagar Sightseeing", "Gulmarg Visit", "Pahalgam Visit", "Sonamarg Visit", "Parking & Toll Included"],
        "inclusions": ["Stay", "Transportation", "All taxes & parking"],
        "exclusions": ["Food", "Adventure activities", "Travel tickets", "Personal expenses", "Pickup & Drop", "Flight/Train Charges", "Any Extra Cabs", "Any cost arising due to natural calamities, weather problems, road blockage, political strikes etc."]
      },
      {
        "id": "kashmir-budget",
        "name": "Kashmir Budget Package",
        "price": "₹2,900",
        "duration": "5 Days / 4 Nights",
        "description": "Short and budget-friendly Kashmir trip covering major highlights with essential sightseeing and stay.",
        "highlights": ["4 Nights Stay", "3 Days Transportation", "Srinagar Sightseeing", "Gulmarg Visit", "Pahalgam Visit", "Parking & Toll Included", "Adventure Activities"],
        "inclusions": ["Stay", "Transportation", "All taxes & parking"],
        "exclusions": ["Food", "Adventure activities", "Travel tickets", "Personal expenses", "Pickup & Drop", "Flight/Train Charges", "Any Extra Cabs", "Any cost arising due to natural calamities, weather problems, road blockage, political strikes etc."]
      }
    ]
  },
  {
    "place": "Manali",
    "region": "Domestic",
    "tagline": "Mountains, Rivers & Adventure",
    "coverImage": "https://images.pexels.com/photos/1032650/pexels-photo-1032650.jpeg",
    "packages": [
      {
        "id": "manali-explorer",
        "name": "Delhi to Manali Explorer",
        "price": "₹4,299",
        "duration": "5 Days / 4 Nights",
        "description": "Travel from Delhi to Manali in a comfortable Volvo bus and explore the best of Manali including temples, valleys, and Kullu sightseeing. Perfect mix of adventure and relaxation. Heavy Snowfall Condition:-During heavy snowfall, sightseeing may be suspended. If you still wish to go sightseeing, you will need to hire an additional 4x4 vehicle at your own cost, as it is not included in the package, and explore independently. Alternatively, you may choose to stay at the hotel. In this case, the hotel balance amount must be paid, the taxi sightseeing charges will be reduced, and the final revised amount will be informed to you. Checkout Time: Guests are required to arrange a 4x4 vehicle on their own for checkout.",
        "highlights": ["Delhi-Manali Volvo (AC)", "2 Breakfast + 2 Dinner", "Hotel Stay (2N)", "Local Sightseeing", "Solang Valley Trip", "Kullu Visit", "Private Taxi"],
        "inclusions": ["Delhi ➝ Manali ➝ Delhi Volvo AC Semi Sleeper", "2 Breakfast + 2 Dinner", "3 Days / 2 Nights Manali Hotel Stay", "1 Day Local Sightseeing", "1 Day Solang Valley", "1 Day Kullu"],
        "exclusions": ["Atal Tunnel & Sissu (Extra Charge)", "Alto – ₹2000", "Tavera – ₹3000", "Tempo Traveller – ₹4500", "Lunch", "Local vehicle (4×4 for snow time)", "Adventure activities", "No activities included in the package", "Heat Pillar - Room Heater - Extra Charge ₹500", "Any cost arising due to natural calamities, weather problems, road blockage, political strikes etc."]
      }
    ]
  },
  {
    "place": "Goa",
    "region": "Domestic",
    "tagline": "Beaches, Parties & Sunsets",
    "coverImage": "https://images.pexels.com/photos/1032650/pexels-photo-1032650.jpeg",
    "packages": [
      {
        "id": "goa-budget-resort",
        "name": "Goa Budget Resort Stay",
        "price": "₹4,500",
        "duration": "3 Days / 2 Nights",
        "description": "Stay in a comfortable resort near Calangute with bike rentals, sightseeing tours, and easy access to Goa’s top beaches. Perfect for friends and budget travelers.",
        "highlights": ["A/C Rooms", "Swimming Pool", "Pickup & Drop (Thivim)", "2 Days Bike Rental", "North Goa Tour", "South Goa Tour", "3 Breakfast + 2 Dinner", "Online Tour Coordinator"],
        "inclusions": [],
        "exclusions": []
      },
      {
        "id": "goa-budget-bike",
        "name": "Goa Budget Bike Trip",
        "price": "₹3,499",
        "duration": "2 Days / 1 Nights",
        "description": "Enjoy Goa on a budget with bike rentals, comfortable A/C stays, and guided support. Perfect for exploring beaches, nightlife, and local culture at your own pace.",
        "highlights": ["A/C Rooms", "2 Days Bike Rental", "Pickup & Drop (Thivim railway station)", "Breakfast & Dinner", "Online Tour Coordinator", "Local Exploration"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  },
  {
    "place": "Kasol",
    "region": "Domestic",
    "tagline": "Rivers, Treks & Hippie Vibes",
    "coverImage": "https://images.pexels.com/photos/258421/pexels-photo-258421.jpeg",
    "packages": [
      {
        "id": "kasol-backpacking",
        "name": "Kasol Backpacking Trip",
        "price": "₹5,500",
        "duration": "5 Days / 4 Nights",
        "description": "Explore the serene Parvati Valley with village treks, waterfalls, and scenic mountain landscapes. A perfect getaway for backpackers and nature lovers.",
        "highlights": ["Delhi to Delhi Volvo", "Breakfast Included", "Stay Included", "Grahan Village Trek", "Tosh Village Visit", "Manikaran Visit", "Local Transport"],
        "inclusions": [],
        "exclusions": []
      },
      {
        "id": "sar-pass",
        "name": "Sar Pass Trek",
        "price": "₹4,999",
        "duration": "5 Days / 4 Nights",
        "description": "Experience pure Himalayan thrill From dense pine forests to snow-covered slopes and an unforgettable summit at 13,800 ft.",
        "highlights": ["Stay (Tents / Guesthouse)", "Meals", "Certified Trek Leader", "Basic Camping Equipment", "Local Transfers"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  },
  {
    "place": "Wayanad",
    "region": "Domestic",
    "tagline": "Nature & Wildlife",
    "coverImage": "https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg",
    "packages": [
      {
        "id": "wayanad-resorts",
        "name": "Wayanad",
        "price": "Enquire Now",
        "duration": "Custom",
        "description": "Discover the wild beauty of Wayanad with lush forests, waterfalls, and spice plantations.",
        "highlights": ["Forest Stay", "Wildlife Safari", "Waterfalls"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  },
  {
    "place": "Munnar",
    "region": "Domestic",
    "tagline": "Tea Gardens & Mist",
    "coverImage": "https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg",
    "packages": [
      {
        "id": "munnar-resorts",
        "name": "Munnar",
        "price": "Enquire Now",
        "duration": "Custom",
        "description": "Experience the majestic tea estates and misty mountains of Munnar.",
        "highlights": ["Tea Estate Visit", "Mist Valley View", "Comfortable Stay"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  },
  {
    "place": "Kodaikanal",
    "region": "Domestic",
    "tagline": "The Princess of Hill Stations",
    "coverImage": "https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg",
    "packages": [
      {
        "id": "kodai-resorts",
        "name": "Kodaikanal",
        "price": "Enquire Now",
        "duration": "Custom",
        "description": "Row through the pristine lakes and walk along the pine forests of Kodaikanal.",
        "highlights": ["Lake Boating", "Pine Forest", "Scenic Views"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  },
  {
    "place": "Ooty",
    "region": "Domestic",
    "tagline": "Queen of Hill Stations",
    "coverImage": "https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg",
    "packages": [
      {
        "id": "ooty-resorts",
        "name": "Ooty",
        "price": "Enquire Now",
        "duration": "Custom",
        "description": "Discover the charm of Ooty. Vintage toy trains, botanical gardens, and heritage.",
        "highlights": ["Toy Train", "Botanical Garden", "Heritage Stay"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  },
  {
    "place": "Vagamon",
    "region": "Domestic",
    "tagline": "Pine Forests & Meadows",
    "coverImage": "https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg",
    "packages": [
      {
        "id": "vagamon-resorts",
        "name": "vagamon",
        "price": "Enquire Now",
        "duration": "Custom",
        "description": "Get away from the crowds and unwind in the rolling meadows and pine forests of Vagamon.",
        "highlights": ["Meadows", "Pine Forest", "Offbeat Stay"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  },
  {
    "place": "Kolukkumalai",
    "region": "Domestic",
    "tagline": "World's Highest Tea Estate",
    "coverImage": "https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg",
    "packages": [
      {
        "id": "kolukkumalai-resorts",
        "name": "kolukkumalai",
        "price": "Enquire Now",
        "duration": "Custom",
        "description": "Experience the world's highest tea estate. Off-road jeep safari, breathtaking sunrise views.",
        "highlights": ["Jeep Safari", "Sunrise View", "Tea Estate"],
        "inclusions": [],
        "exclusions": []
      }
    ]
  }
]

js_content = "window.localTravelData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";"

with codecs.open("data.js", "w", "utf-8") as f:
    f.write(js_content)

import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'data\.js\?v=[0-9]+', 'data.js?v=99', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
