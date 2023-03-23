from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=5, max=30)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5, max=16)])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "secret-key-shit"  # TODO: SECRET_KEY should have a random string.


@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect(url_for("success"))
        else:
            return redirect(url_for("denied"))
    return render_template('login.html', form=form)


@app.route("/success")
def success():
    return render_template('success.html')


@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)