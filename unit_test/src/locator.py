import geocoder

# Get the current location
location = geocoder.ip('me')

# Print the latitude and longitude
print(f"Latitude: {location.latlng[0]}, Longitude: {location.latlng[1]}")