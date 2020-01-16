import os

from app import create_app

config_name = os.getenv('CFG') or 'dev'
app = create_app(config_name)
