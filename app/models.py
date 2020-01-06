from flask_login import UserMixin
from app import db
from datetime import datetime


class User(db.Model, UserMixin):
    user_id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.Boolean)
    nickname = db.Column(db.String(10), unique=True)
    icon_path = db.Column('icon', db.String(20), unique=True)
    signature = db.Column(db.String(25))
    posts = db.relationship('Post', backref='user')
    articles = db.relationship('Article', backref='user')

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
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    reviews = db.relationship('PostReview', backref='post')

    def __repr__(self):
        return '<Post %r>' % self.body


class Article(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    reviews = db.relationship('ArticleReview', backref='article')


class ArticleReview(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.body


class PostReview(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body = db.Column(db.String(100), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.body
