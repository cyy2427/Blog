from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g
from flask_login import login_required, current_user, logout_user
from app import app, lm, db
from app.forms import LoginForm, RegisterForm, PostForm
from app.models import User, Post

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
@login_required
def index():
    if current_user is not None:
        return render_template("start.html", user=current_user)
    else:
        flash("Please login to access this page.")
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
        flash("New post created successfully.")
        return redirect(url_for('user.index'))

    return render_template('newpost.html', title='New Post', form=form, user=current_user)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@user.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@user.route('/myposts')
@login_required
def myposts():
    posts = Post.query.filter(User.username == current_user.username).all()
    return render_template('posts.html', posts=posts, user=current_user)
