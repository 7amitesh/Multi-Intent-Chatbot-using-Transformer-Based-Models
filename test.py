import requests

url = "http://127.0.0.1:5000/predict"
payload = {"text": "book me a flight to Delhi"}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
