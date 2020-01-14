from importlib import import_module

from flask import Flask
from flask_uploads import configure_uploads

from app.views import blueprints
from app.extensions import db, migrate, lm, icon, ckeditor, bootstrap


def load_config_class(config_name):
    config_class_name = '%sConfig' % config_name.capitalize()
    app_name = __name__
    config_module = import_module('%s.config.%s' % (app_name, config_name))
    config_class = getattr(config_module, config_class_name, None)
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


def register_blueprints(app):
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
