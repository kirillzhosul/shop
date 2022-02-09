#!usr/bin/python
"""
    Merchandise shop application auth views.
"""

from flask import Blueprint, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from ...models.user.user import User
from ... import db

bp_auth = Blueprint("auth", __name__)


@bp_auth.route("/auth", methods=["GET"])
def index():
    if not current_user.is_authenticated:
        user = User("test", "test", "test")
        db.session.add(user)
        db.session.commit()

        login_user(user)
    return redirect(url_for("profile.index"))


@bp_auth.route("/auth/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))
