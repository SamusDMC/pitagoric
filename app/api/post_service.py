from flask import request, jsonify

from ..models import Post, PostComment, PostCategory, User, db
from ..helpers.res_helpers import not_found_res


def post_by_id(id):
    """
    Functional route for CRUD post by his id.
    """

    if request.method == 'GET':
        post = db.session.query(Post).filter_by(id=id).first()
        post_dict = post.to_dict()
        post_dict['comments'] = []
        comments = db.session.query(PostComment).filter_by(post_id=id).all()

        for comment in comments:
            post_dict['comments'].append(comment.to_dict())

        if post is None:
            return not_found_res()
        else:
            return jsonify(post_dict)


def posts():
    """
    Functional route for CRUD posts.
    """

    if request.method == 'GET':
        category_name = request.args.get('category')
        username = request.args.get('user')

        if category_name is not None:
            # Get posts by category.
            posts = db.session.query(Post).join(PostCategory).filter(PostCategory.name == category_name).all()
        elif username is not None:
            # Get posts by username.
            posts = db.session.query(Post).join(User).filter(User.username == username).all()
        else:
            # Recente posts.
            posts = db.session.query(Post).order_by(Post.date).limit(10)

    posts_dict = [post.to_dict() for post in posts]

    return jsonify(posts_dict)
