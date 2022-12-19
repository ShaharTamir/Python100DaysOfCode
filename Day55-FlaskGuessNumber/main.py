from flask import Flask
from random import randint

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


if __name__ == "__main__":
    app.run(debug=True)
