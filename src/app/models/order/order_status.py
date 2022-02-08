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

    def __str__(self):
        return ORDER_STATUS_TO_STR[self]

    def get_color(self):
        return ORDER_STATUS_TO_COLOR[self]

    def is_awaiting_payment(self):
        return self == OrderStatus.AWAITING_PAYMENT

    def is_awaiting_receiving(self):
        return self == OrderStatus.DELIVERED


ORDER_STATUS_TO_STR = {
    OrderStatus.AWAITING_PAYMENT: "Ожидает оплаты",
    OrderStatus.CREATED: "Создан",
    OrderStatus.IN_PROGRESS: "В работе",

    OrderStatus.SENT: "Отправлен",
    OrderStatus.DELIVERED: "Доставлен",
    OrderStatus.RECEIVED: "Получен",
    OrderStatus.CANCELLED: "Отменён",
}

ORDER_STATUS_TO_COLOR = {
    OrderStatus.AWAITING_PAYMENT: "warning",
    OrderStatus.CREATED: "primary",
    OrderStatus.IN_PROGRESS: "primary",

    OrderStatus.SENT: "primary",
    OrderStatus.DELIVERED: "danger",
    OrderStatus.RECEIVED: "dark",
    OrderStatus.CANCELLED: "dark",
}
