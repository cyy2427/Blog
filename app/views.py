from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, login_required
from app import app, lm
from app.forms import LoginForm
from app.models import User


@login_required
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'cyy'}  # fake user
    posts = [{'author': {'nickname': 'John'}, 'body': 'Beautiful day!'},
             {'author': {'nickname': 'Susan'}, 'body': 'Cool Movie!'}]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/register', methods=['GET',POST])
def register():
    form = RegisterForm()


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
            return render_template("index.html")

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


