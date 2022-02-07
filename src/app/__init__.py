#!env/bin/python
"""
    Merchandise shop application.
    Provides full application via 'create()' that returns ready to be runned application.
"""

from os.path import exists as path_exists
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__author__ = "Kirill Zhosul"
__copyright = "(c) 2022 Kirill Zhosul"
__license__ = "MIT"

# Global objects.
db = SQLAlchemy()


def create(name=None) -> Flask:
    """
    Returns ready to be runned application.
    :param: name Flask import_name, preferred to be omitted.
    :return: Flask application.
    """
    app = Flask(name if name else __name__)

    # Config.
    from . import config
    app.config.from_object(config.ConfigDevelopment)

    # Database.
    from . import models
    db.init_app(app)
    if not path_exists(app.config.get("SQLALCHEMY_DATABASE_FILEPATH")):
        db.create_all(app=app)

    # Views.
    from . import views
    views.register(app)

    return app
