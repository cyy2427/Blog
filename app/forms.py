from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password = StringField('password', validators=[DataRequired('password is null')])
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password1 = StringField('password', validators=[DataRequired('password is null')])
    password2 = StringField('password', validators=[DataRequired('password is null')])


class PostForm(FlaskForm)
    post = StringField('Post:', validators=[DataRequired('post is null')])
