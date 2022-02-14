#!usr/bin/python
"""
    Merchandise shop application FAQ views.
"""
from jinja2 import exceptions

from flask import Blueprint, url_for, render_template, redirect
from flask_login import current_user

from ...error_handlers.raise_error import raise_error


bp_faq = Blueprint("faq", __name__)


@bp_faq.route("/faq", methods=["GET"])
def index():
    return render_template("faq/index.jinja", user=current_user)


@bp_faq.route("/faq/<name>", methods=["GET"])
def page(name):
    try:
        # Is this is potential exploit?.
        return render_template(f"faq/{name}.jinja", user=current_user)
    except exceptions.TemplateNotFound:
        return raise_error(404, "FAQ page does not exists!")


@bp_faq.route("/help")
@bp_faq.route("/docs")
@bp_faq.route("/documentation")
def index_alias():
    return redirect(url_for("faq.index"))
