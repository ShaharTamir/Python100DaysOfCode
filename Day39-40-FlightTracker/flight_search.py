import requests
from datetime import datetime, timedelta
from flight_data import FlightData


TIME_FORMAT = "%d/%m/%Y"


class FlightSearch:

    def __init__(self, api_key):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.header = {
            "apikey": api_key
        }

    def get_destination_code(self, city_name):
        destination_query_params = {
            "term": city_name,
            "location_types": "city",
        }
        url = self.endpoint + "/locations/query"

        response = requests.get(url=url, headers=self.header, params=destination_query_params)
        response.raise_for_status()
        country_data = response.json()
        return country_data["locations"][0]["code"]

    def find_flight(self, city_code, days_for_trip, date_from: datetime, date_to: datetime):

        url = self.endpoint + "/v2/search"
        flight_search_params = {
            "fly_from": "TLV",
            "fly_to": city_code,
            "date_from": date_from.strftime(TIME_FORMAT),
            "date_to": date_to.strftime(TIME_FORMAT),
            "return_from": (date_from + timedelta(days_for_trip)).strftime(TIME_FORMAT),
            "return_to": date_to.strftime(TIME_FORMAT),
            "flight_type": "return",
            "adults": 2,
            "limit": 50,
            "curr": "USD",
            "max_stopovers": 2
        }

        response = requests.get(url=url, headers=self.header, params=flight_search_params)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print("no results were found!")
            return None

        date_from = data["route"][0]["local_departure"].split("T")[0]
        date_to = data["route"][-1]["local_arrival"].split("T")[0]

        flight = FlightData(
            data["cityTo"],
            data["cityCodeTo"],
            date_from,
            date_to,
            data["price"],
            data["deep_link"])

        return flight
