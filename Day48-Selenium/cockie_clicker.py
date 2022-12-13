from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_driver_path = "~/Downloads/installs/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
ids_in_store = [ "buyCursor", "buyGrandma", "buyFactory",
                 "buyMine", "buyShipment", "buyAlchemy lab",
                 "buyPortal", "buyTime machine"]
current_money = int(driver.find_element(By.ID, "money").text)
item_price = int(driver.find_element(By.ID, ids_in_store[0]).text.split("\n")[0].split()[-1])
timeout = time.time() + 5 # 5 sec timeout

while True:
    cookie.click()
    if time.time() > timeout:
        current_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        for id in ids_in_store[::-1]:
            try:
                item = driver.find_element(By.ID, id)
                item_price = int(item.text.split("\n")[0].split()[-1].replace(",", ""))
            except StaleElementReferenceException:
                print("skip this one...")
            else:
                if current_money >= item_price:
                    current_money -= item_price
                    driver.find_element(By.ID, id).click()
        timeout = time.time() + 5

