#!env/bin/python
"""
    Item model.
    Represents shop item.
"""

import datetime
from ... import db
from ..review.review import ReviewMark
from ..category import Category


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

        price_with_discount = int(self.price * (percent / 100))
        return price_with_discount, percent

    def get_scores(self):
        """
        Returns amount of bad, good and all reviews.
        :return: Tuple with amount of bad, good and total reviews.
        """
        all_reviews = len([review for review in self.reviews])
        bad_reviews = len([review for review in self.reviews if review.mark == ReviewMark.BAD])
        good_reviews = len([review for review in self.reviews if review.mark == ReviewMark.GOOD])

        return bad_reviews, good_reviews, all_reviews

    def get_category_title(self):
        return Category.query.filter_by(id=self.category_id).first().title

    def get_icon(self):
        pass
