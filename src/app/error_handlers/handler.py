#!usr/bin/python
"""
    Merchandise shop error handler.
"""

from flask import render_template, request, redirect, url_for, Response
from flask_login import current_user
from werkzeug.exceptions import HTTPException

from .names import NAMES


def __get_error_code(error: HTTPException) -> int:
    """
    Returns error code from error.
    :param error: Error from which to get error code.
    :return: Error code.
    """
    return getattr(error, "code", 500)


def __render(code) -> Response:
    """
    Renders error code.
    :param code: Code to render.
    :return: Response to show (or even may be redirect).
    """
    if code == 401:
        return redirect(url_for("auth.index"))

    name = NAMES[code] if code in NAMES else "UNKNOWN"
    return Response(render_template(
        "errors/handler.jinja",
        code=code, addr=request.remote_addr, path=request.path,
        name=name, user=current_user
    ), code)


def handler(error: HTTPException) -> Response:
    """
    Handles error from Flask.
    :param error: Error to handle.
    :return: Rendered response or redirect.
    """
    return Response(__render(__get_error_code(error)))

