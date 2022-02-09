#!usr/bin/python
"""
    Config files for app configuration.
    Contains several classes for the
"""

import os


# Base config.
class Config:
    SECRET_KEY = "very-strong-secret-key-for-hackers"
    FLASK_SECRET_KEY = SECRET_KEY

    DEBUG = False

    JSON_AS_ASCII = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_FILENAME = "database\\database.db"
    SQLALCHEMY_DATABASE_FILEPATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                SQLALCHEMY_DATABASE_FILENAME)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{SQLALCHEMY_DATABASE_FILEPATH}"


# Config, that should be used for development purposes.
class ConfigDevelopment(Config):
    DEBUG = True


# Config, that should be used for production.
class ConfigProduction(Config):
    DEBUG = False
