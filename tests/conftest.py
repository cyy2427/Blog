import os
import pytest
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from app.models import *


@pytest.fixture
def client():
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TEST'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

