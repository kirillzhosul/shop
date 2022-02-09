#!usr/bin/python
"""
    Merchandise shop error raising function.
"""

from typing import Optional
from werkzeug.exceptions import HTTPException

from .handler import handler


def raise_error(code: int, description: Optional[str] = None):
    error = HTTPException(
        description,
        None
    )
    error.code = code
    return handler(error)

