from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from os import environ
from datetime import datetime, timedelta

# INIT
flight_search_key = environ.get("TEQUILA_FLIGHT_SEARCH_KEY")
username = "shahar1360@gmail.com"
password = environ.get("PY_GMAIL_PASS")

searcher = FlightSearch(flight_search_key)
data_manager = DataManager()
alerter = NotificationManager(username, password)

data_manager.get_price_sheet_data()
data_manager.get_subscribers()

date_from = datetime.now() + timedelta(days=7)
date_to = datetime.now() + timedelta(days=30*6)
min_days_for_trip = 10

for row in data_manager.prices:
    row["iata"] = searcher.get_destination_code(row["destination"])
    data_manager.curr_flights.append(searcher.find_flight(row["iata"], min_days_for_trip, date_from, date_to))
    if row["price"] == "" or row["price"] > data_manager.curr_flights[-1].price:
        row["price"] = data_manager.curr_flights[-1].price

data_manager.update_price_sheet_data()

top_cheapest = data_manager.get_top_cheapest()

for flight in top_cheapest:
    for user in data_manager.users:
        alerter.alert_flight(flight, user)

print("alerts have been sent.")
