from app import create_app

config_name = 'dev'
app = create_app(config_name)
app.run()

