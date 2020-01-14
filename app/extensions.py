from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES


db = SQLAlchemy()
migrate = Migrate()

lm = LoginManager()
lm.login_view = '/login'

icon = UploadSet('icon')

ckeditor = CKEditor()
bootstrap = Bootstrap()

