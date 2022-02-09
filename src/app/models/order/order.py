#!env/bin/python
"""
    Order model.
    Represents item order request.
"""

import datetime
from .order_delivery_type import OrderDeliveryType
from .order_status import OrderStatus
from ... import db


class Order(db.Model):
    """
        Represents item order request.
    """
    id: int = db.Column(db.Integer, primary_key=True)

    status: int = db.Column(db.Integer, nullable=False)  # default -> see constructor.

    delivery_type: int = db.Column(db.Integer, nullable=False)
    delivery_address: str = db.Column(db.Text, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    items = db.relationship("OrderItem", backref="order")  # ON DELETE CASCADE

    date_created: datetime.datetime = db.Column(db.DateTime(timezone=False), nullable=False)

    def __init__(self, customer_id: int, delivery_type: OrderDeliveryType, delivery_address: str):
        self.status = OrderStatus.AWAITING_PAYMENT.value

        self.customer_id = customer_id

        self.delivery_type = delivery_type.value
        self.delivery_address = delivery_address

        self.date_created = datetime.datetime.now()

    def get_uid(self):
        return f"{self.customer_id}-{self.id}"

    def set_status(self, status: OrderStatus):
        self.status = status.value

    def get_status(self):
        return OrderStatus(self.status)

    def get_delivery_type(self):
        return OrderDeliveryType(self.delivery_type)

    def get_date_created(self):
        return self.date_created.strftime("%m.%d.%y %H:%M")

    def get_price(self):
        """
        Returns price of the all items in the order.
        :return: Sum of the items price.
        """
        return sum(order_item.price for order_item in self.items)

    def get_quantity(self):
        """
        Returns quantity of the items in the order.
        :return: Sum of the items quantity.
        """
        return sum(order_item.quantity for order_item in self.items)
