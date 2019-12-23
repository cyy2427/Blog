from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password = PasswordField('password', validators=[DataRequired('password is null')])
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password1 = PasswordField('password1', validators=[DataRequired('password1 is null')])
    password2 = PasswordField('password2', validators=[DataRequired('password2 is null')])


class PostForm(FlaskForm):
    post = TextAreaField('Post:', validators=[DataRequired('post is null')])
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    review = TextAreaField('Review:', validators=[DataRequired('review is null')])
    submit = SubmitField('Submit')
