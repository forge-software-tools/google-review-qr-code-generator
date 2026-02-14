import requests
import qrcode
import os

# CONFIG
API_KEY = "YOUR_GOOGLE_PLACES_API_KEY" # Replace this or use env var

def find_place_id(query):
    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress"
    }
    data = {"textQuery": query}
    
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 200:
        results = resp.json().get('places', [])
        if results:
            return results[0]
    return None

def generate_qr(place_id):
    link = f"https://search.google.com/local/writereview?placeid={place_id}"
    print(f"Generated Link: {link}")
    
    img = qrcode.make(link)
    img.save("google-review-qr.png")
    print("Saved to google-review-qr.png")

if __name__ == "__main__":
    if API_KEY == "YOUR_GOOGLE_PLACES_API_KEY":
        API_KEY = input("Enter your Google Maps API Key: ")
        
    query = input("Enter Business Name (e.g. Joe's Pizza NYC): ")
    place = find_place_id(query)
    
    if place:
        print(f"Found: {place['displayName']['text']} ({place['formattedAddress']})")
        generate_qr(place['id'])
    else:
        print("Business not found.")
