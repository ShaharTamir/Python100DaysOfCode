import smtplib
import os
import datetime as dt
from random import choice

SUNDAY = 6
MY_EMAIL = "shahar1360@gmail.com"
APP_PASSWORD = os.environ.get("PY_GMAIL_PASS")
TO_EMAIL = "shahar.tamir@infinitylabs.co.il"
SUBJECT = "Weekly motivational quote"

date = dt.datetime.now()
day_of_week = date.weekday()  # Monday is 0...

if day_of_week == SUNDAY:
    with open("quotes.txt", "r") as quotes:
        quote = choice(quotes.readlines())

    msg = f"From: {MY_EMAIL}\nTo: {TO_EMAIL}\nSubject: {SUBJECT}\n\n"
    msg += quote

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(MY_EMAIL, TO_EMAIL, msg=msg)
        connection.close()
        print("email sent")
