#!usr/bin/python
"""
    Merchandise shop application catalog views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user
from ...models.item.item import Item
from ...models.category import Category
from ... import db

bp_catalog = Blueprint("catalog", __name__)


@bp_catalog.route("/catalog", methods=["GET"])
def index():
    args_limit = request.args.get("l", type=int, default=9)
    args_offset = request.args.get("o", type=int, default=0)
    args_query = request.args.get("q", type=str, default="")
    args_category_id = request.args.get("cid", type=int, default=0)

    db_items, db_count = Item.search(args_query, args_category_id,
                                     args_limit, args_offset)
    db_category = Category.get_category_by_id(args_category_id)

    return render_template("catalog/index.jinja",
                           items=db_items, count=db_count,
                           category=db_category,
                           query=args_query,
                           user=current_user)


@bp_catalog.route("/categories", methods=["GET"])
def categories():
    args_limit = request.args.get("l", type=int, default=99)
    args_offset = request.args.get("o", type=int, default=0)

    db_items, db_count = Category.get_paginated(args_limit, args_offset)

    return render_template("catalog/categories.jinja",
                           categories=db_items,
                           count=db_count,
                           user=current_user)


@bp_catalog.route("/catalog/debug", methods=["GET"])
def debug():
    from random import randrange, choice
    for _ in range(30):
        category = Category(choice([
            "Кружка ",
            "Футболка ",
            "Рубашка ",
            "Худи ",
            "Блокнот ",
            "Ручка ",
            "Подарочный набор "
        ]))
        db.session.add(category)
        db.session.commit()
    for _ in range(30):
        # description =
        title = choice([
            "Кружка ",
            "Футболка ",
            "Рубашка ",
            "Худи ",
            "Блокнот ",
            "Ручка ",
            "Подарочный набор "
        ]) + "".join([chr(randrange(1072, 1103, 1)) for _ in range(5)])
        description = "".join([chr(randrange(1072, 1103, 1)) for _ in range(100)])

        item = Item(title, description, "{}", randrange(1, 9999, 1), randrange(1, 9999, 1), randrange(1, 30))
        db.session.add(item)
        db.session.commit()
    return "OK!"
