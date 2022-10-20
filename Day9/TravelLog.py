'''
Write a function that will work with the following 
line of code to add the entry for Russia to the travel_log:

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.
'''

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
  travel_log.append({
    "country": country,
    "visits": visits,
    "cities": cities,
  })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
