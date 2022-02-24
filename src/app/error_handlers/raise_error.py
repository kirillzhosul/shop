#!usr/bin/python
"""
    Merchandise shop application error raising function.
"""

from typing import Optional

from flask import Response
from werkzeug.exceptions import HTTPException

from .handler import handler


def raise_error(code: int, description: Optional[str] = None) -> Response:
    """
    Raises error by returning Response to you.
    :param code: Code of the error which you want to raise.
    :param description: Description of the error which you want to raise.
    :return: Response which you should return as response.
    """
    error = HTTPException(description, None)
    error.code = code

    return handler(error)

