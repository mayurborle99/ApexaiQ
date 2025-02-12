import requests
import json

url = "https://dummyjson.com/comments"  

response = requests.get(url)

if response.status_code == 200:
    
    json_data = response.json()

    
    with open('data.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    
    print("JSON data has been saved to 'data.json' file.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
