#!usr/bin/python
"""
    Merchandise shop application root views.
"""

from flask import Blueprint

bp_root = Blueprint("root", __name__)


@bp_root.route("/", methods=["GET"])
def root_index():
    return "Merchandise shop application."
