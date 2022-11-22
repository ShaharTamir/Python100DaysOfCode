import requests
import os

MY_LAT = 31.046051
MY_LON = 34.851612

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": os.environ.get("WA_PASS")
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=weather_parameters)
response.raise_for_status()
data = response.json()

for condition in data["weather"]:
    if condition["id"] < 700:
        print("you are going to need an umbrella today.")

