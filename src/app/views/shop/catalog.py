#!usr/bin/python
"""
    Merchandise shop application root views.
"""

from flask import Blueprint, render_template, request
from ...models.item.item import Item
from ... import db
bp_catalog = Blueprint("catalog", __name__)


@bp_catalog.route("/catalog", methods=["GET"])
def catalog_index():
    args_limit = request.args.get("l")
    args_offset = request.args.get("o")
    args_query = request.args.get("q", type=str, default="")

    db_filter = Item.query.filter(Item.title.ilike(f"%{args_query}%"))
    db_items = db_filter.limit(args_limit).offset(args_offset).all()
    db_count = db_filter.count()

    return render_template("catalog/index.jinja",
                           items=db_items,
                           count=db_count,
                           query=args_query)

@bp_catalog.route("/fill", methods=["GET"])
def catalog_fill():
    from random import randrange
    for _ in range(30):
        title = "".join([chr(randrange(1072, 1103, 1)) for _ in range(30)])
        description = "".join([chr(randrange(1072, 1103, 1)) for _ in range(100)])

        item = Item(title, description, "{}", randrange(1, 9999, 1), randrange(1, 9999, 1), randrange(1, 4))
        db.session.add(item)
        db.session.commit()
    return "OK!"
