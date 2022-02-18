#!usr/bin/python
"""
    Merchandise shop auth API views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from .auth_api import bp_api_auth
    app.register_blueprint(bp_api_auth)
