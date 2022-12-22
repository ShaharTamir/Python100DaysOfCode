from flask import Flask, render_template
from random import randint
import requests
from time import sleep

random_number = 0
app = Flask(__name__)


@app.route("/")
def hello():
    global random_number
    random_number = randint(0, 9)
    return """<h1>Guess the number from 0 to 9!!</h1>
    <img src="https://media0.giphy.com/media/Vibsr6IH5JybVK32dP/giphy.gif?cid=ecf05e47ekocugxe012qwkwe7wigob04366m941kwbwut6u8&rid=giphy.gif&ct=g">
    """


@app.route("/guess/<int:number>")
def make_guess(number):
    if number == random_number:
        return """
        <p style="font-weight: bold; font-size: 50px;">SUCCESS!!</p>
        <img src="https://media3.giphy.com/media/3orieUe6ejxSFxYCXe/giphy.gif?cid=ecf05e470404uqsecrdmpobg1e9sj9cqgci0ngrylrb2gfpz&rid=giphy.gif&ct=g">
        <p>To start again go to <a href="http://localhost:5000/"> hello </a> page </p>
        """
    # print(f"psst.. the number is {random_number}")
    if number > random_number:
        string = "Too high,"
    else:
        string = "Too low,"

    return f"""
    <p style="color:red; font-weight: bold; font-size: 50px;">{string} Guess again...</p>
    <img src="https://media1.giphy.com/media/LSKN6u6u6BWpZRWyyq/giphy.gif?cid=ecf05e476pccwiu1b86ifkutr5jqd8a818aahr2wtq04n9pw&rid=giphy.gif&ct=g">
    """


def try_get_url(url, params, header):
    response = ''
    while response == '':
        try:
            response = requests.get(url, params=params, headers=header)
        except requests.exceptions.SSLError:
            print("failed once, try again in 1 sec")
            sleep(1)
        else:
            return response


@app.route("/guess/some_name/<name>")
def send_name(name):
    gender_api_url = "https://api.genderize.io"
    age_api_url = "https://api.agify.io"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        "Accept-Language": 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    api_params = {
        "name": name
    }

    gender_response = try_get_url(gender_api_url, api_params, headers)
    gender_response.raise_for_status()
    gender = gender_response.json()["gender"]

    age_response = try_get_url(age_api_url, api_params, headers)
    age_response.raise_for_status()
    age = age_response.json()["age"]

    return render_template("name_guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
