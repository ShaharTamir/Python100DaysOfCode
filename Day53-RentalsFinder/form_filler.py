from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException


class FormFiller:

    def __init__(self, form_link):
        chrome_driver_path = "/home/shahar/Downloads/installs/chromedriver_linux64/chromedriver"
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        self.form_link = form_link

    def new_form(self, address, price, link):
        self.driver.get(self.form_link)
        not_loaded = True
        while not_loaded:
            try:
                fields = self.driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")
                fields[0].send_keys(address)
            except ElementNotInteractableException:
                print("not interactable!! got the wrong element!")
            except IndexError:
                print("elements not found")
                return
            else:
                not_loaded = False

        fields[1].send_keys(price)
        fields[2].send_keys(link)
        submit = self.driver.find_element(By.CLASS_NAME, "uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd")
        submit.click()
