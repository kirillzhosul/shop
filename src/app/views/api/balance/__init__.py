#!usr/bin/python
"""
    Merchandise shop balance API views.
"""

from typing import NoReturn

from flask import Flask

from .balance_api import bp_api_balance


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    """
    app.register_blueprint(bp_api_balance)
