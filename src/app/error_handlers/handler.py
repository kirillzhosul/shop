#!usr/bin/python
"""
    Merchandise shop error handler.
"""

from typing import Tuple, Optional
from flask import Flask, render_template, request, redirect, url_for
from flask_login import current_user
from werkzeug.exceptions import HTTPException

from .names import NAMES


def __handle(error: HTTPException, app: Optional[Flask]):
    if app:
        app.logger.error(error.description)
    return getattr(error, "code", 500)


def __render(code):
    if code == 401:
        return redirect(url_for("auth.index"))

    return render_template(
        "errors/handler.jinja",
        code=code, addr=request.remote_addr,
        name=NAMES[code], user=current_user
    ), code


def handler(error: HTTPException, app: Optional[Flask] = None) -> Tuple[str, int]:
    return __render(__handle(error, app))

