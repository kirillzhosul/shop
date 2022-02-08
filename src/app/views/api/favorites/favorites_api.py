#!usr/bin/python
"""
    Merchandise shop application favorites API views.
"""

from flask import Blueprint, request, jsonify
from flask_login import current_user

from ....models.favorite_item import FavoriteItem
from ....models.item import Item

from .... import db


bp_api_favorites = Blueprint("api_favorites", __name__)


@bp_api_favorites.route("/api/favorites/add", methods=["GET"])
def api_favorites_add():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Авторизуйтесь для выполнения запроса!",
            "authentication_required": True
        }), 401
    item_id = request.args.get("item_id", type=int, default=0)
    item = Item.query.filter_by(id=item_id).first()
    if item_id == 0 or not item:
        return jsonify({
            "error": "Товар с индексом item_id не найден в каталоге!"
        }), 404
    favorite_item = FavoriteItem(item_id, current_user.id)

    db.session.add(favorite_item)
    db.session.commit()

    return jsonify({
        "favorite_item_id": favorite_item.id
    }), 200


@bp_api_favorites.route("/api/favorites/get", methods=["GET"])
def api_favorites_get():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Авторизуйтесь для выполнения запроса!",
            "authentication_required": True
        }), 401
    favorite_items = [
        {
            "favorite_item_id": favorite_item.id,
            "item_id": favorite_item.item_id,
        } for favorite_item in current_user.favorite_items
    ]
    favorite_count = len(current_user.favorite_items)

    return jsonify({
        "favorite_items": favorite_items,
        "total_count": favorite_count
    }), 200


@bp_api_favorites.route("/api/favorites/remove", methods=["GET"])
def api_favorites_remove():
    if not current_user.is_authenticated:
        return jsonify({
            "error": "Авторизуйтесь для выполнения запроса!",
            "authentication_required": True
        }), 401
    favorite_item_id = request.args.get("favorite_item_id", type=int, default=0)
    favorite_item = FavoriteItem.query.filter_by(id=favorite_item_id).first()
    if not favorite_item:
        return jsonify({
            "error": "Товар с индексом favorite_item_id не найден в избранных"
        }), 404
    if favorite_item.owner_id != current_user.id:
        return jsonify({
            "error": "Товар который вы пытаетесь удалить, находиться не в вашем списке избранных!"
        }), 403

    db.session.delete(favorite_item)
    db.session.commit()

    return jsonify({
    }), 200
