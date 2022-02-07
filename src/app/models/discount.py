#!env/bin/python
"""
    Discount model.
    Represents item discount.
"""

import datetime
from .. import db


class Discount(db.Model):
    """
        Represents item discount.
    """
    id = db.Column(db.Integer, primary_key=True)

    percent = db.Column(db.Integer, nullable=False)

    date_created = db.Column(db.DateTime(timezone=False), nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)

    def __init__(self, percent, item_id):
        self.percent = percent

        self.item_id = item_id

        self.date_created = datetime.datetime.now()
