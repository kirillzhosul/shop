#!usr/bin/python
"""
    Merchandise shop application developer documentation views.
"""
from jinja2 import exceptions

from flask import Blueprint, url_for, render_template, redirect
from flask_login import current_user

from ...error_handlers.raise_error import raise_error


bp_dev_docs = Blueprint("dev_docs", __name__)


@bp_dev_docs.route("/dev", methods=["GET"])
def index():
    return render_template("dev/index.jinja", user=current_user)


@bp_dev_docs.route("/dev/<name>", methods=["GET"])
def page(name):
    try:
        # Is this is potential exploit?.
        return render_template(f"dev/{name}.jinja", user=current_user)
    except exceptions.TemplateNotFound:
        return raise_error(404, "Developer documentation page does not exists!")


@bp_dev_docs.route("/developer")
@bp_dev_docs.route("/api")
def index_alias():
    return redirect(url_for("dev_docs.index"))
