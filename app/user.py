from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g
from flask_login import login_required, current_user, logout_user
from app import app, lm, db
from app.forms import LoginForm, RegisterForm, PostForm
from app.models import User, Post

user = Blueprint('user', __name__, url_prefix='/user')


@login_required
@user.route('/')
def index():
    posts = [{'author': {'nickname': 'John'}, 'body': 'Beautiful day!'},
             {'author': {'nickname': 'Susan'}, 'body': 'Cool Movie!'}]
    return render_template("index.html",
                           title='Home',
                           user=current_user,
                           posts=posts)


@user.route('/newpost', methods=['GET', 'POST'])
@login_required
def newpost():
    form = PostForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)
            return render_template('newpost.html', title='New Post', form=form)

        post_body = form.post.data
        post = Post(body=post_body, user_id=current_user.user_id)
        db.session.add(post)
        db.session.commit()
        flash("New post created successfully.")
        return redirect(url_for('index'))

    return render_template('newpost.html', title='New Post', form=form)


@login_required
@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
