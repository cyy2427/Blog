def test_posts(client, auth):
    auth.login()

    get_response = client.get('post/all')
    assert get_response.status_code == 200


def test_newpost(client, auth):
    auth.login()

    get_response = client.get('user/newpost')
    assert get_response.status_code == 200
