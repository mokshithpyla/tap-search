from flask import Flask

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.secret_key = "flask rocks!"
    app.config.from_object(__name__)