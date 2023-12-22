import json

import requests

# Get user input for the city
city = input("Enter the city for ranking (e.g., Los Angeles): ").lower().replace(" ", "-")

url_api = f'https://api.midway.tomtom.com/ranking/liveHourly/USA_{city}'

try:
    usa_req = requests.get(url_api)
    usa_req.raise_for_status()
    usa_json = usa_req.json()
    print(usa_json)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")



