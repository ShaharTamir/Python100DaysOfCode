from flask import render_template, redirect, url_for, flash
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask import abort
from functools import wraps
from flask_gravatar import Gravatar
from flask_singleton import FlaskSingleton
from database_tables import BlogUser, BlogPost, BlogComment

app = FlaskSingleton().get_app()
db = FlaskSingleton.get_db()
login_manager = FlaskSingleton.get_login_manager()

with app.app_context():
    db.create_all()

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Need to log in to view our content")
    return redirect(url_for('login'))


def admin_only(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        if current_user and current_user.id == 1:
            return func(*args, **kwargs)
        else:
            abort(403)
    return wrapper_func


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    logout_user()
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = BlogUser(
            email=form.data["email"],
            password=generate_password_hash(password=form.data["password"],
                                            method="pbkdf2:sha256:1",
                                            salt_length=8),
            name=form.data["name"]
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    logout_user()
    form = LoginForm()
    if form.validate_on_submit():
        user = BlogUser.query.filter(BlogUser.email == form.data["email"]).first()
        if user and check_password_hash(user.password, form.data["password"]):
            login_user(user)
            return redirect(url_for("get_all_posts"))
        else:
            flash("Password incorrect, try again!")
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
@login_required
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = BlogComment(
            text=comment_form.text.data,
            author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
        comment_form.text.data = ''
    return render_template("post.html", post=requested_post, form=comment_form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@login_required
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/new-post", methods=['GET', 'POST'])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
