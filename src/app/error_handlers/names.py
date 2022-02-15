#!usr/bin/python
"""
    Merchandise shop handled error names.
"""

NAMES = {
    200: "OK",

    400: "BAD REQUEST",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    410: "Gone",
    418: "I'm a teapot",

    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
}

CODES = [
    401, 403, 404, 500, 418
]
