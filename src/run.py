#!usr/bin/python
# Refactoring by SantaSpeen
# 23.02.2022
"""
    Merchandise shop application runner.
    Runs the Flask application.
"""

from typing import NoReturn

import app


# Settings.
CONFIG = app.config.ConfigDevelopment


def run_server() -> NoReturn:
    """
    Creates app and runs app with werkzeug server.
    """
    wsgi_app = app.create(cfg=CONFIG)
    wsgi_app.run(host=CONFIG.HOST, port=CONFIG.PORT)


# Entry point.
if __name__ == "__main__":
    run_server()
