from flask import url_for
from app.models import User
from flask_login import current_user


def register(client, username, password):
    return client.post('/register', data={"username": username, "password1":password, "password2": password},
                       follow_redirects=True)


def test_register(client):
    get_response = client.get('/register')
    assert get_response.status_code == 200

    register_response = register(client, 'test123', 'test123')
    assert b'Successfully registered.' in register_response.data
    assert register_response.status_code == 200

    assert User.query.filter(User.username == 'test123', User.password == 'test123').first() is not None


def test_login(client, auth):

    get_response = client.get('/login')
    assert get_response.status_code == 200

    login_response = auth.login()
    assert url_for('post.all_posts') in login_response.headers['Location']
    assert current_user.username == 'test'


def test_logout(auth):
    auth.login()
    assert current_user.username == 'test'

    auth.logout()
    assert current_user.is_authenticated is False





