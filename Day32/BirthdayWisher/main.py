import pandas
import datetime as dt
import smtplib
from random import choice

MY_EMAIL = "shahar1360@gmail.com"
APP_PASSWORD = # TODO: python_gmail_app_password
LETTERS = ["letter1.txt", "letter2.txt", "letter3.txt"]


def happy_birthday_msg(to, age, name):
    msg = f"From: {MY_EMAIL}\nTo: {to}\nSubject: Happy Birthday!\n\n"
    file = choice(LETTERS)
    with open(f"Letters/{file}", "r") as letter:
        msg += letter.read().replace("[name]", f"{name}").replace("[age]", f"{age}")
    return msg


date = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="index")
today_birthdays = [person for person in birthdays.values() if
                   person["month"] == date.month and person["day"] == date.day]

if len(today_birthdays) > 0:
    with smtplib.SMTP("smtp.gmail.com") as email_connection:
        email_connection.starttls()
        email_connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        for person in today_birthdays:
            age = date.year - person["year"]
            msg = happy_birthday_msg(person["email"], age, person["name"])
            email_connection.sendmail(MY_EMAIL, person["email"], msg=msg)
        email_connection.close()
