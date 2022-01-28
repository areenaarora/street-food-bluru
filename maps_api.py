import requests

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

payload={
    "location": "12.9716° N, 77.5946° E",
    "radius": "10000",
    "type": "restaurant",
    "key": "AIzaSyAKXkkNUgzYoZlqHtehC-Brkor_VNPpCWY"
}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)