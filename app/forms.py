from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('username is null')])
    password = PasswordField('Password', validators=[DataRequired('password is null')])
    remember_me = BooleanField('Remember me', default=False)
    login = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password1 = PasswordField('password1', validators=[DataRequired('password1 is null')])
    password2 = PasswordField('password2', validators=[DataRequired('password2 is null')])
    register = SubmitField('Register')


class PostForm(FlaskForm):
    post = CKEditorField('Post:', validators=[DataRequired('post is null')])
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    review = TextAreaField('Review:', validators=[DataRequired('review is null')])
    submit = SubmitField('Review')


class IconForm(FlaskForm):
    icon = FileField('Choose File', validators=[DataRequired('No file selected')])
    submit = SubmitField('Upload')
