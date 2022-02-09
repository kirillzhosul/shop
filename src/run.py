#!usr/bin/python
"""
    Merchandise shop application runner.
    Runs the Flask application.
"""

import app

if __name__ == "__main__":
    wsgi_app = app.create(None, app.config.ConfigProduction)
    wsgi_app.run(host="0.0.0.0", port=80)
