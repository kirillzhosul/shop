#!usr/bin/python
"""
    Merchandise shop application cart API views.
"""

from flask import Blueprint, request, jsonify
from flask_login import current_user
from ....decorators import login_required
from ....models.cart_item import CartItem
from ....models.item import Item
from .... import db

bp_api_cart = Blueprint("api_cart", __name__)


@login_required(always_json=True)
@bp_api_cart.route("/api/cart/add", methods=["GET"])
def api_cart_add():
    item_id = request.args.get("item_id", type=int, default=0)
    item = Item.query.filter_by(id=item_id).first()
    if item_id == 0 or not item:
        return jsonify({
            "error": "Товар с индексом item_id не найден в каталоге!"
        }), 404
    cart_item = CartItem(item_id, current_user.id)

    item_quantity = request.args.get("quantity", type=int, default=1)
    if item_quantity != 1:
        if item_quantity < 0:
            return jsonify({
                "error": "item_quantity должен быть больше 0!"
            }), 400
        if item_quantity > item.quantity:
            return jsonify({
                "error": "item_quantity не должен превышать кол-во товара на складе!",
                "requested_quantity": item_quantity,
                "avaliable_quantity": item.quantity
            }), 400
        cart_item.quantity = item_quantity

    db.session.add(cart_item)
    db.session.commit()

    return jsonify({
        "cart_item_id": cart_item.id
    }), 200


@login_required(always_json=True)
@bp_api_cart.route("/api/cart/get", methods=["GET"])
def api_cart_get():
    cart_count = sum([cart_item.quantity for cart_item in current_user.cart_items])
    cart_price = sum([
        Item.query.filter_by(id=cart_item.item_id).first().get_price_with_discount()[0]
        for cart_item in current_user.cart_items
    ])

    cart_items = [
        {
            "cart_item_id": cart_item.id,
            "item_id": cart_item.item_id,
            "quantity": cart_item.quantity
        } for cart_item in current_user.cart_items
    ]

    return jsonify({
        "cart_items": cart_items,
        "total_price": cart_price,
        "total_count": cart_count
    }), 200


@login_required(always_json=True)
@bp_api_cart.route("/api/cart/remove", methods=["GET"])
def api_cart_remove():
    cart_item_id = request.args.get("cart_item_id", type=int, default=0)
    cart_item = CartItem.query.filter_by(id=cart_item_id).first()
    if not cart_item:
        return jsonify({
            "error": "Товар с индексом cart_item_id не найден в корзине"
        }), 404
    if cart_item.owner_id != current_user.id:
        return jsonify({
            "error": "Товар который вы пытаетесь удалить, находиться не в вашей корзине!"
        }), 403

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({
    }), 200

# TODO Quantity cart API.
