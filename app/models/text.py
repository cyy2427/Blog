from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr

from app.extensions import db
from app.models.user import User


class Text(db.Model):

    # 作为基类，将不创建表
    __abstract__ = True

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body = db.Column(db.String(), nullable=True)
    datetime = db.Column(db.DateTime, default=datetime.now, nullable=False)

    @declared_attr
    def user_id(self):
        return db.Column('author', db.ForeignKey('user.id'), nullable=False)

    @property
    def author(self):
        author = User.query.get(self.user_id)
        return author

    @property
    def datetime(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M')

    @property
    def username(self):
        return self.author.username

    @property
    def icon_path(self):
        return self.author.icon_path


class Post(Text):
    like = db.Column(db.Integer, default=0, nullable=False)
    reviews = db.relationship('PostReview', backref='post')

    def __repr__(self):
        return '<Post %r>' % self.id


class Article(Text):
    title = db.Column(db.String(50), nullable=False)
    like = db.Column(db.Integer, default=0, nullable=False)
    reviews = db.relationship('ArticleReview', backref='article')

    def __repr__(self):
        return '<Article %r>' % self.id


class PostReview(Text):
    body = db.Column(db.String(), nullable=False)
    post_id = db.Column(db.ForeignKey('post.id'), nullable=False)


class ArticleReview(Text):
    body = db.Column(db.String(), nullable=False)
    article_id = db.Column(db.ForeignKey('article.id'), nullable=False)

