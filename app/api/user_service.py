from flask import request, jsonify
from ..models import User, db

hide_props_user = ['password']


def users():
    if request.method == 'GET':
        users = db.session.query(User).all()

        return jsonify([user.to_dict(hide_props_user) for user in users])


def user_by_id(id):
    if request.method == 'GET':
        user = db.session.query(User).filter_by(id=id).first()

        return jsonify(user.to_dict(hide_props_user))
