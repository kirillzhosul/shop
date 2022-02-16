#!usr/bin/python
"""
    Config files for app configuration.
    Contains several classes for the
"""

import os


# Base config.
class Config:
    # Secret key, should be rewritten
    SECRET_KEY = os.urandom(12).hex()

    # Utils.
    FLASK_SECRET_KEY = SECRET_KEY
    JSON_AS_ASCII = False
    DEBUG = False

    # Database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_FILENAME = "database\\database.db"
    SQLALCHEMY_DATABASE_FILEPATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                SQLALCHEMY_DATABASE_FILENAME)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{SQLALCHEMY_DATABASE_FILEPATH}"


# Config, that should be used for development purposes.
class ConfigDevelopment(Config):
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY") or "development-secret-key"
    DEBUG = True


# Config, that should be used for production.
class ConfigProduction(Config):
    SECRET_KEY = os.getenv("MERCHANDISE_SHOP_SECRET_KEY")
    DEBUG = False
