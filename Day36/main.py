import smtplib   # emailing
import os        # getenv vars access tokens
import requests  # API requests
from stock import Stock

NEWS_API_KEY = os.environ.get("STOCK_NEWS_PASS")
STOCKS_HOURS_API_KEY = os.environ.get("STOCK_HOURS_PASS")
EMAIL_PASS = os.environ.get("PY_GMAIL_PASS")
EMAIL = "shahar1360@gmail.com"


def is_the_stock_open():
    hours_url = "https://financialmodelingprep.com/api/v3/is-the-market-open"
    hours_params = {
        "apikey": STOCKS_HOURS_API_KEY
    }
    response = requests.get(hours_url, params=hours_params)
    return response.json()["isTheStockMarketOpen"]


def get_headlines(stock_name: str = ""):
    news_url = "https://newsapi.org/v2/top-headlines"
    news_params = {
        "q": stock_name,
        "sources": "bloomberg,business-insider,fortune",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(news_url, params=news_params)
    response.raise_for_status()
    headlines = response.json()
    articles = ""
    for article in headlines["articles"]:
        articles += article + "\n"
    return articles


if not is_the_stock_open():
    stock = Stock("QCOM")
    stock_headlines = get_headlines("qualcom")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, EMAIL_PASS)
        msg = f"From: {EMAIL}\nTo: {EMAIL}\nSubject: daily stocks report\n\n"
        msg += f"{stock}\n{stock_headlines}"
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=msg.encode("utf8"))
    print("email sent")

