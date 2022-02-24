#!usr/bin/python
"""
    Merchandise shop application legal views.
"""

from typing import NoReturn
from flask import Flask

from . import legal


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param app: Flask application.
    """
    app.register_blueprint(legal.bp_legal)
