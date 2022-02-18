#!usr/bin/python
"""
    Merchandise shop order API views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from .order_api import bp_api_order
    app.register_blueprint(bp_api_order)
