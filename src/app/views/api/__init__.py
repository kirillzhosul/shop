#!usr/bin/python
"""
    Merchandise shop API views.
"""
# TODO: Catalog API.
# TODO: Categories API.
# TODO: Item API.

from typing import NoReturn

from flask import Flask

from . import (
    cart, favorites, auth, balance, order  # Account API.
)


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    # Passing to next register functions.
    [module.register(app) for module in (
        # Modules to register.
        cart, favorites, auth,
        balance, order
    )]