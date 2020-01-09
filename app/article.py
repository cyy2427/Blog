from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.forms import ReviewForm, ArticleForm
from app.models import User, Article
from app.utils import *
import os

article = Blueprint('article', __name__, url_prefix='/article')


@article.route('/all')
@login_required
def all_articles():
    articles = models_to_json(Article.query.all(), 'title', 'body', 'datetime')
    icon_path = get_icon_path(current_user.icon_path)
    return render_template('articles.html', user=current_user, icon_path=icon_path, articles=articles)


@article.route('/new', methods=['GET', 'POST'])
@login_required
def write_article():
    form = ArticleForm()
    if request.method == 'POST':
        title = form.title.data
        body = form.body.data
        new_article = Article(title=title, body=body, user_id=current_user.user_id)
        db.session.add(new_article)
        db.session.commit()
        db.session.close()
        flash('Article submitted.')
        return redirect(url_for('article.all_articles'))
    return render_template('new_article.html', user=current_user, form=form)


@article.route('/<int:article_id>', methods=['GET', 'POST'])
@login_required
def show_article(article_id):
    target_article = Article.query.get(article_id)
    author = User.query.get(target_article.user_id)

    return render_template('show_article.html', user=current_user)