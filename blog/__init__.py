import sentry_sdk
from flask import Flask, render_template
from flask_uploads import configure_uploads
from sentry_sdk.integrations.flask import FlaskIntegration

from blog.config import app_config
from blog.views import blueprints
from blog.extensions import db, migrate, lm, icon, ckeditor, bootstrap
from blog.models.user import User

SENTRY_DSN = "https://f057f89dff9a4e34a3d8433a643aabf8@sentry.io/1887833"


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
    register_error_handlers(app)
    sentry_sdk.init(dsn=SENTRY_DSN,
                    integrations=[FlaskIntegration()])

    @lm.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)


def register_error_handlers(app):

    @app.errorhandler(404)
    def error_404(error):
        return render_template('error.html', error=error)

    @app.errorhandler(500)
    def error_500(error):
        return render_template('error.html', error=error)
