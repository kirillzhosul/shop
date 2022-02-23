#!usr/bin/python
"""
    Merchandise shop developer views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    with app.app_context():
        from . import documentation
        app.register_blueprint(documentation.bp_dev_docs)
