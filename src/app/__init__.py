#!env/bin/python
# Refactoring by SantaSpeen
# 23.02.2022
"""
    Merchandise shop application.
    Provides full application via 'create()' that returns ready to be runned application.
"""

from os.path import exists as path_exists
from typing import Type, NoReturn

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .config import *
from . import (
    views,                  # Init views
    error_handlers,         # Init error handlers
    models                  # SQLAlchemy models
)


__author__ = "Kirill Zhosul"
__copyright = "(c) 2022 Kirill Zhosul"
__license__ = "MIT"

# Global objects.
db: SQLAlchemy = SQLAlchemy()
lm: LoginManager = LoginManager()


def login_manager_init_app(app: Flask) -> NoReturn:
    """
    Initialises login manager.
    :param app: Flask application.
    """
    from .models.user.user import User  # pylint: disable=import-outside-toplevel, unused-import
    lm.init_app(app)

    # lm.refresh_view = "auth.refresh"
    lm.login_view = "auth.index"
    lm.login_message = "Пожалуйста авторзийтесь для продолжения!"
    lm.needs_refresh_message = (
        u"Для безопасности, войдите заного в свой аккаунт для продолжения."
    )

    @lm.user_loader
    def user_loader(uid):
        if uid is None or uid == 'None':
            uid = -1

        try:
            return User.query.get(int(uid))
        except Exception as e:
            return None


def create(name: str = None, cfg: Type[ConfigProduction] or Type[ConfigDevelopment] = ConfigProduction) -> Flask:
    """
    Returns ready to be runned application.
    :param: name Flask import_name, preferred to be omitted.
    :return: Flask application.
    """
    app = Flask(name if name else __name__)

    # Config.
    app.config.from_object(cfg)
    app.url_map.strict_slashes = False

    # Database.
    db.init_app(app)
    if not path_exists(app.config.get("SQLALCHEMY_DATABASE_FILEPATH")):
        db.create_all(app=app)

    # Register views.
    views.register(app)

    # Register error handlers.
    error_handlers.register(app)

    # Login manager.
    login_manager_init_app(app)

    # String slashes.
    app.url_map.strict_slashes = False

    return app
