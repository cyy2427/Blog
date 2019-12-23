import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import db
from app.models import User, Post, Review

posts = Post.query.filter(User.username == 'cyy2427').all()
for post in posts:
    print(post.user_id)
    print(post.body)

review_sample = Review(body='Nice!', post_id=1, user_id=1)
db.session.add(review_sample)
db.session.commit()
r = Review.query.get(1)
print(r.body)
db.session.delete(r)
db.session.commit()




