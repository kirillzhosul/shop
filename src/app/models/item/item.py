#!env/bin/python
"""
    Item model.
    Represents shop item.
"""

from typing import Union, Tuple, List

import datetime

from ..review.review import ReviewMark
from ..category import Category

from ... import db


class Item(db.Model):
    """
        Represents shop item.
    """
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    metainformation = db.Column(db.Text, nullable=False)  # JSON.

    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    date_created = db.Column(db.DateTime(timezone=False), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    discounts = db.relationship("Discount", backref="item")  # ON DELETE CASCADE
    images = db.relationship("ItemImage", backref="item")  # ON DELETE CASCADE
    reviews = db.relationship("Review", backref="item")  # ON DELETE CASCADE

    cart_items = db.relationship("CartItem", backref="item")  # ON DELETE CASCADE
    favorite_items = db.relationship("FavoriteItem", backref="item")  # ON DELETE CASCADE
    order_items = db.relationship("OrderItem", backref="item")  # ON DELETE CASCADE

    def __init__(self, title: str, description: str, metainformation: str, price: float, quantity: int, category_id: int):
        self.title = title
        self.description = description
        self.metainformation = metainformation

        self.price = price
        self.quantity = quantity
        self.category_id = category_id

        self.date_created = datetime.datetime.now()

    def get_price_with_discount(self):
        """
        Returns price with all applied discounts and overall percent.
        :return: Price with applied discounts and percent.
        """
        percent = 0
        for discount in self.discounts:
            percent += discount.percent

        if percent <= 0:
            return self.price, percent

        price_with_discount = self.price - int(self.price * (percent / 100))
        return price_with_discount, percent, self.price

    def get_scores(self):
        """
        Returns amount of bad, good and all reviews.
        :return: Tuple with amount of bad, good and total reviews.
        """
        all_reviews = len([review for review in self.reviews])
        bad_reviews = len([review for review in self.reviews if review.mark == ReviewMark.BAD])
        good_reviews = len([review for review in self.reviews if review.mark == ReviewMark.GOOD])

        return bad_reviews, good_reviews, all_reviews

    def get_category_title(self) -> str:
        """
        Returns current item category title.
        :return: Own category title.
        """
        return Category.query.filter_by(id=self.category_id).first().title

    @staticmethod
    def search(query: str, category_id: int, limit: int, offset: int) -> Tuple[List, int]:
        """
        Returns all items with given search query.
        :param query: String with query.
        :param category_id: ID of the category, or 0 if it should be skipped.
        :param limit: Database load limit.
        :param offset: Database offset to load.
        :return: Tuple with items list and items count.
        """
        db_filter = Item.query.filter(Item.title.ilike(f"%{query}%"))
        if category_id != 0:
            db_filter = db_filter.filter_by(category_id=category_id)

        db_items = db_filter.limit(limit).offset(offset).all()
        db_count = db_filter.count()

        return db_items, db_count

    @staticmethod
    def get_by_id(item_id: int) -> Union["Item", None]:
        """
        Returns item or None if not found.
        :param item_id: ID of the item.
        :return: Item  object or None if was not found.
        """
        if item_id == 0 or item_id is None:
            return None

        return Item.query.filter_by(id=item_id).first() or None

    @staticmethod
    def get_by_id_or_404(item_id: int) -> "Item":
        """
        Returns item or raises 404 if not found.
        :param item_id: ID of the item.
        :return: Item object.
        """
        return Item.query.filter_by(id=item_id).first_or_404()