#!usr/bin/python
"""
    Merchandise shop application developer documentation views.
"""

from flask import Blueprint, redirect, url_for

bp_dev_docs = Blueprint("dev_docs", __name__)


@bp_dev_docs.route("/dev", methods=["GET"])
def index():
    return "TBD"


@bp_dev_docs.route("/developer")
@bp_dev_docs.route("/api")
def index_alias():
    return redirect(url_for("dev_docs.index"))
