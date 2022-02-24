#!usr/bin/python
"""
    Merchandise shop application item views.
"""

from flask import Blueprint, send_from_directory, current_app

bp_static = Blueprint("ext_static", __name__)


@bp_static.route("/robots.txt")
def robots():
    """
    Handles static `robots.txt` file for search index.
    File should be located in the root, so this view does that.
    """
    return send_from_directory(current_app.static_folder, "robots.txt")


@bp_static.route("/sitemap.xml")
def sitemap():
    """
    Handles static `sitemap.xml` file for search index.
    File should be located in the root, so this view does that.
    """
    return send_from_directory(current_app.static_folder, "sitemap.xml")
