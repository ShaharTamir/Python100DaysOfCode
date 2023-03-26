import pandas
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def build_val(number, value):
    new_val = ""
    for _ in range(number):
        new_val += value
    return new_val, new_val


COFFEE_CHOICES = [build_val(num, '☕️') for num in range(1, 6)]
WIFI_CHOICES = [build_val(num, '💪') for num in range(1, 6)]
POWER_CHOICES = [build_val(num, '🔌') for num in range(1, 6)]
WIFI_CHOICES.insert(0, ('✘', '✘'))
POWER_CHOICES.insert(0, ('✘', '✘'))


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=COFFEE_CHOICES, validators=[DataRequired()])
    wifi_strength = SelectField('WIFI Strength Rating', choices=WIFI_CHOICES, validators=[DataRequired()])
    power_socket = SelectField('Power Socket Availability', choices=POWER_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = form.data
        data.popitem()
        data.popitem()
        data_frame = pandas.DataFrame([data])
        data_frame.to_csv('cafe-data.csv', mode='a', index=False, header=False)
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
