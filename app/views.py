from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, login_required, current_user
from app import app, lm, db
from app.forms import LoginForm, RegisterForm
from app.models import User
from app.user import user
from app.post import post
from app.article import article

# 主视图
app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(article)


# 主页
@app.route('/')
@login_required
def welcome():
    return redirect(url_for('post.all_posts'))


# 用户注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)
            return redirect(render_template('register.html', title='Register', form=form))

        # 密码两次输入验证
        if form.password1.data != form.password2.data:
            flash('passwords did not match')
            return redirect(render_template('register.html', title='Register', form=form))

        new_user = User(username=form.username.data, password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        flash('Successfully registered.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# 用户登录
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
            return redirect(url_for('post.all_posts'))
        elif User.query.filter(User.username == form.username.data).first():
            flash('Incorrect password.', 'danger')
            return redirect(url_for('login'))
        else:
            flash('User does not exist.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
