import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app.models import User, Post

posts = Post.query.filter(User.username == 'cyy2427').all()
for post in posts:
    print(post.user_id)
    print(post.body)

