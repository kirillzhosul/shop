#!usr/bin/python
"""
    Merchandise shop application developer documentation views.
"""

from flask import Blueprint, url_for, render_template, redirect
from flask_login import current_user

from ...services.templates import templates_get_name_list
from ...error_handlers.raise_error import raise_error


bp_dev_docs = Blueprint("dev_docs", __name__)

# Reading allowed pages.
dev_pages = templates_get_name_list("dev", "pages")


@bp_dev_docs.route("/dev", methods=["GET"])
def index():
    return render_template("dev/index.jinja", user=current_user)


@bp_dev_docs.route("/dev/<name>", methods=["GET"])
def page(name):
    if name in dev_pages:
        return render_template(f"dev/pages/{name}.jinja", user=current_user)
    return raise_error(404, "Developer documentation page does not exists!")


@bp_dev_docs.route("/developer")
@bp_dev_docs.route("/api")
def index_alias():
    return redirect(url_for("dev_docs.index"))
