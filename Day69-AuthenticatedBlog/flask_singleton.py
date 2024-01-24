from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


class FlaskSingleton:

    def __new__(cls, name='main'):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FlaskSingleton, cls).__new__(cls)
            cls.instance.app = Flask(name)
            cls.instance.app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
            cls.instance.ckeditor = CKEditor(cls.instance.app)
            Bootstrap(cls.instance.app)
            cls.instance.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
            # cls.instance.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            cls.instance.db = SQLAlchemy(cls.instance.app)
            cls.instance.login_manager = LoginManager()
            cls.instance.login_manager.init_app(cls.instance.app)
        return cls.instance

    @classmethod
    def get_app(cls) -> Flask:
        return cls.instance.app

    @classmethod
    def get_db(cls) -> SQLAlchemy:
        return cls.instance.db

    @classmethod
    def get_login_manager(cls):
        return cls.instance.login_manager
