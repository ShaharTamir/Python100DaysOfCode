from flask import Flask, render_template, request
import smtplib

app = Flask(__name__, template_folder="./")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/action", methods=["POST"])
def action():
    d = request.form.to_dict()
    name = request.form.get("name")
    password = request.form.get("password")
    print(d, name, password)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

