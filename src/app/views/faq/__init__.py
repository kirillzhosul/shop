#!usr/bin/python
"""
    Merchandise shop FAQ views.
"""

from typing import NoReturn

from flask import Flask

from . import faq


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    app.register_blueprint(faq.bp_faq)
