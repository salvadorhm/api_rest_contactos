import requests

URI = "http://localhost:8000/v1/contactos"

response = requests.get(URI)

print(f"GET: {response.text}")
print(f"GET: {response.status_code}")

data = {"nombre": "Demo", "email": "demo@email"}
response = requests.post(URI, json=data)

print(f"POST: {response.text}")
print(f"POST: {response.status_code}")
