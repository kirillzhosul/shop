#!usr/bin/python
"""
    Merchandise shop static views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """

    from .static import bp_static
    app.register_blueprint(bp_static)

