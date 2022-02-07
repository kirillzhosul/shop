#!usr/bin/python
"""
    Merchandise shop application auth views.
"""

from flask import Blueprint
from flask_login import login_user
from ...models.user.user import User
from ... import db

bp_auth = Blueprint("auth", __name__)


@bp_auth.route("/auth/debug", methods=["GET"])
def auth_debug():
    user = User("test", "test", "test")
    db.session.add(user)
    db.session.commit()

    login_user(user)
    return "OK!"


@bp_auth.route("/auth", methods=["GET"])
def auth_index():
    return "TBD"


@bp_auth.route("/auth/login", methods=["GET"])
def auth_login():
    return "TBD"


@bp_auth.route("/auth/register", methods=["GET"])
def auth_register():
    return "TBD"
