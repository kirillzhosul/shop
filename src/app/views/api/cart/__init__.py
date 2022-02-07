#!usr/bin/python
"""
    Merchandise shop cart API views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from .cart_api import bp_api_cart
    app.register_blueprint(bp_api_cart)
