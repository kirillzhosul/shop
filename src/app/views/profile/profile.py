#!usr/bin/python
"""
    Merchandise shop application profile views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from ...error_handlers.raise_error import raise_error

from ...models.item.item import Item
from ...models.user.user import User

bp_profile = Blueprint("profile", __name__)


@bp_profile.route("/profile", methods=["GET"])
@login_required
def index():
    user = None
    user_id = request.args.get("id", type=int, default=0)
    if user_id != 0:
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return raise_error(404, "Профиль пользователя с данным id не найден!")
        return raise_error(403, "На данный момент нет возможности просмотра чужих профилей!")

    if user is None:
        user = current_user

    return render_template("profile/index.jinja", user=user)


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


@bp_profile.route("/orders", methods=["GET"])
@login_required
def orders():
    return render_template("profile/orders.jinja",
                           user=current_user)
