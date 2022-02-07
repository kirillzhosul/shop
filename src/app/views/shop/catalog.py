#!usr/bin/python
"""
    Merchandise shop application root views.
"""

from flask import Blueprint, render_template, request
from flask_login import current_user, login_user
from ...models.item.item import Item
from ...models.user.user import User
from ...models.category import Category
from ... import db

bp_catalog = Blueprint("catalog", __name__)


@bp_catalog.route("/catalog", methods=["GET"])
def catalog_index():
    args_limit = request.args.get("l", type=int, default=9)
    args_offset = request.args.get("o", type=int, default=0)
    args_query = request.args.get("q", type=str, default="")
    args_category_id = request.args.get("cid", type=int, default=0)

    db_filter = Item.query.filter(Item.title.ilike(f"%{args_query}%"))
    if args_category_id != 0:
        db_filter = db_filter.filter_by(category_id=args_category_id)

    db_items = db_filter.limit(args_limit).offset(args_offset).all()
    db_count = db_filter.count()

    category = None if args_category_id == 0 else Category.query.filter_by(id=args_category_id).first()
    return render_template("catalog/index.jinja",
                           items=db_items,
                           count=db_count,
                           query=args_query,
                           category=category,
                           user=current_user)


@bp_catalog.route("/categories", methods=["GET"])
def catalog_categories():
    args_limit = request.args.get("l", type=int, default=99)
    args_offset = request.args.get("o", type=int, default=0)

    db_filter = Category.query.limit(args_limit).offset(args_offset)
    db_items = db_filter.all()
    db_count = db_filter.count()

    return render_template("catalog/categories.jinja",
                           categories=db_items,
                           count=db_count,
                           user=current_user)


@bp_catalog.route("/debug/fill", methods=["GET"])
def debug_fill():
    from random import randrange
    for _ in range(30):
        title = "".join([chr(randrange(1072, 1103, 1)) for _ in range(30)])
        description = "".join([chr(randrange(1072, 1103, 1)) for _ in range(100)])

        item = Item(title, description, "{}", randrange(1, 9999, 1), randrange(1, 9999, 1), randrange(1, 4))
        db.session.add(item)
        db.session.commit()
    return "OK!"


@bp_catalog.route("/debug/auth", methods=["GET"])
def debug_auth():
    user = User("test", "test", "test")
    db.session.add(user)
    db.session.commit()

    login_user(user)
    return "OK!"
