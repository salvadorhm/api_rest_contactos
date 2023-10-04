import requests
import json

URI = "https://www.dnd5eapi.co/api/classes/"

response = requests.get(URI)

print(f"GET: {response.text}")

data = json.loads(response.text)

for i in range(0,data['count']):
    print(f"Name: {data['results'][i]['name']} - URL: {data['results'][i]['url']}")

