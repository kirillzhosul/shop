#!usr/bin/python
"""
    Merchandise shop application handled error names.
"""

# All names of errors for user.
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

# This is registered codes,
# all codes in that list will be register with handler.
CODES = [
    401, 403, 404, 500, 418
]
