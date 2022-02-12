#!usr/bin/python
"""
    Merchandise shop error handler.
"""

from typing import Tuple
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from werkzeug.exceptions import HTTPException

from .names import NAMES


def __handle(error: HTTPException):
    return getattr(error, "code", 500)


def __render(code):
    if code == 401:
        return redirect(url_for("auth.index"))

    name = NAMES[code] if code in NAMES else "UNKNOWN"

    return render_template(
        "errors/handler.jinja",
        code=code, addr=request.remote_addr,
        name=name, user=current_user
    ), code


def handler(error: HTTPException) -> Tuple[str, int]:
    return __render(__handle(error))

