from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

TIMEOUT = 20
chrome_driver_path = "/home/shahar/Downloads/installs/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.bezeq.co.il/internetandphone/internet/speedtest/")
finished = False

# go into the 2 frames to access the speed test tags.
try:
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
except NoSuchElementException:
    print("page not loaded properly. exit.")
    driver.quit()
    exit()

attempts = 0
while not finished and attempts < TIMEOUT:
    sleep(3)
    attempts += 1
    try:
        results_elem = driver.find_element(By.CSS_SELECTOR, '.test--finished')
        finished = True
    except NoSuchElementException:
        print("not yet found")


if attempts == TIMEOUT:
    print("not found.")
    exit()

results = results_elem.find_elements(By.CSS_SELECTOR, '.number.monochrome-primary')
keys = ["ping", "down", "up"]
speed = {}

for i in range(len(results)):
    speed[keys[i]] = results[i].text

print(speed)

driver.quit()
