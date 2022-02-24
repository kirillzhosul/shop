#!usr/bin/python
"""
    Merchandise shop application catalog views.
"""

from flask import Blueprint, render_template, request, redirect, url_for, Response
from flask_login import current_user

from ...models.item.item import Item
from ...models.category import Category

from ... import db


bp_catalog = Blueprint("catalog", __name__)


@bp_catalog.route("/catalog", methods=["GET"])
def index() -> str:
    """Catalog index page. Displays catalog with list of items. """
    limit = request.args.get("l", type=int, default=9)
    offset = request.args.get("o", type=int, default=0)
    query = request.args.get("q", type=str, default="")
    category_id = request.args.get("cid", type=int, default=0)

    items, count = Item.search(query, category_id, limit, offset)
    category = Category.get_by_id(category_id)

    return render_template("catalog/index.jinja",
                           items=items, count=count,
                           category=category, query=query,
                           user=current_user)


@bp_catalog.route("/categories", methods=["GET"])
def categories() -> str:
    """Categories view page. Displays list of all categories."""
    limit = request.args.get("l", type=int, default=30)
    offset = request.args.get("o", type=int, default=0)

    items, count = Category.get_paginated(limit, offset)

    return render_template("catalog/categories.jinja",
                           categories=items, count=count,
                           user=current_user)


@bp_catalog.route("/catalog/debug", methods=["GET"])
def debug() -> Response:
    """
    Debug view, should be removed later.
    Fills catalog with random debug information / items.
    :return:
    """
    from random import randrange, choice
    from ...models.discount import Discount

    n = 30
    _random_names = [
        "Кружка ", "Футболка ",
        "Рубашка ", "Худи ",
        "Блокнот ", "Ручка ",
        "Подарочный набор "
    ]

    for _ in range(n):
        db.session.add(Category(choice(_random_names)))
    db.session.commit()

    for _ in range(n):
        title = choice(_random_names) + "".join([chr(randrange(1072, 1103, 1)) for _ in range(5)])
        description = "".join([chr(randrange(1072, 1103, 1)) for _ in range(100)])

        item = Item(title, description, "{}", randrange(1, 9999, 1), randrange(1, 9999, 1), randrange(1, 30))
        db.session.add(item)
        db.session.commit()

        if choice([True, False]):
            db.session.add(Discount(randrange(5, 95, 1), item.id))
    db.session.commit()

    return redirect(url_for("catalog.index"))
