#!usr/bin/python
"""
    Merchandise shop application profile views.
"""

from flask import Blueprint


bp_profile = Blueprint("profile", __name__)


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
