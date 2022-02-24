#!usr/bin/python
"""
    Merchandise shop application item views.
"""

from flask import Blueprint, send_from_directory, current_app

bp_static = Blueprint("ext_static", __name__)


@bp_static.route("/robots.txt")
def robots():
    return send_from_directory(current_app.static_folder, "robots.txt")


@bp_static.route("/sitemap.xml")
def sitemap():
    return send_from_directory(current_app.static_folder, "sitemap.xml")


@bp_static.route("/favicon.ico")
def favicon():
    return send_from_directory(current_app.static_folder, "favicon.svg")

