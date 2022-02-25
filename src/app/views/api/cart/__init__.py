#!usr/bin/python
"""
    Merchandise shop cart API views.
"""

from typing import NoReturn

from flask import Flask

from .cart_api import bp_api_cart


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    """
    app.register_blueprint(bp_api_cart)
