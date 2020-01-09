import os
import pytest
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from app.models import *


@pytest.fixture
def client():
    # 设置测试数据库路径和测试环境
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TEST'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

    # 初始化测试数据库
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(User(username='test', password='test'))
            db.session.commit()
            db.session.close()
        yield client


# 测试环境下用户登录登出类
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post('/login', data={'username': username, 'password': password})

    def logout(self):
        return self._client.get('/user/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)


