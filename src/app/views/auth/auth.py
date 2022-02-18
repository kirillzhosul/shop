#!usr/bin/python
"""
    Merchandise shop application auth views.
"""

from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required, current_user
from ...models.user.user import User
from ... import db

bp_auth = Blueprint("auth", __name__)


@bp_auth.route("/auth/", methods=["GET"])
def index():
    return render_template("auth/index.jinja", user=current_user)


@bp_auth.route("/auth/login", methods=["GET"])
def login():
    return render_template("auth/login.jinja", user=current_user)


@bp_auth.route("/auth/register", methods=["GET"])
def register():
    return render_template("auth/register.jinja", user=current_user)


@bp_auth.route("/auth/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))
