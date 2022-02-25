#!usr/bin/python
"""
    Merchandise shop application auth API views.
"""
# TODO: Phone, mail, name validators.

from flask import Blueprint, request
from flask_login import logout_user, current_user

from ....services.api.wrappers import api_auth_dissallowed, api_auth_required
from ....services.api.response import ApiResponse
from ....services.api.errors import ApiErrorType
from ....services.auth import try_login_user
from ....models.user.user import User
from .... import db


bp_api_auth = Blueprint("api_auth", __name__)


@bp_api_auth.route("/api/auth/login", methods=["GET"])
@api_auth_dissallowed
def login():
    """API Login method, login you to the account using given credentials. """
    email = request.args.get("email", type=str, default="")
    password = request.args.get("password", type=str, default="")
    remember = request.args.get("remember", type=bool, default=True)

    if not email:
        return ApiResponse.error(ApiErrorType.FIELD_REQUIRED, field="email")

    if not password:
        return ApiResponse.error(ApiErrorType.FIELD_REQUIRED, field="password")

    if not try_login_user(email, password, remember):
        return ApiResponse.error(ApiErrorType.AUTH_FAILED)

    return ApiResponse.success({
        "user": {
            "id": current_user.id,
            "email": current_user.email
        },
    })


@bp_api_auth.route("/api/auth/register", methods=["GET"])
@api_auth_dissallowed
def register():
    """API register method. Register a new account and login in to it. """
    name = request.args.get("name", type=str, default="")
    phone = request.args.get("phone", type=str, default="")
    email = request.args.get("email", type=str, default="")

    password = request.args.get("password", type=str, default="")
    password_confirmation = request.args.get("password_confirmation", type=str, default="")

    if len(name) <= 5:
        return ApiResponse.error(ApiErrorType.FIELD_TOO_SHORT, field="name")
    if len(phone) <= 5:
        return ApiResponse.error(ApiErrorType.FIELD_TOO_SHORT, field="phone")
    if len(email) <= 5:
        return ApiResponse.error(ApiErrorType.FIELD_TOO_SHORT, field="email")
    if len(password) <= 5:
        return ApiResponse.error(ApiErrorType.FIELD_TOO_SHORT, field="password")

    if len(name) >= 254:
        return ApiResponse.error(ApiErrorType.FIELD_TOO_LONG, field="name")
    if len(phone) >= 254:
        return ApiResponse.error(ApiErrorType.FIELD_TOO_LONG, field="phone")
    if len(email) >= 254:
        return ApiResponse.error(ApiErrorType.FIELD_TOO_LONG, field="email")

    if password != password_confirmation:
        return ApiResponse.error(ApiErrorType.AUTH_PASSWORD_CONFIRMATION_MISMATCH)

    if User.exists(email):
        return ApiResponse.error(ApiErrorType.AUTH_ALREADY_EXISTS)

    user = User(email, name, password, phone if phone else None)
    db.session.add(user)
    db.session.commit()

    if not try_login_user(email, password, True):
        return ApiResponse.error(ApiErrorType.AUTH_FAILED)

    return ApiResponse.success({
        "user": {
            "id": user.id,
            "email": user.email,
            "name":  user.name,
            "phone":  user.phone
        },
    })


@bp_api_auth.route("/api/auth/logout", methods=["GET"])
@api_auth_required
def logout():
    """API logout method, logs user ot of the profile. """
    logout_user()
    return ApiResponse.success({})
