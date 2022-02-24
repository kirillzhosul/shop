#!usr/bin/python
"""
    Merchandise shop profile views.
"""

from typing import NoReturn
from flask import Flask

from . import profile


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param app: Flask application.
    """
    app.register_blueprint(profile.bp_profile)
