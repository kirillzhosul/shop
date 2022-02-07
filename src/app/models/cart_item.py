#!env/bin/python
"""
    Cart item model.
    Represents cart item.
"""

from .. import db


class CartItem(db.Model):
    """
       Represents cart item.
    """
    id = db.Column(db.Integer, primary_key=True)

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, item_id: int, owner_id):
        self.item_id = item_id
        self.owner_id = owner_id
