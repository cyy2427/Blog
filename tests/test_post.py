from app.models import Post, PostReview


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
    post = Post.query.get(1)
    assert post.user_id == 1
    assert post.body == 'test post'
    assert post.datetime is not None

    show_post = client.get('post/1')
    assert show_post.status_code == 200


def test_review(client, auth):
    auth.login()

    post_response = client.post('user/newpost', data={'post': 'test post'})
    review_response = client.post('post/1', data={'review': 'test review'})
    review = PostReview.query.get(1)
    assert review.user_id == 1
    assert review.post_id == 1
    assert review.body == 'test review'
    assert review.datetime is not None
