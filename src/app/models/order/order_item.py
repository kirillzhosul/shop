#!env/bin/python
"""
    Order item model.
    Represents order item itself.
"""

from ... import db
from ..item.item import Item


class OrderItem(db.Model):
    """
        Represents order item itself.
    """
    id = db.Column(db.Integer, primary_key=True)

    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)

    def __init__(self, order_id: int, item: Item, quantity: int):
        self.order_id = order_id
        self.item_id = item.id

        self.price, _ = item.get_price_with_discount() * quantity
        self.quantity = quantity
