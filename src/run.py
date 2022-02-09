#!usr/bin/python
"""
    Merchandise shop application runner.
    Runs the Flask application.
"""

import app

if __name__ == "__main__":
    app.create().run(debug=True, host="0.0.0.0", port=80)
