import os


class DevConfig:

    DEBUG = True

    POSTGRES_HOST = '172.16.0.5'
    POSTGRES_PORT = '54322'
    POSTGRES_USER = 'intern'
    POSTGRES_PW = 'intern'
    POSTGRES_DB = 'helloflask'
    POSTGRES_TEST_DB = 'helloflask_test'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s'\
                              % (POSTGRES_USER, POSTGRES_PW, POSTGRES_HOST,
                                 POSTGRES_PORT, POSTGRES_DB)

    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.urandom(666)
    RECAPTCHA_PUBLIC_KEY = os.urandom(110)
    RECAPTCHA_PRIVATE_KEY = os.urandom(110)

    UPLOADED_ICON_DEST = '/static/uploads/'
    UPLOADED_ICON_ALLOW = 'IMAGES'
