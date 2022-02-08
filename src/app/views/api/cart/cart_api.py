#!usr/bin/python
"""
    Merchandise shop application cart API views.
"""

from flask import Blueprint, request, jsonify
from flask_login import current_user
from ....models.cart_item import CartItem
from ....models.item import Item
from .... import db

bp_api_cart = Blueprint("api_cart", __name__)

# TODO: Cart item quantity.


@bp_api_cart.route("/api/cart/add", methods=["GET"])
def api_cart_add():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Not authenticated!"
        }), 401

    item_id = request.args.get("item_id", type=int, default=0)
    if item_id == 0 or not Item.query.filter_by(id=item_id).first():
        return jsonify({
            "error": "Item with given item_id does not exist!"
        }), 404
    cart_item = CartItem(item_id, current_user.id)

    db.session.add(cart_item)
    db.session.commit()

    return jsonify({}), 200


@bp_api_cart.route("/api/cart/get", methods=["GET"])
def api_cart_get():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Not authenticated!"
        }), 401

    db_cart_items = CartItem.query.filter_by(owner_id=current_user.id).all()
    cart_price = sum([
        Item.query.filter_by(id=cart_item.item_id).first().price
        for cart_item in db_cart_items
    ])
    cart_items = [
        {
            "item_id": cart_item.item_id
        } for cart_item in db_cart_items
    ]

    return jsonify({
        "cart_items": cart_items,
        "total_price": cart_price,
        "total_count": len(cart_items)
    }), 200
