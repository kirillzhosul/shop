#!usr/bin/python
"""
    Merchandise shop application profile views.
"""

from flask import Blueprint, render_template
from flask_login import current_user, login_required


bp_profile = Blueprint("profile", __name__)


@bp_profile.route("/profile", methods=["GET"])
@login_required
def index() -> str:
    """Profile view page. Displays all current profile (account) information. """
    return render_template("profile/index.jinja", user=current_user)


@bp_profile.route("/cart", methods=["GET"])
@login_required
def cart() -> str:
    """Profile cart page. Displays all current profile (account) cart items. """
    return render_template("profile/cart.jinja",
                           user=current_user)


@bp_profile.route("/favorites", methods=["GET"])
@login_required
def favorites() -> str:
    """Profile favorites page. Displays all current profile (account) favorite items. """
    return render_template("profile/favorites.jinja",
                           user=current_user)


@bp_profile.route("/orders", methods=["GET"])
@login_required
def orders() -> str:
    """Profile orders page. Displays all current profile (account) orders. """
    return render_template("profile/orders.jinja",
                           user=current_user)
