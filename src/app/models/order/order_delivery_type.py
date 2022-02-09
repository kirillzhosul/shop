#!env/bin/python
"""
    Order delivery type enumeration.
"""

from enum import Enum, auto


class OrderDeliveryType(Enum):
    """ Enumeration for order delivery types. """
    BY_OWN = auto()
    COURIER = auto()

    def __str__(self):
        return ORDER_DELIVERY_TYPE_TO_STR[self]


ORDER_DELIVERY_TYPE_TO_STR = {
    OrderDeliveryType.BY_OWN: "Самовывоз",
    OrderDeliveryType.COURIER: "Курьером",
}
