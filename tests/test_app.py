def test_home(auth, client):

    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200

    auth.login()
    response_after_login = client.get('/', follow_redirects=True)
    assert response_after_login.status_code == 200


