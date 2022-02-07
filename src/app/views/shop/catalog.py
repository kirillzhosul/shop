#!usr/bin/python
"""
    Merchandise shop application root views.
"""

from flask import Blueprint, render_template, request
from ...models.item.item import Item
bp_catalog = Blueprint("catalog", __name__)


@bp_catalog.route("/catalog", methods=["GET"])
def catalog_index():
    limit = request.args.get("l")
    offset = request.args.get("o")
    query = request.args.get("q", type=str, default="")

    query = "%{}%".format(query)
    items = Item.query.filter(Item.title.ilike(query)).limit(limit).offset(offset).all()

    return render_template("catalog/index.jinja", items=items)
