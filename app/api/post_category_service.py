from flask import request, jsonify

from ..models import PostCategory, db
from ..helpers.res_helpers import not_found_res


def post_category_by_id(id):
    """
    Functional route for CRUD post category by his id.
    """

    if request.method == 'GET':
        post_category = db.session.query(PostCategory).filter_by(id=id).first()

        if post_category is None:
            return not_found_res()
        else:
            return jsonify(post_category.to_dict())


def post_categories():
    """
    Functional route for CRUD post categories.
    """

    if request.method == 'GET':
        limit = request.args.get('limit')

        if limit is not None:
            post_categories = db.session.query(PostCategory).limit(int(limit))
        else:
            post_categories = db.session.query(PostCategory).all()

        post_categories_dict = [post_category.to_dict() for post_category in post_categories]

        return jsonify(post_categories_dict)
