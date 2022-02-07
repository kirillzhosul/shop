#!env/bin/python
"""
    Order model.
    Represents item order request.
"""

import datetime
from .order_delivery_type import OrderDeliveryType
from ... import db


class Order(db.Model):
    """
        Represents item order request.
    """
    id = db.Column(db.Integer, primary_key=True)

    delivery_type = db.Column(db.Integer, nullable=False)
    delivery_address = db.Column(db.Text, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    items = db.relationship("OrderItem", backref="order")  # ON DELETE CASCADE

    date_created = db.Column(db.DateTime(timezone=False), nullable=False)

    def __init__(self, customer_id: int, delivery_type: OrderDeliveryType, delivery_address):
        self.customer_id = customer_id

        self.delivery_type = delivery_type
        self.delivery_address = delivery_address

        self.date_created = datetime.datetime.now()

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
