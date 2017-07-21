from flask import request, jsonify
from ..models import User, db


def user_get_all():
    if request.method == 'GET':
        users = db.session.query(User).all()

        return jsonify([user.to_json() for user in users])


def user_get_by_id(id):
    if request.method == 'GET':
        user = db.session.query(User).filter_by(id=id).first()

        return jsonify(user.to_json())
