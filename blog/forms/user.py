from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import InputRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('username is null')])
    password = PasswordField('Password', validators=[InputRequired('password is null')])
    login = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('username is null')])
    password = PasswordField('Password1', validators=[InputRequired('password is null'),
                                                      EqualTo('confirm', 'Passwords must match')])
    confirm = PasswordField('Password2', validators=[InputRequired('password is null')])
    register = SubmitField('Register')


class IconForm(FlaskForm):
    icon = FileField('Choose Field', validators=[InputRequired('No file selected')])
    upload = SubmitField('upload')