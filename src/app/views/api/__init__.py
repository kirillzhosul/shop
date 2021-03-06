#!usr/bin/python
"""
    Merchandise shop API views.
"""

from typing import NoReturn
from flask import Flask

# TODO: Catalog API.
# TODO: Categories API.


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from . import cart
    from . import favorites
    from . import auth
    from . import balance
    from . import order
    auth.register(app)
    cart.register(app)
    favorites.register(app)
    balance.register(app)
    order.register(app)