#!usr/bin/python
"""
    Merchandise shop application balance API views.
"""

from flask import Blueprint, jsonify
from flask_login import current_user

from ....services.api.wrappers import api_auth_required
from .... import db


bp_api_balance = Blueprint("api_balance", __name__)


@bp_api_balance.route("/api/balance/get", methods=["GET"])
@api_auth_required
def get():
    return jsonify({
        "real": current_user.balance_bonus,
        "bonus": current_user.balance_real
    }), 200


@bp_api_balance.route("/api/balance/topup", methods=["GET"])
@api_auth_required
def topup():
    current_user.balance_bonus += 500
    current_user.balance_real += 1250
    db.session.commit()

    return jsonify({
        "payment_service_url": "",
        "error": "Баланс пополнен на 1250Р и 500БР. Тестовый режим оплаты"
    }), 200
