#!env/bin/python
"""
    Merchandise shop API service wrappers.
    Provides wrappers for API.
"""

from typing import Callable, Any

from functools import wraps

from flask import Response
from flask_login import current_user

from .response import ApiResponse
from .errors import ApiErrorType


def api_auth_required(function: Callable[[Any], Response]) -> Callable:
    """
    Decorator that will return `ApiErrorType.AUTH_REQUIRED` when user is not authenticated.
    :param function: Function to decorate.
    :return: Function
    """
    @wraps(function)
    def wrapper(*args, **kwargs) -> Response:
        """Wrapper, will return `ApiErrorType.AUTH_REQUIRED` if current user is not authenticated. """
        if not current_user.is_authenticated:
            return ApiResponse.error(ApiErrorType.AUTH_REQUIRED)

        return function(*args, **kwargs)

    return wrapper
