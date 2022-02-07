#!env/bin/python
"""
    Review model.
    Represents item review from user.
"""

import datetime
from .review_mark import ReviewMark
from ... import db


class Review(db.Model):
    """
        Represents item review from user.
    """
    id = db.Column(db.Integer, primary_key=True)

    mark = db.Column(db.Boolean, nullable=False)
    text = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)

    date_created = db.Column(db.DateTime(timezone=False), nullable=False)

    attachments = db.relationship("ReviewImage", backref="review")  # ON DELETE CASCADE

    def __init__(self, text: str, mark: ReviewMark, item_id: int, author_id: int):
        self.text = text
        self.mark = mark

        self.item_id = item_id
        self.author_id = author_id

        self.date_created = datetime.datetime.now()
