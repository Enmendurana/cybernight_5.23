import requests
import json

url = "https://chall6.cybernight.org/challenges-server/api/login"

headers = {
    "Content-Type": "application/json"
}

data = {
    "username": "ime_uporabnika",
    "password": "FirstChallengeSuccessfullyCompleted"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.content)
