import os


class BaseConfig:

    DEBUG = False

    DB_ENGINE = os.getenv('DB_ENGINE')
    DB_API = os.getenv('DB_API')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PW = os.getenv('DB_PW')
    DB_DEV = os.getenv('DB_DEV')
    DB_TEST = os.getenv('DB_TEST')
    DB_PRODUCTION = os.getenv('DB_PRODUCTION')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f'{DB_ENGINE}+{DB_API}://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_DEV}'

    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.urandom(666)

    UPLOADED_ICON_DEST = 'blog/static/uploads/'
    UPLOADED_ICON_ALLOW = 'IMAGES'
    CKEDITOR_SERVE_LOCAL = True


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s:%s/%s' \
                              % (BaseConfig.DB_ENGINE,
                                 BaseConfig.DB_USER,
                                 BaseConfig.DB_PW,
                                 BaseConfig.DB_HOST,
                                 BaseConfig.DB_PORT,
                                 BaseConfig.DB_TEST)


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s:%s/%s' \
                              % (BaseConfig.DB_ENGINE,
                                 BaseConfig.DB_USER,
                                 BaseConfig.DB_PW,
                                 BaseConfig.DB_HOST,
                                 BaseConfig.DB_PORT,
                                 BaseConfig.DB_PRODUCTION)
