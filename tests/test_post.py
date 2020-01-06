from app.models import Post


def test_posts(client, auth):
    auth.login()

    get_response = client.get('post/all')
    assert get_response.status_code == 200


def test_newpost(client, auth):
    auth.login()

    get_response = client.get('user/newpost')
    assert get_response.status_code == 200

    post_response = client.post('user/newpost', data={'post': 'test post'})
    assert post_response.status_code == 302
    assert Post.query.filter(Post.user_id == 1, Post.body == 'test post').first() is not None
