from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    body = TextAreaField('Post', validators=[InputRequired('post is null')])
    submit = SubmitField('Submit')


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired('title is null')])
    body = CKEditorField('Body', validators=[InputRequired('body is null')])
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    body = TextAreaField('Review', validators=[InputRequired('Review is null')])
    submit = SubmitField('Submit')


class DeleteForm(FlaskForm):
    yes = SubmitField('Yes')
    no = SubmitField('No')
