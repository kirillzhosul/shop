#!env/bin/python
"""
    Category model.
    Represents item categories.
"""

from typing import Optional

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

    @staticmethod
    def get_category_by_id(category_id: int) -> Optional["Category"]:
        """
        Returns category with that ID or None if was not found.
        :param category_id:
        :return:
        """
        if category_id == 0 or category_id is None:
            return None
        return Category.query.filter_by(id=category_id).first()

    @staticmethod
    def get_paginated(limit: int, offset: int):
        db_filter = Category.query.limit(limit).offset(offset)
        db_items = db_filter.all()
        db_count = db_filter.count()

        return db_items, db_count
