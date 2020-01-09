import os
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user, logout_user
from app import db, icon
from app.forms import PostForm, IconForm
from app.models import User, Post
from app.utils import get_icon_path

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
@login_required
def index():
    if current_user is not None:
        return render_template("start.html", user=current_user)
    else:
        flash('Please login to access this page.', 'info')
        return redirect(url_for('login'))


@user.route('/newpost', methods=['GET', 'POST'])
@login_required
def newpost():
    form = PostForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)
            return render_template('newpost.html', title='New Post', form=form, user=current_user)

        post_body = form.post.data
        post = Post(body=post_body, user_id=current_user.user_id)
        db.session.add(post)
        db.session.commit()
        db.session.close()
        flash("New post created successfully.")
        return redirect(url_for('user.index'))

    return render_template('newpost.html', title='New Post', form=form, user=current_user)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@user.route('/myposts')
@login_required
def myposts():
    posts = db.session.query(Post.body, User.username).filter(User.username == current_user.username).all()
    return render_template('posts.html', posts=posts, user=current_user)


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    icon_path = get_icon_path(current_user.icon_path)
    form = IconForm()
    if request.method == 'POST' and form.validate_on_submit():
        filename = icon.save(request.files['icon'], folder='icons')
        user = User.query.get(current_user.user_id)
        user.icon_path = os.path.split(filename)[-1]
        db.session.commit()
        flash('Icon uploaded.')
        return redirect(url_for('user.profile'))
    return render_template('profile.html', user=current_user, icon_path=icon_path, form=form)

