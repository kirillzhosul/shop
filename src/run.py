#!usr/bin/python
"""
    Merchandise shop application runner.
    Runs the Flask application.
"""

import app

# Settings.
HOST = "0.0.0.0"
PORT = 80
CONFIG = app.config.ConfigDevelopment

if __name__ == "__main__":
    wsgi_app = app.create(None, CONFIG)
    wsgi_app.run(host=HOST, port=PORT)
