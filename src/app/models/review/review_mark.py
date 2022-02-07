#!env/bin/python
"""
    Order review mark enumeration.
"""

from enum import Enum


class ReviewMark(Enum):
    """ Enumeration for review mark type. """
    GOOD = True
    BAD = False
