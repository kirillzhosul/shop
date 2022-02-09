#!usr/bin/python
"""
    Merchandise shop application profile views.
"""

from flask import Blueprint, render_template
from flask_login import current_user, login_required
from ...models.item.item import Item

bp_profile = Blueprint("profile", __name__)


@bp_profile.route("/profile", methods=["GET"])
def index():
    return "TBD"


@bp_profile.route("/cart", methods=["GET"])
@login_required
def cart():
    cart_count = sum([cart_item.quantity for cart_item in current_user.cart_items])
    cart_price = sum([
        Item.query.filter_by(id=cart_item.item_id).first().get_price_with_discount()[0]
        for cart_item in current_user.cart_items
    ])

    return render_template("profile/cart.jinja",
                           user=current_user,
                           cart_count=cart_count,
                           cart_price=cart_price)


@bp_profile.route("/favorites", methods=["GET"])
def favorites():
    return "TBD"


@bp_profile.route("/orders", methods=["GET"])
def orders():
    return render_template("profile/orders.jinja",
                           user=current_user)
