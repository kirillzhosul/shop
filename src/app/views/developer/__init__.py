#!usr/bin/python
"""
    Merchandise shop application. developer views.
"""

from typing import NoReturn

from flask import Flask

from . import documentation


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    """
    app.register_blueprint(documentation.bp_dev_docs)
