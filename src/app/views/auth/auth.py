#!usr/bin/python
"""
    Merchandise shop application auth views.
"""

from flask import Blueprint, redirect, url_for
from flask_login import login_user
from ...models.user.user import User
from ... import db

bp_auth = Blueprint("auth", __name__)


@bp_auth.route("/auth", methods=["GET"])
def index():
    user = User("test", "test", "test")
    db.session.add(user)
    db.session.commit()

    login_user(user)
    return redirect(url_for("profile.index"))


@bp_auth.route("/auth/login", methods=["GET"])
def login():
    return "TBD"


@bp_auth.route("/auth/register", methods=["GET"])
def register():
    return "TBD"
