from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "~/Downloads/installs/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.amazon.com/Garmin-Forerunner-Smartwatch-Advanced-Dynamics/dp/B07QLVHBLF/ref=sr_1_3?crid=9WASWNC8212X&keywords=garmin+245&qid=1670574254&sprefix=garmin+245%2Caps%2C234&sr=8-3")
price = driver.find_element(By.XPATH, "//div[@id='corePrice_feature_div']")
print(f"price element: {price}")
print(f"price text: {price.text.split()}")

driver.quit()
