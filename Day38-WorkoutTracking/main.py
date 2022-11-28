import requests
from datetime import datetime
from os import environ

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_header = {
    "x-app-id": environ.get("NUTRIX_ID"),
    "x-app-key": environ.get("NUTRIX_KEY")
}

nutri_params = {
    "query": input("Please enter your exercise: "),
    "gender": "male",
    "weight_kg": 86.5,
    "height_cm": 176,
    "age": 26
}

response = requests.post(url=NUTRI_ENDPOINT, headers=nutri_header, json=nutri_params)
response.raise_for_status()
nutri_response = response.json()["exercises"][0]

for exercise in nutri_response:
    sheet_params = {
        "sheet1":  {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M"),
            "exercise": nutri_response["user_input"].title(),
            "duration (min)": nutri_response["duration_min"],
            "calories": nutri_response["nf_calories"],
            "id": -1
        }
    }

    GOOGLE_ENDPOINT = environ.get("WORKOUT_SHEET_ENDPOINT")
    response = requests.post(url=GOOGLE_ENDPOINT, json=sheet_params)
    response.raise_for_status()
print("workout logged!")
