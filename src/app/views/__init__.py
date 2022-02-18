#!usr/bin/python
"""
    Merchandise shop views.
"""

from typing import NoReturn
from flask import Flask


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    :return:
    """
    from . import root
    app.register_blueprint(root.bp_root)

    from . import shop
    from . import auth
    from . import profile
    from . import api
    from . import developer
    from . import static
    from . import faq
    from . import legal

    legal.register(app)
    faq.register(app)
    developer.register(app)
    shop.register(app)
    auth.register(app)
    profile.register(app)
    api.register(app)
    static.register(app)
