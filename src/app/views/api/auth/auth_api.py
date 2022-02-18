#!usr/bin/python
"""
    Merchandise shop application favorites API views.
"""

from flask import Blueprint, request, jsonify, url_for
from flask_login import current_user, login_user, logout_user

from ....models.user.user import User

from .... import db


bp_api_auth = Blueprint("api_auth", __name__)


@bp_api_auth.route("/api/auth/login", methods=["GET"])
def login():
    if current_user.is_authenticated:
        return jsonify({
            "error": "Вы уже авторизованы, вам не требется авторизация!",
            "redirect_to": url_for("profile.index"),
            "auth_required": False
        }), 400

    # This method of handling auth is NOT very safe, but yes.
    email = request.args.get("email", type=str, default="")
    password = request.args.get("password", type=str, default="")

    if len(email) == 0 or len(password) == 0:
        return jsonify({
            "error": "Заполните все поля!"
        }), 400

    if not (user := User.query.filter_by(email=email).first()):
        return jsonify({
            "error": "Данные для входа не верны!"
        }), 400

    # Password check here TODO.

    login_user(user, remember=True,
               force=False, fresh=True)

    return jsonify({
        "user": {
            "id": user.id,
            "email": user.email
        },
        "redirect_to": url_for("profile.index")
    }), 200


@bp_api_auth.route("/api/auth/register", methods=["GET"])
def register():
    if current_user.is_authenticated:
        return jsonify({
            "error": "Вы уже авторизованы, вам не требется авторизация!",
            "redirect_to": url_for("profile.index"),
            "auth_required": False
        }), 400

    # This method of handling auth is NOT very safe, but yes.
    name = request.args.get("name", type=str, default="")
    phone = request.args.get("phone", type=str, default="")
    email = request.args.get("email", type=str, default="")

    password = request.args.get("password", type=str, default="")
    password_confirmation = request.args.get("password_confirmation", type=str, default="")

    reject_auto_login = request.args.get("reject_auto_login", type=bool, default=False)

    # TODO. REVIEW.
    if len(name) == 0 or len(phone) == 0 or len(email) == 0:
        return jsonify({"error": "Заполните поля "
                                 "`name`, `phone`, `email`, `password`, `password_confirmation` в запросе!"}), 400
    if len(name) <= 5 or len(phone) <= 5 or len(email) <= 5:
        return jsonify({"error": "Одно из полей запроса `name`, `phone`, `email` слишком короткое"}), 400
    if len(name) >= 254 or len(phone) >= 254 or len(email) >= 254:
        return jsonify({"error": "Одно из полей запроса `name`, `phone`, `email` слишком длинное"}), 400
    if len(password) <= 5:
        return jsonify({"error": "Пароль слишком короткий!"}), 400
    if password != password_confirmation:
        return jsonify({"error": "Пароль и подтверждение пароля не совпадает!"}), 400

    user = User(email, name, phone)
    db.session.add(user)
    db.session.commit()

    if not reject_auto_login:
        login_user(user, remember=True,
                   force=False, fresh=False)

    return jsonify({
        "user": {
            "id": user.id,
            "email": user.email,
            "name":  user.name,
            "phone":  user.phone
        },
        "already_login": not reject_auto_login,
        "redirect_to": url_for("auth.login" if reject_auto_login else "profile.index")
    }), 200


@bp_api_auth.route("/api/auth/logout", methods=["GET"])
def logout():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Вам не требуется выход!",
            "redirect_to": url_for("auth.index"),
            "auth_required": True
        }), 401

    logout_user()

    return jsonify({
        "redirect_to": url_for("auth.index")
    }), 200
