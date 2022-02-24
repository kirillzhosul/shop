#!usr/bin/python
"""
    Merchandise shop static views.
"""

from typing import NoReturn
from flask import Flask

from .static import bp_static


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    app.register_blueprint(bp_static)

