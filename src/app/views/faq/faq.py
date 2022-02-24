#!usr/bin/python
"""
    Merchandise shop application FAQ views.
"""


from flask import Blueprint, url_for, render_template, redirect
from flask_login import current_user

from ...services.templates import templates_get_name_list
from ...error_handlers.raise_error import raise_error


bp_faq = Blueprint("faq", __name__)

# Reading allowed pages.
faq_pages = templates_get_name_list("faq", "pages")


@bp_faq.route("/faq", methods=["GET"])
def index():
    return render_template("faq/index.jinja", user=current_user)


@bp_faq.route("/faq/<name>", methods=["GET"])
def page(name):
    if name in faq_pages:
        return render_template(f"faq/pages/{name}.jinja", user=current_user)
    return raise_error(404, "FAQ page does not exists!")


@bp_faq.route("/help")
@bp_faq.route("/docs")
@bp_faq.route("/documentation")
def index_alias():
    return redirect(url_for("faq.index"))
