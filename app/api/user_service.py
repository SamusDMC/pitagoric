from flask import request, jsonify
from ..models import User, db
from ..decorators import auth_required

hide_props_user = ['password']
response_dict = {}


@auth_required
def users(user_session):
    if request.method == 'GET':
        users = db.session.query(User).all()
        response_dict['user_session'] = user_session.to_dict(hide_props_user)
        response_dict['data'] = [user.to_dict(hide_props_user) for user in users]

        return jsonify(response_dict)


@auth_required
def user_by_id(id, user_session):
    if request.method == 'GET':
        user = db.session.query(User).filter_by(id=id).first()
        response_dict['user_session'] = user_session.to_dict(hide_props_user)
        response_dict['data'] = user.to_dict(hide_props_user)

        return jsonify(response_dict)


@auth_required
def user_session(user_session):
    return jsonify(user_session.to_dict(hide_props_user))
