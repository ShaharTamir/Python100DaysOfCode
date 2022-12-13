from bs4 import BeautifulSoup
import requests
import os
import smtplib

EMAIL_PASS = os.environ.get("PY_GMAIL_PASS")
EMAIL = "shahar1360@gmail.com"

with open("URLs.txt", "r") as url_file:
    urls = url_file.readlines()

with open("TargetPrices.txt", "r") as prices_file:
    prices = prices_file.readlines()

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
           "Accept-Language": 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7'}
items_under_target_price = []

for i in range(len(prices)):
    response = requests.get(
        urls[i],
        headers=headers
    )

    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        price_whole = soup.find(name="span", class_="a-price-whole").text
        price_fraction = soup.find(name="span", class_="a-price-fraction").text
    except AttributeError:
        print("page not loaded properly. try again later. skip.")
    else:
        price = int(price_whole.split(".")[0])
        if price < float(prices[i]):
            items_under_target_price.append({"url": urls[i], "price": price})


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(EMAIL, EMAIL_PASS)
    msg = f"From: {EMAIL}\nTo: {EMAIL}\nSubject: amazon price drop\n\n"
    msg += "your item is under target price. buy!:\n\n"
    for item in items_under_target_price:
        msg += f"{item['url']} : price: {item['price']}"
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=msg)

print("email sent\n")
