#!usr/bin/python
"""
    Merchandise shop views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Regisgers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from . import root
    app.register_blueprint(root.bp_root)
