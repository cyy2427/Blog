from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    user_id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(20))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    __tablename__ = 'user'

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
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviews = db.relationship('Review', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post %r>' % self.body


class Review(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body = db.Column(db.String(100))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Review %r>' % self.body
