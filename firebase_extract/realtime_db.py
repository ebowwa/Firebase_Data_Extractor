# scheme_edesia/database/realtime_database.py

from firebase_admin import db
import json

def parse_food_trucks(food_trucks_data):
    food_trucks_info = []
    for truck_id, details in food_trucks_data.items():
        food_truck_info = {
            'id': truck_id,
            'name': details.get('Name', 'N/A'),
            'category': details.get('Category', 'N/A'),
            'description': details.get('Description', 'N/A'),
            'email': details.get('Email', 'N/A'),
            'phone': details.get('Phone', 'N/A'),
            'image': details.get('Image', 'N/A'),
            'ownerName': details.get('OwnerName', 'N/A'),
            'likes': details.get('likes', 0),
        }
        food_trucks_info.append(food_truck_info)
    return food_trucks_info

def backup_and_parse_realtime_db():
    # Asynchronously retrieve the FoodTrucks data and parse it
    ref = db.reference('FoodTrucks')
    food_trucks_data = ref.get()
    parsed_food_trucks = parse_food_trucks(food_trucks_data)

    # Save the entire database
    root_ref = db.reference('/')
    entire_db_data = root_ref.get()

    # Convert the data to a JSON string and write to a file
    json_data = json.dumps(entire_db_data, indent=4)
    with open('entire_database_backup.json', 'w') as file:
        file.write(json_data)

    # Save the parsed food trucks data to a file
    save_parsed_food_trucks_to_file(parsed_food_trucks)

def save_parsed_food_trucks_to_file(parsed_data, filename='parsed_food_trucks.json'):
    with open(filename, 'w') as file:
        json_data = json.dumps(parsed_data, indent=4)
        file.write(json_data)
    print(f'Parsed food trucks data has been saved to {filename}.')
