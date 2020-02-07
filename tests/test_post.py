from blog.models.text import Post, PostReview


def test_posts(client, auth):
    auth.login()

    get_response = client.get('post/all')
    assert get_response.status_code == 200


def test_new_post(client, auth):
    auth.login()

    get_response = client.get('post/new')
    assert get_response.status_code == 200

    post_response = client.post('post/new', data={'body': 'test post'})
    assert post_response.status_code == 302
    post = Post.query.get(1)
    assert post.user_id == 1
    assert post.body == 'test post'
    assert post.datetime is not None

    show_post = client.get('post/1')
    assert show_post.status_code == 200


def test_post_review(client, auth):
    auth.login()

    client.post('post/new', data={'body': 'test post'})
    client.post('post/1', data={'body': 'test review'})
    review = PostReview.query.get(1)
    assert review.user_id == 1
    assert review.post_id == 1
    assert review.body == 'test review'
    assert review.datetime is not None


def test_del_post(client, auth):
    auth.login()
    client.post('post/new', data={'body': 'test post'})
    client.post('post/1', data={'body': 'test review'})
    post = Post.query.get(1)
    assert post.reviews[0].body == 'test review'

    response = client.get('post/1/del', follow_redirects=True)
    assert response.status_code == 200
    assert Post.query.get(1) is None
