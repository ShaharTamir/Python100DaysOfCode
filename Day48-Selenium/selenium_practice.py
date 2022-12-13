from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pprint


def get_python_events(driver):
    driver.get("https://www.python.org/")
    upcoming_events_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')
    print(upcoming_events_elements)
    upcoming_events = []

    for event in upcoming_events_elements:
        event_name_link = event.find_element(By.TAG_NAME, "a")
        name = event_name_link.text
        link = event_name_link.get_property("href")
        time = event.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        time = time.split("T")[0]
        upcoming_events.append({"name": name, "link": link, "time": time})

    driver.quit()
    pprint.pprint(upcoming_events)


def wiki_practice(driver):
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    english_values = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
    # print(english_values.text)
    # english_values.click()
    portals = driver.find_element(By.LINK_TEXT, 'Content portals')
    # print(portals)
    # portals.click()
    searchbar = driver.find_element(By.NAME, 'search')
    searchbar.send_keys("Python")
    searchbar.send_keys(Keys.ENTER)


chrome_driver_path = "~/Downloads/installs/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
wiki_practice(driver)





