#!usr/bin/python
"""
    Merchandise shop legal views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from . import legal
    app.register_blueprint(legal.bp_legal)
