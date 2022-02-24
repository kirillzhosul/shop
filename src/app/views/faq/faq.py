#!usr/bin/python
"""
    Merchandise shop application FAQ views.
"""

from flask import Blueprint, render_template
from flask_login import current_user

from ...services.templates import templates_get_name_list
from ...error_handlers.raise_error import raise_error


bp_faq = Blueprint("faq", __name__)

faq_pages = None  # Allowed pages for FAQ.


@bp_faq.route("/faq", methods=["GET"])
def index() -> str:
    """FAQ index page. """
    return render_template("faq/index.jinja", user=current_user)


@bp_faq.route("/faq/<name>", methods=["GET"])
def page(name) -> str:
    """
    FAQ page. Displays requested FAQ page, or 404 if page was not found.
    :param name: FAQ requested page.
    """

    # Reading allowed pages.
    global faq_pages
    if not faq_pages:
        faq_pages = templates_get_name_list("faq", "pages")

    if name not in faq_pages:
        return raise_error(404)

    return render_template(f"faq/pages/{name}.jinja", user=current_user)
