from bs4 import BeautifulSoup
import requests
from pprint import pprint


class ZillowScraper:

    def __init__(self, link):
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        self.link = link
        self.property_prefix = "https://www.zillow.com"
        response = requests.get(
            self.link,
            headers=self.header
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        self.all_data = soup.find_all(class_="property-card-data")

    def extract_text(self, name: str, location: int, splitter: str):
        data = []
        for item in self.all_data:
            data_text = item.findNext(name).text
            data.append(data_text.split(splitter)[location])
        return data

    def get_addresses(self):
        addresses = self.extract_text("address", -1 , "| ")
        return addresses

    def get_prices(self):
        prices = self.extract_text("span", 0 , "+")
        prices = [int(price.replace("$", "").replace(",", "")) for price in prices]
        return prices

    def get_links(self):
        links = [self.property_prefix + item.findNext("a").get("href") for item in self.all_data]
        return links
