#!usr/bin/python
"""
    Merchandise shop application legal views.
"""

from flask import Blueprint, render_template
from flask_login import current_user

bp_legal = Blueprint("legal", __name__)


@bp_legal.route("/legal/privacy", methods=["GET"])
def privacy():
    return render_template("legal/privacy.jinja", user=current_user)


@bp_legal.route("/legal/agreement", methods=["GET"])
def agreement():
    return render_template("legal/agreement.jinja", user=current_user)
