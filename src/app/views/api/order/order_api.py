#!usr/bin/python
"""
    Merchandise shop application order API views.
"""

from flask import Blueprint, request, jsonify, url_for
from flask_login import current_user

from ....models.order.order import Order
from ....models.order.order_status import OrderStatus

from .... import db


bp_api_order = Blueprint("api_order", __name__)


@bp_api_order.route("/api/order/pay", methods=["GET"])
def pay():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Авторизуйтесь для выполнения запроса!",
            "redirect_to": url_for("auth.login"),
            "auth_required": True
        }), 401
    order_id = request.args.get("order_id", type=int, default=0)
    order = Order.query.filter_by(id=order_id).first()
    if order_id == 0 or not order:
        return jsonify({
            "error": "Заказ с индексом order_id не найден!"
        }), 404

    order_price = order.get_price()
    if current_user.get_balance() < order_price:
        return jsonify({
            "error": f"Пополните баланс на {order_price - current_user.get_balance()}Р"
        }), 400

    current_user.pay(order_price)
    order.set_status(OrderStatus.CREATED)
    db.session.commit()

    return jsonify({
    }), 200

