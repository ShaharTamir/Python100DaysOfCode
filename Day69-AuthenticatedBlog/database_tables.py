from flask_singleton import FlaskSingleton
from flask_login import UserMixin
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

db = FlaskSingleton().get_db()
login_manager = FlaskSingleton.get_login_manager()


class BlogUser(UserMixin, db.Model):
    __tablename__ = "blog_users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("BlogComment", back_populates="author")
    # profile_pic: Mapped[str]


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_users.id"))
    author = relationship("BlogUser", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("BlogComment", back_populates="parent_post")


class BlogComment(db.Model):
    __tablename__ = "blog_comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_users.id"))
    author = relationship("BlogUser", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)



@login_manager.user_loader
def load_user(user_id):
    return BlogUser.query.get(user_id)

