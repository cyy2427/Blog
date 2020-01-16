from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user

from app.extensions import db
from app.forms.text import ReviewForm, ArticleForm
from app.models.text import Article, ArticleReview


# 长文本（文章）内容蓝图
article = Blueprint('article', __name__)


# 文章列表显示（按时间倒叙）
@article.route('/all')
@login_required
def all_articles():
    articles = Article.query.order_by(Article._datetime.desc()).all()
    return render_template('articles.html', articles=articles, user=current_user)


# 发布新文章
@article.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = ArticleForm()
    if request.method == 'POST':
        title = form.title.data
        body = form.body.data
        new_article = Article(title=title, body=body, user_id=current_user.id)
        db.session.add(new_article)
        db.session.commit()
        db.session.close()
        flash('Article submitted.')
        return redirect(url_for('article.all_articles'))
    return render_template('new_article.html', user=current_user, form=form)


# 文章详情（根据文章id查找）
@article.route('/<int:article_id>', methods=['GET', 'POST'])
@login_required
def show_article(article_id):
    target_article = Article.query.get(article_id)
    if target_article is None:
        abort(404)

    reviews = target_article.reviews
    rv_count = len(reviews)

    # 评论发表和提交
    form = ReviewForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)

        review_body = form.review.data
        review = ArticleReview(body=review_body, user_id=current_user.user_id, article_id=article_id)
        db.session.add(review)
        db.session.commit()
        db.session.close()
        flash('Review submitted.')
        return redirect(url_for('article.show_article', article_id=article_id))

    return render_template('show_article.html', user=current_user,
                           article=target_article, form=form,
                           reviews=reviews, rv_count=rv_count)