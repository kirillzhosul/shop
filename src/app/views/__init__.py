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

    # Importing lower (next) level views.
    # Should be here as references some things.
    from . import (
        shop,  # Catalog etc.
        auth, profile,  # Accounts.
        api,  # API.
        developer, faq,  # Developer.
        static, legal, root  # Other and static.
    )  # pylint: disable=import-outside-toplevel, unused-import

    # Blueprints.
    app.register_blueprint(root.bp_root)

    # Passing to next register functions.
    view_modules = (
        shop, auth, profile, api,
        faq, static, legal, developer
    )
    for module in view_modules:
        module.register(app)
