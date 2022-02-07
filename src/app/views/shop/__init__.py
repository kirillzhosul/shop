#!usr/bin/python
"""
    Merchandise shop shop views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from . import catalog
    app.register_blueprint(catalog.bp_catalog)