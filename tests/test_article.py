from flask_app.models.text import Article, ArticleReview


def test_articles(client, auth):
    auth.login()

    get_response = client.get('article/all')
    assert get_response.status_code == 200


def test_new_article(client, auth):
    auth.login()

    get_response = client.get('article/new')
    assert get_response.status_code == 200

    post_response = client.post('article/new', data={'title': 'test',
                                                     'body': 'test'})
    assert post_response.status_code == 302

    article = Article.query.get(1)
    assert article.title == 'test'
    assert article.user_id == 1
    assert article.body == 'test'
    assert article.datetime is not None

    show_article = client.get('article/1')
    assert show_article.status_code == 200


def test_article_review(client, auth):
    auth.login()

    client.post('article/new', data={'title': 'test',
                                     'body': 'test'})
    client.post('article/1', data={'body': 'test review'})
    review = ArticleReview.query.get(1)
    assert review.user_id == 1
    assert review.article_id == 1
    assert review.body == 'test review'
    assert review.datetime is not None


def test_del_article(client, auth):
    auth.login()
    client.post('article/new', data={'title': 'test',
                                     'body': 'test'})
    client.post('article/1', data={'body': 'test review'})
    article = Article.query.get(1)
    assert article.reviews[0].body == 'test review'

    response = client.get('article/1/del', follow_redirects=True)
    assert response.status_code == 200
    assert Article.query.get(1) is None
