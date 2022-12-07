
class FlightData:

    def __init__(self, city, code, date_from, date_to, price, link):
        self.city = city
        self.code = code
        self.date_from = date_from
        self.date_to = date_to
        self.price = price
        self.link = link

    def __str__(self) -> str:
        return f"""city: {self.city}
cityCode: {self.code}
from: {self.date_from}
to: {self.date_to}
price: {self.price}
link: {self.link}"""


def sort_key_function(data: FlightData):
    return data.price

