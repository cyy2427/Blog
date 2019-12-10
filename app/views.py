from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'cyy'}  # fake user
    posts = [{'author': {'nickname': 'John'}, 'body': 'Beautiful day!'},
             {'author': {'nickname': 'Susan'}, 'body': 'Cool Movie!'}]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)