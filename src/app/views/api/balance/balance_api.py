#!usr/bin/python
"""
    Merchandise shop application balance API views.
"""

from flask import Blueprint, Response
from flask_login import current_user

from ....services.api.errors import ApiErrorType
from ....services.api.wrappers import api_auth_required
from ....services.api.response import ApiResponse

bp_api_balance = Blueprint("api_balance", __name__)


@bp_api_balance.route("/api/balance/get", methods=["GET"])
@api_auth_required
def get() -> Response:
    """
    Balance API get method.
    Returns current user balance.
    """
    return ApiResponse.success({
        "balance": {
            "real": current_user.balance_bonus,
            "bonus": current_user.balance_real
        }
    })


@bp_api_balance.route("/api/balance/topup", methods=["GET"])
@api_auth_required
def topup():
    """
    Balance API topup method.
    Will top up user balance and return payment error as payment currently in test mode.
    """
    current_user.topup()
    return ApiResponse.error(ApiErrorType.PAYMENT_ERROR)
