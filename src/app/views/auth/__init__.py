#!usr/bin/python
"""
    Merchandise shop application auth views.
"""

from typing import NoReturn

from flask import Flask

from . import auth


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    """
    app.register_blueprint(auth.bp_auth)
