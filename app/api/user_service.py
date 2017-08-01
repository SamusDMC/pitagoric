from flask import request, jsonify

from ..models import User, db
from ..decorators import auth

hide_props_user = ['password']


def user_by_id(id):
    """
    Functional route for get a user by his id.
    """

    if request.method == 'GET':
        user = db.session.query(User).filter_by(id=id).first()

        return jsonify(user.to_dict(hide_props_user))


@auth.login_required_ajax
def current_user(current_user):
    """
    Functional route for the current user.
    """

    if request.method == 'GET':
        return jsonify(current_user.to_dict(hide_props_user))
