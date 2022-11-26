import requests
import os
from datetime import datetime
import smtplib

MY_EMAIL = "shahar1360@gmail.com"
APP_PASSWORD = os.environ.get("PY_GMAIL_PASS")
MY_LAT = 31.046051
MY_LON = 34.851612


def is_the_satellite_near():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lon = float(data["iss_position"]["longitude"])

    if abs(abs(MY_LAT) - abs(iss_lat)) > 5 or \
       abs(abs(MY_LON) - abs(iss_lon)) > 5:
        return False

    return True


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunrise < time_now < sunset:
        return False
    return True


if is_night_time() and is_the_satellite_near():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=APP_PASSWORD)
    connection.sendmail(MY_EMAIL, MY_EMAIL, msg="Subject: Look up!\n\nThe satellite is here!")
    connection.close()
