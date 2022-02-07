#!usr/bin/python
"""
    Merchandise shop auth views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from . import auth
    app.register_blueprint(auth.bp_auth)
