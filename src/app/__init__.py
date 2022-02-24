#!env/bin/python
# Refactoring by SantaSpeen
# 23.02.2022
"""
    Merchandise shop application.
    Provides full application via 'create()' that returns ready to be runned application.
"""

from os.path import exists as path_exists
from typing import NoReturn, Type, Optional

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .config import *
from . import (
    views,                  # Flask views.
    error_handlers,         # Flask error handlers.
)


__author__ = "Kirill Zhosul"
__copyright = "(c) 2022 Kirill Zhosul"
__license__ = "MIT"


# Database global object,
# referenced in business (database) logic,
# and also in database model classes.
db = SQLAlchemy()


def login_manager_init_app(app: Flask) -> NoReturn:
    """
    Initialises login manager.
    :param app: Flask application.
    """

    # Should be here, as uses database model (db),
    # used in user loader.
    from .models.user.user import User  # pylint: disable=import-outside-toplevel, unused-import

    lm = LoginManager()
    lm.init_app(app)

    # Login manager also allows specifying refresh view,
    # but for now it is not done yet.
    # lm.refresh_view = "auth.refresh"

    lm.login_view = "auth.index"
    lm.login_message = "Пожалуйста авторизуйтесь для продолжения!"
    lm.needs_refresh_message = (
        u"Для безопасности, войдите заного в свой аккаунт для продолжения."
    )

    @lm.user_loader
    def user_loader(uid: int) -> Optional[User]:
        """
        Flask login user loader, should return user object or none.
        :param uid: User index for database query.
        :return: User or none.
        """
        return User.query.get(int(uid))


def create(name: str = None, cfg: Type[Config] = ConfigProduction) -> Flask:
    """
    Returns ready to be runned application.
    :param: name Flask import_name, preferred to be omitted.
    :return: Flask application.
    """

    app = Flask(name if name else __name__)
    app.url_map.strict_slashes = False

    # Config.
    app.config.from_object(cfg)
    app.url_map.strict_slashes = False

    # Register views and error handlers.
    views.register(app)
    error_handlers.register(app)

    # Database.

    # That import is used, because db.init_app and db.create_all references all database models.
    from . import models  # pylint: disable=import-outside-toplevel, unused-import
    db.init_app(app)
    if not path_exists(app.config.get("SQLALCHEMY_DATABASE_FILEPATH")):
        db.create_all(app=app)

    # Login manager.
    login_manager_init_app(app)

    return app
