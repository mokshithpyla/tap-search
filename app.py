from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "flask rocks!"
    app.config.from_object(__name__)