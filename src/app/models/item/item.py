#!env/bin/python
"""
    Item model.
    Represents shop item.
"""

import datetime
from ... import db
from ..review.review import ReviewMark


class Item(db.Model):
    """
        Represents shop item.
    """
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    metainformation = db.Column(db.Text, nullable=False)  # JSON.

    price = db.Column(db.Numeric, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    date_created = db.Column(db.DateTime(timezone=False), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    discounts = db.relationship("Discount", backref="item")  # ON DELETE CASCADE
    images = db.relationship("ItemImage", backref="item")  # ON DELETE CASCADE
    reviews = db.relationship("Review", backref="item")  # ON DELETE CASCADE

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
        Returnrs price with all applied discounts.
        :return: Price with applied discounts.
        """
        percent = 0
        for discount in self.discounts:
            percent += discount.percent

        return self.price * (percent / 100)

    def get_scores(self):
        """
        Returns amount of bade and good reviews.
        :return: Tuple with amount of bad and good reviews.
        """
        bad_reviews = len([review for review in self.reviews if review.mark == ReviewMark.BAD])
        good_reviews = len([review for review in self.reviews if review.mark == ReviewMark.GOOD])
        return bad_reviews, good_reviews
