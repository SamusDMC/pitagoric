from flask import request, jsonify, Response

from ..models import *
from ..decorators import auth
from ..helpers.res_helpers import not_found_res

hide_props_user = ['password']


def user_by_id(id):
    """
    Functional route for get a user by his id.
    """

    if request.method == 'GET':
        user = db.session.query(User).filter_by(id=id).first()

        if user is None:
            return not_found_res()
        else:
            return jsonify(user.to_dict(hide_props_user))


@auth.login_required_ajax
def current_user(current_user):
    """
    Functional route for the current user.
    """

    if request.method == 'GET':
        return jsonify(current_user.to_dict(hide_props_user))
