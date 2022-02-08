#!usr/bin/python
"""
    Merchandise shop favorites API views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from .favorites_api import bp_api_favorites
    app.register_blueprint(bp_api_favorites)
