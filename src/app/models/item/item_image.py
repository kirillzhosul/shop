#!env/bin/python
"""
    Item image model.
    Represents image, used to collect albums inside product page.
"""

from ... import db


class ItemImage(db.Model):
    """
        Represents image, used to collect albums inside product page.
    """

    id = db.Column(db.Integer, primary_key=True)

    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)

    def __init__(self, link: str, item_id: int, description: str):
        self.link = link
        self.item_id = item_id
        self.description = description
