from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.forms import ReviewForm
from app.models import User, Post, PostReview
import os

post = Blueprint('post', __name__, url_prefix='/post')


@post.route('/all')
@login_required
def all_posts():
    if current_user.icon_path is None:
        icon_path = None
    else:
        icon_folder = '/static/uploads/icons'
        icon_path = os.path.join(icon_folder, current_user.icon_path)
    posts = db.session.query(Post.body, Post.datetime, User.username).all()

    return render_template('posts.html', posts=posts, user=current_user, icon_path=icon_path)


@post.route('/<int:post_id>', methods=['GET', 'POST'])
@login_required
def show_post(post_id):
    target_post = Post.query.get(post_id)
    post_user = User.query.get(target_post.user_id)
    reviews = target_post.reviews

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
                           reviews=reviews, post_user=post_user, user=current_user)



