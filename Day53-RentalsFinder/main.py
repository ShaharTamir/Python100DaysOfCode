from form_filler import FormFiller
from zillow_scraper import ZillowScraper
from time import sleep

ZILLLOW_LINK = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.52863852539966%2C%22east%22%3A-122.3387810424895%2C%22south%22%3A37.700780072379324%2C%22north%22%3A37.8111203510859%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfnLXU7s7xRo82ZWzLMaSAx4XKMK1RKF4UjL2H_hx3fZTrv0Q/viewform"

san_fransisco_scraper = ZillowScraper(link=ZILLLOW_LINK)
form = FormFiller(FORM_LINK)

addresses = san_fransisco_scraper.get_addresses()
links = san_fransisco_scraper.get_links()
prices = san_fransisco_scraper.get_prices()

for i in range(len(addresses)):
    form.new_form(addresses[i], prices[i], links[i])
    sleep(0.5)

