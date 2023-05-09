import requests
import json

url = "https://chall6.cybernight.org/challenges-server/api/favorite-food"
headers = {"Content-Type": "application/json"}

payload = {"selectField": "pizza"}
data = json.dumps(payload)

response = requests.post(url, headers=headers, data=data)

print(response.text)

