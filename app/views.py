from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user
from app import app, lm, db
from app.forms import LoginForm, RegisterForm
from app.models import User
from app.user import user
from app.post import post


app.register_blueprint(user)
app.register_blueprint(post)


@app.route('/')
def welcome():
    return render_template('start.html')


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
            return redirect(url_for('user.index'))
        else:
            flash('Incorrect username or password.')
            return redirect(url_for('login'))

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
