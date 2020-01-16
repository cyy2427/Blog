from flask import url_for
from flask_login import current_user

from flask_app.models.user import User


def register(client, username, password):
    return client.post('/register', data={"username": username,
                                          "password": password,
                                          "confirm": password},
                       follow_redirects=True)


def test_register(client):
    get_response = client.get('/register')
    assert get_response.status_code == 200

    register_response = register(client,
                                 username='test123',
                                 password='test123')
    assert b'Successfully registered.' in register_response.data
    assert register_response.status_code == 200

    assert User.query.filter(User.username == 'test123') is not None
    user = User.query.filter(User.username == 'test123').first()
    assert user.check_password('test123')


def test_login(client, auth):

    get_response = client.get('/login')
    assert get_response.status_code == 200

    login_response = auth.login()
    assert url_for('main.home') in login_response.headers['Location']
    assert current_user.username == 'test'


def test_logout(auth):
    auth.login()
    assert current_user.username == 'test'

    auth.logout()
    assert current_user.is_authenticated is False





