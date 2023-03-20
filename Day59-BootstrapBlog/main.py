from flask import Flask, render_template
from datetime import datetime
import requests

"""

COPY THIS TO https://www.npoint.io/docs/
[
  {
    "id": 1,
    "title": "The Life of Cactus",
    "subtitle": "Who knew that cacti lived such interesting lives.",
    "user": "Shahar Tamir",
    "user_page": "#!",
    "date": "10 November 2022",
    "content": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify."
  },
  {
    "id": 2,
    "title": "Top 15 Things to do When You are Bored",
    "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
    "user": "Shahar Tamir",
    "user_page": "#!",
    "date": "21 September 2021",
    "content": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today."
  },
  {
    "id": 3,
    "title": "Introduction to Intermittent Fasting",
    "subtitle": "Learn about the newest health craze.",
    "user": "Shahar Tamir",
    "user_page": "#!",
    "date": "12 October 2020",
    "content": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake."
  }
]
"""



app = Flask(__name__)
year = datetime.now().year

response = requests.get("https://api.npoint.io/bdc98b988e17b28dbe89") #TODO: copy the generated url for JSON here.
response.raise_for_status()
response.encoding = 'UTF-8'
blog_posts = response.json()


@app.route("/")
def home():
    global year
    return render_template("index.html", name="Shahar Tamir", curr_year=year, blog_posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", post=blog_posts[post_id - 1])


if __name__ == "__main__":
    app.run(debug=True)
