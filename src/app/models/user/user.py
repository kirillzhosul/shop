#!env/bin/python
"""
    User model.
    Represents shop user-customer.
"""

import datetime
from typing import Optional

from flask_login import UserMixin
from werkzeug.security import (
    generate_password_hash, check_password_hash
)

from ...models.item.item import Item
from ... import db


class User(db.Model, UserMixin):
    """
        Represents shop user-customer.
    """
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=True)

    password = db.Column(db.String(80))

    balance_real = db.Column(db.Integer, default=0, nullable=False)
    balance_bonus = db.Column(db.Integer, default=0, nullable=False)

    favorite_items = db.relationship("FavoriteItem", backref="owner")  # ON DELETE CASCADE
    cart_items = db.relationship("CartItem", backref="owner")  # ON DELETE CASCADE
    reviews = db.relationship("Review", backref="author")  # ON DELETE CASCADE
    orders = db.relationship("Order", backref="customer")  # ON DELETE CASCADE

    avatar_id = db.Column(db.Integer, db.ForeignKey("user_avatar.id"), nullable=True)

    date_created = db.Column(db.DateTime(timezone=False), nullable=False)

    def __init__(self, email: str, name: str, password: str, phone: Optional[str] = None):
        self.name = name
        self.email = email
        self.phone = phone

        self.password = generate_password_hash(password)

        self.date_created = datetime.datetime.now()

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def get_balance(self):
        return self.balance_real + self.balance_bonus

    def pay(self, price: int):
        if price > self.balance_bonus:
            price -= self.balance_bonus
            self.balance_bonus = 0
        else:
            self.balance_bonus -= price
            return

        if price > self.balance_real:
            price -= self.balance_real
            self.balance_real = 0
        else:
            self.balance_real -= price
            return

    def get_cart(self):
        cart_count = sum([cart_item.quantity for cart_item in self.cart_items])
        cart_price = sum([
            Item.query.filter_by(id=cart_item.item_id).first().get_price_with_discount()[0]
            for cart_item in self.cart_items
        ])

        return cart_price, cart_count

    def get_counters(self):
        counter_orders = len(self.orders)
        counter_cart = (
            len(self.cart_items),
            sum([cart_item.item.get_price_with_discount()[0] for cart_item in self.cart_items])
        )
        counter_favorites = len(self.favorite_items)

        return counter_orders, counter_cart, counter_favorites
