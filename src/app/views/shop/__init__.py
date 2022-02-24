#!usr/bin/python
"""
    Merchandise shop application shop views.
"""

from typing import NoReturn
from flask import Flask

from . import (
    catalog,  # Catalog search.
    item      # Item view page.
)


def register(app: Flask) -> NoReturn:
    """
    Registers all views blueprints.
    :param: app Flask application.
    """
    app.register_blueprint(catalog.bp_catalog)
    app.register_blueprint(item.bp_item)
