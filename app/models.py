from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):

    user_id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(20))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    __tablename__ = 'user'

    def __init__(self, user_id, username, password):

        self.user_id = user_id
        self.username = username
        self.password = password


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return '<User %r>' % self.nickname


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User %r>' % self.body
