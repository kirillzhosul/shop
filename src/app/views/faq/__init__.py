#!usr/bin/python
"""
    Merchandise shop FAQ views.
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
        from . import faq
        app.register_blueprint(faq.bp_faq)
