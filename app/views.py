from datetime import datetime
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, login_required, current_user
from app import app, lm
from app.forms import LoginForm, RegisterForm, PostForm
from app.models import User, Post, db


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = current_user
    posts = [{'author': {'nickname': 'John'}, 'body': 'Beautiful day!'},
             {'author': {'nickname': 'Susan'}, 'body': 'Cool Movie!'}]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/newpost', methods=['GET', 'POST'])
@login_required
def newpost():
    user = current_user
    form = PostForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)
            return render_template('newpost.html', title='New Post', form=form)

        post_body = form.post.data
        post = Post(body=post_body, user_id=user.user_id)
        db.session.add(post)
        db.session.commit()
        flash("New post created successfully.")
        return redirect(url_for('index'))

    return render_template('newpost.html', title='New Post', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)
            return redirect(render_template('register.html', title='Register', form=form))
        if form.password1.data != form.password2.data:
            flash('passwords did not match')
            return redirect(render_template('register.html', title='Register', form=form))

        user = User(username=form.username.data, password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash('successfully registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)
            return redirect(render_template('login.html', title='Sign In', form=form))

        user = User.query.filter(User.username == form.username.data, User.password == form.password.data).first()

        if user:
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
