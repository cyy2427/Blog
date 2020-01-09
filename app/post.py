from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.forms import ReviewForm
from app.models import User, Post, PostReview
from app.utils import *

# 短文本蓝图
post = Blueprint('post', __name__, url_prefix='/post')


# 短文本列表显示（按时间倒序）
@post.route('/all')
@login_required
def all_posts():
    icon_path = get_icon_path(current_user.icon_path)
    posts = models_to_json(Post.query.order_by(Post.datetime.desc()).all(),
                           'body', 'datetime', 'id')
    return render_template('posts.html', posts=posts, user=current_user, icon_path=icon_path)


# 短文本详情显示（根据id）
@post.route('/<int:post_id>', methods=['GET', 'POST'])
@login_required
def show_post(post_id):
    target_post = Post.query.get(post_id)
    post_user = User.query.get(target_post.user_id)
    reviews = models_to_json(target_post.reviews, 'body', 'datetime')
    icon_path = get_icon_path(post_user.icon_path)
    rv_count = len(reviews)

    # 评论发布
    form = ReviewForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)

        review_body = form.review.data
        review = PostReview(body=review_body, user_id=current_user.user_id, post_id=post_id)
        db.session.add(review)
        db.session.commit()
        db.session.close()
        flash('Review submitted.')
        return redirect(url_for('post.show_post', post_id=post_id))
    return render_template('show_post.html', form=form, post=target_post,
                           post_user=post_user, user=current_user, icon_path=icon_path,
                           reviews=reviews, rv_count=rv_count)



