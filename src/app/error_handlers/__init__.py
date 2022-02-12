#!usr/bin/python
"""
    Merchandise shop error handlers views.
"""

from typing import NoReturn
from flask import Flask

from .handler import handler
from .names import CODES


def register(app: Flask) -> NoReturn:
    """
    Registers all error handlers views.
    :param: app Flask application.
    :return:
    """

    for code in CODES:
        app.errorhandler(code)(handler)
