from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class EditMovieRateFrom(FlaskForm):
    rate = FloatField(name='rate', label='Your Rating out of 10 e.g. 7.3',
                      validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(120))
    img_url = db.Column(db.String(), nullable=False)


with app.app_context():
    db.create_all()

search_results = []


def sort_func(movie):
    return movie.rating


@app.route("/")
def home():
    global search_results
    search_results = []
    movie_list = Movie.query.all()
    movie_list.sort(reverse=True, key=sort_func)
    # new_movie = Movie(title="Phone Booth",
    # year=2002,
    # description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    # rating=7.3,
    # ranking=10,
    # review="My favourite character was the caller.",
    # img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    return render_template("index.html", movie_list=movie_list)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        return redirect(url_for("select", movie_title=form.data["title"]))
    return render_template("add.html", form=form)


@app.route("/select/<movie_title>")
def select(movie_title):
    global search_results
    movie_db_url = "https://api.themoviedb.org/3/search/movie"
    movie_request_params = {
        "api_key": "dfa9e550f7df4d74c89e5b9a88dd8cd5",
        "language": "en-US",
        "include-adult": False,
        "query": movie_title
    }

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    response = session.get(movie_db_url, params=movie_request_params, verify=False)
    response.raise_for_status()
    data = response.json()
    search_results = data["results"]
    return render_template("select.html", movies_data=data["results"])


@app.route("/add_selected/<int:movie_id>")
def add_selected(movie_id):
    global search_results
    images_url = "https://image.tmdb.org/t/p/w500"
    movie = [i for i in search_results if i["id"] == movie_id][0]
    new_movie = Movie(
        title=movie["original_title"],
        year=movie["release_date"][0:4],
        description=movie["overview"],
        rating=0.0,
        img_url=images_url + movie["poster_path"]
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", movie_id=new_movie.id))


@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    form = EditMovieRateFrom()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = form.data["rate"]
        movie_to_update.review = form.data["review"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    db.session.delete(Movie.query.get(movie_id))
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
