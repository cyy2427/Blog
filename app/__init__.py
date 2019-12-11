from flask import Flask

app: Flask = Flask(__name__)
app.config.from_object('config')

from app import views