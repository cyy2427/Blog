import importlib

from flask import Flask
from flask_uploads import configure_uploads

from flask_app.config import app_config
from flask_app.views import blueprints
from flask_app.extensions import db, migrate, lm, icon, ckeditor, bootstrap
from flask_app.models.user import User


def load_config_class(config_name):
    config_class = app_config[config_name]
    return config_class


def create_app(config_name):
    app = Flask(__name__)
    config_class = load_config_class(config_name)
    app.config.from_object(config_class)
    configure_extensions(app)
    register_blueprints(app)
    return app


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    lm.init_app(app)
    bootstrap.init_app(app)
    ckeditor.init_app(app)
    configure_uploads(app, icon)

    @lm.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)

