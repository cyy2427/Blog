from .user import user
from .article import article
from .main import main
from .post import post

blueprints = ((user, '/user'),
              (article, '/article'),
              (main, '/'),
              (post, '/post')
              )
