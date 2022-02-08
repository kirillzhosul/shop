#!env/bin/python
"""
    Order status enumeration.
"""

from enum import Enum, auto


class OrderStatus(Enum):
    """ Enumeration for order status. """

    # Before delivery.
    AWAITING_PAYMENT = auto()
    CREATED = auto()
    IN_PROGRESS = auto()

    # After delivery.
    SENT = auto()
    DELIVERED = auto()
    RECEIVED = auto()
    CANCELLED = auto()
