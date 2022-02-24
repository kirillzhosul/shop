#!usr/bin/python
"""
    Merchandise shop application item views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user

from ...models.item.item import Item


bp_item = Blueprint("item", __name__)


@bp_item.route("/item", methods=["GET"])
def index() -> str:
    """
    Item view page. Displays item page, or raises 404 if item not found.
    """
    item_id = request.args.get("id", type=int, default=0)
    item = Item.get_by_id_or_404(item_id)

    return render_template("catalog/item.jinja",
                           item=item, user=current_user)
