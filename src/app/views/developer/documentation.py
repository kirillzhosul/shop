#!usr/bin/python
"""
    Merchandise shop application developer documentation views.
"""

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from ...services.templates import templates_get_name_list
from ...error_handlers.raise_error import raise_error


bp_dev_docs = Blueprint("dev_docs", __name__)

dev_pages = None  # Allowed pages for developer documentation.


@bp_dev_docs.route("/faq", methods=["GET"])
def index() -> str:
    """Developer documentation index page. """
    return render_template("dev/index.jinja", user=current_user)


@bp_dev_docs.route("/faq/<name>", methods=["GET"])
def page(name) -> str:
    """
    Developer documentation page. Displays requested documentation page, or 404 if page was not found.
    :param name: Documentation requested page.
    """

    # Reading allowed pages.
    global dev_pages
    if not dev_pages:
        dev_pages = templates_get_name_list("dev", "pages")

    if name not in dev_pages:
        return raise_error(404)

    return render_template(f"dev/pages/{name}.jinja", user=current_user)


@bp_dev_docs.route("/developer")
@bp_dev_docs.route("/api")
def index_alias():
    """
    Name alias for documentation.
    (/api/ without reference to any method will redirect to index so end-user can read more about API)
    """
    return redirect(url_for("dev_docs.index"))


