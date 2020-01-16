from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required

from app.extensions import lm, db
from app.forms.user import LoginForm, RegisterForm
from app.models.user import User

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@login_required
def home():
    return redirect(url_for('post.all_posts'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)

        user = User.query.filter(User.username == form.username.data).first()

        if user is None:
            flash('User does not exist.', 'danger')
            return redirect(url_for('main.login'))
        elif user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Incorrect password.', 'danger')
            return redirect(url_for('main.login'))

    return render_template('login.html', title='Login', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)

        if User.query.filter(User.username == form.username.data).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('main.register'))

        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        flash('Successfully registered.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



