#!usr/bin/python
"""
    Merchandise shop application balance API views.
"""

from flask import Blueprint, jsonify, url_for
from flask_login import current_user

from .... import db


bp_api_balance = Blueprint("api_balance", __name__)


@bp_api_balance.route("/api/balance/get", methods=["GET"])
def get():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Авторизуйтесь для выполнения запроса!",
            "redirect_to": url_for("auth.login"),
            "auth_required": True
        }), 401
    return jsonify({
        "real": current_user.balance_bonus,
        "bonus": current_user.balance_real
    }), 200


@bp_api_balance.route("/api/balance/topup", methods=["GET"])
def topup():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Авторизуйтесь для выполнения запроса!",
            "redirect_to": url_for("auth.login"),
            "auth_required": True
        }), 401

    current_user.balance_bonus += 500
    current_user.balance_real += 1250
    db.session.commit()

    return jsonify({
        "payment_service_url": "https://localhost/payment_service",
        "error": "Баланс пополнен на 1250Р и 500БР. Тестовый режим оплаты"
    }), 200
