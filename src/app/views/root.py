#!usr/bin/python
"""
    Merchandise shop application root views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user

from ..error_handlers.raise_error import raise_error


bp_root = Blueprint("root", __name__)


@bp_root.route("/", methods=["GET"])
def index():
    """Shop index page."""
    return render_template("root/index.jinja", user=current_user)


@bp_root.route("/about", methods=["GET"])
def about():
    """Shop about page."""
    return render_template("root/about.jinja", user=current_user)


@bp_root.route("/contacts", methods=["GET"])
def contacts():
    """Shop contacts page."""
    return render_template("root/contacts.jinja", user=current_user)


@bp_root.route("/error", methods=["GET"])
def error():
    """
    Shop error page, will raise error with code, given in `c` GET parameter.
    Should be not used for end-user, may be removed later or moved in other place.
    """
    code = request.args.get("c", type=int, default=400)
    return raise_error(code)
