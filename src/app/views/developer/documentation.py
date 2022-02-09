#!usr/bin/python
"""
    Merchandise shop application developer documentation views.
"""

from flask import Blueprint, redirect, url_for

bp_dev_docs = Blueprint("dev_docs", __name__)


@bp_dev_docs.route("/dev", methods=["GET"])
def dev_docs_index():
    return "TBD"


@bp_dev_docs.route("/developer")
@bp_dev_docs.route("/api")
def dev_docs_redirect():
    return redirect(url_for("dev_docs.dev_docs_index"))
