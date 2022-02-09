#!env/bin/python
"""
    Merchandise shop application.
    Provides full application via 'create()' that returns ready to be runned application.
"""

from os.path import exists as path_exists
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .config import *

__author__ = "Kirill Zhosul"
__copyright = "(c) 2022 Kirill Zhosul"
__license__ = "MIT"

# Global objects.
db: SQLAlchemy = SQLAlchemy()
lm: LoginManager = LoginManager()


def login_manager_init_app(app: Flask):
    """
    Initialises login manager.
    :param app: Flask application.
    """
    from .models.user.user import User  # pylint: disable=import-outside-toplevel, unused-import
    lm.init_app(app)

    @lm.user_loader
    def user_loader(uid):
        if uid is None or uid == 'None':
            uid = -1

        try:
            return User.query.get(int(uid))
        except Exception:
            return None


def create(name=None, cfg: object = ConfigProduction) -> Flask:
    """
    Returns ready to be runned application.
    :param: name Flask import_name, preferred to be omitted.
    :return: Flask application.
    """
    app = Flask(name if name else __name__)

    # Config.
    app.config.from_object(cfg)

    # Database.
    from . import models
    db.init_app(app)
    if not path_exists(app.config.get("SQLALCHEMY_DATABASE_FILEPATH")):
        db.create_all(app=app)

    # Views.
    from . import views
    views.register(app)

    # Error handlers.
    from . import error_handlers
    error_handlers.register(app)

    # Login manager.
    login_manager_init_app(app)

    # String slashes.
    app.url_map.strict_slashes = False

    return app
