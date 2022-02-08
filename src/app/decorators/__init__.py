#!usr/bin/python
"""
    Merchandise shop application decorators.
"""

from typing import Callable
from functools import wraps

from flask import redirect, url_for, flash, request, jsonify
from flask_login import current_user


# TODO: Add message argument.
def login_required(always_json: bool = False) -> Callable:
    """
    Decorator that allows only authenticated user to continue to page.
    :param: always_json If true, will return JSON even if it is GET request.
    """

    def decorator(route_function: Callable):
        @wraps(route_function)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                if request.method != "GET" or always_json:
                    return jsonify({
                        "error": "Авторизуйтесь для выполнения запроса!",
                        "authentication_required": True
                    }), 401
                else:
                    flash("Авторизуйтесь для продолжения!", category="error")
                    return redirect(url_for("profile.view"))
            return route_function(*args, **kwargs)
        return wrapper
    return decorator
