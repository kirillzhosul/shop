#!usr/bin/python
"""
    Merchandise shop profile views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from . import profile
    app.register_blueprint(profile.bp_profile)