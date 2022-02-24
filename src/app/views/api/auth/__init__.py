#!usr/bin/python
"""
    Merchandise shop application auth API views.
"""

from typing import NoReturn

from flask import Flask

from .auth_api import bp_api_auth


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    """
    app.register_blueprint(bp_api_auth)
