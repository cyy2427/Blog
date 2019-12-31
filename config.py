import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
UPLOADED_ICON_DEST = os.path.join(basedir, 'static/uploads')
CKEDITOR_SERVE_LOCAL = True

CSRF_ENABLED = True
SECRET_KEY = 'hello-flask'
