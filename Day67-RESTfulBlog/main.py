from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()
    '''post1 = BlogPost(
        title="The Life of Cactus",
        subtitle="Who knew that cacti lived such interesting lives.",
        date="10 November 2022",
        body="Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. "
             "Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. "
             "Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea "
             "sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
        author="Shahar Tamir",
        img_url="static/img/post-sample-image.jpg"
    )
    post2 = BlogPost(
        title="Top 15 Things to do When You are Bored",
        subtitle="Are you bored? Don't know what to do? Try these top 15 activities.",
        date="21 September 2021",
        body="Chase ball of string eat plants, meow, "
             "and throw up because I ate plants going to catch the red dot today going to catch the red dot today. "
             "I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get"
             " up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.",
        author="Shahar Tamir",
        img_url="static/img/post-sample-image.jpg"
    )
    post3 = BlogPost(
        title="Introduction to Intermittent Fasting",
        subtitle="Learn about the newest health craze.",
        date="12 October 2020",
        body="Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. "
             "Halvah croissant candy canes bonbon candy. "
             "Apple pie jelly beans topping carrot cake danish tart cake cheesecake. "
             "Muffin danish chocolate soufflé pastry icing bonbon oat cake. "
             "Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.",
        author="Shahar Tamir",
        img_url="static/img/post-sample-image.jpg"
    )
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()'''


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.session.query(BlogPost).get(post_id)
    if requested_post:
        return render_template("post.html", post=requested_post)
    return jsonify(error="Post ID not found"), 404


@app.route("/edit_post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post_data = BlogPost.query.get(post_id)
    form = CreatePostForm(
        title=post_data.title,
        subtitle=post_data.subtitle,
        author=post_data.author,
        img_url=post_data.img_url,
        body=post_data.body
    )
    if form.validate_on_submit():
        post_data.title = form.title.data
        post_data.subtitle = form.subtitle.data
        post_data.body = form.body.data
        post_data.author = form.author.data
        post_data.img_url = form.img_url.data

        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form, is_edit=True)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        publish_date = date.today().strftime("%d %B %Y")
        post = BlogPost(
            title=form.data.get("title"),
            subtitle=form.data.get("subtitle"),
            date=publish_date,
            body=form.data.get("body"),
            author=form.data.get("author"),
            img_url=form.data.get("img_url")
        )
        db.session.add(post)
        db.session.commit()
        
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=False)


@app.route("/delete_post/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(debug=True)
