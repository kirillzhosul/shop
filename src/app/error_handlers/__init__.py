#!usr/bin/python
"""
    Merchandise shop error handlers views.
"""

from typing import NoReturn, Tuple, Optional
from flask import Flask, render_template, request
from flask_login import current_user
from werkzeug.exceptions import HTTPException

NAMES = {
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error",

    418: "I'm a teapot",
}


def raise_error(code: int, description: Optional[str] = None):
    error = HTTPException(
        description,
        None
    )
    error.code = code
    return handler(error)


def handler(error: HTTPException, app: Optional[Flask] = None) -> Tuple[str, int]:
    if app:
        app.logger.error(error.description)
    code = getattr(error, "code", 500)
    return render_template("errors/handler.jinja",
                           code=code,
                           name=NAMES[code],
                           user=current_user,
                           addr=request.remote_addr
                           ), code


def register(app: Flask) -> NoReturn:
    """
    Registers all error handlers views.
    :param: app Flask application.
    :return:
    """

    def __handler(error: HTTPException) -> Tuple[str, int]:
        return handler(error, app)

    for code in NAMES.keys():
        app.errorhandler(code)(__handler)
