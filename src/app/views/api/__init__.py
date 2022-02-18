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
    auth.register(app)
    cart.register(app)
    favorites.register(app)
    balance.register(app)
    balance.register(app)

    from .health import bp_api_health
    app.register_blueprint(bp_api_health)