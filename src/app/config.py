#!usr/bin/python
"""
    Config files for app configuration.
    Contains several classes for the app.
"""

import os


# Base config.
class Config:
    # Secret key, should be overriden inside inherited production / development.
    SECRET_KEY = os.urandom(12).hex()

    # Server settings (werkzeug).
    HOST = "127.0.0.1"
    PORT = 5000

    # Utils.
    FLASK_SECRET_KEY = SECRET_KEY
    JSON_AS_ASCII = False

    # Debug.
    DEBUG = False

    # Database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_FILENAME = "database\\database.db"
    SQLALCHEMY_DATABASE_FILEPATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                SQLALCHEMY_DATABASE_FILENAME)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{SQLALCHEMY_DATABASE_FILEPATH}"


# Config, that should be used for development purposes.
class ConfigDevelopment(Config):
    # Secret.
    SECRET_KEY = os.getenv("FLASK_DEVELOPMENT_SECRET_KEY") or "development-secret-key"

    # Server.
    HOST = "0.0.0.0"
    PORT = 80

    # Debug.
    DEBUG = True


# Config, that should be used for production.
class ConfigProduction(Config):
    # Secret.
    SECRET_KEY = os.getenv("MERCHANDISE_SHOP_SECRET_KEY")

    # Server.
    HOST = "127.0.0.1"
    PORT = 10001

    # Debug.
    DEBUG = False
