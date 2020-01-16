from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required

from flask_app.extensions import db
from flask_app.forms.user import LoginForm, RegisterForm
from flask_app.models.user import User

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@login_required
def home():
    return redirect(url_for('post.all_posts'))


@main.route('/login', methods=['GET'])
def login_get():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@main.route('/login', methods=['POST'])
def login_post():
    form = LoginForm()
    if not form.validate_on_submit():
        flash(form.errors)

    user = User.query.filter(User.username == form.username.data).first()

    if user is None:
        flash('User does not exist.', 'danger')
        return redirect('/login')
    elif user.check_password(form.password.data):
        login_user(user)
        return redirect(url_for('main.home'))
    else:
        flash('Incorrect password.', 'danger')
        return redirect('/login')


@main.route('/register', methods=['GET'])
def register_get():
    form = RegisterForm()
    return render_template('register.html', title='Register', form=form)


@main.route('/register', methods=['POST'])
def register_post():
    form = RegisterForm()
    if not form.validate_on_submit():
        flash(form.errors)
        return redirect('/register')

    if User.query.filter(User.username == form.username.data).first():
        flash('Username already exists.', 'danger')
        return redirect('/register')

    new_user = User(username=form.username.data, password=form.password.data)
    db.session.add(new_user)
    db.session.commit()
    db.session.close()
    flash('Successfully registered.', 'success')
    return redirect('/login')



