#!env/bin/python
"""
    User avatar model.
    Represents image, used as user avatar.
"""

from ... import db


class UserAvatar(db.Model):
    """
        Represents image, used as user avatar.
    """

    id = db.Column(db.Integer, primary_key=True)

    link = db.Column(db.String(255), nullable=False)

    def __init__(self, link: str):
        self.link = link
