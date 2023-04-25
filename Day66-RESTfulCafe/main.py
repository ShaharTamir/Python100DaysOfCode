from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_rand_cafe():
    all_cafes = db.session.query(Cafe).all()
    rand_cafe = choice(all_cafes)
    return jsonify(cafe=rand_cafe.to_dict())


@app.route("/all", methods=['GET'])
def get_all_cafes():
    return jsonify(all_cafes=[cafe.to_dict() for cafe in db.session.query(Cafe).all()])


@app.route("/search/<loc>", methods=['GET'])
def search_cafe(loc):
    loc = loc.title()
    search_results = Cafe.query.filter(Cafe.location.startswith(loc)).all()
    print(search_results)
    if not search_results:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    return jsonify(all_cafes=[cafe.to_dict() for cafe in search_results])


def str_to_bool(s):
    if s in ["True", "true", "1"]:
        return True
    return False


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=str_to_bool(request.form.get("has_toilet")),
        has_wifi=str_to_bool(request.form.get("has_wifi")),
        has_sockets=str_to_bool(request.form.get("has_sockets")),
        can_take_calls=str_to_bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe"})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = db.session.query(Cafe).get(cafe_id)

    if not cafe_to_update:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    cafe_to_update.coffee_price = request.args.get("new_price")
    db.session.commit()

    return jsonify(response={"success": "Successfully updated the cafe"})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = "TopSecretAPIKey"
    cafe_to_delete = db.session.query(Cafe).get(cafe_id)

    if not cafe_to_delete:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    if request.args.get("api-key") == api_key:
        db.session.delete(cafe_to_delete)
        db.session.commit()
    else:
        return jsonify(error="Sorry that is not allowed. Make sure you have the correct api key."), 403

    return jsonify(response={"success": "Successfully deleted the cafe"})


if __name__ == '__main__':
    app.run(debug=True)
