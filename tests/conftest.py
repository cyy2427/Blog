import os
import pytest
from app import app
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from app.models import *


@pytest.fixture
def client():
    app.config['TEST'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

    with app.test_client() as client:
        with app.app_context():
            test_db = SQLAlchemy()
            test_db.init_app(app)
            test_db.create_all()
        yield client

    test_db.drop_all()

