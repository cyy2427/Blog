def test_posts(client):
    get_response = client.get('post/all')
    assert get_response.status_code == 200


def test_newpost(client):
    get_response = client.get('user/newpost')
    assert get_response.status_code == 200
