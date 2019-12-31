import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
lm = LoginManager()
lm.login_view = "/login"
lm.init_app(app)


icon = UploadSet('icon', IMAGES)
configure_uploads(app, icon)

bootstrap = Bootstrap(app)
ckeditor = CKEditor(app)

from app import views, models
