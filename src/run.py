#!usr/bin/python
"""
    Merchandise shop application runner.
    Runs the Flask application.
"""

import app

# Settings.
CONFIG = app.config.ConfigDevelopment

if __name__ == "__main__":
    wsgi_app = app.create(None, CONFIG)
    wsgi_app.run(host=CONFIG.HOST, port=CONFIG.PORT)
