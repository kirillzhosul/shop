#!usr/bin/python
"""
    Merchandise shop error handlers views.
"""

from typing import NoReturn, Tuple
from flask import Flask
from werkzeug.exceptions import HTTPException

from .handler import handler
from .names import CODES


def register(app: Flask) -> NoReturn:
    """
    Registers all error handlers views.
    :param: app Flask application.
    :return:
    """

    def __handler(error: HTTPException) -> Tuple[str, int]:
        return handler(error, app)

    for code in CODES:
        app.errorhandler(code)(__handler)
