#!usr/bin/python
"""
    Merchandise shop application API health views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user
from ... import db

bp_api_health = Blueprint("api_health", __name__)


def get_db_health_status():
    try:
        return db.session.execute("SELECT 2 + 2 * 3").first()[0] == 8
    except Exception:
        return False


@bp_api_health.route("/health/api", methods=["GET", "POST"])
def index():
    db_status = get_db_health_status()
    return render_template("health/api.jinja", db_status=db_status, addr=request.remote_addr, user=current_user)
