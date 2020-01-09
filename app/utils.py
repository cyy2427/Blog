import os
from app.models import User
from datetime import datetime


def get_icon_path(icon_path):
    if icon_path is None:
        return None
    else:
        icon_folder = '/static/uploads/icons'
        return os.path.join(icon_folder, icon_path)


def get_author(model):
    d = {}
    author = User.query.get(model.user_id)
    d['username'] = author.username
    d['icon_path'] = get_icon_path(author.icon_path)
    return d


def model_to_dict(model, *colnames):
    d = {}
    for col in colnames:
        value = getattr(model, col)
        if isinstance(value, datetime):
            value = value.strftime('%Y-%m-%d %H:%M')
        d[col] = value
    return d


def models_to_json(models, *colnames):
    j = []
    for model in models:
        author = get_author(model)
        content = model_to_dict(model, *colnames)
        d = dict(author, **content)
        j.append(d)
    return j
