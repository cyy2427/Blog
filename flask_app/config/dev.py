import os


class BaseConfig:

    DEBUG = False

    POSTGRES_HOST = '172.16.0.5'
    POSTGRES_PORT = '54322'
    POSTGRES_USER = 'intern'
    POSTGRES_PW = 'intern'
    POSTGRES_DB = 'helloflask'
    POSTGRES_TEST_DB = 'helloflask_test'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s'\
                              % (POSTGRES_USER, POSTGRES_PW, POSTGRES_HOST,
                                 POSTGRES_PORT, POSTGRES_DB)

    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.urandom(666)

    UPLOADED_ICON_DEST = 'app/static/uploads/'
    UPLOADED_ICON_ALLOW = 'IMAGES'
    CKEDITOR_SERVE_LOCAL = True


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' \
                              % (BaseConfig.POSTGRES_USER,
                                 BaseConfig.POSTGRES_PW,
                                 BaseConfig.POSTGRES_HOST,
                                 BaseConfig.POSTGRES_PORT,
                                 BaseConfig.POSTGRES_TEST_DB)
