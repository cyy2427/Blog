from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user

from flask_app.extensions import db
from flask_app.forms.text import PostForm, ReviewForm
from flask_app.models.text import Post, PostReview

# 短文本蓝图
post = Blueprint('post', __name__)


@post.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_post = Post(body=form.body.data, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            db.session.close()
            return redirect(url_for('post.all_posts'))

    return render_template('new_post.html', form=form, user=current_user)


# 短文本列表显示（按时间倒序）
@post.route('/all')
@login_required
def all_posts():
    posts = Post.query.order_by(Post._datetime.desc()).all()
    return render_template('posts.html', posts=posts, user=current_user)


# 短文本详情显示（根据id）
@post.route('/<int:post_id>', methods=['GET', 'POST'])
@login_required
def show_post(post_id):
    target_post = Post.query.get(post_id)
    if target_post is None:
        abort(404)
    reviews = target_post.reviews
    rv_count = len(reviews)

    # 评论发布
    form = ReviewForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)

        review_body = form.body.data
        review = PostReview(body=review_body, user_id=current_user.id, post_id=post_id)
        db.session.add(review)
        db.session.commit()
        db.session.close()
        flash('Review submitted.')
        return redirect(url_for('post.show_post', post_id=post_id))
    return render_template('show_post.html', form=form,
                           post=target_post, user=current_user,
                           reviews=reviews, rv_count=rv_count)




