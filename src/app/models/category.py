#!env/bin/python
"""
    Category model.
    Represents item categories.
"""

from .. import db


class Category(db.Model):
    """
        Represents item categories.
    """
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)

    items = db.relationship("Item", backref="category")

    def __init__(self, title: str):
        self.title = title
