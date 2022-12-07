import requests
from flight_data import sort_key_function
from os import environ
from user_data import UserData

SHEETY_API_KEY = environ.get("FLIGHT_SHEETY_API_KEY")
SHEETY_ENDPOINT = environ.get("FLIGHT_SHEET_ENDPOINT")
PRICES_SHEET = "prices"
USERS_SHEET = "users"


class DataManager:

    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.header = {"Authorization": SHEETY_API_KEY}
        self.prices = None
        self.users = []
        self.curr_flights = []

    def get_price_sheet_data(self):
        response = requests.get(url=self.endpoint + PRICES_SHEET, headers=self.header)
        response.raise_for_status()
        self.prices = response.json()[PRICES_SHEET]

    def update_price_sheet_data(self):
        for data in self.prices:
            sheet_data = {
                "price": data
            }
            row_url = self.endpoint + f"{PRICES_SHEET}/{data['id']}"
            response = requests.put(url=row_url, headers=self.header, json=sheet_data)
            response.raise_for_status()

    def get_top_cheapest(self):
        self.curr_flights.sort(key=sort_key_function)
        if len(self.curr_flights) > 3:
            return self.curr_flights[:3]
        return self.curr_flights

    def get_subscribers(self):
        response = requests.get(url=self.endpoint + USERS_SHEET, headers=self.header)
        response.raise_for_status()
        raw_users = response.json()[USERS_SHEET]
        for user in raw_users:
            self.users.append(UserData(user["firstName"], user["lastName"], user["email"]))

    def add_subscriber(self, new_user: UserData):
        emails = [user["email"] for user in self.users]
        if new_user.email in emails:
            return False

        sheet_data = {
            "user": {
                "firstName": new_user.name,
                "lastName": new_user.last_name,
                "email": new_user.email,
                "id": -1
            }
        }

        response = requests.post(url=self.endpoint + USERS_SHEET, headers=self.header, json=sheet_data)
        response.raise_for_status()
        return True
