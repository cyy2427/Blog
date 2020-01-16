import os

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flask_app.extensions import db


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    __password = db.Column('password', db.String)
    username = db.Column(db.String(64), unique=True, nullable=False)
    sex = db.Column(db.Boolean)
    nickname = db.Column(db.String(10), unique=True)
    _icon_path = db.Column('icon', db.String(20), unique=True)
    signature = db.Column(db.String(25))
    posts = db.relationship('Post', backref='user')
    articles = db.relationship('Article', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.__password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self, pw):
        return check_password_hash(self.__password, pw)

    @property
    def icon_path(self):
        if self._icon_path is None:
            return '/static/no-icon.jpg'
        else:
            return os.path.join('/static/uploads/icons', self._icon_path)



