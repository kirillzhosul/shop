#!usr/bin/python
"""
    Merchandise shop shop views.
"""

from typing import NoReturn
from flask import Flask

from . import (
    catalog, item
)


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    app.register_blueprint(catalog.bp_catalog)
    app.register_blueprint(item.bp_item)
