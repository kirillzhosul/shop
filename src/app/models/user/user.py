#!env/bin/python
"""
    User model.
    Represents shop user-customer.
"""

import datetime
from typing import Optional
from ... import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
        Represents shop user-customer.
    """
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=True)

    favorite_items = db.relationship("FavoriteItem", backref="owner")  # ON DELETE CASCADE
    cart_items = db.relationship("CartItem", backref="owner")  # ON DELETE CASCADE
    reviews = db.relationship("Review", backref="author")  # ON DELETE CASCADE
    orders = db.relationship("Order", backref="customer")  # ON DELETE CASCADE

    avatar_id = db.Column(db.Integer, db.ForeignKey("user_avatar.id"), nullable=True)

    date_created = db.Column(db.DateTime(timezone=False), nullable=False)

    def __init__(self, email: str, name: str, phone: Optional[str] = None):
        self.name = name
        self.email = email
        self.phone = phone

        self.date_created = datetime.datetime.now()

    def get_counters(self):
        counter_orders = len(self.orders)
        counter_cart = len(self.cart_items)
        counter_favorites = len(self.favorite_items)
        return counter_orders, counter_cart, counter_favorites
