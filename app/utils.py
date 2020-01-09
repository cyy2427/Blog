import os
from app.models import User
from datetime import datetime


# 数据库用户表的头像路径只存储文件名，通过此函数得到相对路径用于前端头像显示
def get_icon_path(icon_path):
    if icon_path is None:
        return None
    else:
        icon_folder = '/static/uploads/icons'
        return os.path.join(icon_folder, icon_path)


# 获取文本的作者用户对象的用户名和头像路径用于展示
def get_author(model):
    d = {}
    author = User.query.get(model.user_id)
    d['username'] = author.username
    d['icon_path'] = get_icon_path(author.icon_path)
    return d


# 将query所得的models列表转换未json格式用于jinja2模板渲染
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
