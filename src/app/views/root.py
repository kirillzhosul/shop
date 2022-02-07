#!usr/bin/python
"""
    Merchandise shop application root views.
"""

from flask import Blueprint, render_template

bp_root = Blueprint("root", __name__)


@bp_root.route("/", methods=["GET"])
def root_index():
    return render_template("index.jinja")


@bp_root.route("/about", methods=["GET"])
def root_about():
    return render_template("about.jinja")


@bp_root.route("/contacts", methods=["GET"])
def root_contacts():
    return render_template("contacts.jinja")
