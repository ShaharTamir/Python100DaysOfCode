from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        new_user = User(email=form_data["email"],
                        password=generate_password_hash(password=form_data["password"],
                                                        method="pbkdf2:sha256:1",
                                                        salt_length=8),
                        name=form_data["name"]
                        )
        # TODO: Add try catch for unique user verify
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    logout_user()
    if 'POST' == request.method:
        user = db.session.query(User).filter(User.email == request.form.get("email")).first()
        if user and check_password_hash(pwhash=user.password, password=request.form.get("password")):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash("Error logging in -\nwrong password or username")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
def download():
    return send_from_directory(directory="./", path="static/files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
