import os

from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user

from blog.extensions import db
from blog.forms.text import PostForm, ReviewForm
from blog.models.text import Post, PostReview

# 短文本蓝图
post = Blueprint('post', __name__)


@post.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_post = Post(body=form.body.data,
                            user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            db.session.close()
            return redirect(url_for('post.all_posts'))

    return render_template('new_post.html',
                           form=form,
                           user=current_user)


# 短文本列表显示（按时间倒序）
@post.route('/all', methods=['GET'])
@login_required
def all_posts():
    posts = Post.query.order_by(Post._datetime.desc()).all()
    return render_template('posts.html',
                           posts=posts,
                           user=current_user)


@post.route('/<int:post_id>', methods=['GET'])
@login_required
def show_post(post_id):
    target_post = Post.query.get(post_id)
    if target_post is None:
        abort(404)
    reviews = target_post.reviews
    rv_count = len(reviews)
    form = ReviewForm()
    return render_template('show_post.html', form=form,
                           post=target_post, user=current_user,
                           reviews=reviews, rv_count=rv_count)


@post.route('/<int:post_id>', methods=['POST'])
@login_required
def review_post(post_id):
    review_form = ReviewForm()

    if review_form.validate_on_submit():
        review_body = review_form.body.data
        new_review = PostReview(body=review_body,
                                user_id=current_user.id,
                                post_id=post_id)
        db.session.add(new_review)
        db.session.commit()
        db.session.close()
        flash('Review submitted.')
        return redirect(url_for('post.show_post', post_id=post_id))


@post.route('/<int:post_id>/edit', methods=['GET'])
@login_required
def edit_post(post_id):
    if Post.query.get(post_id) is None:
        abort(404)

    edit_post = Post.query.get(post_id)
    if current_user.id == edit_post.user_id:
        edit_form = PostForm()
        return render_template('new_post.html',
                               form=edit_form,
                               user=current_user)


@post.route('/<int:post_id>/del', methods=['GET'])
@login_required
def delete_post(post_id):
    if Post.query.get(post_id) is None:
        abort(404)
    del_post = Post.query.get(post_id)
    if current_user.id == del_post.user_id:
        if del_post.reviews is not None:
            reviews = del_post.reviews
            for review in reviews:
                db.session.delete(review)
        db.session.delete(del_post)
        db.session.commit()
        db.session.close()
        flash("Post deleted.", 'success')
        return redirect(url_for('post.all_posts'))
    else:
        return redirect(url_for('post.all_posts')), 403


@post.errorhandler(404)
def post_not_found(error):
    if os.path.split(request.path)[-1].isdigit():
        message = {'name': 'Post not found.',
                   'description': 'Please check your access to right post.'}
        return render_template('error.html', error=message), 404
    else:
        return render_template('error.html', error=error)



