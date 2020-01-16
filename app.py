import os

from flask_app import create_app

config_name = os.getenv('APP_CFG') or 'dev'
app = create_app(config_name)
