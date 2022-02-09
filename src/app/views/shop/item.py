#!usr/bin/python
"""
    Merchandise shop application item views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user
from ...models.item.item import Item

bp_item = Blueprint("item", __name__)


@bp_item.route("/item", methods=["GET"])
def index():
    args_id = request.args.get("id", type=int, default=0)

    db_item = Item.query.filter_by(id=args_id).first_or_404()

    return render_template("catalog/item.jinja",
                           item=db_item,
                           user=current_user)
