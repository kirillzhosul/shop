#!env/bin/python
"""
    Review image model.
    Represents review attached images.
"""

from ... import db


class ReviewImage(db.Model):
    """
        Represents review attached images.
    """
    id = db.Column(db.Integer, primary_key=True)

    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    review_id = db.Column(db.Integer, db.ForeignKey("review.id"), nullable=False)

    def __init__(self, link: str, review_id: int, description: str):
        self.link = link
        self.review_id = review_id
        self.description = description
