#!usr/bin/python
"""
    Merchandise shop application auth views.
"""

from flask import Blueprint, redirect, url_for
from flask_login import logout_user

from ...services.auth import render_or_profile_if_not_guest


bp_auth = Blueprint("auth", __name__)


@bp_auth.route("/auth/", methods=["GET"])
def index():
    """Auth index page."""
    return render_or_profile_if_not_guest("auth/index.jinja")


@bp_auth.route("/auth/login", methods=["GET"])
def login():
    """Auth login page. """
    return render_or_profile_if_not_guest("auth/login.jinja")


@bp_auth.route("/auth/register", methods=["GET"])
def register():
    """Auth register page. """
    return render_or_profile_if_not_guest("auth/register.jinja")


@bp_auth.route("/auth/logout", methods=["GET"])
def logout():
    """Logout page. Will log out the user and redirect to auth page. """
    logout_user()
    return redirect(url_for("auth.index"))