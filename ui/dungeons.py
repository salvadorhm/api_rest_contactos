import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"
response = requests.get(URI)
response = json.loads(response.text)
while True:
    for i in range(response['count']):
        print(f"{i+1}.- {response['results'][i]['name']}")

    character = int(input("Choose one character: "))
    print(f"{response['results'][character-1]['url']}")

    NEW_URI = f"https://www.dnd5eapi.co{response['results'][character-1]['url']}"
    print(NEW_URI)
    character_response = requests.get(NEW_URI)
    #print(f"{character_response.text}")
    character_response = json.loads(character_response.text)
    for i in range(len(character_response['proficiencies'])):
        print(f"{character_response['proficiencies']['name']}")
