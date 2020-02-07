import pytest

from blog import create_app
from blog.extensions import db
from blog.models.user import User


@pytest.fixture
def client():
    # 设置测试数据库路径和测试环境
    app = create_app('test')

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


