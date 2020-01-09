from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import DataRequired


# 登陆表单
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('username is null')])
    password = PasswordField('Password', validators=[DataRequired('password is null')])
    remember_me = BooleanField('Remember me', default=False)
    login = SubmitField('Login')


# 注册表单
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('username is null')])
    password1 = PasswordField('password1', validators=[DataRequired('password1 is null')])
    password2 = PasswordField('password2', validators=[DataRequired('password2 is null')])
    register = SubmitField('Register')


# 短文本发布表单
class PostForm(FlaskForm):
    post = TextAreaField('Post:', validators=[DataRequired('post is null')])
    submit = SubmitField('Submit')


# 长文本发布表单
class ArticleForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired('title is null')])
    body = CKEditorField(validators=[DataRequired('body is null')])
    submit = SubmitField('Submit')


# 评论发布表单
class ReviewForm(FlaskForm):
    review = TextAreaField('Review:', validators=[DataRequired('review is null')])
    submit = SubmitField('Review')


# 头像文件上传表单
class IconForm(FlaskForm):
    icon = FileField('Choose File', validators=[DataRequired('No file selected')])
    submit = SubmitField('Upload')
