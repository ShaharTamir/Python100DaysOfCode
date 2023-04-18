from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import sqlite3


class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    author_name = StringField('Author Name', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
    submit = SubmitField('Submit')


# database init SQLite
# db = sqlite3.connect("books-collection.db", check_same_thread=False)
# cursor = db.cursor()

# flask app init
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SomeRandomString'
Bootstrap(app)

# database init SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(30), nullable=False)
    author_name = db.Column(db.String(40), nullable=False)
    rate = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '%s - %s - %r/10.0' % (self.book_name, self.author_name, self.rate)


with app.app_context():
    db.create_all()

all_books = []
# create table : cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

@app.route('/')
def home():
    global all_books
    # SQLite code
    # all_books = cursor.execute('SELECT * FROM books').fetchall()
    all_books = Book.query.all()
    return render_template('index.html', book_list=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        data = form.data
        ''' SQLite code
        cursor.execute(f'INSERT INTO books VALUES({len(all_books) + 1}, "{data["book_name"]}", "{data["author_name"]}", {data["rating"]})')
        db.commit() '''

        new_book = Book(id=len(all_books) + 1, book_name=data["book_name"], author_name=data["author_name"],
                        rate=data["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    if 'POST' == request.method and request.form.get('new_rate'):
        book_to_update = Book.query.get(book_id)
        book_to_update.rate = request.form.get('new_rate')
        db.session.commit()
        return redirect(url_for('home'))
    book = [b for b in all_books if b.id == book_id]
    return render_template('edit.html', book=book[0])


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

