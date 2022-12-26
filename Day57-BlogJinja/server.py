from flask import Flask, render_template
from blog_post import BlogPost
from datetime import datetime
app = Flask(__name__)
blog = []
year = datetime.now().year

@app.route("/")
def home_page():
    global blog

    blog = [
        BlogPost("Hello", "My pleasure", "content content"),
        BlogPost("Hello2", "My pleasure2", "content content"),
        BlogPost("Hello3", "My pleasure3", "content content")
    ]

    return render_template("index.html", blog_posts=blog, num_posts=len(blog), year=year)


@app.route("/blog/<int:num>")
def get_blog(num):
    print(blog[num])
    return render_template("post.html", post=blog[num], year=year)


if "__main__" == __name__:
    app.run(debug=True)

