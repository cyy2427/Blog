def register(client, username, password):
    return client.post('/register', data={"username": username, "password1":password, "password2": password},
                       follow_redirects=True)


def login(client, username, password):
    return client.post('/login', data={'username': username, 'password': password, 'remember_me': False},
                       follow_redirects=True)


def test_register(client):
    get_response = client.get('/register')
    assert get_response.status_code == 200

    post_response = register(client, 'test123', 'test123')
    assert b'Successfully registered.' in post_response.data
    assert post_response.status_code == 200


def test_login(client):
    get_response = client.get('/login')
    assert get_response.status_code == 200

    post_response = login(client, 'nonexist', 'nonexist')
    assert b'User does not exist.' in post_response.data
    assert post_response.status_code == 200



