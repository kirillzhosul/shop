#!usr/bin/python
"""
    Merchandise shop application profile views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user, login_user
from ...models.user.user import User
from ... import db

bp_profile = Blueprint("profile", __name__)


@bp_profile.route("/debug/auth", methods=["GET"])
def debug_auth():
    user = User("test", "test", "test")
    db.session.add(user)
    db.session.commit()

    login_user(user)
    return "OK!"


@bp_profile.route("/profile", methods=["GET"])
def profile_index():
    return "TBD"


@bp_profile.route("/cart", methods=["GET"])
def profile_cart():
    return "TBD"


@bp_profile.route("/favorites", methods=["GET"])
def profile_favorites():
    return "TBD"


@bp_profile.route("/orders", methods=["GET"])
def profile_orders():
    return "TBD"
