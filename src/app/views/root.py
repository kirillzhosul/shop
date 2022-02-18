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
    return render_template("root/index.jinja", user=current_user)


@bp_root.route("/about", methods=["GET"])
def about():
    return render_template("root/about.jinja", user=current_user)


@bp_root.route("/contacts", methods=["GET"])
def contacts():
    return render_template("root/contacts.jinja", user=current_user)


@bp_root.route("/error", methods=["GET"])
def error():
    code = request.args.get("c", type=int, default=404)
    return raise_error(code)
