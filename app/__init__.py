# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Any additional configuration or extensions can be added here

    return app
