#!env/bin/python
"""
    Order delivery type enumeration.
"""

from enum import Enum, auto


class OrderDeliveryType(Enum):
    """ Enumeration for order delivery types. """
    BY_OWN = auto()
    COURIER = auto()
